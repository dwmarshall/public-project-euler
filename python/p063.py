from math import floor, log10

count = 0
for i in range(1, 10):
    count += floor(1 / (1 - log10(i)))
print(count)
