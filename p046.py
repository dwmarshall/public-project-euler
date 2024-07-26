from itertools import count
from generators import primes
from libraries.numeric import issquare

P = primes.sequence()

primes = [next(P)]

for n in count(3, 2):
    while primes[-1] < n:
        primes.append(next(P))
    if n in primes:
        continue
    found = False
    for p in primes[:-1]:
        if issquare((n - p) // 2):
            print(f"{n} can be expressed as {p} + 2 * {n - p} squared")
            found = True
            break
    if not found:
        print(f"{n} cannot be expressed this way")
        break
