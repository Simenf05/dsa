"""String algorithms for contests."""

from collections import deque
from typing import Dict, List, Tuple


def kmp_table(pattern: str) -> List[int]:
    """Prefix function (pi table) for KMP."""
    n = len(pattern)
    pi = [0] * n
    j = 0
    for i in range(1, n):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text: str, pattern: str) -> List[int]:
    """Return start indices where pattern occurs in text."""
    if not pattern:
        return list(range(len(text) + 1))
    pi = kmp_table(pattern)
    res: List[int] = []
    j = 0
    for i, c in enumerate(text):
        while j > 0 and c != pattern[j]:
            j = pi[j - 1]
        if c == pattern[j]:
            j += 1
        if j == len(pattern):
            res.append(i - j + 1)
            j = pi[j - 1]
    return res


def z_function(s: str) -> List[int]:
    """Z-function for string s."""
    n = len(s)
    z = [0] * n
    l = 0
    r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z


def rolling_hash(s: str, base: int = 257, mod: int = 2**61 - 1) -> Tuple[List[int], List[int]]:
    """Compute rolling hash (prefix hashes and base powers)."""
    n = len(s)
    h = [0] * (n + 1)
    p = [1] * (n + 1)
    for i, c in enumerate(s):
        h[i + 1] = (h[i] * base + ord(c)) % mod
        p[i + 1] = (p[i] * base) % mod
    return h, p


def substring_hash(h: List[int], p: List[int], l: int, r: int, mod: int = 2**61 - 1) -> int:
    """Hash of s[l:r] using precomputed h and p."""
    return (h[r] - h[l] * p[r - l]) % mod


class TrieNode:
    __slots__ = ("children", "end")

    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


class AhoCorasick:
    """Aho–Corasick for multiple-pattern matching."""

    def __init__(self, patterns: List[str]):
        self._build(patterns)

    def _build(self, patterns: List[str]) -> None:
        self.next = []
        self.link = []
        self.out = []

        self.next.append({})
        self.link.append(0)
        self.out.append([])

        for idx, pat in enumerate(patterns):
            node = 0
            for ch in pat:
                if ch not in self.next[node]:
                    self.next[node][ch] = len(self.next)
                    self.next.append({})
                    self.link.append(0)
                    self.out.append([])
                node = self.next[node][ch]
            self.out[node].append(idx)

        q = deque()
        for ch, nxt in self.next[0].items():
            q.append(nxt)

        while q:
            v = q.popleft()
            for ch, u in self.next[v].items():
                q.append(u)
                j = self.link[v]
                while j and ch not in self.next[j]:
                    j = self.link[j]
                self.link[u] = self.next[j].get(ch, 0)
                self.out[u].extend(self.out[self.link[u]])

    def search(self, text: str) -> List[Tuple[int, int]]:
        """Return list of (pattern_index, end_pos)."""
        res: List[Tuple[int, int]] = []
        node = 0
        for i, ch in enumerate(text):
            while node and ch not in self.next[node]:
                node = self.link[node]
            node = self.next[node].get(ch, 0)
            for pat_id in self.out[node]:
                res.append((pat_id, i))
        return res
