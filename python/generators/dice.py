from random import randint
from typing import Iterator, List


def rolls(*args: int) -> Iterator[List[int]]:
    if len(args) == 0:
        args = [6, 6]
    while True:
        yield [randint(1, x) for x in args]
