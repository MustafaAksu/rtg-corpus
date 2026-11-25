#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
run_phase2_baseline.py — scientific Phase-2 baseline for TDR-G defect graphs.

Per audit spec:
  - export real TDR-G runs at N,k,policy over several seeds
  - objects: Core_G_T (= DEF-AZ-CORE by PROP-AZ-CORE-EQUIV), G_cumulative
  - null: degree-EXACT directed double-edge-swap (az_v5), not stub-matching
  - radius: corrected ARPACK (spectral_radius_patch)
  - statistic: R_max over Q_N (frozen q_max=24), empirical p vs null R_max
  - emit a full CONV-AZ-MANIFEST per (seed,object) and an aggregate report

Status of outputs: [NUM diagnostic] [scope: stated N only, Null0 degree-exact].
NOT candidate-level (single null type; mechanism open).
"""
from __future__ import annotations
import sys, os, json, argparse, hashlib
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "lib"))

import genesis_mode_b_mc_graph_export as sim
from conv_az_graph_export import build_export, write_export, recurrent_core_directed
from spectral_radius_patch import hashimoto_spectral_radius as R_arpack
from hashimoto import hashimoto_spectrum_full, R_max as R_max_full, divisor_set
from phase2_harness import directed_config_null  # Null0: degree-exact directed swap


EPS_ANGLE_DEFAULT = 1e-10


def reciprocal_pair_swap(edges, rng, max_tries=200):
    """
    Null1: reciprocal-pair-preserving degree-exact swap.

    Operates on UNDIRECTED edges (each present as both orientations in `edges`).
    A double-edge swap on undirected edges {a,b},{c,d} -> {a,d},{c,b} is applied,
    then BOTH orientations are emitted. This preserves the bidirected (reciprocal-pair)
    structure exactly, so it factors out the export-convention symmetry that Null0
    does not. Only the TDR-G-specific arrangement of pairs is randomized.
    """
    # collapse to undirected set
    und = set()
    for a, b in edges:
        if a != b:
            und.add(tuple(sorted((a, b))))
    U = [list(e) for e in und]
    m = len(U)
    if m < 2:
        return list(edges)
    uset = set(map(tuple, U))
    n_swaps = 10 * m
    done = 0
    tries = 0
    while done < n_swaps and tries < n_swaps * max_tries:
        tries += 1
        i, j = rng.integers(0, m), rng.integers(0, m)
        if i == j:
            continue
        a, b = U[i]
        c, d = U[j]
        # rewire {a,b},{c,d} -> {a,d},{c,b}
        if len({a, b, c, d}) < 4:
            continue
        e1 = tuple(sorted((a, d)))
        e2 = tuple(sorted((c, b)))
        if e1 in uset or e2 in uset:
            continue
        uset.discard(tuple(sorted((a, b)))); uset.discard(tuple(sorted((c, d))))
        uset.add(e1); uset.add(e2)
        U[i] = list(e1); U[j] = list(e2)
        done += 1
    # emit both orientations
    out = []
    for a, b in uset:
        out.append((a, b)); out.append((b, a))
    return out


NULL_MODELS = {
    "degree_exact_swap": directed_config_null,            # Null0
    "reciprocal_pair_preserving_swap": reciprocal_pair_swap,  # Null1
}


def theta_relabel_null(edges, rng):
    """
    Null3-lite (theta-geometry null): rebuild a defect graph from a RANDOM theta
    assignment on Z_N with the same number of nodes, using the SAME antipodal
    defect rule (|theta_a - theta_b - N/2| <= k). This preserves the Z_N geometry
    and node count but destroys the TDR-G dynamical arrangement of theta values.

    If the 4|q rule SURVIVES this null, it is intrinsic to the antipodal-band
    geometry on Z_N (static). If it DISAPPEARS, the rule is dynamical (TDR-G
    advance trajectory), which would be the stronger arithmetic claim.

    NOTE: requires N and k, passed via closure (see make_theta_null).
    """
    raise NotImplementedError("use make_theta_null(N,k) to bind geometry")


def make_theta_null(N, k):
    """Bind N,k to produce a theta-relabel null callable (RAW antipodal graph)."""
    def _null(edges, rng):
        # infer node count from the observed graph
        nodes = sorted({x for e in edges for x in e})
        n = len(nodes)
        if n == 0:
            return []
        # assign random distinct theta in Z_N
        if n > N:
            n = N
        thetas = list(rng.choice(N, size=n, replace=False))
        # antipodal defect rule
        half = N // 2
        out = []
        for i in range(n):
            for j in range(i + 1, n):
                d = (thetas[i] - thetas[j]) % N
                dd = ((d - half) + N) % N
                # signed centered distance from antipode
                sc = dd - N if dd > half else dd
                if abs(sc) <= k:
                    a, b = nodes[i], nodes[j]
                    out.append((a, b)); out.append((b, a))
        return out
    return _null


def make_theta_core_null(N, k):
    """
    Core-MATCHED theta null (per audit): build the raw random-theta antipodal graph,
    then pass it through the SAME core extraction as the observed object, so the
    comparison is Core(G_T) vs Core(random-theta antipodal graph), not vs the raw graph.
    By PROP-AZ-CORE-EQUIV the 2-core re-directed = DEF-AZ-CORE under both-orientations.
    """
    raw_null = make_theta_null(N, k)
    def _null(edges, rng):
        raw = raw_null(edges, rng)
        if not raw:
            return []
        return recurrent_core_directed(raw)
    return _null


def export_run(N, k, T, seed, policy, out_dir):
    import random
    rng = random.Random(seed)
    u = sim.init_universe(N=N, k=k, rng=rng, exclude_zero_delta=False)
    eh, nh, bt = [], [], []
    prev = int(u.births)
    for _ in range(T):
        if len(u.theta) >= 10000:
            break
        sim.step_universe(u, multistar_policy=policy, collect_motif=False)
        nodes = sorted(int(n) for n in u.theta.keys())
        edges = sorted(sim.graph_edges_for(nodes, u.theta, u.N, u.k))
        eh.append([(int(a), int(b)) for a, b in edges]); nh.append(nodes)
        if int(u.births) > prev:
            for _ in range(int(u.births) - prev):
                bt.append(len(eh) - 1)
            prev = int(u.births)
    run_id = f"N{N}_k{k}_{policy}_r{seed}"
    export = build_export(eh, bt, nh, N=N, k=k, policy=policy, run_id=run_id, T=T, seed=seed)
    write_export(export, out_dir)
    return export, run_id


def directed_edges_of(obj):
    return [(int(a), int(b)) for a, b in obj["directed_edges"]]


def R_max_arpack_on_eigs(edges, N, q_max=24, eps_angle=EPS_ANGLE_DEFAULT):
    """R_q over eigenvalue angles, EXCLUDING near-zero eigenvalues (CONV-AZ-ANGLE-ZERO).
    Radius is dense full-spectrum here (core sizes small); ARPACK is the large-graph path."""
    if not edges:
        return 0.0, -1, 0.0, 0, 0
    eigs_all = hashimoto_spectrum_full(edges)
    n_total = len(eigs_all)
    eigs = eigs_all[np.abs(eigs_all) > eps_angle]   # drop zero eigenvalues
    n_used = len(eigs)
    if n_used == 0:
        return 0.0, -1, 0.0, n_total, 0
    rmax, argq = R_max_full(eigs, N, q_max)
    rho = float(np.max(np.abs(eigs_all)))  # dense full-spectrum radius
    return rmax, argq, rho, n_total, n_used


def per_q_table(edges, N, q_max=24, eps_angle=EPS_ANGLE_DEFAULT):
    from hashimoto import R_q
    eigs_all = hashimoto_spectrum_full(edges)
    eigs = eigs_all[np.abs(eigs_all) > eps_angle]
    return {q: (R_q(eigs, q) if len(eigs) else 0.0) for q in divisor_set(N, q_max)}


def run_diagnostic(edges, N, n_nulls, seed, null_fn, q_max=24,
                   eps_angle=EPS_ANGLE_DEFAULT, emit_per_q=False):
    """Observed R_max + chosen-null distribution + empirical p. Optional per-q table."""
    from hashimoto import R_q
    rng = np.random.default_rng(seed)
    obs_rmax, obs_q, obs_rho, n_tot, n_used = R_max_arpack_on_eigs(edges, N, q_max, eps_angle)
    Q = divisor_set(N, q_max)
    obs_per_q = per_q_table(edges, N, q_max, eps_angle) if emit_per_q else None

    null_rmax = []
    null_per_q = {q: [] for q in Q} if emit_per_q else None
    for _ in range(n_nulls):
        ne = null_fn(edges, rng)
        if not ne:
            continue
        rm, _, _, _, _ = R_max_arpack_on_eigs(ne, N, q_max, eps_angle)
        null_rmax.append(rm)
        if emit_per_q:
            eigs_all = hashimoto_spectrum_full(ne)
            eigs = eigs_all[np.abs(eigs_all) > eps_angle]
            for q in Q:
                null_per_q[q].append(R_q(eigs, q) if len(eigs) else 0.0)
    null_rmax = np.array(null_rmax)
    p = (1 + int(np.sum(null_rmax >= obs_rmax - 1e-12))) / (1 + len(null_rmax))

    out = {
        "R_max_obs": obs_rmax, "R_max_argq": int(obs_q), "rho_B": obs_rho,
        "n_eigs_total": int(n_tot), "n_eigs_used": int(n_used),
        "null_mean": float(null_rmax.mean()) if len(null_rmax) else None,
        "null_sd": float(null_rmax.std()) if len(null_rmax) else None,
        "n_nulls": int(len(null_rmax)),
        "p_emp": float(p),
        "ratio": float(obs_rmax / null_rmax.mean()) if len(null_rmax) and null_rmax.mean() > 0 else None,
    }
    if emit_per_q:
        pq = {}
        for q in Q:
            arr = np.array(null_per_q[q])
            nm = float(arr.mean()); ns = float(arr.std())
            z = (obs_per_q[q] - nm) / ns if ns > 0 else 0.0
            pv = (1 + int(np.sum(arr >= obs_per_q[q] - 1e-12))) / (1 + len(arr))
            pq[str(q)] = {"obs": obs_per_q[q], "null_mean": nm, "null_sd": ns,
                          "z": z, "p_emp": pv}
        out["per_q"] = pq
    return out


def full_manifest(N, k, policy, T, seed, obj_name, edges, stats, run_id, paths):
    kn = k / N
    return {
        "run_id": f"{run_id}__{obj_name}",
        "N": N, "k": k, "k_over_N_actual": kn,
        "regime": "B1" if (N % 30 == 0 and k == N // 15) else "B2",
        "canonical_scaling": (N % 30 == 0 and k == N // 15),
        "policy": policy, "T": T, "seed": seed,
        "graph_export": {"type": "recurrent_core" if "Core" in obj_name else "cumulative",
                         "directed_edges": "both_orientations",
                         "multiedges_allowed": False, "selfloops_allowed": False},
        "hashimoto": {"script_version": "az_v5+patch", "spectrum_mode": "full-spectrum",
                      "eigensolver": "dense_for_Rq+arpack_for_radius", "tolerance": 1e-10},
        "nulls": {"null0_count": stats["n_nulls"]},
        "statistics": {"rho_B": stats["rho_B"], "R_max": stats["R_max_obs"],
                       "R_max_argq": stats["R_max_argq"], "p_emp": stats["p_emp"],
                       "ratio": stats["ratio"]},
        "artifact_paths": paths,
        "null_model": "degree_exact_double_edge_swap",
    }


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=120)
    ap.add_argument("--k", type=int, default=8)
    ap.add_argument("--policy", default="bound_symmetric")
    ap.add_argument("--T", type=int, default=1000)
    ap.add_argument("--seeds", type=int, nargs="+", default=[1, 2, 3])
    ap.add_argument("--objects", nargs="+", default=["Core_G_T", "G_cumulative"])
    ap.add_argument("--nulls", type=int, default=1000)
    ap.add_argument("--null-model", default="degree_exact_swap",
                    choices=list(NULL_MODELS.keys()) + ["theta_geometry", "theta_core_geometry"])
    ap.add_argument("--emit-per-q", action="store_true")
    ap.add_argument("--eps-angle", type=float, default=EPS_ANGLE_DEFAULT)
    ap.add_argument("--out-dir", default="phase2_baseline")
    ap.add_argument("--export-report", default="AZ_PHASE2_N120_BASELINE_v1.json")
    args = ap.parse_args(argv)

    null_choice = args.null_model
    if null_choice == "theta_geometry":
        null_fn = make_theta_null(args.N, args.k)
    elif null_choice == "theta_core_geometry":
        null_fn = make_theta_core_null(args.N, args.k)
    else:
        null_fn = NULL_MODELS[null_choice]
    os.makedirs(args.out_dir, exist_ok=True)
    report = {"params": vars(args), "runs": [], "null_model": args.null_model,
              "radius": "dense_full_spectrum", "eps_angle": args.eps_angle,
              "status": "[NUM diagnostic]"}

    for seed in args.seeds:
        export, run_id = export_run(args.N, args.k, args.T, seed, args.policy, args.out_dir)
        objmap = {"Core_G_T": export["objects"]["Core(G_T)"],
                  "G_T": export["objects"]["G_T"],
                  "G_cumulative": export["objects"]["G_cumulative"]}
        for obj_name in args.objects:
            obj = objmap[obj_name]
            edges = directed_edges_of(obj)
            stats = run_diagnostic(edges, args.N, args.nulls, seed, null_fn,
                                   eps_angle=args.eps_angle, emit_per_q=args.emit_per_q)
            man = full_manifest(args.N, args.k, args.policy, args.T, seed,
                                obj_name, edges, stats, run_id,
                                {obj_name: f"{run_id}__{obj_name.replace('(','_').replace(')','')}.json"})
            man["null_model"] = args.null_model
            mpath = os.path.join(args.out_dir, f"{run_id}__{obj_name}__AZmanifest.json")
            json.dump(man, open(mpath, "w"), indent=2)
            report["runs"].append({"seed": seed, "object": obj_name,
                                   "n_edges": len(edges), **stats,
                                   "manifest": os.path.basename(mpath)})
            print(f"seed {seed} {obj_name:<13} edges={len(edges):>5} "
                  f"n_eig={stats['n_eigs_used']}/{stats['n_eigs_total']} "
                  f"R_max={stats['R_max_obs']:.4f} null={stats['null_mean']:.4f} "
                  f"ratio={stats['ratio']:.3f} p={stats['p_emp']:.4f} "
                  f"[{args.null_model}, n_null={stats['n_nulls']}]")

    rpath = os.path.join(args.out_dir, args.export_report)
    json.dump(report, open(rpath, "w"), indent=2)
    print(f"\nreport -> {rpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
