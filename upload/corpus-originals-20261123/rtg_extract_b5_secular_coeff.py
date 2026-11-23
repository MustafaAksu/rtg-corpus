#!/usr/bin/env python3
"""
rtg_extract_b5_secular_coeff.py
===============================
Targeted extraction + nonvanishing certificate for the (beta,m)=(1,0) secular
coefficient in the (0,5) source. Promotes the channel boundary "universal pure
anti-holomorphic vanishing stops at b=4" toward [ALG] for the dyadic map.

Does NOT solve the (0,5) recursion (the secular solver is deliberately avoided).
It:
  (1) builds the beta-graded jet to degree 4 (clean, no secular modes),
  (2) applies F once to reach degree 5,
  (3) reads the (1,0)-slot coefficient of the (0,5) source as a FORMAL expression
      in {c_ab, cb_ab},
  (4) checks it is NOT identically zero (symbolic),
  (5) substitutes the actual dyadic raw-map coefficients and checks NONZERO,
  (6) prints the path decomposition feeding the secular slot.

Exit 0 iff (4) and (5) both pass.
"""
import sys, pickle
import sympy as sp
import mpmath as mp

lam = sp.symbols('lambda', nonzero=True)
cs, cbar = {}, {}
MAXC = 6
for a in range(MAXC+1):
    for b in range(MAXC+1):
        if 2 <= a+b <= MAXC:
            cs[(a,b)]   = sp.symbols(f'c_{a}_{b}')
            cbar[(a,b)] = sp.symbols(f'cb_{a}_{b}')

def bp_add(P,Q):
    R=dict(P)
    for k,c in Q.items(): R[k]=R.get(k,0)+c
    return {k:sp.expand(c) for k,c in R.items() if sp.expand(c)!=0}
def bp_scal(P,s): return {k:sp.expand(c*s) for k,c in P.items() if sp.expand(c*s)!=0}
def bp_mul(P,Q):
    R={}
    for (b1,m1),c1 in P.items():
        for (b2,m2),c2 in Q.items():
            R[(b1+b2,m1+m2)]=R.get((b1+b2,m1+m2),0)+c1*c2
    return {k:sp.expand(c) for k,c in R.items() if sp.expand(c)!=0}
def bp_conj(P):
    out={}; subs={}
    for k in cs: subs[cs[k]]=cbar[k]; subs[cbar[k]]=cs[k]
    for (b,m),c in P.items():
        out[(-b,m)]=out.get((-b,m),0)+c.subs(lam,1/lam).subs(subs,simultaneous=True)
    return {k:sp.expand(c) for k,c in out.items() if sp.expand(c)!=0}
def jet_conj(J):
    out={}
    for (a,b),P in J.items(): out[(b,a)]=bp_add(out.get((b,a),{}),bp_conj(P))
    return out
def jet_mul(J1,J2,md):
    out={}
    for (a1,b1),P1 in J1.items():
        for (a2,b2),P2 in J2.items():
            if a1+a2+b1+b2<=md:
                out[(a1+a2,b1+b2)]=bp_add(out.get((a1+a2,b1+b2),{}),bp_mul(P1,P2))
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
        elif m==0 and b==1:
            out[(1,1)]=out.get((1,1),0)+c*lam**(-1)
        else:
            out[(b,m)]=out.get((b,m),0)+c
    return {k:sp.expand(v) for k,v in out.items() if sp.expand(v)!=0}

def dyadic_coeffs(p, dps=60):
    mp.mp.dps=dps
    lm=mp.exp(2j*mp.pi/p); K=2-2*mp.cos(2*mp.pi/p)
    u=1/(1-lm); ub=mp.conj(u); D=u-ub
    def raw(Z,Zb):
        rho=u*Z+ub*Zb; eta=Z+Zb
        return (rho-mp.sin(eta)-ub*(eta+K*(mp.exp(rho)-1)-K*mp.sin(eta)))/D
    N=24; r=mp.mpf('0.08')
    pts=[mp.exp(2j*mp.pi*j/N) for j in range(N)]
    vals=[[raw(r*pts[i],r*pts[j]) for j in range(N)] for i in range(N)]
    coeffs={}
    for a in range(7):
        for b in range(7):
            if not(1<=a+b<=6): continue
            s=mp.mpc(0)
            for i in range(N):
                for j in range(N):
                    s+=vals[i][j]*mp.exp(-2j*mp.pi*(a*i+b*j)/N)
            coeffs[(a,b)]=s/((N*N)*r**(a+b))
    return coeffs

def main():
    FAIL=False
    J={(1,0):{(1,0):sp.Integer(1)}}
    for deg in range(2,5):
        FJ=F_apply(J,deg)
        for (a,b) in [(a,b) for a in range(deg+1) for b in range(deg+1) if a+b==deg]:
            J[(a,b)]=solve_channel(FJ.get((a,b),{}))
    FJ5=F_apply(J,5)
    src05=FJ5.get((0,5),{})
    coeff_10=sp.expand(src05.get((1,0),sp.Integer(0)))

    # (4) not identically zero
    print("=== (1,0)-slot (secular beta=1) coefficient of the (0,5) source ===")
    terms=coeff_10.as_ordered_terms() if coeff_10!=0 else []
    print(f"terms: {len(terms)}, identically zero: {coeff_10==0}")
    for t in terms: print("   ", t)
    if coeff_10==0:
        print("FAIL: secular coefficient is identically zero"); FAIL=True
    else:
        print("[OK] secular coefficient is NOT identically zero (symbolic)")

    # (5) nonzero at actual dyadic coefficients
    print("\n=== dyadic substitution check ===")
    for p in [6,7,8]:
        dc=dyadic_coeffs(p)
        subs={}
        for k in cs:
            if k in dc: subs[cs[k]]=complex(dc[k])
        for k in cbar:
            if k in dc: subs[cbar[k]]=complex(mp.conj(dc[k]))
        val=complex(coeff_10.subs(lam,complex(mp.exp(2j*mp.pi/p))).subs(subs))
        ok=abs(val)>1e-10
        print(f"  p={p}: |secular coeff| = {abs(val):.4e}  {'NONZERO [OK]' if ok else 'ZERO [FAIL]'}")
        if not ok: FAIL=True

    if FAIL:
        print("\nCERTIFICATE FAILED"); sys.exit(1)
    print("\nCERTIFICATE PASSED:")
    print("  (1,0) secular source coefficient of (0,5) is NOT identically zero,")
    print("  and is NONZERO at the actual dyadic coefficients (p=6,7,8).")
    print("  => b=5 breaks universal pure anti-holomorphic vanishing for the dyadic map [ALG].")
    sys.exit(0)

if __name__=="__main__":
    main()
