#!/usr/bin/env python3
"""
recog_cell_a_p7_rawcomp_cert.py — RECOG CELL-A, p=7 independent check.

Composes the RAW primitive p=7 dyad map (no Birkhoff normalization at all)
seven times to cubic order in the Z-eigenframe of
normalize_p7_full_onestep_cyclotomic.py (rho = uZ + ubar Zbar, eta = Z + Zbar,
u = 1/(1-lam), K_7 = 2 - lam - lam^6, lam = exp(2 pi i/7)) and checks:

  (1) the seven-step quadratic part vanishes,
  (2) the seven-step cubic residual is confined to the (2,1) channel,
  (3) its coefficient equals the claimed exact mu_7 in Q(zeta_7),
  (4) mu_7 = 7 conj(lam) nu_3^{(1,7)} with the script's normalized nu_3,
  (5) Re mu_7 < 0 (leading radial contraction of the normalized 7-step return).

Route independence: this uses raw composition + leading-term invariance of a
tangent-to-identity map, not the normalization/bridge algebra.  High-precision
mpmath (50 dps); a symbolic Q(zeta_7) reduction is left to the owning Dyadic stream.
"""
import mpmath as mp, sys
mp.mp.dps = 50
lam = mp.exp(2j*mp.pi/7); lb = mp.conj(lam)
K = 2 - lam - lb; u = 1/(1 - lam); ub = mp.conj(u)
DEG = 3
def mul(A, B):
    C = {}
    for (i, j), a in A.items():
        for (k, l), b in B.items():
            if i + j + k + l <= DEG: C[(i+k, j+l)] = C.get((i+k, j+l), 0) + a*b
    return C
def add(A, B, s=1):
    C = dict(A)
    for k, v in B.items(): C[k] = C.get(k, 0) + s*v
    return C
def scal(A, s): return {k: v*s for k, v in A.items()}
def powr(A, n):
    R = {(0, 0): mp.mpc(1)}
    for _ in range(n): R = mul(R, A)
    return R
Zp, Zbp = {(1, 0): mp.mpc(1)}, {(0, 1): mp.mpc(1)}
rho = add(scal(Zp, u), scal(Zbp, ub)); eta = add(Zp, Zbp)
sin_eta = add(eta, scal(powr(eta, 3), -mp.mpf(1)/6))
exp_rho = add(add(rho, scal(powr(rho, 2), mp.mpf(1)/2)), scal(powr(rho, 3), mp.mpf(1)/6))
rho1 = add(rho, sin_eta, -1)
eta1 = add(add(eta, scal(exp_rho, K)), scal(sin_eta, -K))
F = [scal(add(rho1, scal(eta1, ub), -1), 1/(u-ub)), scal(add(scal(eta1, u), rho1, -1), 1/(u-ub))]
def compose(F, G):
    out = []
    for f in F:
        R = {}
        for (i, j), c in f.items():
            R = add(R, scal(mul(powr(G[0], i), powr(G[1], j)), c))
        out.append(R)
    return out
G = F
for _ in range(6): G = compose(F, G)
D = add(G[0], Zp, -1)
tol = mp.mpf('1e-40')
ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}"); ok = ok and bool(cond)
check("seven-step quadratic part vanishes", all(abs(v) < tol for k, v in D.items() if sum(k) == 2))
check("cubic residual confined to (2,1)", all(abs(v) < tol for k, v in D.items() if sum(k) == 3 and k != (2, 1)))
mu7 = D[(2, 1)]
claim = (-16 - 11*lam - 6*lam**2 - 15*lam**3 - 3*lam**4 - 12*lam**5)/2
nu3 = (12 - 4*lam + lam**2 + 6*lam**3 - 3*lam**4 + 9*lam**5)/14
check("raw (2,1) coefficient == claimed exact mu_7", abs(mu7 - claim) < tol)
check("bridge: mu_7 == 7 conj(lam) nu_3^{(1,7)}", abs(7*lb*nu3 - mu7) < tol)
check("Re mu_7 < 0", mp.re(mu7) < 0)
print("mu_7 =", mp.nstr(mu7, 30))
print("arg mu_7 (deg) =", mp.nstr(mp.arg(mu7)*180/mp.pi, 15), "   [frame-invariant under Z -> cZ]")
mu6 = mp.mpc(-0.5, -2*mp.sqrt(3)/3)
print("arg mu_6 (deg) =", mp.nstr(mp.arg(mu6)*180/mp.pi, 15), "   (p=6, W-frame)")
print("CERTIFICATE PASS" if ok else "CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
