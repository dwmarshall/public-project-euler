N = 100

powers = set()

for a in range(2, N + 1):
    for b in range(2, N + 1):
        powers.add(a**b)

print(len(powers))
