import asyncio
import json
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import httpx
import pytest
from browser_use.llm.exceptions import ModelProviderError, ModelRateLimitError
from browser_use.llm.messages import SystemMessage
from openai import APIStatusError

from model_policy import ModelResponseTimeout, RequestPolicy, error_details
from player import Action, Turn, SYSTEM
from runner import make_model
from runner import Recorder, TimedModel


def api_error(status, body, retry=None):
    response = httpx.Response(status, request=httpx.Request('POST', 'https://example.test'),
                              headers={'retry-after': str(retry)} if retry is not None else {}, json=body)
    cause = APIStatusError('API failure', response=response, body=body)
    error = ModelRateLimitError('Rate limited') if status == 429 else ModelProviderError('Provider failed', status)
    error.__cause__ = cause
    return error


def test_diagnostics_preserve_status_metadata_and_redact_secrets(monkeypatch):
    monkeypatch.setenv('OPENAI_API_KEY', 'secret-user-key-for-test')
    error = api_error(429, {'error': {'message': 'secret-user-key-for-test https://endpoint/?token=private bu_private123',
                                     'metadata': {'provider_name': 'Example', 'limit_source': 'upstream_provider_shared_pool',
                                                  'raw': 'do not log raw bodies', 'error_type': 'rate_limit_exceeded'}}}, retry=60)
    details = error_details(error)
    assert details['http_status'] == 429 and details['retry_after_s'] == 60
    assert details['provider_name'] == 'Example' and details['retryable']
    assert details['limit_source'] == 'upstream_provider_shared_pool'
    assert 'private' not in json.dumps(details) and 'secret-user' not in json.dumps(details)
    assert 'raw' not in details


async def test_rate_limit_retries_same_model_and_preserves_diagnostics():
    error = api_error(429, {'error': {'message': 'busy'}}, retry=0.01)
    model = Mock(ainvoke=AsyncMock(side_effect=[error, 'response']))
    record = Mock()
    policy = RequestPolicy(2)
    assert await policy.invoke(model, [], Turn, record, 1, 'round 1') == 'response'
    assert model.ainvoke.await_count == 2
    assert any(c.args[0] == 'model_retry' for c in record.event.call_args_list)


async def test_retry_after_cannot_extend_round_budget_or_reissue_early():
    error = api_error(429, {'error': {'message': 'busy'}}, retry=30)
    model = Mock(ainvoke=AsyncMock(side_effect=error))
    policy = RequestPolicy(2)
    with pytest.raises(ModelResponseTimeout):
        await policy.invoke(model, [], Turn, Mock(), 0.02, 'round 1')
    assert model.ainvoke.await_count == 1
    assert policy.retry_at > 0


async def test_nonretryable_request_failure_is_not_retried():
    error = api_error(400, {'error': {'message': 'unsupported schema'}})
    model = Mock(ainvoke=AsyncMock(side_effect=error))
    with pytest.raises(ModelProviderError):
        await RequestPolicy(2).invoke(model, [], Turn, Mock(), 1, 'round 1')
    assert model.ainvoke.await_count == 1
    assert error_details(error)['category'] == 'invalid_request'


async def test_retry_exhaustion_is_bounded():
    error = api_error(503, {'error': {'message': 'unavailable'}}, retry=0)
    model = Mock(ainvoke=AsyncMock(side_effect=error))
    with pytest.raises(ModelProviderError):
        await RequestPolicy(2).invoke(model, [], Turn, Mock(), 1, 'round 1')
    assert model.ainvoke.await_count == 3


@pytest.mark.parametrize('cap', [None, 8000])
async def test_openai_wire_omits_output_cap_unless_explicit(cap, monkeypatch):
    monkeypatch.setenv('OPENAI_API_KEY', 'fake-key')
    monkeypatch.setenv('OPENAI_BASE_URL', 'https://example.test/v1')
    seen = []

    async def handle(request):
        seen.append(json.loads(request.content))
        return httpx.Response(200, json={'id': 'test', 'object': 'chat.completion', 'created': 0, 'model': 'test',
            'choices': [{'index': 0, 'finish_reason': 'stop', 'message': {'role': 'assistant',
                'content': Turn(actions=[Action(kind='done')]).model_dump_json()}}]})

    model = make_model(SimpleNamespace(provider='openai', model='org/model', navigation_timeout=60,
                                      max_output_tokens=cap, reasoning='low'))
    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as client:
        model.http_client = client
        await model.ainvoke([SystemMessage(content='Test')], output_format=Turn)
    assert seen[0].get('max_completion_tokens') == cap
    if cap is None:
        assert 'max_completion_tokens' not in seen[0] and 'max_tokens' not in seen[0]


async def test_unsupported_native_schema_falls_back_to_validated_prompt_json(tmp_path, monkeypatch):
    monkeypatch.setenv('OPENAI_API_KEY', 'fake-key')
    monkeypatch.setenv('OPENAI_BASE_URL', 'https://example.test/v1')
    seen = []

    async def handle(request):
        seen.append(json.loads(request.content))
        if len(seen) == 1:
            return httpx.Response(400, json={'error': {'message': 'Provider returned error', 'code': 400,
                'metadata': {'provider_name': 'Example', 'raw': 'model features structured outputs not support'}}})
        return httpx.Response(200, json={'id': 'test', 'object': 'chat.completion', 'created': 0, 'model': 'test',
            'choices': [{'index': 0, 'finish_reason': 'stop', 'message': {'role': 'assistant',
                'content': Turn(actions=[Action(kind='done')]).model_dump_json()}}]})

    model = make_model(SimpleNamespace(provider='openai', model='org/model', navigation_timeout=60,
                                      max_output_tokens=None, reasoning='low'))
    record = Recorder(tmp_path/'run')
    async with httpx.AsyncClient(transport=httpx.MockTransport(handle)) as client:
        model.http_client = client
        result = await RequestPolicy().invoke(TimedModel(model, record), [SystemMessage(content=SYSTEM)],
                                              Turn, record, 1, 'SURFACE')
    assert result.completion.actions[0].kind == 'done'
    assert 'response_format' in seen[0] and 'response_format' not in seen[1]
    assert json.dumps(Turn.model_json_schema()) in seen[1]['messages'][0]['content']
    assert 'Do not wrap it in name or arguments' in seen[1]['messages'][0]['content']
    assert all('MUST contain at most 5 words' in call['messages'][0]['content'] for call in seen)
    events = [json.loads(l) for l in (record.output/'events.jsonl').read_text().splitlines()]
    assert any(e['event'] == 'model_compatibility' and e['same_model'] for e in events)
