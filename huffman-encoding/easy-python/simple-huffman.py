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


def encode(data, encoding):
    streng = ""
    for ch in data:
        streng += encoding[ch]
    return streng





# Hardkodete tester på format: ((data, encoding), svar)
tests = [
    (("na", {"n": "0", "a": "1"}), "01"),
    (("na", {"n": "1", "a": "0"}), "10"),
    (("nabn", {"n": "1", "a": "01", "b": "10"}), "101101"),
    (("abccba", {"a": "00", "b": "01", "c": "1"}), "0001110100"),
    (("accca", {"c": "0", "a": "1"}), "10001"),
    (("abbca", {"a": "01", "b": "1", "c": "00"}), "01110001"),
    (("ffXf", {"X": "0", "f": "1"}), "1101"),
    (("iidvvv", {"v": "0", "d": "10", "i": "11"}), "111110000"),
    (("gaaCa", {"g": "00", "C": "01", "a": "1"}), "0011011"),
    (
        ("qtqXctqqX", {"q": "0", "X": "10", "c": "110", "t": "111"}),
        "01110101101110010",
    ),
    (
        (
            "MYQOIQIMMQ",
            {"I": "00", "Y": "010", "O": "011", "M": "10", "Q": "11"},
        ),
        "1001011011001100101011",
    ),
    (("zzJzv", {"J": "00", "v": "01", "z": "1"}), "1100101"),
    (("aaxaaxx", {"x": "0", "a": "1"}), "1101100"),
    (
        (
            "UIoIUIUEEl",
            {"E": "00", "o": "010", "l": "011", "U": "10", "I": "11"},
        ),
        "1011010111011100000011",
    ),
    (("GgwGN", {"g": "00", "w": "01", "N": "10", "G": "11"}), "1100011110"),
    (("EEucu", {"u": "0", "c": "10", "E": "11"}), "11110100"),
    (("RTQTj", {"R": "00", "Q": "01", "j": "10", "T": "11"}), "0011011110"),
    (("XsXPP", {"P": "0", "s": "10", "X": "11"}), "11101100"),
    (("diDDDiiD", {"D": "0", "d": "10", "i": "11"}), "101100011110"),
    (("HHuGuHu", {"u": "0", "G": "10", "H": "11"}), "11110100110"),
    (("uqzq", {"q": "0", "u": "10", "z": "11"}), "100110"),
    (("rKr", {"K": "0", "r": "1"}), "101"),
    (("YYiEEEY", {"E": "0", "i": "10", "Y": "11"}), "11111000011"),
    (("iONONNO", {"N": "0", "i": "10", "O": "11"}), "10110110011"),
    (("QuQuuxu", {"x": "00", "Q": "01", "u": "1"}), "0110111001"),
    (("yGGyy", {"G": "0", "y": "1"}), "10011"),
]

failed = False
for test_case, answer in tests:
    data, encoding = test_case
    student = encode(data, {c: e for c,e in encoding.items()})
    if student != answer:
        if failed:
            print("-"*50)

        failed = True
        print(f"""
Koden feilet for følgende instans:
data: {data}
encoding: {encoding}

Ditt svar: {student}
Riktig svar: {answer}
        """)

if use_extra_tests:
    with open("tests_encode.txt") as extra_tests_data:
        extra_tests = []
        for line in extra_tests_data:
            data, encoding, answer = line.strip().split(" | ")
            encoding = {
                c: e
                for c, e in map(
                    lambda x: x.split(":"),
                    encoding.split(","),
                )
            }
            extra_tests.append(((data, encoding), answer))

    n_failed = 0
    for test_case, answer in extra_tests:
        data, encoding = test_case
        student = encode(data, {c: e for c,e in encoding.items()})
        if student != answer:
            n_failed += 1
            if failed and n_failed <= 5:
                print("-"*50)

            failed = True
            if n_failed <= 5:
                print(f"""
Koden feilet for følgende instans:
data: {data}
encoding: {encoding}

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
