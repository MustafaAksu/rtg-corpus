#!/usr/bin/env python3
# DYAD OPEN 3 -- P2 exact symbolic gate (M-1a, M-1b, M-1c).  Status of output: [ALG -- SESSION].
# Scope: leading chart offsets and spiral residuals in NORMALIZED coordinates z, one block = F = T^6.
# Inputs (adopted DYAD v6.4.13): h2 (DYAD-ALG-NF6), mu = -1/2 - i*2*sqrt3/3, omega = e^{2 pi i/3} (section 6.14),
#   P5 = (Q/24)(5 eta^3 - 43 eta^2 rho + 4 eta rho^2 - 5 rho^3) (DYAD-THM-PRIM-CTR).
# Exit 0 iff every main check holds AND every negative control fails.  Writes p2_coefficients.json.
import sys, json, sympy as sp
t = sp.symbols('t')
I = sp.I; s3 = sp.sqrt(3)
X, Y = sp.symbols('X Y', real=True)
z = X + I*Y; zb = X - I*Y; q = X**2 + Y**2
mu = -sp.Rational(1, 2) - I*2*s3/3
c20, c11, c02 = -(1 + I*s3)/12, -sp.Rational(1, 3), (1 - I*s3)/24      # h2 = c20 z^2 + c11 z zb + c02 zb^2
h2 = lambda Z, Zb: c20*Z**2 + c11*Z*Zb + c02*Zb**2
zero = lambda e: sp.simplify(sp.expand(e)) == 0
re_ = lambda e: sp.expand((e + sp.conjugate(e))/2)
im_ = lambda e: sp.expand((e - sp.conjugate(e))/(2*I))
def ddir(f, v):  # real directional derivative of f(X,Y) along complex vector v
    return sp.expand(sp.diff(f, X)*re_(v) + sp.diff(f, Y)*im_(v))
res, neg = {}, {}

# ---- M-1a: leading static offsets ---------------------------------------------------------
# D_Q = |h|^2 - q, degree-3 part = 2 Re(zb h2)  (only h2 enters at degree 3)
D3 = re_(2*zb*h2(z, zb))
eps = sp.symbols('eps', positive=True)
hz = eps*z + eps**2*h2(z, zb)            # h truncated at degree 2; higher h_k start at eps^3 and do not reach eps^3 of D_Q
DQ_series = sp.expand(re_(hz*sp.conjugate(hz)) - eps**2*q)
res["M1a_DQ_deg3"] = zero(DQ_series.coeff(eps, 3) - D3)
# D_Theta = arg(h/z) = Im log(1 + h2/z + ...), degree-1 part = Im(h2/z) = Im(zb*h2)/q
DT1 = sp.simplify(im_(zb*h2(z, zb))/q)
u = sp.symbols('u')
res["M1a_arg_series"] = sp.series(sp.log(1 + eps*u), eps, 0, 2).removeO().coeff(eps, 1) == u   # Im-linear => deg-1 = Im(h2/z)
# harmonic forms (r = 1, z = w = e^{i Theta}); exact coefficients
def harm(f_complex_monomials):
    # f given as dict {(a,b): coeff} meaning sum coeff z^a zb^b ; returns dict harmonic k=a-b -> coeff
    out = {}
    for (a, b), cf in f_complex_monomials.items():
        out[a-b] = sp.simplify(out.get(a-b, 0) + cf)
    return out
# D3 = zb*h2 + z*conj(h2): monomials
D3_mon = {(2, 1): c20, (1, 2): c11, (0, 3): c02}
D3_mon_c = {(b, a): sp.conjugate(cf) for (a, b), cf in D3_mon.items()}
D3_h = harm(D3_mon); D3_h2 = harm(D3_mon_c)
D3_harm = {k: sp.simplify(D3_h.get(k, 0) + D3_h2.get(k, 0)) for k in set(D3_h) | set(D3_h2)}
# check harmonic form reproduces D3
recon = sum(cf*(z**max(k, 0))*(zb**max(-k, 0))*q**((3-abs(k))//2) for k, cf in D3_harm.items())
res["M1a_D3_harmonic_recon"] = zero(recon - D3)

# ---- M-1b: (I-5)  P5(L^{-1} z) = D(D3)[mu q z] + 2 q D3 ------------------------------------
def P5_of(sgn):
    om = -sp.Rational(1, 2) + sgn*I*s3/2
    eta = Y/sp.im(om); rho = X - sp.re(om)*eta
    Qp = sp.expand(rho**2 - rho*eta + eta**2); assert zero(Qp - q)
    return sp.expand(Qp/24*(5*eta**3 - 43*eta**2*rho + 4*eta*rho**2 - 5*rho**3))
SQ5 = ddir(D3, mu*q*z)                                  # [S_Q]_5 = D(D3)[mu q z]
res["M1b_I5"] = zero(P5_of(1) - SQ5 - 2*q*D3)
neg["N1_wrong_omega"] = zero(P5_of(-1) - SQ5 - 2*q*D3)
neg["N2_missing_2qD3"] = zero(P5_of(1) - SQ5)
neg["N3_crossterm_sign"] = zero(P5_of(1) - SQ5 + 2*q*D3)
# chart-side check of [S_Q]_5 by expansion of D3(z + eps^2 mu q z) (scaling z -> eps z)
SQ5_series = sp.expand(D3.subs({X: X + t*re_(mu*q*z), Y: Y + t*im_(mu*q*z)}, simultaneous=True))
res["M1b_SQ5_two_methods"] = zero(sp.diff(SQ5_series, t).subs(t, 0) - SQ5)

# ---- M-1c: L_Theta = D(Im(h2/z))[mu q z]  (normalized coordinates, one F-block) -----------
L_dir = sp.simplify(ddir(DT1, mu*q*z))
# monomial formula: Im( sum c_ab (a mu + b conj mu) q z^a zb^b / z ), with h2/z monomials z^(a-1) zb^b
mub = sp.conjugate(mu)
g = c20*(1*mu)*z + c11*(mub)*zb + c02*(2*mub - mu)*zb**3/q      # zb^2/z = zb^3/q, bidegree (-1,2) -> (2 mub - mu)
L_mon = sp.simplify(q*im_(g))
res["M1c_L_two_methods"] = sp.simplify(L_dir - L_mon) == 0
neg["N4_angular_sign_flip"] = sp.simplify(ddir(DT1, -mu*q*z) - L_mon) == 0
neg["N5_mu_conj_swap"] = sp.simplify(ddir(DT1, mub*q*z) - L_mon) == 0
# [S_Theta]_3 = L_Theta : series check D_Theta1(z + mu q z) - D_Theta1(z), linear order
LT_series = sp.diff(DT1.subs({X: X + t*re_(mu*q*z), Y: Y + t*im_(mu*q*z)}, simultaneous=True), t).subs(t, 0)
res["M1c_series"] = sp.simplify(LT_series - L_mon) == 0
# harmonic coefficients on r = 1:  f(Theta) = sum_k C_k e^{i k Theta}
Th = sp.symbols('Theta', real=True)
def fourier(expr, deg):
    e = sp.simplify(expr.subs({X: sp.cos(Th), Y: sp.sin(Th)}))
    out = {}
    for k in range(-5, 6):
        ck = sp.simplify(sp.integrate(sp.expand(sp.expand_trig(e)*sp.exp(-I*k*Th)).rewrite(sp.exp), (Th, 0, 2*sp.pi))/(2*sp.pi))
        if ck != 0: out[k] = sp.nsimplify(sp.radsimp(ck))
    return out
F_D3 = fourier(D3, 3); F_DT1 = fourier(DT1, 1); F_L = fourier(L_mon, 3); F_SQ5 = fourier(SQ5, 5)
for nm, F, ex in (("D3", F_D3, D3), ("DT1", F_DT1, DT1), ("L", F_L, L_mon), ("SQ5", F_SQ5, SQ5)):
    rec = sum(cf*sp.exp(I*k*Th) for k, cf in F.items())
    res["fourier_recon_"+nm] = sp.simplify(sp.expand(rec - ex.subs({X: sp.cos(Th), Y: sp.sin(Th)})).rewrite(sp.exp)) == 0
    res["harmonics_odd_"+nm] = all(k % 2 != 0 for k in F) and all(abs(k) in (1, 3, 5) for k in F)
ok = all(res.values()) and not any(neg.values())
out = {"main": {k: bool(v) for k, v in res.items()}, "negative_controls_must_be_false": {k: bool(v) for k, v in neg.items()},
       "verdict": "PASS" if ok else "FAIL",
       "coefficients_r1_exp_basis": {nm: {str(k): str(v) for k, v in sorted(F.items())} for nm, F in
            (("D_Q_deg3 [x r^3]", F_D3), ("D_Theta_deg1 [x r]", F_DT1), ("L_Theta [x r^3, per F-block]", F_L), ("S_Q_deg5 [x r^5, per F-block]", F_SQ5))},
       "L_Theta_closed_form": str(sp.simplify(L_mon))}
json.dump(out, open("p2_coefficients.json", "w"), indent=1, ensure_ascii=False)
print(json.dumps(out, indent=1, ensure_ascii=False))
sys.exit(0 if ok else 1)
