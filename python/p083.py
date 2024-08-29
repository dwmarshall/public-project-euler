import heapq
import math
from typing import List

with open("../data/0081_matrix.txt") as f:
    M = f.read()

matrix = []
for row in M.splitlines():
    matrix.append([int(x) for x in row.split(",")])


def find_min_cost(matrix: List[List[int]]) -> int:

    rows = len(matrix)
    cols = len(matrix[0])

    min_cost = [[math.inf] * cols for _ in range(rows)]

    heap = [(matrix[0][0], 0, 0)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while heap:
        current_cost, x, y = heapq.heappop(heap)

        if x == rows - 1 and y == cols - 1:
            return current_cost

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                new_cost = current_cost + matrix[nx][ny]
                if new_cost < min_cost[nx][ny]:
                    min_cost[nx][ny] = new_cost
                    heapq.heappush(heap, (new_cost, nx, ny))

    return min_cost[rows - 1][cols - 1]


print(find_min_cost(matrix))
