from generators import primes
from typing import List

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
