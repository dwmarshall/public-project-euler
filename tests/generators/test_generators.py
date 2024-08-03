import generators
import generators.fibonacci
import generators.polygonal
import generators.primes


def test_fibonacci_default():
    f = generators.fibonacci.sequence()
    first_ten = [next(f) for _ in range(10)]
    assert first_ten == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fibonacci_different():
    f = generators.fibonacci.sequence(1, 2)
    first_ten = [next(f) for _ in range(10)]
    assert first_ten == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_heptagonal():
    h = generators.polygonal.heptagonal_numbers()
    first_ten = [next(h) for _ in range(10)]
    assert first_ten == [1, 7, 18, 34, 55, 81, 112, 148, 189, 235]


def test_hexagonal():
    h = generators.polygonal.hexagonal_numbers()
    first_ten = [next(h) for _ in range(10)]
    assert first_ten == [1, 6, 15, 28, 45, 66, 91, 120, 153, 190]


def test_octagonal():
    o = generators.polygonal.octagonal_numbers()
    first_ten = [next(o) for _ in range(10)]
    assert first_ten == [1, 8, 21, 40, 65, 96, 133, 176, 225, 280]


def test_generalized_pentagonal():
    p = generators.polygonal.pentagonal_numbers(generalized=True)
    first_ten = [next(p) for _ in range(10)]
    assert first_ten == [0, 1, 2, 5, 7, 12, 15, 22, 26, 35]


def test_pentagonal():
    p = generators.polygonal.pentagonal_numbers()
    first_ten = [next(p) for _ in range(10)]
    assert first_ten == [1, 5, 12, 22, 35, 51, 70, 92, 117, 145]


def test_prime():
    p = generators.primes.sequence()
    first_ten = [next(p) for _ in range(10)]
    assert first_ten == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_square():
    s = generators.polygonal.square_numbers()
    first_ten = [next(s) for _ in range(10)]
    assert first_ten == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def test_triangular():
    t = generators.polygonal.triangular_numbers()
    first_ten = [next(t) for _ in range(10)]
    assert first_ten == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
