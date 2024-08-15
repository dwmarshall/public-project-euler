from itertools import count, permutations, product
from math import isclose
import operator
from typing import Callable, List


def initial_integers(s: set) -> int:
    for i in count(1):
        if i not in s:
            return i - 1


def safe_operation(op: Callable, x: int | float, y: int | float) -> int | float:
    try:
        return op(x, y)
    except ZeroDivisionError:
        return None


def apply_operations(
    a: int, b: int, c: int, d: int, op1: Callable, op2: Callable, op3: Callable
) -> List[int]:
    results = []
    results.append(
        safe_operation(op3, safe_operation(op2, safe_operation(op1, a, b), c), d)
    )  # ((a op1 b) op2 c) op3 d
    results.append(
        safe_operation(op2, safe_operation(op1, a, b), safe_operation(op3, c, d))
    )  # (a op1 b) op2 (c op3 d)
    results.append(
        safe_operation(op1, a, safe_operation(op3, safe_operation(op2, b, c), d))
    )  # a op1 ((b op2 c) op3 d)
    results.append(
        safe_operation(op1, safe_operation(op2, a, safe_operation(op3, b, c)), d)
    )  # (a op1 (b op2 c)) op3 d
    results.append(
        safe_operation(op3, safe_operation(op1, a, b), safe_operation(op2, c, d))
    )  # (a op1 b) op3 (c op2 d)

    return [x for x in results if x is not None]


operators = [
    operator.__add__,
    operator.__sub__,
    operator.__mul__,
    operator.__truediv__,
]

max_tuple, max_n = None, 0

# value = 1
# value = operator.mul(value, 2)
# value = operator.add(value, 3)
# value = operator.sub(value, 4)
# print(value)
for t in product(range(1, 10), repeat=4):
    if any(t[x + 1] <= t[x] for x in range(len(t) - 1)):
        continue
    results = set()
    for a, b, c, d in permutations(t):
        for op1, op2, op3 in product(operators, repeat=3):
            for value in apply_operations(a, b, c, d, op1, op2, op3):
                if value > 0 and isclose(value, int(value)):
                    results.add(int(value))
    n = initial_integers(results)
    if n > max_n:
        max_tuple, max_n = t, n

print(max_tuple, max_n)
