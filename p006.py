N = 100

sumOfSquares = sum(x * x for x in range(N+1))
sumOfNums = sum(list(range(N+1)))

print(sumOfNums * sumOfNums - sumOfSquares)
