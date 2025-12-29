# 🎄 Advent of Code — Day 5: Cafeteria  
Fresh Ingredient Ranges (Interval Merging)

## Problem
The input contains:
1) A list of **inclusive ID ranges** `a-b` describing which ingredient IDs are *fresh* (ranges can overlap).
2) A blank line.
3) A list of available ingredient IDs.

An ID is **fresh** if it lies in **any** range.

---

## ⭐ Part 1 — Count Fresh Available IDs
### Goal
Count how many IDs in the second section are fresh.

### Approach
- Sort and **merge** overlapping/touching ranges into disjoint intervals.
- For each available ID, check membership using **binary search** on interval starts.

### Complexity
- Merge: `O(r log r)`
- Queries: `O(q log r)`  
(`r` = number of ranges, `q` = number of IDs)

---

## ⭐⭐ Part 2 — Count All Fresh IDs in the Ranges
### Goal
Ignore the available IDs. Compute how many distinct IDs are covered by the fresh ranges.

### Approach
- Merge the ranges (same as Part 1).
- Sum each merged interval’s size: `(end - start + 1)`.

### Complexity
- Merge: `O(r log r)`
- Counting: `O(r)`

---

## Notes
- Merging intervals handles overlaps cleanly and prevents double-counting.
- Part 1 uses the merged representation for fast membership tests.
- Part 2 uses the merged representation for fast total coverage counting.
