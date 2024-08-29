import math

with open("../data/0081_matrix.txt") as f:
    M = f.read()

matrix = []
for row in M.splitlines():
    matrix.append([int(x) for x in row.split(",")])

rows = len(matrix)
cols = len(matrix[0])

dp = [[math.inf] * cols for _ in range(rows)]

for i in range(rows):
    dp[i][0] = matrix[i][0]

for j in range(1, cols):
    for i in range(rows):
        # Moving from the left
        dp[i][j] = min(dp[i][j], dp[i][j - 1] + matrix[i][j])

    # propagate changes downwards
    for i in range(1, rows):
        dp[i][j] = min(dp[i][j], dp[i - 1][j] + matrix[i][j])

    # propagate upwards
    for i in range(rows - 2, -1, -1):
        dp[i][j] = min(dp[i][j], dp[i + 1][j] + matrix[i][j])

print(min(dp[i][-1] for i in range(rows)))
