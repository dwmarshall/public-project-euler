from generators import fibonacci
from itertools import takewhile

N = 4000000

print(sum(x for x in takewhile(lambda y: y < N, fibonacci.sequence()) if x % 2 == 0))
