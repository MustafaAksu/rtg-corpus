#!/usr/bin/env python3
"""
dzt_channel_universality_check.py — DZT verification for DZT-OPEN-CHANNEL-UNIV (DYAD-RESP-DZT-002).

Tests whether the q=4,(0,3) phase x real-subfield factorization is channel-universal.
Uses qb_extract.qb_cyclo (Dyadic-owned general (q,b) extractor).

Two checks:
 (A) Admissibility gate: source (0,b) is an extra-charge slot at order q iff q | (b+1).
 (B) Factorization test (CORRECT form): Q_p = (root of unity) * (real-subfield element)
     iff sigma_{-1}(Q_p)/Q_p reduces to a MONOMIAL +/- z^j mod Phi_p.
     NOTE: the modulus-only test (all conjugates on unit circle) is VACUOUS here, since
     Q has rational coefficients so |sigma_{-1}(Q)/Q| = 1 at every embedding automatically;
     Kronecker needs the algebraic-integer condition, which the ratio fails. Hence the
     exact monomial test is the right one.

Result (finite horizon): factorization holds for q=4,(0,3) (monomial ratio), FAILS for the
admissible substitutes q=3,(0,5) and q=4,(0,7) (multi-term ratio) -> channel-specific.
"""
import sys, sympy as sp
from qb_extract import qb_cyclo
z = sp.symbols('z')

def admissible(q, b):
    return (b + 1) % q == 0

def factorizes(p, q, b):
    val,_,_ = qb_cyclo(p, q, b)
    Phi = sp.Poly(sp.cyclotomic_poly(p, z), z)
    red = lambda e: sp.rem(sp.Poly(sp.expand(e), z), Phi).as_expr()
    if sp.expand(val) == 0:
        return None  # zero / degenerate
    sig = red(val.subs(z, z**(p - 1)))
    ratio = red(sig * red(sp.invert(val, Phi.as_expr(), z)))
    terms = sp.Poly(ratio, z).terms()
    is_monomial = (len(terms) == 1 and abs(terms[0][1]) == 1)
    return is_monomial, len(terms)

if __name__ == "__main__":
    print("ADMISSIBILITY GATE  q|(b+1):")
    for q,b in [(4,3),(3,3),(6,3),(4,5),(3,5),(6,5),(4,7),(3,2)]:
        print(f"  q={q},(0,{b}): {'admissible' if admissible(q,b) else 'INADMISSIBLE'}")
    print("\nFACTORIZATION (monomial-ratio) TEST:")
    plan = [(4,3,[12,16,20],"control: should PASS"),
            (3,5,[12,15,18],"diff-q substitute"),
            (4,7,[12,16],"diff-degree substitute")]
    allctrl_pass = True; anysub_pass = False
    for q,b,ps,lab in plan:
        for p in ps:
            r = factorizes(p,q,b)
            if r is None:
                print(f"  q={q},(0,{b}) p={p}: zero/degenerate")
                continue
            tag = "factorizes" if r[0] else "FAILS"
            print(f"  q={q},(0,{b}) p={p}: {tag} (ratio {r[1]} term(s))   [{lab}]")
            if q==4 and b==3: allctrl_pass &= r[0]
            else: anysub_pass |= r[0]
    print("\nCONCLUSION:", "channel-SPECIFIC (control factorizes, substitutes fail)"
          if (allctrl_pass and not anysub_pass) else "unexpected")
    sys.exit(0)
