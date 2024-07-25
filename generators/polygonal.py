from typing import Iterator


def triangular_numbers() -> Iterator[int]:
    t = n = 1
    while True:
        yield t
        n += 1
        t += n


def pentagonal_numbers() -> Iterator[int]:
    p = n = 1
    while True:
        yield p
        n += 1
        p = n * (3 * n - 1) // 2
