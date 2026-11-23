#!/usr/bin/env python3
# DYAD OPEN 3 -- P3 remainder certificate (exit-gated, exact rational arithmetic).
# Target per NF-REM row r in {1/20, 1/40} (rows not mixed), for 0 < |z| <= r, one block F = T^6, normalized chart:
#   |S_Theta(z) - L_Theta(z)| <= K_Theta(r) q^2 ,   |S_Q(z) - [S_Q]_5(z)| <= K_Q(r) q^3 ,   q = |z|^2.
# Inputs: adopted DYAD v6.4.13 -- DYAD-ALG-NF6 (h regenerated exactly here and checked), DYAD-THM-NF-INV (|h/z-1|<1/16 on |z|<=1/10),
#   DYAD-THM-NF-REM (|Fhat-J| <= C7|z|^7 on |z|<=r: C7=100 (r=1/20), 30 (r=1/40)), jet J (regenerated, checked).
# All bounds are rational upper bounds; moduli |c| of c in Q(i sqrt3) are replaced by rational ceilings of sqrt(|c|^2).
import sys, json, math
sys.path.insert(0, '.')
from dyad_return_qchi_exact import Q, P
from fractions import Fraction as Fr
from math import factorial, isqrt
N = 6
chi = Q(0, 1); om = Q(Fr(-1, 2), Fr(1, 2)); lam = Q(Fr(1, 2), Fr(1, 2)); lamb = lam.conj()
z = P({(1, 0): Q(1)}, N); zb = P({(0, 1): Q(1)}, N); one = P({(0, 0): Q(1)}, N)
eta = (z - zb).scale(Q(0, Fr(-1, 3))); rho = z - eta.scale(om)
def series(x, cf):
    r = P({}, N); p = one
    for k in range(1, N+1):
        p = p*x
        if cf(k) != 0: r = r + p.scale(Q(cf(k)))
    return r
sinx = lambda x: series(x, lambda k: 0 if k % 2 == 0 else Fr((-1)**((k-1)//2), factorial(k)))
expm1 = lambda x: series(x, lambda k: Fr(1, factorial(k)))
f = (rho - sinx(eta)) + (eta + expm1(rho) - sinx(eta)).scale(om)
comp = lambda a, b: a.compose(b, b.conj())
h = z; n = z.scale(lam)
for k in range(2, N+1):
    E = (comp(f, h) - comp(h, n)).deg(k)
    for (a, b), v in E.d.items():
        mult = Q(1)
        for _ in range(a): mult = mult*lam
        for _ in range(b): mult = mult*lamb
        if (a-b-1) % 6 == 0: n = n + P({(a, b): v}, N)
        else: h = h + P({(a, b): (-v)/(lam-mult)}, N)
J = n
for _ in range(5): J = comp(n, J)
chk = {}
s3 = Q(0, 1)  # i*sqrt3
mu = J.get((2, 1)); a32 = J.get((3, 2)); a05 = J.get((0, 5))
chk['mu = -1/2 - i*2sqrt3/3'] = mu == Q(Fr(-1, 2), Fr(-2, 3))
chk['J linear = id'] = J.get((1, 0)) == Q(1) and J.get((0, 1)).iszero()
chk['J has only (1,0),(2,1),(3,2),(0,5) through deg 6'] = set(k for k, v in J.d.items() if sum(k) <= 6) == {(1, 0), (2, 1), (3, 2), (0, 5)}
chk['chart law 245/216 = |mu|^2 + 2Re a32'] = (mu*mu.conj() + (a32 + a32.conj())) == Q(Fr(245, 216))
im = lambda c: (c - c.conj())/Q(0, 2)        # (c - cbar)/(2i) as element: Im c * 1 ... returns i*sqrt3*b / (2i)?
# Im(x) for x=a+b*i*sqrt3 equals b*sqrt3 ; check 89 sqrt3/324 = Im(a32 - mu^2/2) via the chi-coefficient
chk['chart law 89sqrt3/324 = Im(a32 - mu^2/2)'] = (a32 - mu*mu*Q(Fr(1, 2))).b == Fr(89, 324)
h2ref = {(2, 0): Q(Fr(-1, 12), Fr(-1, 12)), (1, 1): Q(Fr(-1, 3)), (0, 2): Q(Fr(1, 24), Fr(-1, 24))}
chk['h2 matches NF6'] = all(h.get(k) == v for k, v in h2ref.items()) and len(h.deg(2).d) == 3
chk['h has 23 nonzero coefficients incl. linear'] = len(h.d) == 23
chk['resonant coefficients of h are zero'] = all((a-b-1) % 6 != 0 for (a, b) in h.d if a+b >= 2)
# ---------- rational modulus ceilings ----------
SC = 10**12
def ub_sqrt(x):  # rational >= sqrt(x), x Fraction >= 0
    num = x.numerator*SC*SC; den = x.denominator
    r = isqrt(num//den) + 1
    return Fr(r, SC)
def abs2(c): return c.a*c.a + 3*c.b*c.b
def ub_abs(c):
    if c.iszero(): return Fr(0)
    x = abs2(c); rn, rd = isqrt(x.numerator), isqrt(x.denominator)
    if rn*rn == x.numerator and rd*rd == x.denominator: return Fr(rn, rd)   # exact modulus
    return ub_sqrt(x)
Mcoef = {2: Fr(7, 12), 3: Fr(39, 500), 4: Fr(14, 125), 5: Fr(11, 250), 6: Fr(1, 20)}
for k in range(2, 7):
    chk[f'deg-{k} modulus sum of h <= M(s) coefficient'] = sum(ub_abs(v) for v in h.deg(k).d.values()) <= Mcoef[k] + Fr(1, 10**9) if k > 2 else True
# exact degree-2 modulus sum = 7/12 (moduli 1/6, 1/3, 1/12)
chk['deg-2 moduli exact 1/6,1/3,1/12'] = [abs2(h.get(k)) for k in [(2, 0), (1, 1), (0, 2)]] == [Fr(1, 36), Fr(1, 9), Fr(1, 144)]
absmu = ub_abs(mu); A5 = ub_abs(a32) + ub_abs(a05)
# g = (h - z)/z : monomial c z^a zb^b of h_k -> c z^(a-1) zb^b ; |g| <= sum |c| s^(k-1) ; ||Dg|| <= sum |c| (|a-1|+b) s^(k-2)
def Gpoly(kmin):  # dict power -> coeff for |g| bound
    d = {}
    for (a, b), v in h.d.items():
        k = a+b
        if k >= kmin: d[k-1] = d.get(k-1, 0) + ub_abs(v)
    return d
def G1poly(kmin):
    d = {}
    for (a, b), v in h.d.items():
        k = a+b
        if k >= kmin: d[k-2] = d.get(k-2, 0) + ub_abs(v)*(abs(a-1)+b)
    return d
ev = lambda d, s: sum(c*s**p for p, c in d.items())
c20, c11, c02 = h.get((2, 0)), h.get((1, 1)), h.get((0, 2))
L1 = ub_abs(c20) + ub_abs(c11) + 3*ub_abs(c02)        # ||D g1|| (g1 = h2/z), homogeneous degree 0
# D_Q = |h|^2 - |z|^2 as exact polynomial (degree <= 12)
Nb = 12
hz = P(h.d, Nb); hzc = hz.conj(); zz = P({(1, 0): Q(1)}, Nb); zzc = zz.conj()
DQ = hz*hzc - zz*zzc
B = {k: sum(ub_abs(v) for v in DQ.deg(k).d.values()) for k in range(3, 13)}
chk['D_Q has no degree < 3'] = all(sum(k) >= 3 for k in DQ.d)
D3ref = (zzc*P(h.deg(2).d, Nb)) + (zz*P(h.deg(2).d, Nb).conj())
chk['[D_Q]_3 = 2Re(zbar h2)'] = all((DQ.deg(3) - D3ref).d[k].iszero() for k in (DQ.deg(3) - D3ref).d) if (DQ.deg(3) - D3ref).d else True
rows = {Fr(1, 20): 100, Fr(1, 40): 30}
out = {'rows': {}}
for r, C7 in rows.items():
    s = r
    beta = absmu*s**2 + A5*s**4 + C7*s**6        # |delta| <= s*beta ; delta = Fhat(z) - z
    rhob = A5*s**5 + C7*s**7                      # |delta - mu q z|
    sp_ = s*(1 + beta)                            # segment radius bound
    Gs = ev(Gpoly(2), sp_); G1s = ev(G1poly(2), sp_); G1ge2 = ev(G1poly(3), sp_)
    ok_dom = Gs < Fr(1, 16) and sp_ <= Fr(1, 10) and beta < Fr(1, 2)
    # angular pieces (each already divided by q^2 = s^4); monotone increasing in s, so value at s=r is the sup
    TA1 = 4*ub_abs(c02)*s*beta**2/(1 - beta) / s**4         # 2nd-order Taylor of Im(c02 zb^2/z): |D^2 phi| <= 8|v|^2/|w|, |w| >= s(1-beta)
    TA2 = L1*rhob / s**4                                     # D g1 [delta - mu q z]
    TB = G1ge2*s*beta / s**4                                 # Im g_{>=2}(z') - Im g_{>=2}(z)
    TC = (Gs/(1 - Gs))*G1s*s*beta / s**4                     # [Im Log(1+g) - Im g] increment
    KT = TA1 + TA2 + TB + TC
    # angular static constants: |D_Theta - Im g1| <= c1 s^2 ; ||D D_Theta|| <= c2 ; ||D^2 Im g1(w)|| <= c3/|w|
    Gge2 = ev(Gpoly(3), s); G0 = ev(Gpoly(2), s)
    c1 = (Gge2 + G0**2/(2*(1 - G0)))/s**2
    c2 = ev(G1poly(2), s)/(1 - G0)
    c3 = 8*ub_abs(c02)
    # radial: S_Q - [S_Q]_5 = [D3(z+d)-D3(z)-DD3[d]] + DD3[d - mu q z] + [D_{>=4}(z')-D_{>=4}(z)]
    RA = Fr(1, 2)*6*B[3]*sp_*(s*beta)**2 / s**6
    RB = 3*B[3]*s**2*rhob / s**6
    RC = sum(k*B[k]*sp_**(k-1) for k in range(4, 13))*s*beta / s**6
    KQ = RA + RB + RC
    dec = lambda x: float(x)
    ceil_r = lambda x, d=1000: Fr(math.ceil(x*d), d)
    out['rows'][str(r)] = {
        'C7': C7, 'domain_ok(|g|<1/16, s+ <= 1/10, beta<1/2)': ok_dom,
        'beta(r)': dec(beta), 'K_Theta_exact_rational': str(KT), 'K_Theta_float': dec(KT), 'K_Theta_stated': str(ceil_r(KT)),
        'K_Theta_parts(A1,A2,B,C)': [dec(TA1), dec(TA2), dec(TB), dec(TC)],
        'c1': str(ceil_r(c1)), 'c2': str(ceil_r(c2)), 'c3 (per 1/|w|)': str(c3),
        'K_Q_exact_rational': str(KQ), 'K_Q_float': dec(KQ), 'K_Q_stated': str(ceil_r(KQ)),
        'K_Q_parts(A,B,C)': [dec(RA), dec(RB), dec(RC)],
        'primitive_form: K_Theta*(256/225)^2': str(ceil_r(ceil_r(KT)*Fr(256, 225)**2)),
        'primitive_form: K_Q*(256/225)^3': str(ceil_r(ceil_r(KQ)*Fr(256, 225)**3))}
    chk[f'row {r}: domain conditions'] = ok_dom
out['inputs'] = {'|mu| ub': str(absmu), 'A5=|a32|+|a05| ub': str(A5), 'a32': repr(a32), 'a05': repr(a05), 'L1': str(L1),
                 'B_k (D_Q degree-k modulus sums, k=3..12)': {k: float(v) for k, v in B.items()}}
out['checks'] = chk
ok = all(chk.values())
NEG = sys.argv[1] if len(sys.argv) > 1 else ''
# negative controls (each must make the script exit 1):
#   neg_K   : state K_Theta one unit in the third decimal below the exact rational value
#   neg_h2  : perturb the c02 coefficient of h2 (NF6 identity check must fail)
#   neg_mu  : use conj(mu) as the cubic coefficient (mu identity check must fail)
if NEG == 'neg_h2': chk['h2 matches NF6'] = (h.get((0, 2)) + Q(Fr(1, 1000))) == h2ref[(0, 2)]
if NEG == 'neg_mu': chk['mu = -1/2 - i*2sqrt3/3'] = mu.conj() == Q(Fr(-1, 2), Fr(-2, 3))
ok = all(chk.values())
for v in out['rows'].values():
    KTs = Fr(v['K_Theta_stated']) - (Fr(1, 1000) + (Fr(v['K_Theta_stated']) - Fr(v['K_Theta_exact_rational'])) if NEG == 'neg_K' else 0)
    ok = ok and KTs >= Fr(v['K_Theta_exact_rational']) and Fr(v['K_Q_stated']) >= Fr(v['K_Q_exact_rational'])
out['verdict'] = 'PASS' if ok else 'FAIL'
for v in out['rows'].values():
    v.pop('K_Theta_exact_rational'); v.pop('K_Q_exact_rational')
json.dump(out, open('p3_certificate.json' if not NEG else 'p3_'+NEG+'.json', 'w'), indent=1, default=str)
print(json.dumps(out, indent=1, default=str))
sys.exit(0 if ok else 1)
