#!/usr/bin/env python3
"""Independent replay of dim ker(ad_X3) on degree-k fields, k=2..7, for the triad six-step cubic.
Independent of triad_formal_involution_birth_jet.py: X3 is built from the K3 SESSION record v0.1.2 chiral identities
   du = c0 u|u|^2 - i b N u,  dv = c0 v|v|^2 - i b N v,  N=|u|^2+|v|^2,  c0 = 1/6 + i sqrt3/9,  b = 2 sqrt3/9
(Genesis v2.8.6 §6.3a (d)). Kernel dimension is invariant under the real-linear change (s,c) <-> (u,v).
Method: complexify (u, ub, v, vb independent); the real kernel dimension of a real operator equals the complex
kernel dimension of its complexification. Rank by numpy SVD (float64) with an explicit gap report. [NUM] replay.
Exit 0 iff dims = (0,2,0,0,0,0) and every rank decision has a singular-value gap > 1e6.
Negative control --control-real (c0 real, b = 0; rotations survive) must exit 1. Note: b = 0 alone does NOT change
the k = 3 dimension (two decoupled dyads also give 2), so it is not used as a control."""
import sys, itertools, numpy as np
c0 = 1/6 + 1j*np.sqrt(3)/9; b = 2*np.sqrt(3)/9
if '--control-real' in sys.argv: c0, b = 1/6, 0.0   # negative control: real cubic, no chiral coupling
# variables: 0=u,1=ub,2=v,3=vb ; polynomials as dict exponent-tuple -> complex
def P(*terms): return {e: c for e, c in terms}
U, UB, V, VB = (1,0,0,0), (0,1,0,0), (0,0,1,0), (0,0,0,1)
add = lambda *es: tuple(map(sum, zip(*es)))
X = [  # du, dub, dv, dvb
 P((add(U,U,UB), c0 - 1j*b), (add(U,V,VB), -1j*b)),
 P((add(UB,UB,U), np.conj(c0) + 1j*b), (add(UB,V,VB), 1j*b)),
 P((add(V,V,VB), c0 - 1j*b), (add(V,U,UB), -1j*b)),
 P((add(VB,VB,V), np.conj(c0) + 1j*b), (add(VB,U,UB), 1j*b)),
]
def d(p, j):
    o = {}
    for e, c in p.items():
        if e[j]:
            f = list(e); f[j] -= 1; o[tuple(f)] = o.get(tuple(f), 0) + c*e[j]
    return o
def mul(p, q):
    o = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = add(e1, e2); o[e] = o.get(e, 0) + c1*c2
    return o
dX = [[d(X[i], j) for j in range(4)] for i in range(4)]
def mons(k): return [e for e in itertools.product(range(k+1), repeat=4) if sum(e) == k]
dims = {}; ok = True
for k in range(2, 8):
    ms = mons(k); out = {e: n for n, e in enumerate(mons(k+2))}
    cols = []
    for i in range(4):
        for m in ms:
            Y = [{} for _ in range(4)]; Y[i] = {m: 1.0}
            col = np.zeros(4*len(out), complex)
            for a in range(4):
                acc = {}
                for j in range(4):
                    for e, c in mul(X[j], d(Y[a], j)).items(): acc[e] = acc.get(e, 0) + c
                    for e, c in mul(Y[j], dX[a][j]).items(): acc[e] = acc.get(e, 0) - c
                for e, c in acc.items(): col[a*len(out) + out[e]] += c
            cols.append(col)
    M = np.array(cols).T; s = np.linalg.svd(M, compute_uv=False)
    n = M.shape[1]; rank = int((s > 1e-9*s[0]).sum()); ker = n - rank
    gap = (s[rank-1]/max(s[rank], 1e-300)) if rank < len(s) else float('inf')
    dims[k] = ker; ok &= gap > 1e6
    print(f'k={k}: unknowns {n}, kernel dim {ker}, smallest kept sv {s[rank-1]:.3e}, next {s[rank] if rank < len(s) else 0:.3e}')
ok &= dims == {2: 0, 3: 2, 4: 0, 5: 0, 6: 0, 7: 0}
print('dims', tuple(dims.values()), '->', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
