from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock

import pytest

from player import Action, NavigationRecovery, Turn, observation, play_actions
from test_guard import observer


@pytest.mark.parametrize('kind', ['fill', 'wait'])
async def test_scout_stall_recovers_after_two_model_turns(tmp_path, kind):
    obs = observer(tmp_path, answering=False, timer='', buttons=['DESCEND ▼'],
                   text='THE MIDNIGHT ZONE\nPLANKTON\n“Rick and Morty”\n+10 PTS')
    action = Action(kind=kind, target='Your answer', text='midnight zone')
    model = Mock(ainvoke=AsyncMock(return_value=SimpleNamespace(completion=Turn(actions=[action]), usage=None)))
    assert await play_actions(obs, model, max_steps=3) == 'step_limit_exceeded'
    assert model.ainvoke.await_count == 2
    obs.page.get_by_role.assert_called_once_with('button', name='DESCEND ▼', exact=True)
    obs.page.get_by_role.return_value.press.assert_awaited_once()
    events = (obs.record.output / 'events.jsonl').read_text()
    assert 'navigation_recovery' in events
    assert 'action_result' in events


async def test_strict_mode_does_not_recover(tmp_path):
    obs = observer(tmp_path, answering=False, timer='', buttons=['DESCEND ▼'])
    model = Mock(ainvoke=AsyncMock(return_value=SimpleNamespace(
        completion=Turn(actions=[Action(kind='fill', target='Your answer', text='midnight zone')]), usage=None)))
    await play_actions(obs, model, max_steps=4, navigation_recovery='off')
    assert model.ainvoke.await_count == 4
    obs.page.get_by_role.assert_not_called()


async def test_recovery_is_bounded_even_when_navigation_does_nothing(tmp_path):
    obs = observer(tmp_path, answering=False, timer='', buttons=['DESCEND ▼'])
    recovery = NavigationRecovery('bounded')
    state = await obs.read()
    for _ in range(10):
        await recovery.before_turn(state, obs)
    obs.page.get_by_role.return_value.press.assert_awaited_once()


async def test_recovery_never_submits_or_extends_an_active_round(tmp_path):
    obs = observer(tmp_path)
    state = await obs.read()
    expires = obs.deadline.expires
    recovery = NavigationRecovery('bounded')
    for _ in range(4):
        assert not await recovery.before_turn(state, obs)
    assert obs.deadline.expires == expires
    obs.page.get_by_role.assert_not_called()


async def test_recovery_reobserves_and_rejects_a_stale_phase(tmp_path):
    obs = observer(tmp_path, answering=False, timer='', buttons=['DESCEND ▼'])
    state = await obs.read()
    recovery = NavigationRecovery('bounded')
    await recovery.before_turn(state, obs)
    await recovery.before_turn(state, obs)
    obs.page.evaluate.return_value.update(answering=True, timer='25', buttons=['DIVE'])
    await recovery.before_turn(state, obs)
    obs.page.get_by_role.assert_not_called()


async def test_phase_guidance_does_not_treat_scenery_as_question(tmp_path):
    obs = observer(tmp_path, answering=False, timer='', buttons=['DESCEND ▼'], text='THE MIDNIGHT ZONE')
    state = await obs.read()
    payload = observation(state, obs)
    assert payload['phase'] == 'between_rounds'
    assert payload['prompt'] is None
    assert payload['allowed_actions'] == ['click DESCEND ▼']
    assert 'MIDNIGHT' not in str(payload)


async def test_ambiguous_navigation_is_not_guessed(tmp_path):
    obs = observer(tmp_path, answering=False, timer='', buttons=['DESCEND ▼', 'SURFACE ▲'])
    recovery = NavigationRecovery('bounded')
    for _ in range(4):
        assert not await recovery.before_turn(await obs.read(), obs)
    obs.page.get_by_role.assert_not_called()


async def test_failed_recovery_is_logged_and_not_retried(tmp_path):
    import json
    obs = observer(tmp_path, answering=False, timer='', buttons=['DESCEND ▼'])
    recovery = NavigationRecovery('bounded')
    state = await obs.read()
    await recovery.before_turn(state, obs)
    await recovery.before_turn(state, obs)
    obs.page.get_by_role.return_value.press.side_effect = TimeoutError()
    with pytest.raises(TimeoutError):
        await recovery.before_turn(state, obs)
    assert not await recovery.before_turn(state, obs)
    events = [json.loads(l) for l in (obs.record.output / 'events.jsonl').read_text().splitlines()]
    assert events[-1]['event'] == 'navigation_recovery'
    assert events[-1]['result'] == 'TimeoutError'


async def test_recovery_has_a_whole_run_budget(tmp_path):
    obs = observer(tmp_path, answering=False, timer='', buttons=['DESCEND ▼'])
    recovery = NavigationRecovery('bounded')
    for number in range(9):
        obs.page.evaluate.return_value['round_label'] = f'PREVIEW {number}'
        state = await obs.read()
        for _ in range(3):
            await recovery.before_turn(state, obs)
    assert obs.page.get_by_role.return_value.press.await_count == 8
