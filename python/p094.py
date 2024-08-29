from generators import pythagorean

N = 1_000_000_000


perimeters = set()

for a, b, c in pythagorean.triples():
    # This is a ridiculous factor that achieves the desired result.
    # The triples are generate in no particular order, so we need
    # to be certain that there are no remaining triples to qualify.
    if min(a, b, c) > 100 * N:
        break
    if 2 * a - c == 1:
        print(f"{c}, {c}, {2 * a} is an almost")
        perimeter = 3 * c + 1
        if perimeter <= N:
            perimeters.add(perimeter)
    elif 2 * b - c == 1:
        print(f"{c}, {c}, {2 * b} is an almost")
        perimeter = 3 * c + 1
        if perimeter <= N:
            perimeters.add(perimeter)
    elif c - 2 * a == 1:
        print(f"{c}, {c}, {2 * a} is an almost")
        perimeter = 3 * c - 1
        if perimeter <= N:
            perimeters.add(perimeter)
    elif c - 2 * b == 1:
        print(f"{c}, {c}, {2 * b} is an almost")
        perimeter = 3 * c - 1
        if perimeter < N:
            perimeters.add(perimeter)


print(perimeters)
print(sum(perimeters))
