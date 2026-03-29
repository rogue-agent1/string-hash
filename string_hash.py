#!/usr/bin/env python3
"""String hashing algorithms — Rabin-Karp, FNV, DJB2, polynomial."""
import sys

def djb2(s):
    h = 5381
    for c in s:
        h = ((h << 5) + h + ord(c)) & 0xFFFFFFFF
    return h

def fnv1a(s):
    h = 0x811c9dc5
    for c in s:
        h ^= ord(c)
        h = (h * 0x01000193) & 0xFFFFFFFF
    return h

def poly_hash(s, base=31, mod=10**9+7):
    h = 0
    for c in s:
        h = (h * base + ord(c)) % mod
    return h

def rabin_karp(text, pattern):
    if not pattern: return []
    n, m = len(text), len(pattern)
    if m > n: return []
    base, mod = 256, 10**9+7
    ph = th = 0
    power = pow(base, m-1, mod)
    for i in range(m):
        ph = (ph * base + ord(pattern[i])) % mod
        th = (th * base + ord(text[i])) % mod
    results = []
    for i in range(n - m + 1):
        if ph == th and text[i:i+m] == pattern:
            results.append(i)
        if i < n - m:
            th = (th - ord(text[i]) * power) % mod
            th = (th * base + ord(text[i+m])) % mod
    return results

def test():
    assert djb2("hello") == djb2("hello")
    assert djb2("hello") != djb2("world")
    assert fnv1a("test") != fnv1a("tset")
    assert poly_hash("abc") != poly_hash("abd")
    r = rabin_karp("abcabcabc", "abc")
    assert r == [0, 3, 6]
    assert rabin_karp("hello", "xyz") == []
    assert rabin_karp("aaa", "a") == [0, 1, 2]
    print("  string_hash: ALL TESTS PASSED")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test": test()
    else: print("String hashing algorithms")
