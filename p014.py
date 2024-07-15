from functools import cache


@cache
def collatz(n: int) -> int:
    if n == 1:
        return 1
    if n % 2 == 1:
        return 1 + collatz(3 * n + 1)
    else:
        return 1 + collatz(n // 2)


maxTerms = 0
maxN = 0

N = 1000000

for n in range(1, N):
    terms = collatz(n)
    if terms > maxTerms:
        maxN, maxTerms = n, terms

print(maxN)
