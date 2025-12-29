import re
from collections import deque
from typing import List, Tuple

Machine = Tuple[List[int], List[List[int]], List[int]]

def read_input(path: str = "input.txt") -> List[Machine]:
    machines: List[Machine] = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            lights_str = re.search(r"\[(.*?)]", line).group(1)
            buttons_str = re.findall(r"\((.*?)\)", line)
            joltages_match = re.search(r"\{(.*?)}", line)
            if joltages_match:
                joltages_str = joltages_match.group(1)
                joltages = [int(x) for x in joltages_str.split(",")]
            else:
                joltages = []

            lights = [1 if c == '#' else 0 for c in lights_str]

            buttons = []
            for b in buttons_str:
                if b.strip() == "":
                    buttons.append([])
                else:
                    buttons.append([int(x) for x in b.split(",")])
            machines.append((lights, buttons, joltages))
    return machines


def min_presses_for_machine(lights: List[int], buttons: List[List[int]]) -> int:
    target = 0
    for i, v in enumerate(lights):
        if v == 1:
            target |= 1 << i

    if target == 0:
        return 0

    button_masks: List[int] = []
    for b in buttons:
        mask = 0
        for idx in b:
            mask |= 1 << idx
        button_masks.append(mask)

    if not button_masks:
        raise ValueError("Target not reachable: no buttons for this machine")

    start = 0
    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        state, dist = queue.popleft()

        for bm in button_masks:
            new_state = state ^ bm
            if new_state == target:
                return dist + 1
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, dist + 1))

    raise ValueError("Target configuration unreachable for this machine")

if __name__ == "__main__":
    machines = read_input()
    total_presses = 0

    for lights, buttons, joltages in machines:
        presses = min_presses_for_machine(lights, buttons)
        total_presses += presses

    print(total_presses)