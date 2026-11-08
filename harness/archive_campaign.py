"""Resume a fixed archived-game panel using only private remote checkpoints."""
import argparse
import base64
import asyncio
from datetime import datetime, timezone
import hashlib
import json
import os
import re
import signal
import time
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import urlsplit

import httpx
from playwright.async_api import TimeoutError as BrowserTimeout

from archive_aggregate import export_archive, game_dates
from campaign import source_hashes
from private_storage import MemoryRecorder, PrivateGitHubStore, github_token
from runner import READ_STATE, execute_report, load_config
from reporting import PERCENTILE
from player import AUTOCORRECTION_POLICY


def plan(roster, games, catalog, root, concurrency, campaign_id='archive-75-20261106-v3'):
    if not re.fullmatch(r'archive-75-20261106(?:-[a-z0-9]+)*', campaign_id):
        raise ValueError('Invalid archive campaign identifier')
    dates = game_dates()
    if len(roster['runs']) != 100 or len({r['model'] for r in roster['runs']}) != 100:
        raise ValueError('Use the existing 100-model leaderboard roster')
    if [g['date'] for g in games] != dates:
        raise ValueError('Archive manifest must cover November 6 through August 24, 2026, in descending order')
    for g in games:
        url = urlsplit(g['url'])
        if url.scheme != 'https' or url.netloc != 'krillion.io' or url.path == '/' or 'unlock' in url.path:
            raise ValueError('Use observed, non-authenticated Krillion archive URLs')
        if not g.get('visible_label'):
            raise ValueError('Every game needs its exact observed visible archive/date label')
    if len({g['url'] for g in games}) != 75 or len({g['visible_label'] for g in games}) != 75:
        raise ValueError('Each archived game must have a unique URL and visible label')
    meta = {m['id']: m for m in catalog['data']}
    absent = [r['model'] for r in roster['runs'] if r['model'] not in meta]
    if absent:
        raise ValueError('Roster models unavailable in current OpenRouter catalog: ' + ', '.join(absent))
    hashes = source_hashes(root)
    for filename in ('private_storage.py', 'archive_campaign.py', 'archive_aggregate.py'):
        hashes[filename] = hashlib.sha256((root / filename).read_bytes()).hexdigest()
    return dict(version=2, campaign=campaign_id, dates=dates, games=games,
                models=[dict(id=r['model'], name=r.get('name', r['model']), rank=i+1,
                             pricing=meta[r['model']].get('pricing', {})) for i, r in enumerate(roster['runs'])],
                source_sha256=hashes, concurrency=concurrency,
                settings=dict(answer_word_limit_instruction=5, autocorrection_policy=AUTOCORRECTION_POLICY, max_output_tokens=None, model_retries=2, navigation_timeout=60,
                              navigation_recovery='bounded', round_timeout_policy='continue',
                              terminal_failure_policy='collect_actual_scorecard', reasoning='low',
                              margin=3, vision=False))


def report_path(manifest, model, day):
    model_id = hashlib.sha256(model.encode()).hexdigest()[:24]
    return f"{manifest['campaign']}/runs/{day}/{model_id}.json.gz"


FIVE_WORD_PLAYER_HASHES = (
    "698d0856af689161831a304f3d5dd3177185c6f1f82e115b163fcd297328a2b1",
    "568e9c0053f24330a13975667d28f51349a933eec4f54f76237d7b08fb99f952",
)

# Audited storage-only dependency addition: existing dependency versions stay fixed.
# The adapter is pinned separately so this switch cannot admit arbitrary new code.
GCS_STORAGE_SOURCE_CHANGES = {
    'uv.lock': ('83aea2ba8223fab2f874ae9e739f89b08352e020889ec55823c9c4640e395547',
                '027ee0d5be64ea49068bb72de46d5dd8de94df2dd9abdcc8c195096b8ff2fc34'),
    'gcs_storage.py': (None, 'dd3e4cce00db8657b36c4d554a7478437840d3f662ec9ba96eead6591e021153'),
}


def execution_revision(original, current, reason, *, allow_five_word_prompt=False,
                       allow_gcs_storage=False):
    """Allow orchestration changes or the user's exact, audited prompt amendment."""
    stable = lambda m: {k: v for k, v in m.items() if k not in ('concurrency', 'source_sha256')}
    comparable = stable(current)
    amendment = None
    if allow_five_word_prompt:
        if (original['settings'].get('answer_word_limit_instruction') is not None
                or current['settings'].get('answer_word_limit_instruction') != 5
                or (original['source_sha256'].get('player.py'), current['source_sha256'].get('player.py')) != FIVE_WORD_PLAYER_HASHES):
            raise ValueError('Five-word amendment must match the exact approved prompt-only source change')
        comparable = {**comparable, 'settings': dict(comparable['settings'])}
        del comparable['settings']['answer_word_limit_instruction']
        amendment = 'five_word_system_prompt_v1'
    if stable(original) != comparable:
        raise ValueError('Campaign gameplay settings, dates, roster or prices changed')
    changed = {name for name in original['source_sha256'].keys() | current['source_sha256'].keys()
               if original['source_sha256'].get(name) != current['source_sha256'].get(name)}
    allowed = {'archive_campaign.py', 'player.py'} if amendment else {'archive_campaign.py'}
    if allow_gcs_storage:
        for filename, hashes in GCS_STORAGE_SOURCE_CHANGES.items():
            if (original['source_sha256'].get(filename), current['source_sha256'].get(filename)) != hashes:
                raise ValueError('GCS migration must match the exact audited storage-only source change')
        allowed |= GCS_STORAGE_SOURCE_CHANGES.keys()
    if changed - allowed:
        raise ValueError('Only scheduler source may change within an existing campaign')
    if not reason or not reason.strip():
        raise ValueError('Scheduler revision requires an explicit audit reason')
    revision = dict(reason=reason.strip(), original_concurrency=original['concurrency'],
                concurrency=current['concurrency'], source_sha256=current['source_sha256'],
                original_source_sha256=original['source_sha256'])
    if amendment:
        revision.update(policy_amendment=amendment, answer_word_limit_instruction=5,
                        preserve_prior_results=True)
    if allow_gcs_storage:
        revision.update(storage_amendment='gcs_private_reports_v1', preserve_prior_results=True)
    return revision


def retryable_startup_failure(saved):
    """Only a proven pre-game archive failure can be retried automatically."""
    report, events = saved['report'], saved.get('events', [])
    failures = report.get('agent_failures', [])
    forbidden = {'archive_prepared', 'browser_ready', 'model_input', 'model_call',
                 'model_output', 'model_usage', 'round_open', 'action', 'submission'}
    return (not report.get('scorecard_verified') and report.get('rounds') == []
            and report.get('metrics', {}).get('model_calls') == 0
            and report.get('metrics', {}).get('usage_calls') == 0
            and not any(e['event'] in forbidden for e in events)
            and any(e['event'] == 'cloud_session' for e in events)
            and len(failures) == 1 and failures[0].get('error_type') == 'TimeoutError'
            and any(f.get('function') == 'verify_archive_page'
                    for f in failures[0].get('frames', [])))


async def load_checkpoint(store, known_paths, manifest, model, day):
    """Preserve every attempt; a verified score is terminal, including zero."""
    original = report_path(manifest, model, day)
    retry_root = original.replace('/runs/', '/startup-retries/').removesuffix('.json.gz')
    paths = [original] + [f'{retry_root}/attempt-{n}.json.gz' for n in range(1, 4)]
    for i, path in enumerate(paths):
        if path not in known_paths:
            if any(p in known_paths for p in paths[i+1:]):
                raise ValueError('Checkpoint attempt history has a gap')
            return None, path, paths[i-1] if i else None
        saved = await store.read(path)
        if not saved or saved.get('model') != model or saved.get('game_date') != day:
            raise ValueError('Checkpoint identity mismatch')
        if saved['report'].get('scorecard_verified'):
            if any(p in known_paths for p in paths[i+1:]):
                raise ValueError('A verified score must not have subsequent attempts')
            return saved, path, None
        if not retryable_startup_failure(saved):
            raise ValueError('An unverified saved run needs diagnosis before resuming')
    raise ValueError('Archive startup retry limit reached; manual diagnosis required')


async def verify_archive_page(page, game, record=None, recovery_timeout=240):
    # Evidence supplied from actual calendar navigation, never inferred from a URL pattern.
    if page.url != game['url']:
        raise RuntimeError('Archive URL changed; refusing to benchmark a different puzzle')
    begin = page.get_by_role('button', name='▼ BEGIN DESCENT ▼', exact=True)
    replay = page.get_by_role('button', name='PLAY THIS ONE AGAIN ↻', exact=True)
    started, recovering, clicks = time.monotonic(), False, 0
    # A saved profile can contain a half-finished game after a coordinator crash.
    # Finish only that old game, without answers, then use its official replay.
    async with asyncio.timeout(recovery_timeout):
        while True:
            if page.url != game['url']:
                raise RuntimeError('Archive URL changed during preparation')
            if await begin.is_visible() or await replay.is_visible():
                break
            state = await page.evaluate(READ_STATE)
            if (re.fullmatch(r'PROMPT [1-7] OF 7', state['round_label'])
                    or (str(state['score']).isdigit()
                        and any(b in state['buttons'] for b in ('DESCEND ▼', 'SURFACE ▲')))):
                if not recovering and record:
                    record.event('archive_reset_started', game_date=game['date'])
                recovering = True
            if recovering and not state['answering']:
                targets = [b for b in state['buttons'] if b in ('DESCEND ▼', 'SURFACE ▲')]
                if len(targets) == 1:
                    clicks += 1
                    if clicks > 14:
                        raise RuntimeError('Archive recovery navigation stalled')
                    await page.get_by_role('button', name=targets[0], exact=True).press('Enter')
                    if record:
                        record.event('archive_reset_navigation', target=targets[0])
            if not recovering and time.monotonic() - started > 20:
                raise TimeoutError('Archive did not expose a recognized game state')
            await asyncio.sleep(0.25)
    replayed = await replay.is_visible()
    if replayed:
        # Use the game's own replay control; retain login and purchase entitlement.
        await replay.press('Enter')
    await begin.wait_for(timeout=20000)
    # Krillion uppercases labels with CSS; inner_text and locator text can differ in case.
    label = re.compile(r'^' + re.escape(game['visible_label']) + r'$', re.IGNORECASE)
    await page.get_by_text(label).wait_for(timeout=20000)
    if page.url != game['url']:
        raise RuntimeError('Archive URL changed; refusing to benchmark a different puzzle')
    state = await page.evaluate(READ_STATE)
    if state['score'] != '0' or state['answering'] or state['results'] or not await begin.is_enabled():
        raise RuntimeError('Archive did not reset to a clean initial game')
    if recovering and record:
        record.event('archive_reset_finished', game_date=game['date'],
                     duration_s=round(time.monotonic() - started, 4))
    return replayed


async def capture_archive_percentile(page, record, timeout=10000):
    try:
        await page.wait_for_function(
            "pattern => new RegExp(pattern, 'i').test(document.body.innerText)",
            arg=PERCENTILE.pattern, timeout=timeout)
    except BrowserTimeout:
        record.event('archive_percentile_unavailable')


async def run_pending(pending, concurrency, one, stop, stop_file):
    # Refill after durable upload; keep only a bounded number of reports in memory.
    work, failures = iter(pending), []
    async def worker():
        while not stop.is_set() and not stop_file.exists():
            item = next(work, None)
            if item is None:
                return
            try:
                await one(*item)
            except Exception as exc:
                failures.append(exc)
                stop.set()
    await asyncio.gather(*(worker() for _ in range(min(concurrency, len(pending)))))
    if failures:
        raise failures[0]


class CampaignProgress:
    """Aggregate counters only; never serialize models, prompts, or trajectories."""
    public_repo = "Anupam-Anupam/Krillion-Bench"
    branch = "campaign-status"

    def __init__(self, campaign_id, completed, workers, output, store, publish=False):
        self.campaign_id, self.completed, self.workers = campaign_id, completed, workers
        self.output, self.store, self.publish = output, store, publish
        self.active, self.status = 0, "running"

    def snapshot(self):
        return dict(campaign=self.campaign_id, verified=self.completed, total=7500,
                    active=self.active, workers=self.workers, status=self.status,
                    updated_at=datetime.now(timezone.utc).isoformat())

    def render(self):
        filled = int(30 * self.completed / 7500)
        bar = "#" * filled + "-" * (30 - filled)
        return f"[{bar}] {self.completed:,} / 7,500 ({self.completed/75:.2f}%) | {self.active}/{self.workers} active | {self.status}"

    async def emit(self):
        snapshot = self.snapshot()
        # The sole local live output is an aggregate snapshot, not a run report.
        self.output.parent.mkdir(parents=True, exist_ok=True)
        temp = self.output.with_suffix('.tmp')
        temp.write_text(json.dumps(snapshot, indent=2) + '\n')
        temp.replace(self.output)
        print(self.render(), flush=True)
        if not self.publish:
            return
        try:
            async with asyncio.timeout(20):
                endpoint = f'/repos/{self.public_repo}/contents/campaign-progress.json'
                response = await self.store.client.get(endpoint, params={'ref': self.branch})
                if response.status_code not in (200, 404):
                    raise RuntimeError('Progress checkpoint lookup failed')
                body = dict(message='Update aggregate benchmark progress', branch=self.branch,
                            content=base64.b64encode(json.dumps(snapshot).encode()).decode(),
                            author=dict(name='Anupam Chettimada',
                                        email='92892810+Anupam-Anupam@users.noreply.github.com'))
                if response.status_code == 200:
                    body['sha'] = response.json()['sha']
                response = await self.store.client.put(endpoint, json=body)
                if response.status_code not in (200, 201):
                    raise RuntimeError('Progress checkpoint update failed')
        except Exception as exc:
            # A public status outage must not cancel an in-flight private game.
            # The UI ages out stale status; retry on the next minute, not in a loop.
            print(json.dumps(dict(event='progress_publish_failed', error_type=type(exc).__name__)), flush=True)

    async def watch(self, stop, stop_file):
        while True:
            if stop.is_set() or stop_file.exists():
                self.status = 'draining'
            await self.emit()
            await asyncio.sleep(60)


async def campaign(args):
    for env in args.env_file:
        load_config(env)
    profile_id = os.environ.get('KRILLION_PROFILE_ID')
    if not profile_id:
        raise ValueError('Set KRILLION_PROFILE_ID to the restored Browser Use cloud profile')
    if not os.environ.get('BROWSER_USE_API_KEY') or not os.environ.get('OPENAI_API_KEY'):
        raise ValueError('Browser Use and OpenRouter credentials are required')
    if os.environ.get('OPENAI_BASE_URL') != 'https://openrouter.ai/api/v1':
        raise ValueError('This campaign requires the explicit OpenRouter API endpoint')
    roster = json.loads(args.roster.read_text())
    use_gcs = getattr(args, 'storage', 'github') == 'gcs'
    if use_gcs and not all(getattr(args, k, None) for k in
                           ('gcs_bucket', 'gcs_project', 'gcs_project_number', 'gcs_credentials')):
        raise ValueError('GCS requires explicit bucket, project, project number and credential file')
    store = PrivateGitHubStore(args.repo, github_token())
    if use_gcs:
        from gcs_storage import PrivateGCSStore, ReadThroughStore, ReportLayout
        try:
            destination = PrivateGCSStore(args.gcs_bucket, args.gcs_project, args.gcs_project_number,
                                         ReportLayout(r['model'] for r in roster['runs']),
                                         credentials_file=args.gcs_credentials)
            store = ReadThroughStore(destination, store)
        except BaseException:
            await store.close()
            raise
    try:
        await store.verify()
        root = Path(__file__).parent
        games = json.loads(args.games.read_text())
        campaign_id = getattr(args, 'campaign_id', 'archive-75-20261106-v3')
        if not re.fullmatch(r'archive-75-20261106(?:-[a-z0-9]+)*', campaign_id):
            raise ValueError('Invalid archive campaign identifier')
        manifest_path = campaign_id + '/manifest.json.gz'
        existing = await store.read(manifest_path)
        if existing:
            # Freeze original prices, sources, roster, dates, and controls on resume.
            catalog = {'data': existing['models']}
        else:
            async with httpx.AsyncClient(timeout=30) as client:
                response = await client.get('https://openrouter.ai/api/v1/models')
                response.raise_for_status()
                catalog = response.json()
        manifest = plan(roster, games, catalog, root, args.concurrency, campaign_id)
        if use_gcs:
            manifest['source_sha256']['gcs_storage.py'] = hashlib.sha256((root / 'gcs_storage.py').read_bytes()).hexdigest()
        execution_id = hashlib.sha256(json.dumps(manifest, sort_keys=True).encode()).hexdigest()
        if existing is not None and existing != manifest:
            revision_path = campaign_id + '/execution-revisions/' + execution_id + '.json.gz'
            prior_revision = await store.read(revision_path)
            reason = (prior_revision or {}).get('reason') or getattr(args, 'execution_revision_reason', None)
            revision = execution_revision(existing, manifest, reason,
                allow_five_word_prompt=(getattr(args, 'accept_five_word_prompt', False)
                    or (prior_revision or {}).get('policy_amendment') == 'five_word_system_prompt_v1'),
                allow_gcs_storage=(use_gcs and (getattr(args, 'accept_gcs_migration', False)
                    or (prior_revision or {}).get('storage_amendment') == 'gcs_private_reports_v1')))
            if prior_revision is not None and prior_revision != revision:
                raise ValueError('Execution revision differs from its immutable checkpoint')
            if prior_revision is None:
                await store.put(revision_path, revision)
        if existing is None:
            await store.put(manifest_path, manifest)
        if use_gcs:
            await store.prepare_campaign(existing or manifest)
        pending = []
        completed = []
        known_paths = await store.paths()
        for game in games:
            for model in manifest['models']:
                saved, path, retry_of = await load_checkpoint(
                    store, known_paths, manifest, model['id'], game['date'])
                if saved is None:
                    pending.append((game, model, path, retry_of))
                else:
                    # Keep only aggregate fields in campaign memory after reading the report.
                    completed.append(public_inputs(saved))
        fingerprints = {}
        for saved in completed:
            day, fingerprint = saved['game_date'], saved.get('prompt_fingerprint')
            if not fingerprint or (day in fingerprints and fingerprints[day] != fingerprint):
                raise ValueError('Saved archived prompt evidence does not match the fixed panel')
            fingerprints[day] = fingerprint
        print(json.dumps(dict(verified=len(completed), pending=len(pending), planned=7500)), flush=True)
        if args.limit:
            pending = pending[:args.limit]
        stop = asyncio.Event()
        stop_file = getattr(args, 'stop_file', Path('.campaign-stop'))
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGTERM, signal.SIGINT):
            loop.add_signal_handler(sig, stop.set)
        semaphore = asyncio.Semaphore(args.concurrency)
        async def one(game, model, path, retry_of):
            async with semaphore:
                if stop.is_set():
                    return
                record = MemoryRecorder(hashlib.sha256(path.encode()).hexdigest()[:24])
                original_event = record.event
                def event(kind, **data):
                    original_event(kind, **data)
                    if kind == 'cloud_session':
                        print(json.dumps(dict(event=kind, model=model['id'],
                                              session_id=data['session_id'])), flush=True)
                    elif kind == 'inference_interruption':
                        print(json.dumps(dict(event=kind, model=model['id'],
                                              round=data.get('round'), reason=data.get('reason'))), flush=True)
                record.event = event
                async def prepare(page):
                    replayed = await verify_archive_page(page, game, record)
                    record.event('archive_prepared', game_date=game['date'], replayed=replayed)
                async def finalize(page):
                    await capture_archive_percentile(page, record)
                run_args = SimpleNamespace(command='play', browser='cloud', provider='openai',
                    model=model['id'], url=game['url'], profile_id=profile_id, prepare_page=prepare,
                    finalize_page=finalize,
                    margin=3, max_steps=50, run_timeout=600, max_output_tokens=None,
                    model_retries=2, navigation_timeout=60, reasoning='low',
                    navigation_recovery='bounded', vision=False, answers_file=None)
                report = await execute_report(run_args, record, pricing=model['pricing'])
                prompt_fingerprint = hashlib.sha256(json.dumps(
                    [r['prompt'] for r in report['rounds']], ensure_ascii=False).encode()).hexdigest()
                saved = dict(model=model['id'], game_date=game['date'], execution_id=execution_id,
                             retry_of=retry_of, answer_word_limit_instruction=5,
                             captured_at=datetime.now(timezone.utc).isoformat(), report=report,
                             prompt_fingerprint=prompt_fingerprint, events=record.events)
                # No new game starts in this slot until its report is remotely acknowledged.
                try:
                    await store.put(path, saved)
                except Exception:
                    stop.set()
                    raise
                if not report.get('scorecard_verified'):
                    stop.set()
                    raise RuntimeError('Unverified archived scorecard saved privately; scheduling paused')
                expected = fingerprints.setdefault(game['date'], prompt_fingerprint)
                if expected != prompt_fingerprint:
                    stop.set()
                    raise RuntimeError('Different prompts observed for the same archive date; scheduling paused')
                completed.append(public_inputs(saved))
                progress.completed = len(completed)
                print(progress.render(), flush=True)
                print(json.dumps(dict(model=model['id'], game_date=game['date'],
                                      verified=len(completed), planned=7500)), flush=True)
        progress = CampaignProgress(campaign_id, len(completed), args.concurrency,
                                    getattr(args, 'progress_output', Path('artifacts/campaign-progress.json')),
                                    store, getattr(args, 'publish_progress', False))
        async def tracked_one(*item):
            progress.active += 1
            try:
                await one(*item)
            finally:
                progress.active -= 1
        progress_task = asyncio.create_task(progress.watch(stop, stop_file))
        try:
            await run_pending(pending, args.concurrency, tracked_one, stop, stop_file)
            progress.status = 'complete' if len(completed) == 7500 else 'paused'
        except BaseException:
            progress.status = 'needs_attention'
            raise
        finally:
            progress_task.cancel()
            await asyncio.gather(progress_task, return_exceptions=True)
            await progress.emit()
            for sig in (signal.SIGTERM, signal.SIGINT):
                loop.remove_signal_handler(sig)
        if stop.is_set() or stop_file.exists():
            print(json.dumps(dict(status='drained', verified=len(completed), planned=7500)), flush=True)
        if len(completed) == 7500:
            result = export_archive(manifest, completed)
            if existing and 'answer_word_limit_instruction' not in existing['settings']:
                result['protocol_note'] = ("At the user's request, a five-word answer instruction was added "
                                           'during this campaign; earlier verified results were retained without reruns.')
            # This is the only local output: numeric aggregates, never trajectories.
            args.public_output.write_text(json.dumps(result, indent=2, allow_nan=False) + '\n')
            print('All 7,500 games verified; aggregate-only leaderboard export ready.', flush=True)
    finally:
        await store.close()


def public_inputs(saved):
    r = saved['report']
    return dict(model=saved['model'], game_date=saved['game_date'],
                prompt_fingerprint=saved.get('prompt_fingerprint'), report={
        'scorecard_verified': r['scorecard_verified'], 'final_score': r.get('final_score'),
        'daily_percentile': r.get('daily_percentile'), 'metrics': r['metrics'],
        'rounds': [{'round_outcome': x.get('round_outcome')} for x in r['rounds']],
        'recoveries': [{} for _ in r.get('recoveries', [])]})


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', default='Anupam-Anupam/Krillion-Bench-Private-Runs')
    parser.add_argument('--storage', choices=('github', 'gcs'), default='github')
    parser.add_argument('--gcs-bucket')
    parser.add_argument('--gcs-project')
    parser.add_argument('--gcs-project-number')
    parser.add_argument('--gcs-credentials', type=Path)
    parser.add_argument('--accept-gcs-migration', action='store_true', help='Apply the exact audited storage-only migration; preserve historical checkpoints')
    parser.add_argument('--games', type=Path, required=True, help='Observed archive URL/date/label manifest')
    parser.add_argument('--roster', type=Path, default=Path(__file__).resolve().parents[1] / 'web/data/leaderboard-data.json')
    parser.add_argument('--env-file', type=Path, action='append', default=[])
    parser.add_argument('--concurrency', type=int, default=2)
    parser.add_argument('--campaign-id', default='archive-75-20261106-v3')
    parser.add_argument('--execution-revision-reason')
    parser.add_argument('--accept-five-word-prompt', action='store_true', help='Apply the explicitly authorized prompt-only amendment while preserving earlier scores')
    parser.add_argument('--publish-progress', action='store_true', help='Publish aggregate counters to the personal public status branch')
    parser.add_argument('--progress-output', type=Path, default=Path('artifacts/campaign-progress.json'))
    parser.add_argument('--stop-file', type=Path, default=Path('.campaign-stop'))
    parser.add_argument('--limit', type=int, help='Pilot: only this many pending games')
    parser.add_argument('--public-output', type=Path, default=Path('archive-leaderboard.json'))
    args = parser.parse_args()
    if not 1 <= args.concurrency <= 20 or (args.limit is not None and args.limit < 1):
        parser.error('Concurrency must be 1–20; pilot limit must be positive')
    try:
        asyncio.run(campaign(args))
    except Exception as exc:
        # Never print remote response bodies, authenticated URLs, or credentials.
        print(json.dumps(dict(status='stopped', error_type=type(exc).__name__)), flush=True)
        raise SystemExit(1)
