from collections import deque
from typing import List, Tuple

Grid = List[List[int]]
Pos = Tuple[int, int]

DIRECTIONS = [
    (0, 1), (1, 0), (0, -1), (-1, 0),
    (-1, 1), (-1, -1), (1, 1), (1, -1),
]

def read_input(filename: str) -> Grid:
    grid: Grid = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            grid.append([1 if c == "@" else 0 for c in line])
    return grid


def total_removable_rolls(grid: Grid) -> int:
    n, m = len(grid), len(grid[0])

    neighbor_count = [[0] * m for _ in range(n)]

    def neighbors(i: int, j: int):
        for dx, dy in DIRECTIONS:
            ni, nj = i + dx, j + dy
            if 0 <= ni < n and 0 <= nj < m:
                yield ni, nj

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                neighbor_count[i][j] = sum(grid[ni][nj] for ni, nj in neighbors(i, j))

    q: deque[Pos] = deque()
    in_queue = [[False] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and neighbor_count[i][j] < 4:
                q.append((i, j))
                in_queue[i][j] = True

    removed = 0

    while q:
        i, j = q.popleft()
        in_queue[i][j] = False

        if grid[i][j] == 0 or neighbor_count[i][j] >= 4:
            continue

        grid[i][j] = 0
        removed += 1

        for ni, nj in neighbors(i, j):
            if grid[ni][nj] == 1:
                neighbor_count[ni][nj] -= 1
                if neighbor_count[ni][nj] < 4 and not in_queue[ni][nj]:
                    q.append((ni, nj))
                    in_queue[ni][nj] = True

    return removed


if __name__ == "__main__":
    grid = read_input("input.txt")
    print(f"Part 2: {total_removable_rolls(grid)}")
