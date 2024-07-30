from generators.polygonal import (
    triangular_numbers,
    square_numbers,
    pentagonal_numbers,
    hexagonal_numbers,
    heptagonal_numbers,
    octagonal_numbers,
)
from itertools import dropwhile, permutations, takewhile

triangles = list(
    dropwhile(lambda n: n < 1000, takewhile(lambda n: n < 10000, triangular_numbers()))
)
squares = list(
    dropwhile(lambda n: n < 1000, takewhile(lambda n: n < 10000, square_numbers()))
)
pentagons = list(
    dropwhile(lambda n: n < 1000, takewhile(lambda n: n < 10000, pentagonal_numbers()))
)
hexagons = list(
    dropwhile(lambda n: n < 1000, takewhile(lambda n: n < 10000, hexagonal_numbers()))
)
heptagons = list(
    dropwhile(lambda n: n < 1000, takewhile(lambda n: n < 10000, heptagonal_numbers()))
)
octagons = list(
    dropwhile(lambda n: n < 1000, takewhile(lambda n: n < 10000, octagonal_numbers()))
)

sequences = [squares, pentagons, hexagons, heptagons, octagons]

for w in permutations(sequences):
    tuples = [(t,) for t in triangles]
    for item in w:
        new_tuples = []
        for t in tuples:
            new_tuples.extend([t + (x,) for x in item if t[-1] % 100 == x // 100])
        tuples = new_tuples
    for t in tuples:
        if t[-1] % 100 == t[0] // 100:
            print(f"{t} => {sum(t)}")
