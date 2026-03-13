"""Advanced data structures and algorithms for high-level contest problems."""

from typing import Callable, List, Optional, Tuple


def mo_algorithm(queries: List[Tuple[int, int]], add: Callable[[int], None], remove: Callable[[int], None], get_answer: Callable[[], int]) -> List[int]:
    """Mo's algorithm template.

    queries: list of (l, r) inclusive ranges
    add: function to add an index
    remove: function to remove an index
    get_answer: function returning current answer
    """
    n = len(queries)
    if n == 0:
        return []
    block = int(len(queries) ** 0.5) or 1
    sorted_q = sorted(enumerate(queries), key=lambda x: (x[1][0] // block, x[1][1]))
    ans = [0] * n
    cur_l = 0
    cur_r = -1
    for idx, (l, r) in sorted_q:
        while cur_r < r:
            cur_r += 1
            add(cur_r)
        while cur_r > r:
            remove(cur_r)
            cur_r -= 1
        while cur_l < l:
            remove(cur_l)
            cur_l += 1
        while cur_l > l:
            cur_l -= 1
            add(cur_l)
        ans[idx] = get_answer()
    return ans


class HeavyLightDecomposition:
    """Simple HLD skeleton for path queries on trees."""

    def __init__(self, adj: List[List[int]], root: int = 0):
        self.n = len(adj)
        self.adj = adj
        self.parent = [-1] * self.n
        self.depth = [0] * self.n
        self.size = [1] * self.n
        self.head = [0] * self.n
        self.pos = [0] * self.n
        self.cur = 0

        self._dfs_size(root, -1)
        self._dfs_decompose(root, root)

    def _dfs_size(self, u: int, p: int) -> None:
        self.parent[u] = p
        self.size[u] = 1
        for v in self.adj[u]:
            if v == p:
                continue
            self.depth[v] = self.depth[u] + 1
            self._dfs_size(v, u)
            self.size[u] += self.size[v]

    def _dfs_decompose(self, u: int, h: int) -> None:
        self.head[u] = h
        self.pos[u] = self.cur
        self.cur += 1
        heavy = -1
        for v in self.adj[u]:
            if v == self.parent[u]:
                continue
            if heavy == -1 or self.size[v] > self.size[heavy]:
                heavy = v
        if heavy != -1:
            self._dfs_decompose(heavy, h)
        for v in self.adj[u]:
            if v == self.parent[u] or v == heavy:
                continue
            self._dfs_decompose(v, v)

    def query_path(self, u: int, v: int, query_segment: Callable[[int, int], int]) -> int:
        """Query on path u-v where query_segment(l,r) operates on pos[]."""
        res = 0
        while self.head[u] != self.head[v]:
            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                u, v = v, u
            res = max(res, query_segment(self.pos[self.head[v]], self.pos[v]))
            v = self.parent[self.head[v]]
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        res = max(res, query_segment(self.pos[u], self.pos[v]))
        return res
