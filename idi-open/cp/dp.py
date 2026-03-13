"""Dynamic programming templates and common patterns."""

from functools import lru_cache
from typing import List, Tuple


def knapsack_01(weights: List[int], values: List[int], W: int) -> int:
    """0/1 knapsack (O(nW))."""
    n = len(weights)
    dp = [0] * (W + 1)
    for i in range(n):
        w, v = weights[i], values[i]
        for cap in range(W, w - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - w] + v)
    return dp[W]


def longest_increasing_subsequence(arr: List[int]) -> int:
    """O(n log n) LIS length."""
    import bisect

    dp = []
    for x in arr:
        i = bisect.bisect_left(dp, x)
        if i == len(dp):
            dp.append(x)
        else:
            dp[i] = x
    return len(dp)


def bitmask_dp(n: int, cost: List[List[int]]) -> int:
    """Held-Karp TSP DP template (O(n^2 2^n))."""
    ALL = 1 << n
    dp = [[float("inf")] * n for _ in range(ALL)]
    dp[1][0] = 0
    for mask in range(1, ALL):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):
                    continue
                dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + cost[u][v])
    return min(dp[ALL - 1][i] + cost[i][0] for i in range(n))


def tree_dp(root: int, adj: List[List[int]], values: List[int]):
    """Simple tree DP example: max independent set."""
    n = len(adj)
    dp0 = [0] * n
    dp1 = [0] * n

    def dfs(u: int, p: int):
        dp0[u] = 0
        dp1[u] = values[u]
        for v in adj[u]:
            if v == p:
                continue
            dfs(v, u)
            dp0[u] += max(dp0[v], dp1[v])
            dp1[u] += dp0[v]

    dfs(root, -1)
    return max(dp0[root], dp1[root])


def memoized(fn):
    """Simple memoization decorator (top-down DP)."""

    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        res = fn(*args)
        cache[args] = res
        return res

    return wrapper


def digit_dp(n: int, digits: List[int]):
    """Template for digit DP. Use to count numbers with constraints."""

    @lru_cache(None)
    def dfs(pos: int, tight: bool, leading: bool) -> int:
        if pos == len(digits):
            return 1
        limit = digits[pos] if tight else 9
        res = 0
        for d in range(limit + 1):
            nt = tight and (d == limit)
            nl = leading and (d == 0)
            res += dfs(pos + 1, nt, nl)
        return res

    return dfs(0, True, True)
