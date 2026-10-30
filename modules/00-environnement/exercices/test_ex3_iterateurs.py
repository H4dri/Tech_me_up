import inspect

import pytest

from ex3_iterateurs import Countdown, chunks


def test_chunks():
    assert list(chunks([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]


def test_chunks_exact_split():
    assert list(chunks([1, 2, 3, 4], 2)) == [[1, 2], [3, 4]]


def test_chunks_empty():
    assert list(chunks([], 3)) == []


def test_chunks_is_a_generator():
    assert inspect.isgenerator(chunks([1, 2, 3], 2))


def test_countdown_in_a_loop():
    assert list(Countdown(3)) == [3, 2, 1]


def test_countdown_with_next():
    countdown = Countdown(2)
    assert next(countdown) == 2
    assert next(countdown) == 1
    with pytest.raises(StopIteration):
        next(countdown)


def test_countdown_does_not_use_yield():
    assert not inspect.isgeneratorfunction(Countdown.__iter__)
    assert not inspect.isgeneratorfunction(Countdown.__next__)
