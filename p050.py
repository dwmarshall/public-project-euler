from generators import primes
from itertools import accumulate, takewhile

N = 1000000


def filter(x: int) -> bool:
    return x < N


maxLength, maxPrime = 0, 0

prime = list(takewhile(filter, primes.sequence()))
prefixes = list(takewhile(filter, accumulate(prime)))
prime = set(prime)

for i, prefix in enumerate(prefixes):
    if prefix in prime and i > maxLength:
        maxLength, maxPrime = i, prefix

print(f"after accumulate, {maxLength}, {maxPrime}")

for i in range(len(prefixes)):
    for j in range(i):
        if (d := prefixes[i] - prefixes[j]) in prime and i - j > maxLength:
            print(f"span from {j} to {i} = {d}")
            maxLength, maxPrime = i - j, d

print(maxPrime)
