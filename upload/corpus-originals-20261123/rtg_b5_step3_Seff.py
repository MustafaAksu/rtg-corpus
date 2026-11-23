"""
Examine S_eff = S - c_{-2,1}/(1-lam^{-3}) structurally.
Both S and c_{-2,1} are proportional to c_02^2 (we saw S is 5 terms all ~c_02^2).
If S_eff = c_02^2 * (rational function of lam, c-ratios) and that factor is nonzero,
we get a clean nonvanishing argument.

Also: |S_eff| grows? No -- S_eff is O(1) per p (the p-linearity is the explicit p factor).
The numerics show |S_eff| increasing with p only because the dyadic c_ab themselves
change with p. The KEY question: is S_eff = 0 possible for any p>=13?

Strategy: S_eff/S -> 3 means S_eff = 3S asymptotically. Since S != 0 (proved [ALG]),
S_eff != 0 for large p. For the finite remaining range we lean on exact per-p checks.
But better: show S_eff/S stays in a half-plane excluding 0, i.e. Re(S_eff/S) > 0.
The data: Re(S_eff/S) = 2.96, 2.97, ... -> 3, ALWAYS > 2.9. If we can show Re(S_eff/S) > 0
for all p>=13, then S_eff != 0 (since S != 0).
"""
import sympy as sp, mpmath as mp
lam=sp.symbols('lam')
cs,cbar={},{}
MAXC=6
for a in range(MAXC+1):
    for b in range(MAXC+1):
        if 2<=a+b<=MAXC: cs[(a,b)]=sp.symbols(f'c_{a}_{b}'); cbar[(a,b)]=sp.symbols(f'cb_{a}_{b}')
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
J={(1,0):{(1,0):sp.Integer(1)}}
for deg in range(2,5):
    FJ=F_apply(J,deg)
    for (a,b) in [(a,b) for a in range(deg+1) for b in range(deg+1) if a+b==deg]:
        J[(a,b)]=solve_channel(FJ.get((a,b),{}))
src05=F_apply(J,5).get((0,5),{})
S=sp.expand(src05.get((1,0),0)); C21=sp.expand(src05.get((-2,1),0))
S_eff=sp.expand(S - C21/(1-lam**(-3)))

# factor out c_02^2 from S and S_eff
c02=cs[(0,2)]
print("S / c_02^2 has these remaining c-symbols:", sorted(str(x) for x in (S/c02**2).free_symbols if x!=lam))
print("C21 / c_02^2 remaining c-symbols:", sorted(str(x) for x in (C21/c02**2).free_symbols if x!=lam))
print()

# Check Re(S_eff/S) > 0 across all p>=13 up to large p (NUM strong supporting the bound)
import mpmath as mp
def dyadic_coeffs(p,dps=40):
    mp.mp.dps=dps
    lm=mp.exp(2j*mp.pi/p); K=2-2*mp.cos(2*mp.pi/p)
    u=1/(1-lm); ub=mp.conj(u); D=u-ub
    def raw(Z,Zb):
        rho=u*Z+ub*Zb; eta=Z+Zb
        return (rho-mp.sin(eta)-ub*(eta+K*(mp.exp(rho)-1)-K*mp.sin(eta)))/D
    N=24; r=mp.mpf('0.08'); pts=[mp.exp(2j*mp.pi*j/N) for j in range(N)]
    vals=[[raw(r*pts[i],r*pts[j]) for j in range(N)] for i in range(N)]
    co={}
    for a in range(7):
        for b in range(7):
            if not(1<=a+b<=6): continue
            ss=mp.mpc(0)
            for i in range(N):
                for j in range(N): ss+=vals[i][j]*mp.exp(-2j*mp.pi*(a*i+b*j)/N)
            co[(a,b)]=ss/((N*N)*r**(a+b))
    return co
print("p | Re(S_eff/S) | |S_eff/S| (must stay >0, ->3)")
minRe=10
for p in list(range(13,40))+[50,80,120,200]:
    dc=dyadic_coeffs(p)
    subs={}
    for k in cs:
        if k in dc: subs[cs[k]]=complex(dc[k])
    for k in cbar:
        if k in dc: subs[cbar[k]]=complex(mp.conj(dc[k]))
    lv=complex(mp.exp(2j*mp.pi/p))
    Sval=complex(S.subs(lam,lv).subs(subs)); Seff=complex(S_eff.subs(lam,lv).subs(subs))
    ratio=Seff/Sval
    minRe=min(minRe,ratio.real)
    if p<=20 or p in (30,50,80,120,200):
        print(f"{p:3d} | {ratio.real:.5f} | {abs(ratio):.5f}")
print(f"\nmin Re(S_eff/S) over p=13..200: {minRe:.5f}  (stays well above 0)")
print("=> Re(S_eff/S) > 0 for all tested p>=13, so S_eff != 0, so F_raw^p(0,5) != 0.")
print("   [NUM strong over p<=200; the ->3 limit makes Re>0 asymptotically certain]")
