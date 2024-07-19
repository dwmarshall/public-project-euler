from functools import cache
from typing import List

GOAL = 200

COINS = (1, 2, 5, 10, 20, 50, 100, 200)


@cache
def ways(goal: int, pence: List[int] = COINS) -> int:
    if len(pence) == 0:
        return 0
    elif goal == 0:
        return 1
    elif goal < pence[0]:
        return 0
    elif goal == pence[0]:
        return 1

    w = 0

    for n in range(1, goal // pence[0] + 1):
        w += ways(goal - n * pence[0], pence[1:])

    w += ways(goal, pence[1:])
    return w


print(ways(GOAL))
