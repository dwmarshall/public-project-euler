from generators import primes
from itertools import islice

N = 10001
print(next(islice(primes.sequence(), N - 1, N)))
