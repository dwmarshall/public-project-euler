from math import gcd

N = 12000

total = 0

for d in range(2, N + 1):
    for n in range(d // 3, d // 2 + 1):
        if n * 3 <= d:
            continue
        if n * 2 >= d:
            break
        if gcd(n, d) == 1:
            total += 1

print(total)
