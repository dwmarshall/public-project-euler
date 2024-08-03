from math import isqrt


def digital_sum(n: int, digits: int) -> int:
    total = 0
    remainder = n
    estimate = 0
    for d in range(digits):
        for x in range(9, -1, -1):
            y = (20 * estimate + x) * x
            if y <= remainder:
                break
        total += x
        estimate *= 10
        estimate += x
        remainder -= y
        remainder *= 100
    return total


grand_total = 0
for n in range(1, 101):
    if isqrt(n) * isqrt(n) == n:
        continue
    grand_total += digital_sum(n, 100)
print(grand_total)
