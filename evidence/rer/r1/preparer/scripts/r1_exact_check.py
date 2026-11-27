"""RER R1 independent exact jet check, scoped to the declared projected model.
No imported producer or reviewer code. No analytic radius/physical certificate.
"""
import sympy as sp
from sympy.polys.rings import ring
from sympy.polys.domains import QQ

# Work in raw real dyad variables; k is a symbolic parameter, not a state coordinate.
R,x,y,z,w,k=ring('x,y,z,w,k',QQ)
zero=R.zero
A=lambda u:(u[0]-u[1],u[0])
q=lambda u:(zero,u[0]**2/2)
r=lambda u:(u[1]**3/6,(u[0]**3+u[1]**3)/6)
h=lambda u:(-u[0]**2/2+u[0]*u[1]/2-u[1]**2/4,(-u[0]**2+u[1]**2)/4)
add=lambda a,b:tuple(i+j for i,j in zip(a,b))
sub=lambda a,b:tuple(i-j for i,j in zip(a,b))
scale=lambda a,c:tuple(c*i for i in a)
def diff(p,u,v):
    # All q/h derivatives computed by exact polarization of a quadratic form.
    return sub(sub(p(add(u,v)),p(u)),p(v))

def project(edges):
    mean=scale(tuple(sum(e[j] for e in edges) for j in range(2)),QQ(1,3))
    return tuple(sub(e,mean) for e in edges)

def jet(edges, qfun, rfun, projected):
    L=tuple(edges); Q=tuple((zero,zero) for _ in edges); C=Q
    for _ in range(6):
        nL=tuple(A(a) for a in L)
        nQ=tuple(add(A(b),qfun(a)) for a,b in zip(L,Q))
        nC=tuple(add(add(A(c),diff(qfun,a,b)),rfun(a)) for a,b,c in zip(L,Q,C))
        L,Q,C=(nL,project(nQ),project(nC)) if projected else (nL,nQ,nC)
    assert L==tuple(edges) and all(a==(zero,zero) for a in Q)
    return C

def qsig(u): return scale(q(u),k)
def rsig(u):
    # T H = H Ttilde; H=id+(1-k)h, no cubic term chosen.
    # cubic rtilde=r+Dq*h-Dh(Au)*qtilde.
    H=lambda a:scale(h(a),1-k)
    return sub(add(r(u),diff(q,u,H(u))),diff(H,A(u),qsig(u)))

assert sub(add(q((x,y)),A(h((x,y)))),h(A((x,y))))==(zero,zero)
print('quadratic homological cancellation: PASS')
assert sub(add(q((x,y)),A(scale(h((x,y)),1-k))),scale(h(A((x,y))),1-k))==qsig((x,y))
print('q_sigma = k q_G: PASS')
# W of the raw-coordinate closure sum (-3*x^2,-3*x^2/2) is
# -(9+3*i*sqrt(3))*x^2/4; the linearly closed chart triple is not raw closed.
assert add(scale(h((x,zero)),2),h((-2*x,zero)))==(-3*x*x,-QQ(3,2)*x*x)
print('C15B explicit closure-set mismatch: PASS')

# Directly compute conjugated isolated return and projected triad for arbitrary k.
iso=jet([(x,y)],qsig,rsig,False)[0]
iso_raw=jet([(x,y)],q,r,False)[0]
assert iso==iso_raw
QG=lambda a:a[0]**2-a[0]*a[1]+a[1]**2
B=lambda a,b:a[0]*b[0]-(a[0]*b[1]+a[1]*b[0])/2+a[1]*b[1]
# W(J_Q s)=i W(s); no sqrt(3) in the matrix after multiplying sqrt(3).
J3=lambda a:(a[0]-2*a[1],2*a[0]-a[1])
assert iso==scale(add(scale((x,y),-QQ(1,2)),scale(J3((x,y)),-QQ(2,3))),QG((x,y)))
print('isolated mu = -1/2 - 2i sqrt(3)/3 independent of k: PASS')
S=(x,y); D=(z,w)
edges=(S,add(scale(S,-QQ(1,2)),D),sub(scale(S,-QQ(1,2)),D))
C=jet(edges,qsig,rsig,True)
C0=jet(edges,q,r,True)
assert tuple(sum(e[i] for e in C) for i in range(2))==(zero,zero)
# Reconstruct modal cubic from independently iterated edge jets.
cs=C[0]; cd=scale(sub(C[1],C[2]),QQ(1,2))
# Complex C10/C20 expression in real coordinates. S_area=(sqrt(3)/2)*K.
K=y*z-x*w; I=B(S,D); Qs=QG(S); Qc=QG(D); N=QQ(3,2)*Qs+2*Qc
nu_re=-QQ(1,2)+QQ(2,3)*k*k; nu_im_over_sqrt3=-QQ(2,3)+QQ(1,3)*k*k; chi=k*k/3
sep=project(tuple(scale(e,QG(e)) for e in edges))
expected=[]
for i in range(3):
    ch=scale(J3(sub(edges[(i+1)%3],edges[(i-1)%3])),chi*K/3)
    expected.append(add(add(scale(sep[i],nu_re),scale(J3(sep[i]),nu_im_over_sqrt3)),ch))
assert tuple(expected)==C
print('full projected six-step cubic for symbolic k (all 6 edge components): PASS')
# Radial and area derivatives at quartic degree, area divided by sqrt(3)/2.
dqs=2*B(S,cs); dqc=2*B(D,cd); di=B(cs,D)+B(S,cd)
dK=cs[1]*z-cs[0]*w+y*cd[0]-x*cd[1]; dN=QQ(3,2)*dqs+2*dqc
assert dN==nu_re*N*N+QQ(3,2)*K*K
assert dK==QQ(2,3)*(-QQ(1,2)+k*k)*N*K
assert N*N-9*K*K==(QQ(3,2)*Qs-2*Qc)**2+12*I*I
print('C20 norm/area quartic identities and sharp shape bound: PASS')
# k=1 raw exact C12 coefficients.
cs0=C0[0]; cd0=scale(sub(C0[1],C0[2]),QQ(1,2))
a=2*B(S,cs0); b=2*B(D,cd0); c=B(cs0,D)+B(S,cd0)
d=cs0[1]*z-cs0[0]*w+y*cd0[0]-x*cd0[1]
assert a==Qs**2/4+Qs*Qc/3+K**2/2-QQ(2,3)*I*K
assert b==Qs*Qc/4+Qc**2/3+QQ(3,8)*K**2+I*K/2
assert c==N*I/6+(Qs/4-Qc/3)*K
assert d==N*K/3
assert Qc*a+Qs*b-2*I*c-QQ(3,2)*K*d==0
print('C12 all signed-Gram coefficients and Gram differential: PASS')
# Exact reflection of primitive projected map follows from slot permutations;
# independently check reflection of the cubic as a regression control.
reflect=lambda p:p.compose(z,-z).compose(w,-w)
assert tuple(reflect(p) for p in cs0)==cs0
assert tuple(reflect(p) for p in cd0)==scale(cd0,-1)
print('cubic slot-2/3 reflection: PASS')
# Counterexample using the r^0 coefficient only, at both nonzero root branches.
Aq,Cq,Bi,Om=sp.symbols('Q_T Q_cT I_T Omega_T',real=True)
converted=2*((Aq/2)**2/4+(Aq/2)*(Cq/2)/3+sp.Rational(2,3)*(-Om/2)**2-sp.Rational(4,9)*sp.sqrt(3)*(Bi/2)*(-Om/2))
# A_q*C_q=B_i^2+Om^2, valid for the root-normalized planar pair.
modal=Aq**2/8+Bi**2/6+Om**2/2+2*sp.sqrt(3)*Bi*Om/9
assert sp.expand(converted-modal-(Aq*Cq-Bi**2-Om**2)/6)==0
print('C12 to T6d normalization using Gram constraint: PASS')
hist=-24*Aq**2+18*Bi*Aq-18*Bi**2-12*sp.sqrt(3)*Bi*Om+6*sp.sqrt(3)*Aq*Om-6*Om**2
assert sp.expand(modal.subs({Bi:-Bi,Om:-Om},simultaneous=True)-modal)==0
assert sp.expand(hist-hist.subs({Bi:-Bi,Om:-Om},simultaneous=True)-36*Bi*Aq-12*sp.sqrt(3)*Aq*Om)==0
# Qc_T=Q_T=1, I=0, Omega=+/-1 lies in the interior of the root radicand.
for sign in (1,-1):
    vals={Aq:1,Bi:0,Om:sign}
    m=sp.simplify(modal.subs(vals)); t=sp.simplify(hist.subs(vals))
    assert m==sp.Rational(5,8) and t.is_negative
    print('T6d r^0 witness sign=%+d: modal=%s, diagnostic=%s' % (sign,m,t))
print('All checks PASS; exact degree-three/four algebra only, no source script or reviewer script run.')
