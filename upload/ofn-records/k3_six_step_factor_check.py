# Six-step-clock factor obstruction for the projected K3 / kappa-family centre-manifold map.
# Claim: let f(u,v) = (p u|u|^2 + q|v|^2 u, p v|v|^2 + q|u|^2 v) be the six-step cubic (chiral form, real-linear
# coordinates of C^2 = R^4).  A real-linear surjection l: R^4 -> R^d (d=1,2,3) with  l∘f = t∘l  for some cubic t
# (i.e. l∘f constant on the fibres of l) exists, for real (p,q), only if
#     d=2 : q = 0          d=1,3 : p = q = 0.
# Method: every rank-d l is, up to left GL_d, [I | M]·P for some coordinate permutation P (all charts enumerated);
# lex Groebner basis in (M, p, q) and elimination of M give the parameter locus where a solution exists.
# Also re-checks psi2 of exact_q.py against the degree-2 centre-manifold invariance equation if that file is given.
import sympy as sp, itertools, sys
x=sp.symbols('x0:4',real=True); pr,pi,qr,qi=sp.symbols('pr pi qr qi',real=True)
p=pr+sp.I*pi; q=qr+sp.I*qi
def fR(X):
    u=X[0]+sp.I*X[1]; v=X[2]+sp.I*X[3]; uu=sp.expand(u*sp.conjugate(u)); vv=sp.expand(v*sp.conjugate(v))
    a=sp.expand(p*u*uu+q*vv*u); b=sp.expand(p*v*vv+q*uu*v)
    return sp.Matrix([sp.re(a),sp.im(a),sp.re(b),sp.im(b)]).applyfunc(sp.expand)
def locus(r):
    res=[]
    for cols in itertools.combinations(range(4),r):
        perm=list(cols)+[i for i in range(4) if i not in cols]
        mm=sp.symbols(f'n0:{r*(4-r)}',real=True); Mx=sp.Matrix(r,4-r,mm); P=sp.eye(4)[perm,:]
        L=sp.Matrix.hstack(sp.eye(r),Mx)*P; Kb=P.T*sp.Matrix.vstack(-Mx,sp.eye(4-r))
        cc=sp.symbols(f'k0:{4-r}',real=True); X=sp.Matrix(x)
        d=sp.expand(L*(fR(list(X+Kb*sp.Matrix(cc)))-fR(list(X))))
        eqs=[sp.expand(co) for comp in d for co in sp.Poly(comp,*x,*cc).coeffs()]
        G=sp.groebner(eqs,*mm,pr,pi,qr,qi,order='lex')
        res.append([g for g in G.exprs if not (g.free_symbols & set(mm))])
    return res
ok=True
# real points of the locus: d=2 -> every chart's elimination ideal must contain qr,qi or force p=q=0 ;
for r,need in [(1,'pq'),(2,'q'),(3,'pq')]:
    for E in locus(r):
        I=sp.groebner(E+[],pr,pi,qr,qi,order='lex')
        # test: does the ideal imply qr^2+qi^2 = 0 over the reals?  check q-norm in radical via membership of a power
        qn=qr**2+qi**2; pn=pr**2+pi**2
        good = any(I.contains(qn**e) for e in (1,2)) or (I.contains(qr) and I.contains(qi))
        if need=='pq': good = good and any(I.contains(pn**e) for e in (1,2))
        print(f"rank {r}: elimination ideal {list(I.exprs)} -> {'OK' if good else 'FAIL'}"); ok&=good
print("ALL PASS" if ok else "FAIL"); sys.exit(0 if ok else 1)
