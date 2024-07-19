from generators import primes
from itertools import takewhile

# make a list of all the primes under 1000
primeSet = set(takewhile(lambda x: x < 1000000, primes.sequence()))


def consecutivePrimes(a: int, b: int) -> int:
    n = 0
    while n * n + a * n + b in primeSet:
        n += 1
    return n


maxA, maxB, maxPrimes = 0, 0, 0

for candidateB in primes.sequence():
    if candidateB > 1000:
        break
    for candidateA in range(-1000, 1001):
        if (numPrimes := consecutivePrimes(candidateA, candidateB)) > maxPrimes:
            print(f"new winner!: {candidateA} {candidateB} => {numPrimes}")
            maxA, maxB, maxPrimes = candidateA, candidateB, numPrimes

print(maxA * maxB)
