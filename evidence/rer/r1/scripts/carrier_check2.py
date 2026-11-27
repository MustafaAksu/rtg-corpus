import sys; import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from mpmath import mp, mpf, mpc, sqrt, im, re, conj, exp, pi, fabs, sin
import carrier_check as C
mp.dps = 80; r3 = sqrt(3); lam = C.lam
# 4) independence from cubic chart jet: H = z + sig*h2 + c3*z^2*zbar + c4*zbar^3
def make3(sig, c3, c4):
    H = lambda z: z + sig*C.h2(z) + c3*z**2*conj(z) + c4*conj(z)**3
    def Hinv(y):
        z = y
        for _ in range(300):
            zn = y - (H(z) - z)
            if fabs(zn - z) < mpf(10)**(-mp.dps+5): return zn
            z = zn
        return z
    return H, Hinv
for sig in (mpf('0.2'), mpf('0.7')):
    C.make = lambda s, sig=sig: make3(s, mpc('0.37','-0.21'), mpc('-0.5','0.8'))
    k = 1 - sig; a = -mpf(1)/2 + 2*k**2/3; A, B = mpc('0.3','0.8'), mpc('-0.9','0.2')
    ws = [A, B, -(A+B)]; N, S = C.NS(ws)
    print('cubic-jet chart sigma', float(sig), ' dN err', float(abs(C.quartic(A, B, sig, 'N') - (a*N**2 + 2*S**2))), ' dS err', float(abs(C.quartic(A, B, sig, 'S') - mpf(2)/3*(-mpf(1)/2+k**2)*N*S)))
# 5) mu22(q) closed form and Genesis normalization: coefficient of w^2 wbar in T^6 - id
def coeff_w2wb(Tmap):
    vals = []
    for eps in (mpf('1e-7'), mpf('2e-7')):
        M = 24; acc = 0
        for j in range(M):
            th = 2*pi*j/M; w = eps*exp(1j*th); x = w
            for _ in range(6): x = Tmap(x)
            acc += (x - w) * exp(-1j*th)
        vals.append(acc/M/eps**3)
    return 2*vals[0] - vals[1]
print('mu (full Genesis T):', coeff_w2wb(C.TW), ' claim', -0.5 - 2j*float(r3)/3)
def quadW(w):  # quadratic part of Genesis T in W frame: W(0, rho^2/2)
    r, e = C.fromW(w); return C.toW(0, r**2/2)
print('mu22,G:', coeff_w2wb(lambda w: lam*w + quadW(w)), ' claim', -1 - 0.5j*float(r3))
import random; random.seed(7); worst = 0
for _ in range(4):
    u, v, t = [mpc(random.uniform(-1,1), random.uniform(-1,1)) for _ in range(3)]
    got = coeff_w2wb(lambda w: lam*w + u*w**2 + v*w*conj(w) + t*conj(w)**2)
    clm = (9+3j*r3)*u*v - (3+3j*r3)*abs(v)**2 - 6*abs(t)**2
    worst = max(worst, abs(got - clm))
print('mu22(q) closed form, 4 random q, max err:', float(worst))
