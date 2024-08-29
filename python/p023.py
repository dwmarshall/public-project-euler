from libraries.numeric import proper_divisors

N = 28124

abundant = [False] * N
abundant_sum = 0

for n in range(2, N):
    if sum(proper_divisors(n)) > n:
        abundant[n] = True

for n in range(1, N):
    unsummed = True
    for i in range(n // 2, n):
        if abundant[i] and abundant[n - i]:
            unsummed = False
            break
    if unsummed:
        abundant_sum += n

print(abundant_sum)
