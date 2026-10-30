import pytest

from ex2_fonctions import average, describe, make_counter


def test_average():
    assert average(2, 4, 6) == 4.0


def test_average_single_number():
    assert average(5) == 5


def test_average_without_numbers():
    with pytest.raises(ValueError):
        average()


def test_describe_with_details():
    assert describe("Rex", species="dog", age=3) == "Rex (species=dog, age=3)"


def test_describe_without_details():
    assert describe("Rex") == "Rex"


def test_counter():
    counter = make_counter()
    assert counter() == 1
    assert counter() == 2
    assert counter() == 3


def test_counter_with_start():
    counter = make_counter(10)
    assert counter() == 11


def test_counters_are_independent():
    first = make_counter()
    second = make_counter()
    first()
    first()
    assert second() == 1
    assert first() == 3
