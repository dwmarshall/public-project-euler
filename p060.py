from collections import defaultdict
from generators import primes
from functools import cache
from itertools import combinations, permutations, takewhile
from libraries.numeric import is_prime


@cache
def prime_pair(a: int, b: int) -> bool:
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


D = 5
N = 9000

prime_list = list(takewhile(lambda x: x < N, primes.sequence()))

matching = [[] for _ in range(D + 1)]

for a, b in combinations(prime_list[1:], 2):
    if prime_pair(a, b):
        matching[2].append((a, b))
print(f"2:{len(matching[2])}")

for d in range(3, D + 1):
    for tuple in matching[d - 1]:
        index = prime_list.index(tuple[-1])
        for p in prime_list[index + 1 :]:
            if all(prime_pair(x, p) for x in tuple):
                matching[d].append(tuple + (p,))
    print(f"{d}:{len(matching[d])}")

print(matching[D])
print(min(sum(t) for t in matching[D]))
