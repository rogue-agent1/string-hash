from string_hash import polynomial_hash, rolling_hash, fingerprint, consistent_hash
h1 = polynomial_hash("hello")
h2 = polynomial_hash("hello")
h3 = polynomial_hash("world")
assert h1 == h2
assert h1 != h3
rh = rolling_hash("abcde", 3)
assert len(rh) == 3  # abc, bcd, cde
assert rh[0] == polynomial_hash("abc")
f1 = fingerprint("test")
f2 = fingerprint("test")
assert f1 == f2
assert fingerprint("a") != fingerprint("b")
b = consistent_hash("key1", 10)
assert 0 <= b < 10
assert consistent_hash("key1", 10) == consistent_hash("key1", 10)
print("string_hash tests passed")
