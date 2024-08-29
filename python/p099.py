from math import log

data = []

with open("../data/0099_base_exp.txt") as f:
    for i, s in enumerate(f):
        s = s.strip()
        line_number, base, exponent = i, *s.split(",")
        data.append((int(exponent) * log(int(base)), line_number))

data.sort(reverse=True)

# data[0][1] + 1 is the line with the largest number
print(data[0][1] + 1)
