"""Capture provider accounting after gameplay deadlines without extending gameplay.

Generation IDs and pending responses live only in memory. Public exports receive
only the existing numeric accounting allowlist.
"""
import asyncio
from urllib.parse import urlsplit

import httpx

from metrics import clean_usage, number


class BillingClient(httpx.AsyncClient):
    def __init__(self, record, **kwargs):
        self.record = record
        self.pending = set()
        self.generations = {}
        self.requests_started = 0
        self.responses_accounted = 0
        super().__init__(event_hooks={'response': [self.capture]}, **kwargs)

    async def send(self, request, **kwargs):
        # The model's caller still receives cancellation at its original deadline.
        # Only HTTP completion/accounting continues, with no actions or answers.
        self.requests_started += 1
        task = asyncio.create_task(super().send(request, **kwargs))
        self.pending.add(task)
        try:
            return await asyncio.shield(task)
        finally:
            if task.done():
                self.pending.discard(task)

    async def capture(self, response):
        if response.status_code != 200 or 'application/json' not in response.headers.get('content-type', ''):
            return
        await response.aread()
        try:
            body = response.json()
        except ValueError:
            return
        if not isinstance(body, dict):
            return
        usage = clean_usage(body.get('usage'))
        generation = body.get('id')
        is_openrouter = urlsplit(str(response.request.url)).hostname == 'openrouter.ai'
        if is_openrouter and isinstance(generation, str) and generation.startswith('gen-') and any(usage.get(k) is None for k in ('input_tokens', 'output_tokens', 'cost_usd')):
            self.generations[generation] = (response.request.headers.get('authorization'), usage)
        elif usage:
            self.record.event('model_usage', usage=usage)
            self.responses_accounted += 1

    async def finish_accounting(self, timeout=60):
        tasks = list(self.pending)
        if tasks:
            done, unfinished = await asyncio.wait(tasks, timeout=timeout)
            for task in unfinished:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)
            self.pending.clear()
        # Only known IDs from this run are queried. No account-wide discovery.
        async with httpx.AsyncClient(timeout=15) as lookup:
            for generation, (authorization, captured_usage) in self.generations.items():
                recovered_usage = dict(captured_usage)
                if not authorization:
                    continue
                for attempt in range(3):
                    try:
                        response = await lookup.get('https://openrouter.ai/api/v1/generation',
                                                    params={'id': generation},
                                                    headers={'Authorization': authorization})
                        if response.status_code == 404 and attempt < 2:
                            await asyncio.sleep(1)
                            continue
                        response.raise_for_status()
                        data = response.json()['data']
                        usage = {key: number(data.get(field)) for key, field in
                                 [('input_tokens', 'native_tokens_prompt'),
                                  ('output_tokens', 'native_tokens_completion'),
                                  ('reasoning_tokens', 'native_tokens_reasoning'),
                                  ('cached_tokens', 'native_tokens_cached'),
                                  ('cost_usd', 'total_cost')]}
                        usage = {k: v for k, v in usage.items() if v is not None}
                        recovered_usage.update(usage)
                        break
                    except (httpx.HTTPError, ValueError, KeyError, TypeError):
                        break
                if recovered_usage:
                    self.record.event('model_usage', usage=recovered_usage)
                    self.responses_accounted += 1
        self.generations.clear()
        self.record.event('billing_capture_finished', requests=self.requests_started,
                          accounted_responses=self.responses_accounted,
                          unresolved_requests=max(0, self.requests_started-self.responses_accounted))
