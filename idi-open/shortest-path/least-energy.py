#!/usr/bin/python3
# coding=utf-8
import random
import itertools
import math

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
random_tests = 100
# Lavest mulig antall reaksjoner i generert instans.
reactions_lower = 13
# Høyest mulig antall reaksjoner i generert instans. Om denne verdien er satt høyt
# (>25), kan det ta lang tid å generere instansene.
reactions_upper = 15
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

def relax(u, v, distance, weight, predecessor):
    if distance[u] + weight < distance[v]:
        distance[v] = distance[u] + weight
        predecessor[v] = u


def least_energy(reactions, start, goal, laws_of_thermodynamics=True):
    # Build distance and predecessor maps directly
    distance = {}
    predecessor = {}

    # Initialize all vertices lazily
    for u, v, _ in reactions:
        distance.setdefault(u, float("inf"))
        distance.setdefault(v, float("inf"))
        predecessor.setdefault(u, None)
        predecessor.setdefault(v, None)

    distance[start] = 0

    # Relax edges |V|-1 times
    for _ in range(len(distance) - 1):
        updated = False
        for u, v, w in reactions:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w
                predecessor[v] = u
                updated = True
        if not updated:  # Early exit if no updates — saves time
            break

    # Reconstruct path
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()

    return path

# Hardkodete tester på format: (reactions, start, goal), lavest mulig energi
tests = [
    (([("A", "B", 100), ("B", "C", -20), ("A", "C", 70)], "A", "C"), 70),
    (([("A", "B", 100)], "A", "B"), 100),
    (([("B", "A", -100)], "B", "A"), -100),
    (([("A", "B", 100), ("B", "A", -100)], "A", "B"), 100),
    (([("A", "B", 100), ("B", "A", -100)], "B", "A"), -100),
    (([("A", "B", 100), ("B", "C", -50), ("A", "C", 70)], "A", "C"), 50),
    (([("A", "B", 100), ("B", "C", -20), ("A", "C", 70)], "A", "C"), 70),
    (
        (
            [
                ("A", "C", -100),
                ("B", "C", -100),
                ("A", "C", -201),
                ("B", "A", 100),
            ],
            "A",
            "C",
        ),
        -201,
    ),
    (([("Y", "N", 11), ("N", "Y", -10)], "Y", "N"), 11),
    (
        (
            [
                ("E", "K", 68),
                ("F", "K", 21),
                ("K", "F", -21),
                ("F", "E", 50),
                ("K", "E", 10),
                ("E", "F", -1),
            ],
            "E",
            "F",
        ),
        -1,
    ),
    (
        (
            [("C", "V", 36), ("C", "B", 18), ("B", "C", -17), ("V", "B", 54)],
            "C",
            "B",
        ),
        18,
    ),
    (
        (
            [
                ("P", "G", 47),
                ("G", "T", 52),
                ("T", "P", 20),
                ("P", "T", -19),
                ("G", "P", 30),
            ],
            "T",
            "G",
        ),
        67,
    ),
    (
        (
            [
                ("F", "Y", 69),
                ("U", "F", 47),
                ("Y", "U", -5),
                ("Y", "F", 18),
                ("U", "Y", 6),
            ],
            "U",
            "Y",
        ),
        6,
    ),
    (
        (
            [
                ("K", "G", -27),
                ("A", "G", 52),
                ("G", "A", 18),
                ("K", "A", -17),
                ("A", "K", 17),
            ],
            "K",
            "A",
        ),
        -17,
    ),
    (
        (
            [
                ("X", "H", 2),
                ("X", "U", 48),
                ("H", "X", -1),
                ("U", "H", 41),
                ("H", "U", 36),
                ("U", "X", 49),
            ],
            "X",
            "U",
        ),
        38,
    ),
    (([("V", "L", 11), ("L", "V", -10)], "V", "L"), 11),
    (([("C", "W", 23), ("W", "C", -22)], "W", "C"), -22),
    (
        (
            [("K", "P", 30), ("I", "P", 21), ("I", "K", 19), ("P", "I", -20)],
            "P",
            "K",
        ),
        -1,
    ),
]


def bruteforce_solve(S, R, s, g):
    S.remove(s)
    S.remove(g)
    R = {(a, b): e for a, b, e in R}
    sol = float("inf")
    for i in range(0, len(S)):
        for perm in itertools.permutations(S, r=i):
            cost = 0
            perm = tuple([s]) + perm + tuple([g])
            for x, y in zip(perm, perm[1:]):
                if (x, y) not in R:
                    break
                cost += R[(x, y)]
            else:
                sol = min(sol, cost)
    return sol


def gen_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(max(1, nl), nu)
        ns = random.randint(
                max(5, math.ceil(1.2*math.ceil(math.sqrt(n)))),
                max(5, min(2*math.ceil(math.sqrt(n)), n))
            )
        substances = set()
        while len(substances) < ns:
            substances.add(
                "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                        k=math.ceil(math.log(ns, 20))))
            )
        substances = tuple(substances)

        R = dict()
        for _ in range(n):
            a, b = substances[:2]
            while (a, b) in R:
                a, b = random.sample(substances, k=2)

            R[(a, b)] = random.randint(-50, 99)

        for i in range(2, len(substances) + 1):
            for perm in itertools.permutations(substances, r=i):
                if all((a, b) in R for a, b in zip(perm, perm[1:] + perm[:1])):
                    e = sum(R[(a, b)] for a, b in zip(perm, perm[1:] + perm[:1]))
                    if e < 0:
                        R[(perm[0], perm[1])] += -e

        R = [(*x, e) for x, e in R.items()]
        random.shuffle(R)


        s, g = random.sample(substances, k=2)
        while bruteforce_solve(set(substances), R, s, g) == float("inf"):
            s, g = random.sample(substances, k=2)

        yield (R, s, g), bruteforce_solve(set(substances), R, s, g)



if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        reactions_lower,
        reactions_upper,
    ))


def get_feedback(student, answer, reactions, start, goal):
    if type(student) != list:
        return "Du returnerte ikke en liste"
    if len(student) < 2:
        return "Du returnerte en liste med færre en to elementer"
    if student[0] != start:
        return "Listen din starter ikke med startstoffet"
    if student[-1] != goal:
        return "Listen din ender ikke med målstoffet"
    costs = {}
    for a, b, e in reactions:
        costs[(a, b)] = e
    cost = 0
    for i in range(len(student) - 1):
        if (student[i], student[i + 1]) not in costs:
            return "Du gjør en reaksjon som ikke er lov"
        cost += costs[(student[i], student[i + 1])]
    if cost > answer:
        return "Du lager ikke stoffet på den mest energieffektive måten"


failed = False
for test_case, answer in tests:
    reactions, start, goal = test_case
    student = least_energy(reactions[:], start, goal)
    response = get_feedback(student, answer, reactions, start, goal)
    if response is not None:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
start: {start}
goal: {goal}
reactions:
    {(chr(10) + '    ').join(f"{a} -> {b} (energi: {e})" for a, b, e in reactions)}

Ditt svar: {student}
Minste mulige energi: {answer}
Feilmelding: {response}
""")


if not failed:
    print("Koden fungerte for alle eksempeltestene.")
