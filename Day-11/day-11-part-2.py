from typing import Dict, List, Tuple

Graph = Dict[str, List[str]]


def read_input(path: str = "input.txt") -> Graph:
    graph: Graph = {}
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, connections_str = line.split(":")
            label = label.strip()
            connections: List[str] = connections_str.strip().split()
            graph[label] = connections
    return graph


def count_paths_with_both(graph: Graph, start: str, target: str, must1: str, must2: str) -> int:
    memo: Dict[Tuple[str, bool, bool], int] = {}

    def dfs(node: str, seen1: bool, seen2: bool) -> int:
        seen1 = seen1 or (node == must1)
        seen2 = seen2 or (node == must2)

        key = (node, seen1, seen2)
        if key in memo:
            return memo[key]

        if node == target:
            memo[key] = 1 if (seen1 and seen2) else 0
            return memo[key]

        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt, seen1, seen2)

        memo[key] = total
        return total

    return dfs(start, False, False)


if __name__ == "__main__":
    graph = read_input()
    count = count_paths_with_both(graph, "svr", "out", "dac", "fft")
    print(count)
