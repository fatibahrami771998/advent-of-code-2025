# 🎄 Advent of Code — Day 6  
Cephalopod Math Worksheet (Column Parsing)

## Problem
The input is a wide “worksheet” containing multiple vertical math problems laid out side-by-side.
Each problem has a column of numbers and an operator (`+` or `*`) on the bottom row. Problems are separated by a full column of spaces.

- **Part 1:** Read numbers normally (left-to-right), compute each problem’s result, and sum them.
- **Part 2:** Read the worksheet **right-to-left by columns**. Each column forms one number (top digit = most significant). Compute each problem and sum again.

---

## Part 1 — Row-wise Parsing
### Approach
- Read number rows with `split()` into aligned columns.
- Read the operator row (`+` / `*`).
- For each column/problem:
  - Start at `0` for `+`, or `1` for `*`
  - Combine all numbers in that column using the operator.
- Sum all problem results.

---

## Part 2 — Grid + Column-wise Parsing
### Approach
- Read the input as a fixed-width **character grid** (preserve spaces).
- Identify each problem as a contiguous **block of non-empty columns** (separated by all-space columns).
- For each block:
  - Find the operator from the bottom row.
  - Read columns **right-to-left**:
    - Collect digits from top to bottom (ignoring spaces)
    - Each column with digits becomes one number
  - Apply the operator across the extracted numbers.
- Sum all block results.

---

## Key Ideas
- Part 1 works with whitespace tokenization (`split()`).
- Part 2 must preserve layout; treat the worksheet as a grid.
- “Full blank column” is the separator between problems.
- Column-wise reconstruction is the core twist in Part 2.
