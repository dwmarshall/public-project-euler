import libraries
import pytest

import libraries.itertools


def test_powerset():
    assert list(libraries.itertools.powerset([1, 2, 3])) == [
        (),
        (1,),
        (2,),
        (3,),
        (1, 2),
        (1, 3),
        (2, 3),
        (1, 2, 3),
    ]
