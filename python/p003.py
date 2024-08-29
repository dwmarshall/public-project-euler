from generators import primes

# TARGET = 13195
TARGET = 600851475143

prime = primes.sequence()
maxFactor = 0

while (p := next(prime)) * p < TARGET:
    if TARGET % p == 0:
        maxFactor = p

print(maxFactor)
