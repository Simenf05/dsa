#!/usr/bin/python3
# coding=utf-8

from collections import deque
from typing import List, Optional, Tuple

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

def max_flow(
    source: int, sink: int, nodes: int, capacities: List[List[int]]
) -> Tuple[List[List[int]], int]:
    flows = [[0] * nodes for _ in range(nodes)]

    path = find_augmenting_path(source, sink, nodes, flows, capacities)
    total_flow = 0

    while path != None:
        flow = max_path_flow(path, flows, capacities)
        send_flow(path, flow, flows)
        total_flow += flow

        path = find_augmenting_path(source, sink, nodes, flows, capacities)

    return flows, total_flow


# Hjelpefunksjoner
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
        """Lager en sti fra foreldrelisten"""
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
    return int(flow)


def send_flow(path: List[int], flow: int, flows: List[List[int]]):
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
        [
            [0, 12, 11, 0, 0, 0],
            [-12, 0, 0, 12, 0, 0],
            [-11, 0, 0, 0, 11, 0],
            [0, -12, 0, 0, -7, 19],
            [0, 0, -11, 7, 0, 4],
            [0, 0, 0, -19, -4, 0],
        ],
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
        [
            [0, 12, 12, 0, 0, 0],
            [-12, 0, 0, 12, 0, 0],
            [-12, 0, 0, 8, 4, 0],
            [0, -12, -8, 0, 0, 20],
            [0, 0, -4, 0, 0, 4],
            [0, 0, 0, -20, -4, 0],
        ],
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
        [
            [0, 12, 12, 0, 0, 0],
            [-12, 0, 0, 12, 0, 0],
            [-12, 0, 0, 7, 5, 0],
            [0, -12, -7, 0, -1, 20],
            [0, 0, -5, 1, 0, 4],
            [0, 0, 0, -20, -4, 0],
        ],
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
        [
            [0, 1, 1, 1, 1],
            [-1, 0, 0, 0, 1],
            [-1, 0, 0, 0, 1],
            [-1, 0, 0, 0, 1],
            [-1, -1, -1, -1, 0],
        ],
    ),
]

failed = False

def format_2d_table(table):
    if type(table) != list:
        return str(table)
    return "\n".join(", ".join(map(str, row)) for row in table)

def format_input(source, sink, nodes, capacities):
    return f"""
Kilde: {source}
Sluk: {sink}
Antall noder: {nodes}
Kapasiteter:
{format_2d_table(capacities)}

"""

for test_case in tests:
    (
        source,
        sink,
        nodes,
        capacities,
        answer_flow,
        answer_flows,
    ) = test_case
    try:
        student_flows, student_flow = max_flow(
            source, sink, nodes, capacities
        )
    except TypeError:
        failed = True
        student_answer = max_flow(source, sink, nodes, capacities)
        print(
            f"Koden feilet for følgende input: {format_input(*test_case[:4])}"
            + f"Forventet svar:\n({answer_flow}, {answer_flows})\n\n"
            + f"Ditt svar:\n{student_answer}"
        )
        break
    if student_flow != answer_flow:
        failed = True
        print(
            f"Koden feilet for følgende input: {format_input(*test_case[:4])}"
            + f"Din flyt: {student_flow}\nRiktig maksflyt: {answer_flow}"
        )
        break
    if student_flows != answer_flows:
        failed = True
        print(
            f"Koden feilet for følgende input: {format_input(*test_case[:4])}"
            + f"Ditt flytnett:\n{format_2d_table(student_flows)}\n\n"
            + f"Riktig flytnett:\n{format_2d_table(answer_flows)}"
        )
        break

if not failed:
    print("Koden fungerte for alle eksempeltestene.")
