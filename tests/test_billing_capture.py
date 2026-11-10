import asyncio
import json

import httpx
import pytest

from billing_capture import BillingClient
from metrics import aggregate
from private_storage import MemoryRecorder


async def test_deadline_cancellation_keeps_late_billing_without_delaying_caller():
    release = asyncio.Event()
    async def provider(request):
        await release.wait()
        return httpx.Response(200, json={'id':'gen-private', 'usage':{
            'prompt_tokens':100,'completion_tokens':20,'cost':.03}})
    record = MemoryRecorder('billing-test')
    async with BillingClient(record, transport=httpx.MockTransport(provider)) as client:
        request = asyncio.create_task(client.post('https://openrouter.ai/api/v1/chat/completions',json={}))
        await asyncio.sleep(0)
        request.cancel()
        with pytest.raises(asyncio.CancelledError):
            await request
        record.event('model_call', duration_s=1)
        assert not any(e['event']=='model_usage' for e in record.events)
        release.set()
        await client.finish_accounting()
    metrics = aggregate(record.events)
    assert metrics['run_cost_usd']==.03 and metrics['output_tokens']==20
    assert metrics['usage_complete']
    assert 'gen-private' not in json.dumps(record.events)


async def test_failed_provider_is_unresolved_not_assumed_free():
    async def provider(request):
        return httpx.Response(429,json={'error':{'message':'private'}})
    record=MemoryRecorder('billing-test')
    async with BillingClient(record,transport=httpx.MockTransport(provider)) as client:
        await client.post('https://openrouter.ai/api/v1/chat/completions',json={})
        record.event('model_call',duration_s=1)
        await client.finish_accounting()
    assert aggregate(record.events)['run_cost_usd'] is None
    assert record.events[-1]['unresolved_requests']==1
    assert 'private' not in json.dumps(record.events)


async def test_generation_lookup_recovers_missing_cost_without_duplicate_usage(monkeypatch):
    original_client=httpx.AsyncClient
    async def provider(request):
        return httpx.Response(200,json={'id':'gen-private','usage':{'prompt_tokens':10,'completion_tokens':2}})
    async def lookup(request):
        assert request.url.params['id']=='gen-private'
        return httpx.Response(200,json={'data':{'native_tokens_prompt':10,'native_tokens_completion':2,'total_cost':.004}})
    record=MemoryRecorder('billing-test')
    async with BillingClient(record,transport=httpx.MockTransport(provider)) as client:
        await client.post('https://openrouter.ai/api/v1/chat/completions',json={},headers={'Authorization':'Bearer private-key'})
        record.event('model_call',duration_s=1)
        monkeypatch.setattr(httpx,'AsyncClient',lambda **kw:original_client(transport=httpx.MockTransport(lookup),**kw))
        await client.finish_accounting()
    assert aggregate(record.events)['run_cost_usd']==.004
    assert len([e for e in record.events if e['event']=='model_usage'])==1
    assert 'private' not in json.dumps(record.events)
