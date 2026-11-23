#!/usr/bin/env python3
"""Exact arithmetic certificate for N-3C+ roots-of-unity projector facts.

This certificate verifies residue/slot statements that do not require the
full OPEN-9 coefficient engine:
  1) vector-monomial charge chi_p(a,b)=a-b-1 mod p;
  2) p=6 resonant slots through degree 5;
  3) first pure anti-holomorphic resonant slot b=p-1;
  4) q=4 subgroup permission of target (0,3) for both p=8 and p=12.

It does NOT compute nonlinear OPEN-9 cascade coefficients.
"""
from fractions import Fraction


def charge(p, a, b):
    return (a - b - 1) % p


def resonant(p, a, b):
    return charge(p, a, b) == 0


def slots(p, D):
    return [(a, D-a) for a in range(D+1) if resonant(p, a, D-a)]

print("N-3C+ roots-of-unity projector certificate")
print("charge chi_p(a,b)=a-b-1 mod p")

expected_p6 = {
    2: [],
    3: [(2,1)],
    4: [],
    5: [(0,5),(3,2)],
}
for D, exp in expected_p6.items():
    got = slots(6, D)
    assert got == exp, (D, got, exp)
    print(f"p=6 degree {D}: {got}")

for p in range(3, 21):
    first = next(b for b in range(1, 3*p+1) if resonant(p, 0, b))
    assert first == p-1, (p, first)
print("pure anti-holomorphic first resonant slot: (0,p-1) for p=3..20 PASS")

# q=4 subgroup target (0,3)
assert resonant(4, 0, 3)
assert not resonant(8, 0, 3)
assert not resonant(12, 0, 3)
print("target (0,3): q=4 subgroup-resonant; not full-p resonant for p=8 or p=12")
print("  chi_4(0,3)=", charge(4,0,3))
print("  chi_8(0,3)=", charge(8,0,3))
print("  chi_12(0,3)=", charge(12,0,3))

# Degree-2 no-cascade statement: if degree 2 is the first nonlinear degree,
# there is no lower-degree nonlinear cascade, and p=6 has no resonant degree-2 slots.
assert slots(6,2) == []
print("p=6 degree-2 resonant support empty: direct cyclic average is zero; with no lower nonlinear degree, degree-2 p-step term is kinematically absent.")

print("ALL ASSERTIONS PASSED")
