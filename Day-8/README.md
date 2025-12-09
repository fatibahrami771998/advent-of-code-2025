🎄 Advent of Code — Day 8  
3D Junction Box Networks (Kruskal + Union–Find)

## Problem
Each line of the input is `x,y,z`, the position of a junction box. Edges are always added in order of increasing Euclidean distance squared, but only if they connect two different components.

## Approach
- Parse all points, generate every pairwise edge with squared distance.  
- Sort edges ascending.  
- Use Union–Find (DSU with path compression + union by size) to accept edges that merge components.  
- This is Kruskal’s algorithm; Part 1 stops early, Part 2 runs to full connectivity.

Complexity: O(n² log n) to build/sort edges, O(n² α(n)) for unions; memory O(n²) for the edge list. Suitable for the provided AoC input sizes.

## Running the solutions
From this folder with `input.txt` present:
- Part 1: `python day-8.py`  
  - Adds the first 1000 merging edges.  
  - Prints the three largest circuit sizes and their product.
- Part 2: `python day-8-part-2.py`  
  - Runs until the graph is fully connected.  
  - Prints the indices of the last merging pair, their X coordinates, and the product.

## What each part computes
- Part 1: After 1000 successful merges, gather component sizes, take the top three, and multiply them.  
- Part 2: Track the final edge that actually merges two remaining components; multiply the X coordinates of its endpoints.

## Key ideas
- Kruskal-style edge ordering drives the “shortest first” wiring.  
- DSU keeps connectivity checks near O(1).  
- Stopping criteria differ: fixed merge budget (Part 1) vs full connectivity (Part 2).