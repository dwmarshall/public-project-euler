from collections import Counter
from generators import primes
from functools import cache, reduce
from itertools import product
from math import sqrt
from typing import List

# Divisors stuff comes from this page:
# https://rosettacode.org/wiki/Proper_divisors#Python


def gcd(u: int, v: int) -> int:
    multiplier = 1
    while u % 2 == 0 and v % 2 == 0:
        u //= 2
        v //= 2
        multiplier *= 2

    t = -v if u % 2 == 1 else u

    while t != 0:
        while t % 2 == 0:
            t //= 2
        if t > 0:
            u = t
        else:
            v = -t
        t = u - v

    return u * multiplier


def lcm(n: List[int]) -> int:
    if len(n) == 2:
        return n[0] * n[1] // gcd(n[0], n[1])
    else:
        subLCM = lcm(n[1:])
        return n[0] * subLCM // gcd(n[0], subLCM)


def number_of_divisors(n: int) -> int:
    divisors = 1
    prime = primes.sequence()
    while (p := next(prime)) <= n:
        exponent = 0
        while n % p == 0:
            n //= p
            exponent += 1
        if exponent:
            divisors *= exponent + 1
    return divisors


@cache
def prime_divisors(n: int) -> List[int]:
    """
    a list of the prime divisors, such as
    220 => [2, 2, 5, 11]
    """
    assert n > 0
    for i in range(2, int(sqrt(n) + 1)):
        d, m = divmod(n, i)
        if not m:
            return [i] + prime_divisors(d)
    return [n]


def prime_factors(n: int) -> dict:
    """
    A dictionary of the prime divisors of a number,
    such as 220 => {2: 2, 5: 1, 11: 1}
    """
    d = prime_divisors(n)
    # rosettacode.org has this line, not sure what the
    # d[-1] == d is about, however
    # d = [] if d == [n] else (d[:-1] if d[-1] == d else d)
    d = [] if d == [n] else d
    return dict(Counter(d))


def proper_divisors(n: int) -> set:
    """
    The set of proper divisors of a number,
    e.g. 220 => {1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110}
    """
    assert n > 0
    factors_dict = prime_factors(n)
    factors, occurrences = factors_dict.keys(), factors_dict.values()
    multiplicities = product(*(range(oc + 1) for oc in occurrences))
    divs = {
        reduce(int.__mul__, (pf ** m for pf, m in zip(factors, multis)), 1)
        for multis in multiplicities
    }
    divs.discard(n)
    return divs or ({1} if n != 1 else set())
