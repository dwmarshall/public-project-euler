from generators import primes
from itertools import permutations, takewhile


# all the pandigital numbers with n digits
def pandigital(n: int) -> list[int]:
    permutant = "".join(str(x) for x in range(1, n + 1))

    return [int("".join(x)) for x in permutations(permutant)]


primeList = list(takewhile(lambda x: x < 100000, primes.sequence()))


def is_prime(n: int) -> bool:
    for p in primeList:
        if n % p == 0:
            return False
    return True


maxPandigital = 0

for N in range(2, 10):
    L = pandigital(N)
    for n in L:
        if is_prime(n):
            maxPandigital = max(maxPandigital, n)

print(maxPandigital)
