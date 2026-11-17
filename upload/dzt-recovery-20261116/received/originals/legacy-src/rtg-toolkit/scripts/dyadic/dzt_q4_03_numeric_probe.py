#!/usr/bin/env python3
"""Numeric q=4,(0,3) subgroup-strobe probe using canonical rtg_p_* engine.
Status: NUM diagnostic only; exact certificates must use rtg_p_horizon_audit.py certify.
"""
import argparse, math, sys, os
import rtg_p_core as core
import rtg_p_subgroup as subgroup


def q403_value_numeric(p:int, D:int=4, tol:float=1e-12):
    q=4
    if p % q != 0:
        raise ValueError(f"p={p} is not divisible by q=4")
    s = p//q
    f1 = core.build_1step_map(p,D,tol)
    fs = core.iterate_map(f1,s,D,tol)
    lam, *_ = core.nconstants(p)
    R_raw = core.nscale(fs[0], lam**(-s), 0.0)
    R_raw[(1,0)] = R_raw.get((1,0),0.0j)-1.0
    R = {k:v for k,v in core.nclean(R_raw,tol).items() if sum(k)>=2}
    K_extra = subgroup.extra_charges_for_subgroup(p,q)
    J = subgroup.project_by_charge(R,p,K_extra)
    return J.get((0,3),0.0j), len(J), sorted(J.keys(), key=lambda k:(sum(k),k))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--p', nargs='+', type=int, required=True)
    ap.add_argument('--D', type=int, default=4)
    ap.add_argument('--tol', type=float, default=1e-12)
    args=ap.parse_args()
    print('q=4,(0,3) numeric diagnostic from canonical raw R=lambda^-s f_p^s - Id')
    print('Status: NUM diagnostic only; use exact certify cases for ALG.')
    for p in args.p:
        v, supp, active = q403_value_numeric(p,args.D,args.tol)
        print(f"p={p:>3} s={p//4:>3} coeff(0,3) = {v.real:+.16e} {v.imag:+.16e}i |abs|={abs(v):.16e} supp={supp}")

if __name__=='__main__':
    main()
