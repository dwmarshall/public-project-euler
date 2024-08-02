from libraries.numeric import totient

N = 1000000

print(sum(totient(x) for x in range(2, N + 1)))
