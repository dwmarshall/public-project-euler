from collections import deque
from typing import Iterator, Tuple


def triples() -> Iterator[Tuple[int, int, int]]:
    T = deque([(3, 4, 5)])

    while True:
        a, b, c = T.popleft()
        yield a, b, c
        a1 = a - 2 * b + 2 * c
        b1 = 2 * a - b + 2 * c
        c1 = 2 * a - 2 * b + 3 * c
        T.append((a1, b1, c1))
        a2 = a + 2 * b + 2 * c
        b2 = 2 * a + b + 2 * c
        c2 = 2 * a + 2 * b + 3 * c
        T.append((a2, b2, c2))
        a3 = -a + 2 * b + 2 * c
        b3 = -2 * a + b + 2 * c
        c3 = -2 * a + 2 * b + 3 * c
        T.append((a3, b3, c3))
