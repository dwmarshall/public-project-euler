from functools import cache

L = 100


@cache
def partition_count(m: int, max_part: int) -> int:
    if m == 0:
        return 1
    if max_part == 0 or m < 0:
        return 0
    return partition_count(m, max_part - 1) + partition_count(m - max_part, max_part)


print(partition_count(L, L - 1))
