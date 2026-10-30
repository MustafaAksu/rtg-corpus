#!/usr/bin/env python3
"""OFN REF-CLOSURE working note — exact checks (SESSION evidence; not an owner certificate).

usage: python3 -I evidence/ofn/scripts/ofn_ref_closure_check.py [--force-fail]
  exit 0 iff every check passes; --force-fail marks the first check as failed to show that a failure gives exit 1.

Constructions (abelian carrier group H, written additively; graph G connected, edges oriented):
  d : H^V -> H^E, (d s)_{ij} = s_i - s_j          node differences
  Q_node = H^V / H_diag                            node-origin gauge quotient
  C_0 = {r in H^E : oriented sum around every cycle = 0}   closure sector
  Q_edge = H^E / H_diag^E                          one relation as reference (edges measured relative to each other)
  kappa_n : C_0 -> Q_edge, the composite C_0 -> H^E -> Q_edge, on the cycle graph C_n with coherent orientation.

Checks (finite groups Z_N by exhaustive enumeration; R by exact linear algebra):
  R1  d induces a bijection Q_node -> C_0          (K_3, C_4 and K_4; Z_N, N = 2..7)
  R2  on C_n, forgetting one edge is a bijection C_0 -> H^{E minus e0}; on all of H^E it is not injective
  R3  kappa_n has kernel H[n] and cokernel H/nH    (n = 3, 4; Z_N, N = 2..12); over R: det = n
  R4  the diagonal edge action preserves C_0 only for c with n c = 0; the diagonal node action fixes every edge
  R5  control: counts |Q_node| = |C_0| = |Q_edge| agree for every N although kappa_3 fails to be bijective when 3 | N
"""
import itertools, math, sys
import sympy as sp

OK = []


def report(name, ok, detail=""):
    OK.append(bool(ok))
    print(f"{'PASS' if ok else 'FAIL'}  {name}" + (f"  — {detail}" if detail else ""))


GRAPHS = {
    "K3": (3, [(0, 1), (1, 2), (2, 0)], [[(0, 1), (1, 1), (2, 1)]]),
    "C4": (4, [(0, 1), (1, 2), (2, 3), (3, 0)], [[(0, 1), (1, 1), (2, 1), (3, 1)]]),
    # K4: cycle basis 0-1-2-0, 0-2-3-0, 0-1-3-0 with edge signs relative to the listed orientation
    "K4": (4, [(0, 1), (1, 2), (2, 0), (2, 3), (3, 0), (1, 3)],
           [[(0, 1), (1, 1), (2, 1)], [(2, -1), (3, 1), (4, 1)], [(0, 1), (5, 1), (4, 1)]]),
}


def d(s, edges, N):
    return tuple((s[i] - s[j]) % N for i, j in edges)


def closed(r, cycles, N):
    return all(sum(sg * r[e] for e, sg in cyc) % N == 0 for cyc in cycles)


# ---- R1 node-origin gauge quotient = closure sector
ok1, det1 = True, []
for name, (nv, edges, cycles) in GRAPHS.items():
    for N in range(2, 8):
        reps = [s for s in itertools.product(range(N), repeat=nv) if s[0] == 0]      # section of the diagonal action
        img = {d(s, edges, N) for s in reps}
        C0 = {r for r in itertools.product(range(N), repeat=len(edges)) if closed(r, cycles, N)}
        good = len(img) == len(reps) and img == C0
        ok1 &= good
        if not good: det1.append(f"{name},N={N}")
report("R1 d induces a bijection Q_node -> C_0 (K_3, C_4, K_4; Z_N, N=2..7)", ok1, ", ".join(det1) or "image = closure sector, injective on the gauge section")

# ---- R2 forgetting one edge on C_n
ok2 = True
for n in (3, 4):
    edges = [(k, (k + 1) % n) for k in range(n)]
    for N in range(2, 8):
        C0 = [r for r in itertools.product(range(N), repeat=n) if sum(r) % N == 0]
        proj = {r[:-1] for r in C0}
        full = {r[:-1] for r in itertools.product(range(N), repeat=n)}
        ok2 &= len(proj) == len(C0) == N ** (n - 1) and len(full) < N ** n
report("R2 on C_n forgetting one edge is a bijection on C_0 (a parametrization) but not injective on all of H^E", ok2,
       "n=3,4; N=2..7; the lost datum on H^E is the cycle sum (holonomy)")

# ---- R3 kappa_n kernel H[n], cokernel H/nH
ok3, rows = True, []
for n in (3, 4):
    for N in range(2, 13):
        C0 = [r for r in itertools.product(range(N), repeat=n) if sum(r) % N == 0]
        cls = lambda r: tuple((x - r[-1]) % N for x in r)          # representative of r + H_diag with last entry 0
        images = {}
        for r in C0:
            images.setdefault(cls(r), []).append(r)
        ker = len(images.get(tuple([0] * n), []))
        coker = N ** (n - 1) // len(images)                         # |Q_edge| = N^(n-1)
        g = math.gcd(n, N)
        good = ker == g and coker == g and all(len(v) == g for v in images.values())
        ok3 &= good
        if n == 3: rows.append(f"N={N}:{ker}")
report("R3a kappa_n: |ker| = |H[n]| = gcd(n,N) and |coker| = |H/nH| = gcd(n,N) (n=3,4; Z_N, N=2..12)", ok3,
       "n=3 kernel sizes " + " ".join(rows))
for n in (3, 4, 5):
    M = sp.eye(n - 1) + sp.ones(n - 1, n - 1)        # q_k = r_k - r_n with r_n = -(r_1+...+r_{n-1})
    report(f"R3b over R: kappa_{n} in coordinates is I + J, det = {M.det()}", M.det() == n, "bijective over R^d (det != 0)")
# U(1): kernel of kappa_3 = cube roots of unity, via r1^2 r2 = r1 r2^2 = 1
# exact statement on the circle R/Z: (2a+b, a+2b) in Z^2 with a, b in [0,1)  <=>  (a, b) in {0, 1/3, 2/3}-diagonal solutions
ker_u1 = sorted({(sp.Rational(i, 3), sp.Rational(j, 3)) for i in range(3) for j in range(3)
                 if (2 * sp.Rational(i, 3) + sp.Rational(j, 3)).is_integer and (sp.Rational(i, 3) + 2 * sp.Rational(j, 3)).is_integer})
Minv = (sp.eye(2) + sp.ones(2, 2)).inv()
lattice_ok = all(bool(x.is_integer) for x in (3 * Minv))
report("R3c over U(1) = R/Z: ker kappa_3 = {(0,0), (1/3,1/3), (2/3,2/3)} (3-to-1), surjective (U(1) divisible)",
       ker_u1 == [(0, 0), (sp.Rational(1, 3), sp.Rational(1, 3)), (sp.Rational(2, 3), sp.Rational(2, 3))] and lattice_ok,
       f"kernel {ker_u1}; (I+J)^-1 Z^2 is contained in (1/3) Z^2")

# ---- R4 diagonal node vs diagonal edge action
ok4 = True
for n in (3, 4):
    for N in range(2, 10):
        pres = [c for c in range(N) if all(sum((x + c) % N for x in r) % N == 0
                                           for r in itertools.product(range(N), repeat=n) if sum(r) % N == 0)]
        ok4 &= pres == [c for c in range(N) if (n * c) % N == 0]
edges3 = [(0, 1), (1, 2), (2, 0)]
node_triv = all(d(tuple((x + c) % 7 for x in s), edges3, 7) == d(s, edges3, 7) for s in itertools.product(range(7), repeat=3) for c in range(7))
report("R4 diagonal edge shift by c preserves C_0 iff n c = 0; diagonal node shift fixes every edge", ok4 and node_triv,
       "n=3,4; N=2..9 (for U(1), n=3: only cube roots of unity)")

# ---- R5 counts agree although kappa_3 is not bijective when 3 | N
ok5 = True
for N in range(2, 13):
    qn = len({d(s, edges3, N) for s in itertools.product(range(N), repeat=3)})                     # = |Q_node| by R1
    c0 = sum(1 for r in itertools.product(range(N), repeat=3) if sum(r) % N == 0)
    qe = len({tuple((x - r[-1]) % N for x in r) for r in itertools.product(range(N), repeat=3)})
    ok5 &= qn == c0 == qe == N ** 2
fails = [N for N in range(2, 13) if math.gcd(3, N) != 1]
report("R5 control: |Q_node| = |C_0| = |Q_edge| = N^2 on K_3 for every N, yet kappa_3 is not bijective for N in " + str(fails),
       ok5 and fails == [3, 6, 9, 12], "matching counts do not decide the identification")

if "--force-fail" in sys.argv:
    OK[0] = False
    print("FORCED FAIL of R1 (--force-fail)")
ok = len(OK) == 9 and all(OK)
print("RESULT:", "PASS" if ok else "FAIL")
raise SystemExit(0 if ok else 1)
