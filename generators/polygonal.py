from typing import Iterator

def triangular_numbers() -> Iterator[int]:
    t = n = 1
    while True:
        yield t
        n += 1
        t += n
