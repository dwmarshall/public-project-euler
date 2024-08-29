from fractions import Fraction
from generators import irrational
import math


def test_convergents():
    x = irrational.convergents(iter([1, 2, 3, 4]))
    assert next(x) == Fraction(1, 1)
    assert next(x) == Fraction(3, 2)
    assert next(x) == Fraction(10, 7)
    assert next(x) == Fraction(43, 30)


def test_convergents_pi():
    quotients = irrational.partial_quotients(math.pi)
    pi = irrational.convergents(quotients)
    assert next(pi) == Fraction(3, 1)
    assert next(pi) == Fraction(22, 7)
    assert next(pi) == Fraction(333, 106)
    assert next(pi) == Fraction(355, 113)
    assert next(pi) == Fraction(103993, 33102)


def test_partial_quotients():
    p = irrational.partial_quotients(math.sqrt(13))
    assert next(p) == 3
    assert next(p) == 1
    assert next(p) == 1
    assert next(p) == 1
    assert next(p) == 1
    assert next(p) == 6
    assert next(p) == 1


def test_root_terms():
    r = irrational.root_terms(7)
    assert next(r) == (2, 2, 3)
    assert next(r) == (1, 1, 2)
    assert next(r) == (1, 1, 3)
    assert next(r) == (1, 2, 1)
    assert next(r) == (4, 2, 3)
    assert next(r) == (1, 1, 2)
