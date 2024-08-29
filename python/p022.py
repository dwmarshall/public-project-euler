f = open("../data/names.txt")
s = f.read()
f.close()

names = s.split(",")
for i in range(len(names)):
    names[i] = names[i][1:-1]
names.sort()
score = 0
for i in range(len(names)):
    score += (i + 1) * sum(ord(c) - ord("A") + 1 for c in names[i])
print(score)
