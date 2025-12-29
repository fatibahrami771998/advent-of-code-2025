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

def max_joltage(bank: List[int]) -> int:
    n = len(bank)
    suffix_max = [0] * n
    suffix_max[-1] = bank[-1]
    for i in range(n - 2, -1, -1):
        suffix_max[i] = max(bank[i], suffix_max[i + 1])
    best = 0
    for i in range(n-1):
        ones_digit = suffix_max[i+1]
        joltage = bank[i]*10 + ones_digit
        if joltage > best:
            best = joltage
    return best

def total_joltage(banks: List[List[int]]) -> int:
    return sum(max_joltage(bank) for bank in banks)

if __name__ == "__main__":
    banks = read_input("input.txt")
    print(f"part 1: {total_joltage(banks)}")