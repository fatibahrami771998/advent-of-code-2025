from __future__ import annotations

from functools import lru_cache
from typing import List, Tuple


Grid = List[str]


def read_grid(path: str = "input.txt") -> Tuple[Grid, Tuple[int, int]]:
    rows: List[str] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if line.strip() == "":
                continue
            rows.append(line)

    if not rows:
        raise ValueError("Empty input")

    w = max(len(r) for r in rows)
    grid = [r.ljust(w, ".") for r in rows]

    for r, row in enumerate(grid):
        c = row.find("S")
        if c != -1:
            return grid, (r, c)

    raise ValueError("No start 'S' found in the grid")


def count_timelines(grid: Grid, start: Tuple[int, int]) -> int:
    h = len(grid)
    w = len(grid[0])
    sr, sc = start

    next_split: List[List[int]] = [[-1] * w for _ in range(h)]
    next_in_col = [-1] * w
    for r in range(h - 1, -1, -1):
        for c in range(w):
            if grid[r][c] == "^":
                next_in_col[c] = r
            next_split[r][c] = next_in_col[c]

    def can_emit(split_row: int, col: int) -> bool:
        return 0 <= col < w and grid[split_row][col] != "^"

    @lru_cache(maxsize=None)
    def dp(r: int, c: int) -> int:
        if r >= h:
            return 1

        s = next_split[r][c]
        if s == -1:
            return 1

        total = 0

        left_c = c - 1
        if left_c < 0:
            total += 1
        elif can_emit(s, left_c):
            total += dp(s + 1, left_c)

        right_c = c + 1
        if right_c >= w:
            total += 1
        elif can_emit(s, right_c):
            total += dp(s + 1, right_c)

        return total

    return dp(sr + 1, sc)


if __name__ == "__main__":
    grid, start = read_grid("input.txt")
    print(f"Part 2: {count_timelines(grid, start)}")
