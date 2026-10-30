#!/usr/bin/env python3
"""Atlas reading of Dyadic's q_* (DYAD-THM-OPEN18) from the recovered certificate open18_arb_cert3.cpp, whose first
line reads "// open18_arb_cert_final.cpp". That certificate sweeps branch Gamma_3 (footprint step n=3) on
q in [0.001, 1.26021320256] and Gamma_4 (n=4) on [1.26021520256, 2.0] of the canonical family (rho_0, eta_0) = (0, q),
leaving out a gap of half-width 1e-6 around 1.26021420256; it says that "branch legality and q_* root isolation are
supplied by independent footprint audits" (not recovered). This script locates the root inside that gap of every
step-n quantity that changes sign there and reports Theta_n = Arg(W_n), W = rho + omega*eta, omega = e^{2 pi i/3}, against the
ISP funnel edges -pi/3, -2pi/3 (DYAD §6.8). An atlas reading, not an owner statement.
Run: python3 -I evidence/atlas/dyad_inbox_20261030/qstar_dyad_split.py   (needs mpmath)"""
import mpmath as mp
mp.mp.dps = 50
w = (-1 + mp.sqrt(3) * 1j) / 2
LO, HI = mp.mpf('1.26021320256'), mp.mpf('1.26021520256')

def orb(q, n=6):
    r, e = mp.mpf(0), mp.mpf(q); o = [(r, e)]
    for _ in range(n):
        r, e = r - mp.sin(e), e + mp.e**r - 1 - mp.sin(e); o.append((r, e))
    return o

def th(p): return mp.arg(p[0] + w * p[1])

found = []
for k in range(1, 7):
    for name, f in (('rho_%d' % k, lambda o, k=k: o[k][0]), ('eta_%d' % k, lambda o, k=k: o[k][1]),
                    ('Theta_%d+pi/3' % k, lambda o, k=k: th(o[k]) + mp.pi / 3), ('Theta_%d+2pi/3' % k, lambda o, k=k: th(o[k]) + 2 * mp.pi / 3)):
        if mp.sign(f(orb(LO))) != mp.sign(f(orb(HI))):
            found.append((name, mp.findroot(lambda q: f(orb(q)), (LO + HI) / 2, tol=mp.mpf(10)**-45)))
for name, z in found: print('%-14s changes sign in the gap; root q = %s' % (name, mp.nstr(z, 36)))
q = found[0][1]
print('gap centre 1.26021420256 vs root: |diff| =', mp.nstr(abs(q - mp.mpf('1.26021420256')), 3))
for lab, qq in (('q_*-1e-6', q - mp.mpf('1e-6')), ('q_*+1e-6', q + mp.mpf('1e-6'))):
    o = orb(qq)
    print(lab, ' '.join('Theta_%d=%s' % (k, mp.nstr(th(o[k]), 9)) for k in (2, 3, 4, 5)), ' (-pi/3 =', mp.nstr(-mp.pi / 3, 9), ')')
print("NUMGEN q* (numgen-v1.21 L909) = 0.3156258836..., root of eta_6(q)-q: a different number")
