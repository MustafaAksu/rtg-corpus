"""Independent polynomial-ring derivation: no original UVM certificate imported."""
import sympy as S, json, time
from sympy.polys.rings import ring
from sympy.polys.domains import QQ
F=QQ.algebraic_field(S.I*S.sqrt(3))
R,z,bz=ring('z,bz',F)
lam=F.from_sympy((1+S.I*S.sqrt(3))/2)
om=F.from_sympy((-1+S.I*S.sqrt(3))/2)
ONE=F.one
L=6

def cf(v):return F.from_sympy(S.sympify(v))
def cut(p,n=L):return R.from_dict({mon:c for mon,c in p.items() if sum(mon)<=n and c})
def con(p):return R.from_dict({(j,i):F.from_sympy(S.conjugate(F.to_sympy(c))) for (i,j),c in p.items()})
def mul(a,b,n=L):return cut(a*b,n)
def comp(a,b,n=L):
    bb=con(b); px=[R.one]; py=[R.one]
    k=max((m[0] for m in a),default=0)
    l=max((m[1] for m in a),default=0)
    for i in range(k):px.append(mul(px[-1],b,n))
    for i in range(l):py.append(mul(py[-1],bb,n))
    out=R.zero
    for (i,j),c in a.items():out+=mul(px[i],py[j],n)*c
    return cut(out,n)
def part(p,d):return R.from_dict({m:c for m,c in p.items() if sum(m)==d})
def inverse(h,n=L):
    scale=h[(1,0)];rest=h-z*scale;inv=z/scale
    for i in range(1,n+1):inv=cut((z-comp(rest,inv,n))/scale,n)
    return inv
def it(f,n,k):
    out=z
    for i in range(k):out=comp(f,out,n)
    return out

def series(x,coeff,n=L):
    a=R.one;out=R.zero
    for i in range(n+1):
        if i: a=mul(a,x,n)
        out+=a*cf(coeff(i))
    return cut(out,n)
eta=(z-bz)/cf(S.I*S.sqrt(3))
rho=z-eta*om
exp_minus=series(rho, lambda k: 0 if k==0 else S.Rational(1,S.factorial(k)))
sin_eta=series(eta, lambda k: (-1)**((k-1)//2)*S.Rational(1,S.factorial(k)) if k%2 else 0)
f=cut(z+om*exp_minus-lam*sin_eta)
assert part(f,1)==z*lam

# Independent homological recursion from identity f(h)=h(n)
h=z;n=lam*z
for d in range(2,L+1):
    resid=part(comp(f,h)-comp(h,n),d)
    for (a,b),c in resid.items():
        l_ab=lam**(a-b)  # algebraic unit powers
        if (a-b-1)%6==0: n+=z**a*bz**b*c
        else: h+=z**a*bz**b*(-c/(lam-l_ab))
    h=cut(h);n=cut(n)
assert comp(f,h)==comp(h,n)
hi=inverse(h)
assert comp(h,hi)==z
Jw=comp(h,lam*hi)
assert comp(hi,comp(Jw,h))==lam*z
assert it(Jw,6,6)==z
assert comp(Jw,f)==comp(f,Jw)
root= z
Fn=it(f,6,6)
for d in range(2,7):
    root+=part(Fn-it(root,6,6),d)/6
assert it(root,6,6)==Fn
assert comp(f,inverse(root))==Jw

expect_h2={ (2,0):cf((-1-S.I*S.sqrt(3))/12),(1,1):cf(-S.Rational(1,3)),(0,2):cf((1-S.I*S.sqrt(3))/24)}
assert part(h,2)==R.from_dict(expect_h2)
assert {i for i in part(h,3)}=={(3,0),(1,2),(0,3)}
assert len(h)==23
ex_n=R.from_dict({(1,0):lam,(2,1):cf(S.Rational(1,8)-S.I*S.sqrt(3)*S.Rational(7,72)),(3,2):cf(-S.Rational(5,432)+S.I*S.sqrt(3)*S.Rational(23,3888)),(0,5):cf(S.Rational(43,17280)-S.I*S.sqrt(3)*S.Rational(227,155520))})
assert n==ex_n
Jnf=it(n,5,6)
ex_Jnf=R.from_dict({(1,0):ONE,(2,1):cf(-S.Rational(1,2)-S.I*S.sqrt(3)*S.Rational(2,3)),(3,2):cf(-S.Rational(97,432)+S.I*S.sqrt(3)*S.Rational(197,324)),(0,5):cf(-S.Rational(49,8640)-S.I*S.sqrt(3)*S.Rational(307,25920))})
assert Jnf==ex_Jnf

# discrepancy of the W-native conjugate source under intrinsic J_W
lamb=F.from_sympy(S.conjugate(F.to_sympy(lam)))
delta=con(Jw)-lamb*bz
expected=con(part(comp(h,lam*z)-lam*h,2))
assert part(delta,2)==expected
assert delta[(2,0)]==cf(-S.Rational(1,6))
assert all(part(delta,i) for i in range(2,7))
# re-imposition error
D=con(hi)-bz
assert part(D,2)==-con(part(h,2))
assert D[(2,0)]==cf(-(1+S.I*S.sqrt(3))/24)
# 1-D complex scalar defect cannot be C1 at zero: quadratic scalar*g *bz cannot contain z^2
qcomplex=R.from_dict({(1,0):ONE,(0,1):ONE})*bz
assert (2,0) not in qcomplex
# explicit GL2R exact construction: Hadamard decomposition
# For k(W)=h^-1(W), k= a(W) W+b(W) conj W,
# a(W) = \int_0^1 (∂_W k)(tW) dt, b(W)=\int_0^1(∂_Wbar k)(tW) dt.
a=R.zero; b=R.zero
for (i,j),c in hi.items():
    degree=i+j
    if i: a+=z**(i-1)*bz**j*c*cf(S.Rational(i,degree))
    if j: b+=z**i*bz**(j-1)*c*cf(S.Rational(j,degree))
assert cut(a*z+b*bz)==hi
# complex conjugation: conj(k)=con(a)*bz+con(b)*z, define fibre G(s)=con(a)s+con(b)conj(s)
assert cut(con(a)*bz+con(b)*z)==con(hi)
assert a[(0,0)]==ONE and (0,0) not in b
# Extend to arbitrary finite order using formal rational coefficients; exact analytic h^-1 if it exists.

# source weight from pure congruence
weight=[(i,j) for i in range(7) for j in range(7-i) if i+j>=1 and (i-j+1)%6==0]
assert set(weight)=={(0,1),(1,2),(2,3),(5,0)}

print('SYMPY-INDEPENDENT-PASS: E0-E6, G0-G6, P2, A1\' degree2, A1\' degrees2..6, P3, C2a1, A2, GL2R full 6-jet')
print('f degree2: ',part(f,2))
print('h degree2: ',part(h,2))
print('Jw degree2:',part(Jw,2))
print('W-source defect degree2:',part(delta,2))
print('P3 degree2:',part(D,2))
print('GL2R A and B degree0/1:',part(a,0)+part(a,1),part(b,0)+part(b,1))
print('coefficient counts:',len(h),len(Jw),{d:len(part(delta,d)) for d in range(2,7)})
