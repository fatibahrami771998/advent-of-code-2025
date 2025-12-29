# 🎄 Advent of Code — Day 11  
Reactor Path Analysis

Each line of input describes a directed graph connection:

```
aaa: you hhh
bbb: ddd eee
```

The task is to analyze how data can flow through this graph.

---

## ⭐ Part 1 — Count all paths from `you` to `out`

Data flows only **forward** along device outputs. This means that the graph is **directed** and there is no **cycle**. 
We must count all distinct paths starting at `you` and ending at `out`.

### Approach
- Parse the graph: `device → list of outputs`.
- Run DFS to enumerate path counts.
- Memoize `paths(node)` to avoid recomputation (graph behaves as a DAG).

---

## ⭐ Part 2 — Paths that visit both `dac` and `fft`

Now we count only the paths from `svr` to `out` that pass through **both**:

- `dac`
- `fft`

Order does not matter.

### Approach
- Perform DFS from `svr`.
- Track two booleans during traversal: `seen_dac`, `seen_fft`.
- When reaching `out`, count the path only if both flags are true.
- Memoize on `(node, seen_dac, seen_fft)` for efficiency.

---

## 📌 Summary

- **Part 1:** Count all possible paths through a directed graph.  
- **Part 2:** Count only paths that include specific intermediate nodes.  
- DFS with memoization makes both parts efficient and clean.
