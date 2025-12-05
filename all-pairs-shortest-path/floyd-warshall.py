#!/usr/bin/python3
# coding=utf-8
import sys
sys.set_int_max_str_digits(10**6)

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et lite sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å teste på
# et større sett med 500 genererte instanser. For å teste på det
# større settet med genererte instanser, må du (1) laste ned filen med
# testene fra øvingssystemet, (2) legge den samme plass som denne
# python-filen og (3) sette variabelen under til True. Merk at det kan
# ta litt tid å kjøre alle de 500 ekstra testene.
use_extra_tests = True

def general_floyd_warshall(D, n, f, g):
    r = range(n)
    for k in r:
        for i in r:
            for j in r:
                D[i][j] = f(D[i][j], g(D[i][k], D[k][j]))


class Operator:
    def __init__(self, name, function):
        self.name = name
        self.function = function


# Hardkodete tester på format: (D, f, g, svar)
tests = [
    (
        [
            [1, 3, 8, 3, 4],
            [3, 1, 4, 2, 7],
            [2, 4, 1, 7, 1],
            [2, 2, 5, 1, 7],
            [3, 9, 2, 6, 1],
        ],
        Operator("minimum", lambda x, y: min(x, y)),
        Operator("multiplikasjon", lambda x, y: x * y),
        [
            [1, 3, 8, 3, 4],
            [3, 1, 4, 2, 4],
            [2, 4, 1, 6, 1],
            [2, 2, 5, 1, 5],
            [3, 8, 2, 6, 1],
        ],
    ),
    (
        [
            [1, 1, float("inf")],
            [float("inf"), 1, 1],
            [1, float("inf"), 1],
        ],
        Operator("minimum", lambda x, y: min(x, y)),
        Operator("addisjon", lambda x, y: x + y),
        [[1, 1, 2], [2, 1, 1], [1, 2, 1]],
    ),
    (
        [
            [0, 3, 8, float("inf"), -4],
            [float("inf"), 0, float("inf"), 1, 7],
            [float("inf"), 4, 0, float("inf"), float("inf")],
            [2, float("inf"), -5, 0, float("inf")],
            [float("inf"), float("inf"), float("inf"), 6, 0],
        ],
        Operator("minimum", lambda x, y: min(x, y)),
        Operator("addisjon", lambda x, y: x + y),
        [
            [0, 1, -3, 2, -4],
            [3, 0, -4, 1, -1],
            [7, 4, 0, 5, 3],
            [2, -1, -5, 0, -2],
            [8, 5, 1, 6, 0],
        ],
    ),
]

def validate(student, answer):
    try:
        len(student)
        len(student[0])
    except:
        return "Koden returnerte ikke en tabell"

    if len(student) != len(answer) or any(len(A) != len(B)
                                          for A, B in zip(student, answer)):
        return "Tabellen som ble returnert har ikke riktig dimensjoner"

    if any(a != b for A, B in zip(student, answer) for a, b in zip(A, B)):
        return "Et eller flere av elementene i tabellen har feil verdi"


def table_format(T):
    try:
        return "\n    " + "\n    ".join(map(str, T))
    except:
        return str(T)


failed = False
for D, f, g, answer in tests:
    student = [row[:] for row in D]
    general_floyd_warshall(student, len(D), f.function, g.function)
    feedback = validate(student, answer)
    if feedback is not None:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
D: {table_format(D)}
n: {len(D)}
f: {f.name}
g: {g.name}

Ditt svar: {table_format(student)}
Riktig svar: {table_format(answer)}
Feedback: {feedback}
""")

if use_extra_tests:
    with open("tests_floyd_warshall.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            D, f, g, answer = map(eval, line.strip().split(" | "))
            extra_tests.append((D, f, g, answer))

    n_failed = 0
    for D, f, g, answer in extra_tests:
        student = [row[:] for row in D]
        general_floyd_warshall(student, len(D), f.function, g.function)
        feedback = validate(student, answer)
        if feedback is not None:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans.
D: {table_format(D)}
n: {len(D)}
f: {f.name}
g: {g.name}

Ditt svar: {table_format(student)}
Riktig svar: {table_format(answer)}
Feedback: {feedback}
""")
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden din passerte alle eksempeltestene.")

