#!/usr/bin/env python3
"""A3 -- pole-comparator quadrature typing (R4 sub-item 1), exact symbolic certificate + [NUM] periodic-orbit probe.

Primitive map (Dyadic §6.1, lifted chart):  T(rho, eta) = (rho - sin eta,  eta + e^rho - 1 - sin eta).
Pole comparator (RECOG-DEF-POLE-COMPARATOR):  C_pole = e^{i eta};  quadrature  Qd := {Re C_pole = 0} = {cos eta = 0}.

Exact gates (sympy):
  Q1  Jacobian identities in the primitive chart: tr J = 2 - c, det J = 1 + (e^rho - 1) c, Disc = c (c - 4 e^rho), c = cos eta.
  Q2  On Qd: J = [[1,0],[e^rho,1]] (nontrivial unipotent; Jordan type [[1,1],[0,1]]); its 1-eigenspace is the eta-direction.
  Q3  Comparator-geometric characterisations of Qd (statements about the canonical observables rho, eta, not about a chart):
        (a) rho(Tx) - rho(x) = -Im C_pole, so |Delta rho| <= 1 with equality exactly on Qd (extremal radial transfer);
        (b) d(rho o T - rho)/d eta = -Re C_pole: Qd is the critical locus of the radial transfer along the comparator fiber;
        (c) with the DECLARED reference form Omega = d rho ^ d eta = d conj(zeta) ^ d zeta / (2 i |zeta|^2) on the RRF wrapped native ratio
            zeta = e^{rho + i eta} (multiplicative Haar form, S-invariant): T^* Omega = (1 + (e^rho - 1) Re C_pole) Omega, so Qd together with
            {rho = 0} is the Omega-area-neutral locus. Scope: relative to the declared Omega (transported with charts); not an RRF observable.
  Q4  Retyping witnesses (why the unipotent type carries no chart-free content):
        chart A  phi_A(rho, eta) = (rho + eps sin eta, eta): on Qd the transformed one-step Jacobian has
                 tr = 2 + eps e^rho cos(eta') with eta' = eta + e^rho - 1 - sin eta, det = 1; so Qd points become
                 elliptic (|tr|<2) or hyperbolic (tr>2) depending on sign(eps cos eta'): the parabolic type is not chart-invariant.
        chart B  phi_B(rho, eta) = (rho, eta + (e/(e-1)) e^rho): on the branch eta = pi/2 the transformed Jacobian is the identity
                 (trivial unipotent) -- the shear strength e^rho is a chart artefact.
        Both charts are global diffeomorphisms of the lifted plane (and of the cylinder: eta-periodicity is respected).
  Q5  (t,d)-plane: for a period-n point the multiplier pair (tr M_n, det M_n) is chart-invariant, but a quadrature crossing
        contributes the factor det J = 1 to d_n and is not separable in t_n; verified on a symbolic 2-step example that
        tr(J(Tx) J(x)) on Qd depends on the partner point (no fixed signature).
  Q6  Exact inventory of periodic orbits of the WRAPPED map inside the pole-comparator inversion-fixed value stratum Sigma = {C_pole = +-1} = {sin eta = 0}
        (S-invariant as a set, not pointwise fixed by the state swap S): on Sigma, rho is
        preserved and eta -> eta + e^rho - 1, so an orbit stays in Sigma iff e^rho - 1 = m pi (m in Z, m >= 0 since e^rho > 0... m >= 0
        with m = 0 the zero-winding P1, P2); m even: the winding fixed points (log(1+2 pi k), 0/pi), k = m/2 (Dyadic §1 table);
        m odd: NEW period-2 orbits {(log(1+m pi), 0), (log(1+m pi), pi)} alternating between the pole strata C_pole = +1 and -1,
        with multipliers tr M_2 = 1, det M_2 = 1 - m^2 pi^2 (hyperbolic, orientation-reversing). None of these touches Qd.
Negative controls:
  NC1 a constant linear chart (a genuine conjugacy) must preserve tr and det at every point (type invariance under conjugacy).
  NC2 chart A with eps = 0 must reproduce the primitive-chart unipotent on Qd.
[NUM] probe (numpy): Newton search for periodic orbits T^n x = x + (0, 2 pi L), n <= 8, |L| <= 2, in rho in [-2.5, 2.5], from a grid;
  deduplicated; P1-degenerate false positives (T^6 = id + O(|x|^3)) rejected; for each orbit (t_n, d_n), the minimal |cos eta| along
  the orbit and whether consecutive points lie on opposite sides of Qd. Exploratory sampled search: no completeness claim, no
  nonexistence claim about periodic points on Qd, no certificate.
usage: python -I recog_a3_quadrature_typing.py [OUT_JSON]
"""
import json, math, sys
import numpy as np
import sympy as sp

rho, eta, eps = sp.symbols('rho eta epsilon', real=True)
c, s = sp.cos(eta), sp.sin(eta)
T = sp.Matrix([rho - s, eta + sp.exp(rho) - 1 - s])
J = T.jacobian([rho, eta])
res = {}
# Q1
trJ, detJ = sp.simplify(J.trace()), sp.simplify(J.det())
disc = sp.simplify(trJ**2 - 4*detJ)
q1 = (sp.simplify(trJ - (2 - c)) == 0 and sp.simplify(detJ - (1 + (sp.exp(rho) - 1)*c)) == 0
      and sp.simplify(disc - c*(c - 4*sp.exp(rho))) == 0)
res["Q1_jacobian_identities"] = bool(q1)
# Q2 on quadrature (both branches)
q2 = True
for e0 in (sp.pi/2, -sp.pi/2):
    Jq = J.subs(eta, e0)
    q2 &= (Jq == sp.Matrix([[1, 0], [sp.exp(rho), 1]]))
    q2 &= ((Jq - sp.eye(2)) != sp.zeros(2, 2)) and (((Jq - sp.eye(2))**2) == sp.zeros(2, 2))   # nontrivial unipotent
    q2 &= (Jq*sp.Matrix([0, 1]) == sp.Matrix([0, 1]))                                             # eigenvector = eta-direction
res["Q2_unipotent_shear_on_quadrature"] = bool(q2)
# Q3 comparator-geometric characterisations
drho = T[0] - rho                                   # = -sin eta = -Im C_pole
q3a = sp.simplify(drho + sp.im(sp.exp(sp.I*eta))) == 0
q3b = sp.simplify(sp.diff(drho, eta) + sp.re(sp.exp(sp.I*eta))) == 0
q3c = sp.simplify(detJ - 1 - (sp.exp(rho) - 1)*sp.re(sp.exp(sp.I*eta))) == 0
# swap invariance of the comparator area form d rho ^ d eta under S(rho,eta) = (-rho,-eta): det DS = +1
S = sp.Matrix([-rho, -eta]); q3d = (S.jacobian([rho, eta]).det() == 1)
res["Q3_comparator_geometry"] = {"a_extremal_radial_transfer": bool(q3a), "b_critical_locus_along_fiber": bool(q3b),
                                 "c_area_neutral_locus": bool(q3c), "d_area_form_swap_invariant": bool(q3d)}
q3 = q3a and q3b and q3c and q3d
# Q4 retyping witnesses
def transformed_jacobian(phi):
    """D(phi o T o phi^{-1}) at phi(x), expressed at x: Dphi(Tx) * DT(x) * Dphi(x)^{-1}  (phi: Matrix in rho, eta)."""
    Dphi = phi.jacobian([rho, eta])
    DphiT = Dphi.subs({rho: T[0], eta: T[1]}, simultaneous=True)
    return sp.simplify(DphiT * J * Dphi.inv())
phiA = sp.Matrix([rho + eps*s, eta])
JA = transformed_jacobian(phiA)
etap = T[1]
trA_expected = 2 - c + eps*sp.exp(rho)*(sp.cos(etap) - c)      # general formula, reduces to 2 + eps e^rho cos(eta') on Qd
q4a = (sp.simplify(JA.trace() - trA_expected) == 0) and (sp.simplify(JA.det() - detJ) == 0)
# on the quadrature: tr = 2 + eps e^rho cos(eta'), det = 1 -> explicit elliptic / hyperbolic instances at (rho, eta) = (0, pi/2)
JA_q = JA.subs(eta, sp.pi/2)
trA_q = sp.simplify(JA_q.trace())
q4a &= sp.simplify(trA_q - (2 + eps*sp.exp(rho)*sp.cos(sp.pi/2 + sp.exp(rho) - 2))) == 0
# numeric instances: rho = 0, eta = pi/2: eta' = pi/2 - 1, cos(eta') = sin 1 > 0
tr_pos = float(trA_q.subs({rho: 0, eps: sp.Rational(1, 2)}))      # > 2 : hyperbolic
tr_neg = float(trA_q.subs({rho: 0, eps: -sp.Rational(1, 2)}))     # in (-2, 2): elliptic
res["Q4_chartA"] = {"trace_general_ok": bool(q4a), "tr_at_rho0_eps+0.5": tr_pos, "tr_at_rho0_eps-0.5": tr_neg,
                    "hyperbolic_instance": tr_pos > 2, "elliptic_instance": abs(tr_neg) < 2, "det_on_Qd": 1.0}
q4a &= (tr_pos > 2) and (abs(tr_neg) < 2)
alpha = sp.E/(sp.E - 1)
phiB = sp.Matrix([rho, eta + alpha*sp.exp(rho)])
JB = transformed_jacobian(phiB)
JB_q = sp.simplify(JB.subs(eta, sp.pi/2))
q4b = (JB_q == sp.eye(2))
JB_q2 = sp.simplify(JB.subs(eta, -sp.pi/2))              # other branch: shear strength e^rho (1 + alpha (e - 1)) = e^rho (1 + e)
q4b &= (sp.simplify(JB_q2[1, 0] - sp.exp(rho)*(1 + sp.E)) == 0)
res["Q4_chartB"] = {"identity_on_branch_pi_over_2": bool(JB_q == sp.eye(2)), "shear_on_branch_minus_pi_over_2": str(sp.simplify(JB_q2[1, 0]))}
# both charts are global diffeomorphisms: det Dphi = 1 everywhere, and they are explicit bijections (shear maps)
q4c = (sp.simplify(phiA.jacobian([rho, eta]).det()) == 1) and (sp.simplify(phiB.jacobian([rho, eta]).det()) == 1)
res["Q4_charts_are_unimodular_shears"] = bool(q4c)
q4 = q4a and q4b and q4c
# Q5 two-step example: tr(J(Tx) J(x)) on Qd depends on the partner point
M2 = sp.simplify((J.subs({rho: T[0], eta: T[1]}, simultaneous=True) * J).subs(eta, sp.pi/2))
tr2 = sp.simplify(M2.trace()); d2 = sp.simplify(M2.det())
q5 = (sp.simplify(d2 - detJ.subs({rho: T[0], eta: T[1]}, simultaneous=True).subs(eta, sp.pi/2)) == 0) and (sp.diff(tr2, rho) != 0)
res["Q5_two_step_on_Qd"] = {"tr2": str(tr2), "det2": str(d2), "tr2_depends_on_rho": bool(sp.diff(tr2, rho) != 0)}
# NC1 constant linear chart = conjugacy: tr, det preserved
Lc = sp.Matrix([[2, 1], [1, 1]])
phiL = Lc*sp.Matrix([rho, eta])
JL = transformed_jacobian(phiL)
nc1 = (sp.simplify(JL.trace() - trJ) == 0) and (sp.simplify(JL.det() - detJ) == 0)
# NC2 chart A with eps = 0 reproduces the primitive unipotent on Qd
nc2 = (sp.simplify(JA.subs({eps: 0, eta: sp.pi/2})) == sp.Matrix([[1, 0], [sp.exp(rho), 1]]))
# Q6 pole-stratum (C_pole = +-1) wrapped-periodic inventory (exact, symbolic m)
m = sp.symbols('m', integer=True, positive=True)
rm = sp.log(1 + m*sp.pi)
T0 = T.subs({rho: rm, eta: 0}, simultaneous=True); Tpi = T.subs({rho: rm, eta: sp.pi}, simultaneous=True)
q6 = (sp.simplify(T0[0] - rm) == 0) and (sp.simplify(T0[1] - m*sp.pi) == 0) and (sp.simplify(Tpi[0] - rm) == 0) and (sp.simplify(Tpi[1] - (m + 1)*sp.pi) == 0)
Mm = (J.subs({rho: rm, eta: sp.pi}, simultaneous=True) * J.subs({rho: rm, eta: 0}, simultaneous=True))
q6 &= (sp.simplify(Mm.trace() - 1) == 0) and (sp.simplify(Mm.det() - (1 - m**2*sp.pi**2)) == 0)
# fixed-point multipliers for even m = 2k: (tr, det) = (1, 1 + 2 pi k) at eta = 0 and (3, 1 - 2 pi k) at eta = pi
k = sp.symbols('k', integer=True, positive=True)
J0 = J.subs({rho: sp.log(1 + 2*sp.pi*k), eta: 0}, simultaneous=True); Jpi = J.subs({rho: sp.log(1 + 2*sp.pi*k), eta: sp.pi}, simultaneous=True)
q6 &= (sp.simplify(J0.trace() - 1) == 0) and (sp.simplify(J0.det() - (1 + 2*sp.pi*k)) == 0) and (sp.simplify(Jpi.trace() - 3) == 0) and (sp.simplify(Jpi.det() - (1 - 2*sp.pi*k)) == 0)
# converse: a wrapped-periodic orbit inside Sigma needs e^rho - 1 in pi Z (eta advances by e^rho - 1 each step and must stay in pi Z)
res["Q6_pole_stratum_wrapped_periodic_inventory"] = {"rho_m": "log(1 + m pi)", "period": "1 if m even (winding fixed points), 2 if m odd (new)",
                                          "period2_multipliers": "(tr, det) = (1, 1 - m^2 pi^2)", "fixed_multipliers": "(1, 1+2 pi k) at eta=0; (3, 1-2 pi k) at eta=pi", "ok": bool(q6)}
res["gates"] = {"Q1": bool(q1), "Q2": bool(q2), "Q3": bool(q3), "Q4": bool(q4), "Q5": bool(q5), "Q6": bool(q6), "NC1_conjugacy_preserves_type": bool(nc1), "NC2_eps0_reproduces": bool(nc2)}

# ---------------- [NUM] periodic-orbit probe (exploratory; not a proof input) ----------------
def Tn(x, n):
    r, e = x
    for _ in range(n):
        r, e = r - math.sin(e), e + math.exp(r) - 1 - math.sin(e)
    return r, e
def DTn(x, n):
    r, e = x; M = np.eye(2)
    for _ in range(n):
        Jx = np.array([[1.0, -math.cos(e)], [math.exp(r), 1.0 - math.cos(e)]]); M = Jx @ M
        r, e = r - math.sin(e), e + math.exp(r) - 1 - math.sin(e)
    return M
orbits = []
NMAX, LMAX = 8, 2
rng_r = np.linspace(-2.5, 2.5, 41); rng_e = np.linspace(0, 2*math.pi, 48, endpoint=False)
for n in range(1, NMAX + 1):
    for L in range(-LMAX, LMAX + 1):
        for r0 in rng_r:
            for e0 in rng_e:
                x = np.array([r0, e0]); ok = False
                for it in range(40):
                    if abs(x[0]) > 6: break
                    f = np.array(Tn(x, n)) - x - np.array([0.0, 2*math.pi*L])
                    if np.linalg.norm(f) < 1e-13: ok = True; break
                    A = DTn(x, n) - np.eye(2)
                    try: dx = np.linalg.solve(A, -f)
                    except np.linalg.LinAlgError: break
                    if np.linalg.norm(dx) > 2: dx *= 2/np.linalg.norm(dx)
                    x = x + dx
                if not ok: continue
                # minimal period check and dedupe modulo the orbit and eta mod 2pi
                pts = []; y = x.copy()
                for k in range(n):
                    em = y[1] % (2*math.pi)
                    if em > 2*math.pi - 1e-7: em = 0.0
                    pts.append((float(y[0]), float(em))); y = np.array(Tn(y, 1))
                # reject the P1-degenerate false positives: T^6 = id + O(|x|^3) near P1, so Newton 'converges' at |x| ~ 1e-5
                if min(abs(p[0]) + min(p[1], 2*math.pi - p[1]) for p in pts) < 1e-3 and n > 1: continue
                minimal = all(np.linalg.norm(np.array(Tn(x, m)) - x - np.array([0.0, 2*math.pi*round((Tn(x, m)[1]-x[1])/(2*math.pi))])) > 1e-8 for m in range(1, n))
                if not minimal: continue
                key = min((round(p[0], 6), round(p[1], 6)) for p in pts)
                if any(o["key"] == key for o in orbits): continue
                M = DTn(x, n); t, d = float(np.trace(M)), float(np.linalg.det(M))
                mincos = min(abs(math.cos(p[1])) for p in pts)
                jumps = any(math.cos(pts[k][1])*math.cos(pts[(k+1) % n][1]) < 0 for k in range(n))   # consecutive points on opposite sides of Qd
                orbits.append({"key": key, "n": n, "L": L, "points": [(round(p[0], 10), round(p[1], 10)) for p in pts],
                               "t": t, "d": d, "disc": t*t - 4*d, "min_abs_cos_eta": mincos, "jumps_across_Qd": jumps})
res["NUM_periodic_orbit_probe"] = {"box": "rho in [-2.5,2.5], eta mod 2pi; n<=8; |L|<=2; grid 41x48; Newton", "n_orbits": len(orbits),
                                   "orbits": sorted(orbits, key=lambda o: (o["n"], o["L"], o["key"]))}
for o in res["NUM_periodic_orbit_probe"]["orbits"]: o.pop("key")
ok = all(res["gates"].values())
res["ALL_PASS"] = ok
out = sys.argv[1] if len(sys.argv) > 1 else "a3_quadrature_typing.json"
json.dump(res, open(out, "w"), indent=1, default=str)
for k, v in res["gates"].items(): print(k, "PASS" if v else "FAIL")
print("chart A on Qd at rho=0: tr(eps=+1/2) =", tr_pos, "(hyperbolic);  tr(eps=-1/2) =", tr_neg, "(elliptic)")
print("chart B: identity on eta=pi/2 branch:", res["Q4_chartB"]["identity_on_branch_pi_over_2"])
print("two-step on Qd: tr2 =", tr2)
print("[NUM] periodic orbits found:", len(orbits))
for o in res["NUM_periodic_orbit_probe"]["orbits"]:
    print("  n=%d L=%+d  (t,d)=(%.6f, %.6f)  disc=%.4g  min|cos eta|=%.4f  jumps across Qd=%s  x0=(%.6f, %.6f)" % (o["n"], o["L"], o["t"], o["d"], o["disc"], o["min_abs_cos_eta"], o["jumps_across_Qd"], o["points"][0][0], o["points"][0][1]))
print("ALL PASS" if ok else "FAILURES")
sys.exit(0 if ok else 1)
