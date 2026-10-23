#!/usr/bin/env python3
"""
recog_cell_d_lattice_memory_cert.py — RECOG CELL-D (rev. 4, normalized coefficients + canonical-comparator pair test): the lattice harmonic leaves a FINITE phase memory.

REVISION 3 (18 Sep 2026, after external review): rev. 2 used the RAW six-step quintic coefficients of Dyadic
§6.9 (c32 = -77/216 + i 97sqrt3/648, c05 = -61/2160 - i 43sqrt3/6480) inside a normal-form model. Those are
coefficients of the raw T^6 in the linear eigenframe, where a nonzero quartic jet is still present. This
revision (i) derives the post-H2 six-step jet from the primitive map with the Dyadic §6.2 h_2, (ii) checks
that the quartic jet vanishes and that the post-H2 lattice coefficient equals 6 conj(lam) nu_5^{(1,6)} from
the Dyadic one-step normalized ledger, and (iii) uses the post-H2 coefficients throughout:
    c32 = -97/432 + i 197sqrt3/324,   c05 = -49/8640 - i 307sqrt3/25920.
Model (post-H2 frame; residual U(1)-equivariant gauge does not affect c05 or the leading memory):
    W' = W + mu |W|^2 W + c32 |W|^4 W + c05 conj(W)^5,   mu = -1/2 - i 2sqrt3/3, tau = 2sqrt3/3.

Claim (leading order in Q0): the total asymptotic phase shift caused by the lattice term, relative to the
same orbit with c05 = 0, is

    dTheta_lat(inf) = Im[ (1 - 2 i tau)/(1 - 6 i tau) * c05 * Q0 * exp(-6 i Theta0) ] * (1 + O(Q0)),

with |1 - 6 i tau| = 7 exactly and (1-2i tau)/(1-6i tau) = (17 + 4 i tau)/49.
Radial memory vanishes (log Q difference -> 0): only phase is retained (consistent with Genesis plateau memory).

Structure of the derivation: direct phase kick Im(z_m) plus radial kick 2 Re(z_m) Q_m propagated through the
backbone kappa-shift, z_m = c05 Q_m^2 e^{-6 i Theta_m}; continuum limit of the sum with Q_m = q/(1+qm),
Theta_m = Theta0 - tau log(1+qm) gives the 1/(1 - 6 i tau) factor.

Exact form of the transfer coefficient with the post-H2 c05:
    (1-2i tau)/(1-6i tau) * c05 = -(43 + 5611 sqrt3 i)/1270080,
so  Lambda = Q0/1270080 * [43 sin(6 Theta0) - 5611 sqrt3 cos(6 Theta0)] + O(Q0^2).
(The rev. 2 raw-coefficient value -(2767+1219 sqrt3 i)/317520 is retained only as a superseded number.)

Checks: (1) |1-6i tau| = 7 exactly; (1b) exact transfer coefficient; (2) numeric orbit difference vs closed
form for several (Q0, Theta0), relative error <= 8*Q0 and DECREASING with Q0 (leading-order consistency);
(3) no retained log Q memory (radial difference -> 0; a bounded log-periodic oscillation in 1/Q is not excluded);
(4) equal-amplitude pair with different lattice phase acquires a nonzero relative phase;
(5) STRONG comparator-closure counterexample: two pairs with IDENTICAL comparator data (Q_a=Q_b=q,
    Theta_b-Theta_a = pi/6) but different common lattice phase alpha retain different pair memories,
    Delta Phi_lat(alpha) = -2 Lambda(q, alpha) + O(q^2).
Leading amplitude |Lambda| <= 0.00765198 Q0 holds at leading order only (post-H2 frame); no finite-Q0 rigorous bound
is claimed (that is CELL-D2).
(6) rev. 4: pairs chosen with IDENTICAL CANONICAL (raw-frame) comparator data, transported through H2^{-1} into the
    post-H2 model, still retain different pair memories.
"""
import mpmath as mp, sys
mp.mp.dps = 30
s3 = mp.sqrt(3)
mu  = mp.mpc(-mp.mpf(1)/2, -2*s3/3)
c32 = mp.mpc(-mp.mpf(97)/432, 197*s3/324)      # post-H2
c05 = mp.mpc(-mp.mpf(49)/8640, -307*s3/25920)   # post-H2
c32_raw = mp.mpc(-mp.mpf(77)/216, 97*s3/648); c05_raw = mp.mpc(-mp.mpf(61)/2160, -43*s3/6480)
tau = 2*s3/3
ok = True
def check(name, cond):
    global ok
    print(f"[{'PASS' if cond else 'FAIL'}] {name}"); ok = ok and bool(cond)

# ---- (0) derive the post-H2 six-step jet from the primitive map ----
DEG = 5
def mul(A,B):
    C={}
    for (i,j),a in A.items():
        for (k,l),b in B.items():
            if i+j+k+l<=DEG: C[(i+k,j+l)]=C.get((i+k,j+l),0)+a*b
    return C
def add(A,B,sg=1):
    C=dict(A)
    for k,v in B.items(): C[k]=C.get(k,0)+sg*v
    return C
def scal(A,x): return {k:v*x for k,v in A.items()}
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
om = mp.mpc(-0.5, s3/2); omb = mp.conj(om)
Zp={(1,0):mp.mpc(1)}; Zbp={(0,1):mp.mpc(1)}
eta_=scal(add(Zp,Zbp,-1),1/(om-omb)); rho_=add(Zp,scal(eta_,-om))
fac=lambda n: mp.factorial(n)
se=add(add(eta_,scal(powr(eta_,3),-1/fac(3))),scal(powr(eta_,5),1/fac(5)))
er={}
for n in range(1,6): er=add(er,scal(powr(rho_,n),1/fac(n)))
rho1=add(rho_,se,-1); eta1=add(add(eta_,er),se,-1)
F=[add(rho1,scal(eta1,om)), add(rho1,scal(eta1,omb))]
G=F
for _ in range(5): G=compose(F,G)
raw=add(G[0],Zp,-1)
h2={(2,0):-(1+1j*s3)/12,(1,1):mp.mpf(-1)/3,(0,2):(1-1j*s3)/24}      # Dyadic §6.2
H=[add(Zp,h2), add(Zbp,conjpoly(h2))]
Iv=[Zp,Zbp]
for _ in range(5):
    Iv=[add(Zp,compose([h2],Iv)[0],-1), add(Zbp,compose([conjpoly(h2)],Iv)[0],-1)]
Dn=add(compose(Iv,compose(G,H))[0],Zp,-1)
tolc=mp.mpf('1e-25')
check("raw six-step (3,2),(0,5) equal the Dyadic §6.9 'raw' values", abs(raw[(3,2)]-c32_raw)<tolc and abs(raw[(0,5)]-c05_raw)<tolc)
check("raw six-step has a nonzero quartic jet", any(abs(v)>1e-10 for k,v in raw.items() if sum(k)==4))
check("post-H2 quartic jet vanishes", all(abs(v)<tolc for k,v in Dn.items() if sum(k)==4))
check("post-H2 cubic is mu Z^2 Zb only", abs(Dn[(2,1)]-mu)<tolc and all(abs(v)<tolc for k,v in Dn.items() if sum(k)==3 and k!=(2,1)))
check("post-H2 (3,2),(0,5) equal the values used here", abs(Dn[(3,2)]-c32)<tolc and abs(Dn[(0,5)]-c05)<tolc)
lam6 = mp.exp(1j*mp.pi/3); nu5_onestep = mp.mpc(mp.mpf(43)/17280, -227*s3/155520)   # Dyadic §6.11
check("bridge: post-H2 c05 == 6 conj(lam) nu_5^{(1,6)} (one-step normalized ledger)", abs(6*mp.conj(lam6)*nu5_onestep - c05) < tolc)

check("|1 - 6 i tau| = 7 exactly", abs(abs(1-6j*tau) - 7) < mp.mpf('1e-15'))
coef = (1-2j*tau)/(1-6j*tau)*c05
check("(1-2i tau)/(1-6i tau) c05 = -(43 + 5611 sqrt3 i)/1270080",
      abs(coef + mp.mpc(43, 5611*s3)/1270080) < mp.mpf('1e-15'))

def run(Q0, Th0, lat, N):
    W = mp.sqrt(Q0)*mp.exp(1j*Th0); th = mp.mpf(Th0)
    for _ in range(N):
        Wn = W + mu*W*W*mp.conj(W) + c32*W**3*mp.conj(W)**2 + (c05*mp.conj(W)**5 if lat else 0)
        th += mp.arg(Wn/W); W = Wn
    return th, mp.log(abs(W)**2)

def pred(Q0, Th0):
    return mp.im((1-2j*tau)/(1-6j*tau) * c05 * Q0 * mp.exp(-6j*Th0))

N = 40000
errs = {}
for Q0 in [mp.mpf('0.04'), mp.mpf('0.02'), mp.mpf('0.01')]:
    rel = []
    for Th0 in [0, 0.35, 0.7, 1.0]:
        thL, lQL = run(Q0, Th0, True, N); th0, lQ0 = run(Q0, Th0, False, N)
        num = thL - th0; p = pred(Q0, Th0)
        rel.append(abs(num - p)/abs(p))
        check(f"radial memory ~0 at Q0={Q0},Th0={Th0}: |dlogQ|={mp.nstr(abs(lQL-lQ0),3)}", abs(lQL-lQ0) < 1e-6)
    errs[Q0] = max(rel)
    print(f"  Q0={Q0}: max relative error of phase-memory closed form = {mp.nstr(errs[Q0],4)}")
check("relative error <= 8*Q0 (O(Q0) correction) at all tested Q0", all(errs[q] < 8*q for q in errs))
check("relative error decreases with Q0 (leading-order consistency)", errs[mp.mpf('0.04')] > errs[mp.mpf('0.02')] > errs[mp.mpf('0.01')])

# (4) equal-amplitude pair, different lattice phase
Q0 = mp.mpf('0.02'); tha,_ = run(Q0, 0.0, True, N); thb,_ = run(Q0, mp.pi/6, True, N)
tha0,_ = run(Q0, 0.0, False, N); thb0,_ = run(Q0, mp.pi/6, False, N)
dpair = (thb - tha) - (thb0 - tha0)     # lattice-induced relative phase between equal-Q states
print("equal-amplitude pair (Theta0 = 0 vs pi/6): lattice-induced relative phase =", mp.nstr(dpair, 6),
      " predicted", mp.nstr(pred(Q0, mp.pi/6)-pred(Q0, 0.0), 6))
check("equal-amplitude pair acquires nonzero relative phase via lattice term", abs(dpair) > 1e-5)
# (5) identical comparator data, different common lattice phase
q = mp.mpf('0.02'); delta = mp.pi/6
def pair_memory(alpha):
    ta,_ = run(q, alpha, True, N); tb,_ = run(q, alpha+delta, True, N)
    ta0,_ = run(q, alpha, False, N); tb0,_ = run(q, alpha+delta, False, N)
    return (tb-ta) - (tb0-ta0)
m0 = pair_memory(mp.mpf(0)); m1 = pair_memory(mp.mpf('0.5'))
p0 = -2*pred(q, mp.mpf(0)); p1 = -2*pred(q, mp.mpf('0.5'))
print("identical-comparator pairs: alpha=0 ->", mp.nstr(m0,6), "(pred", mp.nstr(p0,6), ");  alpha=0.5 ->", mp.nstr(m1,6), "(pred", mp.nstr(p1,6), ")")
check("identical comparator data, different lattice phase -> different retained pair memory", abs(m0 - m1) > 1e-5)
check("pair memory matches -2*Lambda(q,alpha) to O(q)", abs(m0-p0) < 8*q*abs(p0) and abs(m1-p1) < 8*q*abs(p1))
# (6) identical CANONICAL (raw-frame) comparator data, transported through H2^{-1}
def H2inv_point(w):
    # evaluate the series inverse Iv (post-H2 coordinate z as function of raw w) at the point w
    z = mp.mpc(0)
    for (i,j),c in Iv[0].items(): z += c * w**i * mp.conj(w)**j
    return z
def run_z(z0, lat, N):
    W = z0; th = mp.arg(z0)
    for _ in range(N):
        Wn = W + mu*W*W*mp.conj(W) + c32*W**3*mp.conj(W)**2 + (c05*mp.conj(W)**5 if lat else 0)
        th += mp.arg(Wn/W); W = Wn
    return th
def pair_memory_raw(alpha, q=mp.mpf('0.02'), delta=mp.pi/6):
    wa = mp.sqrt(q)*mp.exp(1j*alpha); wb = mp.sqrt(q)*mp.exp(1j*(alpha+delta))   # identical raw C_->, all alpha
    za, zb = H2inv_point(wa), H2inv_point(wb)
    return (run_z(zb,True,N)-run_z(za,True,N)) - (run_z(zb,False,N)-run_z(za,False,N))
r0 = pair_memory_raw(mp.mpf(0)); r1 = pair_memory_raw(mp.mpf('0.5'))
print("identical CANONICAL comparator pairs (raw w, via H2^-1): alpha=0 ->", mp.nstr(r0,6), "; alpha=0.5 ->", mp.nstr(r1,6))
check("identical canonical (raw) comparator data -> different retained pair memory", abs(r0 - r1) > 1e-5)
print("leading amplitude: |Lambda| <= |17+4i tau|/49 * |c05| * Q0 =", mp.nstr(abs(17+4j*tau)/49*abs(c05),8), "* Q0  (leading order only, post-H2)")
print("CERTIFICATE PASS" if ok else "CERTIFICATE FAIL"); sys.exit(0 if ok else 1)
