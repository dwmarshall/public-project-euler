from itertools import chain, combinations
from typing import Iterable, Iterator, Tuple


def powerset(iterable: Iterable) -> Iterator[Tuple]:
    "powerset([1,2,3]) → () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
