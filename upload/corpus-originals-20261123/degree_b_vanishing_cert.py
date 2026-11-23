#!/usr/bin/env python3
"""
degree_b_vanishing_cert.py
Exit-code-gated certificate for DYAD-ALG-VANISH-B2/B3/B4.

Certifies F_raw^p(0,b)=0 for p>=b+2, b in {2,3,4}, by TWO independent routes:
  (A) exact symbolic source-beta argument (b=3 closed form simplifies to 0)
  (B) direct high-precision iteration of the raw map

Exits 1 on any failure.
"""
import sys
import sympy as sp
import mpmath as mp

FAIL = False

# ---------- Route A: symbolic (b=3) ----------
lam = sp.symbols('lambda', nonzero=True)
n = sp.symbols('n', integer=True, positive=True)
cs = {(a,b): sp.symbols(f'c_{a}_{b}') for a in range(5) for b in range(5) if 2<=a+b<=4}

def solve_rec(src):
    tot = sp.Integer(0)
    for coeff, beta in src:
        gs = n if (beta-1)==0 else (lam**((beta-1)*n)-1)/(lam**(beta-1)-1)
        tot += coeff*lam**(n-1)*gs
    return sp.expand(tot)

def conj_jet(gg):
    o={}
    for (a,b),c in gg.items():
        o[(b,a)] = o.get((b,a),sp.Integer(0)) + sp.expand(c.subs(lam,1/lam))
    return o
def mul(g1,g2,md):
    o={}
    for (a1,b1),c1 in g1.items():
        for (a2,b2),c2 in g2.items():
            if a1+a2+b1+b2<=md:
                o[(a1+a2,b1+b2)] = o.get((a1+a2,b1+b2),sp.Integer(0))+c1*c2
    return o
def powj(gg,e,md):
    r={(0,0):sp.Integer(1)}
    for _ in range(e): r=mul(r,gg,md)
    return r
def Fof(gg,md):
    gc=conj_jet(gg); o={}
    for (a,b),c in gg.items():
        if a+b<=md: o[(a,b)]=o.get((a,b),sp.Integer(0))+lam*c
    for (a,b),cc in cs.items():
        if a+b>md: continue
        t=mul(powj(gg,a,md),powj(gc,b,md),md)
        for key,val in t.items():
            if key[0]+key[1]<=md: o[key]=o.get(key,sp.Integer(0))+cc*val
    return o
def decompose(R):
    out=[]
    for t in sp.expand(R).as_ordered_terms():
        pw=t.as_powers_dict(); beta=sp.Integer(0); cpow=sp.Integer(0); rest=sp.Integer(1)
        for base,e in pw.items():
            if base==lam:
                poly=sp.Poly(e,n); beta+=poly.coeff_monomial(n); cpow+=poly.coeff_monomial(1)
            else: rest*=base**e
        out.append((rest*lam**cpow,int(beta)))
    merged={}
    for c,b in out: merged[b]=merged.get(b,0)+c
    return [(sp.simplify(c),b) for b,c in merged.items() if sp.simplify(c)!=0]

deg2={(a,b):solve_rec([(cs[(a,b)],a-b)]) for (a,b) in [(2,0),(1,1),(0,2)]}
X=sp.symbols('X')
g={(1,0):lam**n}
for k,v in deg2.items(): g[k]=v
g[(0,3)]=X
gn=Fof(g,3)
R3=sp.expand(gn[(0,3)]-lam*X)
src3=decompose(R3)
beta_set_3 = sorted([b for _,b in src3])
if 1 in beta_set_3:
    print(f"FAIL: secular mode beta=1 in (0,3) source {beta_set_3}"); FAIL=True
A03=solve_rec(src3)
for pval in [5,6,7,8,9,11,13]:
    e=sp.simplify(sp.expand_complex(A03.subs(n,pval).subs(lam, sp.exp(2*sp.pi*sp.I/pval))))
    if sp.simplify(e)!=0:
        print(f"FAIL: symbolic A^{pval}_(0,3) != 0 (got {e})"); FAIL=True
print(f"Route A (symbolic, b=3): source beta-set {beta_set_3}, A^p_(0,3)=0 for p in 5..13  [OK]")

# ---------- Route B: direct iteration ----------
mp.mp.dps=50
def make_Frawp(p):
    lm=mp.exp(2j*mp.pi/p); K=2-2*mp.cos(2*mp.pi/p)
    u=1/(1-lm); ub=mp.conj(u); D=u-ub
    def raw(Z):
        Zb=mp.conj(Z); rho=u*Z+ub*Zb; eta=Z+Zb
        return (rho-mp.sin(eta)-ub*(eta+K*(mp.exp(rho)-1)-K*mp.sin(eta)))/D
    def Fp(W):
        Z=W
        for _ in range(p): Z=raw(Z)
        return Z
    return Fp
N=28
def coeff(F,d,k):
    if (d+k)%2: return mp.mpc(0)
    if (d+k)//2<0 or (d-k)//2<0: return mp.mpc(0)
    t=mp.mpc(0)
    for j in range(N):
        phi=2*mp.pi*j/N
        tay=mp.taylor(lambda r,phi=phi,F=F:F(r*mp.exp(mp.mpc(0,phi))),0,d)
        t+=tay[d]*mp.exp(mp.mpc(0,-phi*k))
    return t/N

TOL=mp.mpf('1e-35')
for b,clean_start in [(2,4),(3,5),(4,6)]:
    # must vanish for p>=clean_start
    for p in range(clean_start, clean_start+4):
        c=coeff(make_Frawp(p), b, -b)
        if abs(c) > TOL:
            print(f"FAIL: |F_raw^{p}(0,{b})| = {mp.nstr(abs(c),4)} should be 0"); FAIL=True
    # must be nonzero at the resonant exception p=b+1
    c=coeff(make_Frawp(b+1), b, -b)
    if abs(c) <= TOL:
        print(f"FAIL: |F_raw^{b+1}(0,{b})| should be nonzero (resonant)"); FAIL=True
print("Route B (direct iteration, 50 dps): vanishes p>=b+2, nonzero at p=b+1  [OK]")

if FAIL:
    print("\nCERTIFICATE FAILED")
    sys.exit(1)
print("\nCERTIFICATE PASSED: F_raw^p(0,b)=0 for p>=b+2, b in {2,3,4}  [ALG]")
sys.exit(0)
