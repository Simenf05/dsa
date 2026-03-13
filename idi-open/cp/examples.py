"""Example problem solutions (easy) using the toolkit.

These are not contest problems themselves, but demonstrate how to apply the
library for typical easy/intro problems.
"""

from typing import List, Tuple

from cp.ds import FenwickTree, UnionFind
from cp.dp import longest_increasing_subsequence
from cp.graph import bfs, connected_components, dijkstra
from cp.math import modpow, sieve


def two_sum(nums: List[int], target: int) -> Tuple[int, int]:
    """Find any two indices i,j with nums[i]+nums[j]==target."""
    seen = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in seen:
            return seen[need], i
        seen[x] = i
    raise ValueError("No solution")


def count_components(n: int, edges: List[Tuple[int, int]]) -> int:
    """Count connected components in an undirected graph."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return len(connected_components(adj))


def shortest_path_grid(grid: List[str]) -> int:
    """Shortest path in a grid from top-left to bottom-right (4-dir)."""
    n = len(grid)
    m = len(grid[0])
    start = (0, 0)
    goal = (n - 1, m - 1)
    q = [start]
    dist = {start: 0}
    while q:
        x, y = q.pop(0)
        if (x, y) == goal:
            return dist[(x, y)]
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
                if (nx, ny) not in dist:
                    dist[(nx, ny)] = dist[(x, y)] + 1
                    q.append((nx, ny))
    return -1


def use_fenwick(arr: List[int]) -> List[int]:
    """Compute prefix sums using Fenwick tree."""
    fw = FenwickTree(len(arr))
    for i, v in enumerate(arr):
        fw.add(i, v)
    return [fw.sum(i) for i in range(len(arr))]


def prime_sieve_example(n: int) -> List[int]:
    """List primes <= n."""
    return sieve(n)


def modpow_example(a: int, b: int, mod: int) -> int:
    """Compute a^b mod mod."""
    return modpow(a, b, mod)


if __name__ == "__main__":
    print("two_sum([2,7,11,15], 9) ->", two_sum([2, 7, 11, 15], 9))
    print("count_components(5, [(0,1),(1,2),(3,4)]) ->", count_components(5, [(0, 1), (1, 2), (3, 4)]))
    print("LIS of [3,1,4,1,5,9] ->", longest_increasing_subsequence([3, 1, 4, 1, 5, 9]))
    print("Fenwick prefix sums of [1,2,3,4] ->", use_fenwick([1, 2, 3, 4]))
    print("Primes <= 20 ->", prime_sieve_example(20))
    print("modpow(2, 10, 1000) ->", modpow_example(2, 10, 1000))
