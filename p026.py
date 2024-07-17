D = 1000
maxCycle = 0

cycles = []

for d in range(2, D):
    for r in range(1, 1000):
        x = 10 ** (r + 2) - 10**2
        if x % d == 0:
            cycles.append((r, d))
            break

cycles.sort()
print(cycles[-1])
