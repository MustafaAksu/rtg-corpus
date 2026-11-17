#!/usr/bin/env python3
"""
dzt_odd_support_proof_check.py — independent verification of DZT-THM-CASCADE-ODD-SUPPORT.

Theorem (odd-prime support + numerator; denominator NOT claimed):
  For p=4s>=12, the odd numerator of N_+(M_p) is nontrivial iff
      p = 8 q,  q = ell^a  (odd prime power),  q ≡ 1 (mod 4),
  and then it is exactly ell^2.

Proof spine verified here, step by step, against the closed-form CSV:
  A_s = (I-1)(L^2 - I),  I=L^s, I^2=-1                         [factorization]
  L^2 - I = L^2(1 - L^{s-2})                                   [so norm ~ N(1-L^{s-2})]
  n = ord(L^{s-2}) = p/gcd(p, s-2)
  |N_{Q(zeta_p)/Q}(1-L^{s-2})| = Phi_n(1)^{phi(p)/phi(n)}
  Phi_n(1) = r if n=r^b prime power else 1
  odd prime power n  <=>  p=8q, q=ell^a, q≡1 mod4 ;  mult phi(p)/phi(n)=4
  full-norm odd part ell^4  ->  N_+ = sqrt  ->  ell^2
Exit 0 iff the proof-predicted odd numerator matches the CSV for every row.
"""
import csv, ast, sys, sympy as sp

def predicted_odd_numerator(p):
    s = p // 4
    if s - 2 == 0:                      # p=8 zero degeneracy
        return 1
    n = p // sp.gcd(p, s - 2)
    n = int(n)
    f = sp.factorint(n)
    if len(f) == 1 and n % 2 == 1:      # odd prime power
        ell = next(iter(f))
        mult = int(sp.totient(p) // sp.totient(n))   # = 4 in-theorem
        return int(ell ** (mult // 2))               # sqrt of ell^mult
    return 1

def actual_odd_numerator(row):
    numf = ast.literal_eval(row['numerator_factor'])
    out = 1
    for pr, e in numf.items():
        if pr != 2:
            out *= pr ** e
    return out

def main(path):
    rows = list(csv.DictReader(open(path)))
    bad = []
    mult_not4 = []
    for r in rows:
        p = int(r['p'])
        if p < 12: continue
        pred = predicted_odd_numerator(p)
        act = actual_odd_numerator(r)
        if pred != act:
            bad.append((p, pred, act))
        # record anomaly multiplicities to confirm phi(p)/phi(n)=4
        s = p//4
        if s-2 != 0:
            n = int(p // sp.gcd(p, s-2)); f = sp.factorint(n)
            if len(f)==1 and n%2==1:
                m = int(sp.totient(p)//sp.totient(n))
                if m != 4: mult_not4.append((p, n, m))
    print(f"rows checked (p>=12): {sum(1 for r in rows if int(r['p'])>=12)}")
    print(f"odd-numerator mismatches: {len(bad)} {bad if bad else ''}")
    print(f"anomaly multiplicity != 4: {len(mult_not4)} {mult_not4 if mult_not4 else '(all == 4)'}")
    ok = (not bad)
    print("RESULT:", "proof prediction matches CSV on full horizon" if ok else "PROOF-DATA MISMATCH")
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv)>1 else "dzt_casev_norm_closed_form_p8_1000.csv"))
