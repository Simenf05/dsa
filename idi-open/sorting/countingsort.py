#!/usr/bin/python3
# coding=utf-8
import random

# Testsettet pÃ¥ serveren er stÃ¸rre og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke nÃ¥r du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt hÃ¸yde for.

# De lokale testene bestÃ¥r av to deler. Et sett med hardkodete
# instanser som kan ses lengre nedre, og muligheten for Ã¥ generere
# tilfeldige instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved Ã¥ justere pÃ¥ verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = False
# Antall tilfeldige tester som genereres.
random_tests = 10
# Laveste mulige antall tall i generert instans.
numbers_lower = 3
# HÃ¸yest mulig antall tall i generert instans.
numbers_upper = 8
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0


def counting_sort(A, n):
    k = 2049
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in A:
        C[i] += 1

    for i in range(k):
        C[i] = C[i] + C[i - 1]

    for j in range(n - 1, -1, -1):
        B[C[A[j]] - 1] = A[j]
        C[A[j]] -= 1

    return B


def run():
    arr = [1, 2, 3, 4, 5, 3, 2, 1, 4, 5, 6, 7, 8, 4, 3, 2, 1, 3, 5, 2, 200, 3, 7, 8, 9, 6, 4, 3, 2]
    sorted = counting_sort(arr, len(arr))
    print(arr)
    print(sorted)

run()
exit()

# Hardkodete tester
tests = [
    [1, 2, 3, 4],
    [],
    [1],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [1, 1, 2, 1],
    [1281, 1, 2],
    [0, 2047, 0, 2047],
    [995, 334, 709, 999, 502, 303, 274, 488, 997, 568, 546, 756],
    [648, 298, 568, 681, 795, 356, 603, 772, 373, 50, 253, 116],
]

def gen_examples(k, lower, upper):
    for _ in range(k):
        yield [
                random.randint(0, 2047)
                for _ in range(random.randint(lower, upper))
            ]


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        numbers_lower,
        numbers_upper,
    ))

failed = False
for A in tests:
    answer = sorted(A)
    student = counting_sort(A[:], len(A))
    break
    if student != answer:
        if failed:
            print("-"*50)
        failed = True
        print(f"""
Koden feilet for fÃ¸lgende instans:
A: {A}
n: {len(A)}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
