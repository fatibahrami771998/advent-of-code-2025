# 🎄 Advent of Code — Day 2  
Gift Shop ID Validation

Our task is to detect **invalid product IDs** inside several numeric ranges.  
An ID is invalid if its digits follow certain repeating-pattern rules.

---

## ⭐ Part 1 — Double Repetition Only

### Invalid ID Rule  
An ID is invalid if it consists of some digit sequence repeated **exactly twice**:

Examples:
- `55` → `"5"` repeated twice  
- `6464` → `"64"` repeated twice  
- `123123` → `"123"` repeated twice  

Constraints:
- No leading zeroes  
- Only **even-length** IDs can match this rule

### Approach  
For each range we should:

1. Determine the digit lengths present.  
2. For each even length `d`:
   - Let `h = d / 2`  
   - Generate all base strings `S` of length `h` (first digit cannot be 0)  
   - Form `N = int(S + S)`  
3. Keep `N` if it lies in `[L, R]`  
4. Sum all invalid IDs across all ranges

This avoids brute-forcing the entire numeric interval.

---

## ⭐⭐ Part 2 — Any Repetition ≥ 2

### Updated Invalid ID Rule  
An ID is invalid if it consists of **any digit block** `S` repeated  
**k times**, where **k ≥ 2**.

Examples:
- `12341234` → `"1234"` × 2  
- `123123123` → `"123"` × 3  
- `1212121212` → `"12"` × 5  
- `1111111` → `"1"` × 7  

Now *odd and even* lengths are valid, and some IDs have multiple valid decompositions.

### Approach  
For each digit length `d` in the range:

1. For each divisor `k ≥ 2` of `d`:  
   - Compute `block_len = d / k`  
2. Generate all base blocks `S` of length `block_len`  
   - No leading zeroes allowed  
3. Form `N = int(S * k)`  
4. Keep `N` if `L ≤ N ≤ R`  

We use a **set** to avoid duplicates (e.g. `111111` matches multiple patterns).

Finally, we can sum all invalid IDs across all ranges to get the result.

---
