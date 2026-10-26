#!/usr/bin/env python3
# =============================================================================
# NG-7A CERTIFICATE — ADDITIVE RECURRENCE-HOLONOMY OPERATOR / NULL THEOREM  v1
# =============================================================================
# Target: RTG Number Genesis DSN v1.4.1 -> v1.5, module NG-7A
#   (Sub-RID NUMGEN-OPEN-REC-HOL-OPERATOR), PI-locked package 2026-08-28:
#     core:  A = D^T X  =>  C A = 0
#     (1) orientation consistency, (2) gauge invariance,
#     (3) cycle-basis invariance of the declared statistic,
#     (4) typed scalar-vs-multichannel distinction
#   plus: completeness/exactness over field coefficients, TDR-G Z_N
#   zero-control, multiplicative-layer spot theorem, domain convention,
#   separation instances (cycle capacity != holonomy content).
#
# Terminology per PI ruling: for scalar edge data a in R^E the primitive
# observable is the holonomy VECTOR h = C a (equivalently the class
# [a] in H^1 = R^E / im D^T); rank(C a) is NEVER called a holonomy rank.
# r_hol = rank(C A) is reserved for genuinely multi-channel A in R^{E x d},
# d >= 2.
#
# All arithmetic exact: sympy Rational / Python int (mod N for TDR-G control).
# Exit code 0 iff every assertion passes.
# =============================================================================

import sys
import random
from fractions import Fraction

import sympy as sp

random.seed(20260828)
FAILURES = []


def check(name, cond):
    tag = "PASS" if cond else "FAIL"
    print(f"[{tag}] {name}")
    if not cond:
        FAILURES.append(name)


# ---------------------------------------------------------------- graph layer
class Graph:
    """Finite directed multigraph. Edges: list of (tail, head). Loops and
    parallel edges allowed. D[v,e] = +1 if v=head(e), -1 if v=tail(e), 0 else
    (a self-loop column is identically zero)."""

    def __init__(self, n, edges, name):
        self.n = n
        self.edges = list(edges)
        self.m = len(self.edges)
        self.name = name
        D = sp.zeros(n, self.m)
        for j, (t, h) in enumerate(self.edges):
            if t != h:
                D[h, j] += 1
                D[t, j] -= 1
        self.D = D
        # connected components (underlying undirected, isolated loops count)
        parent = list(range(n))

        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u

        for (t, h) in self.edges:
            ru, rv = find(t), find(h)
            if ru != rv:
                parent[ru] = rv
        self.c = len({find(v) for v in range(n)})
        self.beta = self.m - self.n + self.c  # first Betti number
        # cycle-basis matrix C: rows = basis of ker D over Q
        ns = self.D.nullspace()
        if ns:
            rows = []
            for v in ns:
                den = sp.lcm([sp.fraction(x)[1] for x in v])
                rows.append((v * den).T)
            self.C = sp.Matrix.vstack(*rows)
        else:
            self.C = sp.zeros(0, self.m)
        self.comp_of = [find(v) for v in range(n)]


def rand_vec(k, lo=-9, hi=9):
    return sp.Matrix([sp.Rational(random.randint(lo, hi)) for _ in range(k)])


def rand_mat(r, ccols, lo=-9, hi=9):
    return sp.Matrix(r, ccols,
                     [sp.Rational(random.randint(lo, hi)) for _ in range(r * ccols)])


def rand_glq(k):
    while True:
        M = rand_mat(k, k, -5, 5)
        if k == 0 or M.det() != 0:
            return M


def rand_signs(m):
    return sp.diag(*[sp.Integer(random.choice((1, -1))) for _ in range(m)])


def solvable(M, b):
    return M.row_join(b).rank() == M.rank()


def petersen():
    outer = [(i, (i + 1) % 5) for i in range(5)]
    spokes = [(i, i + 5) for i in range(5)]
    inner = [(5 + i, 5 + (i + 2) % 5) for i in range(5)]
    return Graph(10, outer + spokes + inner, "Petersen")


def random_connected(n, extra, tag):
    edges = []
    for v in range(1, n):
        u = random.randrange(v)
        edges.append((u, v) if random.random() < 0.5 else (v, u))
    for _ in range(extra):
        u, v = random.randrange(n), random.randrange(n)
        if u != v:
            edges.append((u, v))
    return Graph(n, edges, tag)


GRAPHS = [
    Graph(3, [(0, 1), (1, 2), (2, 0)], "K3"),
    Graph(4, [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)], "K4"),
    Graph(6, [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)], "TwoTriangles(c=2)"),
    Graph(7, [(0, 1), (1, 2), (1, 3), (0, 4), (4, 5), (4, 6)], "Forest(beta=0)"),
    Graph(3, [(0, 1), (0, 1), (1, 2), (2, 2)], "Multi(parallel+loop)"),
    petersen(),
    random_connected(8, 6, "Rand8"),
    random_connected(12, 9, "Rand12"),
]

# ------------------------------------------------- S1: structural certificate
ok = True
for G in GRAPHS:
    ok &= (G.D * G.C.T == sp.zeros(G.n, G.C.rows))          # rows in ker D
    ok &= (G.C.rank() == G.beta)                             # basis size
    ok &= (G.D.rank() == G.n - G.c)                          # incidence rank
check("S1 structure: C spans ker D, rank C = beta = m-n+c, rank D = n-c "
      "(all graphs incl. multigraph, forest, Petersen)", ok)

# --------------------------------------- T1: core null theorem  C D^T X = 0
ok = True
for G in GRAPHS:
    ok &= (G.C * G.D.T == sp.zeros(G.C.rows, G.n))           # matrix identity
    for _ in range(4):
        x = rand_vec(G.n)
        ok &= (G.C * (G.D.T * x) == sp.zeros(G.C.rows, 1))   # sampled
check("T1 null theorem: C*D^T = 0 as exact matrix identity and "
      "h(D^T x) = 0 for sampled potentials (all graphs)", ok)

# ---------------- T2: completeness / exactness over Q:  im D^T = ker(C·)
ok = True
for G in GRAPHS:
    # dimension certificate: dim ker(C·) = m - beta = n - c = dim im D^T,
    # together with im D^T subset ker(C·) from T1  =>  equality.
    ok &= (G.m - G.beta == G.n - G.c)
    for _ in range(6):
        a = rand_vec(G.m)
        flat = (G.C * a == sp.zeros(G.C.rows, 1)) if G.C.rows else True
        ok &= (flat == solvable(G.D.T, a))
    # engineered flat sample
    a = G.D.T * rand_vec(G.n)
    ok &= solvable(G.D.T, a)
check("T2 completeness over field coefficients: im D^T = ker(C·) by exact "
      "dimension count + sampled equivalence h=0 <=> D^T x = a solvable", ok)

# --------------------------- T3: orientation consistency (edges and cycles)
ok = True
for G in GRAPHS:
    if G.C.rows == 0:
        continue
    S = rand_signs(G.m)                        # flip edge directions
    a = rand_vec(G.m)
    # reoriented graph: D' = D S, valid basis C' = C S, data a' = S a
    ok &= ((G.D * S) * (G.C * S).T == sp.zeros(G.n, G.C.rows))
    ok &= ((G.C * S) * (S * a) == G.C * a)     # holonomy vector invariant
    # cycle-traversal reversal: negate one basis row -> that component flips
    i = random.randrange(G.C.rows)
    N = sp.eye(G.C.rows)
    N[i, i] = -1
    ok &= ((N * G.C) * a == N * (G.C * a))
    ok &= (((N * G.C) * a == sp.zeros(G.C.rows, 1)) ==
           (G.C * a == sp.zeros(G.C.rows, 1)))  # zero-set invariant
check("T3 orientation consistency: h invariant under simultaneous edge "
      "reorientation (C S, S a); row reversal flips only that component; "
      "zero-set invariant", ok)

# ------------------------------------------------------- T4: gauge invariance
ok = True
for G in GRAPHS:
    a = rand_vec(G.m)
    g = rand_vec(G.n)
    ok &= (G.C * (a + G.D.T * g) == G.C * a)   # gauge shift of edge data
    for comp in range(G.c):                    # per-component constant shift
        ind = sp.Matrix([1 if G.comp_of[v] == comp else 0 for v in range(G.n)])
        ok &= (G.D.T * ind == sp.zeros(G.m, 1))
check("T4 gauge invariance: h(a + D^T g) = h(a); per-component constant "
      "potential shifts are exact gauge (D^T 1_comp = 0)", ok)

# ------------------------ T5: cycle-basis covariance / invariant statistics
ok = True
for G in GRAPHS:
    if G.C.rows == 0:
        continue
    M = rand_glq(G.C.rows)
    a = rand_vec(G.m)
    A = rand_mat(G.m, 3)
    ok &= ((M * G.C) * a == M * (G.C * a))                   # h' = M h
    ok &= (((M * G.C) * a == sp.zeros(G.C.rows, 1)) ==
           (G.C * a == sp.zeros(G.C.rows, 1)))               # zero-set
    ok &= (((M * G.C) * A).rank() == (G.C * A).rank())       # rank invariant
check("T5 basis change C -> M C (M in GL(beta,Q)): h' = M h exactly; "
      "zero-set and multi-channel rank invariant", ok)

# ---------------- T6: typed scalar vs multi-channel statistic (PI ruling)
ok = True
scalar_ranks = set()
for G in GRAPHS:
    if G.C.rows == 0:
        continue
    for _ in range(5):
        a = rand_vec(G.m)
        scalar_ranks.add((G.C * a).rank())
    scalar_ranks.add((G.C * (G.D.T * rand_vec(G.n))).rank())  # flat => 0
    A = rand_mat(G.m, 4)
    R = rand_glq(4)
    H = G.C * A
    ok &= ((G.C * (A * R)).rank() == H.rank())               # channel GL-inv
    ok &= (H.rank() <= min(G.beta, 4))                       # bound
    Aflat = G.D.T * rand_mat(G.n, 4)
    ok &= ((G.C * Aflat).rank() == 0)                        # flat => 0
    # per-channel completeness: r_hol = 0 <=> every channel integrable
    ok &= all(solvable(G.D.T, Aflat[:, j]) for j in range(4))
    mixed = Aflat[:, 0].row_join(G.C.T[:, 0])                # flat + cycle col
    ok &= ((G.C * mixed).rank() == 1)
ok &= (scalar_ranks <= {0, 1} and scalar_ranks == {0, 1})
check("T6 typing: rank(C a) in {0,1} for every scalar sample (both values "
      "realized) — scalar observable is h, never a 'rank'; r_hol = rank(CA) "
      "for d>=2 is channel-GL invariant, <= min(beta,d), 0 iff all channels "
      "integrable; mixed witness has r_hol = 1", ok)

# ------- T7: separation instances — cycle capacity != holonomy content
ok = True
for G in [g for g in GRAPHS if g.beta > 0]:
    Aflat = G.D.T * rand_mat(G.n, G.beta)
    ok &= (G.beta > 0 and (G.C * Aflat).rank() == 0)         # capacity, no content
    Awit = G.C.T                                             # columns = cycles
    ok &= ((G.C * Awit).rank() == G.beta)                    # full content
check("T7 separation: beta > 0 with r_hol = 0 (flat data) AND r_hol = beta "
      "(Gram witness A = C^T) realized on every cyclic test graph — "
      "cycle capacity and holonomy content are independent axes", ok)

# ------------------- T8: TDR-G Z_N zero-control (integer/modular layer)
ok = True
for N in (6, 8, 12):
    ring = Graph(N, [(i, (i + 1) % N) for i in range(N)], f"Ring{N}")
    z = [int(v) for v in ring.C.row(0)]                      # integer cycle
    theta = [random.randrange(N) for _ in range(N)]          # Z_N phases
    a = [(theta[h] - theta[t]) % N for (t, h) in ring.edges]
    hol = sum(zi * ai for zi, ai in zip(z, a)) % N
    ok &= (hol == 0)                                         # null mod N
    a_pert = list(a)
    a_pert[0] = (a_pert[0] + 1) % N                          # unit defect
    ok &= (sum(zi * ai for zi, ai in zip(z, a_pert)) % N != 0)
    # random graph with Z_N node phases: every integer kernel vector kills
    # node-difference data mod N
    G = random_connected(7, 5, f"RandZ{N}")
    theta = [random.randrange(N) for _ in range(7)]
    a = [(theta[h] - theta[t]) % N for (t, h) in G.edges]
    for r in range(G.C.rows):
        zr = [int(v) for v in G.C.row(r)]
        ok &= (sum(zi * ai for zi, ai in zip(zr, a)) % N == 0)
check("T8 TDR-G zero-control: node-difference Z_N phase data has zero "
      "holonomy mod N (rings N=6,8,12 and random graphs); a single unit "
      "defect is detected. Mod-N completeness deliberately NOT claimed", ok)

# --------------- T9: multiplicative layer spot theorem (exact rationals)
p = [Fraction(2), Fraction(3), Fraction(5)]                  # node weights
w = [p[h] / p[t] for (t, h) in GRAPHS[0].edges]              # K3 ratios
z = [int(v) for v in GRAPHS[0].C.row(0)]
prod = Fraction(1)
for zi, wi in zip(z, w):
    prod *= wi ** zi
ok = (prod == 1)
w2 = list(w)
w2[1] *= 7
prod2 = Fraction(1)
for zi, wi in zip(z, w2):
    prod2 *= wi ** zi
ok &= (prod2 != 1)
check("T9 multiplicative layer: potential ratios w_e = p_head/p_tail give "
      "cycle product exactly 1; a single-edge x7 defect gives product != 1 "
      "(positive-sector log/exp intertwiner, cf. NG-0R mechanism 2)", ok)

# ------------------------- T10: edge cases and declared-domain convention
forest = GRAPHS[3]
ok = (forest.beta == 0 and forest.C.rows == 0)
ok &= all(solvable(forest.D.T, rand_vec(forest.m)) for _ in range(3))
multi = GRAPHS[4]
loop_idx = [j for j, (t, h) in enumerate(multi.edges) if t == h][0]
x = rand_vec(multi.n)
ok &= ((multi.D.T * x)[loop_idx] == 0)                       # loop diff = 0
a = sp.zeros(multi.m, 1)
a[loop_idx] = sp.Integer(5)
ok &= ((multi.C * a) != sp.zeros(multi.C.rows, 1))           # loop defect seen
# declared-domain convention: delete one K4 edge, recompute (D,C) on the
# support subgraph; all identities persist there
sub = Graph(4, GRAPHS[1].edges[:-1], "K4-minus-edge")
ok &= (sub.C * sub.D.T == sp.zeros(sub.C.rows, sub.n))
ok &= (sub.beta == sub.m - sub.n + sub.c)
check("T10 edge cases: forest has empty h and total integrability; "
      "self-loop carries zero node-difference but detectable defect; "
      "partial data handled by recomputing (D,C) on the declared support "
      "subgraph", ok)

# ----------------------------------------------------------------------------
print("-" * 70)
if FAILURES:
    print(f"RESULT: {len(FAILURES)} FAILURE(S):")
    for f in FAILURES:
        print("   -", f)
    sys.exit(1)
print("RESULT: ALL ASSERTIONS PASS — NG-7A operator/null package certified: "
      "null theorem, field-coefficient completeness, orientation/gauge/basis "
      "invariance, typed scalar-vs-multichannel statistic, separation "
      "instances, TDR-G Z_N zero-control, multiplicative spot theorem, "
      "domain convention.")
sys.exit(0)
