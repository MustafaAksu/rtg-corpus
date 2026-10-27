#!/usr/bin/env python3
"""
tdr24a_ratelaw.py

TDR-24A-R1/R2/R3: decompose cs_rate ~ N^-0.669 into hazard x conditional.

Two candidate conditioning variables tested (v17, run-level bulk, N=480-1440):

(A) Center-deficit D = {C_t <= rho_c * Cbar_N}, rho_c in {0.70..0.85}:
    REJECTED as the natural event variable. The exponent split between P(D)
    and P(cs|D) is threshold-dependent (slides from -0.48/-0.19 at rho=0.70 to
    +0.14/-0.78 at rho=0.85) although the sum stays ~ -0.67. An event definition
    whose decomposition depends on an arbitrary threshold is not structural.

(B) Other-burst B = {O_other_t >= lam * Obar_N}, lam in {2,5,10}:
    ACCEPTED. The split is threshold-STABLE and clean:
        P(B)      ~ N^(-0.07..+0.04)  ~ N^0   (FLAT: bursts occur at a fixed
                                               ~4-9% of steps at every N;
                                               coverage of cs-events 0.85-1.00 across lambda in {2,5,10})
        P(cs|B)   ~ N^(-0.58..-0.61)          (carries the entire exponent)
    => R1 (unlock/burst hazard) is N-INDEPENDENT.
       R2 (clean exposure conditional) carries cs_rate's full N-dependence.

Successful vs sterile bursts (lam=5):
    cs-producing bursts have larger other-floods (1.6-2.2x), stronger center
    depletion (0.83-0.84x), and 3-4x LOWER multistar candidate absorption
    (occ_in_multistar ratio 0.26-0.31). Interpretation: a burst yields a clean
    star only when the shed debris escapes recapture by the multistar -- the
    bottleneck is debris-recapture competition, not shedding frequency.

R3 (attachment): E[occ_in_cs|event] ~ N^+0.766 -- SUBLINEAR vs band (2k+1)~N.
    Not the full-band closure of TDR-24F's q_proj ~ N^1; consistent with
    partial exposure of the band during a one-step event. Recorded as distinct.

REVISED TDR-24A OPEN TARGET:
    Derive P(clean exposure | shedding burst) ~ N^(-0.6) from the recapture
    competition between shed debris and the ~N-wide multistar absorption zone.
    Heuristic: an exposed hub survives classification as clean only if no
    debris fragment lands within its defect band; with debris scattered over
    a region ~N wide and absorption cross-section ~(2k+1) ~ N, a survival
    probability decaying as a power of N is natural -- but the specific
    exponent ~0.6 (vs 1.0) is NOT yet derived. Do not promote past [HEUR].

Exponent caution (per collaborator): -0.669 is "near -2/3, candidate rational,
unproven". The conditional's -0.58..-0.61 differs from -2/3 by more than the
fit scatter; treat all rational identifications as open.
"""

import csv
import math
import argparse
from collections import defaultdict


def bulk_runs(path, tail_threshold):
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    return {r for r, m in rf.items() if m <= tail_threshold}


def load_rows(path, step_min, tail_threshold):
    bulk = bulk_runs(path, tail_threshold)
    rows = []
    N = k = T = None
    policy = "unknown"
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            if v[C["run_id"]] not in bulk: continue
            if int(v[C["step"]]) < step_min: continue
            if N is None:
                N, k = int(v[C["N"]]), int(v[C["k"]])
                T = int(v[C["T"]]) if "T" in C else -1
                policy = v[C["policy"]] if "policy" in C else "unknown"
            rows.append((float(v[C["occ_clean_pairs_other"]]),
                         float(v[C["multistar_centers_total"]]),
                         float(v[C["clean_star_components"]]),
                         float(v[C["occ_clean_pairs_in_multistar"]]),
                         float(v[C["M_pre"]])))
    return (policy, T, round(k / N, 6)), N, rows


def fit(xs, ys):
    lx = [math.log(x) for x in xs]; ly = [math.log(y) for y in ys]
    n = len(lx); mx = sum(lx)/n; my = sum(ly)/n
    sxx = sum((a-mx)**2 for a in lx)
    a = sum((lx[i]-mx)*(ly[i]-my) for i in range(n)) / sxx
    ss = sum((y-my)**2 for y in ly)
    sr = sum((ly[i]-(a*(lx[i]-mx)+my))**2 for i in range(n))
    return a, (1 - sr/ss if ss else 1.0)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--step-min", type=int, default=4001)
    p.add_argument("--tail-threshold", type=float, default=500)
    p.add_argument("--lambdas", type=float, nargs="*", default=[2, 5, 10])
    p.add_argument("--rhos", type=float, nargs="*", default=[0.70, 0.75, 0.80, 0.85])
    args = p.parse_args()

    # Group by analysis slice (policy, T, k/N); pool rows of same-N files within
    # a slice (no silent overwrite); refuse cross-slice fitting.
    slices = {}
    for path in args.csvs:
        slc, N, rows = load_rows(path, args.step_min, args.tail_threshold)
        slices.setdefault(slc, {}).setdefault(N, []).extend(rows)
    if len(slices) > 1:
        print(f"NOTE: {len(slices)} distinct (policy,T,k/N) slices supplied; "
              f"each is analyzed separately below, never mixed.")

    for slc in sorted(slices):
        if len(slices) > 1:
            print(f"\n=== slice (policy, T, k/N) = {slc} ===")
        analyze_slice(slices[slc], args)


def analyze_slice(byN, args):
    R = {}
    for N, rows in byN.items():
        n = len(rows)
        Obar = sum(r[0] for r in rows)/n
        Cbar = sum(r[1] for r in rows)/n
        ncs = sum(1 for r in rows if r[2] > 0)
        res = {"cs_rate": ncs/n}
        for lam in args.lambdas:
            B = [r for r in rows if r[0] >= lam*Obar]
            Bcs = [r for r in B if r[2] > 0]
            res[f"PB_{lam}"] = len(B)/n
            res[f"PcsB_{lam}"] = len(Bcs)/len(B) if B else 0.0
            res[f"coverage_{lam}"] = len(Bcs)/ncs if ncs else 0.0  # P(B | cs)
            # successful-vs-sterile diagnostics at this lambda
            St = [r for r in B if r[2] == 0]
            if Bcs and St:
                m = lambda rs, i: sum(r[i] for r in rs)/len(rs)
                res[f"flood_ratio_{lam}"]    = m(Bcs,0)/m(St,0)
                res[f"center_ratio_{lam}"]   = m(Bcs,1)/m(St,1)
                res[f"recapture_ratio_{lam}"]= m(Bcs,3)/m(St,3) if m(St,3) else float("nan")
        for rho in args.rhos:
            nD = sum(1 for r in rows if r[1] <= rho*Cbar)
            nDcs = sum(1 for r in rows if r[1] <= rho*Cbar and r[2] > 0)
            res[f"PD_{rho}"] = nD/n
            res[f"PcsD_{rho}"] = nDcs/nD if nD else 0.0
        R[N] = res

    Ns = sorted(R)
    a, _ = fit(Ns, [R[N]["cs_rate"] for N in Ns])
    print(f"cs_rate ~ N^{a:+.3f}\n")
    print("Other-burst conditioning (B):")
    for lam in args.lambdas:
        aB, rB = fit(Ns, [R[N][f"PB_{lam}"] for N in Ns])
        aC, rC = fit(Ns, [R[N][f"PcsB_{lam}"] for N in Ns])
        covs = [R[N][f"coverage_{lam}"] for N in Ns]
        print(f"  lam={lam:>4}: P(B)~N^{aB:+.3f}(R²{rB:.2f})  "
              f"P(cs|B)~N^{aC:+.3f}(R²{rC:.2f})  sum={aB+aC:+.3f}  "
              f"P(B|cs)={min(covs):.2f}-{max(covs):.2f}")
    print("\nSuccessful-vs-sterile burst diagnostics (ratios cs-burst/sterile):")
    print(f"{'N':>6} {'lam':>5} {'flood':>7} {'centers':>8} {'recapture':>10}")
    for N in Ns:
        for lam in args.lambdas:
            if f"flood_ratio_{lam}" in R[N]:
                print(f"{N:>6} {lam:>5} {R[N][f'flood_ratio_{lam}']:>7.2f} "
                      f"{R[N][f'center_ratio_{lam}']:>8.2f} "
                      f"{R[N][f'recapture_ratio_{lam}']:>10.2f}")
    print("Center-deficit conditioning (D) [threshold-dependent — diagnostic only]:")
    for rho in args.rhos:
        aD, rD = fit(Ns, [R[N][f"PD_{rho}"] for N in Ns])
        aC, rC = fit(Ns, [R[N][f"PcsD_{rho}"] for N in Ns])
        print(f"  rho={rho}: P(D)~N^{aD:+.3f}(R²{rD:.2f})  "
              f"P(cs|D)~N^{aC:+.3f}(R²{rC:.2f})  sum={aD+aC:+.3f}")


if __name__ == "__main__":
    main()
