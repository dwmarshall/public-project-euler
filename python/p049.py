from collections import defaultdict
from generators import primes
from itertools import combinations, dropwhile, takewhile

prime = list(
    dropwhile(lambda x: x < 1000, takewhile(lambda x: x < 10000, primes.sequence()))
)

permutations = defaultdict(list)

for p in prime:
    key = "".join(sorted(str(p)))
    permutations[key].append(p)

for value in permutations.values():
    if len(value) < 3:
        continue
    for a, b, c in combinations(value, 3):
        if b - a == 3330 and c - b == 3330:
            print(f"{a}{b}{c}")
