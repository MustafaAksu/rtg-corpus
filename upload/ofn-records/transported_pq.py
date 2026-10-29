# Transported kappa-family F^N_k(z)_e = N(z_e) - (k/3) sum N, N = lambda z + n21 z^2 zbar + O(5) (lambda-equivariant NF).
# N has no quadratic part => centre-manifold psi = O(3); psi_3 enters cubic only via linear part (killed by P).
# Reduced one-step cubic G3_e = n21 (w_e|w_e|^2 - S), S = (1/3) sum w_j|w_j|^2 ; G3 is lambda-equivariant,
# so six-step cubic f3 = 6*conj(lambda)*G3 = mu*(w_e|w_e|^2 - S), mu = 6 conj(lambda) n21.  Kappa-independent.
import sympy as sp
s3=sp.sqrt(3); lam=sp.Rational(1,2)+sp.I*s3/2; lamb=sp.conjugate(lam)
n21=sp.Rational(1,8)-7*sp.I*s3/72
mu=sp.nsimplify(sp.expand(6*lamb*n21)); print("mu =",mu)
u,v,U,V=sp.symbols('u v U V')        # U=conj u, V=conj v
w2=(u-v)/(lam-lamb); w1=u-lam*w2; W2=(U-V)/(lamb-lam); W1=U-lamb*W2
w3=-w1-w2; W3=-W1-W2
S=(w1*w1*W1+w2*w2*W2+w3*w3*W3)/3
f1=mu*(w1*w1*W1-S); f2=mu*(w2*w2*W2-S)
uf=sp.Poly(sp.expand(f1+lam*f2),u,v,U,V); vf=sp.Poly(sp.expand(f1+lamb*f2),u,v,U,V)
p=sp.nsimplify(sp.simplify(uf.coeff_monomial(u**2*U))); q=sp.nsimplify(sp.simplify(uf.coeff_monomial(u*v*V)))
pv=sp.nsimplify(sp.simplify(vf.coeff_monomial(v**2*V))); qv=sp.nsimplify(sp.simplify(vf.coeff_monomial(u*v*U)))
oth=[m for m,c in zip(uf.monoms(),uf.coeffs()) if m not in [(2,0,1,0),(1,1,0,1)] and sp.simplify(c)!=0]
print("p =",sp.radsimp(p)," q =",sp.radsimp(q)," | v-comp p,q:",sp.radsimp(pv),sp.radsimp(qv)," other monomials:",oth)
print("Re p =",sp.simplify(sp.re(p)),"  Re q =",sp.simplify(sp.re(q)))
