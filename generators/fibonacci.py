from typing import Iterator


def sequence(first: int = 1, second: int = 1) -> Iterator[int]:
    F = (first, second)
    while True:
        yield F[0]
        F = (F[1], sum(F))
