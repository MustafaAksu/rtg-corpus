#!/usr/bin/env python3
"""Tie incidence of `largest_center` on the pinned engine (SESSION probe for the TDR-19 decision note).

    python3 -I evidence/tdrg/decision_notes/largest_center_tie_probe.py ENGINE N k T SEEDS [MAX_NODES]

Loads the engine file ENGINE (upload/tdrg-records/genesis_mode_b_mc_v18.py), wraps its
choose_largest_center without changing what it returns, and runs run_one(multistar_policy="largest_center")
for seeds 0..SEEDS-1. For every multistar event it records whether two or more valid centres share the
maximal in-component degree, i.e. whether the node-ID tie-break decided the firing centre.
Prints one JSON object. It changes no engine behaviour: the wrapper returns the original choice.
"""
import importlib.util, json, sys

eng, N, k, T, S = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
cap = int(sys.argv[6]) if len(sys.argv) > 6 else 600
spec = importlib.util.spec_from_file_location("engine", eng)
m = importlib.util.module_from_spec(spec); sys.modules["engine"] = m; spec.loader.exec_module(m)
orig = m.choose_largest_center
stat = {"events": 0, "ties": 0, "tie_sizes": {}}

def wrapped(comp, adj, centers):
    s = set(comp)
    degs = [len(adj[c] & s) for c in centers]
    top = max(degs); n = degs.count(top)
    stat["events"] += 1
    if n >= 2:
        stat["ties"] += 1
        stat["tie_sizes"][n] = stat["tie_sizes"].get(n, 0) + 1
    return orig(comp, adj, centers)

m.choose_largest_center = wrapped
runs = []
for seed in range(S):
    e0, t0 = stat["events"], stat["ties"]
    u = m.run_one(N=N, k=k, T=T, seed=seed, multistar_policy="largest_center", max_nodes=cap)
    runs.append({"seed": seed, "events": stat["events"] - e0, "ties": stat["ties"] - t0, "births": u.births})
print(json.dumps({"N": N, "k": k, "T": T, "seeds": S, "max_nodes": cap, "events": stat["events"], "ties": stat["ties"],
                  "tie_fraction": round(stat["ties"] / stat["events"], 4) if stat["events"] else None,
                  "tie_sizes": stat["tie_sizes"], "runs": runs}))
