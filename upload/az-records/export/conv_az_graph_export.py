#!/usr/bin/env python3
"""
conv_az_graph_export.py  —  TDR-G defect-graph export under CONV-AZ-GRAPH-EXPORT.

[RID: TDRG-AZ-EXPORT-BASELINE]  Status: [ENG/NUM diagnostic]

Resolves the AZ-OPEN-EDGE architectural decision and implements the four frozen
graph objects required by the Arithmetic/Zeta study (RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN):

  G_T            : the defect graph at the final tick T (directed, both orientations).
  Core(G_T)      : the recurrent core (2-core of the underlying simple graph, then
                   re-directed) — the substructure on which the Hashimoto operator is
                   non-degenerate (extract_recurrent_core operates correctly only here).
  G_birth(w)     : the defect graph at the tick of the w-th birth (birth-anchored
                   snapshot; w is 1-indexed). Returns None if fewer than w births occurred.
  G_cumulative   : union of all directed defect edges that were ever present, across all
                   ticks (the persistent-contact graph).

EDGE CONVENTION (resolves AZ-OPEN-EDGE):
  DIRECTED, BOTH ORIENTATIONS. Each symmetric defect pair {a,b} exports as the two
  independent directed edges (a,b) and (b,a). Rationale (from AZ-OPEN-EDGE consequences):
  one-directed-edge-per-pair makes extract_recurrent_core silently return empty and the
  Hashimoto operator ill-defined; both-orientations gives a well-defined 2|E| x 2|E|
  Hashimoto operator. This is the canonical format; the Hashimoto size consequence is
  documented and must be respected by all downstream spectral code.

This module does NOT compute cross-branch claims. All outputs are branch-local TDR-G
diagnostics tagged [ENG/NUM diagnostic]; nothing here is promoted, and SG-PROG-1/4 and
SG-AZ-3 forbid using any of it as continuous-branch evidence.
"""

from __future__ import annotations

import json
import hashlib
import datetime
from pathlib import Path
from collections import defaultdict, Counter
from typing import Any


SCHEMA = "tdrg_az_graph_export_v1"
CONVENTION = "CONV-AZ-GRAPH-EXPORT"
EDGE_CONVENTION = "directed_both_orientations"   # resolves AZ-OPEN-EDGE


# ---------------------------------------------------------------------------
# Graph primitives (directed, both-orientations convention)
# ---------------------------------------------------------------------------

def undirected_to_directed(undirected_pairs: list[tuple[int, int]]) -> list[list[int]]:
    """Each {a,b} -> [a,b] and [b,a]. Deduplicated, sorted, stable."""
    seen = set()
    out = []
    for a, b in undirected_pairs:
        a, b = int(a), int(b)
        for e in ((a, b), (b, a)):
            if e not in seen:
                seen.add(e)
                out.append([e[0], e[1]])
    out.sort()
    return out


def two_core_nodes(undirected_pairs: list[tuple[int, int]]) -> set[int]:
    """Iteratively strip degree<=1 vertices; the residue is the 2-core, which carries
    every cycle and is exactly where the Hashimoto operator is non-degenerate."""
    adj = defaultdict(set)
    for a, b in undirected_pairs:
        if a != b:
            adj[a].add(b); adj[b].add(a)
    changed = True
    while changed:
        changed = False
        for v in [v for v in adj if len(adj[v]) <= 1]:
            for w in list(adj[v]):
                adj[w].discard(v)
            del adj[v]
            changed = True
    return set(adj)


def recurrent_core_directed(undirected_pairs: list[tuple[int, int]]) -> list[list[int]]:
    """Directed both-orientations edge list restricted to the 2-core."""
    core = two_core_nodes(undirected_pairs)
    kept = [(a, b) for a, b in undirected_pairs if a in core and b in core]
    return undirected_to_directed(kept)


# ---------------------------------------------------------------------------
# Graph-object payloads
# ---------------------------------------------------------------------------

def _graph_object(name: str, nodes: list[int], undirected_pairs: list[tuple[int, int]],
                  meta: dict[str, Any]) -> dict[str, Any]:
    directed = undirected_to_directed(undirected_pairs)
    return {
        "object": name,
        "edge_convention": EDGE_CONVENTION,
        "n_nodes": len(nodes),
        "nodes": sorted(int(n) for n in nodes),
        "n_undirected_edges": len(undirected_pairs),
        "n_directed_edges": len(directed),
        "directed_edges": directed,
        **meta,
    }


def build_export(tick_edge_history: list[list[tuple[int, int]]],
                 birth_ticks: list[int],
                 node_history: list[list[int]],
                 *,
                 N: int, k: int, policy: str, run_id: str,
                 T: int, seed: int | None) -> dict[str, Any]:
    """Assemble the four CONV-AZ-GRAPH-EXPORT objects from per-tick history.

    tick_edge_history[t] : undirected defect pairs present at tick t (0-indexed by tick).
    birth_ticks          : ticks (indices into tick_edge_history) at which a birth occurred.
    node_history[t]      : node ids present at tick t.
    """
    if not tick_edge_history:
        raise ValueError("empty tick history")

    # G_T : final tick
    gt_pairs = tick_edge_history[-1]
    gt_nodes = node_history[-1]
    G_T = _graph_object("G_T", gt_nodes, gt_pairs, {"tick": len(tick_edge_history) - 1})

    # Core(G_T)
    core_directed = recurrent_core_directed(gt_pairs)
    core_nodes = sorted({n for e in core_directed for n in e})
    Core_GT = {
        "object": "Core(G_T)",
        "edge_convention": EDGE_CONVENTION,
        "core_definition": "2-core of underlying simple graph, re-directed both orientations",
        "n_nodes": len(core_nodes),
        "nodes": core_nodes,
        "n_directed_edges": len(core_directed),
        "directed_edges": core_directed,
        "nonempty": len(core_directed) > 0,
    }

    # G_birth(w) : snapshot at each birth tick (store all; consumers pick w)
    birth_objs = {}
    for w, bt in enumerate(birth_ticks, start=1):
        if 0 <= bt < len(tick_edge_history):
            birth_objs[str(w)] = _graph_object(
                f"G_birth({w})", node_history[bt], tick_edge_history[bt],
                {"birth_index": w, "tick": bt})

    # G_cumulative : union of all directed edges ever present
    cum = set()
    all_nodes = set()
    for t, pairs in enumerate(tick_edge_history):
        all_nodes.update(node_history[t])
        for a, b in pairs:
            cum.add((int(a), int(b))); cum.add((int(b), int(a)))
    G_cumulative = {
        "object": "G_cumulative",
        "edge_convention": EDGE_CONVENTION,
        "n_nodes": len(all_nodes),
        "nodes": sorted(all_nodes),
        "n_directed_edges": len(cum),
        "directed_edges": sorted([list(e) for e in cum]),
        "n_ticks": len(tick_edge_history),
    }

    return {
        "schema": SCHEMA,
        "convention": CONVENTION,
        "edge_convention": EDGE_CONVENTION,
        "run_id": run_id, "N": N, "k": k, "policy": policy,
        "T": T, "seed": seed,
        "n_births": len(birth_ticks),
        "objects": {
            "G_T": G_T,
            "Core(G_T)": Core_GT,
            "G_birth": birth_objs,
            "G_cumulative": G_cumulative,
        },
    }


# ---------------------------------------------------------------------------
# Manifest
# ---------------------------------------------------------------------------

def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def write_export(export: dict[str, Any], out_dir: str | Path) -> dict[str, Any]:
    """Write each graph object as its own JSON file + a manifest with checksums."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    artifact_paths = {}

    def dump(name: str, obj: Any) -> None:
        fn = out / f"{export['run_id']}__{name.replace('(', '_').replace(')', '')}.json"
        fn.write_text(json.dumps(obj, indent=2, sort_keys=True), encoding="utf-8")
        artifact_paths[name] = fn.name

    dump("G_T", export["objects"]["G_T"])
    dump("Core_G_T", export["objects"]["Core(G_T)"])
    dump("G_cumulative", export["objects"]["G_cumulative"])
    for w, obj in export["objects"]["G_birth"].items():
        dump(f"G_birth_{w}", obj)

    manifest = {
        "schema": SCHEMA,
        "convention": CONVENTION,
        "edge_convention": EDGE_CONVENTION,
        "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "run_id": export["run_id"],
        "N": export["N"], "k": export["k"], "policy": export["policy"],
        "T": export["T"], "seed": export["seed"], "n_births": export["n_births"],
        "artifact_paths": artifact_paths,
        "checksums": {name: _sha256(out / fn) for name, fn in artifact_paths.items()},
    }
    (out / f"{export['run_id']}__manifest.json").write_text(
        json.dumps(manifest, indent=2, sort_keys=True), encoding="utf-8")
    return manifest


if __name__ == "__main__":
    # self-test on a tiny hand-built history
    hist = [[(0, 1)], [(0, 1), (1, 2), (2, 0)], [(0, 1), (1, 2), (2, 0)]]
    nodes = [[0, 1], [0, 1, 2], [0, 1, 2]]
    exp = build_export(hist, birth_ticks=[1], node_history=nodes,
                        N=24, k=1, policy="bound_symmetric", run_id="selftest", T=3, seed=0)
    print("G_T directed edges:", exp["objects"]["G_T"]["n_directed_edges"])
    print("Core nonempty:", exp["objects"]["Core(G_T)"]["nonempty"],
          "core directed edges:", exp["objects"]["Core(G_T)"]["n_directed_edges"])
    print("G_birth keys:", list(exp["objects"]["G_birth"].keys()))
    print("G_cumulative directed edges:", exp["objects"]["G_cumulative"]["n_directed_edges"])
