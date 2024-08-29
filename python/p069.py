from fractions import Fraction
from libraries.numeric import totient

N = 1000000

max_totient = (0, Fraction(0, 1))

for n in range(2, N + 1):
    ratio = Fraction(n, totient(n))
    if ratio > max_totient[1]:
        max_totient = n, ratio

print(max_totient)
