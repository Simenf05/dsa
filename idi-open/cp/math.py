"""Math and number theory utilities for competitive programming."""

from __future__ import annotations

import math
from typing import List, Tuple


def gcd(a: int, b: int) -> int:
    """Greatest common divisor."""
    return math.gcd(a, b)


def extgcd(a: int, b: int) -> Tuple[int, int, int]:
    """Extended GCD: returns (g, x, y) such that a*x + b*y == g == gcd(a, b)."""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extgcd(b, a % b)
    return g, y1, x1 - (a // b) * y1


def modpow(a: int, e: int, mod: int) -> int:
    """Modular exponentiation."""
    res = 1
    a %= mod
    while e > 0:
        if e & 1:
            res = (res * a) % mod
        a = (a * a) % mod
        e //= 2
    return res


def modinv(a: int, mod: int) -> int:
    """Modular inverse (mod must be prime or a and mod coprime)."""
    g, x, _ = extgcd(a, mod)
    if g != 1:
        raise ValueError("Modular inverse does not exist")
    return x % mod


def sieve(n: int) -> List[int]:
    """Sieve of Eratosthenes. Returns list of primes <= n."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            for j in range(start, n + 1, step):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]


def prime_factors(n: int) -> List[Tuple[int, int]]:
    """Prime factorization as list of (prime, exponent)."""
    res: List[Tuple[int, int]] = []
    if n < 0:
        n = -n
    for p in (2, 3):
        if n % p == 0:
            cnt = 0
            while n % p == 0:
                n //= p
                cnt += 1
            res.append((p, cnt))
    f = 5
    while f * f <= n:
        for d in (f, f + 2):
            if n % d == 0:
                cnt = 0
                while n % d == 0:
                    n //= d
                    cnt += 1
                res.append((d, cnt))
        f += 6
    if n > 1:
        res.append((n, 1))
    return res


def nCr_mod(n: int, r: int, mod: int) -> int:
    """Compute n choose r modulo mod (mod should be prime for inverse)."""
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    num = 1
    den = 1
    for i in range(1, r + 1):
        num = (num * (n - r + i)) % mod
        den = (den * i) % mod
    return num * modinv(den, mod) % mod
