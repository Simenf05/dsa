#!/usr/bin/env python3
"""Easy problem: count connected components in an undirected graph.

Input format:
- n m
- m lines with u v (0-indexed or 1-indexed, both supported)

Output: number of connected components.
"""

import sys

from cp.easy.problems import count_components


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > n or v > n:
            # assume 1-based
            u -= 1
            v -= 1
        edges.append((u, v))

    print(count_components(n, edges))


if __name__ == "__main__":
    main()
