total = 0

for n in range(1000000):
    base10 = str(n)
    if base10 != base10[::-1]:
        continue
    base2 = f"{n:b}"
    if base2 == base2[::-1]:
        total += n

print(total)
