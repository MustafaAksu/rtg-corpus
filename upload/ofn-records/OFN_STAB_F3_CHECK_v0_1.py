# OFN_STAB_F3_CHECK_v0_1 (OFN co-owner SESSION, 19 Oct 2026). Exact Groebner of f3(Bx)=B f3(x) with reality+invertibility: Stab(f3)=T^2 x| swap.
import sympy as sp
u,v,U,V=sp.symbols('u v U V'); a,b,c,d,A,B,C,D,sd=sp.symbols('a b c d A B C D sd')
S3=sp.sqrt(3)
n21=sp.Rational(1,8)-7*sp.I*S3/72; p=n21/3; q=2*p   # one-step reduced chiral cubic (FMS/Genesis: p'=n21/3, q'=2p')
def f3(x,y,X,Y): return (p*x*x*X+q*y*Y*x, p*y*y*Y+q*x*X*y)
x=a*u+b*v; y=c*u+d*v; X=A*U+B*V; Y=C*U+D*V
L=f3(x,y,X,Y); f=f3(u,v,U,V)
R_=(a*f[0]+b*f[1], c*f[0]+d*f[1])
eqs=[]
for i in range(2):
    P=sp.Poly(sp.expand(L[i]-R_[i]),u,v,U,V)
    eqs+=P.coeffs()
# conjugate equations (reality): conj system with symbols swapped
sw={a:A,b:B,c:C,d:D,A:a,B:b,C:c,D:d}
ceqs=[sp.expand(sp.conjugate(e).subs({sp.conjugate(s):s for s in (a,b,c,d,A,B,C,D)}).xreplace(sw)) for e in eqs]
G=sp.groebner(eqs+ceqs+[(a*d-b*c)*sd-1],sd,b,c,a,d,B,C,A,D,order='lex',extension=[S3,sp.I])
for g in G.exprs: print(sp.factor(g,extension=[S3,sp.I]))
