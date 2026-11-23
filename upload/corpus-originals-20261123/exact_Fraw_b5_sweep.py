"""
DYAD-OPEN-B5-ALLP Step 1: exact cyclotomic certificates for F_raw^p(0,5),
p = 6,7,8,9,10,11,12. Uses the corrected field-reduction engine (sp.invert).
Each p: reduce mod Phi_p(lambda), iterate the raw map p times as a degree-5 jet,
extract (0,5), confirm exact nonzero in Q(zeta_p).
"""
import sympy as sp
from functools import lru_cache
import sys

def run_p(p):
    lam=sp.symbols('lam')
    Phi=sp.Poly(sp.cyclotomic_poly(p, lam), lam, domain=sp.QQ)
    MD=5
    @lru_cache(maxsize=None)
    def red_cached(e):
        e=sp.sympify(e)
        if not e.has(lam): return e
        e=sp.cancel(sp.together(e))
        num,den=sp.fraction(e)
        nump=sp.Poly(sp.expand(num),lam,domain=sp.QQ).rem(Phi)
        denp=sp.Poly(sp.expand(den),lam,domain=sp.QQ).rem(Phi)
        if denp.is_zero: raise ZeroDivisionError('zero denom mod Phi')
        inv=sp.invert(denp,Phi)
        return sp.expand((nump*inv).rem(Phi).as_expr())
    def red(e): return red_cached(sp.sympify(e))
    def add_to(d,k,v):
        if v!=0: d[k]=d.get(k,0)+v
    def clean(A):
        R={}
        for k,v in A.items():
            rv=red(v)
            if rv!=0: R[k]=rv
        return R
    Z,Zb=sp.symbols('Z Zb')
    # lam^{-1} = lam^{p-1} only mod (lam^p-1); but in Q(zeta_p), 1/lam is reduced via invert.
    u=red(1/(1-lam)); ub=red(1/(1-1/lam)); D=red(u-ub); invD=red(1/D)
    K=red(2-lam-1/lam)
    rho=u*Z+ub*Zb; eta=Z+Zb
    exp_rho=sum(rho**k/sp.factorial(k) for k in range(1,MD+1))
    sin_eta=eta-eta**3/sp.factorial(3)+eta**5/sp.factorial(5)
    rho_p=rho-sin_eta
    eta_p=eta+K*exp_rho-K*sin_eta
    raw_expr=sp.expand((rho_p-ub*eta_p)*invD)
    raw_jet={}
    for term in sp.Add.make_args(raw_expr):
        pd=term.as_powers_dict(); a=int(pd.get(Z,0)); b=int(pd.get(Zb,0))
        if 1<=a+b<=MD:
            raw_jet[(a,b)]=raw_jet.get((a,b),0)+term/(Z**a*Zb**b)
    raw_jet=clean(raw_jet)
    def jmul(A,B):
        R={}
        for (a1,b1),c1 in A.items():
            for (a2,b2),c2 in B.items():
                if a1+a2+b1+b2<=MD: add_to(R,(a1+a2,b1+b2),c1*c2)
        return clean(R)
    def powers(A):
        Ps=[{(0,0):sp.Integer(1)}]
        for e in range(1,MD+1): Ps.append(jmul(Ps[-1],A))
        return Ps
    def jconj(A):
        return clean({(b,a):red(c.subs(lam,1/lam)) for (a,b),c in A.items()})
    def compose(g):
        gc=jconj(g); gp=powers(g); gcp=powers(gc); out={}
        for (a,b),coef in raw_jet.items():
            term=jmul(gp[a],gcp[b])
            for k,v in term.items(): add_to(out,k,coef*v)
        return clean(out)
    g={(1,0):sp.Integer(1)}
    for _ in range(p): g=compose(g)
    c05=red(g.get((0,5),0))
    nz = (sp.Poly(c05,lam).is_zero==False) if c05!=0 else False
    numval=complex(sp.N(c05.subs(lam, sp.exp(2*sp.pi*sp.I/p)),40))
    return c05, nz, numval

if __name__=="__main__":
    plist=[int(x) for x in sys.argv[1:]] or [6,7,8]
    for p in plist:
        try:
            c05,nz,nv=run_p(p)
            print(f"p={p}: nonzero={nz}  |F_raw^p(0,5)|={abs(nv):.6f}")
            print(f"      exact: {c05}")
        except Exception as ex:
            print(f"p={p}: ERROR {ex}")
        sys.stdout.flush()
