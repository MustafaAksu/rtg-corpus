#!/usr/bin/env python3
"""DZT owner review of the norm law (triage row 2): independent checks.

    python3 -I evidence/dzt/norm_law_review/dzt_norm_law_review_check.py [PMAX_EXACT [PMAX_SIGN [PMAX_PATTERN]]]
    defaults: 2000 1000 20000

Written for the review from the definitions; no recovered DZT script and no LIT script is run or
imported. Requires python-flint (exact integer resultants), mpmath and numpy.

Objects (p = 4s, L = zeta_p, I = L^s, both field elements of K = Q(zeta_p)):
    Q_p = L^5 A_s / (2 (L+1)^4 (L^2+L+1)),  A_s = L^(s+2) + L^s - L^2 + 1   (Dyadic closed form, imported)
    M_p = Q_p / (I L^3),   N_full = N_{K/Q}(Q_p) = N_{K/Q}(M_p),   N_+ = N_{K+/Q}(M_p).
For an integer polynomial f, N_{K/Q}(f(L)) = Res(Phi_p, f) (Phi_p monic, f evaluated at the roots).

Part A (exact, 12 <= p <= PMAX_EXACT, and p = 8):
  A1  Res(Phi_p, A_s) = Res(Phi_p, x^s - 1) * Res(Phi_p, x^2 - x^s)       factorization A_s = (I-1)(L^2-I)
  A2  N(I-1) = 2^(phi/2)                                                   (row 5: not a unit)
  A3  N(L^2-I) = D(p) (LIT §3) = order formula of the odd-support note
  A4  N(L+1) = Phi_p(-1) = B(p): 2 iff p = 2^k, else 1                       (row 4)
  A5  N(L^2+L+1) = C(p): 4 iff p = 3*2^k, else 1
  A6  N_full = 2^(-phi/2) D / (B^4 C)  (LIT Proposition), and N_full is the square of a rational
  A7  odd part of the numerator of |N_+| = l^2 iff p = 8 l^a, l^a = 1 mod 4, else 1   (v0.17 ODD-SUPPORT)
  A8  denominator of |N_+| = 2^(d_p), d_p = phi/4 + [p=2^k] + [p=3*2^k]              (v0.17 DENOMINATOR)
  A9  |N_+| equals the recovered CSV (read as data) for 12 <= p <= 1000, and the 14 values of DZT §6.3
  A10 p = 8: Res(Phi_8, A_2) = 0
Part B (sign, 12 <= p <= PMAX_SIGN): N_+ as the product of sigma_a(M_p) over 0 < a < p/2, gcd(a,p)=1,
  each computed from the complex closed form (mpmath, 50 digits); its modulus against Part A; its sign
  against the LIT count (-1)^(c1+c2); and the LIT real form of every conjugate against the closed form.
Part C (pattern, 12 <= p <= PMAX_PATTERN): the LIT §5 classification of the negative points against
  the count. A finite check; not a proof.
Exit 0 iff every check passes.
"""
import sys
from fractions import Fraction
from math import gcd, isqrt
from flint import fmpz_poly
from mpmath import mp, mpf, mpc, exp, pi, cos, sin, sqrt as msqrt, fabs
import numpy as np

PA = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
PB = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
PC = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
CSV = "upload/dzt-recovery-20261116/received/originals/downloads/dzt_casev_norm_closed_form_p8_1000.csv"
TABLE = dict(zip((12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64),
                 map(Fraction, "1/4 1/8 1/4 1/8 1/8 1/32 1/8 25/16 1/32 1/32 1/64 1/64 1/16 1/512".split())))
x = fmpz_poly([0, 1])
fails = []


def check(cond, what):
    if not cond:
        fails.append(what)


def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def phi(n):
    r = n
    for q in factor(n):
        r = r // q * (q - 1)
    return r


def prime_power(n):                      # (l, a) if n = l^a with a >= 1, else None
    f = factor(n)
    return next(iter(f.items())) if len(f) == 1 else None


def is_2k(p):
    return p & (p - 1) == 0


def is_3_2k(p):
    return p % 3 == 0 and is_2k(p // 3)


def anomaly(p):                          # (l, a) if p = 8 l^a, l odd prime, l^a = 1 mod 4
    if p % 8 or (p // 8) % 2 == 0:
        return None
    q = p // 8
    pp = prime_power(q) if q > 1 else None
    return pp if pp and q % 4 == 1 else None


def D_lit(p):                            # LIT §3, case analysis on s
    s = p // 4
    if s % 2:
        return 1
    if s % 4 == 0:
        return 4 if is_2k(s) else 1
    q = s // 2
    if q % 4 == 3:
        return 1
    pp = prime_power(q)
    return pp[0] ** 4 if pp else 1


def D_order(p):                          # odd-support note: N(1 - L^(s-2)) = Phi_n(1)^(phi(p)/phi(n))
    s = p // 4
    n = p // gcd(p, s - 2)
    pp = prime_power(n)
    return pp[0] ** (phi(p) // phi(n)) if pp else 1


def sqrt_frac(fr):
    a, b = fr.numerator, fr.denominator
    ra, rb = isqrt(a), isqrt(b)
    return Fraction(ra, rb) if ra * ra == a and rb * rb == b else None


# ---------------- Part A ----------------
absN = {}
P8 = fmpz_poly.cyclotomic(8)
check(P8.resultant(x**4 + x**2 - x**2 + 1) == 0, "A10 p=8: Res(Phi_8, A_2) != 0")  # A_2 = x^4 + 1 = Phi_8
nA = 0
for p in range(12, PA + 1, 4):
    s, ph = p // 4, phi(p)
    P = fmpz_poly.cyclotomic(p)
    RA = int(P.resultant(x**(s + 2) + x**s - x**2 + 1))
    RI = int(P.resultant(x**s - 1))
    RD = int(P.resultant(x**2 - x**s))
    RB = int(P.resultant(x + 1))
    RC = int(P.resultant(x**2 + x + 1))
    R5 = int(P.resultant(x**5))
    B = 2 if is_2k(p) else 1
    C = 4 if is_3_2k(p) else 1
    check(RA == RI * RD, "A1 p=%d" % p)
    check(RI == 2 ** (ph // 2), "A2 p=%d" % p)
    check(RD == D_lit(p) == D_order(p), "A3 p=%d: %d %d %d" % (p, RD, D_lit(p), D_order(p)))
    check(RB == int(P(-1)) == B, "A4 p=%d" % p)
    check(RC == C, "A5 p=%d" % p)
    check(R5 == 1, "A6 N(L^5) p=%d" % p)
    Nf = Fraction(R5 * RA, 2 ** ph * RB ** 4 * RC)
    check(Nf == Fraction(D_lit(p), 2 ** (ph // 2) * B ** 4 * C), "A6 LIT Proposition p=%d" % p)
    r = sqrt_frac(Nf)
    check(r is not None, "A6 not a square p=%d" % p)
    if r is None:
        continue
    absN[p] = r
    odd = r.numerator
    while odd % 2 == 0:
        odd //= 2
    an = anomaly(p)
    check(odd == (an[0] ** 2 if an else 1), "A7 p=%d odd=%d" % (p, odd))
    dp = ph // 4 + is_2k(p) + is_3_2k(p)
    check(r.denominator == 2 ** dp and r.numerator % 2 == 1, "A8 p=%d" % p)
    nA += 1
rows = [l.rstrip("\n").split(",") for l in open(CSV, encoding="utf-8")][1:]
csv_vals = {int(r[0]): Fraction(r[4]) for r in rows}
nC = 0
for p, v in csv_vals.items():
    if p >= 12 and p <= PA:
        check(absN.get(p) == v, "A9 CSV p=%d" % p)
        nC += 1
for p, v in TABLE.items():
    check(absN.get(p) == v, "A9 table p=%d" % p)
anomalies = [p for p in range(12, PA + 1, 4) if anomaly(p)]
print("Part A  exact, p = 12..%d step 4: %d points; A1-A8 on every point; p = 8 vanishes" % (PA, nA))
print("        CSV rows compared (p = 12..1000): %d; DZT §6.3 table: %d values" % (nC, len(TABLE)))
print("        anomaly points (p <= %d): %d; first ones %s; p <= 1000: %d" %
      (PA, len(anomalies), anomalies[:6], sum(1 for p in anomalies if p <= 1000)))

# ---------------- Part B ----------------
mp.dps = 50


def Qc(L, I):
    return L**5 * (I * L**2 + I - L**2 + 1) / (2 * (L + 1)**4 * (L**2 + L + 1))


def count_sign(p):
    c1 = c2 = 0
    for a in range(1, (p + 1) // 2):
        if 2 * a < p and gcd(a, p) == 1:
            if 3 * a > p:
                c1 += 1
            if (a % 4 == 1 and 8 * a > p) or (a % 4 == 3 and 8 * a > 3 * p):
                c2 += 1
    return -1 if (c1 + c2) % 2 else 1


signs, max_rel, max_form, max_im = {}, mpf(0), mpf(0), mpf(0)
for p in range(12, PB + 1, 4):
    s = p // 4
    prod = mpc(1)
    for a in range(1, p // 2):
        if gcd(a, p) == 1:
            th = 2 * pi * a / p
            L = exp(1j * th)
            I = L**s
            m = Qc(L, I) / (I * L**3)
            eps = 1 if a % 4 == 1 else -1
            form = (cos(th) - eps * sin(th)) / (16 * cos(th / 2)**4 * (1 + 2 * cos(th)))
            max_form = max(max_form, fabs(m - form) / fabs(form))
            max_im = max(max_im, fabs(m.imag) / fabs(m))
            prod *= m
    exact = absN[p]
    rel = fabs(fabs(prod.real) - mpf(exact.numerator) / exact.denominator) / (mpf(exact.numerator) / exact.denominator)
    max_rel = max(max_rel, rel)
    sg = 1 if prod.real > 0 else -1
    signs[p] = sg
    check(rel < mpf(10) ** -30, "B modulus p=%d" % p)
    check(sg == count_sign(p), "B sign count p=%d" % p)
check(max_form < mpf(10) ** -30, "B real form")
neg14 = [p for p in sorted(TABLE) if signs[p] < 0]
print("Part B  sign, p = 12..%d: %d points; |prod| vs exact max rel err %s; real form vs closed form max rel err %s;"
      % (PB, len(signs), mp.nstr(max_rel, 3), mp.nstr(max_form, 3)))
print("        max |Im sigma_a(M)|/|sigma_a(M)| %s; sign = (-1)^(c1+c2) at every point; negative points <= %d: %d"
      % (mp.nstr(max_im, 3), PB, sum(1 for v in signs.values() if v < 0)))
print("        negative points of the 14-point table: %s" % neg14)


# ---------------- Part C ----------------
def lit_rule_negative(p):
    if is_2k(p) and p >= 16:
        return True
    if is_3_2k(p) and p >= 24:
        return True
    if p % 4 == 0 and p != 12:
        q = p // 4
        pp = prime_power(q) if q > 1 and q % 2 else None
        if pp and pp[0] % 8 in (3, 5):
            return True
    return False


def count_sign_np(p):
    a = np.arange(1, (p + 1) // 2, dtype=np.int64)
    a = a[(2 * a < p) & (np.gcd(a, p) == 1)]
    c1 = np.count_nonzero(3 * a > p)
    c2 = np.count_nonzero(((a % 4 == 1) & (8 * a > p)) | ((a % 4 == 3) & (8 * a > 3 * p)))
    return -1 if (c1 + c2) % 2 else 1


nneg, bad = 0, []
for p in range(12, PC + 1, 4):
    sg = count_sign_np(p)
    if p <= PB:
        check(sg == signs[p], "C numpy count vs B p=%d" % p)
    nneg += sg < 0
    if (sg < 0) != lit_rule_negative(p):
        bad.append(p)
check(not bad, "C pattern exceptions %s" % bad[:10])
print("Part C  pattern, p = 12..%d: %d points; negative %d; exceptions to the LIT §5 rule: %d"
      % (PC, len(range(12, PC + 1, 4)), nneg, len(bad)))

print("FAILURES: %d %s" % (len(fails), fails[:10]))
print("RESULT:", "PASS" if not fails else "FAIL")
sys.exit(0 if not fails else 1)
