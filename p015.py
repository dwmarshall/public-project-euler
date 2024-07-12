N = 20

grid = [[1] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

print(grid[-1][-1])
