from bisect import bisect_right
from typing import List, Tuple

Range = Tuple[int, int]


def read_input(path: str = "input.txt") -> Tuple[List[Range], List[int]]:
    ranges: List[Range] = []
    ids: List[int] = []
    reading_ranges = True

    with open(path) as f:
        for line in f:
            line = line.strip()
            if line == "":
                reading_ranges = False
                continue

            if reading_ranges:
                a_str, b_str = line.split("-")
                ranges.append((int(a_str), int(b_str)))
            else:
                ids.append(int(line))

    return ranges, ids

def merge_ranges(ranges: List[Range]) -> List[Range]:
    if not ranges:
        return []

    ranges.sort()
    merged: List[Range] = [ranges[0]]

    for a, b in ranges[1:]:
        last_a, last_b = merged[-1]
        if a <= last_b + 1:
            merged[-1] = (last_a, max(last_b, b))
        else:
            merged.append((a, b))

    return merged


def is_fresh(x: int, merged: List[Range]) -> bool:
    starts = [a for a, _ in merged]
    i = bisect_right(starts, x) - 1
    if i < 0:
        return False
    a, b = merged[i]
    return a <= x <= b


def count_fresh_ids(ranges: List[Range], ids: List[int]) -> int:
    merged = merge_ranges(ranges)
    return sum(1 for x in ids if is_fresh(x, merged))

if __name__ == "__main__":
    ranges, ids = read_input()
    print(f"Part 1: {count_fresh_ids(ranges, ids)}")