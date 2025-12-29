# 🎄 Advent of Code — Day 1  
Dial Rotation Passwords

## Part 1 — Counting Final Zero Positions
We are given a sequence of dial rotations (`Lk`, `Rk`).  
The dial starts at **50** and has values **0–99** arranged in a loop.

Each rotation:
- `Rk` → move forward **k** clicks  
- `Lk` → move backward **k** clicks  

**Part 1 asks:**  
How many rotations end with the dial pointing **exactly at 0**?

We update each final position using modular arithmetic and count the times `position == 0`.

---

## Part 2 — Counting All Zero Clicks
Under password method `0x434C49434B`, we must count **every individual click** that lands on 0 during a rotation.

During a rotation of `k` clicks, we should check all values of `t` where:

```
(position + step * t) % 100 == 0
```

Count all such `t` in `1 … k`.

This can be computed efficiently using modular math without simulating every click.

---

## Summary
- The dial is circular (`mod 100`).  
- **Part 1:** count only when a rotation *ends* on 0.  
- **Part 2:** count *all intermediate* clicks that land on 0.  
- Modular arithmetic provides a clean and efficient solution.
