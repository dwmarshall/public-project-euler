from functools import cache
from itertools import accumulate
from operator import mul

FACTORIALS = [1] + list(accumulate(range(1, 10), mul))


@cache
def factorial_sum(n: int) -> int:
    if n < 10:
        return FACTORIALS[n]
    n, r = divmod(n, 10)
    return FACTORIALS[r] + factorial_sum(n)


N = 1000000
total = 0
for i in range(1, N):
    n = i
    chain = set()
    while n not in chain:
        chain.add(n)
        n = factorial_sum(n)
    if len(chain) == 60:
        print(f"{i} has a chain of length {len(chain)}")
        total += 1

print(total)
