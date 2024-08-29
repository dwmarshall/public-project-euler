from itertools import accumulate
from operator import mul

factorials = [1] + list(accumulate(range(2, 10), mul, initial=1))

total = 0

for n in range(10, 1000000):
    factorial_sum = sum(factorials[int(x)] for x in str(n))
    if factorial_sum == n:
        print(f"{n} is a factorial sum!")
        total += n

print(total)
