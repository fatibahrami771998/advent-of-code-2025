# 🎄 Advent of Code — Day 7  
Tachyon Manifold

## Problem
A tachyon beam enters a vertical manifold at `S` and moves **downward**.

- Empty cells (`.`): beam passes through.
- Splitters (`^`): the beam stops and emits new beams to the **left** and **right**.
- Beams never move upward.

---

## Part 1 — Classical Manifold

### Goal
Count how many times a beam encounters a splitter (`^`) and splits.

### Approach
- Track active beam positions row by row.
- When a beam hits `^`, count a split and activate left/right beams.
- Continue until all beams exit the grid.

### Complexity
- **Time:** `O(H × W)`
- **Memory:** `O(W)`

---

## Part 2 — Quantum Manifold (Many Worlds)

### Goal
Count how many distinct **timelines** a single particle can end up on.

### Key Insight
Each splitter doubles timelines, but timelines that reach the **same cell** merge.

### Approach
- Dynamic programming per row.
- Each cell stores how many ways it can be reached.
- At `^`, distribute counts left and right.
- Sum all counts in the last row.

### Complexity
- **Time:** `O(H × W)`
- **Memory:** `O(W)`

---

## Summary
- Same grid parsing for both parts.
- Part 1 counts **split events**.
- Part 2 counts **distinct timelines**.
- Row-wise DP avoids exponential blow-up.
