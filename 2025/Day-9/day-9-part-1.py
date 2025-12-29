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


def max_rectangle_area(points: List[Point]) -> int:
    n = len(points)
    max_area = 0

    for i in range(n):
        for j in range(i + 1, n):
            area = rectangle_area(points[i], points[j])
            if area > max_area:
                max_area = area

    return max_area


if __name__ == "__main__":
    pts = read_points()
    answer = max_rectangle_area(pts)
    print(answer)
