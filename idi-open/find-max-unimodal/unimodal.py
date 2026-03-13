#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import numpy as np

# Testsettet pÃ¥ serveren er stÃ¸rre og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke nÃ¥r du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt hÃ¸yde for.

# De lokale testene bestÃ¥r av to deler. Et sett med hardkodete
# instanser som kan ses lengre nede, og muligheten for Ã¥ generere
# tilfeldig instanser. Genereringen av de tilfeldige instansene
# kontrolleres ved Ã¥ juste pÃ¥ verdiene under.

# Kontrollerer om det genereres tilfeldige instanser.
generate_random_tests = True 
# Antall tilfeldige tester som genereres
random_tests = 100
# Lavest mulig antall verdier i generert instans.
n_lower = 1000
# HÃ¸yest mulig antall verdier i generert instans.
n_upper = n_lower
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 1


def check_if_increasing(x, pos, dir):
    return x[(pos+dir) % len(x)] > x[pos]

def new_find(arr, pos, jump_dist):
    print(jump_dist)

    is_right_increasing = check_if_increasing(arr, pos, 1)
    is_left_increasing = check_if_increasing(arr, pos, -1)

    new_jump_dist = max(jump_dist // 2, 1)

    if (not is_left_increasing) and (not is_right_increasing):
        return arr[pos]
    elif is_left_increasing:
        new_pos = (pos - jump_dist) % len(arr)
        return new_find(arr, new_pos, new_jump_dist)
    else:
        new_pos = (pos + jump_dist) % len(arr)
        return new_find(arr, new_pos, new_jump_dist)


def find_maximum(x):
    return new_find(x, 0, len(x) // 2 - 2)


arr = [66, 67, 68, 72, 69, 51, 37, 15, 17]
arr2 = [9, 2, 1, 3, 4, 5, 6, 7, 8]
arr3 = [3, 1]
arr4 = [2, 0, 1]
arr5 = [2, 4, 8, 12, 7, 6, 5, 4, 3]

mat = []
mat.append([60, 72, 75, 3, 14, 16, 18, 27, 43])
mat.append([24, 2, 89, 88, 87, 84, 72, 71, 46, 37])
mat.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
mat.append([5, 27, 28, 34, 12, 3])
mat.append([10, 11, 12, 13, 14, 13, 12])
mat.append([66, 67, 68, 72, 69, 51, 37, 15, 17])
mat.append([6, 5, 4, 3, 2, 1])
mat.append([16, 7, 9, 15, 79, 69, 42, 39, 30])





def run():
    for a in mat:
        print(f"correct: {max(a)}, my: {find_maximum(a)}, len: {len(a)}")

run()

exit()

# Hardkodete tester pÃ¥ format: (x, svar)
tests = [
    ([1], 1),
    ([1, 3], 3),
    ([3, 1], 3),
    ([1, 2, 1], 2),
    ([1, 0, 2], 2),
    ([2, 0, 1], 2),
    ([0, 2, 1], 2),
    ([0, 1, 2], 2),
    ([2, 1, 0], 2),
    ([2, 3, 1, 0], 3),
    ([2, 3, 4, 1], 4),
    ([2, 1, 3, 4], 4),
    ([4, 2, 1, 3], 4),
]

# En liste som ikke kan skrives til
class List:
    def __init__(self, li):
        self.__internal_list = li

    def __getitem__(self, key):
        return self.__internal_list[key]

    def __len__(self):
        return len(self.__internal_list)

    def __setitem__(self):
        raise NotImplementedError(
            "Du skal ikke trenge Ã¥ skrive til listen"
        )

# Genererer tilfeldige instanser med svar
def generate_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        x = random.sample(range(5*n), k=n)
        answer = max(x)
        t = x.index(answer)
        x = sorted(x[:t]) + [answer] + sorted(x[t + 1:], reverse=True)
        t = random.randint(0, n)
        x = x[t:] + x[:t]
        yield x, answer

def test_nums(n):
    test = []
    test.extend(generate_examples(1, n, n))
    # start = time.time()
    for x, _ in tests:
        x_ro = List(x[:])
        print(x)
        mymax = find_maximum(x_ro)
        print(f"max: {max(x)}, mymax: {mymax}")
    # end = time.time()
    
    # print(end - start)


n_values = map(lambda a: int(a), np.linspace(10, 100, 1))

for n in n_values:
    test_nums(n)

exit()

if generate_random_tests:
    if seed:
        random.seed(seed)

    tests.extend(generate_examples(random_tests, n_lower, n_upper))


failed = False
for x, answer in tests:
    x_ro = List(x[:])
    student = find_maximum(x_ro)
    if student != answer:
        if failed:
            print("-"*50)

        failed = True

        print(f"""
Koden ga feil svar for fÃ¸lgende instans:
x: {x}

Ditt svar: {student}
Riktig svar: {answer}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
