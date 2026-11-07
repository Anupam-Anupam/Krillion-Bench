"""Allowlisted usage accounting; missing/cancelled requests never become free requests."""
import math
from datetime import datetime


def number(value):
    if isinstance(value, bool):
        return None
    try:
        value = float(value)
        return value if math.isfinite(value) and value >= 0 else None
    except (TypeError, ValueError):
        return None


def clean_usage(raw):
    if not isinstance(raw, dict):
        return {}
    prompt = raw.get('prompt_tokens_details') or {}
    completion = raw.get('completion_tokens_details') or {}
    costs = raw.get('cost_details') or {}
    fields = {'input_tokens': raw.get('prompt_tokens'), 'output_tokens': raw.get('completion_tokens'),
              'cached_tokens': prompt.get('cached_tokens', raw.get('prompt_cached_tokens')),
              'cache_write_tokens': prompt.get('cache_write_tokens', raw.get('prompt_cache_creation_tokens')),
              'reasoning_tokens': completion.get('reasoning_tokens'), 'cost_usd': raw.get('cost'),
              'output_cost_usd': costs.get('upstream_inference_completions_cost')}
    return {key: number(value) for key, value in fields.items()}


def pricing_for(catalog, model):
    rows = catalog.get('data', catalog.get('models', []))
    return next((r.get('pricing', {}) for r in rows if r.get('id') == model), {})


def estimate(usage, pricing):
    inp, out = usage.get('input_tokens'), usage.get('output_tokens')
    # Apply context-length tiers per request, never to the whole run's token sum.
    pricing = dict(pricing)
    for tier in sorted(pricing.get('overrides', []), key=lambda t: number(t.get('min_prompt_tokens')) or 0):
        threshold = number(tier.get('min_prompt_tokens'))
        if inp is not None and threshold is not None and inp >= threshold:
            pricing.update(tier)
    ip, op = number(pricing.get('prompt')), number(pricing.get('completion'))
    output = out * op if out is not None and op is not None else None
    cached = usage.get('cached_tokens') or 0
    written = usage.get('cache_write_tokens') or 0
    if inp is None or ip is None or output is None or cached + written > inp:
        return None, output
    cache_price = number(pricing.get('input_cache_read')) if cached else 0
    write_price = number(pricing.get('input_cache_write')) if written else 0
    # No assumed cache discount when the frozen catalog lacks the needed rate.
    if cache_price is None or write_price is None:
        return None, output
    request_price = number(pricing.get('request', 0))
    if request_price is None:
        return None, output
    return ((inp - cached - written) * ip + cached * cache_price + written * write_price
            + output + request_price), output


def aggregate(events, pricing=None, started_at=None, ended_at=None):
    pricing = pricing or {}
    calls = [e for e in events if e['event'] == 'model_call']
    raw_events = [e for e in events if e['event'] == 'model_usage']
    # New wire capture includes malformed/truncated responses; legacy model_output does not.
    usages = ([e['usage'] for e in raw_events] if raw_events else
              [clean_usage(e['usage']) for e in events if e['event'] == 'model_output' and e.get('usage')])
    total_calls = len(calls)
    complete = total_calls > 0 and len(usages) == total_calls
    def summed(key):
        values = [u.get(key) for u in usages]
        return sum(values) if values and all(v is not None for v in values) else None
    costs, output_costs = [], []
    cost_sources, output_sources = set(), set()
    for usage in usages:
        estimated, estimated_output = estimate(usage, pricing)
        cost, output = usage.get('cost_usd'), usage.get('output_cost_usd')
        costs.append(cost if cost is not None else estimated)
        output_costs.append(output if output is not None else estimated_output)
        cost_sources.add('reported' if cost is not None else 'estimated')
        output_sources.add('provider_reported' if output is not None else 'estimated')
    def money(values, sources):
        available = [v for v in values if v is not None]
        if not available:
            return None, 'unavailable'
        basis = next(iter(sources)) if len(sources) == 1 else 'mixed'
        if not complete or len(available) != len(values):
            basis = 'partial_' + basis
        return sum(available), basis
    cost, cost_basis = money(costs, cost_sources)
    output_cost, output_basis = money(output_costs, output_sources)
    elapsed = None
    if started_at and ended_at:
        elapsed = max(0, (datetime.fromisoformat(ended_at) - datetime.fromisoformat(started_at)).total_seconds())
    elif events:
        elapsed = max((e.get('elapsed_s', 0) for e in events), default=0)
    return dict(run_cost_usd=cost, cost_basis=cost_basis, output_cost_usd=output_cost,
                output_cost_basis=output_basis, input_tokens=summed('input_tokens'),
                output_tokens=summed('output_tokens'), reasoning_tokens=summed('reasoning_tokens'),
                usage_complete=complete, usage_calls=len(usages), model_calls=total_calls,
                run_duration_s=elapsed, inference_duration_s=sum(e['duration_s'] for e in calls),
                pricing=pricing)


def usage_hook(record):
    async def capture(response):
        # Nonstreaming response only. The adapter will consume the same buffered body.
        if response.status_code != 200 or 'application/json' not in response.headers.get('content-type', ''):
            return
        await response.aread()
        try:
            body = response.json()
            usage = body.get('usage')
            if isinstance(usage, dict):
                record.event('model_usage', usage=clean_usage(usage))
        except (ValueError, AttributeError, TypeError):
            return
    return capture
