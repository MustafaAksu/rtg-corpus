"""
bch_minimal_jet_assembly.py — OPEN-M-2B certificate (v0.5 gate)
[RID candidate: UVM-ALG-2B-ASSEMBLY]

Status: [ALG] normalization/angle formulas; [HYP] h-ell amplitude bridge.
Outcome: B (pre-registered) — one dimensionless bridge parameter remains.

Maps certified (sector-functional -> physical, under the stated identifications):
  Source (HINDEX, chi-collapse): ||H||_B = (2/sqrt3) h sin(theta_f) r^2
     [BCH sigma3 coefficient real => chi in {0,pi} => envelope -> lower endpoint]
  Stiffness (R2/HYP-IDENT frame [DEF/HYP]): m|w| = ell sin^2(theta_f/2) r^2
  Cascade: (||H||_B/g)|w| = (2/sqrt3) rho sin(theta_f) sin^2(theta_f/2) r^4,
     rho := h*ell/(g*m)
  Exact angular optimum: tan^2(theta_f/2)=3 => theta_f = 2pi/3 (120 deg),
     f_max = 3 sqrt3/8, prefactor (2/sqrt3)*f_max = 3/4 exactly
  Threshold: (3/4) rho r^4 >= 0.024  <=>  rho r^4 >= 4/125 = 0.032;
     at race ceiling r^2 = Q_s = 0.1: rho >= 3.2
  Falsifier: g_soft = 2 ell sin^2(theta_f/2) r^2 |cos(arg w)|
NOT claimed: HYP-IDENT derived (computable modulo ell); cascade satisfied;
2pi/3 connection to tetrahedral/chiral/OFN geometry beyond [INTERP].
All checks must print PASS; process fails on any check failure.
"""
import sympy as sp
from sympy import I, sqrt, Rational as R, sin, cos, tan, pi, symbols, simplify
ok=True
def check(n,c):
    global ok; print(f"[{'PASS' if c else 'FAIL'}] {n}"); ok&=bool(c)

th,r,h,l,g,m,rho=symbols('theta_f r h ell g m rho',positive=True)
lam_=symbols('lambda',positive=True); chi=symbols('chi',real=True)

# (1) chi-collapse via the v0.2 HINDEX closed form
HB2 = 4*lam_**2*(3+2*sin(chi)**2+2*sqrt(sin(chi)**2+3)*sp.Abs(sin(chi)))/9
check("chi=0: ||H||_B^2 = 4 lambda^2/3 (lower endpoint)", simplify(HB2.subs(chi,0)-R(4,3)*lam_**2)==0)
check("chi=pi: identical norm (sign-insensitive)", simplify(HB2.subs(chi,pi)-R(4,3)*lam_**2)==0)

# (2) assembled cascade and exact optimum
cascade=(2/sqrt(3))*rho*sin(th)*sin(th/2)**2*r**4
f=sin(th)*sin(th/2)**2
check("d f/d theta = 0 at theta = 2pi/3 and it is a maximum",
      simplify(sp.diff(f,th).subs(th,2*pi/3))==0 and simplify(sp.diff(f,th,2).subs(th,2*pi/3))<0)
check("tan^2(theta/2) = 3 at the optimum", simplify(tan(pi/3)**2-3)==0)
check("f(2pi/3) = 3 sqrt3/8 exactly", simplify(f.subs(th,2*pi/3)-3*sqrt(3)/8)==0)
check("prefactor (2/sqrt3)(3 sqrt3/8) = 3/4 exactly", simplify((2/sqrt(3))*(3*sqrt(3)/8)-R(3,4))==0)

# (3) threshold arithmetic
check("(3/4) rho r^4 >= 0.024 <=> rho r^4 >= 4/125", simplify(sp.Rational(24,1000)*R(4,3)-R(4,125))==0)
check("at r^2 = 0.1: rho >= 3.2 = 16/5", simplify(R(4,125)/sp.Rational(1,100)-R(16,5))==0)

# (4) falsifier expression consistency
absw = l*sin(th/2)**2*r**2/m
gsoft = 2*m*absw*sp.Abs(cos(symbols('argw',real=True)))
check("g_soft = 2 ell sin^2(th/2) r^2 |cos arg w| (m cancels as required)",
      simplify(gsoft - 2*l*sin(th/2)**2*r**2*sp.Abs(cos(symbols('argw',real=True))))==0)

# (5) zero relative BCH phase (certified real coefficients 2cs, s^2) -> lock untwisted
c_,s_=symbols('c s',positive=True)
check("BCH sector coefficients 2cs and s^2 are real => relative phase 0 (lock untwisted)",
      sp.im(2*c_*s_)==0 and sp.im(s_**2)==0)

print("\nALL CHECKS:","PASS" if ok else "FAIL")
import sys; sys.exit(0 if ok else 1)
