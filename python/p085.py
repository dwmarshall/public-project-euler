from itertools import count
import math


def rectangles(m: int, n: int) -> int:
    result = 0

    row_rectangles = 0
    for length in range(1, m + 1):
        row_rectangles += m - length + 1
    for height in range(1, n + 1):
        result += row_rectangles * (n - height + 1)

    return result


GOAL = 2000000

min_diff = (math.inf, 0)

for m in count(1):
    if rectangles(m, 1) > GOAL * 2:
        break
    for n in range(1, m):
        r = rectangles(m, n)
        diff = abs(r - GOAL)
        if diff < min_diff[0]:
            min_diff = (diff, m * n)
        elif r > GOAL and diff > min_diff[0]:
            break

print(min_diff[1])
