import sys, json
src=open('recog_cell_e2c_twin_radial_access.py').read().split('if __name__ == "__main__":')[0]; exec(src)
import mpmath as mp; mp.mp.dps = 60
from flint import arb
RHO_C = mp.acosh(2)
def Tmp(x): r, e = x; s = mp.sin(e); return (r - s, e + mp.sinh(r) - s)
def to_arb(x): return arb(mp.nstr(x, 58))
def inside(c, A, E, w):
    e = Eng.mv(Eng.inv(A), [to_arb(w[0]) - c[0], to_arb(w[1]) - c[1]])
    return all(bool(E[i].contains(e[i])) for i in range(2))
def audit_tile(kt, kr, NTH, NR):
    c0, A0, E0 = tile(kt, kr, NTH, NR); stats = dict(checks=0, clips_with_uncrossed=0, crossed_dropped=0, violations=0, crossed=0, witnesses=0)
    for (u, v) in [(0, 0), (0.9, 0.9), (0.9, -0.9), (-0.9, 0.9), (-0.9, -0.9)]:
        e = [arb(u)*E0[0].rad(), arb(v)*E0[1].rad()]
        p = [c0[i] + A0[i][0]*e[0] + A0[i][1]*e[1] for i in range(2)]
        w = (mp.mpf(p[0].mid().str(55, radius=False)), mp.mpf(p[1].mid().str(55, radius=False)))
        c, A, E, n = c0, A0, E0, 0; stats['witnesses'] += 1; crossed = False
        if not inside(c, A, E, w): stats['violations'] += 1; continue
        while n <= NMAX:
            if abs(w[0]) >= RHO_C: crossed = True
            H = Eng.hull(c, A, E); rho = H[0]
            if rho >= A_thr or rho <= -A_thr:                      # leaf: witness inside a certified-successful enclosure
                stats['checks'] += 1
                if not inside(c, A, E, w): stats['violations'] += 1
                break
            if rho.upper() > A_thr.lower() or rho.lower() < -A_thr.lower():
                E2 = clip(c, A, E)
                if E2 is None:
                    if not crossed and abs(w[0]) < RHO_C: stats['violations'] += 1
                    else: stats['crossed_dropped'] += 1
                    break
                c2, A2, E2 = Eng.recenter(c, A, E2); stats['checks'] += 1
                if not inside(c2, A2, E2, w):
                    if abs(w[0]) < RHO_C: stats['violations'] += 1          # an uncrossed witness vanished: must never happen
                    else: stats['crossed_dropped'] += 1
                    break
                if abs(w[0]) < RHO_C: stats['clips_with_uncrossed'] += 1
                c, A, E = c2, A2, E2
            if max(K.width(E[0]), K.width(E[1])) > WSPLIT:
                j = 0 if K.width(E[0]) >= K.width(E[1]) else 1
                a_, b_ = K.split(E[j]); Ea = list(E); Eb = list(E); Ea[j] = a_; Eb[j] = b_
                ca, Aa, Ea2 = Eng.recenter(c, A, Ea); cb, Ab, Eb2 = Eng.recenter(c, A, Eb)
                if inside(ca, Aa, Ea2, w): c, A, E = ca, Aa, Ea2
                elif inside(cb, Ab, Eb2, w): c, A, E = cb, Ab, Eb2
                else: stats['violations'] += 1; break
                stats['checks'] += 1; continue
            c, A, E, _ = Eng.step(c, A, E); w = Tmp(w); n += 1; stats['checks'] += 1
            if not inside(c, A, E, w): stats['violations'] += 1; break
        if crossed: stats['crossed'] += 1
    return stats
tiles = [(0, 0), (1024, 16), (2048, 31), (3000, 5), (409, 0), (1638, 16)]   # includes sample/adversarial-type positions
tot = {}
for kt, kr in tiles:
    s = audit_tile(kt, kr, NTH_PROD, NR_PROD); print(kt, kr, s, flush=True)
    for k, v in s.items(): tot[k] = tot.get(k, 0) + v
print("TOTAL", tot); print("WITNESS AUDIT PASS" if tot['violations'] == 0 else "WITNESS AUDIT FAIL")
