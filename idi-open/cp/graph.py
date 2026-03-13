"""Graph algorithms for competitive programming.

Key functions:
- dfs, bfs, connected_components, topological_sort
- dijkstra, bellman_ford, floyd_warshall
- kruskal, prim
- kosaraju, tarjan
- maxflow (Dinic), mincut (via maxflow)
- hopcroft_karp (bipartite matching)

This module uses 0-indexed vertices.
"""

import collections
import heapq
from typing import Dict, Iterable, List, Optional, Tuple

from cp.ds import UnionFind

Edge = Tuple[int, int, int]  # (u, v, w)

# ---------- Basic Traversals ----------

def dfs(adj: List[List[int]], start: int, visited=None):
    """Depth-first search (recursive)."""
    if visited is None:
        visited = set()
    visited.add(start)
    for nei in adj[start]:
        if nei not in visited:
            dfs(adj, nei, visited)
    return visited


def bfs(adj: List[List[int]], start: int):
    """Breadth-first search."""
    q = collections.deque([start])
    visited = {start}
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            if v not in visited:
                visited.add(v)
                q.append(v)
    return order


def connected_components(adj: List[List[int]]):
    """Return list of connected components (nodes are 0..n-1)."""
    n = len(adj)
    seen = [False] * n
    comps = []
    for i in range(n):
        if not seen[i]:
            comp = []
            stack = [i]
            seen[i] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for v in adj[u]:
                    if not seen[v]:
                        seen[v] = True
                        stack.append(v)
            comps.append(comp)
    return comps


def topological_sort(adj: List[List[int]]):
    """Kahn's algorithm. Returns list or [] if cycle exists."""
    n = len(adj)
    indeg = [0] * n
    for u in range(n):
        for v in adj[u]:
            indeg[v] += 1
    q = collections.deque([u for u in range(n) if indeg[u] == 0])
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == n else []


# ---------- Shortest paths ----------

def dijkstra(n: int, edges: Iterable[Edge], src: int):
    """Dijkstra's algorithm. Returns dist list and parent list."""
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        # if undirected: adj[v].append((u, w))
    dist = [float("inf")] * n
    parent = [-1] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in adj[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                parent[v] = u
                heapq.heappush(pq, (nd, v))
    return dist, parent


def bellman_ford(n: int, edges: Iterable[Edge], src: int):
    """Bellman-Ford. Returns (dist, parent) or raises ValueError on negative cycle."""
    dist = [float("inf")] * n
    parent = [-1] * n
    dist[src] = 0
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                updated = True
        if not updated:
            break
    # check negative cycle
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Negative weight cycle detected")
    return dist, parent


def floyd_warshall(n: int, weights: List[List[float]]):
    """All-pairs shortest paths. weights[u][v] = cost or inf."""
    dist = [row[:] for row in weights]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


# ---------- Minimum spanning tree ----------

def kruskal(n: int, edges: Iterable[Edge]):
    """Kruskal MST. edges = [(u,v,w), ...]."""
    uf = UnionFind(n)
    mst = []
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if uf.union(u, v):
            mst.append((u, v, w))
    return mst


def prim(n: int, adj: List[List[Tuple[int, int]]], src: int = 0):
    """Prim's MST. adj[u] = [(v,w), ...]"""
    seen = [False] * n
    dist = [float("inf")] * n
    parent = [-1] * n
    dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if seen[u]:
            continue
        seen[u] = True
        for v, w in adj[u]:
            if not seen[v] and w < dist[v]:
                dist[v] = w
                parent[v] = u
                heapq.heappush(pq, (w, v))
    return parent, dist


# ---------- Strongly connected components ----------

def kosaraju(n: int, adj: List[List[int]]):
    """Kosaraju's SCC algorithm."""
    visited = [False] * n
    order = []

    def dfs1(u: int):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for u in range(n):
        if not visited[u]:
            dfs1(u)

    radj = [[] for _ in range(n)]
    for u in range(n):
        for v in adj[u]:
            radj[v].append(u)

    comp = [-1] * n
    cid = 0

    def dfs2(u: int):
        comp[u] = cid
        for v in radj[u]:
            if comp[v] == -1:
                dfs2(v)

    for u in reversed(order):
        if comp[u] == -1:
            dfs2(u)
            cid += 1

    return comp


def tarjan_scc(n: int, adj: List[List[int]]):
    """Tarjan's strongly connected components."""
    index = 0
    stack = []
    onstack = [False] * n
    indices = [-1] * n
    lowlink = [0] * n
    comps = []

    def strongconnect(v: int):
        nonlocal index
        indices[v] = index
        lowlink[v] = index
        index += 1
        stack.append(v)
        onstack[v] = True

        for w in adj[v]:
            if indices[w] == -1:
                strongconnect(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif onstack[w]:
                lowlink[v] = min(lowlink[v], indices[w])

        if lowlink[v] == indices[v]:
            comp = []
            while True:
                w = stack.pop()
                onstack[w] = False
                comp.append(w)
                if w == v:
                    break
            comps.append(comp)

    for v in range(n):
        if indices[v] == -1:
            strongconnect(v)
    return comps


# ---------- Max Flow (Dinic) ----------

class Dinic:
    def __init__(self, n: int):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def max_flow(self, s: int, t: int):
        flow = 0
        while True:
            level = [-1] * self.n
            q = collections.deque([s])
            level[s] = 0
            while q:
                u = q.popleft()
                for v, cap, _ in self.adj[u]:
                    if cap > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                break
            it = [0] * self.n

            def dfs(u: int, f: int):
                if u == t:
                    return f
                for i in range(it[u], len(self.adj[u])):
                    v, cap, rev = self.adj[u][i]
                    if cap > 0 and level[v] == level[u] + 1:
                        ret = dfs(v, min(f, cap))
                        if ret > 0:
                            self.adj[u][i][1] -= ret
                            self.adj[v][rev][1] += ret
                            return ret
                    it[u] += 1
                return 0

            while True:
                pushed = dfs(s, 10**18)
                if pushed == 0:
                    break
                flow += pushed
        return flow

    def min_cut(self, s: int):
        """Return set of vertices reachable from s in residual graph."""
        visited = [False] * self.n
        stack = [s]
        visited[s] = True
        while stack:
            u = stack.pop()
            for v, cap, _ in self.adj[u]:
                if cap > 0 and not visited[v]:
                    visited[v] = True
                    stack.append(v)
        return visited


class EdmondsKarp:
    """Ford–Fulkerson using BFS (Edmonds–Karp)."""

    def __init__(self, n: int):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int):
        self.adj[u].append([v, cap, len(self.adj[v])])
        self.adj[v].append([u, 0, len(self.adj[u]) - 1])

    def max_flow(self, s: int, t: int):
        flow = 0
        while True:
            parent = [(-1, -1)] * self.n
            q = collections.deque([s])
            parent[s] = (s, -1)
            while q and parent[t][0] == -1:
                u = q.popleft()
                for i, (v, cap, rev) in enumerate(self.adj[u]):
                    if cap > 0 and parent[v][0] == -1:
                        parent[v] = (u, i)
                        q.append(v)
                        if v == t:
                            break
            if parent[t][0] == -1:
                break

            # find min residual on path
            v = t
            f = float('inf')
            while v != s:
                u, ei = parent[v]
                f = min(f, self.adj[u][ei][1])
                v = u
            # augment
            v = t
            while v != s:
                u, ei = parent[v]
                self.adj[u][ei][1] -= f
                rev = self.adj[u][ei][2]
                rv = self.adj[v][rev]
                rv[1] += f
                v = u
            flow += f
        return flow


# ---------- Bipartite Matching (Hopcroft–Karp) ----------

def hopcroft_karp(adj: List[List[int]], n_left: int, n_right: int):
    """adj[u] = list of right-side vertices connected to left vertex u."""
    INF = 10**18
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right
    dist = [0] * n_left

    def bfs():
        q = collections.deque()
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        d = INF
        while q:
            u = q.popleft()
            if dist[u] < d:
                for v in adj[u]:
                    if pair_v[v] == -1:
                        d = dist[u] + 1
                    else:
                        if dist[pair_v[v]] == INF:
                            dist[pair_v[v]] = dist[u] + 1
                            q.append(pair_v[v])
        return d != INF

    def dfs(u: int):
        for v in adj[u]:
            if pair_v[v] == -1 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n_left):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u, pair_v
