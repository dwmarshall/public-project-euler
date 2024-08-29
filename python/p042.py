from libraries.numeric import istriangular

with open("data/0042_words.txt") as f:
    s = f.read()

triangularWords = 0
for w in s.split(","):
    score = sum([ord(c) - ord("A") + 1 for c in w[1:-1]])
    if istriangular(score):
        triangularWords += 1

print(triangularWords)
