from generators import primes
from functools import cache
from itertools import combinations
from libraries.numeric import is_prime


@cache
def prime_pair(a: int, b: int) -> bool:
    return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))


D = 5

P = primes.sequence()

prime_list = []
while len(prime_list) < D:
    prime_list.append(next(P))

matching = [[] for _ in range(D + 1)]
matching[1] = [(x,) for x in prime_list]
matching[2] = [(x, y) for x, y in combinations(prime_list, 2) if prime_pair(x, y)]

while True:
    p = next(P)
    for d in range(2, D + 1):
        for t in matching[d - 1]:
            if all(prime_pair(x, p) for x in t):
                matching[d].append(t + (p,))
    matching[1].append((p,))
    if matching[D]:
        print(matching[D])
        break

print(sum(matching[D][0]))
