from __future__ import annotations

from typing import List, Tuple

Point = Tuple[int, int]


def read_points(path: str = "input.txt") -> List[Point]:
    points: List[Point] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            x_str, y_str = line.split(",")
            x = int(x_str)
            y = int(y_str)
            points.append((x, y))
    return points


def rectangle_area(p1: Point, p2: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    width = abs(x1 - x2) + 1
    height = abs(y1 - y2) + 1
    return width * height


def rectangle_is_valid(p1: Point, p2: Point, poly: List[Point]) -> bool:
    x1, y1 = p1
    x2, y2 = p2

    x_min = min(x1, x2)
    x_max = max(x1, x2)
    y_min = min(y1, y2)
    y_max = max(y1, y2)

    n = len(poly)

    for i in range(n):
        lx, ly = poly[i]
        lx2, ly2 = poly[(i + 1) % n]

        if (
            max(lx, lx2) <= x_min
            or min(lx, lx2) >= x_max
            or max(ly, ly2) <= y_min
            or min(ly, ly2) >= y_max
        ):
            continue

        return False

    return True


def max_rectangle_area_part2(points: List[Point]) -> int:
    n = len(points)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]

            area = rectangle_area(p1, p2)
            if area <= max_area:
                continue

            if rectangle_is_valid(p1, p2, points):
                max_area = area

    return max_area


if __name__ == "__main__":
    red_points = read_points()
    answer = max_rectangle_area_part2(red_points)
    print(answer)
