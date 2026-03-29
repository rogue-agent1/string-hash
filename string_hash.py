#!/usr/bin/env python3
"""String hashing utilities. Zero dependencies."""

def polynomial_hash(s, base=31, mod=10**9+7):
    h = 0
    for ch in s:
        h = (h * base + ord(ch)) % mod
    return h

def rolling_hash(s, window):
    if window > len(s): return []
    base, mod = 31, 10**9+7
    h = 0; pw = pow(base, window - 1, mod)
    hashes = []
    for i in range(len(s)):
        h = (h * base + ord(s[i])) % mod
        if i >= window:
            h = (h - ord(s[i - window]) * pw * base) % mod
        if i >= window - 1:
            hashes.append(h)
    return hashes

def fingerprint(s, seed=0):
    """FNV-1a hash."""
    h = 2166136261 ^ seed
    for ch in s:
        h ^= ord(ch)
        h = (h * 16777619) & 0xFFFFFFFF
    return h

def consistent_hash(key, num_buckets):
    h = fingerprint(key)
    return h % num_buckets

if __name__ == "__main__":
    import sys
    s = sys.argv[1] if len(sys.argv) > 1 else "hello"
    print(f"poly: {polynomial_hash(s)}, fnv: {fingerprint(s)}")
