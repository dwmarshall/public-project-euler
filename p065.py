from fractions import Fraction
from itertools import count
from typing import Iterator


def continued(n: int, iter: Iterator[int]) -> Iterator[int]:
    terms = []
    yield n
    for a in iter:
        terms.append(a)
        x = 0
        for b in terms[::-1]:
            x = Fraction(1, b + x)
        yield n + x


def e_terms():
    for k in count(1):
        yield 1
        yield 2 * k
        yield 1


# root2 = continued(1, itertools.repeat(2))
e = continued(2, e_terms())

terms = [next(e) for _ in range(100)]
x = terms[-1].numerator
y = [int(c) for c in str(x)]
print(sum(y))
