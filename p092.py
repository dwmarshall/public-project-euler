from functools import cache


@cache
def reaches_89(n: int) -> bool:
    if n == 89:
        return True
    elif n == 1:
        return False
    new_number = sum(int(x) * int(x) for x in str(n))
    return reaches_89(new_number)


N = 10000000

print(sum(1 if reaches_89(x) else 0 for x in range(2, N)))
