from copy import deepcopy
from typing import List, Set

grids = []

DIGITS = set(range(1, 10))


def line(g: List[List[int]], row: int) -> Set[int]:
    return set(x for x in g[row] if x > 0)


def column(g: List[List[int]], col: int) -> Set[int]:
    return {g[r][col] for r in range(len(g)) if g[r][col] > 0}


def cell(g: List[List[int]], cell_row: int, cell_col: int) -> Set[int]:
    return {
        g[r][c]
        for r in range(cell_row * 3, cell_row * 3 + 3)
        for c in range(cell_col * 3, cell_col * 3 + 3)
        if g[r][c] > 0
    }


def possible_values(g: List[List[int]], row: int, col: int) -> Set[int]:
    assert g[row][col] == 0
    return DIGITS - line(g, row) - column(g, col) - cell(g, row // 3, col // 3)


def valid(g: List[List[int]]) -> bool:
    if any(line(g, r) != DIGITS for r in range(9)):
        return False
    if any(column(g, c) != DIGITS for c in range(9)):
        return False
    if any(cell(g, r, c) != DIGITS for r in range(3) for c in range(3)):
        return False
    return True


def solve(g: List[List[int]]) -> None:
    if valid(g):
        return
    g_prime = deepcopy(g)

    moves = []

    for i in range(9):
        for j in range(9):
            if g_prime[i][j] == 0:
                p = possible_values(g_prime, i, j)
                if len(p) == 0:
                    return
                elif len(p) == 1:
                    v = p.pop()
                    g_prime[i][j] = v
                else:
                    moves.append((len(p), i, j, p))
    # check whether one-choice only moves solved it
    if valid(g_prime):
        g.clear()
        g.extend(g_prime)
        return
    if len(moves) == 0:
        return
    moves.sort()
    _, i, j, options = moves[0]
    for v in options:
        g_prime[i][j] = v
        solve(g_prime)
        if valid(g_prime):
            g.clear()
            g.extend(g_prime)
            return


with open("../data/p096_sudoku.txt") as f:
    for s in f:
        s = s.strip()
        if s.startswith("Grid"):
            grids.append([])
            continue
        grids[-1].append([int(x) for x in s])

total = 0
for g in grids:
    solve(g)
    total += 100 * g[0][0] + 10 * g[0][1] + g[0][2]

print(total)
