from functools import cache
from typing import List


@cache
def all_diagonals(side_length: int) -> List[int]:
    assert side_length % 2 == 1

    if side_length == 1:
        return [1]
    square = side_length * side_length
    return sorted(
        [
            square,
            square - (side_length - 1),
            square - 2 * (side_length - 1),
            square - 3 * (side_length - 1),
        ]
        + all_diagonals(side_length - 2)
    )


def diagonals(side_length: int) -> List[int]:
    assert side_length % 2 == 1

    square = side_length * side_length
    return [
        square - 3 * (side_length - 1),
        square - 2 * (side_length - 1),
        square - (side_length - 1),
        square,
    ]
