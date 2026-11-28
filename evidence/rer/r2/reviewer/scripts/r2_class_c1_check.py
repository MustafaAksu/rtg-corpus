# Independent reviewer check of RER R2 §3 (Claude). Direct six-step iteration of the FULL class-C1 polynomial map
# G(w)_e = N3(w_e) - mean_j N3(w_j), N3(z) = lam z + n z^2 zbar, n = n_T (GEN v2.10 §6.3c C1), flat kappa=1 slice.
# No use of the preparer's modal formulas inside the map.
from mpmath import mp, mpf, mpc, sqrt, conj, re, im, exp, pi
mp.dps = 60
r3 = sqrt(3); lam = mpc(mpf(1)/2, r3/2)
n = mpc(mpf(1)/8, -7*r3/72)
mu = -mpf(1)/2 - 2j*r3/3
N3 = lambda z: lam*z + n*z*z*conj(z)
def G(ws):
    t = [N3(w) for w in ws]; m = sum(t)/3; return [x - m for x in t]
def F(ws):
    for _ in range(6): ws = G(ws)
    return ws
def modal(ws): return ws[0], (ws[1]-ws[2])/2
def state(z, d): return [z, -z/2 + d, -z/2 - d]
def rich(fun, e1=mpf('1e-5')):  # remove next odd order (state-degree +2) by Richardson in eps^2
    a = fun(e1); b = fun(2*e1); return (4*a - b)/3
print('mu = 6*conj(lam)*n:', abs(6*conj(lam)*n - mu) < mpf(10)**-50)
# (a) six-step cubic equals mu * P(w|w|^2)
worst = 0
for (z, d) in [(mpc('0.6','0.2'), mpc('-0.3','0.5')), (mpc('-0.1','0.9'), mpc('0.7','0.1'))]:
    for k in range(3):
        def fa(e, k=k):
            ws = state(e*z, e*d); out = F(ws); c = [w*abs(w)**2 for w in ws]; mc = sum(c)/3
            return (out[k] - ws[k] - mu*(c[k] - mc))/e**3
        worst = max(worst, abs(rich(fa)))
print('(a) six-step cubic = mu*P(w|w|^2), max residual:', float(worst))
# (b) unsigned-Gram nonclosure: leading Delta I at d = +i z and d = -i z equals +/- sqrt3/9 Q^2
z = mpc('0.8','-0.35'); Q = abs(z)**2
for sgn in (1, -1):
    def fb(e, sgn=sgn):
        zz, dd = e*z, sgn*1j*e*z; zs, ds = modal(F(state(zz, dd)))
        return (re(zs*conj(ds)) - re(zz*conj(dd)))/e**4
    print(f'(b) d={"+" if sgn>0 else "-"}iz: Delta4 I / Q^2 =', float(rich(fb)/Q**2), ' claim', float(sgn*r3/9))
# (c) exact scalar closure on d=0: Q+ = Q|lam + 3nQ/4|^2 for one primitive step, and child stays 0
z = mpc('0.31','0.22'); zs, ds = modal(G(state(z, 0)))
print('(c) Q+ exact residual:', float(abs(abs(zs)**2 - abs(z)**2*abs(lam + 3*n*abs(z)**2/4)**2)), ' child:', float(abs(ds)))
# (d) birth-graph defect of trial C_b(z) = i b Q z under F: D(z) = F_c(z,C(z)) - C(F_s(z,C(z))) = b(-sqrt3/3+i)Q^2 z + O(7)
b = mpf('0.7'); Cb = lambda z: 1j*b*abs(z)**2*z
for z in (mpc('0.5','0.4'), mpc('-0.9','0.1')):
    def fd(e, z=z):
        zz = e*z; zs, ds = modal(F(state(zz, Cb(zz)))); return (ds - Cb(zs))/(abs(zz)**4*zz)
    print('(d) defect/(Q^2 z) =', complex(rich(fd)), ' claim', complex(b*(-r3/3 + 1j)))
# (e) oddness and U(1): F(e^{it} X) = e^{it} F(X) for C1 at finite size
X = state(mpc('0.2','0.1'), mpc('-0.05','0.12')); t = mpf('0.37')
A = F([exp(1j*t)*w for w in X]); B = [exp(1j*t)*w for w in F(X)]
print('(e) C1 common U(1) equivariance at finite size, max err:', float(max(abs(a-c) for a, c in zip(A, B))))
# (f) finite-age graph separation: age-k graph C_k (image of graph C_b under F^k); (C_n - C_m)(z) ~ (n-m) D(z) at leading order
def Fs_k_inv(zp, k):  # solve F^k_s(z, C_b(z)) = zp for z by fixed point (tangent-to-identity)
    z = zp
    for _ in range(80):
        ws = state(z, Cb(z))
        for _ in range(k): ws = F(ws)
        z = z - (modal(ws)[0] - zp)
    return z
def Ck(zp, k):
    if k == 0: return Cb(zp)
    z = Fs_k_inv(zp, k); ws = state(z, Cb(z))
    for _ in range(k): ws = F(ws)
    return modal(ws)[1]
zp0 = mpc('0.5','0.4')
for (nn, mm) in [(1, 0), (2, 0), (3, 1)]:
    def ff(e, nn=nn, mm=mm):
        zp = e*zp0; return (Ck(zp, nn) - Ck(zp, mm))/(abs(zp)**4*zp)
    print(f'(f) (C_{nn} - C_{mm})/(Q^2 z) =', complex(rich(ff)), ' claim', complex((nn-mm)*b*(-r3/3 + 1j)))
