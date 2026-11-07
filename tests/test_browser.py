"""Real Chromium integration tests using a deterministic local seven-round game."""
import os

import pytest
from playwright.async_api import async_playwright

from player import Action, execute, verified_completion
from runner import Observer, Recorder, scripted_baseline

HTML = '''<!doctype html><html><body><main id="game"></main><script>
let round = 0, score = 0;
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
 root.innerHTML=`<div>PLANKTON</div><div>“answer ${round}”</div><div>+10 PTS</div><div>SCORE</div><div>${score}</div>`+
 (round<7?'<button onclick="next()">DESCEND ▼</button>':'<button onclick="finish()">SURFACE ▲</button>');
}
function finish() {
 root.innerHTML='<div>DIVE COMPLETE</div><div>SCORE</div><div>70</div><button style="text-transform:uppercase">Copy result</button>';
 for(let i=1;i<=7;i++) root.innerHTML+=`<div title="Round ${i}: answer ${i}, 10 pts">${i}</div>`;
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
