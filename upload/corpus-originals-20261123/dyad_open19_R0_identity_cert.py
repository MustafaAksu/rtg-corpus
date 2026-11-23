# OPEN 19 certificate (exit-gated). Exact Q(i*sqrt3) check: R0 := T^3 o F^{-1/2} (F=T^6) vs S_h = h(-I)h^{-1}, through total degree N.
import sys; sys.path.insert(0,'/home/claude')
from dyad_return_qchi_exact import Q,P
from fractions import Fraction as Fr
from math import factorial
N=int(sys.argv[1]) if len(sys.argv)>1 else 6
chi=Q(0,1); om=Q(Fr(-1,2),Fr(1,2)); lam=Q(Fr(1,2),Fr(1,2)); lamb=lam.conj()
z=P({(1,0):Q(1)},N); zb=P({(0,1):Q(1)},N); one=P({(0,0):Q(1)},N)
eta=(z-zb).scale(Q(0,Fr(-1,3))); rho=z-eta.scale(om)
def series(x,coeffs):
    r=P({},N); p=one
    for k in range(1,N+1):
        p=p*x
        if coeffs(k)!=0: r=r+p.scale(Q(coeffs(k)))
    return r
sinx=lambda x: series(x,lambda k: 0 if k%2==0 else Fr((-1)**((k-1)//2),factorial(k)))
expm1=lambda x: series(x,lambda k: Fr(1,factorial(k)))
f=(rho-sinx(eta))+(eta+expm1(rho)-sinx(eta)).scale(om)
def comp(a,b): return a.compose(b,b.conj())   # a o b
def eq(a,b,upto):
    d=a-b; return all(v.iszero() for k,v in d.d.items() if sum(k)<=upto)
idm=z
T3=comp(f,comp(f,f)); F=comp(T3,T3)
# inverse of F (tangent to id) to degree N
Finv=z
for _ in range(N): Finv=Finv+ (z-comp(F,Finv))
# square root G of Finv, G tangent to id
G=z
for k in range(2,N+1):
    E=(Finv-comp(G,G)).deg(k); G=G+E.scale(Q(Fr(1,2)))
R0=comp(T3,G)
print('N=',N)
print('R0 o R0 = id :',eq(comp(R0,R0),idm,N))
print('R0 f = f R0  :',eq(comp(R0,f),comp(f,R0),N))
print('R0 F = F R0  :',eq(comp(R0,F),comp(F,R0),N))
print('DR0 = -I     :',R0.get((1,0))==Q(-1) and R0.get((0,1)).iszero())
# one-step normalizer h (resonant coefficients zero)
h=z; n=z.scale(lam)
for k in range(2,N+1):
    E=(comp(f,h)-comp(h,n)).deg(k)
    for (a,b),v in E.d.items():
        mult=Q(1)
        for _ in range(a): mult=mult*lam
        for _ in range(b): mult=mult*lamb
        den=lam-mult
        if (a-b-1)%6==0: n=n+P({(a,b):v},N)
        else: h=h+P({(a,b):v.__neg__()/den},N)
print('f h = h n    :',eq(comp(f,h),comp(h,n),N))
hinv=z
for _ in range(N): hinv=hinv+(z-comp(h,hinv))
S=comp(h,comp(z.scale(Q(-1)),hinv))
print('S_h jet == R0 jet through degree',N,':',eq(S,R0,N))
d=(S-R0); bad={k:v for k,v in d.d.items() if sum(k)<=N}

# ---- exit gates ----
import sys as _s
h2=h.deg(2)
checks={
 'R0^2=id':eq(comp(R0,R0),idm,N),'R0f=fR0':eq(comp(R0,f),comp(f,R0),N),'R0F=FR0':eq(comp(R0,F),comp(F,R0),N),
 'DR0=-I':R0.get((1,0))==Q(-1) and R0.get((0,1)).iszero(),'fh=hn':eq(comp(f,h),comp(h,n),N),
 'S_h=R0':eq(S,R0,N),'[R0]_2=2h2':eq(R0.deg(2),h2.scale(Q(2)),2)}
fails=[k for k,v in checks.items() if not v]
print('CHECKS',len(checks),'FAIL' if fails else 'PASS',fails)
_s.exit(1 if fails else 0)
