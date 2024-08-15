from libraries.numeric import is_square

N = 1_000_000_000


perimeters = set()

a = 2

for a in range(2, N // 3):
    # case: base = side + 1
    if is_square(3 * a * a - 2 * a - 1):
        print(f"{a}, {a}, {a + 1} is an almost")
        perimeters.add(3 * a + 1)
    # case: base = side - 1
    if is_square(3 * a * a + 2 * a - 1):
        print(f"{a}, {a}, {a - 1} is an almost")
        perimeters.add(3 * a - 1)
    if perimeters and max(perimeters) >= N:
        break

print(perimeters)
print(sum(perimeters))
