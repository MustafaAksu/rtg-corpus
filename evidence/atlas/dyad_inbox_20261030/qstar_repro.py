#!/usr/bin/env python3
"""Atlas reproduction of NUMGEN's q* (numgen-v1.21 §6.6, L909-912): the root of eta_6(q) - q on the canonical
family (rho_0, eta_0) = (0, q) of the primitive map T(rho, eta) = (rho - sin eta, eta + e^rho - 1 - sin eta)
(DYAD-DEF-PRIMITIVE-MAP), eta_6 wrapped to (-pi, pi]. Evidence for the pipe question to DYAD only; it does not
define or reproduce Dyadic's q* of DYAD-THM-OPEN18, whose definition is not in the repository.
Run: python3 -I evidence/atlas/dyad_inbox_20261030/qstar_repro.py   (needs mpmath)"""
import mpmath as mp
mp.mp.dps = 60
NUMGEN = '0.315625883659561602974267621967906111219946754'

def six(q):
    r, e = mp.mpf(0), q
    for _ in range(6):
        r, e = r - mp.sin(e), e + mp.e**r - 1 - mp.sin(e)
    return r, e

def g(q):
    r, e = six(q)
    return mp.atan2(mp.sin(e), mp.cos(e)) - q

a, b = mp.mpf('0.31562'), mp.mpf('0.31563')
print('bracket signs at 0.31562, 0.31563:', int(mp.sign(g(a))), int(mp.sign(g(b))))
root = mp.findroot(g, (a, b), solver='anderson')
r6, e6 = six(root)
print('q* (atlas)  =', mp.nstr(root, 45))
print('q* (NUMGEN) =', NUMGEN)
print('agree to 45 significant digits:', mp.nstr(root, 45) == NUMGEN)
print('unwrapped eta_6 - q* =', mp.nstr(e6 - root, 5), '(no winding)')
print('rho_6 =', mp.nstr(r6, 20))
