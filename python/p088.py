from functools import cache
from libraries.numeric import proper_divisors
from typing import List


@cache
def product_lists(n: int) -> List[List[int]]:

    results = []

    divisors = proper_divisors(n)
    divisors.remove(1)

    if len(divisors) == 0:
        results.append([n])
    elif len(divisors) == 1:
        only_divisor = divisors.pop()
        results.append(sorted([only_divisor, n // only_divisor]))
    else:
        for d in divisors:
            results.append(sorted([d, n // d]))
            for sublist in product_lists(n // d):
                new_list = sorted([d] + sublist)
                if new_list not in results:
                    results.append(sorted([d] + sublist))

    return results


product_sum_numbers = set()

N = 12000

for k in range(2, N + 1):
    least = k * k
    for n in range(k, 2 * k + 1):
        for product_list in product_lists(n):
            # we know that each list multiplies to n
            if n == sum(product_list) + k - len(product_list):
                least = n
                break
        if least == n:
            break
    product_sum_numbers.add(least)

print(product_sum_numbers)
print(sum(product_sum_numbers))
