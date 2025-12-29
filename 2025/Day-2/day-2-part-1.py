from typing import List, Tuple

RANGE = Tuple[int, int]

def read_input(filename: str) -> List[RANGE]:
    ranges: List[RANGE] = []
    with open(filename) as f:
        text = f.read()
    for part in text.replace("\n", "").split(","):
        if not part.strip():
            continue
        start, end = part.strip().split("-")
        ranges.append((int(start), int(end)))

    return ranges

def generate_invalid_digits(left: int, right: int) -> List[int]:
    invalids: List[int] = []
    len_left = len(str(left))
    len_right = len(str(right))

    for d in range(len_left, len_right + 1):
        if d % 2 == 1:
            continue
        half_len = d // 2
        start = 10 ** (half_len - 1)
        end = 10 ** half_len

        for half in range(start, end):
            s = str(half)
            invalid_digit = int(s + s)
            if invalid_digit > right:
                break
            if invalid_digit >= left:
                invalids.append(invalid_digit)
    return invalids

if __name__ == "__main__":
    ranges = read_input("input.txt")

    result = 0
    for left, right in ranges:
        result += sum(generate_invalid_digits(left, right))
    print(f"Part 1: {result}")