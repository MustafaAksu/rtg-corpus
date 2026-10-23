#!/usr/bin/env python3
"""
recog_r11_chart_ledger_cert.py — RECOG OPEN R11: h-chart ledger (RTG_RELATIONAL_RECOGNITION_DSN_v0.3.2, §6.14).

Owner inputs (RTG_DYADIC_OSCILLATOR_DSN_v6.4.10 §6.14, DYAD-ALG-NF6 / DYAD-THM-NF-REM): six-step normal-form jet in the
degree-six polynomial conjugacy chart W = h(z, zbar),
    J(z) = z + mu z^2 zbar + a32 z^3 zbar^2 + a05 zbar^5,
    mu = -1/2 - i 2sqrt3/3,  a32 = -97/432 + i 197sqrt3/324,  a05 = -49/8640 - i 307sqrt3/25920,
    |Fhat(z) - J(z)| <= C7 |z|^7  (C7 = 100 on |z| <= 1/20; 30 on |z| <= 1/40),
    h2 = -(1+i sqrt3)/12 z^2 - 1/3 z zbar + (1-i sqrt3)/24 zbar^2.

Derives the chart-native laws FROM J (finite-jet identities) and the transport of the canonical raw comparator FROM h;
transfers nothing from the archival Lie-gauge object (47/54, c_theta, a_1, a_2 are not used).

Checks:
 (1)  q-law:      |J|^2 = q - q^2 + [245/216 + 2 Re(a05 e^{-6i Theta})] q^3 + O(q^4);   245/216 = |mu|^2 + 2 Re a32
 (2)  Theta-law:  arg(J/z) = -tau q + [89 sqrt3/324 + Im(a05 e^{-6i Theta})] q^2 + O(q^3);   89 sqrt3/324 = Im(a32 - mu^2/2)
 (3)  chart quintic phase coefficient has the OPPOSITE sign to the archival c_theta = -119 sqrt3/648 (hence no transfer)
 (4)  245/216 != 47/54 (raw angular mean)
 (5)  comparator track A (NF-native) C_z = zbar_a z_b: exact (-I)-covariance identities
 (6)  comparator track B (transported canonical): conj(h(z_a)) h(z_b) = zbar_a z_b + conj(h2(z_a)) z_b + zbar_a h2(z_b) + O(4)
 (7)  Q_prim = |h(z)|^2 on the real ray = t^2 - 3t^3/4 + O(t^4)   (q != Q_prim beyond leading order)
 (8)  R9 budget: degree-7 contribution to Lambda <= 2 C7 q0^2;  leading |Lambda| <= 0.0076520 q0;  dominance threshold q0 < lead/(2 C7)
 (9)  canonical comparator covariance defect under the exact swap S_h = h∘(-I)∘h^{-1}: C_W(S_h t,S_h t) - C_W(t,t) = (3/2) t^3 + O(t^4)
      (numeric, with the independently reconstructed degree-6 h from the one-step homological equation)
"""
import sympy as sp, mpmath as mp, sys
s3 = sp.sqrt(3); I = sp.I
q, Th, t = sp.symbols('q Theta t', positive=True)
mu  = -sp.Rational(1,2) - I*2*s3/3
a32 = -sp.Rational(97,432) + I*197*s3/324
a05 = -sp.Rational(49,8640) - I*307*s3/25920
tau = 2*s3/3
ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}"); ok = ok and bool(cond)

E = sp.exp(-6*I*Th)
r = 1 + mu*q + (a32 + a05*E)*q**2
mod2 = sp.expand(r*sp.conjugate(r))
c3 = sp.simplify(sp.expand_complex(mod2.coeff(q,2)))
check("(1) q-law coefficient of q^3 = 245/216 + 2 Re(a05 e^{-6iTheta}); q^2 coefficient = -1",
      sp.simplify(sp.expand_complex(mod2.coeff(q,1)) + 1) == 0 and
      sp.simplify(c3 - (sp.Rational(245,216) + 2*sp.re(sp.expand_complex(a05*E)))) == 0)
check("    245/216 == |mu|^2 + 2 Re a32", sp.simplify(sp.re(sp.expand_complex(mu*sp.conjugate(mu))) + 2*sp.re(a32) - sp.Rational(245,216)) == 0)
logr = sp.series(sp.log(r), q, 0, 3).removeO()
th1 = sp.simplify(sp.im(sp.expand_complex(logr.coeff(q,1)))); th2 = sp.simplify(sp.im(sp.expand_complex(logr.coeff(q,2))))
check("(2) Theta-law: -tau q + [89sqrt3/324 + Im(a05 e^{-6iTheta})] q^2",
      sp.simplify(th1 + tau) == 0 and sp.simplify(th2 - (89*s3/324 + sp.im(sp.expand_complex(a05*E)))) == 0)
check("    89sqrt3/324 == Im(a32 - mu^2/2)", sp.simplify(sp.im(sp.expand_complex(a32 - mu**2/2)) - 89*s3/324) == 0)
check("(3) chart phase coefficient (+) has opposite sign to archival c_theta (-)", (89*s3/324 > 0) and (-119*s3/648 < 0))
check("(4) 245/216 != 47/54", sp.Rational(245,216) != sp.Rational(47,54))

za, zab, zb, zbb = sp.symbols('z_a zbar_a z_b zbar_b')
def h2(z, zc): return -(1+I*s3)/12*z**2 - sp.Rational(1,3)*z*zc + (1-I*s3)/24*zc**2
def h2c(z, zc): return -(1-I*s3)/12*zc**2 - sp.Rational(1,3)*z*zc + (1+I*s3)/24*z**2     # conj(h2) with z<->zbar
Cz = zab*zb
check("(5) C_z: C_z(-a,-b) = C_z(a,b) and C_z(-a,b) = -C_z(a,b)", sp.simplify((-zab)*(-zb) - Cz) == 0 and sp.simplify((-zab)*zb + Cz) == 0)
CW = sp.expand((zab + h2c(za, zab))*(zb + h2(zb, zbb)))
target = sp.expand(zab*zb + h2c(za, zab)*zb + zab*h2(zb, zbb))
mons = sp.Poly(sp.expand(CW - target), za, zab, zb, zbb).monoms()
check("(6) transported comparator = zbar_a z_b + conj(h2(z_a)) z_b + zbar_a h2(z_b) + O(4)", all(sum(m) >= 4 for m in mons))
hz = t + h2(t, t); Qp = sp.expand(sp.simplify(hz*sp.conjugate(hz)))
check("(7) Q_prim(real ray) = t^2 - 3t^3/4 + O(t^4)", sp.simplify(sp.series(Qp, t, 0, 4).removeO() - (t**2 - 3*t**3/4)) == 0)
lead = sp.Abs((17+4*I*tau)/49*a05)
check("(8) leading amplitude coefficient 0.0076520", abs(sp.N(lead, 8) - 0.0076520) < 1e-6)
for c7 in (100, 30): print(f"    dominance threshold q0 < {sp.N(lead/(2*c7), 6)}  (C7={c7})")

mp.mp.dps = 40; DEG = 6
def mul(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            if i+j+k+l<=DEG: C[(i+k,j+l)]=C.get((i+k,j+l),0)+a*b
    return C
def add(A,B,s=1):
    C=dict(A)
    for k,v in B.items(): C[k]=C.get(k,0)+s*v
    return C
def scal(A,s): return {k:v*s for k,v in A.items()}
def powr(A,n):
    R={(0,0):mp.mpc(1)}
    for _ in range(n): R=mul(R,A)
    return R
def compose(F,G):
    out=[]
    for f in F:
        R={}
        for (i,j),c in f.items(): R=add(R,scal(mul(powr(G[0],i),powr(G[1],j)),c))
        out.append(R)
    return out
def conjpoly(A): return {(j,i):mp.conj(v) for (i,j),v in A.items()}
s3n=mp.sqrt(3); om=mp.mpc(-0.5,s3n/2); omb=mp.conj(om)
Z={(1,0):mp.mpc(1)}; Zb={(0,1):mp.mpc(1)}
eta=scal(add(Z,Zb,-1),1/(om-omb)); rho=add(Z,scal(eta,-om))
fac=lambda n: mp.factorial(n)
se=add(add(eta,scal(powr(eta,3),-1/fac(3))),scal(powr(eta,5),1/fac(5)))
er={}
for n in range(1,DEG+1): er=add(er,scal(powr(rho,n),1/fac(n)))
rho1=add(rho,se,-1); eta1=add(add(eta,er),se,-1)
F1=add(rho1,scal(eta1,om))
lam=mp.exp(1j*mp.pi/3); lamb=mp.conj(lam)
h=dict(Z); nmap={(1,0):lam}
for k in range(2,7):
    lhs=compose([F1],[h,conjpoly(h)])[0]; rhs=compose([h],[nmap,conjpoly(nmap)])[0]
    K={kk:v for kk,v in add(lhs,rhs,-1).items() if sum(kk)==k}
    for (a,b),v in K.items():
        if (a-b-1)%6==0: nmap[(a,b)]=nmap.get((a,b),0)+v
        else: h[(a,b)]=h.get((a,b),0)+(-v)/(lam-lam**a*lamb**b)
def evalp(A, w): return sum(c*w**i*mp.conj(w)**j for (i,j),c in A.items())
def hinv(w, it=80):
    zz = w
    for _ in range(it): zz = w - (evalp(h, zz) - zz)
    return zz
def Sh(w): return evalp(h, -hinv(w))
tt = mp.mpf('1e-3'); defect = abs(Sh(tt))**2 - tt**2
check("(9) C_W(S_h t,S_h t) - C_W(t,t) = (3/2) t^3 + O(t^4)", abs(defect/tt**3 - 1.5) < 5e-3)
print("    defect/t^3 =", mp.nstr(defect/tt**3, 8))
print("CERTIFICATE PASS" if ok else "CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
