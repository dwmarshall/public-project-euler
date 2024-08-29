N = 5

total = 0

for i in range(2, 10 ** (N + 1)):
    if sum(int(n) ** N for n in str(i)) == i:
        print(f"{i} is a qualifying number")
        total += i

print(total)
