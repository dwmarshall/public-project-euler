from functools import cache
from libraries import numeric

proper_divisors = cache(numeric.proper_divisors)

N = 1_000_000

min_term, chain_length, max_chain = 0, 0, None

for m in range(2, N):
    chain = []
    n = m
    while n not in chain and 0 < n <= N:
        chain.append(n)
        n = sum(proper_divisors(n))
    if n == m:
        # print(f"found a chain! {chain}")
        if len(chain) > chain_length:
            chain_length = len(chain)
            min_term = min(chain)
            max_chain = chain

print(min_term, chain_length, max_chain)
