import base64
from contextlib import asynccontextmanager
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import httpx
import pytest

from private_storage import MemoryRecorder, PrivateGitHubStore, blob_sha
from runner import capture_screenshot, execute_report


async def test_memory_run_never_writes_reports_or_screenshots(monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError('Private trajectory attempted filesystem access')
    monkeypatch.setattr(Path, 'mkdir', forbidden)
    monkeypatch.setattr(Path, 'write_text', forbidden)
    monkeypatch.setattr(Path, 'write_bytes', forbidden)
    record = MemoryRecorder('test-run')
    page = Mock(screenshot=AsyncMock())
    await capture_screenshot(page, record, 'not-written.png')
    page.screenshot.assert_not_called()

    @asynccontextmanager
    async def fake_browser(args, recording):
        yield None, page
    monkeypatch.setattr('runner.browser_session', fake_browser)
    args = SimpleNamespace(browser='cloud', model='test/model', provider='openai', vision=False,
                           margin=3, command='smoke', max_output_tokens=None, model_retries=2,
                           navigation_timeout=60, reasoning='low', navigation_recovery='bounded')
    report = await execute_report(args, record, pricing={})
    assert report['status'] == 'smoke_passed'
    assert record.events[-1]['event'] == 'run_finished'
    assert not hasattr(record, 'output')


async def test_private_upload_is_idempotent_and_never_overwrites():
    files = {}
    async def handler(request):
        if '/contents/' not in request.url.path:
            return httpx.Response(200, json=dict(private=True,
                full_name='Anupam-Anupam/Private', permissions={'push': True}))
        path = request.url.path
        if request.method == 'GET':
            return httpx.Response(200, json=files[path]) if path in files else httpx.Response(404)
        import json
        body = json.loads(request.content)
        assert 'sha' not in body  # No overwrite/update operation.
        if path in files:
            return httpx.Response(422)
        content = base64.b64decode(body['content'])
        files[path] = dict(encoding='base64', content=body['content'], sha=blob_sha(content))
        return httpx.Response(201, json={'content': {'sha': blob_sha(content)}})
    async with httpx.AsyncClient(base_url='https://api.github.com', transport=httpx.MockTransport(handler)) as client:
        store = PrivateGitHubStore('Anupam-Anupam/Private', 'test', client=client, write_interval=0)
        report = {'report': {'answer': 'private answer'}}
        first = await store.put('campaign/run.json.gz', report)
        assert await store.put('campaign/run.json.gz', report) == first
        assert await store.read('campaign/run.json.gz') == report
        with pytest.raises(RuntimeError, match='different data'):
            await store.put('campaign/run.json.gz', {'different': True})


async def test_store_refuses_public_repo_before_upload():
    async def handler(request):
        assert request.method == 'GET'
        return httpx.Response(200, json=dict(private=False, full_name='Anupam-Anupam/Private',
                                            permissions={'push': True}))
    async with httpx.AsyncClient(base_url='https://api.github.com', transport=httpx.MockTransport(handler)) as client:
        store = PrivateGitHubStore('Anupam-Anupam/Private', 'test', client=client)
        with pytest.raises(RuntimeError, match='private personal'):
            await store.put('report.json.gz', {'secret': 'answer'})


def test_store_rejects_other_owners():
    with pytest.raises(ValueError, match='personal owner'):
        PrivateGitHubStore('shop/anything', 'test')
