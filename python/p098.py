from collections import defaultdict
from itertools import permutations
from libraries.numeric import is_square
import string

with open("data/0098_words.txt") as f:
    s = f.read()

anagrams = defaultdict(set)
for w in s.split(","):
    key = "".join(sorted(w[1:-1]))
    anagrams[key].add(str(w[1:-1]))

max_square = 0

for k, v in anagrams.items():
    if len(v) == 1:
        continue
    for t in permutations(string.digits, r=len(k)):
        mapping = dict(zip(k, t))
        all_square = True
        max_number = 0
        for anagram in v:
            number = "".join(mapping[c] for c in anagram)
            if number.startswith("0"):
                all_square = False
                break
            if is_square(int(number)):
                max_number = max(max_number, int(number))
            else:
                all_square = False
                break
        if all_square:
            print(f"for {mapping}, {v} is all squares!")
            max_square = max(max_square, max_number)

print(max_square)
