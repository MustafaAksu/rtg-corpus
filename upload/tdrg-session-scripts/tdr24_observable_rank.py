#!/usr/bin/env python3
"""
tdr24_observable_rank.py

Formal rank test of the TDR-24 observable map over the control manifold (log N, log k/N).

PURPOSE (review-directed): the field-count question ("one latent scaling direction or
several independent fields?") is non-identifiable on a rank-deficient experimental
design. This tool measures the rank of the observable Jacobian directly, so field count
becomes an empirical readout instead of an interpretation:

  - Build the matrix L[i,c] = log(observable_i) at cell c.
  - Regress each observable on the control coordinates (log N, log k/N).
  - The rank of the fitted sensitivity (Jacobian) matrix d log O / d (log N, log k/N),
    and the singular-value spectrum of the centered observable matrix, give the number
    of resolvable independent scaling directions.

ON THE CURRENT v17 CORPUS (k/N = 1/15 everywhere): the control manifold is rank 1
(only log N varies; log k/N is constant). Therefore the observable map can express AT
MOST one resolvable scaling direction, REGARDLESS of the true field count. This is a
property of the experimental design (rank deficiency), not of the physics. The tool
reports this explicitly and refuses to claim a field count > control-manifold rank.

DECISIVE EXTENSION: supply cells spanning multiple k/N (e.g. {1/30, 1/15, 1/8}). Then
the control manifold is rank 2 and the observable Jacobian's rank becomes meaningful:
  rank 1  -> single latent scaling direction (chi, C_component, C_birth all co-vary);
  rank 2  -> two genuinely independent scaling fields (orthogonal sensitivities).

Branch-local TDR-G diagnostic [NUM]; nothing here is promoted or cross-branch.
"""

import csv
import math
import argparse
from collections import defaultdict

OBSERVABLES = {
    "occ_per_row":     lambda a: a["occ"] / a["rows"],
    "occ_in_cs_per_row": lambda a: a["oic"] / a["rows"],
    "cs_per_row":      lambda a: a["cs"] / a["rows"],
    "oims_per_row":    lambda a: a["oims"] / a["rows"],
    "chi":             lambda a: a["oic"] / a["cs"],
    "C_component":     lambda a: a["oic"] / a["occ"],
    "C_birth":         lambda a: a["births"] / a["occ"],
}


def pools(path, step_min=4001, tail_threshold=500):
    rf = {}
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            rid = v[C["run_id"]]; mp = float(v[C["M_post"]])
            if mp > rf.get(rid, 0): rf[rid] = mp
    bulk = {r for r, m in rf.items() if m <= tail_threshold}
    a = defaultdict(float)
    with open(path) as f:
        h = f.readline().strip().split(","); C = {c: i for i, c in enumerate(h)}
        for line in f:
            v = line.rstrip("\r\n").split(",")
            if v[C["run_id"]] not in bulk: continue
            if int(v[C["step"]]) < step_min: continue
            a["oic"] += float(v[C["occ_clean_pairs_in_clean_star"]])
            a["occ"] += float(v[C["occ_clean_pairs"]])
            a["cs"] += float(v[C["clean_star_components"]])
            a["oims"] += float(v[C["occ_clean_pairs_in_multistar"]])
            a["births"] += float(v[C["births_step"]])
            a["rows"] += 1
            if a["N"] == 0:
                a["N"] = int(v[C["N"]]); a["k"] = int(v[C["k"]])
    return a


def svd_singular_values(M):
    """Singular values of M (rows x cols) via eigenvalues of M^T M (Jacobi), no numpy."""
    rows = len(M); cols = len(M[0]) if rows else 0
    # A = M^T M  (cols x cols)
    A = [[sum(M[r][i] * M[r][j] for r in range(rows)) for j in range(cols)]
         for i in range(cols)]
    n = cols
    V = [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]
    for _ in range(100):
        off = 0.0; p = q = 0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(A[i][j]) > off:
                    off = abs(A[i][j]); p, q = i, j
        if off < 1e-14:
            break
        app, aqq, apq = A[p][p], A[q][q], A[p][q]
        phi = 0.5 * math.atan2(2 * apq, aqq - app) if (aqq - app) else math.pi / 4
        c, s = math.cos(phi), math.sin(phi)
        for i in range(n):
            aip, aiq = A[i][p], A[i][q]
            A[i][p] = c * aip - s * aiq; A[i][q] = s * aip + c * aiq
        for i in range(n):
            api, aqi = A[p][i], A[q][i]
            A[p][i] = c * api - s * aqi; A[q][i] = s * api + c * aqi
    eig = sorted((max(A[i][i], 0.0) for i in range(n)), reverse=True)
    return [math.sqrt(e) for e in eig]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("csvs", nargs="+")
    p.add_argument("--step-min", type=int, default=4001)
    p.add_argument("--tail-threshold", type=float, default=500)
    p.add_argument("--svd-tol", type=float, default=0.05,
                   help="singular value threshold (fraction of largest) for rank count")
    args = p.parse_args()

    cells = []
    for path in args.csvs:
        a = pools(path, args.step_min, args.tail_threshold)
        cells.append(a)
    cells.sort(key=lambda a: (a["k"] / a["N"], a["N"]))

    logN = [math.log(a["N"]) for a in cells]
    logkN = [math.log(a["k"] / a["N"]) for a in cells]
    n_kN = len({round(x, 6) for x in logkN})
    control_rank = (1 if len({round(x, 6) for x in logN}) > 1 else 0) + (1 if n_kN > 1 else 0)

    print(f"Cells ({len(cells)}): " +
          ", ".join(f"N={a['N']},k/N={a['k']/a['N']:.4f}" for a in cells))
    print(f"Control manifold rank: {control_rank} "
          f"(distinct k/N = {n_kN})")
    print()

    # centered log-observable matrix: rows=cells, cols=observables
    names = list(OBSERVABLES)
    L = [[math.log(OBSERVABLES[nm](a)) for nm in names] for a in cells]
    means = [sum(L[r][j] for r in range(len(cells))) / len(cells) for j in range(len(names))]
    Lc = [[L[r][j] - means[j] for j in range(len(names))] for r in range(len(cells))]

    sv = svd_singular_values(Lc)
    s0 = sv[0] if sv else 0.0
    obs_rank = sum(1 for s in sv if s0 and s / s0 >= args.svd_tol)
    print("Centered log-observable singular values:",
          ", ".join(f"{s:.3f}" for s in sv))
    print(f"Observable matrix effective rank (tol {args.svd_tol}): {obs_rank}")
    print()

    resolvable = min(obs_rank, control_rank) if control_rank else 0
    print(f"RESOLVABLE independent scaling directions = min(obs_rank, control_rank) "
          f"= {resolvable}")
    if control_rank <= 1:
        print("  => Design is rank-deficient (single control lever). Field count is "
              "NON-IDENTIFIABLE: at most one scaling direction is resolvable regardless "
              "of true physics. Supply multiple k/N to lift the degeneracy.")
    else:
        print("  => Multi-lever design: observable rank is now physically meaningful "
              "(rank 1 = single latent; rank >=2 = independent fields).")


if __name__ == "__main__":
    main()
