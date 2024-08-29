from itertools import cycle, product
import re
from string import ascii_lowercase

with open("../data/0059_cipher.txt") as f:
    s = f.read()

encrypted = [int(x) for x in s.split(",")]

keys = product(ascii_lowercase, ascii_lowercase, ascii_lowercase)

p_the = re.compile("\\bthe\\b", re.I)
p_this = re.compile("\\bthis\\b", re.I)

for k in keys:
    key_values = [ord(x) for x in k]
    clear = [chr(x[0] ^ x[1]) for x in zip(encrypted, cycle(key_values))]
    candidate = "".join(clear)
    if p_the.search(candidate) and p_this.search(candidate):
        print(candidate)
        print("".join(k))
        print(sum(ord(x) for x in clear))
        break
