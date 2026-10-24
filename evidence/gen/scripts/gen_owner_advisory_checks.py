#!/usr/bin/env python
"""gen_owner_advisory_checks.py — Genesis co-owner (Claude) checks behind the owner disposition of the
v2.8.9 advisory rows GA-01 (sourced-junction sign / minimizer) and GA-02 (kappa sign convention).

Owner: Genesis co-owner session (Claude), 24 Oct 2026. Status: SESSION evidence for an owner disposition record;
NOT a rerun of any archived Genesis script (none of the archived face-lift / secular / sourced-junction scripts is
held). Objects are taken verbatim from gen-v2.8.9 (sha256 d143673e...c6fc): §6.8 face-lift matrix and §6.9 9A
scalar-M decomposition. B_* is undefined in the owner text, so m is treated as a free real parameter of either sign.

Gates (exact = sympy identities; NUM = seeded floating-point sweep, not an exact proof):
  K1 exact  DeltaM_f(w) = m*N(w), N(w)^2 = |w|^2 I, (DeltaM_f)^2 = m^2|w|^2 I.
  K2 exact  Pi_pm = (I +- N/|w|)/2 are independent of m; DeltaM_f Pi_pm = +- (m|w|) Pi_pm (signed kappa_s = m|w|);
            the 9A inverse ((tau-g)I - DeltaM_f)^{-1} = Pi_+/(tau-g-kappa_s) + Pi_-/(tau-g+kappa_s) holds for both signs of m;
            v_+ = (mu1, mu2-|w|) is the +1 eigenvector of N/|w| (independent of m).
  K3 exact  negative-m label test: with kappa := |m||w| (§6.8), the pole carrying Pi_+ sits at tau-g = sgn(m)*kappa,
            i.e. for m<0 the 'soft branch tau-g-kappa -> 0' of 9A attaches to Pi_- under the §6.8 kappa.
  K4 exact  residue numerators R^(E)_+ = H0^T Pi_+ H0 and R^(B)_+ = H0^T B Pi_+ H0 are unchanged by m -> -m.
  S1 exact  w = 0: DeltaM_f(0) = 0, so K_+ = tau I + DeltaM_f and K_- = tau I - DeltaM_f coincide (= tau I).
  S2 exact  w = 0, |d|^2 = Delta_3: tau d + S = 0 has exactly the two solutions d = -+ sqrt(Delta_3) S/|S|,
            tau = +- |S|/sqrt(Delta_3) when Delta_3 > 0, S != 0; no solution when Delta_3 = 0, S != 0.
  S3 exact  secular identity for both branches: with E_s(d) = (s/2) d^T DeltaM_f d + S^T d and multiplier tau,
            stationarity is (tau I - s DeltaM_f) d = S and |d|^2 = |S|^2 (tau^2 + 2 s a tau + kappa^2)/(tau^2-kappa^2)^2,
            a = r^T DeltaM_f r (r = S/|S|). s=+1 reproduces the §6.8 K_- secular equation (+2a tau); s=-1 the K_+ one.
  S4 NUM    for random data (seeded), on the circle |d|^2 = Delta_3 the global minimiser of E_s exists for BOTH s
            and has multiplier tau <= -kappa (second-order condition s DeltaM_f - tau I >= 0), and tau solves the
            s-branch secular equation; 2000 cases per sign.
Usage: python -I gen_owner_advisory_checks.py   (exit 0 iff all gates PASS)"""
import sys, random, math
import sympy as sp

R = {}
def gate(k, ok, note=""):
    R[k] = bool(ok); print(f"[{'PASS' if ok else 'FAIL'}] {k} {note}")

m, mu1, mu2, tau, g = sp.symbols("m mu1 mu2 tau g", real=True)
W = sp.sqrt(mu1**2 + mu2**2)
N = sp.Matrix([[mu2, -mu1], [-mu1, -mu2]])          # Im w = mu2, Re w = mu1 (w = mu1 + i mu2)
DM = m * N
I2 = sp.eye(2)
# K1
gate("K1", sp.simplify(N*N - W**2*I2) == sp.zeros(2) and sp.simplify(DM*DM - m**2*W**2*I2) == sp.zeros(2),
     "(DeltaM_f)^2 = m^2|w|^2 I")
# K2
Nh = N / W
Pp, Pm = (I2 + Nh)/2, (I2 - Nh)/2
ks = m*W
inv_ok = sp.simplify(((tau-g)*I2 - DM) * (Pp/(tau-g-ks) + Pm/(tau-g+ks)) - I2) == sp.zeros(2)
eig_ok = sp.simplify(DM*Pp - ks*Pp) == sp.zeros(2) and sp.simplify(DM*Pm + ks*Pm) == sp.zeros(2)
vp = sp.Matrix([mu1, mu2 - W])
vp_ok = sp.simplify(Nh*vp - vp) == sp.zeros(2, 1)
gate("K2", inv_ok and eig_ok and vp_ok and not any(x.has(m) for x in list(Pp) + list(Pm)),
     "signed kappa_s=m|w|: projectors m-free, inverse and eigen-relations exact, v_+ eigenvector")
# K3: with kappa=|m||w|, Pi_+ pole location = sgn(m) kappa
kap = sp.Abs(m)*W
mneg = sp.Symbol("mn", negative=True); mpos = sp.Symbol("mp", positive=True)
pole_pos = sp.simplify((ks - kap).subs(m, mpos)) == 0
pole_neg = sp.simplify((ks + kap).subs(m, mneg)) == 0
gate("K3", pole_pos and pole_neg, "Pi_+ pole at tau-g = +kappa (m>0), -kappa (m<0) under kappa=|m||w|")
# K4: residue numerators independent of m
B = sp.Matrix([[1, -sp.Rational(1, 2)], [-sp.Rational(1, 2), 1]])
h1, h2 = sp.symbols("h1 h2", real=True)
H0 = sp.Matrix([h1, h2])
RE = (H0.T*Pp*H0)[0]; RB = (H0.T*B*Pp*H0)[0]
gate("K4", not RE.has(m) and not RB.has(m), "R^(E)_+, R^(B)_+ unchanged under m -> -m")
# S1, S2
gate("S1", DM.subs({mu1: 0, mu2: 0}) == sp.zeros(2), "w=0: DeltaM_f=0, K_+ = K_- = tau I")
s1, s2, D3 = sp.symbols("s1 s2 Delta3", real=True)
d1, d2 = sp.symbols("d1 d2", real=True)
sol = sp.solve([tau*d1 + s1, tau*d2 + s2, d1**2 + d2**2 - D3], [d1, d2, tau], dict=True)
S_n = sp.sqrt(s1**2 + s2**2)
expect = {(sp.simplify(sp.sqrt(D3)/S_n), ), }
ok2 = len(sol) == 2 and all(sp.simplify(x[tau]**2 - S_n**2/D3) == 0 for x in sol)
sol0 = sp.solve([tau*d1 + 1, tau*d2, d1**2 + d2**2], [d1, d2, tau], dict=True)
real0 = [x for x in sol0 if all(sp.im(v) == 0 for v in x.values())]
gate("S2", ok2 and not real0, "two antipodal stationary points, tau=+-|S|/sqrt(Delta_3); none for Delta_3=0")
# S3 secular identity both branches
a = sp.Symbol("a", real=True)
ok3 = True
for s in (1, -1):
    Kinv = ((tau*I2 - s*DM)).inv()
    # take S = sigma * r with r = (cos phi, sin phi)
    ph, sig = sp.symbols("phi sigma", positive=True)
    r = sp.Matrix([sp.cos(ph), sp.sin(ph)])
    d = Kinv * (sig*r)
    lhs = sp.simplify((d.T*d)[0] * (tau**2 - (m*W)**2)**2)
    aval = sp.simplify((r.T*DM*r)[0])
    rhs = sig**2 * (tau**2 + 2*s*aval*tau + (m*W)**2)
    ok3 = ok3 and sp.simplify(lhs - rhs) == 0
gate("S3", ok3, "|d|^2 (tau^2-kappa^2)^2 = sigma^2 (tau^2 + 2 s a tau + kappa^2); s=+1 <-> K_-, s=-1 <-> K_+")
# S4 NUM
rng = random.Random(20261024)
bad = 0; cases = 0
for s in (1, -1):
    for _ in range(2000):
        mm = rng.uniform(-2, 2) or 0.5; w1, w2 = rng.uniform(-1, 1), rng.uniform(-1, 1)
        if abs(mm) < 1e-3 or math.hypot(w1, w2) < 1e-3: continue
        Dm = [[mm*w2, -mm*w1], [-mm*w1, -mm*w2]]; kap_ = abs(mm)*math.hypot(w1, w2)
        Sx, Sy = rng.uniform(-1, 1), rng.uniform(-1, 1); D3v = rng.uniform(0.1, 2.0)
        def E(t):
            dx, dy = math.sqrt(D3v)*math.cos(t), math.sqrt(D3v)*math.sin(t)
            q = dx*(Dm[0][0]*dx + Dm[0][1]*dy) + dy*(Dm[1][0]*dx + Dm[1][1]*dy)
            return 0.5*s*q + Sx*dx + Sy*dy
        ts = [2*math.pi*k/4000 for k in range(4000)]
        t0 = min(ts, key=E)
        lo, hi = t0 - 2*math.pi/4000, t0 + 2*math.pi/4000          # golden refine
        for _ in range(80):
            m1, m2 = lo + (hi-lo)/3, hi - (hi-lo)/3
            if E(m1) < E(m2): hi = m2
            else: lo = m1
        t = (lo+hi)/2; dx, dy = math.sqrt(D3v)*math.cos(t), math.sqrt(D3v)*math.sin(t)
        gx = s*(Dm[0][0]*dx + Dm[0][1]*dy) + Sx; gy = s*(Dm[1][0]*dx + Dm[1][1]*dy) + Sy
        tv = (gx*dx + gy*dy)/D3v                                     # multiplier: grad E = tau d
        sig = math.hypot(Sx, Sy); rx, ry = Sx/sig, Sy/sig
        av = rx*(Dm[0][0]*rx + Dm[0][1]*ry) + ry*(Dm[1][0]*rx + Dm[1][1]*ry)
        sec = D3v*(tv**2 - kap_**2)**2 - sig**2*(tv**2 + 2*s*av*tv + kap_**2)
        cases += 1
        if not (tv <= -kap_ + 1e-6 and abs(sec) < 1e-6*(1 + sig**2*(tv**2 + kap_**2))): bad += 1
gate("S4", bad == 0 and cases > 3900, f"[NUM] global minimiser on the circle: tau <= -kappa and branch secular eq.; {cases} cases, {bad} failures")

ok = all(R.values())
print(f"\n{sum(R.values())}/{len(R)} gates PASS")
sys.exit(0 if ok else 1)
