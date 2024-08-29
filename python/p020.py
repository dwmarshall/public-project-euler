from math import prod

N = 100

product = prod(list(range(1, N + 1)))

print(sum(int(c) for c in str(product)))
