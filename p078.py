from functools import cache
from generators.polygonal import pentagonal_numbers
from itertools import count

P = pentagonal_numbers(generalized=True)
term_list = [next(P)]


@cache
def partition(n: int) -> int:
    if n == 0:
        return 1
    if n < 0:
        return 0
    w = 0
    s = 1
    for k in count():
        if 2 * k + 1 >= len(term_list):
            break
        term1 = term_list[2 * k + 1]
        if term1 > n:
            break
        w += s * partition(n - term1)
        if 2 * k + 2 < len(term_list) and (term2 := term_list[2 * k + 2]) <= n:
            w += s * partition(n - term2)
        s *= -1

    return w


D = 10**6

for n in count(1):
    while max(term_list) < n:
        term_list.append(next(P))
    if partition(n) % D == 0:
        print(n, partition(n))
        break
