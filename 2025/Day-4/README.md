# 🎄 Advent of Code — Day 4  
Printing Department (Grid Simulation)

## Problem
The input is a 2D grid where `@` represents a roll of paper and `.` is empty space.

A roll is **accessible by a forklift** if **fewer than 4** of its **8 surrounding neighbors** are also rolls.

---

## Part 1 — Initially Accessible Rolls

### Goal
Count how many paper rolls are immediately accessible based on the rule above.

### Approach
- Parse the grid into `1` (roll) and `0` (empty).
- For each roll, count occupied neighbors in the 8 directions.
- If the count is `< 4`, it is accessible.

### Complexity
- Time: **O(N × M)**  
- Memory: **O(1)** extra

---

## Part 2 — Chain Removals

### Goal
Once a roll is accessible, it can be removed.
Removing rolls may expose **new** accessible rolls.
Repeat until no more rolls can be removed.

Count **all removed rolls**.

### Approach
- Precompute neighbor counts for all rolls.
- Use a **queue** to track rolls that become accessible.
- When a roll is removed:
  - Update neighbor counts.
  - Push newly-accessible neighbors into the queue.
- Each roll is processed at most once.

This avoids rescanning the full grid every round.

### Complexity
- Time: **O(N × M)**  
- Memory: **O(N × M)**

---

## Summary
- Part 1: Single-pass neighbor counting.
- Part 2: Incremental “peeling” using a queue for efficiency.
- Both parts operate directly on the grid without recursion.

⭐ Efficient and scalable grid simulation.
