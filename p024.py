from itertools import permutations

permuter = permutations("0123456789")

N = 1000000

for _ in range(N - 1):
    next(permuter)

print("".join(next(permuter)))
