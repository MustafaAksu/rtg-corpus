#!/usr/bin/env python3
# RF-06 spot check for the Number Genesis / DISC route (finite sample, NOT a proof).
# Question: is the owner TDR-G rule (genesis_mode_b_mc_v18.py, pinned 9d787b43...) equivariant
# under a COMMON token shift delta_i -> delta_i + c on the 3-node route used by DISC
# (phase advance, SWAP, P3 path-cycle), for every c in Z_24 and k in {0,1,2,3}?
# If yes, the DISC gauge-reduced 4-tuple (theta diffs, delta diffs) is a legitimate state key.
import importlib.util, random, sys, hashlib
F = "genesis_mode_b_mc_v18.py"
assert hashlib.sha256(open(F, "rb").read()).hexdigest().startswith("9d787b43")
spec = importlib.util.spec_from_file_location("G", F); G = importlib.util.module_from_spec(spec)
sys.modules["G"] = G; spec.loader.exec_module(G)
N = 24; rng = random.Random(20260930)
red = lambda u: ((u.theta[0]-u.theta[1]) % N, (u.theta[0]-u.theta[2]) % N,
                 (u.delta[0]-u.delta[1]) % N, (u.delta[0]-u.delta[2]) % N)
bad = 0
for k in (0, 1, 2, 3):
    t = b = m = a = 0
    for _ in range(2500):
        th = {i: rng.randrange(N) for i in range(3)}; dl = {i: rng.randrange(N) for i in range(3)}
        u0 = G.Universe(N=N, k=k, theta=dict(th), delta=dict(dl)); G.step_universe(u0, multistar_policy="bound_symmetric")
        if len(u0.theta) != 3 or u0.births: b += 1; continue
        for c in range(1, N):
            u1 = G.Universe(N=N, k=k, theta=dict(th), delta={i: (dl[i]+c) % N for i in range(3)})
            G.step_universe(u1, multistar_policy="bound_symmetric"); t += 1
            if len(u1.theta) != 3 or u1.births or red(u1) != red(u0): m += 1
            if any((u1.delta[i]-u0.delta[i]) % N != c for i in range(3)): a += 1
    bad += m + a
    print(f"k={k}: shifted runs {t} | birth/star steps {b} | reduced-key mismatches {m} | tokens not shifted by c {a}")
print("EQUIVARIANT ON SAMPLE" if bad == 0 else "EQUIVARIANCE VIOLATED"); sys.exit(0 if bad == 0 else 1)
