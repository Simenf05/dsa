#!/usr/bin/python3
# coding=utf-8

from collections import deque
from typing import List, Optional, Tuple


class Dinic:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.level = [0] * n
        self.it = [0] * n

    class Edge:
        __slots__ = ("v", "cap", "rev")
        def __init__(self, v, cap, rev):
            self.v = v
            self.cap = cap
            self.rev = rev

    def add_edge(self, u, v, c):
        forward = self.Edge(v, c, None)
        backward = self.Edge(u, 0, forward)
        forward.rev = backward
        self.adj[u].append(forward)
        self.adj[v].append(backward)

    # BFS WITHOUT deque (list + pointer)
    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0

        q = [s]      # queue list
        qi = 0        # queue index pointer

        while qi < len(q):
            u = q[qi]
            qi += 1

            for e in self.adj[u]:
                if e.cap > 0 and self.level[e.v] == -1:
                    self.level[e.v] = self.level[u] + 1
                    q.append(e.v)

        return self.level[t] != -1

    # DFS blocking flow
    def dfs(self, u, t, f):
        if u == t:
            return f
        for i in range(self.it[u], len(self.adj[u])):
            self.it[u] = i
            e = self.adj[u][i]
            if e.cap > 0 and self.level[e.v] == self.level[u] + 1:
                pushed = self.dfs(e.v, t, min(f, e.cap))
                if pushed:
                    e.cap -= pushed
                    e.rev.cap += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        flow = 0
        INF = 10**18
        while self.bfs(s, t):
            self.it = [0] * self.n
            pushed = self.dfs(s, t, INF)
            while pushed:
                flow += pushed
                pushed = self.dfs(s, t, INF)
        return flow


def max_flow_highscore(source, sink, nodes, capacities):
    dinic = Dinic(nodes)

    # Add all edges (capacity > 0)
    for u in range(nodes):
        for v in range(nodes):
            c = capacities[u][v]
            if c > 0:
                dinic.add_edge(u, v, c)

    return dinic.max_flow(source, sink)

# def max_flow_highscore(source, sink, nodes, capacities):
#     flows = [[0] * nodes for _ in range(nodes)]
# 
#     path = find_augmenting_path(source, sink, nodes, flows, capacities)
#     total_flow = 0
# 
#     while path != None:
#         flow = max_path_flow(path, flows, capacities)
#         send_flow(path, flow, flows)
#         total_flow += flow
# 
#         path = find_augmenting_path(source, sink, nodes, flows, capacities)
# 
#     return total_flow


# Hjelpefunksjoner du kan bruke
def find_augmenting_path(
    source: int,
    sink: int,
    nodes: int,
    flows: List[List[int]],
    capacities: List[List[int]],
) -> Optional[List[int]]:
    """
    Finn en forøkende sti i et flytnett

    :param source: indeksen til kilden i listen med noder.
    :param sink: indeksen til sluknoden i listen med noder.
    :param nodes: antaller noder i nettverket
    :param flows: flyt-matrise, verdien på indeks (i,j) er flyten mellom node i og j
    :param capacities: kapasitets-matrise, verdien på indeks (i,j) er kapasiteten til kanten (i,j).
                        ingen kant tilsvarer kapasitet 0.
    :returns: en foreldre-liste med den flytforøkende stien hvis funnet, ellers None.
    """

    def create_path(source: int, sink: int, parent: List[int]) -> List[int]:
        """Lager stien ved hjelp av foreldrelisten"""
        node = sink
        path = [sink]
        while node != source:
            node = parent[node]
            path.append(node)
        path.reverse()
        return path

    discovered = [False] * nodes
    parent = [0] * nodes
    queue = deque()
    queue.append(source)

    while queue:
        node = queue.popleft()
        if node == sink:
            return create_path(source, sink, parent)

        for neighbour in range(nodes):
            if (
                not discovered[neighbour]
                and flows[node][neighbour] < capacities[node][neighbour]
            ):
                queue.append(neighbour)
                discovered[neighbour] = True
                parent[neighbour] = node
    return None


def max_path_flow(
    path: List[int], flows: List[List[int]], capacities: List[List[int]]
) -> int:
    """
    Finn maksimal flyt som kan sendes gjennom den oppgitte stien
    """
    flow = float("inf")
    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        flow = min(flow, capacities[u][v] - flows[u][v])
    return flow


def send_flow(path: List[int], flow: float, flows: List[List[float]]):
    """
    Oppdaterer "flows" ved å sende "flow" flyt gjennom stien "path"
    """
    for i in range(1, len(path)):
        u, v = path[i - 1], path[i]
        flows[u][v] += flow
        flows[v][u] -= flow


tests = [
    (
        0,
        5,
        6,
        [
            [0, 16, 13, 0, 0, 0],
            [0, 0, 0, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0],
        ],
        23,
    ),
    (
        0,
        5,
        6,
        [
            [0, 16, 13, 0, 0, 0],
            [16, 0, 4, 12, 0, 0],
            [13, 4, 0, 9, 14, 0],
            [0, 12, 9, 0, 7, 20],
            [0, 0, 14, 7, 0, 4],
            [0, 0, 0, 20, 4, 0],
        ],
        24,
    ),
    (
        0,
        5,
        6,
        [
            [0, 16, 13, 0, 0, 0],
            [16, 0, 4, 12, 0, 0],
            [13, 4, 0, 7, 14, 0],
            [0, 12, 7, 0, 1, 20],
            [0, 0, 14, 1, 0, 4],
            [0, 0, 0, 20, 4, 0],
        ],
        24,
    ),
    (
        0,
        4,
        5,
        [
            [0, 1, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1],
            [1, 1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 0],
        ],
        4,
    ),
]

failed = False

for test_case in tests:
    (
        source,
        sink,
        nodes,
        capacities,
        answer_flow,
    ) = test_case
    student_flow = max_flow_highscore(
        source, sink, nodes, capacities
    )
    if student_flow != answer_flow:
        failed = True
        response = "Koden feilet for følgende input: (tasks={:}). ".format(
            test_case[:4]
        ) + "Din flyt: {:}. Riktig maksflyt: {:}".format(
            student_flow, answer_flow
        )
        print(response)
        break

if not failed:
    print("Koden fungerte for alle eksempeltestene.")
