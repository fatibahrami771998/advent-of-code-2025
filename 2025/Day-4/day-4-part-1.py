from typing import List

Grid = List[List[int]]
def read_input(filename:str) -> Grid:
    grid: Grid = []
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            row = [1 if x == "@" else 0 for x in line]
            grid.append(row)
    return grid

DIRECTIONS = [
    (0,1),
    (1,0),
    (0,-1),
    (-1,0),
    (-1,1),
    (-1,-1),
    (1,1),
    (1,-1),
]

def count_available_rolls(grid: Grid) -> int:
    count = 0
    adjacent_count = 0
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            adjacent_count = 0
            if not grid[i][j]:
                continue
            for dx, dy in DIRECTIONS:
                if 0 <= i+dx < n and 0 <= j+dy < m and grid[i+dx][j+dy]:
                    adjacent_count += 1
            if adjacent_count < 4:
                count += 1
    return count


if __name__ == "__main__":
    grid = read_input("input.txt")
    print(f"Part 1: {count_available_rolls(grid)}")