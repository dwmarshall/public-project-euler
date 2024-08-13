from itertools import product

triangles = 0

N = 50

for x1, y1, x2, y2 in product(range(N + 1), repeat=4):
    if (x1, y1) == (0, 0) or (x2, y2) == (0, 0) or (x1, y1) == (x2, y2):
        continue
    squared_lengths = []
    squared_lengths.append(x1 * x1 + y1 * y1)
    squared_lengths.append(x2 * x2 + y2 * y2)
    squared_lengths.append((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
    squared_lengths.sort()
    if squared_lengths[0] + squared_lengths[1] == squared_lengths[2]:
        print(f"({x1}, {y1}), ({x2}, {y2}) is a right triangle!")
        triangles += 1

# Divide by two instead of trying to sort the points.
print(triangles // 2)
