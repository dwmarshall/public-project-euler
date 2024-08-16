N = 7830457
D = 10

number = 1

for i in range(N):
    number *= 2
    _, number = divmod(number, 10**D)

number *= 28433
number += 1
_, number = divmod(number, 10**D)

print(number)
