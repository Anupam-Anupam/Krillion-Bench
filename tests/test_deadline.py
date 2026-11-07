import math

import pytest

from deadline import DeadlineExceeded, RoundDeadline


def test_reserves_margin_and_timer_rounding():
    clock = RoundDeadline(margin=3)
    clock.observe("round-1", 25, 100)
    assert clock.expires == 121
    clock.check(120.999)
    with pytest.raises(DeadlineExceeded):
        clock.check(121)


def test_frozen_or_increased_timer_never_extends_deadline():
    clock = RoundDeadline()
    clock.observe("same-prompt", 20, 100)
    clock.observe("same-prompt", 20, 105)
    clock.observe("same-prompt", 25, 110)
    assert clock.expires == 116


def test_reconnect_mid_round_uses_remaining_game_time():
    clock = RoundDeadline()
    clock.observe("round-1", 7, 200)
    assert clock.remaining(200) == 3


def test_new_round_gets_new_budget():
    clock = RoundDeadline()
    clock.observe("round-1", 1, 0)
    clock.clear()
    assert math.isinf(clock.remaining(100))
    clock.observe("round-2", 25, 100)
    clock.check(101)


@pytest.mark.parametrize("value", [-1, 26, math.inf, math.nan])
def test_unrecognized_timer_fails_closed(value):
    with pytest.raises(ValueError):
        RoundDeadline().observe("round", value, 0)
