from __future__ import annotations

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
    grid = [r.ljust(w, ".") for r in rows]  # pad with dots

    for r, row in enumerate(grid):
        c = row.find("S")
        if c != -1:
            return grid, (r, c)

    raise ValueError("No start 'S' found in the grid")


def count_splits(grid: Grid, start: Tuple[int, int]) -> int:
    h = len(grid)
    w = len(grid[0])
    sr, sc = start

    active = [False] * w
    active[sc] = True

    split_count = 0

    for r in range(sr + 1, h):
        next_active = [False] * w

        for c in range(w):
            if not active[c]:
                continue

            cell = grid[r][c]
            if cell == "^":
                split_count += 1

                left = c - 1
                if 0 <= left < w and grid[r][left] != "^":
                    next_active[left] = True

                right = c + 1
                if 0 <= right < w and grid[r][right] != "^":
                    next_active[right] = True
            else:
                next_active[c] = True

        active = next_active

    return split_count


if __name__ == "__main__":
    grid, start = read_grid("input.txt")
    print(f"Part 1: {count_splits(grid, start)}")
