#!/bin/env python3
import time

unnskyld_melding = """⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣶⣦⠀⠀
⠀⠀⣠⣤⣤⣄⣀⣾⣿⠟⠛⠻⢿⣷⠀
⢰⣿⡿⠛⠙⠻⣿⣿⠁⠀⠀⠀⣶⢿⡇
⢿⣿⣇⠀⠀⠀⠈⠏⠀⠀⠀ Unnskyld Sara, jeg mente ikke å være slem
⠀⠻⣿⣷⣦⣤⣀⠀⠀⠀⠀⣾⡿⠃⠀
⠀⠀⠀⠀⠉⠉⠻⣿⣄⣴⣿⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⡿⠟⠁⠀⠀⠀⠀
"""

def clear():
    print('\033c')

def set_white():
    print("\033[97m")

def set_pink():
    print("\033[91m")

def si_unnskyld():
    print(unnskyld_melding)


def loop():
    while True:
        clear()
        set_pink()
        si_unnskyld()
        time.sleep(.3)
        clear()
        set_white()
        si_unnskyld()
        time.sleep(.3)

loop()
