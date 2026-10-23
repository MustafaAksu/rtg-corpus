#!/usr/bin/env python3
"""
recog_cell_b_p2_manifolds.py

RECOG CELL-B preliminary diagnostic for RTG_RELATIONAL_RECOGNITION_DSN_v0.2.1.

Purpose
-------
Numerically continue the P2 unstable manifold of the certified primitive dyad map

    T(rho,eta) = (rho - sin eta,
                  eta + exp(rho) - 1 - sin eta)

and locate the first intersection, on the rho-increasing unstable branch, with
the intrinsic rank-loss stratum

    C0 : det DT = 1 + (exp(rho)-1) cos eta = 0.

Method
------
P2 = (0, pi), lambda_u = phi^2, v_u = (1, phi).

The unstable manifold is sampled by the parameterization-limit sequence

    P_n(t) = T^n(P2 + (t/lambda_u^n) v_u),

which converges to the unstable-manifold parameterization normalized by
P'(0)=v_u.  For each n, solve det DT(P_n(t)) = 0 near the first positive root.

This is a high-precision NUM/diagnostic artifact, not an interval-arithmetic
certificate.  "First" means first positive root in the scanned normalized
unstable parameter t on the rho-increasing branch.

The script also:
  * prints the exact local eigendirections,
  * verifies the C0 equation at the converged point,
  * reports the pole-comparator distance delta_eta = dist_S1(eta, pi),
  * scans for an earlier positive root,
  * scans the opposite unstable branch for rank-loss encounters.

Expected converged values
-------------------------
rho_*       ~= 2.03336443891426948448522802818746757945
eta_*       ~= 1.72197974432209828489603892380086928769  (wrapped)
delta_eta_* ~= 1.41961290926769495356660445947863359651 rad
             ~= 81.3378282433 deg

Scope
-----
Conditional on the postulated primitive continuous generator T.
No continuous-to-discrete band-width bridge is claimed.
"""

import mpmath as mp
import sys

mp.mp.dps = 90

SQRT5 = mp.sqrt(5)
PHI = (1 + SQRT5) / 2
LAM_U = PHI**2
LAM_S = PHI**-2
PI = mp.pi

P2 = (mp.mpf("0"), PI)
V_U = (mp.mpf("1"), PHI)
V_S = (mp.mpf("1"), -1/PHI)

def T(x):
    rho, eta = x
    s = mp.sin(eta)
    return (rho - s, eta + mp.exp(rho) - 1 - s)

def detJ(x):
    rho, eta = x
    return 1 + (mp.exp(rho) - 1) * mp.cos(eta)

def wrap(eta):
    return mp.atan2(mp.sin(eta), mp.cos(eta))

def pole_distance(eta):
    """Geodesic distance on S^1 from eta to pi."""
    return mp.acos(mp.cos(eta - PI))

def unstable_point(t, n):
    """
    Parameterization-limit approximation:
      P_n(t)=T^n(P2 + t/lambda_u^n * v_u).
    """
    s = t / (LAM_U**n)
    x = (P2[0] + s*V_U[0], P2[1] + s*V_U[1])
    for _ in range(n):
        x = T(x)
    return x

def h(t, n):
    return detJ(unstable_point(t, n))

def bisect_root(n, lo=mp.mpf("2.8"), hi=mp.mpf("3.2"), tol=mp.mpf("1e-70")):
    flo = h(lo, n)
    fhi = h(hi, n)
    if flo == 0:
        return lo
    if fhi == 0:
        return hi
    if flo * fhi > 0:
        raise RuntimeError(f"root not bracketed for n={n}: h(lo)={flo}, h(hi)={fhi}")
    while hi - lo > tol:
        mid = (lo + hi) / 2
        fm = h(mid, n)
        if fm == 0:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2

def scan_no_earlier_positive_root(n, root, samples=4000):
    """
    Diagnostic only: checks h(t)>0 on a uniform scan of [0, root).
    Does not prove absence of an even-multiplicity tangent root.
    """
    minval = mp.inf
    mint = mp.mpf("0")
    for k in range(samples):
        t = root * mp.mpf(k) / samples
        val = h(t, n)
        if val < minval:
            minval, mint = val, t
        if val <= 0:
            return False, mint, minval
    return True, mint, minval

def scan_opposite_branch(n, tmax=mp.mpf("20"), samples=2000):
    """
    Diagnostic scan of t in [-tmax,0] for detJ <= 0.
    """
    minval = mp.inf
    mint = None
    for k in range(samples + 1):
        t = -tmax + tmax * mp.mpf(k) / samples
        val = h(t, n)
        if val < minval:
            minval, mint = val, t
        if val <= 0:
            return False, mint, minval
    return True, mint, minval

def fmt(x, n=45):
    return mp.nstr(x, n)

def main():
    print("RECOG CELL-B: P2 manifold / C0 diagnostic")
    print("P2 =", P2)
    print("lambda_u = phi^2 =", fmt(LAM_U, 30))
    print("lambda_s = phi^-2 =", fmt(LAM_S, 30))
    print("v_u = (1, phi) =", tuple(fmt(z, 30) for z in V_U))
    print("v_s = (1, -1/phi) =", tuple(fmt(z, 30) for z in V_S))
    print()

    ns = [10, 15, 20, 25, 30, 35]
    rows = []
    for n in ns:
        rt = bisect_root(n)
        x = unstable_point(rt, n)
        rho, eta = x
        ew = wrap(eta)
        de = pole_distance(ew)
        rows.append((n, rt, rho, ew, de, detJ(x)))
        print(
            f"n={n:2d}  "
            f"t*={fmt(rt, 28)}  "
            f"rho*={fmt(rho, 28)}  "
            f"eta*={fmt(ew, 28)}  "
            f"delta={fmt(de, 28)}  "
            f"det={fmt(detJ(x), 8)}"
        )

    n, rt, rho, ew, de, dj = rows[-1]
    c0_rho = mp.log(1 - 1/mp.cos(ew))
    deg = de * 180 / PI

    print("\nConverged CELL-B candidate:")
    print("rho_*       =", fmt(rho, 55))
    print("eta_*       =", fmt(ew, 55))
    print("delta_eta_* =", fmt(de, 55), "rad")
    print("            =", fmt(deg, 30), "deg")
    print("C0 rho(eta) =", fmt(c0_rho, 55))
    print("|rho-rho_C0|=", fmt(abs(rho-c0_rho), 12))

    # convergence check against previous n
    prev = rows[-2]
    conv = max(abs(rho-prev[2]), abs(ew-prev[3]), abs(de-prev[4]))
    print("n=30 -> 35 max coordinate change =", fmt(conv, 12))

    ok_first, mt, mv = scan_no_earlier_positive_root(n, rt)
    print("no earlier sampled positive-branch rank crossing:", ok_first,
          "(min sampled det before root =", fmt(mv, 12), ")")

    ok_opp, omt, omv = scan_opposite_branch(n)
    print("no sampled opposite-branch rank crossing on t in [-20,0]:", ok_opp,
          "(min det =", fmt(omv, 12), "at t =", fmt(omt, 12), ")")

    # The first intersection is expected to be transverse in the t parameter:
    eps = mp.mpf("1e-7")
    dh = (h(rt+eps, n)-h(rt-eps, n))/(2*eps)
    print("d/dt detJ at first root (diagnostic) =", fmt(dh, 20))

    passed = (
        abs(dj) < mp.mpf("1e-60")
        and abs(rho-c0_rho) < mp.mpf("1e-50")
        and conv < mp.mpf("1e-20")
        and ok_first
        and ok_opp
        and abs(dh) > mp.mpf("1e-6")
    )

    print("\nCELL-B DIAGNOSTIC PASS" if passed else "\nCELL-B DIAGNOSTIC FAIL")
    if not passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
