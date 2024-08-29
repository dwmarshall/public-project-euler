from collections import Counter

L = 1500000

perimeter = Counter()

triangles = [(3, 4, 5)]

while triangles:
    a, b, c = triangles.pop()
    # print(f"processing ({a}, {b}, {c})")
    P = a + b + c
    perimeter[P] += 1
    for n in range(2, L // P + 1):
        perimeter[P * n] += 1
    # compute new triangles with Price's ternary tree
    a1 = 2 * a + b - c
    b1 = -2 * a + 2 * b + 2 * c
    c1 = -2 * a + b + 3 * c
    if a1 + b1 + c1 <= L:
        triangles.append((a1, b1, c1))
    a2 = 2 * a + b + c
    b2 = 2 * a - 2 * b + 2 * c
    c2 = 2 * a - b + 3 * c
    if a2 + b2 + c2 <= L:
        triangles.append((a2, b2, c2))
    a3 = 2 * a - b + c
    b3 = 2 * a + 2 * b + 2 * c
    c3 = 2 * a + b + 3 * c
    if a3 + b3 + c3 <= L:
        triangles.append((a3, b3, c3))

print(sum(1 if perimeter[x] == 1 else 0 for x in perimeter))
