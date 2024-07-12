N = 1000

n = 2 ** N

total = 0

while n:
    (n, digit) = divmod(n, 10)
    total += digit

print(total)
