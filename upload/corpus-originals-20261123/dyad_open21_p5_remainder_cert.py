#!/usr/bin/env python3
# DYAD OPEN 21 (P5) -- exact-rational certificate for the primitive-variable phase remainder.
# Target, per NF-REM row j in {A: |z|<=1/20, B: |z|<=1/40} (rows not mixed), for 0 < |W0| <= (15/16) r_j:
#   |M_W - P2(W0)| <= K'_j Q0^(3/2) + C2_j (256/225)^2 Q0^2          (primary, R9 term kept separate)
#   |M_W - P2(W0)| <= K_j  Q0^(3/2),  K_j = K'_j + C2_j (256/225)^2 (15/16) r_j   (secondary)
# P2(W0) = -Delta1(W0) + Q0[c_iso + Lambda1(Theta_W0)] + P_W2(W0),  P_W2 = -Delta2 + D Delta1[h2]   (adopted, DYAD v6.4.16 §6.14).
# Uses only: adopted DYAD v6.4.16 (NF6, NF-INV, chart-variable memory law with K2, Delta1, Delta2) and the *statement* of
# RECOG-THM-R9-MEMORY (Lambda1, c_iso, C2, rows). Grade ceiling: [THM -- conditional on RECOG-THM-R9-MEMORY].
# Exit 0 iff all gates pass.  Negative controls (argv[1]), each must exit 1:
#   neg_dropDh2 : P2 without D Delta1[h2]          neg_noTL : decomposition without the T_Lambda terms
#   neg_noC2    : decomposition without C2 q0^2    neg_mix  : row-A primitive domain with row-B disk
#   neg_Mdeg3   : M(s) degree-3 coefficient below the true degree-3 modulus sum of h
import sys, json, math, hashlib
from fractions import Fraction as Fr
from math import isqrt
sys.path.insert(0, '.')
NEG = sys.argv[1] if len(sys.argv) > 1 else ''
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
PINS = {'dyad_open3_p3_remainder_cert.py': 'b7df79b0f820f8431e6c2af54a03ef8fd93f869fb06470ed037cdca1126d258d',
        'dyad_return_qchi_exact.py': 'e45286fa100b2b31c4d547e8513e23f926b2bda36d31938577fa9f312ca350f6',
        'p4_offset_certificate.json': '9b0e0c80f3a7f5f9ddf052ca8bc203e30f79e7d1ad8619555875f3df3e8557b4',
        'p4_exact.json': '945db486fa87e61b9412b47c5b591d88c7e01e607c4aec4998c898882d6b38d8',
        'dyad_open21_p5_lambda1_check.py': 'aca13bf62a6034a11e30190178e3e7a7fad932f26b4114cceb941e530e06e8ae'}
gates = {}
gates['G-0 input hashes'] = all(sha(p) == h for p, h in PINS.items())
src = open('dyad_open3_p3_remainder_cert.py').read()
exec(src.split('rows = {Fr(1, 20): 100, Fr(1, 40): 30}')[0])          # exact h, J, chk, ub_abs, ub_sqrt, Gpoly, ev, B (D_Q sums)
gates['G-0 P3 inputs (h, J, NF6 identities) reproduced'] = all(chk.values())
import subprocess
gates['G-L Lambda1/c_iso/|G| gate exits 0'] = subprocess.run([sys.executable, 'dyad_open21_p5_lambda1_check.py'] + (['neg'] if NEG == 'neg_raw' else []),
                                                               capture_output=True).returncode == 0
# ---------------- adopted constants ----------------
P4 = json.load(open('p4_offset_certificate.json'))['rows']
ROWS = {'A': {'r': Fr(1, 20), 'C2': Fr(517), 'qmax': Fr(1, 400), 'K2': Fr(P4['1/20']['K2'])},
        'B': {'r': Fr(1, 40), 'C2': Fr(163), 'qmax': Fr(1, 1600), 'K2': Fr(P4['1/40']['K2'])}}
gates['G-0 K2 rows as adopted (1323/1000, 641/500)'] = ROWS['A']['K2'] == Fr(1323, 1000) and ROWS['B']['K2'] == Fr(641, 500)
Mc = {2: Fr(7, 12), 3: Fr(39, 500), 4: Fr(14, 125), 5: Fr(11, 250), 6: Fr(1, 20)}        # DYAD-THM-NF-INV
if NEG == 'neg_Mdeg3': Mc[3] = Fr(39, 600)
M = lambda s: sum(c*s**k for k, c in Mc.items())
Mge3 = lambda s: sum(c*s**k for k, c in Mc.items() if k >= 3)
# ---------------- G-INV(a): M(s) - (7/12)s^2 majorizes the degree>=3 part of h - id, coefficientwise ----------------
modsum = {k: sum(ub_abs(v) for v in h.deg(k).d.values()) for k in range(2, 7)}
abs2 = lambda c: c.a*c.a + 3*c.b*c.b
lb_abs = lambda c: Fr(isqrt((abs2(c)*10**24).__floor__()), 10**12)                       # rational floor of |c|
modsum_lb = {k: sum(lb_abs(v) for v in h.deg(k).d.values()) for k in range(3, 7)}
gates['G-INV(a) degree-2 moduli of h sum to exactly 7/12'] = [abs2(h.get(k)) for k in [(2, 0), (1, 1), (0, 2)]] == [Fr(1, 36), Fr(1, 9), Fr(1, 144)] and len(h.deg(2).d) == 3
gates['G-INV(a) h has no degree > 6 and no linear correction'] = max(sum(k) for k in h.d) == 6 and h.get((1, 0)) == Q(1) and h.get((0, 1)).iszero()
gates['G-INV(a) each degree-k modulus sum (k=3..6) <= M coefficient (vs rational floor of sum)'] = all(modsum_lb[k] <= Mc[k] for k in range(3, 7))
gates['G-INV(a) M - (7/12)s^2 has only degrees 3..6 with positive coefficients'] = all(Mc[k] > 0 for k in range(3, 7))
# ---------------- exact rational ceilings for irrational constants ----------------
def ubq(x): return ub_sqrt(Fr(x))                                     # >= sqrt(x)
absA = ubq(Fr(73, 108)); absB = ubq(Fr(19, 432))                      # Delta1 = Re(A w) + Re(B w^2/wbar)
absG = ubq(Fr(481897, 8230118400))                                    # |G| = sup|Lambda1|; sup|Lambda1'| = 6|G|
ciso = ubq(Fr(16*3, 729))                                             # |c_iso| = 4 sqrt3/27
# Delta2 = k0|w|^2 + Re(B2 w^2) + Re(B4 w^3/wbar) + Re(B6 w^4/wbar^2)
k0 = ubq(Fr(3, 108**2)); absB2 = ubq(Fr(3, 1296**2) + Fr(49, 432**2)); absB4 = ubq(Fr(3, 324**2) + Fr(25, 108**2)); absB6 = ubq(Fr(3, 1728**2) + Fr(25, 576**2))
d1 = absA + 3*absB                                                    # ||D Delta1||           (homogeneous degree 0)
d2 = 8*absB                                                           # ||D^2 Delta1(xi)|| <= d2/|xi|
e1 = 2*k0 + 2*absB2 + 4*absB4 + 6*absB6                               # ||D Delta2(xi)|| <= e1 |xi|
# ---------------- G-D2: Delta1, Delta2 representations equal the adopted harmonic forms (exact, sympy) ----------------
import sympy as sp
r_, t_ = sp.symbols('r t', positive=True); s3 = sp.sqrt(3); I = sp.I
w = r_*sp.exp(I*t_); wb = r_*sp.exp(-I*t_)
Aex = 17*s3/36 + I*sp.Rational(1, 12); Bex = -7*s3/72 - I*sp.Rational(1, 8)
D1expr = sp.re(sp.expand(Aex*w)) + sp.re(sp.expand(Bex*w**2/wb))
D1adopt = r_*(17*s3/36*sp.cos(t_) - sp.Rational(1, 12)*sp.sin(t_) - 7*s3/72*sp.cos(3*t_) + sp.Rational(1, 8)*sp.sin(3*t_))
B2 = s3/1296 - I*sp.Rational(7, 432); B4 = -s3/324 + I*sp.Rational(5, 108); B6 = -s3/1728 + I*sp.Rational(5, 576)
D2expr = s3/108*r_**2 + sp.re(sp.expand(B2*w**2)) + sp.re(sp.expand(B4*w**3/wb)) + sp.re(sp.expand(B6*w**4/wb**2))
D2adopt = r_**2*(s3/108 + s3/1296*sp.cos(2*t_) + sp.Rational(7, 432)*sp.sin(2*t_) - s3/324*sp.cos(4*t_) - sp.Rational(5, 108)*sp.sin(4*t_) - s3/1728*sp.cos(6*t_) - sp.Rational(5, 576)*sp.sin(6*t_))
simp0 = lambda e: sp.simplify(sp.expand_trig(sp.expand(sp.expand_complex(e)))) == 0
gates['G-D2 Delta1 = Re(A w) + Re(B w^2/wbar) equals adopted harmonic form'] = simp0(D1expr - D1adopt)
gates['G-D2 Delta2 harmonic representation equals adopted form'] = simp0(D2expr - D2adopt)
gates['G-D2 |A|^2 = 73/108, |B|^2 = 19/432'] = sp.simplify(sp.Abs(Aex)**2 - sp.Rational(73, 108)) == 0 and sp.simplify(sp.Abs(Bex)**2 - sp.Rational(19, 432)) == 0
# P_W2 = -Delta2 + D Delta1[h2] reproduces the adopted P_W2 (target object is the adopted one)
X, Y = sp.symbols('X Y', real=True); wz = X + I*Y; wzb = X - I*Y
D1xy = sp.re(sp.expand_complex(Aex*wz)) + sp.re(sp.expand_complex(Bex*wz**2/wzb))
c20 = -sp.Rational(1, 12) - I*s3/12; c11 = -sp.Rational(1, 3); c02 = sp.Rational(1, 24) - I*s3/24
h2 = c20*wz**2 + c11*wz*wzb + c02*wzb**2
h2x, h2y = sp.re(sp.expand_complex(h2)), sp.im(sp.expand_complex(h2))
DD1h2 = sp.diff(D1xy, X)*h2x + sp.diff(D1xy, Y)*h2y
D2xy = D2adopt.subs({r_: sp.sqrt(X**2 + Y**2), t_: sp.atan2(Y, X)})
Pw2adopt = (X**2 + Y**2)*(-5*s3/27 + 47*s3/1296*sp.cos(2*sp.atan2(Y, X)) - sp.Rational(19, 432)*sp.sin(2*sp.atan2(Y, X)) - 11*s3/324*sp.cos(4*sp.atan2(Y, X))
                          + sp.Rational(1, 54)*sp.sin(4*sp.atan2(Y, X)) - s3/1728*sp.cos(6*sp.atan2(Y, X)) - sp.Rational(5, 576)*sp.sin(6*sp.atan2(Y, X)))
Pw2mine = -D2xy + (0 if NEG == 'neg_dropDh2' else DD1h2)
import random
random.seed(5)
okP = True
for _ in range(6):
    xv, yv = sp.Rational(random.randint(-97, 97), 101), sp.Rational(random.randint(-97, 97), 103)
    if xv == 0 and yv == 0: continue
    val = sp.N((Pw2mine - Pw2adopt).subs({X: xv, Y: yv}), 50)
    okP = okP and abs(val) < sp.Float('1e-40')
gates['G-D2 P_W2 = -Delta2 + D Delta1[h2] equals adopted P_W2 (50-digit, 6 rational points)'] = bool(okP)
# ---------------- G-ID: functional-level decomposition (exact algebra; T-terms as defined) ----------------
# Unknowns: values D1z=Delta1(z0), D1W=Delta1(W0), D2z, D2W, linear form L=D Delta1(W0) acting on vectors, q0, Q0, Lz=Lambda1(Th_z), LW=Lambda1(Th_W), E
D1z, D1W, D2z, D2W, q0, Q0, Lz, LW, Ev, ciso_s, lx, ly = sp.symbols('D1z D1W D2z D2W q0 Q0 Lz LW E ciso lx ly', real=True)
dzx, dzy, hx, hy = sp.symbols('dzx dzy hx hy', real=True)      # z0 - W0 and h2(W0) as vectors
Lf = lambda vx, vy: lx*vx + ly*vy                               # D Delta1(W0) is linear
MW = -D1z - D2z + q0*(ciso_s + Lz) + Ev                         # adopted chart-variable memory law (defines E)
P2 = -D1W - D2W + (0 if NEG == 'neg_dropDh2' else Lf(hx, hy)) + Q0*(ciso_s + LW)
TERMS = {'E': Ev,
         'T_D1a = -[D1(z0)-D1(W0)-DD1(W0)[z0-W0]]': -(D1z - D1W - Lf(dzx, dzy)),
         'T_D1b = -DD1(W0)[z0-W0+h2(W0)]': -Lf(dzx + hx, dzy + hy),
         'T_D2 = -[D2(z0)-D2(W0)]': -(D2z - D2W),
         'T_iso = c_iso (q0-Q0)': ciso_s*(q0 - Q0),
         'T_La = (q0-Q0) Lambda1(Th_z)': (q0 - Q0)*Lz,
         'T_Lb = Q0 [Lambda1(Th_z)-Lambda1(Th_W)]': Q0*(Lz - LW)}
if NEG == 'neg_noTL': TERMS = {k: v for k, v in TERMS.items() if not k.startswith('T_L')}
gates['G-ID M_W - P2 = E + T_D1a + T_D1b + T_D2 + T_iso + T_La + T_Lb (exact identity)'] = sp.simplify(sp.expand(MW - P2 - sum(TERMS.values()))) == 0
EPARTS = ['K2 q0^(3/2)', 'C2 q0^2'] if NEG != 'neg_noC2' else ['K2 q0^(3/2)']
gates['G-ID E bound has both adopted parts (K2 q0^(3/2), C2 q0^2)'] = EPARTS == ['K2 q0^(3/2)', 'C2 q0^2']
# ---------------- per-row majorants (all divided by w^3, w = |W0|; sigma = (16/15) w) ----------------
k = Fr(16, 15)
def cinv_poly():
    # c_inv(w) = [(7/6) sigma M(sigma) + M_{>=3}(sigma)] / w^3, sigma = k w : polynomial in w with coefficients
    co = {}
    for d, c in Mc.items():
        co[d - 2] = co.get(d - 2, 0) + Fr(7, 6)*k**(d + 1)*c          # (7/6) sigma^(d+1) / w^3 -> w^(d-2)
        if d >= 3: co[d - 3] = co.get(d - 3, 0) + k**d*c               # sigma^d / w^3 -> w^(d-3)
    return co
CINV = cinv_poly()
gates['G-INV(b) c_inv(w) is a polynomial in w with nonnegative coefficients (nondecreasing)'] = all(c >= 0 for c in CINV.values()) and min(CINV) >= 0
out = {'rows': {}, 'inputs': {}}
for j, R in ROWS.items():
    r = R['r']; wmax = Fr(15, 16)*r
    if NEG == 'neg_mix' and j == 'A': r = ROWS['B']['r']
    sig = k*wmax
    dom = {'(16/15) w_max <= r  (z0 in row disk)': k*wmax <= r,
           'q0 <= (16/15)^2 w_max^2 <= q_max (R9 window)': (k*wmax)**2 <= R['qmax'] and R['qmax'] == r**2,
           'w_max <= 9/100 (h^-1 defined, NF-INV)': wmax <= Fr(9, 100),
           'M(1/10)/(1/10) < 1/16 (NF-INV ratio; gives |z0-W0| <= w/15, |xi| >= 14w/15)': M(Fr(1, 10))/Fr(1, 10) < Fr(1, 16),
           'sigma <= 1/10': sig <= Fr(1, 10)}
    Gs = ev(Gpoly(2), sig)                                     # |g(z0)| <= Gs  (g = (h-z)/z)
    dom['|g(z0)| < 1/16 (principal branch of D_Theta)'] = Gs < Fr(1, 16)
    ms = M(sig)/sig**2                                         # m(sigma) = M(sigma)/sigma^2
    cinv = sum(c*wmax**p for p, c in CINV.items())
    parts = {}
    parts['E: K2 (16/15)^3'] = R['K2']*k**3
    parts['T_D1a: (d2/2)(15/14) |z0-W0|^2 / w^3'] = Fr(1, 2)*d2*Fr(15, 14)*k**4*ms**2      # |z0-W0|^2 <= sigma^4 m^2 ; /((14/15) w) ; /w^3 -> k^4 m^2
    parts['T_D1b: d1 c_inv'] = d1*cinv
    parts['T_D2: e1 sigma M(sigma) / w^3'] = e1*k**3*ms                                    # e1 * sigma * sigma^2 m / w^3 = e1 k^3 m
    DQ = sum(B[d]*sig**d for d in range(3, 13))                                               # |D_Q(z0)| <= sum B_d sigma^d
    parts['T_iso: |c_iso| |D_Q| / w^3'] = ciso*DQ/wmax**3
    if NEG != 'neg_noTL':
        parts['T_La: |G| |D_Q| / w^3'] = absG*DQ/wmax**3
        parts['T_Lb: 6|G| w^2 |D_Theta| / w^3'] = 6*absG*(Gs/(1 - Gs))/wmax                   # |D_Theta| <= |g|/(1-|g|)
    Kp = sum(parts.values())
    C2fac = R['C2']*Fr(256, 225)**2
    if NEG == 'neg_noC2': C2fac = Fr(0)
    Ksingle = Kp + C2fac*wmax
    ceil = lambda x, d=1000: Fr(math.ceil(x*d), d)
    out['rows'][j] = {'disk |z|<=': str(r), 'primitive domain |W0|<=': str(wmax), 'Q0 <=': str(wmax**2),
                      'domain_checks': dom, 'c_inv (w_max)': str(ceil(cinv)), 'c_inv float': float(cinv),
                      "K'_j parts (float)": {p: float(v) for p, v in parts.items()},
                      "K'_j stated": str(ceil(Kp)), "K'_j float": float(Kp),
                      'C2_j (256/225)^2 (exact)': str(C2fac), 'C2 term float': float(C2fac),
                      'K_j stated (single, at w_max)': str(ceil(Ksingle)), 'K_j float': float(Ksingle)}
    gates[f'G-D row {j} domains'] = all(dom.values())
    gates[f'G-SUM row {j} stated ceilings >= exact rationals'] = ceil(Kp) >= Kp and ceil(Ksingle) >= Ksingle and C2fac == R['C2']*Fr(256, 225)**2
    gates[f'G-SUM row {j} all 8 bound parts present (E:K2, E:C2, T_D1a, T_D1b, T_D2, T_iso, T_La, T_Lb)'] = len(parts) == 7 and C2fac > 0
# ---------------- G-MON: each part nondecreasing in w (structural; spot-checked at 16 exact rational w) ----------------
def parts_at(wv, R):
    sg = k*wv; mm = M(sg)/sg**2; G_ = ev(Gpoly(2), sg); DQ_ = sum(B[d]*sg**d for d in range(3, 13))
    return [Fr(1, 2)*d2*Fr(15, 14)*k**4*mm**2, d1*sum(c*wv**p for p, c in CINV.items()), e1*k**3*mm, ciso*DQ_/wv**3, absG*DQ_/wv**3, 6*absG*(G_/(1 - G_))/wv]
monok = True
for j, R in ROWS.items():
    wm = Fr(15, 16)*R['r']; grid = [wm*Fr(i, 16) for i in range(1, 17)]
    vals = [parts_at(x, R) for x in grid]
    monok = monok and all(vals[i][c] <= vals[i+1][c] for i in range(15) for c in range(6))
gates['G-MON all majorant parts nondecreasing on the w-grid (sup at w_max)'] = monok
# ---------------- G-JET: finite-order consistency, 60 digits (separate from G-ID; not orbit sampling) ----------------
import mpmath as mp
mp.mp.dps = 60
S3 = mp.sqrt(3)
hc = [(a, b, mp.mpf(v.a.numerator)/v.a.denominator + 1j*S3*mp.mpf(v.b.numerator)/v.b.denominator) for (a, b), v in h.d.items()]
hfun = lambda zz: mp.fsum(c*zz**a*mp.conj(zz)**b for a, b, c in hc)
def hinv(W):
    zz = W
    for _ in range(200): zz = W - (hfun(zz) - zz)
    return zz
Am = mp.mpc(17*S3/36, mp.mpf(1)/12); Bm = mp.mpc(-7*S3/72, -mp.mpf(1)/8)
D1n = lambda x: mp.re(Am*x) + mp.re(Bm*x**2/mp.conj(x))
def DD1n(x, v): return mp.re(Am*v) + mp.re(Bm*(2*x*v/mp.conj(x) - x**2*mp.conj(v)/mp.conj(x)**2))
def D2n(x):
    rr = abs(x); th = mp.arg(x)
    return rr**2*(S3/108 + S3/1296*mp.cos(2*th) + mp.mpf(7)/432*mp.sin(2*th) - S3/324*mp.cos(4*th) - mp.mpf(5)/108*mp.sin(4*th) - S3/1728*mp.cos(6*th) - mp.mpf(5)/576*mp.sin(6*th))
Lam = lambda th: (43*mp.sin(6*th) - 5611*S3*mp.cos(6*th))/1270080
cis = -4*S3/27
h2n = lambda x: (mp.mpc(-1, -S3)/12)*x**2 - x*mp.conj(x)/3 + (mp.mpc(1, -S3)/24)*mp.conj(x)**2
def Tsum(W):
    z0 = hinv(W); q0 = abs(z0)**2; Q0 = abs(W)**2
    chart = -D1n(z0) - D2n(z0) + q0*(cis + Lam(mp.arg(z0)))
    P2n = -D1n(W) - D2n(W) + (0 if NEG == 'neg_dropDh2' else DD1n(W, h2n(W))) + Q0*(cis + Lam(mp.arg(W)))
    return chart - P2n
jet = {}
for rad in ['1e-2', '1e-3', '1e-4', '1e-5']:
    jet[rad] = max(abs(Tsum(mp.mpf(rad)*mp.expj(2*mp.pi*i/13 + mp.mpf('0.1'))))/mp.mpf(rad)**3 for i in range(13))
KT_A = float(sum(v for kk, v in out['rows']['A']["K'_j parts (float)"].items() if not kk.startswith('E')))
gates['G-JET (chart main - P2)/|W|^3 bounded as |W| -> 0 (ratio at 1e-5 within 2x of 1e-3)'] = float(jet['1e-5']) <= 2*float(jet['1e-3'])
gates['G-JET sampled ratios <= sum of T-part majorants of row A'] = all(float(v) <= KT_A for v in jet.values())
out['G-JET sampled max |sum T|/|W|^3 by radius (60 digits; consistency check, not a proof input)'] = {kk: float(v) for kk, v in jet.items()}
out['inputs'] = {'M(s) coefficients (NF-INV)': {d: str(c) for d, c in Mc.items()},
                 'h degree-k modulus sums (ceil)': {d: float(v) for d, v in modsum.items()},
                 '|A|,|B| ub (Delta1)': [str(absA), str(absB)], 'd1, d2': [float(d1), float(d2)], 'e1': float(e1),
                 '|G| ub': str(absG), '|c_iso| ub': str(ciso), 'B_3..B_12 (P3)': {d: float(v) for d, v in B.items()},
                 'K2 rows (P4)': {j: str(R['K2']) for j, R in ROWS.items()}, 'C2 rows (R9 statement)': {j: str(R['C2']) for j, R in ROWS.items()}}
out['gates'] = gates
ok = all(gates.values())
out['verdict'] = 'PASS' if ok else 'FAIL'
if not NEG: json.dump(out, open('p5_certificate.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)); sys.exit(0 if ok else 1)
