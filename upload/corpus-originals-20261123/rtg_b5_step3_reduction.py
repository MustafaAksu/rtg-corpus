"""
DYAD-OPEN-B5-ALLP Step 3: analyze Q_p = R_p / (p lam^{p-1} S) and bound it away from -1.

R_p = sum over non-(1,0) source modes (beta,m) of:  coeff * lam^{p-1} * G_{beta,m}(p)
  where G_{beta,m}(p) = sum_{k=0}^{p-1} k^m lam^{(beta-1)k}.
secular = p lam^{p-1} S, S = coeff of mode (1,0).

So Q_p = [ sum_{(beta,m)!=(1,0)} coeff_{beta,m} G_{beta,m}(p) ] / (p * S).

Key: lam = e^{2pi i/p}. The sums G_{beta,m}(p) have closed forms.
For m=0, beta!=1: G = (lam^{(beta-1)p}-1)/(lam^{beta-1}-1) = 0  (since lam^{(beta-1)p}=1)
  UNLESS p|(beta-1). Our betas in {-5,-4,-3,-2,-1,0,2}, so beta-1 in {-6,-5,-4,-3,-2,-1,1}.
  For p>=13, none of these are divisible by p, so ALL m=0 nonsecular sums VANISH.
For m=1, beta=-2 (the (-2,1) polynomial mode): G_{-2,1}(p)=sum_k k lam^{-3k}, closed form.

So for p>=13: R_p reduces to ONLY the (-2,1) polynomial-mode contribution (+ possibly
(1,1) if present). Let's confirm the mode set and compute Q_p exactly for p>=13.
"""
import sympy as sp, mpmath as mp
from functools import lru_cache
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
print("(0,5) source modes:", sorted(src05.keys()))
print()
print("KEY OBSERVATION for p>=13:")
print("  m=0 nonsecular modes have beta in {-5,-4,-3,-2,-1,0,2} -> beta-1 in {-6,-5,-4,-3,-2,-1,1}")
print("  geometric sum G_{beta,0}(p) = (lam^{(beta-1)p}-1)/(lam^{beta-1}-1) = 0 for p NOT dividing (beta-1)")
print("  for p>=13 > 6 >= |beta-1|, p never divides (beta-1), so ALL m=0 nonsecular sums VANISH.")
print("  => for p>=13, R_p comes ONLY from polynomial modes m>=1:", [k for k in src05 if k[1]>=1])
print()

# So for p>=13: F = secular + (only polynomial-mode contributions).
# The single polynomial mode is (-2,1). Its contribution to R_p:
#   coeff_{-2,1} * lam^{p-1} * sum_{k=0}^{p-1} k lam^{-3k}
# sum_{k=0}^{p-1} k x^k = x(1-p x^{p-1}+(p-1)x^p)/(1-x)^2 ; with x=lam^{-3}, x^p=1:
#   = x(1-p x^{p-1}+(p-1))/(1-x)^2 = x(p - p x^{p-1})/(1-x)^2 = p x(1-x^{p-1})/(1-x)^2
#   x^{p-1}=x^{-1} (since x^p=1) => = p x(1-x^{-1})/(1-x)^2 = p(x-1)/(1-x)^2 = -p/(1-x)
# So G_{-2,1}(p) = -p/(1-lam^{-3})  [for p>=13, exact, p-LINEAR]
x=lam**(-3)
Gtest=sp.simplify(sp.summation(sp.symbols('k')*x**sp.symbols('k'),(sp.symbols('k'),0,sp.symbols('P')-1)))
print("Symbolic check of sum_{k=0}^{P-1} k x^k (general):")
print("  ", Gtest)
print()
print("With x^P=1 (P=p, x=lam^{-3}): the sum reduces to G_{-2,1}(p) = -p/(1-lam^{-3}).")
print("This is p-LINEAR, same order as the secular term p*S. So Q_p has a FINITE limit.")
