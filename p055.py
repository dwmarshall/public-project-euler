def is_palindrome(n: int) -> bool:
    return str(n) == str(n)[::-1]


def reverse_and_add(n: int) -> int:
    return n + int(str(n)[::-1])


MAX_ITERATIONS = 50
N = 10000
total = 0

for n in range(1, N):
    z = reverse_and_add(n)
    lychrel = True
    for _ in range(MAX_ITERATIONS):
        if is_palindrome(z):
            lychrel = False
            break
        z = reverse_and_add(z)
    if lychrel:
        print(f"{n} is a Lychrel number")
        total += 1

print(total)
