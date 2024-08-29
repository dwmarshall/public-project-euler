from fractions import Fraction
from math import floor, isqrt
from typing import Iterator, Tuple


# Most of the idea behind these generators comes from
# https://mathworld.wolfram.com/RegularContinuedFraction.html


def convergents(iter: Iterator[int]) -> Iterator[Fraction]:
    """Expresses a series of partial quotients as a fraction"""
    n = Fraction(next(iter))
    yield n
    a0 = next(iter)
    c0 = Fraction(1, a0)
    yield n + c0
    a1 = next(iter)
    c1 = Fraction(1, a0 + Fraction(1, a1))
    yield n + c1
    while True:
        a2 = next(iter)
        n2 = a2 * c1.numerator + c0.numerator
        d2 = a2 * c1.denominator + c0.denominator
        c2 = Fraction(n2, d2)
        yield n + c2
        c0, c1 = c1, c2


def partial_quotients(f: float) -> Iterator[int]:
    """Expresses an (presumably irrational) number as a series
    of integers such that f = a0, f = a0 + 1/a1,
    f = a0 + 1/(a1 + 1/a2) ..."""
    r = f
    b = floor(f)
    yield b
    while True:
        r = 1 / (r - b)
        b = floor(r)
        yield b


def root_terms(n: int) -> Iterator[Tuple[int, int, int]]:
    """A specialized partial quotient generator that includes
    the parameters for the continued fraction. This permits
    detecting the periodic cycle"""
    a = x = isqrt(n)
    y = n - a * a
    yield a, x, y
    while True:
        a_hat = (isqrt(n) + x) // y
        x_hat = a_hat * y - x
        y_hat = (n - (x - a_hat * y) ** 2) // y
        yield a_hat, x_hat, y_hat
        a = a_hat
        x = x_hat
        y = y_hat
