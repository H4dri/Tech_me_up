import time

import pytest

from ex6_contexte_exceptions import Timer, parse_age


def test_parse_age():
    assert parse_age("42") == 42


def test_parse_age_with_spaces():
    assert parse_age(" 7 ") == 7


def test_parse_age_not_a_number():
    with pytest.raises(ValueError, match="âge invalide : 'abc'"):
        parse_age("abc")


def test_parse_age_negative():
    with pytest.raises(ValueError, match="âge négatif : -3"):
        parse_age("-3")


def test_timer_measures():
    with Timer() as timer:
        time.sleep(0.05)
    assert 0.04 < timer.elapsed < 1


def test_timer_does_not_hide_errors():
    with pytest.raises(ZeroDivisionError):
        with Timer() as timer:
            1 / 0
    assert timer.elapsed >= 0
