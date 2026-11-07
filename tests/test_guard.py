from unittest.mock import AsyncMock, Mock

import pytest
from pydantic import ValidationError

from deadline import DeadlineExceeded
from player import Action, Turn, execute, verified_completion
from runner import Observer, Recorder


def observer(tmp_path, **changes):
    data = dict(prompt="Name a fruit.", round_label="PROMPT 1 OF 7", timer="25",
                answering=True, answer="", buttons=["DIVE"], text="", score="0")
    data.update(changes)
    page = Mock()
    page.evaluate = AsyncMock(return_value=data)
    page.get_by_role.return_value = AsyncMock()
    return Observer(page, Recorder(tmp_path / "run"))


async def test_late_model_response_cannot_execute_action(tmp_path):
    obs = observer(tmp_path)
    before = await obs.read()
    obs.deadline.expires = 0
    with pytest.raises(DeadlineExceeded):
        await execute(Action(kind="fill", target="Your answer", text="quince"), before, obs)
    obs.page.get_by_role.assert_not_called()


async def test_action_for_previous_question_is_rejected(tmp_path):
    obs = observer(tmp_path)
    before = await obs.read()
    obs.page.evaluate.return_value["prompt"] = "Name a country."
    result = await execute(Action(kind="fill", target="Your answer", text="quince"), before, obs)
    assert "Page changed" in result
    obs.page.get_by_role.assert_not_called()


async def test_action_cannot_leak_from_preview_into_answer_phase(tmp_path):
    obs = observer(tmp_path, answering=False, timer="")
    before = await obs.read()
    obs.page.evaluate.return_value.update(answering=True, timer="25")
    result = await execute(Action(kind="fill", target="Your answer", text="quince"), before, obs)
    assert "Page changed" in result
    obs.page.get_by_role.assert_not_called()


async def test_valid_fill_executes(tmp_path):
    obs = observer(tmp_path)
    before = await obs.read()
    result = await execute(Action(kind="fill", target="Your answer", text="quince"), before, obs)
    assert result == "ok"
    obs.page.get_by_role.return_value.fill.assert_awaited_once()


async def test_watchdog_keeps_observing_after_round_deadline(tmp_path):
    import asyncio
    import time
    obs = observer(tmp_path, timer="3")
    watch = asyncio.create_task(obs.watch())
    try:
        await asyncio.sleep(0.01)
        assert obs.deadline.remaining(time.monotonic()) <= 0
        assert not watch.done()
    finally:
        watch.cancel()
        await asyncio.gather(watch, return_exceptions=True)


async def test_unreadable_timer_fails_closed(tmp_path):
    obs = observer(tmp_path, timer="unknown")
    with pytest.raises(RuntimeError, match="cannot safely determine deadline"):
        await obs.read()


async def test_ads_and_unknown_buttons_cannot_be_activated(tmp_path):
    obs = observer(tmp_path, buttons=["DIVE", "BUY NOW"])
    before = await obs.read()
    result = await execute(Action(kind="click", target="BUY NOW"), before, obs)
    assert result != "ok"
    obs.page.get_by_role.assert_not_called()


async def test_model_cannot_claim_early_completion(tmp_path):
    obs = observer(tmp_path)
    before = await obs.read()
    obs.rounds = {str(i): {"points": 100} for i in range(7)}
    assert not verified_completion(obs)
    assert await execute(Action(kind="done"), before, obs) != "done"


def test_invalid_model_actions_rejected():
    with pytest.raises(ValidationError):
        Turn.model_validate({"actions": [{"kind": "evaluate", "text": "fetch('/answers')"}]})
    with pytest.raises(ValidationError):
        Turn(actions=[])


@pytest.mark.parametrize("score,numbers,expected", [
    ("70", list(range(1, 8)), True),
    ("71", list(range(1, 8)), False),
    ("70", [1, 2, 3, 4, 5, 6, 6], False),
    ("60", list(range(1, 7)), False),
])
async def test_scoreboard_requires_unique_rounds_and_matching_total(tmp_path, score, numbers, expected):
    obs = observer(tmp_path, answering=False, text="DIVE COMPLETE", buttons=["Copy result"],
                   score=score, results=[f"Round {n}: answer, 10 pts" for n in numbers])
    obs.rounds = {str(n): {} for n in range(7)}
    await obs.read()
    assert verified_completion(obs) is expected


async def test_model_timeout_at_round_budget_records_interruption_and_continues(tmp_path):
    from player import play_actions
    obs = observer(tmp_path)
    async def timed_out(*args, **kwargs):
        obs.deadline.expires = 0
        obs.page.evaluate.return_value.update(answering=False, timer='', buttons=['DESCEND ▼'],
            text='NOTHING LANDED\n—\n+0 PTS')
        raise TimeoutError()
    model = Mock(ainvoke=AsyncMock(side_effect=timed_out))
    assert await play_actions(obs, model, max_steps=1) == 'step_limit_exceeded'
    row = next(iter(obs.rounds.values()))
    assert row['interruptions'] == ['round_inference_deadline']
    assert row['points'] == 0
    obs.page.get_by_role.assert_not_called()


async def test_submission_is_logged_even_when_keypress_times_out(tmp_path):
    import json
    obs = observer(tmp_path, answer='quince')
    before = await obs.read()
    obs.page.get_by_role.return_value.press.side_effect = TimeoutError()
    with pytest.raises(TimeoutError):
        await execute(Action(kind='click', target='DIVE'), before, obs)
    sub = obs.rounds[before.key]['submissions'][0]
    assert sub['answer'] == 'quince' and sub['outcome'] == 'unconfirmed'
    events = [json.loads(l) for l in (obs.record.output / 'events.jsonl').read_text().splitlines()]
    event = next(e for e in events if e['event'] == 'submission')
    assert event['round_elapsed_s'] == sub['elapsed_s']
    assert events[-1]['event'] == 'action_result' and events[-1]['result'] == 'TimeoutError'


async def test_old_rejection_does_not_grade_a_repeat_submission(tmp_path):
    obs = observer(tmp_path, answer='wrong', text='"wrong": no echo. try again')
    before = await obs.read()
    await execute(Action(kind='click', target='DIVE'), before, obs)
    await obs.read()
    assert obs.rounds[before.key]['submissions'][0]['outcome'] == 'unconfirmed'
    obs.page.evaluate.return_value['input_enabled'] = False
    await obs.read()
    obs.page.evaluate.return_value['input_enabled'] = True
    await obs.read()
    assert obs.rounds[before.key]['submissions'][0]['outcome'] == 'rejected'
