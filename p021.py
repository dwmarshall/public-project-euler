from functools import cache
from libraries.numeric import proper_divisors

@cache
def divisor_sum(n: int) -> int:
    return sum(proper_divisors(n))

total_sum = 0

for n in range(2, 10000):
    s = divisor_sum(n)
    if n != s and n == divisor_sum(s):
        total_sum += n

print(total_sum)
