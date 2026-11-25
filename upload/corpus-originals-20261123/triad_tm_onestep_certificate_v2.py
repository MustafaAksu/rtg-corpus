#!/usr/bin/env python3
"""
F3-FINITE-JET-CONTROL, stage 1: rigorous one-step defect bound for the N=7 / N=8 finite-jet age family
against the real analytic conditional modal map, on a small box, by Taylor models with interval coefficients.

Model: F = N^6, N = (P x I2) o T_e^{x3} o (E x I2), T_e(r,e) = (r - sin e, e + expm1(r) - sin e), kappa = sqrt3 (kt=1).
Finite jet: C_N(s,tau) = sum_{d<=N} C_d(s,tau) from age_family_polynomials_kt1.json (exact rationals).
Defect:     E_N(s,tau) = F_c(s, C_N(s,tau)) - C_N( F_s(s, C_N(s,tau)), tau+1 ).

Method (standard Taylor-model arithmetic, Makino-Berz style, all coefficient arithmetic in mpmath interval
arithmetic, so floating-point rounding is enclosed):
  * variables v = (dr, de, dtau), box |dr|<=h, |de|<=h, |dtau|<=h_tau around a centre (r0,e0,tau0);
  * a Taylor model is (polynomial of total degree <= K with interval coefficients, symmetric remainder bound rho)
    and encloses the function on the whole box: f(v) in P(v) + [-rho, rho];
  * products truncate degrees > K into the remainder via the box bound sum |c_alpha| h^alpha;
  * sin / expm1 of a model use Taylor expansion about the model's constant term with Lagrange remainder
    (|sin^(j)| <= 1 ; |exp^(j)| <= exp(|p0|+|q|)).
Output: a rigorous enclosure of E_N on the box, hence certified  ||E_N||_B <= K_{N} R_min^(N+1)  on that box,
together with the enclosure of E_N at the box centre (to show how tight the bound is).

Usage:  python triad_tm_onestep_certificate.py [--K 8] [--h 0.0025] [--boxes small|stage1]
Needs mpmath and age_family_polynomials_kt1.json in the same directory.
"""
import sys, json, time, itertools
from pathlib import Path
from fractions import Fraction as Fr
import mpmath as mp
from mpmath import iv

mp.mp.dps = 30; iv.dps = 30
args = sys.argv[1:]
def opt(name, default, cast):
    return cast(args[args.index(name)+1]) if name in args else default
KDEG = opt('--K', 8, int)
HBOX = opt('--h', '0.0025', str)
BOXSET = opt('--boxes', 'stage1', str)
ONLY_N = opt('--N', 0, int)
ONLY_BOX = opt('--box-index', -1, int)
NMAX = 8

POLY = json.load(open(Path(__file__).resolve().parent / 'age_family_polynomials_kt1.json'))
Cpoly = {int(k[1:]): {int(m[5:]): [[Fr(x) for x in row] for row in arr] for m, arr in v.items()} for k, v in POLY.items()}

# ------------------------------------------------------------------ Taylor models in 3 variables
NV = 3
MONOS = [a for d in range(KDEG+1) for a in itertools.product(range(d+1), repeat=NV) if sum(a) == d]
IDX = {a: i for i, a in enumerate(MONOS)}
ZERO = iv.mpf(0); ONE = iv.mpf(1)
def ivq(x):   # exact rational / float -> interval
    if isinstance(x, Fr): return iv.mpf(x.numerator) / iv.mpf(x.denominator)
    return iv.mpf(x)
def ub(x):    # upper bound of an interval as a zero-width interval
    return iv.mpf(x.b) if isinstance(x, iv.mpf) else iv.mpf(x)
def fact(n):
    f = 1
    for j in range(2, n+1): f *= j
    return iv.mpf(f)
class TM:
    __slots__ = ('c', 'rem', 'H')
    def __init__(self, c=None, rem=None, H=None):
        self.c = c if c is not None else {}
        self.rem = rem if rem is not None else ZERO             # nonnegative bound, kept as an interval (upper end used)
        self.H = H
    def copy(self): return TM(dict(self.c), self.rem, self.H)
def absmax(x):  # max |x| over an interval (zero-width interval)
    return ub(abs(x))
def hpow(H, a):
    r = ONE
    for hi, ai in zip(H, a): r *= hi**ai
    return r
def const(x, H): return TM({(0,)*NV: ivq(x)}, ZERO, H)
def var(i, H):
    a = [0]*NV; a[i] = 1
    return TM({tuple(a): ONE}, ZERO, H)
def tm_add(x, y):
    c = dict(x.c)
    for a, v in y.c.items(): c[a] = c.get(a, ZERO) + v
    return TM(c, ub(x.rem + y.rem), x.H)
def tm_scale(k, x):
    k = ivq(k)
    return TM({a: k*v for a, v in x.c.items()}, ub(absmax(k) * x.rem), x.H)
def tm_neg(x): return tm_scale(-1, x)
def tm_sub(x, y): return tm_add(x, tm_neg(y))
def poly_bound(x):   # sum |c_alpha| h^alpha  (rigorous bound of the polynomial part on the box)
    b = ZERO
    for a, v in x.c.items(): b += absmax(v) * hpow(x.H, a)
    return ub(b)
def tm_bound(x): return ub(poly_bound(x) + x.rem)
def tm_mul(x, y):
    c = {}; spill = ZERO; H = x.H
    for a, va in x.c.items():
        for b, vb in y.c.items():
            s = tuple(i+j for i, j in zip(a, b))
            if sum(s) <= KDEG: c[s] = c.get(s, ZERO) + va*vb
            else: spill += absmax(va*vb) * hpow(H, s)
    bx = poly_bound(x); by = poly_bound(y)
    rem = ub(spill + x.rem*by + y.rem*bx + x.rem*y.rem)
    return TM(c, rem, H)
def tm_pow_list(q, n):   # [q^0 .. q^n]
    out = [const(1, q.H), q]
    for _ in range(2, n+1): out.append(tm_mul(out[-1], q))
    return out
def tm_fun(x, kind):
    """sin or expm1 of a Taylor model via Taylor expansion about the constant term."""
    p0 = x.c.get((0,)*NV, ZERO)
    q = x.copy(); q.c.pop((0,)*NV, None)
    qb = tm_bound(q)
    qp = tm_pow_list(q, KDEG)
    out = TM({}, ZERO, x.H)
    for j in range(KDEG+1):
        if kind == 'sin':
            d = [iv.sin(p0), iv.cos(p0), -iv.sin(p0), -iv.cos(p0)][j % 4]
        else:
            d = iv.exp(p0)
        out = tm_add(out, TM({a: (d/fact(j))*v for a, v in qp[j].c.items()}, ub(absmax(d/fact(j))*qp[j].rem), x.H))
    # Lagrange remainder of order KDEG+1 on |q| <= qb
    if kind == 'sin': lag = qb**(KDEG+1) / fact(KDEG+1)
    else:             lag = iv.exp(absmax(p0) + qb) * qb**(KDEG+1) / fact(KDEG+1)
    out.rem = ub(out.rem + lag)
    if kind == 'exp': out = tm_sub(out, const(1, x.H))
    return out
def Te(v):
    r, e = v
    se = tm_fun(e, 'sin')
    return (tm_sub(r, se), tm_sub(tm_add(e, tm_fun(r, 'exp')), se))
def Nstep(s, c):
    a = s
    b = (tm_add(tm_scale(-0.5, s[0]), c[0]), tm_add(tm_scale(-0.5, s[1]), c[1]))
    d = (tm_sub(tm_scale(-0.5, s[0]), c[0]), tm_sub(tm_scale(-0.5, s[1]), c[1]))
    A, B, Dd = Te(a), Te(b), Te(d)
    s2 = tuple(tm_scale(Fr(1,3), tm_sub(tm_sub(tm_scale(2, A[i]), B[i]), Dd[i])) for i in range(2))
    c2 = tuple(tm_scale(0.5, tm_sub(B[i], Dd[i])) for i in range(2))
    return s2, c2
SQ2 = ub(iv.sqrt(iv.mpf(2))); SQ32 = ub(iv.sqrt(iv.mpf(3)/2)); SQ3 = ub(iv.sqrt(iv.mpf(3)))
def strip(x): return TM(dict(x.c), ZERO, x.H)
def eucl2(a, b): return ub(iv.sqrt(a*a + b*b))
def Fmap(s, c):
    """Six modal steps with remainder transport.
    State: polynomial parts (s, c) with zero remainder, plus B-norm remainder bounds (rho_s, rho_c) that enclose the
    true deviation of the exact map image from the polynomial parts.  Per step the exact linear part A(+)A is a
    B-isometry (PE = I), so  rho_s' <= (1+lam) rho_s + (2lam/3) rho_c ,  rho_c' <= (1+lam) rho_c + (lam/2) rho_s ,
    lam = sqrt3 * Frobenius(Dn) on the enlarged region, n = T_e - A the nonlinear part; plus the fresh truncation /
    Lagrange remainders generated by the polynomial arithmetic of the step (converted to B-norm)."""
    rho_s = ub(SQ32 * eucl2(s[0].rem, s[1].rem)); rho_c = ub(SQ32 * eucl2(c[0].rem, c[1].rem))
    s = (strip(s[0]), strip(s[1])); c = (strip(c[0]), strip(c[1]))
    for _ in range(6):
        # Lipschitz constant of the nonlinear part on the enlarged region: edge component magnitude bound a
        rs = SQ2 * rho_s; rc = SQ2 * rho_c           # componentwise remainder bounds
        comp = [tm_bound(s[0]) + rs, tm_bound(s[1]) + rs, tm_bound(c[0]) + rc, tm_bound(c[1]) + rc]
        a = ZERO
        for i in range(2):
            a = iv.mpf(max((comp[i]).b, (comp[i]/2 + comp[2+i]).b, a.b))
        fro = ub(iv.sqrt(2*(1 - iv.cos(a))**2 + (iv.exp(a) - 1)**2))
        lam = ub(SQ3 * fro)
        s2, c2 = Nstep(s, c)
        fresh_s = ub(SQ32 * eucl2(s2[0].rem, s2[1].rem)); fresh_c = ub(SQ32 * eucl2(c2[0].rem, c2[1].rem))
        rho_s, rho_c = ub((1+lam)*rho_s + (2*lam/3)*rho_c + fresh_s), ub((1+lam)*rho_c + (lam/2)*rho_s + fresh_c)
        s = (strip(s2[0]), strip(s2[1])); c = (strip(c2[0]), strip(c2[1]))
    return s, c, rho_s, rho_c, lam
def binom_tm(tau, m):  # binom(tau, m) as TM polynomial
    out = const(1, tau.H)
    for j in range(m): out = tm_mul(out, tm_sub(tau, const(j, tau.H)))
    return tm_scale(Fr(1, int(mp.factorial(m))), out)
def C_N_tm(N, s, tau):
    r, e = s
    rp = tm_pow_list(r, N); ep = tm_pow_list(e, N)
    bt = {m: binom_tm(tau, m) for m in range(0, (N-3)//2 + 1)}
    out = [TM({}, ZERO, r.H), TM({}, ZERO, r.H)]
    for d in range(3, N+1):
        for m, coef in Cpoly[d].items():
            for i in range(2):
                acc = TM({}, ZERO, r.H)
                for k, a in enumerate(coef[i]):
                    if a == 0: continue
                    acc = tm_add(acc, tm_scale(a, tm_mul(rp[d-k], ep[k])))
                out[i] = tm_add(out[i], tm_mul(bt[m], acc))
    return tuple(out)

# ------------------------------------------------------------------ certificate on one box
def certify_box(N, r0, e0, tau0, h, htau):
    H = (ivq(Fr(str(h))), ivq(Fr(str(h))), ivq(Fr(str(htau))))
    r = tm_add(const(r0, H), var(0, H)); e = tm_add(const(e0, H), var(1, H)); tau = tm_add(const(tau0, H), var(2, H))
    s = (r, e); c = C_N_tm(N, s, tau)
    sp, cp, rho_s, rho_c, lam = Fmap(s, c)
    cpred = C_N_tm(N, sp, tm_add(tau, const(1, H)))
    E = (tm_sub(cp[0], cpred[0]), tm_sub(cp[1], cpred[1]))
    # Lipschitz bound of C_N(., tau+1) in s on the region (B-norm): L_C = sum_d sum_m |binom(tau+1,m)| * d * sum_k |a_dk| * R^(d-1) * sqrt2
    # REVIEW PATCH: derivative bound must contain the ACTUAL post-map parent s+, not the input box.
    # poly_bound(sp[i]) encloses the Taylor polynomial on the input box;
    # SQ2*rho_s encloses the transported B-norm remainder componentwise in Euclidean coordinates.
    post_abs_r = ub(poly_bound(sp[0]) + SQ2*rho_s)
    post_abs_e = ub(poly_bound(sp[1]) + SQ2*rho_s)
    Rm = ub(iv.sqrt(post_abs_r**2 + post_abs_e**2))
    tb = ivq(abs(Fr(str(tau0))) + Fr(str(htau)) + 1)
    L_C = ZERO
    for d in range(3, N+1):
        for m, coef in Cpoly[d].items():
            bm = ONE
            for j in range(m): bm = bm * (tb + j) / (j+1)
            L_C += bm * d * sum(absmax(ivq(a)) for row in coef for a in row) * Rm**(d-1)
    L_C = ub(SQ2 * SQ32 * L_C)
    # rigorous enclosure of E on the box: polynomial parts + fresh remainders (B-norm) + transported remainders
    bE = (tm_bound(E[0]), tm_bound(E[1]))
    eucl = ub(iv.sqrt(bE[0]**2 + bE[1]**2))
    bnorm = ub(SQ32 * eucl + rho_c + L_C * rho_s)
    # value at centre (enclosure): constant terms +- remainder
    cen = (E[0].c.get((0,)*NV, ZERO), E[1].c.get((0,)*NV, ZERO))
    cen_abs = ub(iv.sqrt(absmax(cen[0])**2 + absmax(cen[1])**2))
    # REVIEW PATCH: exact decimal rational box endpoints, outward-rounded radial extrema.
    aa, bb, hh = abs(Fr(str(r0))), abs(Fr(str(e0))), Fr(str(h))
    lower_sq = max(aa-hh, Fr(0))**2 + max(bb-hh, Fr(0))**2
    upper_sq = (aa+hh)**2 + (bb+hh)**2
    Rmin = iv.sqrt(ivq(lower_sq)).a
    Rmax = ub(iv.sqrt(ivq(upper_sq)))
    K = ub(bnorm / Rmin**(N+1))
    return dict(N=N, centre=(r0, e0, tau0), h=h, htau=htau, Rmin=Rmin, Rmax=Rmax, bound_B=bnorm, bound_eucl=eucl,
                centre_abs=cen_abs, rem=(rho_s, rho_c), K=K, lam=lam, L_C=L_C)

if BOXSET == 'small':
    boxes = [('0.0325', '0', '0.05', HBOX, '0.05')]
else:   # stage-1 sample: three boxes at R ~ 0.03..0.035, tau near 0 and near 2, and the Q_s-maximal direction
    boxes = [('0.0325', '0', '0.05', HBOX, '0.05'), ('0.0325', '0', '1.95', HBOX, '0.05'), ('-0.023', '0.023', '0.05', HBOX, '0.05')]
t0 = time.time()
print(f"Taylor-model degree K={KDEG}, {len(MONOS)} monomials; box half-widths h={HBOX}, h_tau=0.05; kappa=sqrt3; iv.dps={iv.dps}")
for box_index, (r0, e0, tau0, h, htau) in enumerate(boxes):
    if ONLY_BOX >= 0 and box_index != ONLY_BOX: continue
    for N in (7, 8):
        if ONLY_N and N != ONLY_N: continue
        res = certify_box(N, r0, e0, tau0, h, htau)
        print(f"N={N} box centre (r,e,tau)=({r0},{e0},{tau0}) h={h} h_tau={htau}: R in [{mp.nstr(res['Rmin'].b,4)},{mp.nstr(res['Rmax'].b,4)}]"
              f"\n   certified sup_box |E_{N}|_B <= {mp.nstr(res['bound_B'].b,5)}   (poly part Euclid {mp.nstr(res['bound_eucl'].b,5)}; transported B-norm remainders rho_s={mp.nstr(res['rem'][0].b,2)}, rho_c={mp.nstr(res['rem'][1].b,2)}; lam={mp.nstr(res['lam'].b,3)}, L_C={mp.nstr(res['L_C'].b,3)})"
              f"\n   |E_{N}(centre)| enclosure = {mp.nstr(res['centre_abs'].b,5)}   ->  certified K_{N} = bound/Rmin^{N+1} = {mp.nstr(res['K'].b,5)}   [{time.time()-t0:.0f}s]")
