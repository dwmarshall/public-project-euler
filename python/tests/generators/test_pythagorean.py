from generators import pythagorean

PRIMITIVE_TRIPLES = [
    (3, 4, 5),
    (5, 12, 13),
    (21, 20, 29),
    (15, 8, 17),
    (7, 24, 25),
    (55, 48, 73),
    (45, 28, 53),
    (39, 80, 89),
    (119, 120, 169),
    (77, 36, 85),
    (33, 56, 65),
    (65, 72, 97),
    (35, 12, 37),
]


# see https://mathworld.wolfram.com/PythagoreanTriple.html
def test_triples():
    T = pythagorean.triples()
    for pt in PRIMITIVE_TRIPLES:
        assert next(T) == pt
