from itertools import permutations

total = 0
for p in permutations("0123456789"):
    s = "".join(p)
    if int(s[1:4]) % 2:
        continue
    if int(s[2:5]) % 3:
        continue
    if int(s[3:6]) % 5:
        continue
    if int(s[4:7]) % 7:
        continue
    if int(s[5:8]) % 11:
        continue
    if int(s[6:9]) % 13:
        continue
    if int(s[7:10]) % 17:
        continue
    print(f"{s} qualifies!")
    total += int(s)

print(total)
