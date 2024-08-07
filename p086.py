from functools import cache
from itertools import count
from libraries.numeric import is_square

is_square = cache(is_square)

GOAL = 1000000

total = 0

for a in count(1):
    # decide for what values of b + c could make a right triangle
    possible_sums = set(k for k in range(1, 2 * a) if is_square(a * a + k * k))
    cardinality = 0
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            if b + c in possible_sums:
                cardinality += 1
    total += cardinality
    if total > GOAL:
        print(a)
        break
