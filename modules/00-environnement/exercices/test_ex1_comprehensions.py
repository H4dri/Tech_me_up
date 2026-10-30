from ex1_comprehensions import count_words, squares_of_evens


def test_squares_of_evens():
    assert squares_of_evens([1, 2, 3, 4]) == [4, 16]


def test_squares_of_evens_with_zero_and_negatives():
    assert squares_of_evens([-2, -1, 0]) == [4, 0]


def test_squares_of_evens_empty():
    assert squares_of_evens([]) == []


def test_count_words():
    assert count_words("Le chat et le chien") == {"le": 2, "chat": 1, "et": 1, "chien": 1}


def test_count_words_empty():
    assert count_words("") == {}
