import generators
import generators.fibonacci
import generators.polygonal


def test_fibonacci_default():
    f = generators.fibonacci.sequence()
    first_ten = [next(f) for _ in range(10)]
    assert first_ten == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fibonacci_different():
    f = generators.fibonacci.sequence(1, 2)
    first_ten = [next(f) for _ in range(10)]
    assert first_ten == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_pentagonal():
    p = generators.polygonal.pentagonal_numbers()
    first_ten = [next(p) for _ in range(10)]
    assert first_ten == [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]


def test_prime():
    p = generators.primes.sequence()
    first_ten = [next(p) for _ in range(10)]
    assert first_ten == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_triangular():
    t = generators.polygonal.triangular_numbers()
    first_ten = [next(t) for _ in range(10)]
    assert first_ten == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
