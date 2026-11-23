import sympy as sp
from functools import lru_cache
lam=sp.symbols('lam')
Phi=sp.Poly(lam**6+lam**5+lam**4+lam**3+lam**2+lam+1,lam,domain=sp.QQ)
MD=5
@lru_cache(maxsize=None)
def red_cached(e):
    e=sp.sympify(e)
    if not e.has(lam): return e
    e=sp.cancel(sp.together(e))
    num,den=sp.fraction(e)
    nump=sp.Poly(sp.expand(num),lam,domain=sp.QQ).rem(Phi)
    denp=sp.Poly(sp.expand(den),lam,domain=sp.QQ).rem(Phi)
    if denp.is_zero: raise ZeroDivisionError('zero denominator mod Phi')
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

# Build raw jet
Z,Zb=sp.symbols('Z Zb')
u=red(1/(1-lam)); ub=red(1/(1-lam**6)); D=red(u-ub); invD=red(1/D); K=red(2-lam-lam**6)
rho=u*Z+ub*Zb; eta=Z+Zb
exp_rho=sum(rho**k/sp.factorial(k) for k in range(1,MD+1))
sin_eta=eta-eta**3/sp.factorial(3)+eta**5/sp.factorial(5)
rho_p=rho-sin_eta
eta_p=eta+K*exp_rho-K*sin_eta
raw_expr=sp.expand((rho_p-ub*eta_p)*invD)
raw_jet={}
for term in sp.Add.make_args(raw_expr):
    pd=term.as_powers_dict(); a=int(pd.get(Z,0)); b=int(pd.get(Zb,0));
    if 1 <= a+b <= MD:
        coeff=term/(Z**a*Zb**b)
        raw_jet[(a,b)]=raw_jet.get((a,b),0)+coeff
raw_jet=clean(raw_jet)
print('[one-step jet ready]', len(raw_jet), flush=True)

def jmul(A,B):
    R={}
    for (a1,b1),c1 in A.items():
        for (a2,b2),c2 in B.items():
            if a1+a2+b1+b2<=MD:
                add_to(R,(a1+a2,b1+b2),c1*c2)
    return clean(R)

def powers(A):
    Ps=[{(0,0):sp.Integer(1)}]
    for e in range(1,MD+1):
        Ps.append(jmul(Ps[-1],A))
    return Ps

def jconj(A):
    return clean({(b,a):red(c.subs(lam,lam**6)) for (a,b),c in A.items()})

def compose(g):
    gc=jconj(g)
    gp=powers(g); gcp=powers(gc)
    out={}
    for (a,b),coef in raw_jet.items():
        term=jmul(gp[a],gcp[b])
        for k,v in term.items():
            add_to(out,k,coef*v)
    return clean(out)

g={(1,0):sp.Integer(1)}
for k in range(7):
    g=compose(g)
    c05=red(g.get((0,5),0))
    print(k+1, len(g), c05==0, flush=True)

c05=red(g.get((0,5),0))
print('c05=', c05)
print('zero?', c05==0)
print('num=', complex(sp.N(c05.subs(lam, sp.exp(2*sp.pi*sp.I/7)),50)))
