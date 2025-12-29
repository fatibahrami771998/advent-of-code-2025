# 🎄 Advent of Code — Day 9  
Rectangle Areas in a Tile Loop

## Problem
Each input line is `x,y` describing a **red tile** on a large grid.  
A rectangle is formed by choosing **two red tiles** as opposite corners.

---

# Part 1 — Largest Rectangle Using Red Corners

### Goal
Find the largest axis-aligned rectangle that can be formed using **any two red tiles** as opposite corners.  
There are **no restrictions** on what lies inside the rectangle.

### Approach
For every pair of red points `(p1, p2)`:
- `width = |x1 - x2| + 1`  
- `height = |y1 - y2| + 1`  
- Track `area = width * height`.

This brute-force check over all pairs is sufficient.

### Complexity
- Time: **O(n²)**  
- Memory: **O(1)** beyond the input list.

---

# Part 2 — Largest Rectangle Fully Inside the Loop

### New Information
The red tiles are given in order around a rectilinear loop.
Between each consecutive pair (including last→first) is a straight line of green tiles, and the entire interior of the loop is also green.

### Goal
Find the largest rectangle whose entire interior consists only of red or green tiles. In other words, a rectangle that stays fully inside the red/green loop, still using two red tiles as corners.

### Approach

Treat the ordered red tiles as the loop polygon.
A rectangle between (p1, p2) is valid if no polygon edge intersects its interior.
For each rectangle:
1. Compute its bounding box.
2. If its max possible area cannot beat the current best, skip.
3. Check each polygon edge’s bounding box:
- If the edge is entirely left/right/above/below → safe
- Otherwise the edge would cut into the rectangle → reject
4. Accept the rectangle if all edges are safe.

Time: `O(n³)` in the worst case (all pairs × edge scan) but fast enough for AoC input; Memory: `O(1)` extra.

## Running
With `input.txt` in this folder:
```bash
python day-9-part-1.py  # Part 1 solution
python day-9-part-2.py  # Part 2 solution
```

## Summary
- Part 1: pure pairwise rectangle area maximization.  
- Part 2: same pairs, filtered by a bounding-box edge test to ensure the rectangle sits fully inside the loop.  
