from typing import Dict, List, Tuple
import re

ShapeRows = List[str]
ShapesDict = Dict[int, ShapeRows]
Region = Tuple[int, int, List[int]]


def parse_input(path: str = "input.txt") -> Tuple[ShapesDict, List[Region]]:
    with open(path) as f:
        lines = [line.rstrip("\n") for line in f]

    shapes: ShapesDict = {}
    regions: List[Region] = []

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        if re.match(r"^\d+x\d+:\s*", line):
            break

        m = re.match(r"^(\d+):\s*$", line)
        if not m:
            raise ValueError(f"Unexpected line in shapes section: {line}")
        idx = int(m.group(1))
        i += 1

        rows: List[str] = []
        while i < n:
            row_line = lines[i].strip()
            if not row_line:
                i += 1
                break
            if re.match(r"^\d+:\s*$", row_line):
                break
            if re.match(r"^\d+x\d+:\s*", row_line):
                break
            rows.append(row_line)
            i += 1

        shapes[idx] = rows

    while i < n:
        line = lines[i].strip()
        i += 1
        if not line:
            continue
        m = re.match(r"^(\d+)x(\d+):\s*(.*)$", line)
        if not m:
            raise ValueError(f"Unexpected line in regions section: {line}")
        w = int(m.group(1))
        h = int(m.group(2))
        rest = m.group(3).strip()
        if rest:
            counts = [int(x) for x in rest.split()]
        else:
            counts = []
        regions.append((w, h, counts))

    return shapes, regions


def count_fittable_regions(path: str = "input.txt") -> int:
    shapes, regions = parse_input(path)

    shape_areas: Dict[int, int] = {}
    for idx, rows in shapes.items():
        area = sum(row.count("#") for row in rows)
        shape_areas[idx] = area

    max_shape_idx = max(shapes.keys())

    total_ok = 0

    for (w, h, counts) in regions:
        if len(counts) <= max_shape_idx:
            counts = counts + [0] * (max_shape_idx + 1 - len(counts))

        region_area = w * h
        needed_area = 0
        for i in range(max_shape_idx + 1):
            needed_area += shape_areas[i] * counts[i]

        if needed_area <= region_area:
            total_ok += 1

    return total_ok


if __name__ == "__main__":
    print(count_fittable_regions("input.txt"))
