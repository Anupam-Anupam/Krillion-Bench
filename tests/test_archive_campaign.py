from pathlib import Path
import asyncio
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from archive_aggregate import game_dates
from archive_campaign import (execution_revision, load_checkpoint, plan, report_path,
                              retryable_startup_failure, run_pending, verify_archive_page)
from campaign import SOURCES


def inputs(tmp_path):
    for filename in (*SOURCES, 'private_storage.py', 'archive_campaign.py', 'archive_aggregate.py'):
        (tmp_path / filename).write_text('synthetic source')
    roster = {'runs': [{'model': f'test/model-{i}'} for i in range(100)]}
    catalog = {'data': [{'id': r['model'], 'pricing': {}} for r in roster['runs']]}
    games = [{'date': d, 'url': f'https://krillion.io/test-only/{d}',
              'visible_label': 'Synthetic ' + d} for d in game_dates()]
    return roster, games, catalog


def test_plan_preserves_exact_roster_and_dates(tmp_path):
    roster, games, catalog = inputs(tmp_path)
    result = plan(roster, games, catalog, tmp_path, 4)
    assert [m['id'] for m in result['models']] == [r['model'] for r in roster['runs']]
    assert result['dates'] == game_dates()
    assert report_path(result, 'test/model-1', result['dates'][0]) != report_path(result, 'test/model-2', result['dates'][0])


def test_missing_model_does_not_silently_substitute(tmp_path):
    roster, games, catalog = inputs(tmp_path)
    catalog['data'].pop()
    with pytest.raises(ValueError, match='unavailable'):
        plan(roster, games, catalog, tmp_path, 4)


def test_wrong_date_duplicate_url_and_unlock_links_fail_closed(tmp_path):
    roster, games, catalog = inputs(tmp_path)
    games[0]['date'] = '2026-11-07'
    with pytest.raises(ValueError, match='November 6'):
        plan(roster, games, catalog, tmp_path, 4)
    games[0]['date'] = game_dates()[0]
    games[0]['url'] = games[1]['url']
    with pytest.raises(ValueError, match='unique'):
        plan(roster, games, catalog, tmp_path, 4)
    games[0]['url'] = 'https://krillion.io/unlock?session_id=private'
    with pytest.raises(ValueError, match='non-authenticated'):
        plan(roster, games, catalog, tmp_path, 4)


async def test_archive_redirect_cannot_be_mistaken_for_requested_game():
    page = Mock(url='https://krillion.io/')
    page.get_by_text.return_value.wait_for = AsyncMock()
    with pytest.raises(RuntimeError, match='URL changed'):
        await verify_archive_page(page, {'url': 'https://krillion.io/test-only/date', 'visible_label': 'Archive date'})
    page.get_by_text.assert_not_called()


def test_scheduler_revision_preserves_gameplay_and_requires_audit_reason(tmp_path):
    original = plan(*inputs(tmp_path), tmp_path, 8)
    current = deepcopy(original)
    current['concurrency'] = 10
    current['source_sha256']['archive_campaign.py'] = 'new scheduler'
    assert execution_revision(original, current, 'User requested maximum parallelism')['concurrency'] == 10
    with pytest.raises(ValueError, match='audit reason'):
        execution_revision(original, current, None)
    current['source_sha256']['player.py'] = 'different agent'
    with pytest.raises(ValueError, match='Only scheduler'):
        execution_revision(original, current, 'reason')
    current = deepcopy(original)
    current['settings']['margin'] = 1
    with pytest.raises(ValueError, match='gameplay settings'):
        execution_revision(original, current, 'reason')


async def test_rolling_pool_refills_before_slowest_run_finishes(tmp_path):
    release, third_started = asyncio.Event(), asyncio.Event()
    completed = []
    async def one(n):
        if n == 0:
            await release.wait()
        if n == 2:
            third_started.set()
        completed.append(n)
    task = asyncio.create_task(run_pending([(n,) for n in range(3)], 2, one,
                                          asyncio.Event(), tmp_path/'stop'))
    await asyncio.wait_for(third_started.wait(), 1)
    assert 0 not in completed
    release.set()
    await task
    assert sorted(completed) == [0, 1, 2]


async def test_stop_request_drains_inflight_without_starting_more(tmp_path):
    stop, second_started = asyncio.Event(), asyncio.Event()
    completed = []
    async def one(n):
        if n == 0:
            await second_started.wait()
            stop.set()
        else:
            second_started.set()
            await stop.wait()
        completed.append(n)
    await run_pending([(n,) for n in range(5)], 2, one, stop, tmp_path/'stop')
    assert sorted(completed) == [0, 1]


def startup_failure():
    return dict(model='test/model', game_date='2026-11-06', events=[{'event': 'cloud_session'}],
                report=dict(scorecard_verified=False, rounds=[],
                            metrics=dict(model_calls=0, usage_calls=0),
                            agent_failures=[dict(error_type='TimeoutError',
                                frames=[{'function': 'verify_archive_page'}])]))


async def test_startup_retry_preserves_original_and_resumes_verified_zero():
    manifest = {'campaign': 'archive-75-20261106-v2'}
    original = report_path(manifest, 'test/model', '2026-11-06')
    failed = startup_failure()
    store = Mock(read=AsyncMock(return_value=failed))
    saved, retry, previous = await load_checkpoint(store, {original}, manifest, 'test/model', '2026-11-06')
    assert saved is None and previous == original and '/startup-retries/' in retry
    assert retry.endswith('/attempt-1.json.gz')
    success = deepcopy(failed)
    success['report'].update(scorecard_verified=True, final_score='0')
    store.read = AsyncMock(side_effect=[failed, success])
    saved, path, previous = await load_checkpoint(store, {original, retry}, manifest, 'test/model', '2026-11-06')
    assert saved == success and path == retry and previous is None


@pytest.mark.parametrize('event', ['archive_prepared', 'browser_ready', 'model_input',
                                  'model_call', 'action', 'submission', 'round_open'])
def test_never_retry_an_attempt_that_reached_gameplay(event):
    failed = startup_failure()
    failed['events'].append({'event': event})
    assert not retryable_startup_failure(failed)


async def test_checkpoint_retry_limit_and_identity_fail_closed():
    manifest = {'campaign': 'archive-75-20261106-v2'}
    original = report_path(manifest, 'test/model', '2026-11-06')
    root = original.replace('/runs/', '/startup-retries/').removesuffix('.json.gz')
    paths = {original, *(f'{root}/attempt-{i}.json.gz' for i in range(1, 4))}
    store = Mock(read=AsyncMock(return_value=startup_failure()))
    with pytest.raises(ValueError, match='retry limit'):
        await load_checkpoint(store, paths, manifest, 'test/model', '2026-11-06')
    failed = startup_failure()
    failed['model'] = 'wrong/model'
    store.read = AsyncMock(return_value=failed)
    with pytest.raises(ValueError, match='identity'):
        await load_checkpoint(store, paths, manifest, 'test/model', '2026-11-06')


def test_changed_correction_policy_requires_separate_panel(tmp_path):
    current = plan(*inputs(tmp_path), tmp_path, 2)
    assert current['campaign'] == 'archive-75-20261106-v3'
    assert current['settings']['autocorrection_policy'] == 'confirm_site_suggestion_v1'
    original = deepcopy(current)
    del original['settings']['autocorrection_policy']
    with pytest.raises(ValueError, match='gameplay settings'):
        execution_revision(original, current, 'Accept corrections')


async def test_public_progress_contains_only_counts_and_preserves_private_reports(tmp_path):
    import base64
    import json
    import httpx
    from archive_campaign import CampaignProgress
    requests = []
    async def handler(request):
        requests.append(request)
        if request.method == 'GET':
            assert request.url.params['ref'] == 'campaign-status'
            return httpx.Response(200, json={'sha':'old-snapshot'})
        body = json.loads(request.content)
        assert body['branch'] == 'campaign-status' and body['sha'] == 'old-snapshot'
        public = json.loads(base64.b64decode(body['content']))
        assert set(public) == {'campaign','verified','total','active','workers','status','updated_at'}
        assert public['verified'] == 4 and public['total'] == 7500
        assert public['active'] == 8 and public['workers'] == 8
        assert body['author']['email'].endswith('Anupam-Anupam@users.noreply.github.com')
        return httpx.Response(200)
    async with httpx.AsyncClient(base_url='https://api.github.com', transport=httpx.MockTransport(handler)) as client:
        progress = CampaignProgress('archive-75-20261106-v3',4,8,tmp_path/'status.json',SimpleNamespace(client=client),True)
        progress.active = 8
        await progress.emit()
    assert len(requests) == 2
    assert all('/Anupam-Anupam/Krillion-Bench/contents/campaign-progress.json' in r.url.path for r in requests)
    assert json.loads((tmp_path/'status.json').read_text())['verified'] == 4
    assert '4 / 7,500 (0.05%)' in progress.render()


async def test_progress_publish_failure_does_not_abort_games(tmp_path,capsys):
    import httpx
    from archive_campaign import CampaignProgress
    async with httpx.AsyncClient(base_url='https://api.github.com', transport=httpx.MockTransport(lambda r:httpx.Response(429))) as client:
        progress = CampaignProgress('archive-75-20261106-v3',23,8,tmp_path/'status.json',SimpleNamespace(client=client),True)
        await progress.emit()
    assert progress.completed == 23
    assert 'progress_publish_failed' in capsys.readouterr().out
    assert (tmp_path/'status.json').exists()
