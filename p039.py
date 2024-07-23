def pythagoreanSolutions(n: int) -> int:
    solutions = 0
    for a in range(n // 4):
        for b in range(a, n // 2):
            if a * a + b * b == (n - a - b) * (n - a - b):
                solutions += 1

    return solutions


maxP = 0
maxSolutions = 0

for p in range(1, 1001):
    if p * p % 2 == 1:
        continue
    s = pythagoreanSolutions(p)
    if s > maxSolutions:
        maxSolutions = s
        maxP = p

print(maxP)
