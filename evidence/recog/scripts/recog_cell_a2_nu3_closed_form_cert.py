#!/usr/bin/env python3
"""
recog_cell_a2_nu3_closed_form_cert.py — RECOG CELL-A2: closed form and zero set of nu_3^{(1,p)}.

For the p-resonant primitive family
    rho' = rho - sin eta,   eta' = eta + K(e^rho - 1) - K sin eta,   K = 2 - lam - 1/lam,
in the eigenframe  rho = uZ + conj(u) conj(Z),  eta = Z + conj(Z),  u = 1/(1-lam),
the one-step h_2-normalised resonant cubic coefficient depends on lam alone:

    nu_3(lam) = -(lam^5 - lam^4 - lam^3 - 2 lam^2 + 1) / ( 2 (lam-1)(lam+1)(lam^2+lam+1) ).

Checks
 (1) closed form reproduces the exact certified nu_3^{(1,5)} and nu_3^{(1,7)} (exact, mod Phi_p),
 (2) p=6: 6*conj(lam)*nu_3 equals exactly 3 * mu_6^{W-frame} (frame scale factor |c|^2 = 1/3),
 (3) numerator N(lam) has no root on the unit circle: gcd(N, lam^5 N(1/lam)) = 1 and all numeric roots have |root| != 1,
 (4) gcd(N, Phi_p) = 1 for every p with phi(p) <= 5 (the only p for which a root of unity of order p could be a root of a degree-5 integer polynomial),
 (5) raw p-fold composition (independent route) agrees with p*conj(lam)*nu_3(lam) for p = 5..12,
 (6) Re(conj(lam) nu_3(e^{i theta})) = -theta^2/4 + theta^4/48 + O(theta^5)  and is negative on a fine mesh of (0, 2pi/5].

Consequences (see RECOG ledger): nu_3^{(1,p)} != 0 for every p >= 5, hence k_ret(p) = 3 for the whole
p-resonant family; the frame-invariant sign Re mu_p < 0 holds for all sampled p, with Re mu_p ~ -pi^2/p.
"""
import sympy as sp, mpmath as mp, sys
L = sp.symbols('lam'); Lb = 1/L
K = 2 - L - Lb; u = 1/(1-L); ub = 1/(1-Lb)
ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}"); ok = ok and bool(cond)

# ---- symbolic h2 normalisation -------------------------------------------------
def add(A,B,s=1):
    C=dict(A)
    for k,v in B.items(): C[k]=C.get(k,0)+s*v
    return C
def mul(A,B,deg=3):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            if i+j+k+l<=deg: C[(i+k,j+l)]=C.get((i+k,j+l),0)+a*b
    return C
def scal(A,s): return {k:v*s for k,v in A.items()}
def powr(A,n):
    R={(0,0):sp.Integer(1)}
    for _ in range(n): R=mul(R,A)
    return R
def deg(A,d): return {k:v for k,v in A.items() if sum(k)==d}
def dZ(A): return {(i-1,j):v*i for (i,j),v in A.items() if i>0}
def dW(A): return {(i,j-1):v*j for (i,j),v in A.items() if j>0}
def at_Lam(A): return {k:v*L**k[0]*Lb**k[1] for k,v in A.items()}
def Ddot_Lam(h,vZ,vW): return add(scal(mul(dZ(at_Lam(h)),vZ),Lb),scal(mul(dW(at_Lam(h)),vW),L))
Zp={(1,0):sp.Integer(1)}; Wp={(0,1):sp.Integer(1)}
rho=add(scal(Zp,u),scal(Wp,ub)); eta=add(Zp,Wp)
se=add(eta,scal(powr(eta,3),-sp.Rational(1,6)))
er=add(add(rho,scal(powr(rho,2),sp.Rational(1,2))),scal(powr(rho,3),sp.Rational(1,6)))
rho1=add(rho,se,-1); eta1=add(add(eta,scal(er,K)),scal(se,-K))
FZ={k:sp.cancel(v) for k,v in scal(add(rho1,scal(eta1,ub),-1),1/(u-ub)).items()}
FW={k:sp.cancel(v) for k,v in scal(add(scal(eta1,u),rho1,-1),1/(u-ub)).items()}
F2Z,F3Z,F2W=deg(FZ,2),deg(FZ,3),deg(FW,2)
h2Z={k:sp.cancel(v/(L**(k[0]-k[1])-L)) for k,v in F2Z.items()}
h2W={k:sp.cancel(v/(L**(k[0]-k[1])-Lb)) for k,v in F2W.items()}
Y2Z=add(scal(h2Z,L),F2Z); Y2W=add(scal(h2W,Lb),F2W)
Y3Z=add(add(mul(dZ(F2Z),h2Z),mul(dW(F2Z),h2W)),F3Z)
G3Z=add(add(Y3Z, Ddot_Lam(h2Z,Y2Z,Y2W),-1), Ddot_Lam(h2Z,at_Lam(h2Z),at_Lam(h2W)))
nu3 = sp.factor(sp.cancel(G3Z[(2,1)]))
claimed = -(L**5-L**4-L**3-2*L**2+1)/(2*(L-1)*(L+1)*(L**2+L+1))
check("closed form nu_3(lam) as stated", sp.simplify(nu3-claimed)==0)
N = L**5-L**4-L**3-2*L**2+1

# (1) exact agreement with certified p=5, p=7 values, modulo Phi_p
def exact_eq_mod_phi(expr, p):
    num, den = sp.fraction(sp.cancel(expr))
    return sp.rem(sp.expand(num), sp.cyclotomic_poly(p, L), L) == 0
check("p=5: nu_3 == (12 - lam + lam^2 + 8 lam^3)/10  mod Phi_5", exact_eq_mod_phi(nu3-(12-L+L**2+8*L**3)/10, 5))
check("p=7: nu_3 == (12 - 4lam + lam^2 + 6lam^3 - 3lam^4 + 9lam^5)/14  mod Phi_7", exact_eq_mod_phi(nu3-(12-4*L+L**2+6*L**3-3*L**4+9*L**5)/14, 7))
# (2) p=6 frame check
mu6W = -sp.Rational(1,2) - sp.I*2*sp.sqrt(3)/3
z6 = sp.exp(2*sp.pi*sp.I/6)
check("p=6: 6 conj(lam) nu_3 == 3 * mu_6^{W}", sp.simplify(sp.expand_complex(6*nu3.subs(L,z6)/z6 - 3*mu6W))==0)
# (3) no unit-circle roots
Nrev = sp.expand(L**5*N.subs(L,1/L))
roots = sp.Poly(N,L).nroots(n=30)
check("gcd(N, reciprocal N) = 1", sp.gcd(N,Nrev)==1)
check("no numeric root of N on |lam|=1", all(abs(abs(r)-1) > 1e-6 for r in roots))
# (4) cyclotomic candidates
check("gcd(N, Phi_p)=1 for p with phi(p)<=5", all(sp.gcd(N, sp.cyclotomic_poly(p,L))==1 for p in [1,2,3,4,5,6,8,10,12]))
# (5) raw composition cross-check p=5..12
mp.mp.dps = 40
def mu_raw(p):
    lam=mp.exp(2j*mp.pi/p); lb=mp.conj(lam); Kn=2-lam-lb; un=1/(1-lam); ubn=mp.conj(un)
    def madd(A,B,s=1):
        C=dict(A)
        for k,v in B.items(): C[k]=C.get(k,0)+s*v
        return C
    def mmul(A,B):
        C={}
        for (i,j),a in A.items():
            for (k,l),b in B.items():
                if i+j+k+l<=3: C[(i+k,j+l)]=C.get((i+k,j+l),0)+a*b
        return C
    def mscal(A,s): return {k:v*s for k,v in A.items()}
    def mpow(A,n):
        R={(0,0):mp.mpc(1)}
        for _ in range(n): R=mmul(R,A)
        return R
    Z1={(1,0):mp.mpc(1)}; W1={(0,1):mp.mpc(1)}
    r=madd(mscal(Z1,un),mscal(W1,ubn)); e=madd(Z1,W1)
    s_=madd(e,mscal(mpow(e,3),-mp.mpf(1)/6)); x_=madd(madd(r,mscal(mpow(r,2),mp.mpf(1)/2)),mscal(mpow(r,3),mp.mpf(1)/6))
    r1=madd(r,s_,-1); e1=madd(madd(e,mscal(x_,Kn)),mscal(s_,-Kn))
    F=[mscal(madd(r1,mscal(e1,ubn),-1),1/(un-ubn)), mscal(madd(mscal(e1,un),r1,-1),1/(un-ubn))]
    def comp(F,G):
        out=[]
        for f in F:
            R={}
            for (i,j),c in f.items(): R=madd(R,mscal(mmul(mpow(G[0],i),mpow(G[1],j)),c))
            out.append(R)
        return out
    G=F
    for _ in range(p-1): G=comp(F,G)
    D=madd(G[0],Z1,-1)
    return D[(2,1)], lam
nu3f = sp.lambdify(L, nu3, 'mpmath')
agree = True; signs = True
for p in range(5,13):
    m, lam = mu_raw(p)
    agree = agree and abs(m - p*mp.conj(lam)*nu3f(lam)) < mp.mpf('1e-30')
    signs = signs and mp.re(m) < 0
check("raw p-fold composition == p conj(lam) nu_3(lam), p=5..12", agree)
check("Re mu_p < 0 for p=5..12 (frame-invariant sign)", signs)
# (6) small-theta series and sign on (0, 2pi/5]
th = sp.symbols('theta', real=True)
g = sp.simplify((nu3/L).subs(L, sp.exp(sp.I*th)))
ser = sp.nsimplify(sp.expand(sp.simplify(sp.series(g, th, 0, 5).removeO())))
check("Re(conj(lam) nu_3) = -theta^2/4 + theta^4/48 + O(theta^5)", sp.simplify(sp.re(ser) - (-th**2/4 + th**4/48)) == 0)
gf = sp.lambdify(th, g, 'mpmath')
check("Re(conj(lam) nu_3) < 0 on mesh of (0, 2pi/5]", max(mp.re(gf(mp.mpf(k)/4000*2*mp.pi/5)) for k in range(1,4001)) < 0)
print("nu_3(lam) =", claimed)
print("CERTIFICATE PASS" if ok else "CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
