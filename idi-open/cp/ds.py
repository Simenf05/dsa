"""Common data structures used in contests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, List, Optional, TypeVar

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self._data: List[T] = []

    def push(self, x: T) -> None:
        self._data.append(x)

    def pop(self) -> T:
        return self._data.pop()

    def top(self) -> Optional[T]:
        return self._data[-1] if self._data else None

    def empty(self) -> bool:
        return not self._data


class Queue(Generic[T]):
    def __init__(self):
        self._data: List[T] = []
        self._head = 0

    def push(self, x: T) -> None:
        self._data.append(x)

    def pop(self) -> T:
        assert self._head < len(self._data)
        val = self._data[self._head]
        self._head += 1
        if self._head > 100 and self._head * 2 > len(self._data):
            self._data = self._data[self._head :]
            self._head = 0
        return val

    def empty(self) -> bool:
        return self._head >= len(self._data)


class Deque(Generic[T]):
    def __init__(self):
        self._data: List[T] = []

    def push_back(self, x: T) -> None:
        self._data.append(x)

    def push_front(self, x: T) -> None:
        self._data.insert(0, x)

    def pop_back(self) -> T:
        return self._data.pop()

    def pop_front(self) -> T:
        return self._data.pop(0)

    def empty(self) -> bool:
        return not self._data


class UnionFind:
    """Disjoint set union / union-find."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True


class FenwickTree:
    """Binary Indexed Tree for prefix sums."""

    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i: int, v: int) -> None:
        """Add v at index i (0-indexed)."""
        i += 1
        while i <= self.n:
            self.bit[i] += v
            i += i & -i

    def sum(self, i: int) -> int:
        """Prefix sum [0..i]."""
        i += 1
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def range_sum(self, l: int, r: int) -> int:
        return self.sum(r) - (self.sum(l - 1) if l > 0 else 0)


class SegmentTree:
    """Segment tree for range queries and point updates."""

    def __init__(self, data: List[int], func=min, default=10**18):
        self.n = len(data)
        self.func = func
        self.default = default
        self.size = 1
        while self.size < self.n:
            self.size *= 2
        self.tree = [default] * (2 * self.size)
        for i in range(self.n):
            self.tree[self.size + i] = data[i]
        for i in range(self.size - 1, 0, -1):
            self.tree[i] = func(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, i: int, value: int) -> None:
        i += self.size
        self.tree[i] = value
        i //= 2
        while i:
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2

    def query(self, l: int, r: int) -> int:
        """Query in [l, r)"""
        res = self.default
        l += self.size
        r += self.size
        while l < r:
            if l & 1:
                res = self.func(res, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                res = self.func(res, self.tree[r])
            l //= 2
            r //= 2
        return res


@dataclass
class TreapNode:
    key: int
    prio: int
    left: Optional["TreapNode"] = None
    right: Optional["TreapNode"] = None
    size: int = 1


def treap_size(node: Optional[TreapNode]) -> int:
    return node.size if node else 0


def treap_update(node: Optional[TreapNode]) -> None:
    if node:
        node.size = 1 + treap_size(node.left) + treap_size(node.right)


def treap_split(root: Optional[TreapNode], key: int):
    if not root:
        return None, None
    if key < root.key:
        left, right = treap_split(root.left, key)
        root.left = right
        treap_update(root)
        return left, root
    else:
        left, right = treap_split(root.right, key)
        root.right = left
        treap_update(root)
        return root, right


def treap_merge(a: Optional[TreapNode], b: Optional[TreapNode]) -> Optional[TreapNode]:
    if not a or not b:
        return a or b
    if a.prio < b.prio:
        a.right = treap_merge(a.right, b)
        treap_update(a)
        return a
    else:
        b.left = treap_merge(a, b.left)
        treap_update(b)
        return b


def treap_insert(root: Optional[TreapNode], node: TreapNode) -> TreapNode:
    if not root:
        return node
    if node.prio < root.prio:
        left, right = treap_split(root, node.key)
        node.left, node.right = left, right
        treap_update(node)
        return node
    if node.key < root.key:
        root.left = treap_insert(root.left, node)
    else:
        root.right = treap_insert(root.right, node)
    treap_update(root)
    return root


def treap_find(root: Optional[TreapNode], key: int) -> bool:
    while root:
        if key == root.key:
            return True
        root = root.left if key < root.key else root.right
    return False
