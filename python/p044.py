from generators.polygonal import pentagonal_numbers
from itertools import count
from libraries.numeric import ispentagonal

P = pentagonal_numbers()

pentagonals = [0]

for j in count(1):
    Pj = next(P)
    pentagonals.append(Pj)
    done = False
    for k in range(1, j):
        Pk = pentagonals[k]
        if ispentagonal(Pj + Pk) and ispentagonal(Pj - Pk):
            print(Pj - Pk)
            done = True
            break
    if done:
        break
