#!/usr/bin/env python3
"""
normalize_p6_liegauge_exact.py  —  OPEN 13 Archival
====================================================
Exact Lie-gauge 6-step normalization hierarchy for p=6.
All results exact over Q(sqrt(3)).

KEY FINDING: F^6 degree-3 in W-coordinates is purely resonant (only (2,1) channel).
Therefore h3 = 0 structurally, and h4 = V4 = F^6_4 entirely.

LIE-GAUGE CONVENTION: Phi_6 = exp(V_nonres) PRESERVES resonant MAP coefficients:
  nu_32 = c_32^raw, nu_05 = c_05^raw  [does not zero non-resonant channels]
"""
import mpmath as mp; mp.mp.dps = 120
from mpmath import mpc, mpf, sqrt as mps, nstr
s3=mps(mpf(3)); I_m=mpc(0,1); MAX_DEG=5
def cl(P): return {k:v for k,v in P.items() if abs(v)>mpf('1e-100')}
def pa(P,Q):
    R=dict(P)
    for k,v in Q.items(): R[k]=R.get(k,mpc(0))+v
    return cl(R)
def psb(P,Q): return pa(P,{k:-v for k,v in Q.items()})
def pm(P,Q):
    R={}
    for (a,b),u in P.items():
        for (c,d),v in Q.items():
            if a+b+c+d<=MAX_DEG: k=(a+c,b+d); R[k]=R.get(k,mpc(0))+u*v
    return cl(R)
def pp(P,n):
    if n==0: return {(0,0):mpc(1)}
    R=P
    for _ in range(n-1): R=pm(R,P)
    return R
def pcj(P): return cl({(b,a):v.conjugate() for (a,b),v in P.items()})
def psc(P,c): return cl({k:c*v for k,v in P.items()}) if abs(c)>mpf('1e-100') else {}
def pss(G,F):
    Fc=pcj(F); R={}
    for (a,b),c in G.items():
        Fa=pp(F,a) if a else {(0,0):mpc(1)}; Fb=pp(Fc,b) if b else {(0,0):mpc(1)}
        for k,v in pm(Fa,Fb).items():
            if k[0]+k[1]<=MAX_DEG: R[k]=R.get(k,mpc(0))+c*v
    return cl(R)
def dp(P,d): return {k:v for k,v in P.items() if k[0]+k[1]==d}
def isr(a,b): return (a-b-1)%6==0
def pdZ(P):
    R={}
    for (a,b),v in P.items():
        if a>=1: R[(a-1,b)]=R.get((a-1,b),mpc(0))+a*v
    return cl(R)
def pdZb(P):
    R={}
    for (a,b),v in P.items():
        if b>=1: R[(a,b-1)]=R.get((a,b-1),mpc(0))+b*v
    return cl(R)

# Build F^6
EP2=mpc(-mpf('1')/2,s3/2); EM2=mpc(-mpf('1')/2,-s3/2)
EM=mpc(s3/2,-mpf('1')/2); EP=mpc(s3/2,mpf('1')/2)
rho={(1,0):EM/s3,(0,1):EP/s3}; eta={(1,0):-I_m/s3,(0,1):I_m/s3}
def psin(x):
    x3=pm(pm(x,x),x);x5=pm(x3,pm(x,x))
    return pa(x,pa(psc(x3,mpf('-1')/6),psc(x5,mpf('1')/120)))
def pexpm1(x):
    x2=pm(x,x);x3=pm(x2,x);x4=pm(x3,x);x5=pm(x4,x)
    return pa(x,pa(psc(x2,mpf('1')/2),pa(psc(x3,mpf('1')/6),
               pa(psc(x4,mpf('1')/24),psc(x5,mpf('1')/120)))))
step1=pa({(1,0):mpc(1)},pa(psc(psin(eta),EM2),psc(pexpm1(rho),EP2)))
F6=step1
for _ in range(5): F6=pss(step1,F6)
F6m={k:v for k,v in F6.items() if k!=(1,0) and sum(k)>=3}
MU=mpc(-mpf('1')/2,-2*s3/3)

# Lie log
V3=dp(F6m,3); V4=dp(F6m,4); V5r=dp(F6m,5)
cZ=pm(pdZ(V3),V3); cZb=pm(pdZb(V3),pcj(V3))
corr={k:mpf('1')/2*(cZ.get(k,mpc(0))+cZb.get(k,mpc(0))) for k in set(list(cZ)+list(cZb))}
V5={k:V5r.get(k,mpc(0))-corr.get(k,mpc(0)) for k in set(list(V5r)+list(corr))}; V5=cl(V5)

# Split
Vnr={k:v for k,v in {**V3,**V4,**V5}.items() if not isr(*k)}
h3=dp(Vnr,3); h4=dp(Vnr,4); h5nr=dp(Vnr,5)

# Verification
def cjm(F,h,n=8):
    Phi=pa({(1,0):mpc(1)},h); FP=pss(F,Phi); G=FP
    for _ in range(n):
        G=psb(FP,pss(h,G))
        G={k:v for k,v in G.items() if k[0]+k[1]<=MAX_DEG and abs(v)>mpf('1e-90')}
    return cl(G)
hc=dict(h4); hc.update(h5nr)
G=cjm(F6,hc)
C32=mpc(-mpf('77')/216,mpf('97')*s3/648)
C05=mpc(-mpf('61')/2160,-mpf('43')*s3/6480)

print("="*64)
print("OPEN 13 ARCHIVAL — Lie-gauge 6-step normalization")
print("="*64)
print(f"\nh3 = {h3}  [ALG structural — F^6 degree-3 is purely resonant]")
print("\nh4 coefficients [ALG] over Q(sqrt(3)):")
h4_exact={(1,3):mpc(mpf('1')/3,s3/9),(2,2):mpc(-mpf('5')/24,-11*s3/24),
          (3,1):mpc(-mpf('1')/6,-2*s3/9),(4,0):mpc(-mpf('1')/16,7*s3/144),(0,4):mpc(0)}
labels={(1,3):"1/3 + (1/9)*sqrt(3)*i",(2,2):"-5/24 + (-11/24)*sqrt(3)*i",
        (3,1):"-1/6 + (-2/9)*sqrt(3)*i",(4,0):"-1/16 + (7/144)*sqrt(3)*i",(0,4):"0"}
for k in sorted(h4_exact):
    v_num=h4.get(k,mpc(0)); v_ex=h4_exact[k]
    ok=abs(v_ex-v_num)<mpf('1e-100')
    print(f"  h4_{k} = {labels[k]}  {'✓' if ok else 'FAIL err='+nstr(abs(v_ex-v_num),5)}")
print("\nLie log V5 resonant VF channel (intermediate — not retained MAP coeff):")
print(f"  V5_res_(3,2) = c_32^raw - correction = {nstr(V5.get((3,2),mpc(0)),20)}")
print(f"  V5_res_(0,5) = {nstr(V5.get((0,5),mpc(0)),20)}")
print("\nLie-gauge retained MAP coefficients (verified at 120 dps):")
print(f"  (3,2): {nstr(G.get((3,2),mpc(0)),20)}  err={nstr(abs(G.get((3,2),mpc(0))-C32),5)}")
print(f"  matches c_32^raw: {'✓ [ALG by convention]' if abs(G.get((3,2),mpc(0))-C32)<mpf('1e-90') else 'FAIL'}")
print(f"  (0,5): {nstr(G.get((0,5),mpc(0)),20)}  err={nstr(abs(G.get((0,5),mpc(0))-C05),5)}")
print(f"  matches c_05^raw: {'✓ [ALG by convention]' if abs(G.get((0,5),mpc(0))-C05)<mpf('1e-90') else 'FAIL'}")
print(f"\n  c_theta = Im(nu_32) - tau/2 = 97*sqrt(3)/648 - sqrt(3)/3 = -119*sqrt(3)/648")
print(f"  [ALG by convention (Lie gauge)]")
all_ok=(not h3 and abs(G.get((3,2),mpc(0))-C32)<mpf('1e-90') and abs(G.get((0,5),mpc(0))-C05)<mpf('1e-90'))
print(f"\nOPEN 13: {'ALL PASS [ALG]' if all_ok else 'ISSUES'}")
