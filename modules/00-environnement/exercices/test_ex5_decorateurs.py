from ex5_decorateurs import count_calls, repeat


def test_count_calls_keeps_result():
    @count_calls
    def greet(name):
        return f"salut {name}"

    assert greet("Ada") == "salut Ada"


def test_count_calls_counts():
    @count_calls
    def greet(name):
        return f"salut {name}"

    assert greet.calls == 0
    greet("Ada")
    greet("Alan")
    assert greet.calls == 2


def test_count_calls_any_arguments():
    @count_calls
    def add(a, b, c=0):
        return a + b + c

    assert add(1, 2) == 3
    assert add(1, 2, c=3) == 6
    assert add.calls == 2


def test_count_calls_keeps_name():
    @count_calls
    def greet(name):
        return f"salut {name}"

    assert greet.__name__ == "greet"


def test_repeat():
    results = iter([10, 20, 30])

    @repeat(3)
    def next_value():
        return next(results)

    assert next_value() == [10, 20, 30]


def test_repeat_passes_arguments():
    @repeat(2)
    def double(x):
        return x * 2

    assert double(4) == [8, 8]
