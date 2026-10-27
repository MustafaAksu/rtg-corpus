#!/usr/bin/env python3
"""
dynamical_extractor.py  —  trajectory-level observable layer for the response-tensor branch.

[RID: TDRG-RESPONSE-TENSOR / dynamical layer]  [BRANCH/NUM diagnostic]

Motivation (Zeta-side finding + review): the STATIC per-cell observables (C_birth, chi,
ms_abs, ...) may be geometry-saturated projections of a richer trajectory process. If the
system hides degrees of freedom, they appear in TIME correlations before they appear in
static scaling laws. So this module extracts DYNAMICAL INVARIANTS of each run's trajectory
and exposes them as a SEPARATE signal layer.

STRICT CONSTRAINT (review): these features are NOT fed into the static exponent pipeline.
They form their own layer with its own rank test, so we never recompress dynamics back into
static rank artifacts.

Per-cell dynamical invariants (pooled/averaged over the cell's bulk runs):
  - autocorrelation decay time of births_step(t) and occ_clean(t) trajectories
  - event-clustering: Fano factor (var/mean) of births in fixed windows (burstiness)
  - inter-birth interval coefficient of variation (CV; Poisson=1, clustered>1)
  - lag-1..L cross-correlation between births(t) and occupancy(t)
  - trajectory-covariance rank: rank of the per-run covariance of the observable
    time-series (how many independent temporal modes a single run carries)

These are deliberately NOT means/exponents/fits — they are stochastic-process descriptors
that can survive geometry saturation.

The KEY TEST this enables (review's success criterion): does the DYNAMICAL response tensor
have higher null-gated intrinsic rank than the STATIC one on the same cells? If yes, the
static layer was collapsing real degrees of freedom; if no, the saturation is in the system,
not the projection.
"""

from __future__ import annotations

import csv
import math
from collections import defaultdict


def load_run_series(path, tail_threshold=500, step_min=1):
    """Return {run_id: {'births':[...], 'occ':[...], 'cs':[...], 'ms':[...]}} for bulk runs."""
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    bulk = {r for r, m in rf.items() if m <= tail_threshold}
    series = defaultdict(lambda: {"births": [], "occ": [], "cs": [], "ms": [], "step": []})
    meta = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]
            if rid not in bulk: continue
            step = int(v[C["step"]])
            if step < step_min: continue
            s = series[rid]
            s["step"].append(step)
            s["births"].append(float(v[C["births_step"]]))
            s["occ"].append(float(v[C["occ_clean_pairs"]]))
            s["cs"].append(float(v[C["clean_star_components"]]))
            s["ms"].append(float(v[C["multistar_components"]]))
            if not meta:
                meta = {"N": int(v[C["N"]]), "k": int(v[C["k"]]),
                        "policy": v[C["policy"]] if "policy" in C else "unknown"}
    return series, meta


def _autocorr_time(x, max_lag=50):
    """Integrated autocorrelation time (sum of positive autocorrelations)."""
    n = len(x)
    if n < 10: return 0.0
    m = sum(x)/n
    var = sum((xi-m)**2 for xi in x)/n
    if var <= 0: return 0.0
    tau = 0.5
    for lag in range(1, min(max_lag, n//2)):
        c = sum((x[i]-m)*(x[i+lag]-m) for i in range(n-lag))/((n-lag)*var)
        if c <= 0: break
        tau += c
    return tau


def _fano(x, window=50):
    """Fano factor: var/mean of counts in fixed windows (burstiness; Poisson=1)."""
    if len(x) < window: return float("nan")
    sums = [sum(x[i:i+window]) for i in range(0, len(x)-window, window)]
    if len(sums) < 2: return float("nan")
    m = sum(sums)/len(sums)
    if m <= 0: return float("nan")
    var = sum((s-m)**2 for s in sums)/len(sums)
    return var/m


def _interevent_cv(births):
    """Coefficient of variation of inter-birth intervals (clustering; Poisson=1)."""
    idx = [i for i, b in enumerate(births) if b > 0]
    if len(idx) < 3: return float("nan")
    iv = [idx[i+1]-idx[i] for i in range(len(idx)-1)]
    m = sum(iv)/len(iv)
    if m <= 0: return float("nan")
    sd = math.sqrt(sum((x-m)**2 for x in iv)/len(iv))
    return sd/m


def _lag_xcorr(x, y, lag):
    """Cross-correlation of x(t) and y(t+lag)."""
    n = min(len(x), len(y)) - abs(lag)
    if n < 10: return 0.0
    if lag >= 0:
        xa = x[:n]; ya = y[lag:lag+n]
    else:
        xa = x[-lag:-lag+n]; ya = y[:n]
    mx = sum(xa)/n; my = sum(ya)/n
    sx = math.sqrt(sum((a-mx)**2 for a in xa)/n)
    sy = math.sqrt(sum((b-my)**2 for b in ya)/n)
    if sx <= 0 or sy <= 0: return 0.0
    return sum((xa[i]-mx)*(ya[i]-my) for i in range(n))/(n*sx*sy)


def cell_dynamical_features(path, tail_threshold=500, step_min=1001):
    """Per-cell dynamical invariants, averaged over bulk runs (late window default)."""
    series, meta = load_run_series(path, tail_threshold, step_min)
    if not series:
        return None
    feats = defaultdict(list)
    for rid, s in series.items():
        if len(s["births"]) < 100: continue
        feats["tau_births"].append(_autocorr_time(s["births"]))
        feats["tau_occ"].append(_autocorr_time(s["occ"]))
        feats["fano_births"].append(_fano(s["births"]))
        feats["cv_interbirth"].append(_interevent_cv(s["births"]))
        feats["xcorr_bo_lag0"].append(_lag_xcorr(s["births"], s["occ"], 0))
        feats["xcorr_bo_lag1"].append(_lag_xcorr(s["births"], s["occ"], 1))
        feats["xcorr_bo_lagm1"].append(_lag_xcorr(s["births"], s["occ"], -1))
        feats["tau_cs"].append(_autocorr_time(s["cs"]))
    # average over runs, dropping nans
    out = {}
    for kk, vals in feats.items():
        v = [x for x in vals if not (isinstance(x, float) and math.isnan(x))]
        out[kk] = sum(v)/len(v) if v else float("nan")
    return {**meta, "k_over_N": meta["k"]/meta["N"], "obs": out, "n_runs": len(series)}


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("usage: dynamical_extractor.py motif_*.csv"); sys.exit(2)
    print(f"{'N':>5} {'tau_b':>7} {'tau_occ':>8} {'fano_b':>8} {'cv_ib':>7} "
          f"{'xc_l0':>7} {'xc_l1':>7} {'xc_lm1':>7} {'tau_cs':>7}")
    for p in [a for a in sys.argv[1:] if a.endswith(".csv")]:
        c = cell_dynamical_features(p)
        if not c: continue
        o = c["obs"]
        print(f"{c['N']:>5} {o['tau_births']:>7.2f} {o['tau_occ']:>8.2f} "
              f"{o['fano_births']:>8.2f} {o['cv_interbirth']:>7.2f} "
              f"{o['xcorr_bo_lag0']:>7.3f} {o['xcorr_bo_lag1']:>7.3f} "
              f"{o['xcorr_bo_lagm1']:>7.3f} {o['tau_cs']:>7.2f}")
