from functools import cache
from itertools import count


@cache
def partition(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    w = 0
    k = 1
    while True:
        pent1 = k * (3 * k - 1) // 2
        pent2 = k * (3 * k + 1) // 2
        if pent1 > n:
            break
        w += (-1) ** (k - 1) * partition(n - pent1)
        if pent2 <= n:
            w += (-1) ** (k - 1) * partition(n - pent2)
        k += 1
    return w


D = 10**6

for n in count(1):
    if partition(n) % D == 0:
        print(n, partition(n))
        break
