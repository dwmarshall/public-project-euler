from generators.irrational import convergents, root_terms
from math import isqrt
from typing import Iterator, Tuple


def equation(D: int) -> Iterator[Tuple[int, int]]:
    """yields (x, y) tuples for the solution of x^2 - D * y^2 = 1"""
    # There are no solutions if D is a perfect square
    assert isqrt(D) * isqrt(D) != D
    partial_quotients = (t[0] for t in root_terms(D))

    for f in convergents(partial_quotients):
        x = f.numerator
        y = f.denominator
        if x * x - D * y * y == 1:
            yield x, y
            break

    x1, y1 = x, y
    while True:
        x, y = x1 * x + D * y1 * y, x1 * y + y1 * x
        yield x, y
