#!/usr/bin/python3
# coding=utf-8
import random
import math

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for å generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved å justere på verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Lavest mulig antall tog i generert instans.
trains_lower = 20
# Høyest mulig antall tog i generert instans. Om denne verdien er satt høyt
# (>120), kan det ta lang tid å generere instansene.
trains_upper = 50
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0

def parent(i):
    return i//2

def left(i):
    return i*2

def right(i):
    return i*2+1

class MinHeap:

    def __init__(self, length):
        self.heapsize = 0
        self.arr = [0. for _ in range(length)]

    def min_heapify(self, i):
        l = left(i)
        r = right(i)

        if l <= self.heapsize and self.arr[l] < self.arr[i]:
            smallest = l
        else:
            smallest = i

        if r <= self.heapsize and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)


    def heap_extract_min(self):
        min = self.arr[0]
        self.heapsize -= 1
        self.arr[0] = self.arr[self.heapsize]
        self.min_heapify(0)
        return min

    def heap_decrease_key(self, i, key):
        self.arr[i] = key
        while i > 0 and self.arr[parent(i)] > self.arr[i]:
            self.arr[parent(i)], self.arr[i] = self.arr[i], self.arr[parent(i)]
            i = parent(i)

    def min_heap_insert(self, key):
        self.heapsize += 1
        self.arr[self.heapsize-1] = float("inf")
        self.heap_decrease_key(self.heapsize-1, key)

class Graph:
    def __init__(self, verts, edges):
        self.adj = [[] for _ in range(verts)]
        for edge in edges:
            self.adj[edge[0]].append(edge[1])

def dijkstra():
    heap = MinHeap(10)

    heap.min_heap_insert()

    while heap.heapsize > 0:
        pass


def earliest_arrival(timetable, start, goal):

    verts = set()
    for edge in timetable:
        verts.add(edge[0])
        verts.add(edge[1])

    print(verts)

    print(timetable)
    print(start)
    print(goal)


# Hardkodete tester på format: (tog, start, slutt), tidligst tidspunkt
tests = [
    (
        (
            [
                ("G", "Z", 62, 79),
                ("P", "Z", 96, 98),
                ("G", "P", 87, 96),
                ("G", "P", 1, 52),
                ("G", "P", 66, 93),
            ],
            "G",
            "Z",
        ),
        79,
    ),
    (([("A", "B", 100, 101)], "A", "B"), 101),
    (([("B", "A", 20, 30), ("B", "A", 25, 29)], "B", "A"), 29),
    (
        ([("A", "B", 0, 10), ("B", "C", 10, 20), ("A", "C", 0, 30)], "A", "C"),
        20,
    ),
    (
        (
            [("A", "B", 0, 10), ("B", "C", 10, 20), ("A", "C", 10, 15)],
            "A",
            "C",
        ),
        15,
    ),
    (
        (
            [("A", "C", 10, 30), ("B", "C", 15, 25), ("A", "B", 0, 20)],
            "A",
            "C",
        ),
        30,
    ),
    (
        (
            [("A", "B", 10, 30), ("B", "C", 15, 25), ("B", "C", 35, 50)],
            "A",
            "C",
        ),
        50,
    ),
    (
        (
            [("A", "B", 10, 30), ("B", "C", 30, 40), ("B", "C", 35, 50)],
            "A",
            "C",
        ),
        40,
    ),
    (
        (
            [("Y", "C", 43, 98), ("C", "Y", 17, 61), ("Y", "C", 13, 18)],
            "Y",
            "C",
        ),
        18,
    ),
    (([("T", "M", 93, 97)], "T", "M"), 97),
    (
        (
            [
                ("B", "X", 48, 97),
                ("X", "Q", 1, 19),
                ("B", "X", 22, 42),
                ("X", "Q", 2, 35),
                ("B", "X", 63, 78),
            ],
            "B",
            "X",
        ),
        42,
    ),
    (([("W", "R", 41, 58)], "W", "R"), 58),
    (
        (
            [
                ("U", "L", 53, 58),
                ("U", "A", 68, 88),
                ("L", "U", 80, 82),
                ("U", "L", 47, 90),
            ],
            "U",
            "L",
        ),
        58,
    ),
    (([("O", "X", 44, 73)], "O", "X"), 73),
    (
        (
            [
                ("D", "R", 64, 80),
                ("D", "X", 24, 59),
                ("D", "X", 25, 90),
                ("D", "R", 33, 84),
                ("R", "D", 72, 83),
            ],
            "D",
            "R",
        ),
        80,
    ),
    (
        (
            [
                ("X", "P", 32, 95),
                ("X", "P", 89, 99),
                ("X", "P", 28, 93),
                ("P", "X", 76, 96),
            ],
            "P",
            "X",
        ),
        96,
    ),
    (
        (
            [("G", "Y", 22, 94), ("L", "G", 7, 61), ("G", "Y", 96, 98)],
            "G",
            "Y",
        ),
        94,
    ),
    (
        (
            [
                ("A", "B", 0, 4),
                ("B", "C", 4, 7),
                ("A", "C", 0, 15),
                ("B", "D", 4, 13),
                ("C", "D", 8, 11),
            ],
            "A",
            "D",
        ),
        11
    )
]


# Treg bruteforce løsning
def slow_solve(T, s, g, t=0):
    if s == g:
        return t
    m = float("inf")
    for a, b, t0, t1 in T:
        if a == s and t0 >= t:
            m = min(slow_solve(T, b, g, t1), m)
    return m


def gen_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(max(1, nl), nu)
        ns = random.randint(5, max(5, math.log(n, 20)))
        stations = set()
        while len(stations) < ns:
            stations.add(
                "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                        k=math.ceil(math.log(ns, 20))))
            )
        stations = tuple(stations)

        T = []
        for _ in range(n):
            t0 = random.randint(0, 10*n)
            t1 = random.randint(t0 + 1, t0 + 1*n)
            T.append((
                *random.sample(stations, k=2),
                t0,
                t1
            ))

        s, g = random.sample(stations, k=2)
        while slow_solve(T, s, g) == float("inf"):
            s, g = random.sample(stations, k=2)

        check = lambda d, e, f: any(a == d and b == e and t1 == f for a, b, _, t1 in T)

        if check(s, g, slow_solve(T, s, g)):
            for _ in range(20):
                x, y = random.sample(stations, k=2)
                if not check(x, y, slow_solve(T, x, y)):
                    s, g = x, y
                    break
        yield (T, s, g), slow_solve(T, s, g)



if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        trains_lower,
        trains_upper,
    ))

failed = False
for test_case, answer in tests:
    timetable, start, goal = test_case
    student = earliest_arrival(timetable[:], start, goal)
    break
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
start: {start}
goal: {goal}
timetable:
    {(chr(10) + '    ').join(f"{a} -> {b} (reiser {t_0}, fremme {t_1})" for a, b, t_0, t_1 in timetable)}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden fungerte for alle eksempeltestene.")

