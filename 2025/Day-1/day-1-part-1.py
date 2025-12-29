from typing import List, Tuple

START_POINT = 50
NUMS = 100


def read_input() -> List[Tuple[int, int]]:
    rotations = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            direction = line[0]
            amount = int(line[1:])
            step = 1 if direction == "R" else -1
            rotations.append((step, amount))

    return rotations


def count_zero_end_positions(rotations: List[Tuple[int, int]]) -> int:
    pos = START_POINT
    hits = 0

    for step, amount in rotations:
        pos = (pos + step * amount) % NUMS
        if pos == 0:
            hits += 1

    return hits


if __name__ == "__main__":
    rotations = read_input()
    print(f"Part 1: {count_zero_end_positions(rotations)}")
