#!/usr/bin/python3
# coding=utf-8

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
use_extra_tests = False

import numpy as np

def schulze_method(W, n):
    r = range(n)

    p = [[0 for _ in r] for _ in r]

    for i in r:
        for j in r:
            if i != j:
                p[i][j] = max(0, W[i][j] - W[j][i])

    for k in r:
        for i in r:
            if i != k:
                for j in r:
                    if j != k and j != i:
                        p[i][j] = max(p[i][j], min(p[i][k], p[k][j]))

    order = []
    used = set()

    for k in r:
        pass

    for k in r:
        max_row = -1
        max_val = -1
        max_count = 0
        for i in r:
            if i in used:
                continue
            local_max = 0
            local_max_count = 0

            for j in r:
                if p[i][j] > local_max:
                    local_max = p[i][j]
                    local_max_count = 1
                elif p[i][j] == local_max:
                    local_max_count += 1

            if local_max > max_val:
                max_val = local_max
                max_row = i
                max_count = local_max_count
            elif local_max == max_val:
                if local_max_count > max_count:
                    max_val = local_max
                    max_row = i
                    max_count = local_max_count

        used.add(max_row)
        order.append(max_row)

    print(np.array(p))


    return order




# Hardkodete tester på format: (W, svar)
tests = [
    ([[0, 2, 1], [4, 0, 4], [5, 2, 0]], [1, 2, 0]),
    (
        [
            [0, 6, 7, 8, 7, 8],
            [6, 0, 6, 8, 7, 8],
            [5, 6, 0, 6, 5, 7],
            [4, 4, 6, 0, 5, 6],
            [5, 5, 7, 7, 0, 6],
            [4, 4, 5, 6, 6, 0],
        ],
        [0, 1, 4, 2, 3, 5],
    ),
    ([[0]], [0]),
    ([[0, 1], [3, 0]], [1, 0]),
    ([[0, 2], [2, 0]], [0, 1]),
    ([[0, 4, 3], [2, 0, 2], [3, 4, 0]], [0, 2, 1]),
    ([[0, 2, 1], [4, 0, 4], [5, 2, 0]], [1, 2, 0]),
    (
        [
            [0, 1, 3, 3, 3],
            [9, 0, 5, 5, 7],
            [7, 5, 0, 5, 4],
            [7, 5, 5, 0, 6],
            [7, 3, 6, 4, 0],
        ],
        [1, 3, 4, 2, 0],
    ),
]


def validate(student, answer):
    try:
        len(student)
    except:
        return "Koden returnerte ikke en liste"

    if len(student) != len(answer):
        return "Listen inneholder ikke riktig antall kandidater"

    if set(student) != set(answer):
        return "Listen inneholder ikke alle kandidatene"

    if any(a != b for a, b in zip(student, answer)):
        return "En eller flere av kandidatene opptrer i feil rekkefølge"


def generate_feedback(test, expected, student):
    feedback = ""
    feedback += "Koden din feilet for input\n"
    feedback += str(test) + "\n"
    feedback += "Ditt svar er\n"
    feedback += str(student) + ",\n"
    feedback += "men riktig svar er\n"
    feedback += str(expected) + "."
    return feedback


table_format = lambda T: "\n    " + "\n    ".join(map(str, T))
failed = False
for W, answer in tests:
    student = schulze_method([row[:] for row in W], len(W))
    feedback = validate(student, answer)
    if feedback is not None:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans.
W: {table_format(W)}
n: {len(W)}

Ditt svar: {student}
Riktig svar: {answer}
Feedback: {feedback}
""")
        break

if use_extra_tests:
    with open("tests_schulze_method.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            W, answer = map(eval, line.strip().split(" | "))
            extra_tests.append((W, answer))

    n_failed = 0
    for W, answer in extra_tests:
        student = schulze_method([row[:] for row in W], len(W))
        feedback = validate(student, answer)
        if feedback is not None:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans.
W: {table_format(W)}
n: {len(W)}

Ditt svar: {student}
Riktig svar: {answer}
Feedback: {feedback}
""")
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden din passerte alle eksempeltestene.")
