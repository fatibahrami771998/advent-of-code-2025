from typing import List, Tuple
import re
import z3

Machine = Tuple[List[int], List[List[int]], List[int]]


def read_input(path: str = "input.txt") -> List[Machine]:
    machines: List[Machine] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            lights_str = re.search(r"\[(.*?)]", line).group(1)
            lights = [1 if c == "#" else 0 for c in lights_str]

            button_strs = re.findall(r"\((.*?)\)", line)
            buttons: List[List[int]] = []
            for b in button_strs:
                if b.strip() == "":
                    buttons.append([])
                else:
                    buttons.append([int(x) for x in b.split(",")])

            m = re.search(r"\{(.*?)}", line)
            if m:
                joltages = [int(x) for x in m.group(1).split(",")]
            else:
                joltages = []

            machines.append((lights, buttons, joltages))

    return machines


def min_presses_part2(buttons: List[List[int]], target: List[int]) -> int:
    m = len(target)
    b = len(buttons)

    X = [z3.Int(f"b{i}") for i in range(b)]

    opt = z3.Optimize()

    for counter_idx in range(m):
        involved = []
        for j, btn in enumerate(buttons):
            if counter_idx in btn:
                involved.append(X[j])
        opt.add(sum(involved) == target[counter_idx])

    for x in X:
        opt.add(x >= 0)

    opt.minimize(sum(X))

    if opt.check() != z3.sat:
        raise ValueError("No solution found")

    model = opt.model()

    total = sum(model[x].as_long() for x in X)
    return total


if __name__ == "__main__":
    machines = read_input()
    total = 0
    for _lights, buttons, joltages in machines:
        if len(joltages) == 0:
            continue
        total += min_presses_part2(buttons, joltages)

    print(total)
