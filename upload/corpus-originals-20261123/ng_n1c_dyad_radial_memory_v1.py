#!/usr/bin/env python3
"""N-1C-DYAD radial-memory audit for the exact primitive RTG dyad map.

Scope:
  T(rho,eta) = (rho-sin eta, eta + exp(rho)-1-sin eta)
  canonical family (rho0,eta0)=(0,q)
  exact six-step finite iterate T^6

This script provides numerical evidence only.  It does not replace the
DSN's theorem-grade Arb/IA certification pipeline.
"""
import mpmath as mp

mp.mp.dps = 80


def T(rho, eta):
    return rho - mp.sin(eta), eta + (mp.e**rho - 1) - mp.sin(eta)


def iterate(rho, eta, n):
    for _ in range(n):
        rho, eta = T(rho, eta)
    return rho, eta


def q_true(rho, eta):
    # No wrapping occurs in the scoped witness; eta remains in (-pi,pi].
    return rho*rho - rho*eta + eta*eta


def phase_return_residual(q):
    rho6, eta6 = iterate(mp.mpf('0'), q, 6)
    return eta6 - q


def main():
    # A sign-changing bracket for a nontrivial exact six-step phase return.
    qa = mp.mpf('0.31562')
    qb = mp.mpf('0.31563')
    fa = phase_return_residual(qa)
    fb = phase_return_residual(qb)
    assert fa > 0 and fb < 0

    qstar = mp.findroot(phase_return_residual, (qa, qb))
    rho0, eta0 = mp.mpf('0'), qstar
    rho6, eta6 = iterate(rho0, eta0, 6)
    Q0 = q_true(rho0, eta0)
    Q6 = q_true(rho6, eta6)

    # One further primitive step from the two same-phase states.
    _, eta1_from_initial = T(rho0, eta0)
    _, eta1_from_returned = T(rho6, eta6)
    future_phase_split = eta1_from_returned - eta1_from_initial

    print("N-1C-DYAD radial-memory witness")
    print("--------------------------------")
    print(f"bracket residual f({qa}) = {mp.nstr(fa, 25)}")
    print(f"bracket residual f({qb}) = {mp.nstr(fb, 25)}")
    print(f"q*                     = {mp.nstr(qstar, 40)}")
    print(f"eta6-eta0              = {mp.nstr(eta6-eta0, 12)}")
    print(f"rho6                   = {mp.nstr(rho6, 40)}")
    print(f"Q0                     = {mp.nstr(Q0, 40)}")
    print(f"Q6                     = {mp.nstr(Q6, 40)}")
    print(f"Q6-Q0                  = {mp.nstr(Q6-Q0, 40)}")
    print(f"future phase split     = {mp.nstr(future_phase_split, 40)}")
    print(f"exp(rho6)-1            = {mp.nstr(mp.e**rho6-1, 40)}")
    assert abs(eta6-eta0) < mp.mpf('1e-60')
    assert rho6 > 0
    assert Q6 < Q0
    assert abs(future_phase_split - (mp.e**rho6-1)) < mp.mpf('1e-60')

    # Numerical long-block audit from the witness.
    rho, eta = rho0, eta0
    prevQ = q_true(rho, eta)
    monotone = True
    min_drop = None
    blocks = 2000
    for m in range(1, blocks+1):
        rho, eta = iterate(rho, eta, 6)
        Q = q_true(rho, eta)
        drop = prevQ - Q
        if not (Q < prevQ):
            monotone = False
            break
        min_drop = drop if min_drop is None or drop < min_drop else min_drop
        prevQ = Q
    print(f"strict Q decrease over {blocks} blocks (NUM) = {monotone}")
    print(f"Q after {blocks} blocks                    = {mp.nstr(prevQ, 25)}")
    print(f"smallest audited block drop                = {mp.nstr(min_drop, 25)}")
    print("NOTE: long-run monotonicity line is numerical evidence, not a proof for all blocks.")


if __name__ == '__main__':
    main()
