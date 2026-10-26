#!/usr/bin/env python3
# N-5 DISCRIMINATION — IDENTITY CERTIFICATE  v5
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
# v4 -> v5: [COR] every PASS line is now LITERAL — each states only what its
#   expression decides. v4's rows still carried interpretation (hyperbolicity,
#   persistence, eventual periodicity, positivity, the iff reading) inside
#   strings whose expressions checked only coefficients and identities. Rows
#   are renamed *-ID to mark them as identity rows; all interpretation moved
#   to the companion memo.
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
ck("T1a-ID: the L-coefficient of q(m_A L + c_A) - p(m_B L + c_B) equals "
   "(m_A q - m_B p).",
   sp.simplify(sp.diff(D1,L)-(mA*q-mB*p))==0)
ck("T1b-ID: substituting (p,q)=(m_A,m_B) yields exactly c_A m_B - c_B m_A "
   "(the L terms cancel identically).", 
   sp.simplify(sp.expand(D1.subs({p:mA,q:mB}))-(cA*mB-cB*mA))==0)

# ---- T2 periodicity triviality (unchanged) ---------------------------------
ck("T2-ID: b(a m + r_A) - a(b m + r_B) equals b r_A - a r_B identically "
   "(the m terms cancel).",
   sp.simplify(sp.expand(b*(a*m+rA)-a*(b*m+rB))-(b*rA-a*rB))==0)

# ---- T3 CORRECTED: eventual-cycle classification ---------------------------
D3 = sp.expand(q*(a*m+rA)-p*(b*m+rB))
ck("T3-ID: the m-coefficient of q(a m + r_A) - p(b m + r_B) equals (a q - b p).",
   sp.simplify(sp.diff(D3,m)-(a*q-b*p))==0)
ck("T3-COR-ID: that coefficient is nonzero at a worked instance "
   "(p,q,a,b)=(5,1,6,1), where it equals 1.",
   sp.simplify(sp.diff(D3,m).subs({p:5,q:1,a:6,b:1}))==1)

D4 = sp.expand(b*(ap*m+rA)-a*(bp*m+rB))
ck("T4-ID: the m-coefficient of b(a' m + r_A) - a(b' m + r_B) equals "
   "(a' b - a b').",
   sp.simplify(sp.diff(D4,m)-(ap*b-a*bp))==0)
ck("T4-ex-ID: with (a,b)=(6,1), Delta_(6:1) has m-coefficient 0; with "
   "(a,b)=(5,1) it equals -1.",
   sp.expand(1*(6*m)-6*(1*m))==0 and sp.expand(1*(5*m)-6*(1*m))==-m)

Om=sp.Rational(1,2)
f=lambda z: z+Om+(K/(2*sp.pi))*sp.sin(2*sp.pi*z)
fp=lambda z: sp.simplify(sp.diff(f(x),x).subs(x,z))
mult=sp.simplify(fp(0)*fp(sp.Rational(1,2)))
ck("P1a-ID: at Omega=1/2 the lift satisfies f(0)=1/2 and f(1/2)=1, and "
   "f'(0)*f'(1/2) equals 1 - K^2.",
   sp.simplify(f(0)-sp.Rational(1,2))==0 and sp.simplify(f(sp.Rational(1,2))-1)==0
   and sp.simplify(mult-(1-K**2))==0)

print("-"*70)
if FAIL:
    print("FAILURES:",FAIL); sys.exit(1)
print("RESULT: ALL IDENTITY ROWS PASS. Every row above states only what its "
      "expression decides. NOT asserted by this exit code: eventual "
      "periodicity; positivity/uniqueness of the reduced class; the "
      "biconditional readings of T1/T3; hyperbolicity and hyperbolic "
      "persistence in P1a; the monotone-lift ray-crossing theorem; sector "
      "closure; the same-realization quantifier; and the DISC-1D design "
      "constraint D1. All of these are argued in the companion memo.")
sys.exit(0)
