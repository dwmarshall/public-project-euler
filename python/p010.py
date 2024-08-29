from generators import primes

N = 2000000
total = 0

prime = primes.sequence()

while (p := next(prime)) < N:
    total += p

print(total)
