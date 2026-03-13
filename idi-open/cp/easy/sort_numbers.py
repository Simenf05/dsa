#!/usr/bin/env python3
"""Easy problem: sort numbers from input.

Input format (example):
4
3 1 4 2

Output:
1 2 3 4

This is a common "sorting" warm-up problem.
"""

import sys

from cp.easy.problems import sort_numbers


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    arr = list(map(int, data[1 : 1 + n]))
    res = sort_numbers(arr)
    print(" ".join(map(str, res)))


if __name__ == "__main__":
    main()
