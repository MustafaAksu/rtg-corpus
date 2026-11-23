#!/usr/bin/env python3
"""
rtg_b5_Seff_limit_cert.py
=========================
Executable exact certificate for  lim_{lam->1} S_eff/S = 3.

S      = S_05^{(beta=1)}, the secular source coefficient of channel (0,5)
         (five-term, proportional to c_02^2).
S_eff  = S - c_{(-2,1)} / (1 - lam^{-3}),  the effective coefficient appearing in
         the p>=13 identity  F_raw^p(0,5) = p lam^{p-1} S_eff.

This script:
  1. builds the (0,5) source via the beta-graded engine (exact, symbolic c_ab),
  2. extracts S = mode (1,0) and c_{(-2,1)} = mode (-2,1),
  3. substitutes the EXACT dyadic one-step coefficients c_ab(lam),
  4. forms S_eff/S as a rational function of lam,
  5. computes lim_{lam->1} symbolically and asserts it equals 3.

Exit 0 iff the exact limit is 3.
"""
import sys
import sympy as sp

lam = sp.symbols('lam')
cs, cbar = {}, {}
MAXC = 6
for a in range(MAXC+1):
    for b in range(MAXC+1):
        if 2 <= a+b <= MAXC:
            cs[(a,b)]=sp.symbols(f'c_{a}_{b}'); cbar[(a,b)]=sp.symbols(f'cb_{a}_{b}')

def bp_add(P,Q):
    R=dict(P)
    for k,c in Q.items(): R[k]=R.get(k,0)+c
    return {k:sp.expand(c) for k,c in R.items() if sp.expand(c)!=0}
def bp_scal(P,s): return {k:sp.expand(c*s) for k,c in P.items() if sp.expand(c*s)!=0}
def bp_mul(P,Q):
    R={}
    for (b1,m1),c1 in P.items():
        for (b2,m2),c2 in Q.items(): R[(b1+b2,m1+m2)]=R.get((b1+b2,m1+m2),0)+c1*c2
    return {k:sp.expand(c) for k,c in R.items() if sp.expand(c)!=0}
def bp_conj(P):
    out={}; subs={}
    for k in cs: subs[cs[k]]=cbar[k]; subs[cbar[k]]=cs[k]
    for (b,m),c in P.items(): out[(-b,m)]=out.get((-b,m),0)+c.subs(lam,1/lam).subs(subs,simultaneous=True)
    return {k:sp.expand(c) for k,c in out.items() if sp.expand(c)!=0}
def jet_conj(J):
    out={}
    for (a,b),P in J.items(): out[(b,a)]=bp_add(out.get((b,a),{}),bp_conj(P))
    return out
def jet_mul(J1,J2,md):
    out={}
    for (a1,b1),P1 in J1.items():
        for (a2,b2),P2 in J2.items():
            if a1+a2+b1+b2<=md: out[(a1+a2,b1+b2)]=bp_add(out.get((a1+a2,b1+b2),{}),bp_mul(P1,P2))
    return out
def jet_pow(J,e,md):
    R={(0,0):{(0,0):sp.Integer(1)}}
    for _ in range(e): R=jet_mul(R,J,md)
    return R
def F_apply(J,md):
    Jc=jet_conj(J); out={}
    for (a,b),P in J.items():
        if a+b<=md: out[(a,b)]=bp_add(out.get((a,b),{}),bp_scal(P,lam))
    for (a,b) in cs:
        if a+b>md: continue
        T=jet_mul(jet_pow(J,a,md),jet_pow(Jc,b,md),md)
        for key,P in T.items():
            if key[0]+key[1]<=md: out[key]=bp_add(out.get(key,{}),bp_scal(P,cs[(a,b)]))
    return out
def solve_channel(src):
    out={}
    for (b,m),c in src.items():
        if m==0 and b!=1:
            k=c*lam**(-1)/(lam**(b-1)-1)
            out[(b,0)]=out.get((b,0),0)+k; out[(1,0)]=out.get((1,0),0)-k
        elif m==0 and b==1: out[(1,1)]=out.get((1,1),0)+c*lam**(-1)
        else: out[(b,m)]=out.get((b,m),0)+c
    return {k:sp.expand(v) for k,v in out.items() if sp.expand(v)!=0}

# build (0,5) source
J={(1,0):{(1,0):sp.Integer(1)}}
for deg in range(2,5):
    FJ=F_apply(J,deg)
    for (a,b) in [(a,b) for a in range(deg+1) for b in range(deg+1) if a+b==deg]:
        J[(a,b)]=solve_channel(FJ.get((a,b),{}))
src05=F_apply(J,5).get((0,5),{})
S   = sp.expand(src05.get((1,0),0))
C21 = sp.expand(src05.get((-2,1),0))
S_eff = sp.expand(S - C21/(1-lam**(-3)))

# exact dyadic one-step coefficients c_ab(lam)
Z,Zb=sp.symbols('Z Zb')
u=1/(1-lam); ub=1/(1-1/lam); D=u-ub; K=2-(lam+1/lam)
rho=u*Z+ub*Zb; eta=Z+Zb
exp_rho=sum(rho**k/sp.factorial(k) for k in range(1,6))
sin_eta=eta-eta**3/6+eta**5/120
raw=sp.expand((rho-sin_eta-ub*(eta+K*exp_rho-K*sin_eta))/D)
cmap={}
for a in range(7):
    for b in range(7):
        if 2<=a+b<=6: cmap[(a,b)]=sp.simplify(raw.coeff(Z,a).coeff(Zb,b))

subs={}
for k in cs:
    if k in cmap: subs[cs[k]]=cmap[k]
for k in cbar:
    if k in cmap: subs[cbar[k]]=cmap[k].subs(lam,1/lam)

ratio = sp.together(S_eff.subs(subs)) / sp.together(S.subs(subs))
L = sp.simplify(sp.limit(ratio, lam, 1))
print("lim_{lam->1} S_eff/S =", L)
if sp.simplify(L-3)==0:
    print("CERTIFICATE PASSED: exact limit = 3  [ALG]")
    sys.exit(0)
else:
    print("CERTIFICATE FAILED"); sys.exit(1)
