from typing import List

def read_grid(path: str = "input.txt") -> List[str]:
    with open(path) as f:
        rows = [line.rstrip("\n") for line in f]
    width = max(len(r) for r in rows)
    return [r.ljust(width) for r in rows]


def calculate_result(grid: List[str]) -> int:
    h = len(grid)
    w = len(grid[0])
    op_row = h - 1

    is_separator = [all(grid[r][c] == " " for r in range(h)) for c in range(w)]

    blocks = []
    c = 0
    while c < w:
        while c < w and is_separator[c]:
            c += 1
        if c >= w:
            break
        start = c
        while c < w and not is_separator[c]:
            c += 1
        end = c
        blocks.append((start, end))

    total = 0

    for start, end in blocks:
        op = None
        for col in range(start, end):
            if grid[op_row][col] in "+*":
                op = grid[op_row][col]
                break
        if op is None:
            raise ValueError(f"No operator found for block {start}-{end}")

        numbers: List[int] = []
        for col in range(end - 1, start - 1, -1):
            digits = [grid[r][col] for r in range(op_row) if grid[r][col].isdigit()]
            if digits:
                numbers.append(int("".join(digits)))

        if op == "*":
            value = 1
            for x in numbers:
                value *= x
        else:
            value = sum(numbers)

        total += value

    return total


if __name__ == "__main__":
    grid = read_grid()
    print(f"Part 2: {calculate_result(grid)}")
