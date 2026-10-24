#!/usr/bin/env python3
"""dyad_open20_an_stage2_exact_crosscheck.py -- exact cross-check of the stage-2 coefficients a_5..a_8 (OPEN 20 analytic branch).

Requested by the stage-2 co-owner review (check 1): an exact computation of a_5, ..., a_8 that is independent of the
stage-2 generator. Route: the stage-1 machinery (exact field tower Q(i sqrt3) ⊂ E = Q(i sqrt3)[a]/(P); jets of F = T^6
composed in exact rationals in the real chart, here to total degree 11) and the stage-1 graph equation solved order by
order in E, exactly as S2 did for a_3, a_4. The stage-2 generator instead works with one-variable series of the full map
in ball arithmetic and never forms a bivariate jet; the two routes share only the definition of T and the frame change.

Gates:
  X1  orders z^0..z^5 of the graph residual vanish in E (with phi = a z^2); for k = 3..8 the order-z^{k+3} coefficient is
      affine in a_k with the exact linear coefficient L_k = ell (k* - k), and the solved residual vanishes through z^11.
  X2  a_5..a_8 evaluated at a_pil (mpmath, 60 digits, principal square root as in stage-1 S1) agree with the stage-2
      coefficients (scout JSON, 80 stored digits) to 1e-40; a_3, a_4 likewise (already covered by stage-1/C1/C2).
Negative control --control W: evaluates the exact a_k at the other root of P (Im a < 0); X2 must fail.
Usage: python -I -B dyad_open20_an_stage2_exact_crosscheck.py --scout ../open20-an/stage2/scout_N216_dps840.json --out exact_crosscheck.json
Exit 0 all gates pass; 1 otherwise; 3 crash. Output JSON byte-deterministic.
"""
import os, sys, json, argparse
sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr
from dyad_h4_real_route_check import T6
from dyad_open20_an_stage1_prep import Qs, E_, Ec, Ser, MU, C40, D31, CC, A_, B_, KSTAR, OMEGA, A_E, ELL


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--scout', default='scout_N216_dps840.json'); ap.add_argument('--out', default='exact_crosscheck.json')
    ap.add_argument('--control', choices=['W']); opt = ap.parse_args()
    Ec.C3 = -ELL
    D = 11
    R, Ex = T6(D)
    om, omb = OMEGA, OMEGA.conj(); den = om - omb
    zc, wc = (-omb / den, om / den), (Qs(1) / den, Qs(-1) / den)
    def pmul(p, q):
        r = {}
        for (i, j), u in p.items():
            for (k, l), v in q.items():
                if i + j + k + l <= D: r[(i + k, j + l)] = r.get((i + k, j + l), Qs()) + u * v
        return {k: v for k, v in r.items() if not v.iszero()}
    def padd(p, q):
        r = dict(p)
        for k, v in q.items(): r[k] = r.get(k, Qs()) + v
        return {k: v for k, v in r.items() if not v.iszero()}
    pw_r, pw_e = {0: {(0, 0): Qs(1)}}, {0: {(0, 0): Qs(1)}}
    for n in range(1, D + 1):
        pw_r[n] = pmul(pw_r[n - 1], {(1, 0): zc[0], (0, 1): zc[1]}); pw_e[n] = pmul(pw_e[n - 1], {(1, 0): wc[0], (0, 1): wc[1]})
    def convert(P):
        out = {}
        for (i, j), v in P.items(): out = padd(out, {k: u * Qs(v) for k, u in pmul(pw_r[i], pw_e[j]).items()})
        return out
    Rz, Ez = convert(R), convert(Ex)
    Fz = padd(Rz, {k: v * om for k, v in Ez.items()}); Fw = padd(Rz, {k: v * omb for k, v in Ez.items()})
    assert Fz[(2, 1)] == MU and Fz[(4, 0)] == C40 and Fw[(3, 1)] == D31 and Fw[(5, 0)] == CC
    NZ = D
    FzS = Ser({k: Ec([E_(v), 0, 0]) for k, v in Fz.items()}, NZ, NZ); FwS = Ser({k: Ec([E_(v), 0, 0]) for k, v in Fw.items()}, NZ, NZ)
    Zs = Ser({(1, 0): Ec.c(1)}, NZ, 0); zero_y = Ser({}, NZ, 0)
    zser = lambda d: Ser({(k, 0): Ec([v, 0, 0]) for k, v in d.items()}, NZ, 0)
    def graph_res(phi):
        Fzp = FzS.compose(Zs, phi).trunc(NZ, 0); Fwp = FwS.compose(Zs, phi).trunc(NZ, 0)
        return Fwp - phi.compose(Fzp, zero_y)
    G, info = {}, {'jet_degree': D}
    phi = zser({2: A_E}); res = graph_res(phi)
    x1 = {'z0..z5_vanish': all(res.coef(k, 0).iszero() for k in range(0, 6))}
    ak = {}
    for k in range(3, 9):
        R0 = graph_res(phi).coef(k + 3, 0).v[0]
        R1 = graph_res(phi + zser({k: E_(1)})).coef(k + 3, 0).v[0]
        R2 = graph_res(phi + zser({k: E_(2)})).coef(k + 3, 0).v[0]
        Lk = R1 - R0
        x1['L%d=ell(k*-%d)' % (k, k)] = ((R2 - R0) == 2 * Lk) and Lk == ELL * (E_(KSTAR) - k)
        ak[k] = -R0 / Lk
        phi = phi + zser({k: ak[k]})
        x1['z%d_solved' % (k + 3)] = graph_res(phi).coef(k + 3, 0).iszero()
    x1['residual_vanishes_through_z11'] = all(graph_res(phi).coef(j, 0).iszero() for j in range(0, 12))
    G['X1'] = all(x1.values()); info['X1'] = {k: bool(v) for k, v in x1.items()}
    info['exact_a_k_in_E'] = {str(k): repr(ak[k]) for k in range(3, 9)}
    # ---- X2: numeric comparison with the stage-2 coefficients ----
    import mpmath as mp
    mp.mp.dps = 60
    s3 = mp.sqrt(3)
    def num(q): return mp.mpc(mp.mpf(q.p.numerator) / q.p.denominator, mp.mpf(q.q.numerator) / q.q.denominator * s3)
    disc = B_ * B_ - 4 * A_ * CC
    sq = mp.sqrt(num(disc)); assert sq.imag > 0
    a_pil = (-num(B_) - sq) / (2 * num(A_)); a_oth = (-num(B_) + sq) / (2 * num(A_))
    assert a_pil.imag > 0 and a_oth.imag < 0
    aval = a_oth if opt.control == 'W' else a_pil
    sc = json.load(open(opt.scout, encoding='utf-8'))['info']
    x2 = {}; diffs = {}
    for k in range(3, 9):
        ex = num(ak[k].e0) + num(ak[k].e1) * aval
        st2 = mp.mpc(sc['coefficients'][str(k)][0], sc['coefficients'][str(k)][1])
        d = abs(ex - st2); diffs[str(k)] = mp.nstr(d, 5)
        x2['a%d' % k] = bool(d < mp.mpf('1e-40'))
    G['X2'] = all(x2.values()); info['X2'] = {'gates': x2, 'abs_difference_exact_minus_stage2': diffs,
                                             'evaluated_at': 'other root (control W)' if opt.control == 'W' else 'a_pil',
                                             'stage2_source': os.path.basename(opt.scout), 'stage2_N_dps': [sc['N'], sc['dps']]}
    ok = all(G.values())
    for k in sorted(G): print(k, 'PASS' if G[k] else 'FAIL')
    print('RESULT', 'PASS' if ok else 'FAIL')
    with open(opt.out, 'w', encoding='utf-8', newline='\n') as f:
        json.dump({'gates': G, 'info': info, 'all_pass': ok, 'script': 'dyad_open20_an_stage2_exact_crosscheck.py', 'control': opt.control},
                  f, indent=1, sort_keys=True, ensure_ascii=False); f.write('\n')
    return 0 if ok else 1


if __name__ == '__main__':
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as ex:
        import traceback; traceback.print_exc(); print('CRASH', type(ex).__name__, ex); sys.exit(3)
