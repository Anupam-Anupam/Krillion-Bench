"""Diagnose API failures without recording credentials; retry the same model only."""
import asyncio
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import math
import os
import re
import time

from browser_use.llm.exceptions import ModelOutputTruncatedError


class ModelResponseTimeout(TimeoutError):
    """The harness cancelled inference at its wall-clock deadline."""


def redact(value):
    text = str(value)
    for key, secret in os.environ.items():
        if secret and len(secret) >= 8 and any(word in key for word in ('KEY', 'TOKEN', 'SECRET')):
            text = text.replace(secret, '[credential]')
    text = re.sub(r'(?:sk-[\w-]+|bu_[\w-]+|Bearer\s+\S+)', '[credential]', text, flags=re.I)
    text = re.sub(r'(?:https?|wss?)://[^\s\"\']+', '[url]', text)
    return text[:600]


def retry_after(value):
    if value is None:
        return None
    try:
        seconds = float(value)
    except (TypeError, ValueError):
        try:
            seconds = (parsedate_to_datetime(value) - datetime.now(timezone.utc)).total_seconds()
        except (TypeError, ValueError, OverflowError):
            return None
    return max(0, seconds) if math.isfinite(seconds) else None


def error_details(exc):
    chain = []
    current = exc
    while current is not None and id(current) not in {id(e) for e in chain}:
        chain.append(current)
        current = current.__cause__ or current.__context__
    response_error = next((e for e in reversed(chain) if getattr(e, 'response', None) is not None), None)
    source = response_error or exc
    response = getattr(source, 'response', None)
    body = getattr(source, 'body', None)
    if response is not None:
        try:
            body = response.json()
        except (ValueError, RuntimeError):
            pass
    body = body if isinstance(body, dict) else {}
    error = body.get('error', body)
    error = error if isinstance(error, dict) else {}
    metadata = error.get('metadata', {})
    metadata = metadata if isinstance(metadata, dict) else {}
    headers = getattr(response, 'headers', {})
    status = getattr(response, 'status_code', None)
    adapter_status = getattr(exc, 'status_code', None)
    provider_status = error.get('code')
    provider_status = provider_status if isinstance(provider_status, int) else None
    code = provider_status or status or adapter_status
    category = 'provider_error'
    names = {type(e).__name__ for e in chain}
    if isinstance(exc, ModelResponseTimeout):
        category = 'inference_deadline'
    elif isinstance(exc, ModelOutputTruncatedError):
        category = 'output_truncated'
    elif 'ValidationError' in names:
        category = 'invalid_model_output'
    elif status is None and ('Failed to parse structured output' in str(exc) or 'missing or empty `choices`' in str(exc)):
        category = 'empty_model_output'
    elif 'APITimeoutError' in names:
        category = 'transport_timeout'
    elif 'APIConnectionError' in names:
        category = 'transport_error'
    elif code == 429:
        category = 'rate_limit'
    elif code in (401, 403):
        category = 'authentication_or_permission'
    elif code == 402:
        category = 'credit_or_budget'
    elif code in (400, 404, 422):
        category = 'invalid_request'
    details = dict(error_type=type(exc).__name__, category=category, http_status=status,
                   adapter_status=adapter_status, provider_status=provider_status,
                   message=redact(error.get('message', str(exc))),
                   retry_after_s=retry_after(headers.get('retry-after')))
    for key in ('provider_name', 'provider_code', 'error_type', 'limit_source', 'reason'):
        value = metadata.get(key)
        if isinstance(value, (str, int)):
            details['provider_error_type' if key == 'error_type' else key] = redact(value)
    raw = metadata.get('raw')
    if isinstance(raw, str):
        # Keep a bounded, scrubbed explanation, never arbitrary response/header objects.
        details['provider_message'] = redact(raw)
    details['retryable'] = (category in ('transport_timeout', 'transport_error', 'rate_limit', 'empty_model_output')
                           or (category == 'provider_error' and code in (408, 409, 500, 502, 503, 504))
                           or (code == 402 and metadata.get('limit_source') == 'openrouter_in_flight_budget'))
    return details


class RequestPolicy:
    def __init__(self, retries=2):
        self.retries = retries
        self.retry_at = 0.0

    async def invoke(self, model, messages, output_format, record, timeout, round_label):
        try:
            async with asyncio.timeout(timeout):
                for attempt in range(self.retries + 1):
                    await asyncio.sleep(max(0, self.retry_at - time.monotonic()))
                    try:
                        return await model.ainvoke(messages, output_format=output_format)
                    except Exception as exc:
                        details = error_details(exc)
                        record.event('model_issue', round=round_label, attempt=attempt + 1, **details)
                        explanation = details.get('provider_message', '') + ' ' + details['message']
                        unsupported = (details['category'] == 'invalid_request' and
                                       re.search(r'(?:structured.?outputs?|response_format).*(?:not support|unsupported)', explanation, re.I))
                        malformed = details['category'] in ('invalid_model_output', 'empty_model_output')
                        fallback = getattr(model, 'enable_prompt_json', None)
                        if attempt < self.retries and (unsupported or malformed) and callable(fallback) and fallback():
                            record.event('model_compatibility', round=round_label, mode='prompt_json',
                                         reason=details['category'], same_model=True, schema_validation=True)
                            continue
                        if not details['retryable']:
                            raise
                        delay = details['retry_after_s']
                        delay = delay if delay is not None else min(2 ** attempt, 8)
                        self.retry_at = time.monotonic() + delay
                        if attempt == self.retries:
                            raise
                        record.event('model_retry', round=round_label, attempt=attempt + 2,
                                     delay_s=delay, same_model=True)
        except TimeoutError as exc:
            raise ModelResponseTimeout('Inference wall-clock budget expired') from exc
