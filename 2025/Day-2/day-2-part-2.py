from typing import List, Tuple, Set

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
    invalid: Set[int] = set()
    len_left = len(str(left))
    len_right = len(str(right))

    for d in range(len_left, len_right + 1):
        for k in range(2, d + 1):
            if d % k != 0:
                continue

            block_len = d // k
            start = 10 ** (block_len - 1)
            end = 10 ** block_len

            for base in range(start, end):
                s = str(base)
                num_str = s * k
                num = int(num_str)

                if num > right:
                    break
                if num >= left:
                    invalid.add(num)
    return sorted(invalid)

if __name__ == "__main__":
    ranges = read_input("input.txt")

    result = 0
    for left, right in ranges:
        result += sum(generate_invalid_digits(left, right))
    print(f"Part 1: {result}")