N = 1_000_000_000_000

m, n = 3, 1

while True:
    if m % 2 == 1:
        R = n
        B = (2 * R + 1 + m) // 2
        print(f"{R} red, {B} blue, {R + B} total")
        if R + B > N:
            break
    m, n = 3 * m + 8 * n, m + 3 * n
