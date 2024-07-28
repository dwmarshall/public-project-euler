from collections import defaultdict
from generators import primes
from itertools import count
from libraries.itertools import powerset
from libraries.numeric import digitize

GOAL = 8

for N in count(2):
    P = primes.sequence()

    residue = defaultdict(list)

    for p in P:
        if p < 10 ** (N - 1):
            continue
        if p > 10**N:
            break
        digits = list(reversed(list(digitize(p))))
        digitMap = defaultdict(list)
        for i, d in enumerate(digits):
            digitMap[d].append(i)
        for digit in set(digits):
            for t in powerset(digitMap[digit]):
                if t == ():
                    continue
                template = digits[:]
                for i in t:
                    template[i] = "X"
                template = "".join(str(x) for x in template)
                residue[template].append(p)

    maxLen, firstPrime = 0, 0

    for v in residue.values():
        if len(v) > maxLen:
            maxLen = len(v)
            firstPrime = v[0]

    print(f"First {N}-digit prime with {maxLen} primes is {firstPrime}")
    if maxLen >= GOAL:
        break
