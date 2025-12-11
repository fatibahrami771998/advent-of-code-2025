from turtledemo.penrose import start
from typing import List, Dict

Graph = Dict[str, List[str]]

def read_input() -> Graph:
    graph: Graph = {}
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            label, connections_str = line.split(":")
            connections: List[str] = connections_str.strip().split()
            graph[label] = connections
    return graph

def count_paths(graph: Graph, start: str, target: str) -> int:
    memo: Dict[int, int] = {}

    def dfs(node: str) -> int:
        if node == target:
            return 1
        if node in memo:
            return memo[node]

        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt)
        memo[node] = total
        return total
    return dfs(start)

if __name__ == "__main__":
    graph = read_input()
    paths = count_paths(graph, "you", "out")
    print(paths)