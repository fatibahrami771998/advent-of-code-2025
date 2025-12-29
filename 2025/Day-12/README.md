# 🎄 Advent of Code — Day 12  
Christmas Tree Farm — Fitting Oddly-Shaped Presents

## Problem  
The input describes:

1. A list of **present shapes**, drawn using `#` (occupied) and `.` (empty).  
2. A list of **regions**, each given as:

```
WIDTHxHEIGHT: count_0 count_1 count_2 ...
```

Each region indicates how many presents of each shape must fit into the available grid area.  
Presents may be rotated or flipped, but cannot overlap.

The task:  
**Count how many regions can fit all of their required presents.**

---

## Key Observation  
The general problem of tiling irregular shapes is NP-hard.  
However, for the actual Advent of Code input:

> A region can fit all required presents **if and only if**  
> **total present area ≤ region area**.

The tricky packing cases shown in the example do **not** appear in the real input.  
This means a simple area comparison would work just fine!

---

## Approach

### 1. Shape Areas
For each shape, count how many grid cells are occupied:

```
area(shape) = number of '#' cells
```
### 2. Required Area Per Region
Each region specifies quantities like:
```
12x5: 1 0 1 0 2 2
```

Compute:
```
required_area = Σ (shape_area[i] * count[i])
region_area = width * height
```


### 3. Fit Condition
A region can fit all presents if:
```
required_area ≤ region_area
```

Count how many regions satisfy this.

---

## Summary
- Shapes are parsed and their areas computed.  
- Regions are processed by summing total required area.  
- No geometric packing or grid simulation is needed.  
- The **real input** is designed so that area comparison alone solves the problem efficiently.

