#!/usr/bin/env python3
"""OFN isolation working note — exact checks (SESSION evidence; not an owner certificate).

usage: python3 -I evidence/ofn/scripts/ofn_isolation_interface_check.py [--force-fail]
  exit 0 iff all seven checks pass; --force-fail marks I1 as failed to show that a failure gives exit 1.

Model (OFN v0.11 §5.5.4, class C, fixed three-edge carrier, primitive clock, transported chart):
    F_e(z) = N(z_e) - (kappa/3) * sum_j N(z_j),   e = 1, 2, 3.
In the complex coordinate of the chart the linear part acts as multiplication by lam = e^{i pi/3}; omega = lam^2.

Proof status of each item (see the working note):
  I1, I2  general identities over arbitrary edge outputs N(z_j) (abstract symbols): these ARE the proofs.
  I3      lock invariance: general two-line argument in the note; here a supporting check with a generic jet.
  I5      zero total interface: exact consequence of I1; supporting jet check.
  I6      diagnostic only: for the test polynomial N_test(z) = lam z + z^2 zbar, kappa = 1/2 (NOT the selected C2 map
          N_Phi; its six-step cubic coefficient differs from the dyad's mu), two states with equal (z_1, b_1) have
          different next b_1. It shows that one-step sufficiency does not by itself give closed reduced dynamics; it does
          not prove the same for the selected C2 map.
  I7      kappa = 0 control.
Generic jets: all monomials z^a zbar^b of degree <= 7 allowed by the stated symmetry, with independent symbolic
coefficients; conjugation is handled with z = x + i y, x, y real. A finite jet is supporting evidence, not a proof.
"""
import itertools
import sympy as sp

x, y, u, v = sp.symbols("x y u v", real=True)
k = sp.symbols("kappa", real=True)
lam = sp.Rational(1, 2) + sp.sqrt(3) * sp.I / 2
om = lam**2
OK = []


def report(name, ok, detail=""):
    OK.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {detail}" if detail else ""))


def zero(e):
    e = sp.expand(e)
    return sp.simplify(sp.re(e)) == 0 and sp.simplify(sp.im(e)) == 0


def jet(rule, deg=7, tag="c"):
    """Generic polynomial map with complex symbolic coefficients over monomials z^a zbar^b allowed by rule(a, b)."""
    mons = [(a, b) for a in range(deg + 1) for b in range(deg + 1) if 1 <= a + b <= deg and rule(a, b)]
    cs = [sp.Symbol(f"{tag}r{a}_{b}", real=True) + sp.I * sp.Symbol(f"{tag}i{a}_{b}", real=True) for a, b in mons]
    def G(w):
        wb = sp.conjugate(w)
        return sp.expand(sum(c * w**a * wb**b for c, (a, b) in zip(cs, mons)))
    return G, mons


def F(G, Z, kap=k):
    s = sum(G(w) for w in Z)
    return [sp.expand(G(w) - kap * s / 3) for w in Z]


# ---- I1 exact interface identity and injectivity (abstract outputs n1, n2, n3)
n = [sp.Symbol(f"n{j}r", real=True) + sp.I * sp.Symbol(f"n{j}i", real=True) for j in (1, 2, 3)]
Fn = [n[e] - k * sum(n) / 3 for e in range(3)]
ident = all(zero(Fn[e] - n[e] + k / 3 * (n[e] + (sum(n) - n[e]))) for e in range(3))
L = lambda ne, b: (1 - k / 3) * ne - k / 3 * b
iface = all(zero(Fn[e] - L(n[e], sum(n) - n[e])) for e in range(3))
b1, b2 = sp.symbols("b1 b2")
inj = zero(L(n[0], b1) - L(n[0], b2) + k / 3 * (b1 - b2))
report("I1 F_e - N(z_e) = -(kappa/3)(N(z_e) + b_e) and F_e = L_kappa(z_e, b_e), b_e = sum_{j!=e} N(z_j)", ident and iface,
       "identity over arbitrary outputs; no symmetry or truncation used")
report("I2 L_kappa(z_e, b) - L_kappa(z_e, b') = -(kappa/3)(b - b')", inj,
       "for kappa != 0, distinct interface values give distinct edge outputs")

# ---- I3 lock invariance for a generic lam-equivariant jet (a - b = 1 mod 6)
N, monsN = jet(lambda a, b: (a - b) % 6 == 1, tag="N")
z = x + sp.I * y
f0 = F(N, [z, -z, 0])
s0 = zero(f0[0] - N(z)) and zero(f0[1] - N(-z)) and zero(f0[2])
ok_pm = True
for s in (1, 2):
    w1, w2 = om ** (s % 3), om ** ((2 * s) % 3)
    fp = F(N, [z, w1 * z, w2 * z])
    ok_pm &= zero(fp[0] - N(z)) and zero(fp[1] - N(w1 * z)) and zero(fp[2] - N(w2 * z))
report("I3 lock surfaces S_0, S_+, S_- invariant with exact edge law N (generic equivariant jet)", s0 and ok_pm,
       f"{len(monsN)} monomials up to degree 7; supporting check of the general argument")

# ---- I5 zero total interface: b_1 = 0 with nonzero neighbours (z, w, -w); and the single-edge state (z, 0, 0)
w = u + sp.I * v
fq = F(N, [z, w, -w])
q1 = zero(fq[0] - (1 - k / 3) * N(z))
fs = F(N, [z, 0, 0])
s1 = zero(fs[0] - (1 - k / 3) * N(z)) and zero(fs[1] + k / 3 * N(z)) and zero(fs[2] + k / 3 * N(z))
lin = sp.expand(sp.diff(fs[1], x).subs({x: 0, y: 0}))
report("I5 b_1 = 0 gives F_1 = (1 - kappa/3) N(z_1), also for nonzero neighbours (w, -w)", q1)
report("I5b (z,0,0) is not invariant for kappa != 0: F_2 = F_3 = -(kappa/3) N(z)", s1 and sp.simplify(lin) != 0,
       f"d F_2/dx at 0 = {sp.simplify(lin)}, i.e. -(kappa/3) x (linear coefficient of N), = -(kappa/3) lam in the model")

# ---- I6 diagnostic: equal (z_1, b_1), different next b_1, for the test polynomial N_test = lam z + z^2 zbar, kappa = 1/2
Nc = lambda t: sp.expand(lam * t + t**2 * sp.conjugate(t))
kc = sp.Rational(1, 2)
def step(Z):
    s = sum(Nc(t) for t in Z)
    return [sp.expand(Nc(t) - kc * s / 3) for t in Z]
z0 = sp.Rational(1, 10)
A_ = [z0, sp.Rational(1, 10), -sp.Rational(1, 10)]
B_ = [z0, sp.Rational(1, 5) * sp.I, -sp.Rational(1, 5) * sp.I]
bA = sum(Nc(t) for t in A_[1:]); bB = sum(Nc(t) for t in B_[1:])
nA, nB = step(A_), step(B_)
nbA = sum(Nc(t) for t in nA[1:]); nbB = sum(Nc(t) for t in nB[1:])
report("I6 diagnostic (N_test, not C2): one-step sufficiency does not give closed reduced dynamics", zero(bA - bB) and zero(nA[0] - nB[0]) and not zero(nbA - nbB),
       f"next b_1 differs by {sp.nsimplify(sp.simplify(nbA - nbB))}")

# ---- I7 kappa = 0 control: decoupled, residual vanishes, zero interface recovers N
f00 = F(N, [z, w, -w], kap=0)
report("I7 control kappa = 0: F_e = N(z_e) for every state", zero(f00[0] - N(z)) and zero(f00[1] - N(w)))

import sys
if "--force-fail" in sys.argv:
    OK[0] = False
    print("FORCED FAIL of I1 (--force-fail)")
ok = len(OK) == 7 and all(OK)
print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
