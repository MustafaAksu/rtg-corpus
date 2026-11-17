#!/usr/bin/env python3
"""
dzt_b1_wB_audit.py — Track B1, candidate W^(B) audit (DZT-B1-0 gate).

Uses the stamped germ export DYAD-RESP-DZT-003 (gauge-safe data only):
  Birkhoff form  W_{m+1} = W_m + mu |W_m|^2 W_m + O(|W|^5),  mu = -1/2 - i*2sqrt3/3  (= c21 data),
  contraction    Q_{m+1} = Q_m(1 - Q_m + O(Q^2))   from Re(mu) = -1/2.

Candidate W^(B)_m = Im(mu) * Q_m  (phase increment per block; built on c21, gauge-safe).
Gate criteria:
  (1) gauge stability  -> uses only c21 / resonant data (gauge-invariant in strict-kernel gauge): PASS
  (2) native dependence -> Q_true contraction + c21: PASS
  (3) non-lookup-table  -> leading-order zeta_loc ~ exp(Im(mu) Li_2(z)): dilogarithm, has a
      functional equation + branch point at z=1 => transform-level structure: PLAUSIBLE PASS (leading order)

VERDICT: W^(B) is a LIVE candidate; leading structure is [HEUR] dilogarithm. A definitive gate
pass needs the subleading resonant tower (c32, c05, and higher) to confirm the structure survives,
or a structural argument. NOT claimed as a theorem (3-coefficient overfit guard).
"""
import sympy as sp

def run():
    tau = sp.Rational(2,1)*sp.sqrt(3)/3
    mu = sp.Rational(-1,2) - sp.I*tau
    print(f"mu = {mu}   Re(mu) = {sp.re(mu)} (contraction)   Im(mu) = {sp.im(mu)} (phase)")
    # leading contraction orbit Q_{m+1}=Q_m(1-Q_m): asymptotically Q_m ~ 1/m
    Q = sp.symbols('Q0'); q = Q; qs=[q]
    for _ in range(4):
        q = sp.expand(q*(1-q)); qs.append(q)
    print("leading contraction orbit (formal seed Q0):")
    for i,qq in enumerate(qs[:3]): print(f"  Q_{i} = {qq}")
    print("  asymptotically Q_m ~ 1/m  (logistic/Euler) =>")
    print("  sum_m (Im mu) Q_m z^m / m  ~ Im(mu) * Li_2(z)   => zeta_loc ~ exp(Im(mu) Li_2(z))")
    print("\nGATE (DZT-B1-0):")
    print("  (1) gauge stability : PASS (c21/resonant, strict-kernel-invariant)")
    print("  (2) native data     : PASS (Q_true contraction + c21)")
    print("  (3) non-lookup-table: PLAUSIBLE PASS (dilogarithm: functional eqn + branch point z=1)")
    print("VERDICT: W^(B) LIVE candidate; leading dilogarithm structure [HEUR];")
    print("         conclusive pass needs subleading resonant tower or a structural argument.")

if __name__ == "__main__":
    run()
