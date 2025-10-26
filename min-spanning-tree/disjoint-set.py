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
# Laveste mulige antall kall til de tre operasjonene i generert instans.
operations_lower = 10
# Høyest mulig antall kall til de tre operasjonene i generert instans.
operations_upper = 20
# Om denne verdien er 0 vil det genereres nye instanser hver gang.
# Om den er satt til et annet tall vil de samme instansene genereres
# hver gang, om verdiene over ikke endres.
seed = 0



class HigherEdSolver:
    def initialize(self, institutions):
        self.map = {}
        for inst in institutions:
            self.map[inst] = {"name": inst, "parent": inst}


    def parent_institution(self, institution):
        parent = self.map[institution]["parent"]
        if (institution == parent):
            return parent
        new_parent = self.parent_institution(parent)
        self.map[institution]["parent"] = new_parent
        return new_parent


    def fuse(self, institution1, institution2, new_institution):
        self.map[institution1]["parent"] = new_institution
        self.map[institution2]["parent"] = new_institution
        self.map[new_institution] = {"name": new_institution, "parent": new_institution}


class HigherEdTestCase:
    def __init__(self, calls, print_case):
        self.calls = calls
        self.print_case = print_case

    def test(self, initialize, parent_institution, fuse):
        for index, call in enumerate(self.calls):
            if call[0] == "initialize":
                initialize(call[1])
            elif call[0] == "parent_institution":
                res = parent_institution(call[1])
                assert res == call[2], (
                    "Kall:\n"
                    + self.calls_to_str(index + 1)
                    + '\nSistnevte returnerte "{:}", men skulle '.format(res)
                    + 'returnere "{:}"'.format(call[2])
                    if self.print_case
                    else "parent_institution returnerte feil"
                )
            elif call[0] == "fuse":
                fuse(call[1], call[2], call[3])

    def calls_to_str(self, index=None):
        s = ""
        for call in self.calls[:index]:
            if call[0] == "initialize":
                s += 'initialize(["' + '", "'.join(call[1]) + '"])'
            elif call[0] == "parent_institution":
                s += 'parent_institution("{:}")'.format(call[1])
            elif call[0] == "fuse":
                s += 'fuse("{:}", "{:}", "{:}")'.format(call[1], call[2], call[3])
            s += "\n"
        return s


tests = [
    [
        ("initialize", ["UniK", "UniR", "UniW"]),
        ("parent_institution", "UniK", "UniK"),
        ("parent_institution", "UniR", "UniR"),
        ("fuse", "UniK", "UniW", "UniC"),
    ],
    [
        ("initialize", ["UniP", "UniB", "UniY", "UniJ", "UniK"]),
        ("fuse", "UniK", "UniB", "UniT"),
        ("fuse", "UniY", "UniT", "UniM"),
        ("fuse", "UniP", "UniM", "UniV"),
        ("parent_institution", "UniK", "UniV"),
    ],
    [
        ("initialize", ["UniL", "UniQ", "UniB", "UniY", "UniU"]),
        ("parent_institution", "UniL", "UniL"),
        ("fuse", "UniY", "UniB", "UniF"),
        ("parent_institution", "UniB", "UniF"),
        ("fuse", "UniQ", "UniF", "UniX"),
        ("parent_institution", "UniY", "UniX"),
    ],
    [
        ("initialize", ["UniG", "UniS", "UniC", "UniU"]),
        ("parent_institution", "UniG", "UniG"),
        ("fuse", "UniS", "UniC", "UniM"),
    ],
    [
        ("initialize", ["UniB", "UniA", "UniE", "UniO", "UniG"]),
        ("parent_institution", "UniE", "UniE"),
        ("fuse", "UniO", "UniA", "UniN"),
        ("fuse", "UniG", "UniE", "UniD"),
        ("fuse", "UniN", "UniD", "UniW"),
        ("parent_institution", "UniB", "UniB"),
    ],
    [
        ("initialize", ["UniZ", "UniR", "UniM", "UniC", "UniW"]),
        ("fuse", "UniC", "UniM", "UniK"),
        ("parent_institution", "UniC", "UniK"),
    ],
    [
        ("initialize", ["UniE", "UniR", "UniK", "UniQ", "UniD"]),
        ("fuse", "UniD", "UniK", "UniN"),
        ("parent_institution", "UniR", "UniR"),
        ("parent_institution", "UniE", "UniE"),
        ("parent_institution", "UniQ", "UniQ"),
    ],
    [
        ("initialize", ["UniN", "UniZ", "UniY", "UniA", "UniF"]),
        ("fuse", "UniZ", "UniF", "UniK"),
        ("fuse", "UniN", "UniK", "UniX"),
        ("parent_institution", "UniZ", "UniX"),
        ("fuse", "UniA", "UniY", "UniC"),
    ],
    [
        ("initialize", ["UniG", "UniK", "UniI", "UniM"]),
        ("parent_institution", "UniG", "UniG"),
        ("fuse", "UniM", "UniI", "UniY"),
        ("fuse", "UniY", "UniG", "UniS"),
    ],
    [
        ("initialize", ["UniT", "UniK", "UniC"]),
        ("parent_institution", "UniC", "UniC"),
        ("fuse", "UniK", "UniC", "UniZ"),
    ],
    [
        ("initialize", ["UniX", "UniM", "UniY", "UniA", "UniI"]),
        ("fuse", "UniA", "UniI", "UniK"),
        ("parent_institution", "UniM", "UniM"),
        ("fuse", "UniM", "UniY", "UniU"),
        ("parent_institution", "UniI", "UniK"),
        ("fuse", "UniU", "UniK", "UniW"),
    ],
    [
        ("initialize", ["UniK", "UniZ", "UniY"]),
        ("parent_institution", "UniK", "UniK"),
        ("parent_institution", "UniK", "UniK"),
        ("fuse", "UniY", "UniZ", "UniQ"),
        ("parent_institution", "UniK", "UniK"),
        ("parent_institution", "UniY", "UniQ"),
    ],
    [
        ("initialize", ["UniC", "UniJ", "UniD", "UniI", "UniQ"]),
        ("fuse", "UniQ", "UniI", "UniB"),
        ("fuse", "UniC", "UniJ", "UniS"),
        ("parent_institution", "UniD", "UniD"),
        ("parent_institution", "UniI", "UniB"),
    ],
    [
        ("initialize", ["UniU", "UniO", "UniI", "UniS"]),
        ("fuse", "UniO", "UniS", "UniW"),
        ("parent_institution", "UniI", "UniI"),
        ("parent_institution", "UniU", "UniU"),
    ],
]

def gen_examples(k, nl, nu):
    for _ in range(k):
        n = random.randint(nl, nu)
        n_uni = random.randint(max(2, n//3), n)
        unis = set()
        while len(unis) != n_uni:
            unis.add("Uni" + "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                                                    k=math.ceil(math.log(n_uni, 20)))))
        active = set(unis)
        unis = {uni: uni for uni in unis}
        test = []
        test.append(("initialize", list(unis)))
        while len(test) < n:
            o = random.choice(["fuse", "parent_institution"])
            if len(active) < 2 and o == "fuse":
                o = "parent_institution"

            if o == "fuse":
                a, b = random.sample(tuple(active), k=2)
                name = "Uni" + a[3:] + b[3:]
                active.remove(a)
                active.remove(b)
                active.add(name)
                unis[a] = unis[b] = unis[name] = name
                test.append(("fuse", a, b, name))

            if o == "parent_institution":
                x = random.choice(tuple(unis.keys()))
                y = x
                while y != unis[y]:
                    y = unis[y]
                test.append(("parent_institution", x, y))
        yield test


if generate_random_tests:
    if seed:
        random.seed(seed)
    tests += list(gen_examples(
        random_tests,
        operations_lower,
        operations_upper,
    ))


failed = False
for test_case in tests:
    test_case = HigherEdTestCase(test_case, True)
    higher_ed_solver = HigherEdSolver()
    try:
        test_case.test(
            higher_ed_solver.initialize,
            higher_ed_solver.parent_institution,
            higher_ed_solver.fuse,
        )
    except AssertionError as e:
        if failed:
            print("\n" + "-"*50 + "\n")
        print(str(e))
        failed = True
