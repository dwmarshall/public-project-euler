from fractions import Fraction

target = Fraction(3, 7)
current = Fraction(2, 5)

N = 1000000

for d in range(8, N + 1):
    for n in range(d * current.numerator // current.denominator, d):
        if d % n == 0:
            break
        f = Fraction(n, d)
        if f <= current:
            continue
        elif f < target:
            current = f
        else:
            break

print(current.numerator)
