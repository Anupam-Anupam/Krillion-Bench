"""Real Chromium integration tests using a deterministic local seven-round game."""
import os

import pytest
from playwright.async_api import async_playwright

from player import Action, execute, verified_completion
from runner import Observer, Recorder, scripted_baseline

HTML = '''<!doctype html><html><body><main id="game"></main><script>
let round = 0, score = 0, results = [];
const root = document.getElementById('game');
function showStart() { root.innerHTML='<button onclick="next()">▼ BEGIN DESCENT ▼</button>'; }
function next() {
 round++;
 root.innerHTML=`<div class="prompt">Question ${round}</div><div class="ds-prompt-count">PROMPT ${round} OF 7</div>
 <div>SCORE</div><div>${score}</div><div class="ds-time-digits">25</div>
 <form onsubmit="submitAnswer(event)"><input aria-label="Your answer"><button>DIVE</button></form><p id="feedback"></p>`;
}
function submitAnswer(e) {
 e.preventDefault();
 if (document.querySelector('input').value !== 'answer '+round) {
  document.getElementById('feedback').textContent='"'+document.querySelector('input').value+'": no echo. try again'; return;
 }
 score+=10;
 results.push(`Round ${round}: answer ${round}, 10 pts`);
 root.innerHTML=`<div>PLANKTON</div><div>“answer ${round}”</div><div>+10 PTS</div><div>SCORE</div><div>${score}</div>`+
 (round<7?'<button onclick="next()">DESCEND ▼</button>':'<button onclick="finish()">SURFACE ▲</button>');
}
function finish() {
 root.innerHTML=`<div>DIVE COMPLETE</div><div>SCORE</div><div>${score}</div><div>BETTER THAN 42% OF TODAY’S PLAYERS</div><button style="text-transform:uppercase">Copy result</button>`;
 for(let i=0;i<results.length;i++) root.innerHTML+=`<div title="${results[i]}">${i+1}</div>`;
}
function expire() {
 results.push(`Round ${round}: —, 0 pts`);
 root.innerHTML=`<div>NOTHING LANDED</div><div>—</div><div>+0 PTS</div><div>the clock beat you to it.</div><div>SCORE</div><div>${score}</div>`+
 (round<7?'<button onclick="next()">DESCEND ▼</button>':'<button onclick="finish()">SURFACE ▲</button>');
}
showStart();
</script></body></html>'''


@pytest.fixture
async def page():
    executable = os.environ.get('KRILLION_TEST_CHROME')
    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path=executable)
        context = await browser.new_context()
        page = await context.new_page()
        await page.set_content(HTML)
        yield page
        await browser.close()


async def test_scripted_seven_rounds_reach_verified_scoreboard(page, tmp_path):
    obs = Observer(page, Recorder(tmp_path/'run'))
    answers = {f'Question {n}': f'answer {n}' for n in range(1,8)}
    assert await scripted_baseline(page, obs, answers) == 'baseline_finished'
    assert verified_completion(obs)
    assert obs.last_state.score == '70'
    assert len(obs.last_state.results) == 7


async def test_archive_replay_clears_saved_results_before_model_observation(page):
    from archive_campaign import verify_archive_page
    await page.set_content('''<div id="game"><div>SCORE</div><div>545</div>
      <div title="Round 1: old answer, 85 pts">Saved result</div>
      <button onclick="document.getElementById('game').innerHTML = document.getElementById('fresh').innerHTML">PLAY THIS ONE AGAIN ↻</button></div>
      <template id="fresh"><div style="text-transform:uppercase">resurfaced day #114</div>
      <div>SCORE</div><div>0</div><button>▼ BEGIN DESCENT ▼</button></template>''')
    game = dict(url=page.url, visible_label='RESURFACED DAY #114')
    assert await verify_archive_page(page, game) is True
    assert await page.locator('[title^="Round "]').count() == 0
    assert await verify_archive_page(page, game) is False
    await page.get_by_role('button', name='▼ BEGIN DESCENT ▼').evaluate(
        "el => el.insertAdjacentHTML('beforebegin', '<input aria-label=\"Your answer\">')")
    with pytest.raises(RuntimeError, match='clean initial'):
        await verify_archive_page(page, game)


async def test_archive_waits_for_delayed_percentile_but_preserves_missing(page):
    from archive_campaign import capture_archive_percentile
    from private_storage import MemoryRecorder
    record = MemoryRecorder('synthetic-archive')
    await page.set_content('''<div>DIVE COMPLETE</div><script>
      setTimeout(() => document.body.insertAdjacentHTML('beforeend',
      "<div>BETTER THAN 99% OF DAY #114'S ORIGINAL PLAYERS</div>"), 100);
      </script>''')
    await capture_archive_percentile(page, record, timeout=2000)
    assert record.events == []
    await page.set_content('<div>DIVE COMPLETE</div>')
    await capture_archive_percentile(page, record, timeout=50)
    assert record.events[-1]['event'] == 'archive_percentile_unavailable'


async def test_rejection_can_recover_within_same_round(page, tmp_path):
    obs = Observer(page, Recorder(tmp_path/'run'))
    before = await obs.read()
    await execute(Action(kind='click',target='▼ BEGIN DESCENT ▼'),before,obs)
    before = await obs.read()
    await execute(Action(kind='fill',target='Your answer',text='wrong'),before,obs)
    await execute(Action(kind='click',target='DIVE'),before,obs)
    rejected = await obs.read()
    deadline = obs.deadline.expires
    assert rejected.answering
    assert 'no echo. try again' in rejected.text
    await execute(Action(kind='fill',target='Your answer',text='answer 1'),rejected,obs)
    assert obs.deadline.expires <= deadline
    await execute(Action(kind='click',target='DIVE'),rejected,obs)
    accepted = await obs.read()
    assert not accepted.answering
    assert obs.rounds[before.key]['points'] == 10
    assert len(obs.rounds[before.key]['submissions']) == 2
    assert obs.rounds[before.key]['submissions'][0]['outcome'] == 'rejected'
    from reporting import enrich_report
    report = enrich_report(dict(status='partial', rounds=list(obs.rounds.values())))
    attempts = report['rounds'][0]['submissions']
    assert [(s['outcome'], s['rarity']) for s in attempts] == [('rejected', None), ('accepted', 'Plankton')]


async def test_disabled_input_during_submission_does_not_reset_deadline(page, tmp_path):
    obs = Observer(page, Recorder(tmp_path/'run'))
    await page.get_by_role('button', name='▼ BEGIN DESCENT ▼').press('Enter')
    await obs.read()
    deadline = obs.deadline.expires
    await page.get_by_role('textbox').evaluate('(el) => el.disabled = true')
    pending = await obs.read()
    assert pending.answering
    assert obs.deadline.expires <= deadline
    await page.get_by_role('textbox').evaluate('(el) => el.disabled = false')
    await obs.read()
    assert obs.deadline.expires <= deadline


async def test_real_browser_recovers_scout_between_rounds_without_answering(page, tmp_path):
    from types import SimpleNamespace
    from unittest.mock import AsyncMock, Mock
    from player import Turn, play_actions
    obs = Observer(page, Recorder(tmp_path/'run'))
    await page.get_by_role('button', name='▼ BEGIN DESCENT ▼').press('Enter')
    for n in (1, 2):
        state = await obs.read()
        await execute(Action(kind='fill', target='Your answer', text=f'answer {n}'), state, obs)
        await execute(Action(kind='click', target='DIVE'), state, obs)
        state = await obs.read()
        if n == 1:
            await execute(Action(kind='click', target='DESCEND ▼'), state, obs)
    model = Mock(ainvoke=AsyncMock(return_value=SimpleNamespace(
        completion=Turn(actions=[Action(kind='fill', target='Your answer', text='midnight zone')]), usage=None)))
    await play_actions(obs, model, max_steps=3)
    state = await obs.read()
    assert state.prompt == 'Question 3'
    assert state.answering and state.answer == ''
    assert obs.rounds[state.key].get('submissions', []) == []
    assert len(obs.rounds) == 3


class FixturePlayer:
    async def ainvoke(self, messages, output_format):
        import json
        from types import SimpleNamespace
        from player import Turn
        state = json.loads(messages[-1].content[0].text)['page']
        if state['answering']:
            n = state['round_label'].split()[1]
            actions = [Action(kind='fill', target='Your answer', text=f'answer {n}'), Action(kind='click', target='DIVE')]
        else:
            actions = [Action(kind='click', target=state['buttons'][0])]
        return SimpleNamespace(completion=Turn(actions=actions), usage=None)


async def test_inference_deadline_misses_round_then_finishes_real_scorecard(page, tmp_path):
    import asyncio
    import time
    from player import play_actions
    from reporting import write_report, read_events
    obs = Observer(page, Recorder(tmp_path/'run'))
    await page.get_by_role('button', name='▼ BEGIN DESCENT ▼').press('Enter')
    await obs.read()
    obs.deadline.expires = time.monotonic() + 0.1
    await page.evaluate('setTimeout(expire, 250)')
    cancelled = False

    class SlowFirst(FixturePlayer):
        async def ainvoke(self, messages, output_format):
            nonlocal cancelled
            if not cancelled:
                try:
                    await asyncio.sleep(10)
                except asyncio.CancelledError:
                    cancelled = True
                    raise
            return await super().ainvoke(messages, output_format)

    watch = asyncio.create_task(obs.watch())
    try:
        assert await play_actions(obs, SlowFirst()) == 'agent_finished'
        assert not watch.done()
    finally:
        watch.cancel()
        await asyncio.gather(watch, return_exceptions=True)
    report = write_report(dict(status='agent_finished', rounds=list(obs.rounds.values()),
                         final_score=obs.last_state.score, scoreboard=obs.last_state.results),
                         obs.record.output, obs.last_state.text, read_events(obs.record.output))
    assert cancelled and report['scorecard_verified']
    assert report['final_score'] == '60' and report['daily_percentile'] == 42
    assert report['rounds'][0]['round_outcome'] == 'missed'
    assert report['rounds'][0]['points'] == 0
    assert report['rounds'][0]['submissions'] == []
    assert len(report['rounds']) == 7


async def test_uncertain_submit_timeout_observes_acceptance_and_continues(page, tmp_path, monkeypatch):
    import asyncio
    import time
    from player import play_actions
    from reporting import enrich_report
    obs = Observer(page, Recorder(tmp_path/'run'))
    await page.get_by_role('button', name='▼ BEGIN DESCENT ▼').press('Enter')
    await obs.read()
    obs.deadline.expires = time.monotonic() + 0.3
    original = page.get_by_role
    delayed = False

    def get_role(*args, **kwargs):
        nonlocal delayed
        locator = original(*args, **kwargs)
        if kwargs.get('name') == 'DIVE' and not delayed:
            delayed = True

            class SlowAcknowledgement:
                async def press(self, *args, **kwargs):
                    await locator.press(*args, **kwargs)
                    await asyncio.sleep(10)

            return SlowAcknowledgement()
        return locator

    monkeypatch.setattr(page, 'get_by_role', get_role)
    assert await play_actions(obs, FixturePlayer()) == 'agent_finished'
    assert verified_completion(obs) and obs.last_state.score == '70'
    report = enrich_report(dict(status='agent_finished', rounds=list(obs.rounds.values()),
                           final_score='70', scoreboard=obs.last_state.results))
    first = report['rounds'][0]
    assert first['interruptions'] == ['action_timeout']
    assert len(first['submissions']) == 1 and first['submissions'][0]['outcome'] == 'accepted'


async def test_terminal_api_failure_collects_actual_score_without_answer_fallback(page, tmp_path, monkeypatch):
    import json
    from types import SimpleNamespace
    from browser_use.llm.exceptions import ModelProviderError
    import runner
    from reporting import write_report, read_events
    obs = Observer(page, Recorder(tmp_path/'run'))
    await page.evaluate('''() => {
      const originalNext = next;
      next = () => { originalNext(); const n=round;
        setTimeout(() => { if(round===n && document.querySelector('input')) expire(); }, 150); };
    }''')
    async def broken_agent(session, observer, args):
        state = await observer.read()
        await execute(Action(kind='click', target='▼ BEGIN DESCENT ▼'), state, observer)
        state = await observer.read()
        await execute(Action(kind='fill', target='Your answer', text='answer 1'), state, observer)
        await execute(Action(kind='click', target='DIVE'), state, observer)
        await observer.read()
        raise ModelProviderError('Model unavailable', 404)
    monkeypatch.setattr(runner, 'play', broken_agent)
    status, error = await runner.run_game(None, obs, SimpleNamespace(command='play', run_timeout=10))
    report = write_report(dict(status=status, error_type=error, rounds=list(obs.rounds.values()),
                              final_score=obs.last_state.score, scoreboard=obs.last_state.results),
                          obs.record.output, obs.last_state.text, read_events(obs.record.output))
    assert status == 'scored_with_errors' and report['scorecard_verified']
    assert report['final_score'] == '10' and report['daily_percentile'] == 42
    assert sum(len(r['submissions']) for r in report['rounds']) == 1
    assert sum(r['round_outcome'] == 'missed' for r in report['rounds']) == 6
    assert report['agent_failures'][0]['category'] == 'invalid_request'
    assert report['scorecard_collection'][-1]['phase'] == 'verified'
    events = read_events(obs.record.output)
    start = next(i for i,e in enumerate(events) if e['event'] == 'scorecard_collection')
    assert all(e.get('action',{}).get('target') != 'Your answer' and
               e.get('action',{}).get('target') != 'DIVE' for e in events[start:])


async def test_all_seven_game_timeouts_are_ranked_as_a_verified_zero(page, tmp_path):
    from player import play_actions
    from reporting import write_report, read_events
    from leaderboard import export_campaign
    from campaign import summarize
    obs = Observer(page, Recorder(tmp_path/'run'))
    await page.evaluate('''() => {
      const originalNext = next;
      next = () => { originalNext(); document.querySelector('.ds-time-digits').textContent='1';
        setTimeout(expire, 100); };
    }''')
    assert await play_actions(obs, FixturePlayer()) == 'agent_finished'
    report = write_report(dict(status='agent_finished', rounds=list(obs.rounds.values()),
                              final_score=obs.last_state.score, scoreboard=obs.last_state.results),
                          obs.record.output, obs.last_state.text, read_events(obs.record.output))
    row = summarize({'model':'test/model','rank':1}, report, read_events(obs.record.output))
    public = export_campaign({'runs':[row], 'updated_at':'fixture'},
                             {'models':[{'id':'test/model'}], 'settings':{}, 'utc_date':'fixture'},
                             {'test/model':report})['runs'][0]
    assert public['complete'] and public['score'] == 0 and public['daily_percentile'] == 42
    assert public['missed_rounds'] == 7
    assert all(not r['submissions'] for r in public['rounds'])


async def test_score_collection_cannot_turn_broken_browser_into_a_score(tmp_path):
    from unittest.mock import AsyncMock, Mock
    from player import collect_final_score
    obs = Mock(record=Recorder(tmp_path/'run'), read=AsyncMock(side_effect=TimeoutError('disconnected')))
    with pytest.raises(TimeoutError):
        await collect_final_score(obs, 'browser_failure', timeout=1)
    assert obs.read.await_count == 3
    assert '"phase": "verified"' not in (obs.record.output/'events.jsonl').read_text()


async def test_optional_screenshot_failure_is_recorded_without_aborting_game(tmp_path):
    from unittest.mock import AsyncMock, Mock
    from runner import capture_screenshot
    from reporting import read_events
    record = Recorder(tmp_path/'run')
    page = Mock(screenshot=AsyncMock(side_effect=TimeoutError('font animation timeout')))
    await capture_screenshot(page, record, 'initial.png')
    assert read_events(record.output)[0]['event'] == 'artifact_error'
