"""Search techniques for competitive programming."""

from typing import Callable, List, Optional, Tuple


def binary_search(lo: int, hi: int, predicate: Callable[[int], bool]) -> int:
    """Find smallest x in [lo, hi) where predicate(x) is True."""
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


def ternary_search(lo: float, hi: float, f: Callable[[float], float], iters: int = 100) -> float:
    """Ternary search on unimodal function on [lo, hi]."""
    for _ in range(iters):
        m1 = lo + (hi - lo) / 3
        m2 = hi - (hi - lo) / 3
        if f(m1) < f(m2):
            hi = m2
        else:
            lo = m1
    return (lo + hi) / 2


def meet_in_middle(items: List[int], target: int) -> bool:
    """Return True if some subset sum equals target (O(2^{n/2}))."""
    n = len(items)
    half = n // 2
    left = items[:half]
    right = items[half:]

    def sums(arr: List[int]) -> List[int]:
        res = [0]
        for x in arr:
            res += [s + x for s in res]
        return res

    left_sums = sorted(sums(left))
    right_sums = sorted(sums(right))
    i, j = 0, len(right_sums) - 1
    while i < len(left_sums) and j >= 0:
        s = left_sums[i] + right_sums[j]
        if s == target:
            return True
        if s < target:
            i += 1
        else:
            j -= 1
    return False
