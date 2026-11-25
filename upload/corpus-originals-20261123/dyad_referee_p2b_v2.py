#!/usr/bin/env python3
"""
dyad_referee_p2b_v2.py — reviewer's executable referee harness for P2-A v2 / P2-B v2.

Independent reconstruction (does not import any producer/validator code):
  * builds the one-step primitive map f = L∘T∘L^{-1} in exact Q(i√3) from T(ρ,η) = (ρ − sin η, η + e^ρ − 1 − sin η)
  * composes it six times to total degree 9
  * solves the one-step homological equation for the degree-6 normalizer h (resonant h_n = 0)
  * recomputes every ceiling, tail, domain closure and both radius-indexed profiles
Every check is an assert; exit code 1 on any failure. Floats appear only where explicitly
labeled as a non-certificate display (modulus sums are compared with 1e-12 slack against the
rational ceilings; a certificate-grade version replaces them by rational square-root enclosures).
Backend: dyad_return_qchi_exact.py (must be importable as qchi).
"""
import sys, math
from fractions import Fraction as Fr
import mpmath as mp, sympy as sp
try:
    from qchi import Q, P
except ImportError:
    from dyad_return_qchi_exact import Q, P
mp.mp.dps = 60
FAIL = []
def check(name, cond, info=""):
    print(f"[{'PASS' if cond else 'FAIL'}] {name} {info}")
    if not cond: FAIL.append(name)

# ---------- 1. exact jet to degree 9 ----------
N = 9
om = Q(Fr(-1,2), Fr(1,2)); inv_chi = Q(0, Fr(-1,3)); lam = Q(Fr(1,2), Fr(1,2)); lamb = lam.conj()
z = P({(1,0):Q(1)},N); zb = P({(0,1):Q(1)},N); one = P({(0,0):Q(1)},N)
eta = (z-zb).scale(inv_chi); rho = z - eta.scale(om)
def ssin(x):
    r = P({},N)
    for k in range(5):
        n = 2*k+1
        if n <= N: r = r + x.pw(n).scale(Q(Fr((-1)**k, math.factorial(n))))
    return r
def sexpm1(x):
    r = P({},N); xp = one
    for k in range(1,N+1): xp = xp*x; r = r + xp.scale(Q(Fr(1, math.factorial(k))))
    return r
f = (rho - ssin(eta)) + (eta + sexpm1(rho) - ssin(eta)).scale(om)
g, gb = f, f.conj()
for _ in range(5): g, gb = f.compose(g,gb), f.conj().compose(g,gb)
FW = g
check("one-step nonzero coeffs through deg 9 == 48", len(f.d)==48, len(f.d))
check("six-step nonzero coeffs through deg 9 == 46", len(FW.d)==46, len(FW.d))
check("six-step F_2 == 0", len(FW.deg(2).d)==0)
check("mu == -1/2 - 2i√3/3", FW.get((2,1))==Q(Fr(-1,2),Fr(-2,3)))
def modsum(poly): return sum(math.sqrt(float(v.a)**2+3*float(v.b)**2) for v in poly.d.values())
b7,b8,b9 = modsum(FW.deg(7)), modsum(FW.deg(8)), modsum(FW.deg(9))
check("deg-7 vector sum <= 2079/1000", b7 <= 2.079+1e-12, f"{b7:.9f}")
check("deg-8 vector sum <= 577/500",   b8 <= 1.154+1e-12, f"{b8:.9f}")
check("deg-9 vector sum <= 1763/1000", b9 <= 1.763+1e-12, f"{b9:.9f}")
# radial exact degrees (P2-A v2)
FW7 = P(FW.d,7); Qf = FW7*FW7.conj()
check("radial deg4 == -Q^2", Qf.get((2,2))==Q(-1) and len(Qf.deg(4).d)==1)
check("radial (3,3) coefficient of ΔQ6 == 47/54", Qf.get((3,3))==Q(Fr(47,54)))
D5,D6,D7 = modsum(Qf.deg(5)), modsum(Qf.deg(6)), modsum(Qf.deg(7))
check("|P5| ceiling 16931/10000", D5<=1.6931+1e-12, f"{D5:.9f}")
check("|P6| ceiling 6671/5000",   D6<=1.3342+1e-12, f"{D6:.9f}")
check("|P7| ceiling 3567/1000",   D7<=3.567+1e-12,  f"{D7:.9f}")

# ---------- 2. normalizer h from the homological equation ----------
def lampow(a,b):
    r=Q(1)
    for _ in range(a): r=r*lam
    for _ in range(b): r=r*lamb
    return r
h = P({(1,0):Q(1)},N); n = P({(1,0):lam},N)
for k in range(2,7):
    K = (f.compose(h,h.conj()) - h.compose(n,n.conj())).deg(k)
    hk={}; nk={}
    for (a,b),v in K.d.items():
        if (a-b-1)%6==0: nk[(a,b)]=v
        else: hk[(a,b)] = (v*Q(-1))/(lam - lampow(a,b))
    h = h+P(hk,N); n = n+P(nk,N)
check("h2 == -(1+i√3)/12 z^2 - 1/3 z zb + (1-i√3)/24 zb^2",
      h.get((2,0))==Q(Fr(-1,12),Fr(-1,12)) and h.get((1,1))==Q(Fr(-1,3)) and h.get((0,2))==Q(Fr(1,24),Fr(-1,24)))
check("n21 == 1/8 - 7i√3/72", n.get((2,1))==Q(Fr(1,8),Fr(-7,72)))
check("n32 == -5/432 + 23i√3/3888", n.get((3,2))==Q(Fr(-5,432),Fr(23,3888)))
check("n05 == 43/17280 - 227i√3/155520", n.get((0,5))==Q(Fr(43,17280),Fr(-227,155520)))
check("nonzero h coefficients (incl. linear) == 23", len(h.d)==23, len(h.d))
mu=Q(Fr(-1,2),Fr(-2,3)); a32=Q(Fr(-97,432),Fr(197,324)); a05=Q(Fr(-49,8640),Fr(-307,25920))
# NOTE: a32 != 6·conj(λ)·n32 in general — the (3,2) slot of n∘6 carries second-order n21 cross terms.
# The bridge lemma holds for μ and for the (0,5) lattice slot only. Correct check: J_<=5 (n∘6) == J.
n6=n; n6b=n.conj()
for _ in range(5): n6,n6b=n.compose(n6,n6b),n.conj().compose(n6,n6b)
n6_5=P({k:v for k,v in n6.d.items() if sum(k)<=5},N)
J5=P({(1,0):Q(1),(2,1):mu,(3,2):a32,(0,5):a05},N)
check("J_<=5(n∘6) == z + μ z²z̄ + a32 z³z̄² + a05 z̄⁵", all((n6_5.get(k)-J5.get(k)).iszero() for k in set(n6_5.d)|set(J5.d)))
check("μ == 6·conj(λ)·n21 (bridge lemma, cubic slot)", (n.get((2,1))*lamb*Q(6))==mu)
check("a05 == 6·conj(λ)·n05", (n.get((0,5))*lamb*Q(6))==a05)
J = P({(1,0):Q(1),(2,1):mu,(3,2):a32,(0,5):a05},N)
Pj = P({k:v for k,v in FW.d.items() if sum(k)<=6},N)
Dp = Pj.compose(h,h.conj()) - h.compose(J,J.conj())
check("D_poly vanishes through degree 6", all(sum(k)>6 for k in Dp.d))
check("[D_poly]_(0,7) == 31/9720 - 77i√3/19440", Dp.get((0,7))==Q(Fr(31,9720),Fr(-77,19440)))
Mc = {k: modsum(h.deg(k)) for k in range(2,7)}
for k,c in {2:Fr(7,12),3:Fr(39,500),4:Fr(14,125),5:Fr(11,250),6:Fr(1,20)}.items():
    check(f"M(s) ceiling deg {k} = {c}", Mc[k] <= float(c)+1e-12, f"{Mc[k]:.6f}")

# ---------- 3. majorant, tails, profiles ----------
a=Fr(7,6); NM=10
def compose_psi(S):
    out=[Fr(0)]*(NM+1)
    for i,c in enumerate(S): out[i]+=c
    Pp=[Fr(0)]*(NM+1); Pp[0]=Fr(1)
    for nn in range(1,NM+1):
        Qc=[Fr(0)]*(NM+1)
        for i,x in enumerate(Pp):
            if x==0: continue
            for j,y in enumerate(S):
                if y==0 or i+j>NM: continue
                Qc[i+j]+=x*y
        Pp=Qc
        if nn>=2:
            pc=Fr(1+(nn%2),math.factorial(nn))*a**nn
            for kk in range(NM+1): out[kk]+=pc*Pp[kk]
    return out
S=[Fr(0)]*(NM+1); S[1]=Fr(1)
for _ in range(6): S=compose_psi(S)
B=[Fr(0)]*(NM+1)
for i,x in enumerate(S):
    for j,y in enumerate(S):
        if i+j<=NM: B[i+j]+=x*y
check("B5 == 17385641/62208", B[5]==Fr(17385641,62208))
def mf(x): return mp.mpf(x.numerator)/x.denominator
def Psi(s): x=mp.mpf(7)/6*s; return s+(mp.exp(x)-1-x)+(mp.sinh(x)-x)
def S6(r):
    s=r
    for _ in range(6): s=Psi(s)
    return s
r20=mp.mpf(1)/20; K8=(S6(r20)**2-sum(mf(B[nn])*r20**nn for nn in range(2,8)))/r20**8
check("K8(1/20) < 42355 (P2-A v2 tail)", K8<42355, mp.nstr(K8,10))
lhs=Fr(16931,10000)*Fr(1,20)+Fr(6671,5000)*Fr(1,400)+Fr(3567,1000)*Fr(1,8000)+42355*Fr(1,160000)
check("P2-A v2 contraction LHS == 2825241/8000000 < 1/2", lhs==Fr(2825241,8000000) and lhs<Fr(1,2))
r16=mp.mpf(1)/16; K10=(S6(r16)-sum(mf(S[nn])*r16**nn for nn in range(1,10)))/r16**10
check("K10^vec(1/16) < 332000 (P2-B v2 tail)", K10<332000, mp.nstr(K10,10))
sv=mp.mpf(1)/25; m=sv
for _ in range(5): sv=Psi(sv); m=max(m,sv)
check("max_j S_j(1/25) < 47/1000 (tube)", m<mp.mpf(47)/1000, mp.nstr(m,8))
check("(16/15) max_j S_j(1/25) < 1/20 (full tube inside normalized disk)", m*16/15<mp.mpf(1)/20, mp.nstr(m*16/15,8))
s=sp.symbols('s')
M=sp.Rational(7,12)*s**2+sp.Rational(39,500)*s**3+sp.Rational(14,125)*s**4+sp.Rational(11,250)*s**5+sp.Rational(1,20)*s**6
H=s+M; R=sp.Rational(1,10)
check("κ = M'(1/10) = 358439/3000000 < 1/8", sp.diff(M,s).subs(s,R)==sp.Rational(358439,3000000) and sp.diff(M,s).subs(s,R)<sp.Rational(1,8))
check("R - M(R) > 9/100 and M(R)/R < 1/16", (R-M.subs(s,R))>sp.Rational(9,100) and M.subs(s,R)/R<sp.Rational(1,16))
Pc={1:1,3:sp.Rational(1259,1000),4:sp.Rational(173,100),5:sp.Rational(469,500),6:sp.Rational(248,125)}
Jc={1:1,3:sp.Rational(1259,1000),5:sp.Rational(1099,1000)}
Ps=lambda x: sum(v*x**k for k,v in Pc.items()); Js=lambda x: sum(v*x**k for k,v in Jc.items())
Dfull=sp.Poly(sp.expand(Ps(H)+H.subs(s,Js(s))),s)
D7=sum(c*s**mm for (mm,),c in Dfull.terms() if mm>=7)
cb7,cb8,cb9,K=sp.Rational(2079,1000),sp.Rational(577,500),sp.Rational(1763,1000),332000; L=sp.Rational(8,7)
for r,C7adv,CD in [(sp.Rational(1,20),100,1000),(sp.Rational(1,40),30,250)]:
    x=H.subs(s,r); b=x/r
    check(f"r={r}: H(r) < 1/16 and H(r)/r_W < 10/11", x<sp.Rational(1,16) and x*16<sp.Rational(10,11), sp.N(x,12))
    check(f"r={r}: J+(r) < 1/10, H(J+(r)) < 9/100", Js(r)<R and H.subs(s,Js(r))<sp.Rational(9,100))
    check(f"r={r}: S6(H(r)) < 9/100", S6(mp.mpf(str(sp.N(x,40))))<mp.mpf(9)/100)
    Cpoly=D7.subs(s,r)/r**7; Dp6=sp.diff(D7,s).subs(s,r)/r**6
    A=cb7+cb8*x+cb9*x**2+K*x**3; Bv=7*cb7+8*cb8*x+9*cb9*x**2+10*K*x**3
    C7=L*(A*b**7+Cpoly)
    Cd=L*(Bv*b**6*sp.diff(H,s).subs(s,r)+Dp6+sp.diff(M,s,2).subs(s,R)*C7adv*r*sp.diff(Js(s),s).subs(s,r))
    check(f"r={r}: value constant < {C7adv}", C7<C7adv, sp.N(C7,12))
    check(f"r={r}: derivative constant < {CD}", Cd<CD, sp.N(Cd,12))
q=sp.Rational(1,400); u=sp.Rational(1259,1000); AJ=sp.Rational(1099,1000)
br=sp.Rational(19,12)+2*(1+u*q)*(AJ+100*q)+q**2*(AJ+100*q)**2
check("normalized-amplitude corollary q·bracket < 1/2 at q=1/400", q*br<sp.Rational(1,2), sp.N(q*br,10))
check("seed Q0 = 19/250000 < 1/625", Fr(19,250000)<Fr(1,625))
print("\nREFEREE RESULT:", "ALL PASS" if not FAIL else f"FAILURES: {FAIL}")
sys.exit(1 if FAIL else 0)
