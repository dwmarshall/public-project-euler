N = 100

max_digital_sum = 0

for a in range(1, N):
    for b in range(1, N):
        c = a**b
        digital_sum = sum(int(x) for x in str(c))
        max_digital_sum = max(max_digital_sum, digital_sum)

print(max_digital_sum)
