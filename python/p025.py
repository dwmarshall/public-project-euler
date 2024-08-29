from generators import fibonacci

DIGITS = 1000

f = fibonacci.sequence()

i = 1

while len(str(next(f))) < DIGITS:
    i += 1

print(i)
