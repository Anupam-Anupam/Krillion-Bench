"""Resume a fixed archived-game panel using only private remote checkpoints."""
import argparse
import asyncio
from datetime import datetime, timezone
import hashlib
import json
import os
import re
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


def plan(roster, games, catalog, root, concurrency, campaign_id='archive-75-20261106-v2'):
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
                settings=dict(max_output_tokens=None, model_retries=2, navigation_timeout=60,
                              navigation_recovery='bounded', round_timeout_policy='continue',
                              terminal_failure_policy='collect_actual_scorecard', reasoning='low',
                              margin=3, vision=False))


def report_path(manifest, model, day):
    model_id = hashlib.sha256(model.encode()).hexdigest()[:24]
    return f"{manifest['campaign']}/runs/{day}/{model_id}.json.gz"


async def verify_archive_page(page, game):
    # Evidence supplied from actual calendar navigation, never inferred from a URL pattern.
    if page.url != game['url']:
        raise RuntimeError('Archive URL changed; refusing to benchmark a different puzzle')
    begin = page.get_by_role('button', name='▼ BEGIN DESCENT ▼', exact=True)
    replay = page.get_by_role('button', name='PLAY THIS ONE AGAIN ↻', exact=True)
    await begin.or_(replay).wait_for(timeout=20000)
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
    return replayed


async def capture_archive_percentile(page, record, timeout=10000):
    try:
        await page.wait_for_function(
            "pattern => new RegExp(pattern, 'i').test(document.body.innerText)",
            arg=PERCENTILE.pattern, timeout=timeout)
    except BrowserTimeout:
        record.event('archive_percentile_unavailable')


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
    store = PrivateGitHubStore(args.repo, github_token())
    try:
        await store.verify()
        root = Path(__file__).parent
        roster = json.loads(args.roster.read_text())
        games = json.loads(args.games.read_text())
        campaign_id = getattr(args, 'campaign_id', 'archive-75-20261106-v2')
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
        if existing is not None and existing != manifest:
            raise ValueError('Campaign manifest differs; do not mix harness versions or rosters')
        if existing is None:
            await store.put(manifest_path, manifest)
        pending = []
        completed = []
        known_paths = await store.paths()
        for game in games:
            for model in manifest['models']:
                path = report_path(manifest, model['id'], game['date'])
                saved = await store.read(path) if path in known_paths else None
                if saved is None:
                    pending.append((game, model, path))
                elif saved.get('model') != model['id'] or saved.get('game_date') != game['date']:
                    raise ValueError('Checkpoint identity mismatch')
                elif not saved['report'].get('scorecard_verified'):
                    raise ValueError('An unverified saved run needs diagnosis before resuming')
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
        semaphore = asyncio.Semaphore(args.concurrency)
        async def one(game, model, path):
            async with semaphore:
                if stop.is_set():
                    return
                record = MemoryRecorder(hashlib.sha256(path.encode()).hexdigest()[:24])
                async def prepare(page):
                    replayed = await verify_archive_page(page, game)
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
                saved = dict(model=model['id'], game_date=game['date'],
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
                print(json.dumps(dict(model=model['id'], game_date=game['date'],
                                      verified=len(completed), planned=7500)), flush=True)
        # Bounded task creation also bounds in-memory pending reports.
        for offset in range(0, len(pending), args.concurrency):
            outcomes = await asyncio.gather(*(one(*p) for p in pending[offset:offset+args.concurrency]),
                                            return_exceptions=True)
            failure = next((x for x in outcomes if isinstance(x, BaseException)), None)
            if failure:
                raise failure
        if len(completed) == 7500:
            result = export_archive(manifest, completed)
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
    parser.add_argument('--games', type=Path, required=True, help='Observed archive URL/date/label manifest')
    parser.add_argument('--roster', type=Path, default=Path('leaderboard-data.json'))
    parser.add_argument('--env-file', type=Path, action='append', default=[])
    parser.add_argument('--concurrency', type=int, default=4)
    parser.add_argument('--campaign-id', default='archive-75-20261106-v2')
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
