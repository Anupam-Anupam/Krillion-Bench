from pathlib import Path
import asyncio
from copy import deepcopy
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from archive_aggregate import game_dates
from archive_campaign import (execution_revision, load_checkpoint, plan, report_path,
                              retryable_startup_failure, run_pending, verify_archive_page,
                              GCS_STORAGE_SOURCE_CHANGES)
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


def test_gcs_migration_accepts_only_exact_adapter_and_dependency_addition(tmp_path):
    original = plan(*inputs(tmp_path), tmp_path, 10)
    for filename, (before, _) in GCS_STORAGE_SOURCE_CHANGES.items():
        if before is not None:
            original['source_sha256'][filename] = before
    current = deepcopy(original)
    for filename, (_, after) in GCS_STORAGE_SOURCE_CHANGES.items():
        current['source_sha256'][filename] = after
    with pytest.raises(ValueError, match='Only scheduler'):
        execution_revision(original, current, 'Storage cutover')
    revision = execution_revision(original, current, 'Storage cutover', allow_gcs_storage=True)
    assert revision['storage_amendment'] == 'gcs_private_reports_v1'
    assert revision['preserve_prior_results'] is True
    current['source_sha256']['runner.py'] = 'changed gameplay'
    with pytest.raises(ValueError, match='Only scheduler'):
        execution_revision(original, current, 'Storage cutover', allow_gcs_storage=True)
    current['source_sha256']['runner.py'] = original['source_sha256']['runner.py']
    current['source_sha256']['uv.lock'] = 'unreviewed dependencies'
    with pytest.raises(ValueError, match='exact audited'):
        execution_revision(original, current, 'Storage cutover', allow_gcs_storage=True)


def test_pinned_gcs_sources_match_reviewed_files():
    import hashlib
    root = Path(__file__).resolve().parents[1]
    for filename, (_, expected) in GCS_STORAGE_SOURCE_CHANGES.items():
        path = root / ('harness/' + filename if filename.endswith('.py') else filename)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == expected


@pytest.mark.parametrize('concurrency', [2, 10])
async def test_rolling_pool_refills_before_slowest_run_finishes(tmp_path, concurrency):
    initial_full, replacement_started, release = asyncio.Event(), asyncio.Event(), asyncio.Event()
    completed, active, peak = [], set(), 0
    async def one(n):
        nonlocal peak
        active.add(n)
        peak = max(peak, len(active))
        if len(active) == concurrency:
            initial_full.set()
        try:
            if n == 1:
                # One fast game finishes only after every initial slot is occupied.
                await initial_full.wait()
            else:
                if n == concurrency:
                    replacement_started.set()
                await release.wait()
            completed.append(n)
        finally:
            active.remove(n)
    task = asyncio.create_task(run_pending([(n,) for n in range(concurrency + 1)],
                                          concurrency, one, asyncio.Event(), tmp_path/'stop'))
    try:
        await asyncio.wait_for(replacement_started.wait(), 1)
        assert completed == [1]
        assert len(active) == concurrency
        assert 0 in active  # Slow initial game is still running when replacement starts.
    finally:
        release.set()
        await task
    assert peak == concurrency
    assert sorted(completed) == list(range(concurrency + 1))


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


def test_only_explicit_exact_five_word_prompt_amendment_preserves_existing_panel(tmp_path):
    from archive_campaign import FIVE_WORD_PLAYER_HASHES
    current = plan(*inputs(tmp_path), tmp_path, 8)
    current['source_sha256']['player.py'] = FIVE_WORD_PLAYER_HASHES[1]
    original = deepcopy(current)
    original['source_sha256']['player.py'] = FIVE_WORD_PLAYER_HASHES[0]
    del original['settings']['answer_word_limit_instruction']
    with pytest.raises(ValueError, match='gameplay settings'):
        execution_revision(original, current, 'User asked for a word limit')
    revision = execution_revision(original, current, 'User explicitly requested no reruns', allow_five_word_prompt=True)
    assert revision['policy_amendment'] == 'five_word_system_prompt_v1'
    assert revision['preserve_prior_results'] is True
    assert revision['answer_word_limit_instruction'] == 5
    changed = deepcopy(current)
    changed['source_sha256']['player.py'] = 'some other gameplay change'
    with pytest.raises(ValueError, match='exact approved'):
        execution_revision(original, changed, 'reason', allow_five_word_prompt=True)
    changed = deepcopy(current)
    changed['settings']['margin'] = 0
    with pytest.raises(ValueError, match='gameplay settings'):
        execution_revision(original, changed, 'reason', allow_five_word_prompt=True)
    changed = deepcopy(current)
    changed['source_sha256']['runner.py'] = 'different execution rules'
    with pytest.raises(ValueError, match='Only scheduler'):
        execution_revision(original, changed, 'reason', allow_five_word_prompt=True)


def test_five_word_amendment_matches_the_actual_player_source():
    import hashlib
    from archive_campaign import FIVE_WORD_PLAYER_HASHES
    from player import SYSTEM
    assert hashlib.sha256((Path(__file__).resolve().parents[1]/'harness'/'player.py').read_bytes()).hexdigest() == FIVE_WORD_PLAYER_HASHES[1]
    assert "Each answer you enter in the 'Your answer' textbox MUST contain at most 5 words." in SYSTEM
