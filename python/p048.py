from functools import reduce

N = 1000
D = 10

result = reduce(lambda x, y: x + y**y, range(1, N + 1))

print(result % 10**D)
