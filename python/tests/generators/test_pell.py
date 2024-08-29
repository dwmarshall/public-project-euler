from generators import pell
from math import isqrt
import pytest
from random import randint


def test_root_8():
    x = pell.equation(8)
    assert next(x) == (3, 1)
    assert next(x) == (17, 6)
    assert next(x) == (99, 35)
    assert next(x) == (577, 204)


def test_root_4():
    x = pell.equation(4)

    with pytest.raises(AssertionError):
        next(x)


def test_random():
    D = randint(2, 100)

    # Make sure we're not using a perfect square
    while isqrt(D) * isqrt(D) == D:
        D = randint(2, 100)

    g = pell.equation(D)

    for _ in range(100):
        x, y = next(g)
        assert x * x - D * y * y == 1
