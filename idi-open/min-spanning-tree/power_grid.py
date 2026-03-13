#!/usr/bin/python3
# coding=utf-8
from itertools import combinations
import random

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = True
# Antall tilfeldige tester som genereres.
random_tests = 20
# Laveste mulige antall trafokiosker i generert instans.
substations_lower = 3
# Høyest mulig antall trafokiosker generert instans.
# NB: Om dette antallet settes høyt (>8) vil det ta veldig lang tid å kjøre
# testene, da svaret på instansene finnes ved bruteforce.
substations_upper = 8
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


def calc_distance(station1, station2):
    distance = 0
    distance += abs(station1[0] - station2[0])
    distance += abs(station1[1] - station2[1])
    return distance

class DisjointStructure:
    def __init__(self):
        self.map = {}

    def make_set(self, str1):
        self.map[str1] = str1
    
    def find_set(self, str1):
        parent = self.map[str1]
        if str1 == parent:
            return parent
        new_parent = self.find_set(parent)
        self.map[str1] = new_parent
        return new_parent
    
    def union(self, str1, str2):
        parent_str1 = self.find_set(str1)
        parent_str2 = self.find_set(str2)
        self.map[parent_str1] = parent_str2

def power_grid(m, n, substations):

    for sx, sy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:

        sorted_stations = sorted(
            [(sx * x + sy * y, i, (x, y)) for i, (x, y) in enumerate(substations)]
        )
        print(sorted_stations)

    exit()

    ne_distance_from_origo = list(map(lambda station: station[0] + station[1], substations))
    nw_distance_from_origo = list(map(lambda station: -station[0] + station[1], substations))
    se_distance_from_origo = list(map(lambda station: station[0] - station[1], substations))
    sw_distance_from_origo = list(map(lambda station: -station[0] + station[1], substations))

    edges = set()
    for i, distance in enumerate(ne_distance_from_origo[:-1]):
        edges.add((i, i+1, distance))
    for i, distance in enumerate(nw_distance_from_origo[:-1]):
        edges.add((i, i+1, distance))
    for i, distance in enumerate(se_distance_from_origo[:-1]):
        edges.add((i, i+1, distance))
    for i, distance in enumerate(sw_distance_from_origo[:-1]):
        edges.add((i, i+1, distance))

    kruskal_set = DisjointStructure()
    for vert in range(len(substations)):
        kruskal_set.make_set(vert)


    total_len = 0
    edges = sorted(edges, key=lambda edge: edge[2])

    for edge in edges:
        if kruskal_set.find_set(edge[0]) != kruskal_set.find_set(edge[1]):
            total_len += edge[2]
            kruskal_set.union(edge[0], edge[1])

    return total_len


# Hardkodete instanser på format: (m, n, substations)
tests = [
    (3, 3, [(0, 1), (0, 2), (1, 2), (2, 1)]),
    (2, 2, [(1, 1)]),
    (2, 2, [(0, 0), (1, 1)]),
    (2, 2, [(0, 0), (0, 1), (1, 0)]),
    (2, 2, [(0, 0), (0, 1), (1, 0), (1, 1)]),
    (3, 3, [(0, 2), (2, 0)]),
    (3, 3, [(0, 0), (1, 1), (2, 2)]),
    (3, 3, [(1, 1), (0, 1), (2, 1)]),
    (3, 3, [(1, 2)]),
    (3, 3, [(2, 0), (1, 1), (0, 1)]),
    (2, 3, [(1, 1)]),
    (2, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]),
    (2, 2, [(0, 1), (1, 0), (1, 1), (0, 0)]),
    (3, 3, [(0, 1), (0, 2), (2, 1), (2, 2)]),
    (2, 3, [(1, 0), (1, 1), (0, 2)]),
    (2, 3, [(1, 0)]),
    (3, 2, [(1, 0), (2, 1), (0, 0)]),
    (3, 3, [(0, 1), (1, 1), (2, 1), (0, 0)]),
    (3, 3, [(0, 2)]),
]


def gen_examples(substations_lower, substations_upper, k):
    for _ in range(k):
        n, m = random.randint(3, 50), random.randint(3, 50)
        s = random.randint(substations_lower, min(substations_upper, n * m))
        substations = set()
        while len(substations) < s:
            substations.add((
                random.randint(0, m - 1),
                random.randint(0, n - 1)
            ))
        substations = list(substations)

        yield (m, n, substations)

def get_answer(m, n, substations):
    # Finner løsningen på problemet ved bruteforce.
    # NB: Bruker minst noen minutter hvis det er 10+ substations
    s = len(substations)
    if s <= 1:
        return 0

    E = [(i, j) for i in range(0, s - 1) for j in range(i + 1, s)]
    def visit(S, v, ST):
        if v in S:
            return
        S.add(v)
        for (a, b) in ST:
            if a == v:
                visit(S, b, ST)
            if b == v:
                visit(S, a, ST)

    solution = float("inf")
    for ST in combinations(E, s - 1):
        S = set()
        visit(S, 0, ST)
        if len(S) != s:
            continue

        answer = 0
        for (a, b) in ST:
            answer += max(substations[a][0], substations[b][0])
            answer -= min(substations[a][0], substations[b][0])
            answer += max(substations[a][1], substations[b][1])
            answer -= min(substations[a][1], substations[b][1])
        if answer < solution:
            solution = answer

    return solution

if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        substations_lower,
        substations_upper,
        random_tests
    ))

failed = False
for m, n, substations in tests:
    answer = get_answer(m, n, substations)
    student = power_grid(m, n, substations)
    if student != answer:
        if failed:
            print("-"*50)
        failed = True

        print(f"""
Koden feilet for følgende instans:
m: {m}
n: {n}
substations: {', '.join(map(str, substations))}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")

