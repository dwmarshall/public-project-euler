from functools import cache

with open("data/0067_triangle.txt") as f:
    T = f.read()

triangle = []
for row in T.split("\n"):
    if row == "":
        continue
    triangle.append([int(x) for x in row.split(" ")])


@cache
def dfs(row: int, column: int) -> int:
    if row == len(triangle) - 1:
        return triangle[row][column]

    return triangle[row][column] + max(dfs(row + 1, column), dfs(row + 1, column + 1))


print(dfs(0, 0))
