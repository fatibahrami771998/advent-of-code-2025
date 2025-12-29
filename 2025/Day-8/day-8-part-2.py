from __future__ import annotations

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

    def union(self, a: int, b: int) -> bool:
        """Union two sets. Return True only if a merge happened."""
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra

        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True


def last_connection_product(points: List[Point3D]) -> int:
    n = len(points)
    edges = build_edges(points)
    uf = UnionFind(n)

    num_components = n
    last_i = last_j = 0

    for _, i, j in edges:
        if uf.union(i, j):
            num_components -= 1
            last_i, last_j = i, j
            if num_components == 1:
                break

    x1, _, _ = points[last_i]
    x2, _, _ = points[last_j]
    return x1 * x2


if __name__ == "__main__":
    pts = read_points()
    answer = last_connection_product(pts)
    print(answer)
