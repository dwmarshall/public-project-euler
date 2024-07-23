from generators import primes

P = primes.sequence()

primeSet = set()


def isCircular(n: int) -> bool:
    if n < 10:
        return False
    s = str(n)
    leftwards = [int(s[i:]) for i in range(len(s))]
    rightwards = [int(s[:i]) for i in range(1, len(s))]
    return all(x in primeSet for x in leftwards + rightwards)


N = 11  # how many cyclic primes we expect to find
total = 0

while (p := next(P)) and N:
    primeSet.add(p)
    if isCircular(p):
        print(f"{p} is circular!")
        total += p
        N -= 1

print(total)
