def add(x, y):
    return x + y


def subtract(x, y):
    return y - x


def test_add():
    assert add(3, 5) == 8


def test_subtract():
    assert subtract(5, 10) == 5
