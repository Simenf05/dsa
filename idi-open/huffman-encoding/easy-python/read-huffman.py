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
# python-filen og (3) sette variabelen under til True.
use_extra_tests = False

def makearr(node, code=""):
    ch = node.character
    if ch:
        return [(ch, code)]

    left = makearr(node.left_child, code+"0")
    right = makearr(node.right_child, code+"1")

    return left+right

def encoding(node, code=""):
    arr = makearr(node, code)
    dic = dict(arr)
    return dic


# Hardkodete tester på formatet: (tre, encoding)
tests = [
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "n",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "character": None,
        },
        {"n": "0", "a": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "n",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "a",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "b",
                },
                "character": None,
            },
            "character": None,
        },
        {"n": "0", "a": "10", "b": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "c",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "a",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "b",
                },
                "character": None,
            },
            "character": None,
        },
        {"c": "0", "a": "10", "b": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "c",
            },
            "character": None,
        },
        {"a": "0", "c": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "b",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "c",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "d",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"a": "0", "b": "10", "c": "110", "d": "111"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "right_child": {
                "left_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "b",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "d",
                    },
                    "character": None,
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "c",
                },
                "character": None,
            },
            "character": None,
        },
        {"a": "0", "b": "100", "d": "101", "c": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "a",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "b",
                    },
                    "character": None,
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "c",
                },
                "character": None,
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "d",
            },
            "character": None,
        },
        {"a": "000", "b": "001", "c": "01", "d": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "X",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "f",
            },
            "character": None,
        },
        {"X": "0", "f": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "X",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "B",
                },
                "character": None,
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "a",
            },
            "character": None,
        },
        {"X": "00", "B": "01", "a": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "K",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "B",
            },
            "character": None,
        },
        {"K": "0", "B": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "Y",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "F",
                },
                "character": None,
            },
            "right_child": {
                "left_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "O",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "M",
                    },
                    "character": None,
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "Q",
                },
                "character": None,
            },
            "character": None,
        },
        {"Y": "00", "F": "01", "O": "100", "M": "101", "Q": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "F",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "s",
            },
            "character": None,
        },
        {"F": "0", "s": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "S",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "z",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "b",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "O",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"S": "0", "z": "10", "b": "110", "O": "111"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "R",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "e",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "T",
                },
                "character": None,
            },
            "character": None,
        },
        {"R": "0", "e": "10", "T": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "B",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "y",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "d",
                },
                "character": None,
            },
            "character": None,
        },
        {"B": "0", "y": "10", "d": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "u",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "q",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "z",
                },
                "character": None,
            },
            "character": None,
        },
        {"u": "0", "q": "10", "z": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "i",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "J",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "I",
                },
                "character": None,
            },
            "character": None,
        },
        {"i": "0", "J": "10", "I": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "T",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "K",
            },
            "character": None,
        },
        {"T": "0", "K": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "x",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "S",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "d",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "h",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"x": "0", "S": "10", "d": "110", "h": "111"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "y",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "t",
                },
                "character": None,
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "d",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "L",
                },
                "character": None,
            },
            "character": None,
        },
        {"y": "00", "t": "01", "d": "10", "L": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "w",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "p",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "S",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "K",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"w": "0", "p": "10", "S": "110", "K": "111"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "y",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "u",
                },
                "character": None,
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "U",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "a",
                },
                "character": None,
            },
            "character": None,
        },
        {"y": "00", "u": "01", "U": "10", "a": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "e",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "z",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "O",
                },
                "character": None,
            },
            "character": None,
        },
        {"e": "0", "z": "10", "O": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "s",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "S",
                },
                "right_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "l",
                },
                "character": None,
            },
            "character": None,
        },
        {"s": "0", "S": "10", "l": "11"},
    ),
    (
        {
            "left_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "g",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "E",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "i",
                    },
                    "character": None,
                },
                "character": None,
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "U",
            },
            "character": None,
        },
        {"g": "00", "E": "010", "i": "011", "U": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "G",
            },
            "right_child": {
                "left_child": None,
                "right_child": None,
                "character": "W",
            },
            "character": None,
        },
        {"G": "0", "W": "1"},
    ),
    (
        {
            "left_child": {
                "left_child": None,
                "right_child": None,
                "character": "A",
            },
            "right_child": {
                "left_child": {
                    "left_child": None,
                    "right_child": None,
                    "character": "E",
                },
                "right_child": {
                    "left_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "k",
                    },
                    "right_child": {
                        "left_child": None,
                        "right_child": None,
                        "character": "a",
                    },
                    "character": None,
                },
                "character": None,
            },
            "character": None,
        },
        {"A": "0", "E": "10", "k": "110", "a": "111"},
    ),
]


class Node:
    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.character = None

    def __str__(self):
        if self.character is not None:
            representation = f"● character: {self.character}\n"
        else:
            representation = f""
        if self.left_child != None:
            representation += f"┣━━━┓ (venstre)"
            representation += "\n┃   " + str(self.left_child).replace("\n", "\n┃   ")
            representation += f"\n┗━━━┓ (høyre)"
            representation += "\n    " + str(self.right_child).replace("\n", "\n    ")
        return representation

    @classmethod
    def from_dict(cls, dic):
        node = Node()
        left_child = dic.get("left_child", dic.get("l", None))
        right_child = dic.get("right_child", dic.get("r", None))
        if left_child is not None:
            node.left_child = Node.from_dict(left_child)
        if right_child is not None:
            node.right_child = Node.from_dict(right_child)
        node.character = dic.get("character", dic.get("c", None))
        return node


failed = False
for test_case, answer in tests:
    node = Node.from_dict(test_case)
    student = encoding(node)
    if student != answer:
        if failed:
            print("-"*50)

        failed = True
        print(f"""
Koden feilet for følgende instans:
tre:
{node}

Ditt svar: {student}
Riktig svar: {answer}
        """)

if use_extra_tests:
    with open("tests_encoding.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            extra_tests.append(tuple(map(eval, line.strip().split(" | "))))

    n_failed = 0
    for test_case, answer in extra_tests:
        node = Node.from_dict(test_case)
        student = encoding(node)
        if student != answer:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans:
tre:
{node}

Ditt svar: {student}
Riktig svar: {answer}
                """)
            elif n_failed == 6:
                print("Koden har feilet for mer enn 5 av de ekstra testene.")
                print("De resterende feilene vil ikke skrives ut.")

    if n_failed > 0:
        print(f"Koden feilet for {n_failed} av de ekstra testene.")

if not failed:
    print("Koden din fungerte for alle eksempeltestene")
