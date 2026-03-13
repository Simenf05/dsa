"""Greedy algorithm patterns used in contests."""

from heapq import heapify, heappop, heappush
from typing import List, Tuple


def activity_selection(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """Select maximum number of non-overlapping intervals."""
    intervals = sorted(intervals, key=lambda x: x[1])
    res = []
    last_end = -10**18
    for s, e in intervals:
        if s >= last_end:
            res.append((s, e))
            last_end = e
    return res


def interval_scheduling(intervals: List[Tuple[int, int]]) -> int:
    """Return max number of non-overlapping intervals."""
    return len(activity_selection(intervals))


def huffman_coding(freq: List[int]) -> int:
    """Return cost of optimal Huffman tree (sum of merged weights)."""
    pq = freq[:]
    heapify(pq)
    cost = 0
    while len(pq) > 1:
        a = heappop(pq)
        b = heappop(pq)
        cost += a + b
        heappush(pq, a + b)
    return cost


def greedy_sort_by_key(values: List[int]) -> List[int]:
    """Example: sort as a greedy basis for algorithms."""
    return sorted(values)


def nth_smallest(values: List[int], n: int) -> int:
    """Selection algorithm (quickselect, average O(n))."""
    import random

    if not 0 <= n < len(values):
        raise IndexError("n out of range")

    def select(lst, k):
        if len(lst) == 1:
            return lst[0]
        pivot = random.choice(lst)
        lows = [x for x in lst if x < pivot]
        highs = [x for x in lst if x > pivot]
        pivots = [x for x in lst if x == pivot]
        if k < len(lows):
            return select(lows, k)
        elif k < len(lows) + len(pivots):
            return pivot
        else:
            return select(highs, k - len(lows) - len(pivots))

    return select(values, n)
