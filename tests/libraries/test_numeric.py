from generators import primes
from itertools import islice
from libraries import numeric
import pytest


def test_digitize():
    assert list(numeric.digitize(0)) == [0]
    assert list(numeric.digitize(123)) == [3, 2, 1]
    assert list(numeric.digitize(10, 2)) == [0, 1, 0, 1]


def test_gcd():
    assert numeric.gcd(874, 1406) == 38


def test_ispentagonal():
    assert not numeric.ispentagonal(91)
    assert numeric.ispentagonal(92)
    assert not numeric.ispentagonal(93)

    assert numeric.ispentagonal(1926)
    assert not numeric.ispentagonal(1962)


def test_is_prime():
    P = set(islice(primes.sequence(), 1000))
    for n in range(3, max(P), 2):
        if n in P:
            print(f"asserting that {n} is prime")
            assert numeric.is_prime(n)
        else:
            assert not numeric.is_prime(n)


def test_is_square():
    assert not numeric.is_square(48)
    assert numeric.is_square(49)
    assert not numeric.is_square(50)


def test_istriangular():
    assert not numeric.istriangular(54)
    assert numeric.istriangular(55)
    assert not numeric.istriangular(56)


def test_lcm():
    assert numeric.lcm([330, 225]) == 4950
    assert numeric.lcm([330, 75, 450, 11, 37]) == 183150


def test_number_of_divisors():
    assert numeric.number_of_divisors(220) == 12


def test_prime_divisors():
    assert numeric.prime_divisors(37) == [37]
    assert numeric.prime_divisors(220) == [2, 2, 5, 11]

    with pytest.raises(AssertionError):
        numeric.prime_divisors(0)


def test_prime_factors():
    assert numeric.prime_factors(220) == {2: 2, 5: 1, 11: 1}

    with pytest.raises(AssertionError):
        numeric.prime_factors(0)


def test_proper_divisors():
    assert numeric.proper_divisors(220) == {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}
    assert sum(numeric.proper_divisors(220)) == 284

    # edge cases
    assert numeric.proper_divisors(1) == set()

    with pytest.raises(AssertionError):
        numeric.proper_divisors(0)


def test_totient():
    # The totients for 1 .. 100 are formatted this way to keep
    # them from being formatted as one big list.
    TOTIENTS = (
        (1, 1, 2, 2, 4, 2, 6, 4, 6, 4),
        (10, 4, 12, 6, 8, 8, 16, 6, 18, 8),
        (12, 10, 22, 8, 20, 12, 18, 12, 28, 8),
        (30, 16, 20, 16, 24, 12, 36, 18, 24, 16),
        (40, 12, 42, 20, 24, 22, 46, 16, 42, 20),
        (32, 24, 52, 18, 40, 24, 36, 28, 58, 16),
        (60, 30, 36, 32, 48, 20, 66, 32, 44, 24),
        (70, 24, 72, 36, 40, 36, 60, 24, 78, 32),
        (54, 40, 82, 24, 64, 42, 56, 40, 88, 24),
        (72, 44, 60, 46, 72, 32, 96, 42, 60, 40),
    )
    n = 1
    for group in TOTIENTS:
        for item in group:
            assert item == numeric.totient(n)
            n += 1
