"""Independent exact general-quadratic six-step source check (ER2B-C20/C07).
Conjugate coordinates and coefficient symbols are treated as independent formal variables.
"""
from sympy import sqrt, I, Rational
from sympy.polys.domains import QQ
from sympy.polys.rings import ring
K=QQ.algebraic_field(I*sqrt(3))
D=K.from_sympy(I*sqrt(3))
lam=(K.one+D)/2; lb=(K.one-D)/2
R,a,ab,b,bb,u,ub,v,vb,t,tb=ring('a,ab,b,bb,u,ub,v,vb,t,tb',K)
# First component is w, second its formal conjugate.
A=lambda x:(lam*x[0],lb*x[1])
q=lambda x:(u*x[0]**2+v*x[0]*x[1]+t*x[1]**2,tb*x[0]**2+vb*x[0]*x[1]+ub*x[1]**2)
add=lambda a,b:tuple(i+j for i,j in zip(a,b))
sub=lambda a,b:tuple(i-j for i,j in zip(a,b))
scale=lambda a,s:tuple(i*s for i in a)
def proj(es):
    mean=scale(tuple(sum(e[j] for e in es) for j in range(2)),K.one/3)
    return tuple(sub(e,mean) for e in es)
def run(edges,projected):
    L=tuple(edges); Q=tuple((R.zero,R.zero) for _ in edges); C=Q
    for j in range(6):
        L1=tuple(A(x) for x in L)
        Q1=tuple(add(A(y),q(x)) for x,y in zip(L,Q))
        C1=tuple(add(A(z),sub(sub(q(add(x,y)),q(x)),q(y))) for x,y,z in zip(L,Q,C))
        L,Q,C=(L1,proj(Q1),proj(C1)) if projected else (L1,Q1,C1)
    assert L==tuple(edges) and all(e==(R.zero,R.zero) for e in Q)
    return C
mu=(9+3*D)*u*v-(3+3*D)*v*vb-6*t*tb
mub=(9-3*D)*ub*vb-(3-3*D)*v*vb-6*t*tb
chi=(-6+2*D)*u*v+(1+D)*v*vb-4*t*tb
chib=(-6-2*D)*ub*vb+(1-D)*v*vb-4*t*tb
iso=run(((a,ab),),False)[0]
assert iso==(mu*a*a*ab,mub*a*ab*ab)
print('C20 generic mu22(q), both conjugate components: PASS')
es=((a,ab),(b,bb),(-a-b,-ab-bb));cs=run(es,True)
sep=proj(tuple((w*w*wb,w*wb*wb) for w,wb in es))
# i*S = (a*bb-ab*b)/2, -i*S = negative of this.
area_i=(a*bb-ab*b)/2
expected=[]
for i in range(3):
    ed=sub(es[(i+1)%3],es[(i-1)%3])
    expected.append((mu*sep[i][0]/3+2*chi*area_i*ed[0]/3,mub*sep[i][1]/3-2*chib*area_i*ed[1]/3))
assert cs==tuple(expected)
print('C14 nu22=mu22/3 and C07 generic chi(q), all projected components: PASS')
print('Exact quadratic-composition sector only; no all-order or physical claim.')
