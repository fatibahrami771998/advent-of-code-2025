from typing import List, Tuple

def read_input(path: str = "input.txt") -> Tuple[List[List[int]], List[str]]:
    nums: List[List[int]] = []
    signs: List[str] = []
    with open(path) as f:
        lines = f.readlines()
    for line in lines:
        if not line.strip():
            continue
        if "*" in line or "+" in line:
            signs = line.split()
            return nums, signs
        nums.append(list(map(int, line.split())))
    return nums, signs

def calculate_results(nums: List[List[int]], signs: List[str]) -> int:
    results: List[int] = [0 if sign == "+" else 1 for sign in signs]
    for lst in nums:
        for idx, val in enumerate(lst):
            if signs[idx] == "+":
                results[idx] += val
            else:
                results[idx] *= val
    return sum(results)


if __name__ == "__main__":
    nums, signs = read_input()
    print(f"Part 1: {calculate_results(nums, signs)}")