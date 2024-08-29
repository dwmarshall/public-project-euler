from itertools import accumulate
from operator import mul

factorial = [0] + list(accumulate(range(1, 101), mul))


def combinations(n: int, r: int) -> int:
    if n <= r:
        return 1
    return factorial[n] // factorial[r] // factorial[n - r]


total = 0

for n in range(1, 101):
    for r in range(1, n):
        if combinations(n, r) > 1000000:
            total += 1

print(total)
