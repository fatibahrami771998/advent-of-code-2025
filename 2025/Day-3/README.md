# 🎄 Advent of Code — Day 3: Lobby  
Finding the Maximum Joltage Output

The lobby escalator is offline and needs emergency battery power.  
Each line of the input represents a **bank of batteries**, each containing digits `1–9`.  
The goal: select certain batteries (in **original order**) to form the **largest possible number**.

---

## ⭐ Part 1 — Choose 2 Batteries

For each bank:

- We must select **exactly 2 digits**, in order.
- The joltage is the **two-digit number** formed by these digits.
- Goal: maximize this two-digit number.

### Approach  
For each position `i`, the best second digit is the **maximum digit in the suffix** (positions `i+1 ... end`).  
Compute a `suffix_max` array once, then test all valid pairs.

### Complexity  
- **Time:** O(n) per bank  
- **Memory:** O(n)

---

## ⭐ Part 2 — Choose 12 Batteries

Now each bank must select **exactly 12 digits** (still in original order) to form the **largest possible 12-digit number**.

### Key Insight  
This is a classic greedy problem solved with a **monotonic decreasing stack**:

- Scan digits left → right.
- Pop smaller previous digits if replacing them helps form a larger final number.
- Ensure enough digits remain to reach 12 total.
- Keep the first 12 digits of the resulting stack.

This produces the **lexicographically largest** valid selection.

### Complexity  
- **Time:** O(n) per bank  
- **Memory:** O(n)

---

