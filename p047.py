from itertools import count
from libraries.numeric import prime_factors

N = 4
consecutive = 0

for n in count(2):
    if len(prime_factors(n)) == N:
        consecutive += 1
    else:
        consecutive = 0
    if consecutive == N:
        print(f"The first number is {n - N + 1}")
        break
