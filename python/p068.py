from functools import reduce
from itertools import permutations
from operator import concat
from typing import List

tuples = ((0, 1, 2), (3, 2, 4), (5, 4, 6), (9, 6, 7), (8, 7, 1))
firsts = [x[0] for x in tuples]


def is_magic(T: List[int]) -> bool:
    if T[0] < min([T[x] for x in firsts[1:]]):
        L = [sum([T[j] for j in t]) for t in tuples]
        return all([L[0] == x for x in L[1:]])
    else:
        return False


solutions = []
for p in permutations(list(range(1, 11))):
    if is_magic(p):
        solution = [[str(p[i]) for i in t] for t in tuples]
        solution = reduce(concat, solution)
        solutions.append("".join(solution))
print(max(solutions))
