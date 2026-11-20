#!/usr/bin/env python3
"""DYAD OPEN 20 stage 3c-a: the wall constants c_0, c_1 as exact dyadic numbers (owner finding O-1).

Definition (proof record section 1): c_j is the exact dyadic number C_WALL[j] below, the upper endpoint of the ball
TB.cw = second_j(xi*) - 0.15 as the library computes it in the ENGINE PROFILE: Consts at 400 decimal digits, then
the working precision set to 160 bits, then tau_coefficients() and Tube(K, TAU, j) (the order of build_engine and of
the scripts W2-W7; python-flint 0.9.0).  With this definition every use of TB.cw in the engine scripts is exact:
the floors max(TB.cw.upper(), second.lower()) are floors of second > c_j, the out-tests (second <= TB.cw in ball
arithmetic) imply second <= c_j, and the zone-1 test pre >= cj * t uses cj = c_j itself.

Gates:
  REPRO    the engine profile reproduces C_WALL exactly (same library, same python-flint);
  ABOVE    the real number v_j = second_j(xi*) - 0.15 (decimal tau, enclosed at 400 digits throughout) is < c_j;
  CLOSE    c_j - v_j < 2^-150 (the definition moves the wall by less than that);
  MARGIN   second_j(xi*) - c_j > 0.149 (xi* stays inside D_j with its design margin);
  ONE      c_j >= 1 (used in proof record section 12, step 3).
Also reported, not gated: the wall ball of the seed profile (200 bits), for the seed check's H >= c_j.

Usage: cd evidence/dyad/scripts && python3 dyad_open20_an_wall_constants_check.py --out FILE.json
"""
import argparse, hashlib, json, os, sys
from flint import arb, ctx, __version__ as FLINT_VERSION
import dyad_open20_an_stage3c_lib as L

C_WALL = {0: (1086324957910094173414457875632740785514726345335, -158),
          1: (389963341406742017386679541510573444277057039337, -156)}


def exact(me):
    m, e = me
    return arb(m) * arb(2) ** e          # exact at any precision >= 160 bits (m has < 160 bits)


def wall_ball(dps=None, prec=None, consts_dps=400):
    ctx.dps = consts_dps
    K = L.Consts()
    if prec is not None:
        ctx.prec = prec
    else:
        ctx.dps = dps
    TAU = L.tau_coefficients()
    return [L.Tube(K, TAU, j) for j in (0, 1)]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--out', required=True); o = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    lib = os.path.join(here, 'dyad_open20_an_stage3c_lib.py')
    g, info = {}, dict(python_flint=FLINT_VERSION,
                       lib_sha256=hashlib.sha256(open(lib, 'rb').read()).hexdigest(),
                       C_WALL={str(j): dict(mantissa=str(m), exponent=e) for j, (m, e) in C_WALL.items()})
    # engine profile
    TB = wall_ball(prec=160)
    rep = [TB[j].cw.upper().man_exp() for j in (0, 1)]
    g['REPRO'] = all((int(rep[j][0]), int(rep[j][1])) == C_WALL[j] for j in (0, 1))
    info['engine_profile_upper'] = [dict(mantissa=str(int(m)), exponent=int(e)) for m, e in rep]
    # high precision: every object at 400 digits
    ctx.dps = 400
    TBh = wall_ball(dps=400)
    above, close, margin, one, gaps, mg = True, True, True, True, [], []
    for j in (0, 1):
        ctx.dps = 400
        c = exact(C_WALL[j]); v = TBh[j].cw
        above = above and bool(v < c)
        gap = c - v
        close = close and bool(gap < arb(2) ** -150)
        sec = v + arb('0.15')
        margin = margin and bool(sec - c > arb('0.149'))
        one = one and bool(c >= 1)
        gaps.append(arb(gap.upper()).str(5, radius=False)); mg.append(arb((sec - c).lower()).str(8, radius=False))
    g['ABOVE'], g['CLOSE'], g['MARGIN'], g['ONE'] = above, close, margin, one
    info['c_minus_v_upper'] = gaps; info['second_star_minus_c_lower'] = mg
    info['c_decimal_30'] = [exact(C_WALL[j]).str(30, radius=False) for j in (0, 1)]
    # seed profile (reported only)
    ctx.prec = 200
    K = L.Consts(); TAU = L.tau_coefficients(); TBs = [L.Tube(K, TAU, j) for j in (0, 1)]
    info['seed_profile'] = [dict(cw_upper_ge_c=bool(arb(TBs[j].cw.upper()) >= exact(C_WALL[j])),
                                 abs_diff_upper=arb(abs(arb(TBs[j].cw.upper()) - exact(C_WALL[j])).upper()).str(3, radius=False))
                            for j in (0, 1)]
    res = dict(script='dyad_open20_an_wall_constants_check.py', gates=g, all_pass=all(g.values()), info=info)
    with open(o.out, 'w') as f:
        json.dump(res, f, indent=1, sort_keys=True)
    print(json.dumps(res, indent=1, sort_keys=True))
    return 0 if res['all_pass'] else 1


if __name__ == '__main__':
    sys.exit(main())
