# 🎄 Advent of Code — Day 10  
Indicator Lights & Joltage Configuration

Each machine description contains:

- **Indicator lights** in `[ ]`, e.g. `[.##.#]`
- **Buttons** in `( )`, e.g. `(0,2,4)`
- **Joltage requirements** in `{ }`, e.g. `{3,5,4,7}`

Lights start **off** and joltage counters start at **0**.

This day splits into two completely different problems.

---

## ⭐ Part 1 — Indicator Lights (Toggle System)

Buttons toggle their listed lights:
- Each press XORs a bitmask  
- Pressing twice cancels out  
- Goal: reach the target light pattern with the **fewest presses**

### Approach
- Convert the light pattern to a bitmask  
- Convert each button to a bitmask  
- Perform **BFS** starting from state `0` (all lights off)  
- Each action flips bits using XOR  
- The first time the target is reached gives the minimal press count  

Efficient because the search space is small and unweighted.

---

## ⭐ Part 2 — Joltage Counters (Integer Linear System)

Buttons now increment their listed counters:
- Pressing button `j` adds **+1** to its assigned counters  
- Goal: reach each required joltage exactly  
- Buttons may be pressed **any number of times**  

This forms an **integer linear system**:

```
A * x = target
x >= 0
minimize sum(x)
```

Where:
- `x[j]` is the number of times button `j` is pressed  
- Each counter produces one equation  
- All presses must be non-negative integers  

### Approach
Use an **integer optimizer (Z3)**:
- One integer variable per button  
- Add sum constraints per counter  
- Constrain variables to be ≥ 0  
- Minimize the total presses  

Z3 efficiently finds the exact minimum.

---

## 📌 Summary

- **Part 1:** XOR toggle system solved with BFS over bitmasks.  
- **Part 2:** Increment system solved as a constrained integer minimization problem.  
