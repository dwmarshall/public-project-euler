from typing import Iterator

def sequence() -> Iterator[int]:
    F = (1, 1)
    while True:
        yield F[1]
        F = (F[1], sum(F))
