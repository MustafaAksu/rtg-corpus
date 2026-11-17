#!/usr/bin/env python3
"""Step-timed exact q=4,(0,3) certification profiler.
Place in the same directory as rtg_p_certs.py / rtg_p_core.py.
This is a profiler, not a replacement for the canonical cert CLI.
"""
import argparse, time, sys
import sympy as sp
from rtg_p_certs import (
    build_1step_map_exact_through_degree, assert_linear_part_only_degree1,
    charge, cyclotomic_zero_sum_remainder, ssubst, sscale, sclean, project_extra, is_exact_zero
)

def stamp(label,t0):
    dt=time.perf_counter()-t0
    print(f"[{dt:10.3f}s] {label}", flush=True)
    return time.perf_counter()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--p', type=int, required=True)
    ap.add_argument('--q', type=int, default=4)
    ap.add_argument('--D', type=int, default=4)
    ap.add_argument('--slot', nargs=2, type=int, default=[0,3])
    ap.add_argument('--no-final-simplify', action='store_true')
    args=ap.parse_args()
    p,q,D=args.p,args.q,args.D
    slot=tuple(args.slot)
    assert p%q==0
    s=p//q
    t0=time.perf_counter(); t=t0
    print(f"Exact profiler q={q}, p={p}, s={s}, slot={slot}, D={D}", flush=True)
    chi=charge(slot[0],slot[1],p)
    K_extra=set(range(q,p,q))
    print(f"charge={chi}, K_extra={sorted(K_extra)}, in_extra={chi in K_extra}", flush=True)
    t=stamp('start',t0)
    f1=build_1step_map_exact_through_degree(p,D)
    t=stamp(f'1-step exact built; supports=({len(f1[0])},{len(f1[1])})',t0)
    theta=2*sp.pi/sp.Integer(p)
    lam=sp.simplify(sp.cos(theta)+sp.I*sp.sin(theta))
    lamb=sp.conjugate(lam)
    assert_linear_part_only_degree1(f1[0],f1[1],lam,lamb)
    t=stamp('linear-part sanity passed',t0)
    rem,Phi,S_expr=cyclotomic_zero_sum_remainder(p,chi,s)
    print(f"direct-avg rem={rem}", flush=True)
    t=stamp('direct averaging check done',t0)
    G=({(1,0):sp.Integer(1)},{(0,1):sp.Integer(1)})
    for j in range(1,s+1):
        tj=time.perf_counter()
        G=(ssubst(f1[0],G[0],G[1],D), ssubst(f1[1],G[0],G[1],D))
        print(f"  iter {j}/{s}: supports=({len(G[0])},{len(G[1])}), step={time.perf_counter()-tj:.3f}s, total={time.perf_counter()-t0:.3f}s", flush=True)
    t=stamp('cascade complete',t0)
    R_raw=sscale(G[0], sp.expand(lam**(-s)))
    R_raw[(1,0)]=sp.simplify(R_raw.get((1,0),sp.Integer(0))-sp.Integer(1))
    R={k:v for k,v in sclean(R_raw).items() if sum(k)>=2}
    J=project_extra(R,p,K_extra)
    c=J.get(slot,sp.Integer(0))
    t=stamp(f'projected; J support={len(J)}; raw coeff extracted',t0)
    if not args.no_final_simplify:
        c=sp.simplify(c)
        t=stamp('final simplify done',t0)
    print('coeff =', c, flush=True)
    print('zero? ', is_exact_zero(c), flush=True)

if __name__=='__main__':
    main()
