from typing import Iterator


def root2() -> Iterator[tuple]:
    numerator, denominator = 1, 2
    while True:
        yield numerator + denominator, denominator
        numerator, denominator = denominator, 2 * denominator + numerator


R = root2()
total = 0
for i in range(1000):
    n, d = next(R)
    if len(str(n)) > len(str(d)):
        total += 1

print(total)
