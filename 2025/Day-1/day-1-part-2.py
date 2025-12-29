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


def count_zero_hits(rotations: List[Tuple[int, int]]) -> int:
    pos = START_POINT
    hits = 0

    for step, amount in rotations:
        first_hit = (-pos * step) % NUMS
        if first_hit == 0:
            first_hit = NUMS

        if first_hit <= amount:
            hits += 1 + (amount - first_hit) // NUMS

        pos = (pos + step * amount) % NUMS

    return hits


if __name__ == "__main__":
    rotations = read_input()
    print(f"Part 2: {count_zero_hits(rotations)}")
