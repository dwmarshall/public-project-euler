from collections.abc import Callable
from typing import Iterator


def _generate_sequence(formula: Callable[[int], int]) -> Iterator[int]:
    n = 1
    while True:
        yield formula(n)
        n += 1


def triangular_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (n + 1) // 2)


def square_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * n)


def pentagonal_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (3 * n - 1) // 2)


def hexagonal_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (2 * n - 1))


def heptagonal_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (5 * n - 3) // 2)


def octagonal_numbers() -> Iterator[int]:
    return _generate_sequence(lambda n: n * (3 * n - 2))
