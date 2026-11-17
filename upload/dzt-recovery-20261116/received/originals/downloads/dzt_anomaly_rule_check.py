#!/usr/bin/env python3
"""
dzt_anomaly_rule_check.py — DZT-side audit/correction of the closed-form norm pattern.

Verifies the CORRECTED odd-prime anomaly rule for N_+(M_p) against the closed-form
audit CSV (dzt_casev_norm_closed_form_p8_1000.csv):

  CORRECTED RULE (verified, finite horizon p<=1000, 249 points, 0 mismatches):
    odd prime in N_+(M_p)  <=>  p = 8*q with q = ell^a a PRIME POWER and q ≡ 1 (mod 4)
    when anomalous, the numerator of N_+ is exactly ell^2.

  This SUPERSEDES the imported note's "every odd prime power q" pattern, which is
  FALSE: q ≡ 3 (mod 4) prime powers (q=3,7,11,19,23,27,...) give pure 2-powers.
  Counterexamples to the note: p=24,56,88,152,184,216.

  The denominator (power of 2) has NO simple closed form (it is NOT 2^{-phi(q)});
  no denominator law is asserted.

Exit 0 iff the corrected rule matches every CSV row.
"""
import csv, ast, sys, sympy as sp

def predict_anomaly(p):
    if p % 8 != 0: return False
    q = p // 8
    if q < 2: return False
    f = sp.factorint(q)
    return (len(f) == 1) and (q % 4 == 1)   # prime power AND ≡1 mod 4

def main(path):
    rows = list(csv.DictReader(open(path)))
    mism, num_bad, anoms = [], [], []
    for r in rows:
        p = int(r['p']); actual = r['anomaly'].strip().lower() == 'true'
        if actual: anoms.append(p)
        if predict_anomaly(p) != actual:
            mism.append((p, predict_anomaly(p), actual))
        if actual:
            ell = next(iter(sp.factorint(p//8)))
            if ast.literal_eval(r['numerator_factor']) != {ell: 2}:
                num_bad.append(p)
    print(f"rows audited        : {len(rows)}")
    print(f"anomalies           : {len(anoms)} -> {anoms}")
    print(f"rule mismatches     : {len(mism)} {mism if mism else ''}")
    print(f"numerator != ell^2  : {len(num_bad)} {num_bad if num_bad else ''}")
    ok = (not mism) and (not num_bad)
    print("RESULT:", "corrected rule holds on full horizon" if ok else "RULE FAILED")
    return 0 if ok else 1

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "dzt_casev_norm_closed_form_p8_1000.csv"
    raise SystemExit(main(path))
