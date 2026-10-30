#!/usr/bin/env python3
"""OFN 3B-independence working note — exact checks (SESSION evidence; not an owner certificate).

usage: python3 -I evidence/ofn/scripts/ofn_3b_independence_check.py [--force-fail]
  exit 0 iff every check passes; --force-fail marks the first check as failed to show that a failure gives exit 1.

Coordinates: real plane x = (rho, eta), the lifted chart of DYAD-DEF-PRIMITIVE-MAP at P_1 = (0,0) (dyad-v6.4.22 §1):
    T(rho, eta) = (rho - sin eta, eta + (e^rho - 1) - sin eta),   A = DT(0) = [[1,-1],[1,0]].
Uniform recipe (class C form, OFN v0.11 §5.5.4):  T3[G](x1,x2,x3)_e = G(x_e) - (kappa/3) sum_j G(x_j).
Embeddings:  iota_0(x) = (x, -x, 0),   iota_+(x) = (x, A^2 x, A^4 x),   iota_-(x) = (x, A^4 x, A^2 x).
Classes:     G_odd = {G : G(-x) = -G(x)};   G_omega = {G : G(0) = 0, G(A^2 x) = A^2 G(x)};   G_A = {G : G(Ax) = A G(x)}.

Checks:
  K1  linear identities A^3 = -I, A^6 = I, I + A^2 + A^4 = 0 (exact)
  K2  iota_0 intertwining T3[G] o iota_0 = iota_0 o G for a generic odd jet (degree <= 5)
  K3  iota_+ and iota_- intertwining for a generic G_omega jet (degree <= 4; includes even-degree terms)
  K4  falsifier for the specific quadratic q(rho, eta) = (rho*eta, rho^2): G = x + q breaks iota_0 and iota_+
      (not every quadratic breaks iota_+: an A^2-equivariant quadratic preserves it, cf. K3)
  K5  premise -> implication: every G_A jet (built by A-averaging a generic jet) is odd and in G_omega (owner premise
      for C2: [N_Phi, A] = 0, IMP-O10-07; the theorem itself is not re-proved here)
  K6  raw T in the raw chart: T(-x) + T(x) = (0, 2(cosh rho - 1)) exactly (not odd); not A-commuting and not
      A^2-equivariant (order-2 Taylor residuals)
  K7  consequence: in the raw chart the named embedding iota_0 is not invariant under T3[T] for kappa != 0
      (only this embedding is tested; the general raw no-go is the owner result RTG-OFN-ALG-RAW-STANDARD-C-NOGO)
"""
import itertools, sys
import sympy as sp

OK = []
r, e, k = sp.symbols("rho eta kappa", real=True)
A = sp.Matrix([[1, -1], [1, 0]])
I2 = sp.eye(2)


def report(name, ok, detail=""):
    OK.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {detail}" if detail else ""))


def vzero(v):
    return all(sp.expand(c) == 0 for c in v)


def jet(deg, rule, tag):
    """Generic real polynomial map R^2 -> R^2 with monomials rho^a eta^b, 1 <= a+b <= deg, rule(a+b)."""
    mons = [(a, b) for a in range(deg + 1) for b in range(deg + 1) if 1 <= a + b <= deg and rule(a + b)]
    cs = [[sp.Symbol(f"{tag}{i}_{a}_{b}", real=True) for (a, b) in mons] for i in (0, 1)]
    def G(x):
        u, w = x
        return sp.Matrix([sp.expand(sum(c * u**a * w**b for c, (a, b) in zip(cs[i], mons))) for i in (0, 1)])
    return G


def T3(G, X, kap=k):
    outs = [G(x) for x in X]
    s = outs[0] + outs[1] + outs[2]
    return [sp.expand(o - kap * s / 3) for o in outs]


x = sp.Matrix([r, e])
A2, A4 = A**2, A**4
i0 = lambda v: [v, -v, sp.zeros(2, 1)]
ip = lambda v: [v, A2 * v, A4 * v]
im = lambda v: [v, A4 * v, A2 * v]


def intertwines(G, iota):
    lhs = T3(G, iota(x))
    rhs = iota(G(x))
    return all(vzero(a - b) for a, b in zip(lhs, rhs))


# K1
report("K1 A^3 = -I, A^6 = I, I + A^2 + A^4 = 0", A**3 == -I2 and A**6 == I2 and I2 + A2 + A4 == sp.zeros(2))

# K2 odd class -> iota_0
Godd = jet(5, lambda d: d % 2 == 1, "o")
report("K2 iota_0 intertwines for every odd G (generic jet, degree <= 5)", intertwines(Godd, i0),
       "class G_odd makes no reference to T")

# K3 omega class -> iota_+-   (generic jet projected onto G_omega by A^2-averaging)
P = jet(4, lambda d: True, "p")
def Gom(v):
    return sp.expand((P(v) + A2.inv() * P(A2 * v) + A4.inv() * P(A4 * v)) / 3)
om_ok = vzero(Gom(A2 * x) - A2 * Gom(x))
not_odd = not vzero(Gom(-x) + Gom(x))
report("K3 iota_+ and iota_- intertwine for every G in G_omega (generic jet, degree <= 4)",
       om_ok and intertwines(Gom, ip) and intertwines(Gom, im) and not_odd,
       "the jet is A^2-equivariant and not odd, so oddness is not used; G_omega uses omega = A^2, linear T-data")

# K4 falsifier
Gq = lambda v: sp.Matrix([v[0] + v[0] * v[1], v[1] + v[0]**2])
report("K4 falsifier for q = (rho*eta, rho^2): G = x + q breaks iota_0 and iota_+", not intertwines(Gq, i0) and not intertwines(Gq, ip),
       "specific q only; A^2-equivariant quadratics preserve iota_+")

# K5 premise [G, A] = 0  ->  odd and A^2-equivariant
Q = jet(4, lambda d: True, "q")
def GA(v):
    return sp.expand(sum(((A**j).inv() * Q((A**j) * v) for j in range(6)), sp.zeros(2, 1)) / 6)
comm = vzero(GA(A * x) - A * GA(x))
report("K5 [G, A] = 0 implies G odd and G(A^2 x) = A^2 G(x) (A-averaged generic jet)",
       comm and vzero(GA(-x) + GA(x)) and vzero(GA(A2 * x) - A2 * GA(x)) and intertwines(GA, i0) and intertwines(GA, ip),
       "premise for C2 is the owner commutation of N_Phi with A (IMP-O10-07); even-degree terms average to zero")

# K6 raw T in the raw chart
def Tm(v):
    return sp.Matrix([v[0] - sp.sin(v[1]), v[1] + sp.exp(v[0]) - 1 - sp.sin(v[1])])
def taylor2(expr):
    t = sp.Symbol("t")
    s = sp.series(expr.subs({r: t * r, e: t * e}), t, 0, 3).removeO()
    return sp.expand(s.subs(t, 1))
odd_exact = [sp.simplify((c - d).rewrite(sp.exp)) == 0 for c, d in zip(Tm(-x) + Tm(x), [0, 2 * (sp.cosh(r) - 1)])]
odd_res = [taylor2(c) for c in (Tm(-x) + Tm(x))]
comm_res = [taylor2(c) for c in (Tm(A * x) - A * Tm(x))]
om_res = [taylor2(c) for c in (Tm(A2 * x) - A2 * Tm(x))]
lin_ok = sp.Matrix([[sp.diff(c, v).subs({r: 0, e: 0}) for v in (r, e)] for c in Tm(x)]) == A
report("K6 raw T (lifted chart at P_1): T(-x)+T(x) = (0, 2(cosh rho - 1)); not A-commuting, not A^2-equivariant", lin_ok and all(odd_exact) and
       any(c != 0 for c in odd_res) and any(c != 0 for c in comm_res) and any(c != 0 for c in om_res),
       f"exact identity checked; order 2: {odd_res}; DT(0) = A")

# K7 raw embedding iota_0 not invariant under T3[T]
out = T3(Tm, i0(x))
third = [taylor2(c) for c in out[2]]
third_exact = all(sp.simplify((c - d).rewrite(sp.exp)) == 0 for c, d in zip(out[2], [0, -2 * k * (sp.cosh(r) - 1) / 3]))
report("K7 in the raw chart, iota_0 is not invariant under T3[T] for kappa != 0", third_exact and any(c != 0 for c in third),
       "third edge after one step = (0, -(2 kappa/3)(cosh rho - 1)) exactly; it would be 0 on an invariant iota_0")

if "--force-fail" in sys.argv:
    OK[0] = False
    print("FORCED FAIL of K1 (--force-fail)")
ok = len(OK) == 7 and all(OK)
print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
