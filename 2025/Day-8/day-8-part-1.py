from __future__ import annotations

from collections import Counter
from typing import List, Tuple

Point3D = Tuple[int, int, int]
Edge = Tuple[int, int, int]


def read_points(path: str = "input.txt") -> List[Point3D]:
    points: List[Point3D] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str, z_str = line.split(",")
            x = int(x_str)
            y = int(y_str)
            z = int(z_str)
            points.append((x, y, z))
    return points


def build_edges(points: List[Point3D]) -> List[Edge]:
    edges: List[Edge] = []
    n = len(points)

    for i in range(n):
        x1, y1, z1 = points[i]
        for j in range(i + 1, n):
            x2, y2, z2 = points[j]
            dx = x2 - x1
            dy = y2 - y1
            dz = z2 - z1
            d2 = dx * dx + dy * dy + dz * dz
            edges.append((d2, i, j))

    edges.sort(key=lambda e: e[0])
    return edges


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent: List[int] = list(range(n))
        self.size: List[int] = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]


def max_three_circuit_product(points: List[Point3D], num_connections: int = 1000) -> int:
    n = len(points)
    edges = build_edges(points)
    uf = UnionFind(n)

    for idx, (_, i, j) in enumerate(edges):
        if idx >= num_connections:
            break
        uf.union(i, j)

    counts: Counter[int] = Counter()
    for i in range(n):
        root = uf.find(i)
        counts[root] += 1

    circuit_sizes = sorted(counts.values(), reverse=True)
    a, b, c = circuit_sizes[:3]
    return a * b * c


if __name__ == "__main__":
    pts = read_points()
    answer = max_three_circuit_product(pts)
    print(answer)
