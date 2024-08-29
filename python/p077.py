from functools import cache
from generators import primes
from itertools import count

N = 5000

P = primes.sequence()
prime_list = [next(P)]


@cache
def partition_count(m: int, max_prime_index: int) -> int:
    if m == 0:
        return 1
    if max_prime_index < 0 or m < 0:
        return 0
    return partition_count(m, max_prime_index - 1) + partition_count(
        m - prime_list[max_prime_index], max_prime_index
    )


for n in count(4):
    while prime_list[-1] < n:
        prime_list.append(next(P))
    if partition_count(n, len(prime_list) - 1) > N:
        print(n)
        break
