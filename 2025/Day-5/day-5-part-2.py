from typing import List, Tuple, Set

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

def get_all_possible_fresh_ids_count(ranges: List[Range]) -> int:
    merged = merge_ranges(ranges)
    count: int = 0
    for m in merged:
        count += m[1] - m[0] + 1
    return count

if __name__ == "__main__":
    ranges, _ = read_input()
    print(f"Part 2: {get_all_possible_fresh_ids_count(ranges)}")
