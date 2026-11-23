#!/usr/bin/env python3
"""triad_orientation_normalization_audit.py  -- exit-code-gated.

Audits the orientation normalization of the historical Triadic T-6 producers
(t6c2 / t6e / t6f / t6i / t6l, as archived in triad_t6_producers.zip, manifest
SHA256s recorded by the PI 2026-09-30). Polynomials are transcribed verbatim from
triad_direct_orientation_ode_t6f.py (identical to t6i / t6l / t6k / t6h_v2 copies).

Certifies:
 N1  Producer metric: B_dot = [[2,-1],[-1,2]] = 2*B_Genesis; with the t6c2 axis
     substitution, Q_s Q_c - I^2 = Omega^2 exactly and omega_raw := s_eta c_rho -
     s_rho c_eta = -Omega/sqrt3.  (T-6d root closure is CONSISTENT with T-6c2.)
 N2  Gram-identity test: the T-6e increment w (Delta of omega_raw) relates to the
     closure variable by Delta Omega = -sqrt3 * w at r^0, r^1, r^2 (all orders).
 N3  Replication: integrating w as Delta Omega (as t6l did) reproduces
     x* = 0.0962741296 exactly.
 N4  Corrected torsion (Delta Omega = -sqrt3 w): leading large-u coefficient is
     proportional to (mu^2+nu^2)(sqrt3 mu^2 + 2 mu nu + 3 sqrt3 nu^2), which has no
     real root: no torsion wedge exists.
 N5  Corrected boundary radial flow K-dot on K=1 vanishes identically (all r).
 N6  Original (uncorrected) boundary K-dot is nonzero: the T-6i/T-6i2 sector map
     is an artifact of the -sqrt3 factor.
Scope: leading-degree ledger algebra of the archived producers; no new ODE run.
"""
import sys, sympy as sp
F=[]
def check(n,c):
    ok=bool(c); print(('PASS ' if ok else 'FAIL ')+n); F.append(n) if not ok else None
s3=sp.sqrt(3)
# N1
sr,ce,cr,Qs,I,W=sp.symbols('s_rho c_eta c_rho Q_s I_sc Omega',real=True)
M=sp.Matrix([[2,-1],[-1,2]]); Bg=sp.Matrix([[1,-sp.Rational(1,2)],[-sp.Rational(1,2),1]])
check('N1a producer metric = 2*B_Genesis', M==2*Bg)
srs=sp.sqrt(Qs/2); ces=W/(s3*srs); crs=(ces+I/srs)/2
S=sp.Matrix([srs,0]); C=sp.Matrix([crs,ces])
q=lambda a,b:(a.T*M*b)[0]
check('N1b axis subs: B(S,S)=Q_s, B(S,C)=I', sp.simplify(q(S,S)-Qs)==0 and sp.simplify(q(S,C)-I)==0)
check('N1c Q_s Q_c - I^2 = Omega^2 (root closure consistent)', sp.simplify(q(S,S)*q(C,C)-I**2-W**2)==0)
check('N1d omega_raw = -Omega/sqrt3', sp.simplify((0*crs - srs*ces)+W/s3)==0)
# ledger
def L(I,W,Qs):
    return dict(
    I=[(3/Qs)*(-7*I**3-3*s3*I**2*W-7*I*W**2+Qs*(6*I**2-7*I*Qs+3*s3*Qs*W+2*W**2)-3*s3*W**3),
       (-3*sp.sqrt(42)*I**2-6*sp.sqrt(14)*I*W+3*Qs*(-sp.sqrt(42)*I+7*sp.sqrt(14)*W)+7*sp.sqrt(42)*W**2)/(7*sp.sqrt(Qs)),
       -sp.Rational(26,7)*I+20*s3/7*W],
    w=[(-3*I**3+5*s3*I**2*W-3*I*W**2+Qs*(3*I*Qs-4*s3*I*W+5*s3*Qs*W)+5*s3*W**3)/Qs,
       (-7*sp.sqrt(42)*I**2+10*sp.sqrt(14)*I*W+Qs*(7*sp.sqrt(42)*I+3*sp.sqrt(14)*W)-5*sp.sqrt(42)*W**2)/(7*sp.sqrt(Qs)),
       10*s3*W/3],
    Qs=[-18*I**2+18*I*Qs-12*s3*I*W-24*Qs**2+6*s3*Qs*W-6*W**2,-6*sp.sqrt(42)*Qs**sp.Rational(3,2)/7,-sp.Rational(26,7)*Qs],
    Qc=[6*(-4*I**4-8*I**2*W**2+Qs**2*(-3*I**2+2*s3*I*W-W**2)+Qs*(3*I**3-s3*I**2*W+3*I*W**2-s3*W**3)-4*W**4)/Qs**2,
        6*(-sp.sqrt(42)*I**3+5*sp.sqrt(14)*I**2*W-sp.sqrt(42)*I*W**2+5*sp.sqrt(14)*W**3)/(7*Qs**sp.Rational(3,2)),
        2*(-13*I**2+20*s3*I*W-57*W**2)/(7*Qs)])
D=L(I,W,Qs); Qcv=(I**2+W**2)/Qs
for k in range(3):
    rhs=Qcv*D['Qs'][k]+Qs*D['Qc'][k]-2*I*D['I'][k]
    check(f'N2 r^{k}: Delta Omega = -sqrt3*w satisfies Gram identity', sp.simplify(2*W*(-s3)*D['w'][k]-rhs)==0)
    check(f'N2 r^{k}: Delta Omega = w violates it', sp.simplify(2*W*D['w'][k]-rhs)!=0)
# N3/N4
u,mu,nu,x,v=sp.symbols('u mu nu x v',positive=True); mu,nu,x=sp.symbols('mu nu x',real=True)
Dl=L(mu*sp.sqrt(u)*Qs,nu*sp.sqrt(u)*Qs,Qs)
def lead(fac):
    num=mu*fac*Dl['w'][0]-nu*Dl['I'][0]
    tv=sp.expand(sp.simplify((num/(Qs**2*sp.sqrt(u))).subs(sp.sqrt(u),v).subs(u,v**2)))
    return sp.factor(sp.Poly(tv,v).coeff_monomial(v**2))
lo=lead(1); rp=sp.solve(sp.simplify(lo.subs(nu,x*mu)/mu**2),x)
xs=[r for r in rp if r.is_real and float(r)>0]
check('N3 replication x* = 0.0962741296', len(xs)==1 and abs(float(xs[0])-0.0962741296)<1e-9)
lc=lead(-s3)
check('N4a corrected leading torsion = 3K(sqrt3 mu^2 + 2 mu nu + 3sqrt3 nu^2)', sp.simplify(lc-3*(mu**2+nu**2)*(s3*mu**2+2*mu*nu+3*s3*nu**2))==0)
check('N4b no real wedge root (discriminant 4-36<0)', sp.discriminant(s3+2*x+3*s3*x**2,x)<0)
# N5/N6
rho,th=sp.symbols('rho theta',real=True)
Dk=L(mu*sp.sqrt(u)*Qs,nu*sp.sqrt(u)*Qs,Qs); r=rho*sp.sqrt(Qs)
tot=lambda t:t[0]+r*t[1]+r**2*t[2]
def Kdot(fac):
    md=tot(Dk['I'])/(Qs*sp.sqrt(u))-mu*tot(Dk['Qs'])/(2*Qs)-mu*tot(Dk['Qc'])/(2*u*Qs)
    nd=fac*tot(Dk['w'])/(Qs*sp.sqrt(u))-nu*tot(Dk['Qs'])/(2*Qs)-nu*tot(Dk['Qc'])/(2*u*Qs)
    return sp.simplify((2*mu*md+2*nu*nd).subs({mu:sp.cos(th),nu:sp.sin(th)}))
check('N5 corrected boundary K-dot == 0 (all r)', sp.simplify(Kdot(-s3))==0)
ko=Kdot(1); val=float(ko.subs({Qs:0.7,u:12.8,rho:0.36,th:0.6}))
check('N6 original boundary K-dot nonzero (artifact)', abs(val)>1)
print('='*50)
if F: print('FAILED:',F); sys.exit(1)
print('ALL PASS: orientation increment was raw; corrected model has invariant K=1 and no torsion wedge.')
sys.exit(0)
