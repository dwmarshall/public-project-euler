from libraries import spiral
import pytest


def test_all_diagonals():
    assert spiral.all_diagonals(1) == [1]
    assert spiral.all_diagonals(3) == [1, 3, 5, 7, 9]
    assert spiral.all_diagonals(5) == [1, 3, 5, 7, 9, 13, 17, 21, 25]


def test_even_all_diagonals():
    with pytest.raises(AssertionError):
        spiral.all_diagonals(2)


def test_diagonals():
    assert spiral.diagonals(5) == [13, 17, 21, 25]
