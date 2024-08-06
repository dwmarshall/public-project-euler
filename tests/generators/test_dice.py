from collections import Counter
from generators import dice

N = 100000
EPSILON = 0.1


def test_normal_dice():
    D = dice.rolls()
    c = Counter()

    multiple = [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

    for _ in range(N):
        d1, d2 = next(D)
        c[d1 + d2] += 1

    for t in range(2, 13):
        expected = N * multiple[t] // 36
        diff = abs(c[t] - expected)
        assert diff / expected < EPSILON


def test_funny_dice():
    D = dice.rolls(4, 5, 6)
    c = Counter()

    multiple = [0, 0, 0, 1, 3, 6, 10, 14, 17, 18, 17, 14, 10, 6, 3, 1]

    for _ in range(N):
        d1, d2, d3 = next(D)
        c[d1 + d2 + d3] += 1

    for t in range(3, 16):
        expected = N * multiple[t] // 120
        diff = abs(c[t] - expected)
        assert diff / expected < EPSILON
