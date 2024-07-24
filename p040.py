def d(n: int) -> int:
    i = 1
    while len(str(i)) < n:
        n -= len(str(i))
        i += 1
    while len(str(i)) > n:
        i //= 10
    return i % 10


total = 1
for n in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    total *= d(n)
print(total)
