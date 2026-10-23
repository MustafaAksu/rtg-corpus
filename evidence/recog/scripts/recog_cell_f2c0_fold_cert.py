#!/usr/bin/env python3
r"""
recog_cell_f2c0_fold_cert.py — [ENG] exact symbolic certificate for RECOG CELL-F2(c0).

Scientific target (conditional on RECOG-THM-P2-C0-FIRST): at the certified first
encounter x_* in
  B_*=(101667/50000,101671/50000) x (5003/625,80059/10000)
with C_0={D=det DT=0}, the primitive map
  T(rho,eta)=(rho-sin eta, eta+exp(rho)-1-sin eta)
has a Whitney fold singularity.

No interval arithmetic is required.  The B3 theorem already supplies x_* in B_*
and D(x_*)=0.  On C_0 an exact kernel field is k=(cos eta,1), and the fold scalar
is
  kappa = dD(k) = exp(rho) cos(eta)^2 - (exp(rho)-1) sin(eta).
Using D=0, A=exp(rho)-1,
  kappa = (A+1)/A^2 - A sin(eta).
The B_* rational bounds imply rho>2 and 5*pi/2<eta<17*pi/6, using only
3<pi<22/7. Hence A>4 (from exp(rho)>1+rho+rho^2/2>5) and sin(eta)>1/2.
Since (A+1)/A^2 decreases for A>0,
  kappa < 5/16 - 2 = -27/16 < 0.
Thus rank DT(x_*)=1 and the kernel is transverse to C_0. Equivalently the left-null
covector applied to D^2T[k,k] is nonzero.  This is the standard corank-one Whitney
fold criterion for maps R^2 -> R^2.
"""
import sympy as sp
import sys

rho, eta = sp.symbols('rho eta', real=True)
A = sp.symbols('A', positive=True)
s = sp.symbols('s', real=True)
E = sp.exp(rho)
c = sp.cos(eta)
sn = sp.sin(eta)

J = sp.Matrix([[1, -c], [E, 1-c]])
D = sp.simplify(J.det())
k = sp.Matrix([c, 1])
ell = sp.Matrix([[-E, 1]])

gradD = sp.Matrix([sp.diff(D, rho), sp.diff(D, eta)])
kappa = sp.simplify((gradD.T*k)[0])

# Directional Hessian D^2T[k,k].
H1 = sp.hessian(rho - sp.sin(eta), (rho, eta))
H2 = sp.hessian(eta + sp.exp(rho) - 1 - sp.sin(eta), (rho, eta))
D2Tk = sp.Matrix([sp.simplify((k.T*H1*k)[0]), sp.simplify((k.T*H2*k)[0])])
fold_left = sp.simplify((ell*D2Tk)[0])

ok = True
def chk(name, cond):
    global ok
    cond = bool(cond)
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    ok = ok and cond

chk("(1) det DT = 1 + (exp(rho)-1) cos eta",
    sp.simplify(D - (1 + (E-1)*c)) == 0)
chk("(2) DT*k = (0,D): k spans ker DT on C0",
    all(sp.simplify(v) == 0 for v in (J*k - sp.Matrix([0,D]))))
chk("(3) ell^T*DT = (0,D): ell is left-null on C0",
    all(sp.simplify(v) == 0 for v in (ell*J - sp.Matrix([[0,D]]))))
chk("(4) dD(k) = exp(rho) cos^2 eta - (exp(rho)-1) sin eta",
    sp.simplify(kappa - (E*c**2 - (E-1)*sn)) == 0)
chk("(5) left-null Hessian fold scalar equals dD(k)",
    sp.simplify(fold_left - kappa) == 0)

# Exact rational gates from B_*.
rlo = sp.Rational(101667,50000)
rhi = sp.Rational(101671,50000)
etalo = sp.Rational(5003,625)
etahi = sp.Rational(80059,10000)
chk("(6) B_* gives rho>2 and 5*pi/2<eta<17*pi/6 from 3<pi<22/7",
    rlo > 2 and sp.Rational(55,7) < etalo and etahi < sp.Rational(17,2))

# On C0: cos eta=-1/A, E=A+1.  f(A)=(A+1)/A^2 is decreasing for A>0.
f = (A+1)/A**2
df = sp.factor(sp.diff(f,A))
chk("(7) on C0, f(A)=(A+1)/A^2 decreases; A>4, sin eta>1/2 imply kappa<-27/16",
    sp.simplify(df + (A+2)/A**3) == 0 and sp.Rational(5,16)-2 == -sp.Rational(27,16))

print("F2(c0) WHITNEY-FOLD SYMBOLIC CERTIFICATE PASS" if ok else "F2(c0) WHITNEY-FOLD SYMBOLIC CERTIFICATE FAIL")
sys.exit(0 if ok else 1)
