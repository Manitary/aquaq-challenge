import csv
from collections import defaultdict

from utils import get_input, submit


def bfs(graph: dict[str, list[tuple[str, int]]], start: str, end: str) -> int:
    queue: list[tuple[str, int]] = [(start, 0)]
    visited: set[str] = set()
    while queue:
        curr, amount = queue.pop(0)
        if curr == end:
            return amount
        if curr in visited:
            continue
        visited.add(curr)
        for target, cost in graph[curr]:
            if target in visited:
                continue
            queue.append((target, amount + cost))
        queue.sort(key=lambda x: x[1])
    raise ValueError("No path connecting the given nodes")


def main() -> int:
    data = csv.DictReader(get_input(10).split("\n"))
    network: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for row in data:
        network[row["s"]].append((row["d"], int(row["c"])))
    for v in network.values():
        v = sorted(v, key=lambda x: x[1])
    return bfs(network, "TUPAC", "DIDDY")


if __name__ == "__main__":
    ANSWER = main()
    print(f"Answer: {ANSWER}")
    submit(10, ANSWER)
