"""Easy problem functions (callable, reusable)."""

from typing import List, Tuple


def sort_numbers(arr: List[int]) -> List[int]:
    """Sort a list of integers."""
    return sorted(arr)


def binary_search(arr: List[int], x: int) -> int:
    """Binary search on a sorted list. Returns index or -1."""
    lo = 0
    hi = len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def count_components(n: int, edges: List[Tuple[int, int]]) -> int:
    """Count connected components in an undirected graph."""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    seen = [False] * n
    comps = 0
    for i in range(n):
        if not seen[i]:
            comps += 1
            stack = [i]
            seen[i] = True
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
    return comps
