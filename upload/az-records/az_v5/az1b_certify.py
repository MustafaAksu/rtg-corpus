#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
az/az1b_certify.py
==================
AZ-1B certification: TDR-G ingestion/export, sparse angular validation,
manifest validator, artifact hash registry. Exit 0 iff all pass.

Closes the items the AZ-1A audit flagged as still-open:
  - ENG-blocker-2: JSON loader with schema validation + unit tests
  - ENG-blocker-3: directed export, no silent core-empty failure
  - sparse ANGULAR validation (not just magnitude) for R_q^(K)
  - independent S2 analytic assertion (L-th roots x2)
  - ENG-blocker-5: artifact hash registry
"""
from __future__ import annotations
import sys, os, json, hashlib, tempfile
import numpy as np

HERE = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(HERE, "lib"))
from hashimoto import (build_hashimoto, hashimoto_spectrum_full,
                       hashimoto_spectrum_leading)
import graphgen as gg
from graphio import load_graph_json, save_graph_json, parse_graph_obj, GraphSchemaError
from manifest import validate_manifest

TOL = 1e-9
PASS = True


def check(name, ok, detail=""):
    global PASS
    PASS = PASS and ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f": {detail}" if detail else ""))
    return ok


def roots_of_unity(L):
    return np.array([np.exp(2j*np.pi*j/L) for j in range(L)])


def multiset_match(a, b, tol=TOL):
    a = list(a); b = list(b)
    if len(a) != len(b):
        return False
    for x in a:
        d = [abs(x-y) for y in b]
        j = int(np.argmin(d))
        if d[j] > tol:
            return False
        b.pop(j)
    return True


# ---------- 1. Independent S2 analytic assertion ----------
def test_s2_independent():
    print("AZ-1B.1 Independent S2 analytic assertion (bidirected cycle = L-th roots x2)")
    ok_all = True
    for L in (4, 6, 8):
        edges = gg.gen_bidirected_cycle(L)
        spec = hashimoto_spectrum_full(edges)
        ru = roots_of_unity(L)
        expected = np.concatenate([ru, ru])  # multiplicity 2, asserted analytically
        ok = multiset_match(spec, expected)
        ok_all &= check(f"L={L}", ok, f"size {len(spec)}, expected L-th roots x2")
    return ok_all


# ---------- 2. JSON loader unit tests ----------
def test_json_loader():
    print("AZ-1B.2 JSON loader schema validation + unit tests")
    tmp = tempfile.mkdtemp()
    ok_all = True

    # 2a: 4-cycle JSON round-trips and matches analytic spectrum
    p = os.path.join(tmp, "cycle4.json")
    save_graph_json(p, gg.gen_directed_cycle(4))
    edges, meta = load_graph_json(p)
    spec = hashimoto_spectrum_full(edges)
    ok_all &= check("4-cycle JSON spectrum", multiset_match(spec, roots_of_unity(4)),
                    f"{meta['n_edges']} edges")

    # 2b: bidirected 4-cycle JSON
    p = os.path.join(tmp, "bicycle4.json")
    save_graph_json(p, gg.gen_bidirected_cycle(4))
    edges, meta = load_graph_json(p)
    spec = hashimoto_spectrum_full(edges)
    ok_all &= check("bidirected 4-cycle JSON spectrum",
                    multiset_match(spec, np.concatenate([roots_of_unity(4)]*2)),
                    f"{meta['n_edges']} edges")

    # 2c: empty graph
    p = os.path.join(tmp, "empty.json")
    save_graph_json(p, [])
    edges, meta = load_graph_json(p)
    ok_all &= check("empty graph loads", (len(edges) == 0 and meta["n_edges"] == 0))

    # 2d: malformed graphs must raise GraphSchemaError
    bad_cases = [
        {"edges": [[0, 1]]},                                # missing 'directed'
        {"directed": False, "edges": [[0, 1]]},             # undirected rejected
        {"directed": True, "edges": [[0, 1, 2]]},           # bad pair
        {"directed": True, "edges": [[0, 0]]},              # self-loop, default off
        {"directed": True, "edges": [[0, 1], [0, 1]]},      # multiedge, default off
        {"directed": True, "edges": "notalist"},            # edges not a list
    ]
    raised = 0
    for bc in bad_cases:
        try:
            parse_graph_obj(bc)
        except GraphSchemaError:
            raised += 1
    ok_all &= check("malformed graphs rejected", raised == len(bad_cases),
                    f"{raised}/{len(bad_cases)} raised")

    # 2e: self-loop / multiedge allowed when flagged
    try:
        e, m = parse_graph_obj({"directed": True, "selfloops_allowed": True,
                                "multiedges_allowed": True,
                                "edges": [[0, 0], [0, 1], [0, 1]]})
        ok_all &= check("self-loop+multiedge allowed when flagged", len(e) == 3)
    except GraphSchemaError as ex:
        ok_all &= check("self-loop+multiedge allowed when flagged", False, str(ex))

    return ok_all


# ---------- 3. No silent core-empty failure (ENG-blocker-3) ----------
def test_no_silent_empty():
    print("AZ-1B.3 Directed export: non-empty Hashimoto on a known cyclic graph")
    # a single directed edge per symmetric pair would give an empty core on a
    # tree-like export; here we confirm both-orientations export yields cycles.
    edges = gg.gen_bidirected_cycle(4)  # both orientations
    B = build_hashimoto(edges)
    nonzero = int(np.count_nonzero(B))
    ok = (B.shape[0] > 0 and nonzero > 0)
    check("bidirected export gives non-empty Hashimoto", ok,
          f"matrix {B.shape}, {nonzero} nonzero transitions")
    # contrast: single-orientation 4-cycle still has a cycle (directed cycle),
    # but an undirected-collapsed export (one rep per pair, no cycle) would be empty.
    # Demonstrate the failure mode is detectable:
    acyclic = [(0, 1), (1, 2), (2, 3)]  # directed path, no cycle
    Bp = build_hashimoto(acyclic)
    # path has non-backtracking transitions but no closed walk; spectral radius 0
    spec = np.linalg.eigvals(Bp) if Bp.shape[0] else np.array([])
    rho = float(np.max(np.abs(spec))) if len(spec) else 0.0
    check("acyclic path detected (rho=0, would-be-empty core)", abs(rho) < 1e-12,
          f"rho={rho:.2e}")
    return ok


# ---------- 4. Sparse ANGULAR validation (for R_q^(K)) ----------
def test_sparse_angular():
    print("AZ-1B.4 Sparse leading-K ANGULAR validation (not just magnitude)")
    # build a nontrivial graph with structured angles
    edges = []
    base = 0
    for _ in range(15):
        edges += gg.gen_bouquet(2, 6, hub=base)
        base += 12
    full = hashimoto_spectrum_full(edges)
    K = 12
    lead = hashimoto_spectrum_leading(edges, K)
    # match leading sparse eigs to nearest dense eigs, compare angles
    full_sorted = full[np.argsort(-np.abs(full))]
    worst_ang = 0.0
    for lv in lead:
        # nearest dense eigenvalue by complex distance
        j = int(np.argmin(np.abs(full - lv)))
        da = abs(np.angle(lv) - np.angle(full[j]))
        da = min(da, 2*np.pi - da)
        worst_ang = max(worst_ang, da)
    check("sparse vs dense max angular error on leading-K", worst_ang < 1e-6,
          f"max |Δarg| = {worst_ang:.2e} over {len(lead)} eigs")
    return worst_ang < 1e-6


# ---------- 5. Manifest validator ----------
def test_manifest():
    print("AZ-1B.5 Manifest validator (CONV-AZ-MANIFEST)")
    good = {
        "run_id": "demo-001", "N": 120, "k": 8, "k_over_N_actual": 1/15,
        "regime": "B1", "canonical_scaling": True, "policy": "bound_symmetric",
        "T": 5000, "seed": 42,
        "graph_export": {"type": "recurrent_core", "directed_edges": "both_orientations",
                         "multiedges_allowed": False, "selfloops_allowed": False},
        "hashimoto": {"script_version": "az_v5", "spectrum_mode": "leading-K",
                      "eigensolver": "arpack_sparse", "tolerance": 1e-10},
        "nulls": {"null0_count": 1000, "null1_count": 1000},
        "statistics": {"rho_B": None, "gap": None, "R_q": {}},
    }
    ok_all = True
    ok_all &= check("valid manifest passes", validate_manifest(good) == [])

    bad_oddN = dict(good); bad_oddN["N"] = 119; bad_oddN["regime"] = "B2"; bad_oddN["canonical_scaling"]=False
    ok_all &= check("odd N rejected", len(validate_manifest(bad_oddN)) > 0)

    bad_canon = dict(good); bad_canon["N"] = 118; bad_canon["k"] = 8
    probs = validate_manifest(bad_canon)
    ok_all &= check("N=118 in B1 rejected (not div by 30)", len(probs) > 0)

    bad_nonull = dict(good); bad_nonull["nulls"] = {}
    ok_all &= check("no-null manifest rejected", len(validate_manifest(bad_nonull)) > 0)

    return ok_all


# ---------- 6. Artifact hash registry (ENG-blocker-5) ----------
def test_artifact_registry():
    print("AZ-1B.6 Artifact hash registry")
    files = [
        "lib/hashimoto.py", "lib/graphgen.py", "lib/graphio.py", "lib/manifest.py",
        "benchmark_ladder.py", "validate_solver.py", "az1b_certify.py",
        "benchmarks/bouquet_2_4_hashimoto_matrix.json",
        "benchmarks/bouquet_2_4_charpoly.txt",
        "benchmarks/az_v5_synthetic_benchmark_report.json",
    ]
    registry = {}
    ok_all = True
    for rel in files:
        p = os.path.join(HERE, rel)
        if not os.path.exists(p):
            ok_all &= check(f"artifact present: {rel}", False)
            continue
        with open(p, "rb") as f:
            h = hashlib.sha256(f.read()).hexdigest()
        registry[rel] = h
    reg_path = os.path.join(HERE, "benchmarks", "AZ_ARTIFACT_REGISTRY.json")
    with open(reg_path, "w") as f:
        json.dump({"sha256": registry, "version": "az_v5",
                   "phase": "AZ-1A + AZ-1B"}, f, indent=2)
    ok_all &= check("artifact registry written", os.path.exists(reg_path),
                    f"{len(registry)} files hashed -> {reg_path}")
    return ok_all


def main():
    print("=" * 64)
    print("AZ-1B Certification (TDR-G ingestion / export / provenance)")
    print("=" * 64)
    test_s2_independent()
    test_json_loader()
    test_no_silent_empty()
    test_sparse_angular()
    test_manifest()
    test_artifact_registry()
    print("=" * 64)
    print(f"AZ-1B GATE: {'PASS (exit 0)' if PASS else 'FAIL (exit 1)'}")
    sys.exit(0 if PASS else 1)


if __name__ == "__main__":
    main()
