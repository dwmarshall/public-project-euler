from libraries import numeric
import pytest


def test_gcd():
    assert numeric.gcd(874, 1406) == 38


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
