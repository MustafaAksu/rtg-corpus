"""
DYAD-OPEN-B5-ALLP Step 2: general secular decomposition of F_raw^p(0,5).

Target:  F_raw^p(0,5) = p * lam^{p-1} * S  +  R_p
where S = S_05^{(beta=1)} is the secular source coefficient, and R_p collects
the nonsecular cyclotomic sums and polynomial-mode contributions.

Approach: solve the (0,5) recursion A^{n+1} = lam A^n + Source(n) where Source(n)
is the full (0,5) source as modes {(beta,m): coeff} meaning coeff*n^m*lam^{beta n}.
The discrete Duhamel solution of A^{n+1}=lam A^n + n^m lam^{beta n}, A^0=0:
  - (beta != 1):     sum_{k} lam^{n-1-k} k^m lam^{beta k}  -> closed form
  - (beta == 1, m):  sum_{k} lam^{n-1-k} k^m lam^{k} = lam^{n-1} sum_k k^m
                      = lam^{n-1} * (power sum) -> SECULAR (polynomial in n of degree m+1)
At n=p, lam^p=1:
  - (beta != 1, m=0): geometric sum = 0 unless p|(beta-1). For our source betas
    (all in [-5,2], none =1), p|(beta-1) only for small p -> the v6.4 breaker primes.
  - (beta == 1, m=0): A^p gets lam^{p-1} * p * S   <-- THE SECULAR TERM p lam^{p-1} S
  - (beta == 1, m=1): A^p gets lam^{p-1} * sum_{k=0}^{p-1} k = lam^{p-1} p(p-1)/2  (polynomial)
  - (beta != 1, m>=1): finite-difference closed forms; at lam^p=1 reduce.

We compute, symbolically in lam and the formal jet coefficients, then specialize
to dyadic coefficients per p and compare against the swept exact values.
"""
import sympy as sp
from functools import lru_cache

lam = sp.symbols('lam')
nn  = sp.symbols('nn', integer=True, positive=True)
pp  = sp.symbols('pp', integer=True, positive=True)

cs, cbar = {}, {}
MAXC=6
for a in range(MAXC+1):
    for b in range(MAXC+1):
        if 2<=a+b<=MAXC:
            cs[(a,b)]=sp.symbols(f'c_{a}_{b}'); cbar[(a,b)]=sp.symbols(f'cb_{a}_{b}')

# ---- beta-graded engine (modes (beta,m)) to get the (0,5) SOURCE ----
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
        elif m==0 and b==1:
            out[(1,1)]=out.get((1,1),0)+c*lam**(-1)
        else:
            out[(b,m)]=out.get((b,m),0)+c  # leave higher secular as-is (handled in Step-2 solver)
    return {k:sp.expand(v) for k,v in out.items() if sp.expand(v)!=0}

# build jet to degree 4, then F once -> (0,5) source
J={(1,0):{(1,0):sp.Integer(1)}}
for deg in range(2,5):
    FJ=F_apply(J,deg)
    for (a,b) in [(a,b) for a in range(deg+1) for b in range(deg+1) if a+b==deg]:
        J[(a,b)]=solve_channel(FJ.get((a,b),{}))
FJ5=F_apply(J,5)
src05=FJ5.get((0,5),{})
print("(0,5) source modes (beta,m):", sorted(src05.keys()))
S = src05.get((1,0), sp.Integer(0))     # the beta=1, m=0 secular source coefficient
print("\nS_05^{beta=1} (secular source coeff), #terms:", len(sp.expand(S).as_ordered_terms()))

# ---- Step 2 solver: solve A^{n+1}=lam A^n + Source(n) with full modes, evaluate at n=p, lam^p=1 ----
@lru_cache(maxsize=None)
def power_sum(m):
    # sum_{k=0}^{pp-1} k^m  as polynomial in pp (Faulhaber)
    k=sp.symbols('k')
    return sp.simplify(sp.summation(k**m, (k,0,pp-1)))

def solve_at_p(src):
    """Return F_raw^p(0,5) split as (secular_part, residual_part), valid at lam^p=1.
    secular_part = p*lam^{p-1}*S  (the (beta=1,m=0) contribution).
    residual_part = everything else, with lam^{p}->1 applied."""
    secular=sp.Integer(0); residual=sp.Integer(0)
    for (b,m),c in src.items():
        if b==1:
            # A^p gets lam^{p-1} * sum_{k=0}^{p-1} k^m * c
            term = c*lam**(pp-1)*power_sum(m)
            if m==0:
                secular += term          # = c*lam^{p-1}*p  == p lam^{p-1} S-part
            else:
                residual += term         # polynomial-in-p secular (m>=1)
        else:
            # non-secular: A^p = c*lam^{p-1}* sum_{k=0}^{p-1} k^m lam^{(b-1)k}
            k=sp.symbols('k')
            gsum=sp.summation(k**m*lam**((b-1)*k),(k,0,pp-1))
            residual += c*lam**(pp-1)*gsum
    return secular, residual

secular, residual = solve_at_p(src05)
print("\n[secular and residual symbolic forms built]")

# ---- specialize to dyadic coefficients and compare to swept exact values ----
import mpmath as mp
def dyadic_coeffs(p, dps=50):
    mp.mp.dps=dps
    lm=mp.exp(2j*mp.pi/p); K=2-2*mp.cos(2*mp.pi/p)
    u=1/(1-lm); ub=mp.conj(u); D=u-ub
    def raw(Z,Zb):
        rho=u*Z+ub*Zb; eta=Z+Zb
        return (rho-mp.sin(eta)-ub*(eta+K*(mp.exp(rho)-1)-K*mp.sin(eta)))/D
    N=24; r=mp.mpf('0.08')
    pts=[mp.exp(2j*mp.pi*j/N) for j in range(N)]
    vals=[[raw(r*pts[i],r*pts[j]) for j in range(N)] for i in range(N)]
    co={}
    for a in range(7):
        for b in range(7):
            if not(1<=a+b<=6): continue
            ss=mp.mpc(0)
            for i in range(N):
                for j in range(N):
                    ss+=vals[i][j]*mp.exp(-2j*mp.pi*(a*i+b*j)/N)
            co[(a,b)]=ss/((N*N)*r**(a+b))
    return co

# swept exact |F| reference
sweep={6:0.274410,7:0.243185,8:0.289674,9:0.355511,10:0.441559,11:0.550098,12:0.684187}
print("\np | |secular| | |residual| | |sec+res| | swept |F| | match")
for p in [6,7,8,9,10,11,12]:
    dc=dyadic_coeffs(p)
    subs={}
    for k in cs:
        if k in dc: subs[cs[k]]=complex(dc[k])
    for k in cbar:
        if k in dc: subs[cbar[k]]=complex(mp.conj(dc[k]))
    lv=complex(mp.exp(2j*mp.pi/p))
    sec=complex(secular.subs(pp,p).subs(lam,lv).subs(subs))
    res=complex(residual.subs(pp,p).subs(lam,lv).subs(subs))
    tot=sec+res
    ok=abs(abs(tot)-sweep[p])<1e-4
    print(f"{p} | {abs(sec):.5f} | {abs(res):.5f} | {abs(tot):.5f} | {sweep[p]:.5f} | {ok}")
