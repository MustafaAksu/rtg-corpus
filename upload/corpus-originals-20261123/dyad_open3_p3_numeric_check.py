#!/usr/bin/env python3
# [NUM] illustration only (not a proof input): high-precision evaluation of S_Theta - L_Theta and S_Q - [S_Q]_5
# for the exact chart polynomial h (regenerated exactly as in the P3 certificate) and the exact primitive map T.
import sys, json
sys.path.insert(0, '.')
src = open('dyad_open3_p3_remainder_cert.py').read()
exec(src.split('chk = {}')[0])           # builds h, n, J exactly
import mpmath as mp
mp.mp.dps = 60
s3 = mp.sqrt(3)
qc = lambda c: mp.mpf(c.a.numerator)/c.a.denominator + mp.mpf(c.b.numerator)/c.b.denominator*1j*s3
H = [(a, b, qc(v)) for (a, b), v in h.d.items()]
JJ = [(a, b, qc(v)) for (a, b), v in J.d.items() if a+b <= 6]
def poly(C, w): wb = mp.conj(w); return mp.fsum([c*w**a*wb**b for a, b, c in C])
hf = lambda w: poly(H, w)
def hinv(W):
    zz = W
    for _ in range(200):
        zn = W - (hf(zz) - zz)
        if abs(zn - zz) < mp.mpf(10)**(-55): return zn
        zz = zn
    return zz
def T(r, e): return r - mp.sin(e), e + mp.exp(r) - 1 - mp.sin(e)
def FW(W):
    e = 2*mp.im(W)/s3; r = mp.re(W) + e/2
    for _ in range(6): r, e = T(r, e)
    return r - e/2 + 1j*s3/2*e
mu = qc(J.get((2, 1)))
c20, c11, c02 = qc(h.get((2, 0))), qc(h.get((1, 1))), qc(h.get((0, 2)))
def L_Theta(w):
    q = abs(w)**2; wb = mp.conj(w)
    return mp.im(mu*c20*q*w + mp.conj(mu)*c11*q*wb + (2*mp.conj(mu) - mu)*c02*wb**3)
D3 = [(2, 1, c20 + mp.conj(c11)), (1, 2, c11 + mp.conj(c20)), (0, 3, c02), (3, 0, mp.conj(c02))]
def SQ5(w):
    v = mu*abs(w)**2*w; wb = mp.conj(w)
    return mp.re(mp.fsum([c*(a*w**(a-1)*wb**b*v if a else 0) + c*(b*w**a*wb**(b-1)*mp.conj(v) if b else 0) for a, b, c in D3]))
DT = lambda w: mp.arg(hf(w)/w)
DQ = lambda w: abs(hf(w))**2 - abs(w)**2
res = {}
for r, C7, KT, KQ in ((mp.mpf(1)/20, 100, 0.984, 2.353), (mp.mpf(1)/40, 30, 0.909, 2.064)):
    mT = mQ = mR = 0
    for frac in (1, mp.mpf(1)/2, mp.mpf(1)/4, mp.mpf(1)/8):
        for k in range(72):
            w = r*frac*mp.expj(2*mp.pi*k/72 + mp.mpf(1)/7)
            wp = hinv(FW(hf(w))); q = abs(w)**2
            mR = max(mR, abs(wp - poly(JJ, w))/abs(w)**7)
            mT = max(mT, abs(DT(wp) - DT(w) - L_Theta(w))/q**2)
            mQ = max(mQ, abs(DQ(wp) - DQ(w) - SQ5(w))/q**3)
    res[str(float(r))] = {'max |Fhat-J|/|z|^7 (C7=%d)' % C7: float(mR), 'max |S_T-L_T|/q^2 (K_Theta=%s)' % KT: float(mT),
                          'max |S_Q-[S_Q]_5|/q^3 (K_Q=%s)' % KQ: float(mQ),
                          'within': bool(mR <= C7 and mT <= KT and mQ <= KQ)}
print(json.dumps(res, indent=1)); json.dump(res, open('p3_numeric.json', 'w'), indent=1)
sys.exit(0 if all(v['within'] for v in res.values()) else 1)
