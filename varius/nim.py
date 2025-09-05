#!/usr/bin/python3
# coding=utf-8

# Testsettet pÃ¥ serveren er stÃ¸rre og mer omfattende enn dette.
# Hvis programmet ditt fungerer lokalt, men ikke nÃ¥r du laster det opp,
# er det gode sjanser for at det er tilfeller du ikke har tatt hÃ¸yde for.

# Kontrollerer om koden skal kjÃ¸res pÃ¥ stÃ¸rre hardkodete tester.
# Disse inneholder mellom 100 og 10000 fyrstikker. Ellers har alle
# eksemplene mindre enn 100 fyrstikker.
large_tests = True


def take_pieces(n_pieces):
    diff = n_pieces % 8
    if diff == 0:
        diff = 8
    elif diff == 1:
        return diff 
    next = n_pieces - diff
    if next % 8 == 0:
        return diff - 1



# Hardkodete tester pÃ¥ formatet: (n_pieces, svar)
tests = [
    (1, None),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 4),
    (6, 5),
    (7, 6),
    (8, 7),
    (22, 5),
    (41, None),
    (61, 4),
    (79, 6),
    (88, 7),
    (91, 2),
]

# Store hardkodete tester
if large_tests:
    tests += [
        (8649, None),
        (5169, None),
        (2735, 6),
        (5830, 5),
        (2457, None),
        (5264, 7),
        (8793, None),
        (1899, 2),
        (4282, 1),
        (2827, 2),
        (3856, 7),
        (8193, None),
        (3398, 5),
        (4337, None),
        (1977, None),
        (7453, 4),
        (2578, 1),
        (8534, 5),
        (1361, None),
        (7760, 7),
        (5263, 6),
        (9760, 7),
        (5205, 4),
        (2448, 7),
        (4368, 7),
        (2108, 3),
        (3079, 6),
        (6096, 7),
        (5273, None),
        (3071, 6),
        (3510, 5),
        (9355, 2),
        (2327, 6),
        (5776, 7),
        (4487, 6),
        (8434, 1),
        (7087, 6),
        (2243, 2),
        (3688, 7),
        (9516, 3),
        (401, None),
        (9383, 6),
        (4321, None),
        (3962, 1),
        (5538, 1),
        (7299, 2),
        (6493, 4),
        (3893, 4),
        (8737, None),
        (6671, 6),
    ]

failed = False
for n, answer in tests:
    student = take_pieces(n)
    if (answer is not None and student != answer) or \
       (answer is None and student not in (1, 2, 3, 4, 5, 6, 7)):
        if failed:
            print("-"*50)
        failed = True

        print(f"""
Koden feilet for fÃ¸lgende instans:
n: {n}

Ditt svar: {student}
Riktig svar: {answer if answer is not None else
'En av verdiene 1, 2, 3, 4, 5, 6, 7'}
""")

if not failed:
    print("Koden ga riktig svar for alle eksempeltestene")
