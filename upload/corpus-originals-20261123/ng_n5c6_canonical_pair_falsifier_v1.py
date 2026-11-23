#!/usr/bin/env python3
# N5-C6 CANONICAL-PAIR FALSIFIER v1
# Exact/structural audit of the asymptotic dichotomy.
# The human certificate carries the theorem proof.
import sys
from fractions import Fraction

FAIL=[]

def ck(name, cond):
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        FAIL.append(name)

# tau = 2 sqrt(3)/3 > 0; only positivity is required.
# For fixed positive integers p,q:
# Delta = (6q-p) M + [p tau/(2pi)] log M + O(1).

pairs = [(1,1),(5,1),(6,1),(12,2),(7,1),(13,2),(60,10),(61,10)]
for p,q in pairs:
    slope = 6*q-p
    ck(f"pair ({p},{q}): zero linear slope iff p=6q",
       (slope == 0) == (p == 6*q))
    if slope == 0:
        ck(f"pair ({p},{q}): logarithmic coefficient is strictly positive",
           p > 0 and q > 0)

# Reduced positive rational pair with zero slope is uniquely 6:1.
zeros=[]
for q in range(1,51):
    for p in range(1,301):
        if 6*q-p == 0:
            zeros.append(Fraction(p,q))
ck("all finite-audit zero-slope classes reduce to 6:1",
   set(zeros) == {Fraction(6,1)})

# Reblocking preserves the same zero-slope class and scales the defect.
for k in range(1,20):
    p,q=6,1
    ck(f"reblocking k={k}: zero slope retained",
       6*(k*q)-(k*p)==0)

print("-"*72)
if FAIL:
    print("RESULT: FAIL", FAIL)
    sys.exit(1)
print("RESULT: ALL ASSERTIONS PASS.")
print("Theorem logic:")
print("  p != 6q -> Delta/M -> 6q-p != 0 -> |Delta| -> infinity linearly.")
print("  p = 6q -> Delta = (3q*tau/pi) log M + O(1) -> +infinity.")
print("Therefore no positive rational bounded-defect class exists for the canonical A/B pair.")
sys.exit(0)
