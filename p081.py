from functools import cache

with open("data/0081_matrix.txt") as f:
    M = f.read()

matrix = []
for row in M.splitlines():
    matrix.append([int(x) for x in row.split(",")])


@cache
def dfs(i: int, j: int) -> int:
    choices = []
    if i < len(matrix) - 1:
        choices.append(matrix[i][j] + dfs(i + 1, j))
    if j < len(matrix[0]) - 1:
        choices.append(matrix[i][j] + dfs(i, j + 1))
    return min(choices) if choices else matrix[i][j]


print(dfs(0, 0))
