from generators import primes
from itertools import product, takewhile
import math

GOAL = 50000000

MAX_SQUARE = math.ceil(math.exp(math.log(GOAL) / 2))
MAX_CUBE = math.ceil(math.exp(math.log(GOAL) / 3))
MAX_FOURTH = math.ceil(math.exp(math.log(GOAL) / 4))

squares = list(takewhile(lambda x: x <= MAX_SQUARE, primes.sequence()))
cubes = list(takewhile(lambda x: x <= MAX_CUBE, squares))
fourths = list(takewhile(lambda x: x <= MAX_FOURTH, squares))

result = set()

for x, y, z in product(squares, cubes, fourths):
    number = x * x + y * y * y + z * z * z * z
    if number < GOAL:
        result.add(number)

print(len(result))
