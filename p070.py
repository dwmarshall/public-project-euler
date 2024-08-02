from fractions import Fraction
from libraries.numeric import totient
from math import gcd

N = 7
GCD_FACTOR = 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23 * 29 * 31 * 37

max_totient = (0, Fraction(100, 1))

for n in range(10**N // 2 + 1, 10**N, 2):
    if gcd(n, GCD_FACTOR) > 1:
        continue
    t = totient(n)
    if sorted(str(n)) == sorted(str(t)) and Fraction(n, t) < max_totient[1]:
        print(f"new winner! {n}")
        max_totient = (n, Fraction(n, t))

print(max_totient)
