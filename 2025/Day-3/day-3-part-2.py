from typing import List

def read_input(filename: str) -> List[List[int]]:
    with open(filename) as f:
        lines = f.readlines()
    banks: List[List[int]] = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        bank = [int(d) for d in line]
        banks.append(bank)
    return banks

def max_joltage(bank: List[int], k: int) -> int:
    stack : List[int] = []
    remaining = len(bank)

    for digit in bank:
        while stack and digit > stack[-1] and len(stack) - 1 + remaining >= k:
            stack.pop()
        stack.append(digit)
        remaining -= 1
    chosen = stack[:k]

    value = 0
    for d in chosen:
        value = value*10 + d
    return value


if __name__== "__main__":
    banks = read_input("input.txt")
    total = sum(max_joltage(bank, 12) for bank in banks)
    print(f"Part 2: {total}")