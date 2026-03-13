#!/usr/bin/env python3
"""Easy problem: binary search.

Reads:
- n
- sorted list of n integers
- q
- q query integers

For each query, print the index (0-based) of the value or -1 if not found.
"""

import sys

from cp.easy.problems import binary_search


def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    arr = [int(next(it)) for _ in range(n)]
    q = int(next(it))
    out = []
    for _ in range(q):
        x = int(next(it))
        out.append(str(binary_search(arr, x)))
    print("\n".join(out))


if __name__ == "__main__":
    main()
