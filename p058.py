from itertools import count
from libraries.numeric import is_prime
from libraries.spiral import diagonals

THRESHOLD = 0.10

diagonal_count = 1
prime_count = 0

for n in count(3, 2):
    diagonal_count += 4
    for d in diagonals(n):
        if is_prime(d):
            prime_count += 1
    ratio = prime_count / diagonal_count
    if ratio < THRESHOLD:
        print(f"for side length {n}: {prime_count} / {diagonal_count} = {ratio}")
        break
