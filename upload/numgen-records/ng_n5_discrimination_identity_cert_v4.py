#!/usr/bin/env python3
# N-5 DISCRIMINATION — IDENTITY CERTIFICATE  v4
# Base: RTG_NUMBER_GENESIS_DSN_v1.15 (sha256 d56440c6...3375, verified)
#
# SCOPE OF THIS ARTIFACT (corrected description, per review):
#   This is an IDENTITY CERTIFICATE SUPPORTING MEMO PROOFS. Its exit code
#   certifies the algebraic identities below and nothing else. Eventual
#   periodicity, the monotone-lift ray-crossing theorem, and the finite-sector
#   scope assumptions are mathematical premises argued in the memo, NOT
#   established by this script. Earlier versions described their exit code too
#   broadly; that is corrected here.
#
# v3 -> v4: [COR] v3 placed D1 (a design constraint about experimental
#   structure) inside the exit-code certificate, where its actual test only
#   verified that the polynomial b a' - a b' is not identically zero. The PASS
#   line asserted far more: a same-realization quantifier, a need for two
#   distinct deformation points, admissibility of three k values, and dual
#   activity at them. None of that is checkable here. This repeated, in milder
#   form, the A3/A6 category error. D1 is REMOVED from this certificate and
#   lives in the memo as: T3 + T4 + same-realization definition => D1.
#
# v2 -> v3: [COR] T3 of v2 was WRONG. It claimed unbounded defect is impossible
#   in a finite-state branch. False, and it contradicted this file's own T2:
#   for an eventual cycle with per-cycle counts (a,b), Delta_{p:q} has
#   m-coefficient (qa - pb), so EVERY class other than a:b diverges linearly.
#   Corrected statement below. Consequences reversed: DISC-1B remains
#   falsifiable, and the C6-style bounded/unbounded contrast IS available in a
#   finite invariant sector.
import sys
import sympy as sp
FAIL=[]
def ck(n,c):
    print(f"[{'PASS' if c else 'FAIL'}] {n}")
    if not c: FAIL.append(n)

L,mA,mB,cA,cB,p,q = sp.symbols('L m_A m_B c_A c_B p q')
m,a,b,rA,rB,ap,bp,K,x = sp.symbols('m a b r_A r_B a_prime b_prime K x')

# ---- T1 (unchanged from v2, premise explicit) ------------------------------
D1 = sp.expand(q*(mA*L+cA) - p*(mB*L+cB))
ck("T1a [premise: L prefix-cofinally unbounded] L-coefficient of q N_A - p N_B "
   "is (m_A q - m_B p); with L unbounded, bounded defect IFF q m_A = p m_B",
   sp.simplify(sp.diff(D1,L)-(mA*q-mB*p))==0)
ck("T1b [no extra premise] at (p,q)=(m_A,m_B) the parent count cancels, "
   "leaving m_B c_A - m_A c_B", 
   sp.simplify(sp.expand(D1.subs({p:mA,q:mB}))-(cA*mB-cB*mA))==0)

# ---- T2 periodicity triviality (unchanged) ---------------------------------
ck("T2 periodicity: b N_A - a N_B = b r_A - a r_B for a period with (a,b) "
   "counts; the period count cancels, so a dual-active periodic pair is "
   "bounded AT ITS OWN CLASS a:b",
   sp.simplify(sp.expand(b*(a*m+rA)-a*(b*m+rB))-(b*rA-a*rB))==0)

# ---- T3 CORRECTED: eventual-cycle classification ---------------------------
D3 = sp.expand(q*(a*m+rA)-p*(b*m+rB))
ck("T3 CORRECTED — finite-state eventual-cycle classification. For a "
   "deterministic map on a CLOSED FINITE INVARIANT SECTOR with predicates "
   "determined by finite state/transition data, every orbit is eventually "
   "periodic. If the eventual cycle is dual-active with per-cycle counts "
   "a,b>0 it realizes EXACTLY ONE reduced bounded class a:b; for every other "
   "p:q the defect grows linearly as (qa-pb)m+O(1). If a=0 or b=0 that cycle "
   "supplies no positive dual-active bounded class.",
   sp.simplify(sp.diff(D3,m)-(a*q-b*p))==0)
ck("T3-COR the v2 claim 'unbounded defect impossible in finite state' is "
   "FALSIFIED by the same identity: the m-coefficient (qa-pb) is nonzero for "
   "every p:q != a:b",
   sp.simplify(sp.diff(D3,m).subs({p:5,q:1,a:6,b:1}))==1)

# ---- T4 class-change <=> loss of boundedness of the FIXED old class --------
D4 = sp.expand(b*(ap*m+rA)-a*(bp*m+rB))
ck("T4 equivalence: evaluating the OLD class a:b on a deformed cycle "
   "(a',b') gives m-coefficient (b a' - a b'), which vanishes iff "
   "a:b = a':b'. Hence class-change under deformation and LINEAR LOSS OF "
   "BOUNDEDNESS of the fixed original class are EQUIVALENT. DISC-1D-C may "
   "therefore keep the strong bounded->unbounded form.",
   sp.simplify(sp.diff(D4,m)-(ap*b-a*bp))==0)
ck("T4-ex minimal witness: cycle A^6 B gives Delta_(6:1)=O(1) while cycle "
   "A^5 B gives Delta_(6:1) = -m + O(1). Both finite and exactly periodic; "
   "the same fixed class is bounded in one and linearly unbounded in the "
   "other — a C6-style contrast inside finite state.",
   sp.expand(1*(6*m)-6*(1*m))==0 and sp.expand(1*(5*m)-6*(1*m))==-m)

# ---- P1a now fully exact, no [NUM] premise ---------------------------------
Om=sp.Rational(1,2)
f=lambda z: z+Om+(K/(2*sp.pi))*sp.sin(2*sp.pi*z)
fp=lambda z: sp.simplify(sp.diff(f(x),x).subs(x,z))
mult=sp.simplify(fp(0)*fp(sp.Rational(1,2)))
ck(f"P1a EXACT [ALG]: at Omega=1/2 the sine terms vanish exactly, so "
   f"0 -> 1/2 -> 1 is an exact period-2 lift orbit with multiplier "
   f"f'(0) f'(1/2) = {mult} = 1-K^2, hyperbolic attracting for 0<K<1. "
   f"Hyperbolic persistence then gives an OPEN parameter neighbourhood. No "
   f"numerical multiplier is needed; the Omega=0.48 value 0.634807 remains "
   f"supplementary [NUM].",
   sp.simplify(f(0)-sp.Rational(1,2))==0 and sp.simplify(f(sp.Rational(1,2))-1)==0
   and sp.simplify(mult-(1-K**2))==0)

print("-"*70)
if FAIL:
    print("FAILURES:",FAIL); sys.exit(1)
print("RESULT: ALL IDENTITIES PASS. Exit code certifies the algebraic "
      "identities T1a/T1b/T2/T3/T4/P1a ONLY. Everything else — eventual "
      "periodicity, the monotone-lift ray-crossing theorem, sector closure, "
      "the same-realization quantifier and the DISC-1D design constraint D1 "
      "— are memo-level premises and consequences, deliberately NOT asserted "
      "by this exit code.")
sys.exit(0)
