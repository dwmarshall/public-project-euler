from itertools import count

for n in count(1):
    form = sorted(str(n))
    multiples = [sorted(str(n * i)) for i in range(2, 7)]
    if all(x == form for x in multiples):
        print(n)
        break
