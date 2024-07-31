from math import floor, isqrt, sqrt
from typing import Tuple


def terms(n: int, T: Tuple[int, int, int]) -> Tuple[int, int, int]:
    a, x, y = T
    a_hat = floor(x / (sqrt(n) - y))
    x_hat = round((n - y * y) / x)
    y_hat = round(a_hat * x_hat + sqrt(n) - x * x_hat / (sqrt(n) - y))
    return (a_hat, x_hat, y_hat)


N = 10000
odd_period = 0
for n in range(2, N + 1):
    a0 = isqrt(n)
    if a0 * a0 == n:
        continue
    T = (a0, 1, a0)
    a = [T]
    while True:
        T = terms(n, a[-1])
        if T in a[1:]:
            break
        else:
            a.append(T)
    print(f"period of {n} is {a}")
    if len(a) % 2 == 0:
        odd_period += 1
print(odd_period)
