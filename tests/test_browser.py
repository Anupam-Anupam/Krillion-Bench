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
