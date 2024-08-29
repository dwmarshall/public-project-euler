from generators import primes
from itertools import takewhile
from typing import List

N = 1000000


def rotations(n: int) -> List[int]:
    result = []
    digits = [c for c in str(n)]
    while (r := int("".join(digits))) not in result:
        result.append(r)
        digits = digits[-1:] + digits[:-1]
    return result


primeSet = set(takewhile(lambda n: n < N, primes.sequence()))

circular = 0

for n in range(2, N):
    if n in primeSet and all(d in primeSet for d in rotations(n)):
        circular += 1

print(circular)
