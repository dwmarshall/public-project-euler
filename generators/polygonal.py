from collections.abc import Callable
from itertools import count
from typing import Iterator


def _generate_sequence(formula: Callable[[int], int]) -> Iterator[int]:
    for n in count(1):
        yield formula(n)


def _generate_generalized_sequence(formula: Callable[[int], int]) -> Iterator[int]:
    n = 0
    for i in count(2):
        yield formula(n)
        n = (-1) ** i * (i // 2)


def triangular_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (n + 1) // 2)


def square_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * n)


def pentagonal_numbers(generalized: bool = False) -> Iterator[int]:
    def formula(n: int) -> int:
        return n * (3 * n - 1) // 2

    if generalized:
        return _generate_generalized_sequence(formula)
    else:
        return _generate_sequence(formula)


def hexagonal_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (2 * n - 1))


def heptagonal_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (5 * n - 3) // 2)


def octagonal_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (3 * n - 2))
