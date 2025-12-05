#!/usr/bin/python3
# coding=utf-8

# Testsettet på serveren er større og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke når du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt høyde for.

# De lokale testene består av to deler. Et lite sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for å teste på
# et større sett med 1000 genererte instanser. For å teste på det
# større settet med genererte instanser, må du (1) laste ned filen med
# testene fra øvingssystemet, (2) legge den samme plass som denne
# python-filen og (3) sette variabelen under til True. Merk at det kan
# ta litt tid å kjøre alle de 1000 ekstra testene.
use_extra_tests = True

def verify_tsp(path, k, weight_matrix):
    visited = [False] * len(weight_matrix)

    if path[0] != path[-1]:
        return False
    total_weight = 0

    for i, node in enumerate(path[:-1]):
        if node == path[i+1]:
            return False
        if visited[node]:
            return False
        visited[node] = True
        total_weight += weight_matrix[node][path[i+1]]

    if total_weight > k:
        return False

    return True


# Hardkodede tester på format: (sti, k, vektmatrise), svar
tests = [
    (([0, 1, 2, 0], 3, [[0, 1, 1], [1, 0, 1], [1, 1, 0]]), True),
    (([0, 2, 1, 3, 0], 7,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), True),
    (([0, 2, 1, 3, 0], 8,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), True),
    (([0, 2, 1, 0], 6,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), False),
    (([0, 2, 1, 3, 0], 6,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), False),
    (([0, 2, 2, 3, 0], 7,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), False),
    (([2, 0, 3, 1, 2], 7,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), True),
    (([2, 0, 3, 1, 3], 7,
      [[0, 4, 1, 3], [4, 0, 2, 1], [1, 2, 0, 5], [3, 1, 5, 0]]), False)
]

failed = False

for (path, k, weight_matrix), answer in tests:
    student = verify_tsp(path[:], k, [row[:] for row in weight_matrix])
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for følgende instans:
path: {path}
k: {k}
weight_matrix:
    {(chr(10) + '    ').join(map(str, weight_matrix))}

Ditt svar: {student}
Riktig svar: {answer}
""")
if use_extra_tests:
    with open("tests_verify_tsp.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            path, k, weight_matrix, answer = line.strip().split(" | ")
            path = list(map(int, path.split(",")))
            k = int(k)
            weight_matrix = [list(map(int, row.split(","))) for row in
                             weight_matrix.split(";")]
            answer = answer == "True"

            extra_tests.append(((path, k, weight_matrix), answer))

    n_failed = 0
    for (path, k, weight_matrix), answer in extra_tests:
        student = verify_tsp(path[:], k, [row[:] for row in weight_matrix])
        if student != answer:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans:
path: {path}
k: {k}
weight_matrix:
    {(chr(10) + '    ').join(map(str, weight_matrix))}

Ditt svar: {student}
Riktig svar: {answer}
""")
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden fungerte for alle eksempeltestene.")

