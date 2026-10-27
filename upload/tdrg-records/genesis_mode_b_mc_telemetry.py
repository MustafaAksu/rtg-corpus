# genesis_mode_b_mc_telemetry.py
# telemetry-1: provenance/exposure instrumentation successor of pinned v15.3 kernel.
# Parent kernel SHA256: 4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608
# Scientific event law is intentionally unchanged; legacy endpoint/ID conventions are observed, not repaired.
# v15.3 parent: Engine patched with TDR-24F structural leaf incidence and zero-indexed histograms
#
# Key features:
#   - CLI support: --policy, --N, --k, --grid-N, --ratios, --T, --batch, --max-nodes, --seed
#   - optimized graph_edges_for with optional brute-force audit
#   - multistar accounting: seen / resolved / trapped / bound / births
#   - path-tie accounting: seen / bound / failed
#   - bound_symmetric policy: multistars + path double-ties treated as inert bound states
#   - invariant pool rates: rN_T, rN_steps, rN_err
#   - optional motif logging: --motif-log motif.csv --motif-stride 10
#   - occupancy survival diagnostics for clean-star vs multistar filtering
#   - NEW: Exact leaf incidence tracking to close TDR-24F slot-volume identity.
#
# Policies:
#   "trap"             -> multistars ambiguous, path ties ambiguous
#   "bound_multistar"  -> multistars bound, path ties ambiguous
#   "bound_path_tie"   -> alias of bound_symmetric for backward compatibility
#   "bound_symmetric"  -> multistars bound, path ties bound
#   "largest_center"   -> one multistar center fires: largest leaf-count, then lowest ID
#   "all_centers"      -> all valid multistar centers fire simultaneously on frozen snapshot

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import json
import os
import platform
import random
import sys
import uuid
from collections import Counter, deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from math import comb
from pathlib import Path
from typing import Any

PARENT_SIMULATOR_SHA256 = "4c94d8741dc43780394cc563d04be9b2ee5c9767a43a048878fc67640dafa608"
CSV_SCHEMA_VERSION = "mode_b_motif_v15.3_telemetry1"
MANIFEST_SCHEMA_VERSION = "mode_b_manifest_v1"
CONVENTION_ID = "legacy_signed_centered_plus_antipode_low_id_v1"
LARGEST_CENTER_TIE_POLICY = "max_leaf_count_then_lowest_node_id"
ALL_CENTERS_ORDER_POLICY = "sorted_node_id_on_frozen_snapshot"


def sha256_file(path: str | os.PathLike[str]) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def state_hash(N: int, k: int, theta: dict[int, int], delta: dict[int, int]) -> str:
    payload = {
        "N": N,
        "k": k,
        "theta": [[int(i), int(theta[i])] for i in sorted(theta)],
        "delta": [[int(i), int(delta[i])] for i in sorted(delta)],
    }
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class ManifestLogger:
    """Append-only JSONL provenance stream.  Exclusive creation is enforced."""

    def __init__(self, path: str):
        self.path = path
        self._f = open(path, "x", encoding="utf-8", newline="\n")

    def write(self, event: dict[str, Any]) -> None:
        record = dict(event)
        record.setdefault("timestamp_utc", utc_now())
        self._f.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
        self._f.flush()

    def close(self) -> None:
        if not self._f.closed:
            self._f.close()

# ------------------------------------------------------------
# Z_N geometry
# ------------------------------------------------------------

def signed_centered(x: int, N: int) -> int:
    """
    Return representative in (-N/2, N/2].
    Assumes N is even.
    """
    y = x % N
    if y > N // 2:
        y -= N
    return y

def cyclic_distance(a: int, b: int, N: int) -> int:
    x = (a - b) % N
    return min(x, N - x)

def signed_defect_error(theta_i: int, theta_j: int, N: int) -> int:
    """
    Signed distance of Delta_ij = theta_i - theta_j from antipode N/2.
    """
    return signed_centered((theta_i - theta_j) % N - N // 2, N)

def is_defect(theta_i: int, theta_j: int, N: int, k: int) -> bool:
    return abs(signed_defect_error(theta_i, theta_j, N)) <= k

# ------------------------------------------------------------
# Graph construction
# ------------------------------------------------------------

def graph_edges_for(nodes: list[int], theta: dict[int, int], N: int, k: int) -> list[tuple[int, int]]:
    if not nodes:
        return []

    sorted_nodes = sorted(nodes, key=lambda n: theta[n])
    theta_sorted = [theta[n] for n in sorted_nodes]
    edges: list[tuple[int, int]] = []

    for a in nodes:
        ant = (theta[a] + N // 2) % N
        lo = (ant - k) % N
        hi = (ant + k) % N

        if lo <= hi:
            i = bisect.bisect_left(theta_sorted, lo)
            j = bisect.bisect_right(theta_sorted, hi)
            candidates = sorted_nodes[i:j]
        else:
            i1 = bisect.bisect_left(theta_sorted, lo)
            j2 = bisect.bisect_right(theta_sorted, hi)
            candidates = sorted_nodes[i1:] + sorted_nodes[:j2]

        for b in candidates:
            if b > a:
                edges.append((a, b))

    return edges

def graph_edges_bruteforce(nodes: list[int], theta: dict[int, int], N: int, k: int) -> list[tuple[int, int]]:
    edges: list[tuple[int, int]] = []
    for i, a in enumerate(nodes):
        for b in nodes[i + 1:]:
            if is_defect(theta[a], theta[b], N, k):
                edges.append((min(a, b), max(a, b)))
    return sorted(edges)

def audit_graph_edges(n_trials: int = 500, seed: int = 0) -> int:
    rng = random.Random(seed)
    fails = 0

    for _ in range(n_trials):
        N = rng.choice([30, 60, 90, 120, 240])
        k = rng.randint(1, N // 6 - 1)
        m = rng.randint(4, 60)
        theta = {i: rng.randrange(N) for i in range(m)}
        nodes = list(theta.keys())

        fast = sorted(graph_edges_for(nodes, theta, N, k))
        brute = graph_edges_bruteforce(nodes, theta, N, k)

        if fast != brute:
            fails += 1

    return fails

def build_adj(nodes: list[int], edges: list[tuple[int, int]]) -> dict[int, set[int]]:
    adj = {n: set() for n in nodes}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return adj

def connected_components(nodes: list[int], adj: dict[int, set[int]]) -> list[list[int]]:
    seen: set[int] = set()
    comps: list[list[int]] = []

    for n in nodes:
        if n in seen:
            continue

        q = deque([n])
        seen.add(n)
        comp: list[int] = []

        while q:
            x = q.popleft()
            comp.append(x)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)

        comps.append(comp)

    return comps

# ------------------------------------------------------------
# Component structure
# ------------------------------------------------------------

def component_edge_count(comp: list[int], adj: dict[int, set[int]]) -> int:
    s = set(comp)
    return sum(len(adj[v] & s) for v in comp) // 2

def component_degree_sequence(comp: list[int], adj: dict[int, set[int]]) -> tuple[int, ...]:
    s = set(comp)
    return tuple(sorted((len(adj[v] & s) for v in comp), reverse=True))

def is_path_component(comp: list[int], adj: dict[int, set[int]]) -> bool:
    n = len(comp)
    if n < 3:
        return False
    e = component_edge_count(comp, adj)
    deg = component_degree_sequence(comp, adj)
    return e == n - 1 and deg == tuple([2] * (n - 2) + [1, 1])

def is_cycle_component(comp: list[int], adj: dict[int, set[int]]) -> bool:
    n = len(comp)
    if n < 4:
        return False
    e = component_edge_count(comp, adj)
    deg = component_degree_sequence(comp, adj)
    return e == n and deg == tuple([2] * n)

def star_centers(comp: list[int], adj: dict[int, set[int]]) -> list[int]:
    s = set(comp)
    centers: list[int] = []

    for c in comp:
        leaves = list(adj[c] & s)
        if len(leaves) < 3:
            continue

        if all(
            leaves[j] not in adj[leaves[i]]
            for i in range(len(leaves))
            for j in range(i + 1, len(leaves))
        ):
            centers.append(c)

    return centers

def classify_component(comp: list[int], adj: dict[int, set[int]]) -> tuple[str, list[int]]:
    n = len(comp)
    e = component_edge_count(comp, adj)
    deg = component_degree_sequence(comp, adj)

    if e == 0:
        return "isolated", []

    if n == 2 and e == 1:
        return "single_edge", []

    centers = star_centers(comp, adj)
    if len(centers) == 1:
        c = centers[0]
        return f"star_k1c_c{len(adj[c] & set(comp))}", centers

    if len(centers) > 1:
        return f"multistar_centers_{len(centers)}", centers

    if is_path_component(comp, adj):
        return f"path_p{n}", []

    if is_cycle_component(comp, adj):
        return f"cycle_c{n}_bound", []

    if n == 3 and e == 3:
        return "triangle_forbidden_or_wideband", []

    return f"ambiguous_n{n}_e{e}_deg{'-'.join(map(str, deg))}", []

# ------------------------------------------------------------
# Motif diagnostics
# ------------------------------------------------------------

# Dynamically generate potential histogram columns to allow robust extraction.
# Inclusive cap: 0..100. Clean stars should normally occupy >=3, but including
# 0,1,2 prevents DictWriter failures for rare/degenerate multistar structures.
MAX_LEAF_HISTOGRAM = 100
HISTOGRAM_FIELDS = (
    [f"multistar_leaves_{i}" for i in range(0, MAX_LEAF_HISTOGRAM + 1)] +
    [f"clean_star_leaves_{i}" for i in range(0, MAX_LEAF_HISTOGRAM + 1)]
)

MOTIF_FIELDS = [
    "run_id", "policy", "N", "k", "k_over_N", "T_requested", "batch", "step",
    "M_pre", "M_post", "edges", "rho", "births_step",
    "single_edge_components", "path_components", "cycle_components",
    "clean_star_components", "multistar_components", "ambiguous_components",
    "star_centers_total", "multistar_centers_total",
    "multistar_centers_mean", "multistar_centers_max",
    "path_ties_seen_step", "path_ties_bound_step", "path_ties_failed_step",
    "multistar_seen_step", "multistar_bound_step", "multistar_resolved_step",
    "multistar_trapped_step", "multistar_births_step",
    "occ_band_width", "occ_q_band", "occ_windows", "occ_mean", "occ_max",
    "occ_clean_pairs", "occ_multistar_pairs", "occ_both_ge3_pairs", "occ_singleton_pairs",
    "occ_clean_pairs_in_clean_star", "occ_clean_pairs_in_multistar",
    "occ_clean_pairs_embedded", "occ_clean_pairs_other", "occ_clean_pairs_false",
    "occ_clean_survival_rate", "occ_clean_birth_survival_rate",
    "occ_clean_component_compression",
    "clean_star_leaf_incidence_total",
    "multistar_leaf_incidence_total",
    "struct_leaf_incidence_total",
    "clean_star_unique_leaves_total",
    "multistar_unique_leaves_total",
    "struct_unique_leaves_total",
    "struct_component_count",
    "struct_center_count",
    "clean_star_leaves_over_100",
    "multistar_leaves_over_100",
] + HISTOGRAM_FIELDS


def _component_lookup(
    classified: list[tuple[list[int], str, list[int]]] | None,
) -> dict[int, tuple[str, set[int], frozenset[int]]]:
    if classified is None:
        return {}

    out: dict[int, tuple[str, set[int], frozenset[int]]] = {}
    for comp, ctype, centers in classified:
        comp_set = frozenset(comp)
        centers_set = set(centers)
        for node in comp:
            out[node] = (ctype, centers_set, comp_set)
    return out


def occupancy_diagnostics(
    nodes: list[int],
    theta: dict[int, int],
    N: int,
    k: int,
    classified: list[tuple[list[int], str, list[int]]] | None = None,
) -> dict[str, float | int]:

    width = 2 * k + 1
    q_band = width / N
    theta_items = list(theta.items())

    base: dict[str, float | int] = {
        "occ_band_width": width,
        "occ_q_band": q_band,
        "occ_windows": N,
        "occ_mean": 0.0,
        "occ_max": 0,
        "occ_clean_pairs": 0,
        "occ_multistar_pairs": 0,
        "occ_both_ge3_pairs": 0,
        "occ_singleton_pairs": 0,
        "occ_clean_pairs_in_clean_star": 0,
        "occ_clean_pairs_in_multistar": 0,
        "occ_clean_pairs_embedded": 0,
        "occ_clean_pairs_other": 0,
        "occ_clean_pairs_false": 0,
        "occ_clean_survival_rate": 0.0,
        "occ_clean_birth_survival_rate": 0.0,
        "occ_clean_component_compression": 0.0,
    }

    if not theta_items:
        return base

    window_nodes: list[list[int]] = []
    counts: list[int] = []
    for c in range(N):
        members = [node for node, th in theta_items if cyclic_distance(th, c, N) <= k]
        window_nodes.append(members)
        counts.append(len(members))

    clean_pairs, multistar_pairs, both_ge3_pairs, singleton_pairs = 0, 0, 0, 0
    in_clean_star, in_multistar, embedded, other = 0, 0, 0, 0

    comp_lookup = _component_lookup(classified)

    def classify_clean_candidate(singleton_node: int, leaf_nodes: list[int]) -> str:
        candidate_nodes = [singleton_node] + list(leaf_nodes)
        info = comp_lookup.get(singleton_node)
        if info is None:
            return "other"

        ctype, centers_set, comp_set = info
        for node in candidate_nodes:
            node_info = comp_lookup.get(node)
            if node_info is None or node_info[2] != comp_set:
                return "other"

        if ctype.startswith("star_k1c_") and singleton_node in centers_set:
            return "clean_star"
        if ctype.startswith("multistar_centers_"):
            return "multistar"
        if ctype != "isolated":
            return "embedded"
        return "other"

    for c in range(N // 2):
        x_nodes = window_nodes[c]
        y_nodes = window_nodes[(c + N // 2) % N]
        x, y = len(x_nodes), len(y_nodes)

        if (x == 1 and y >= 3) or (y == 1 and x >= 3):
            clean_pairs += 1
            cls = classify_clean_candidate(x_nodes[0] if x == 1 else y_nodes[0], y_nodes if x == 1 else x_nodes)

            if cls == "clean_star": in_clean_star += 1
            elif cls == "multistar": in_multistar += 1
            elif cls == "embedded": embedded += 1
            else: other += 1

        if (x >= 2 and y >= 3) or (y >= 2 and x >= 3): multistar_pairs += 1
        if x >= 3 and y >= 3: both_ge3_pairs += 1
        if x == 1 or y == 1: singleton_pairs += 1

    base.update({
        "occ_mean": sum(counts) / N,
        "occ_max": max(counts),
        "occ_clean_pairs": clean_pairs,
        "occ_multistar_pairs": multistar_pairs,
        "occ_both_ge3_pairs": both_ge3_pairs,
        "occ_singleton_pairs": singleton_pairs,
        "occ_clean_pairs_in_clean_star": in_clean_star,
        "occ_clean_pairs_in_multistar": in_multistar,
        "occ_clean_pairs_embedded": embedded,
        "occ_clean_pairs_other": other,
        "occ_clean_pairs_false": other,
        "occ_clean_survival_rate": (in_clean_star / clean_pairs) if clean_pairs else 0.0,
        "occ_clean_birth_survival_rate": 0.0,
        "occ_clean_component_compression": 0.0,
    })
    return base


def step_motif_snapshot(
    classified: list[tuple[list[int], str, list[int]]],
    adj: dict[int, set[int]],
) -> dict[str, int | float]:
    counts = Counter(ctype for _, ctype, _ in classified)

    single_edge_components = counts.get("single_edge", 0)
    path_components = sum(v for k, v in counts.items() if k.startswith("path_p"))
    cycle_components = sum(v for k, v in counts.items() if k.startswith("cycle_c") and k.endswith("_bound"))
    clean_star_components = sum(v for k, v in counts.items() if k.startswith("star_k1c_"))
    multistar_components = sum(v for k, v in counts.items() if k.startswith("multistar_centers_"))
    ambiguous_components = sum(
        v for k, v in counts.items()
        if k.startswith("ambiguous_") or k == "triangle_forbidden_or_wideband"
    )

    star_centers_total = 0
    multistar_centers_total = 0
    multistar_center_counts: list[int] = []

    # TDR-24F Histogram Arrays
    multistar_leaf_counts = {}
    clean_star_leaf_counts = {}
    multistar_leaves_over_100 = 0
    clean_star_leaves_over_100 = 0

    # TDR-24F structural closure telemetry.
    #
    # Important distinction:
    #   unique leaves    = non-center nodes in the component
    #   leaf incidence   = sum over centers of within-component degree
    #
    # The slot-volume closure needs node-normalized leaf incidence:
    #
    #   cbar_struct_node = Σ leaf_incidence / Σ M_pre
    #   psi_slot ≈ cbar_struct_node / (2k+1)
    #
    clean_star_leaf_incidence_total = 0
    multistar_leaf_incidence_total = 0
    clean_star_unique_leaves_total = 0
    multistar_unique_leaves_total = 0

    for comp, ctype, centers in classified:
        comp_set = set(comp)

        if ctype.startswith("star_k1c_"):
            star_centers_total += len(centers)

            c = centers[0] if centers else None
            n_leaves = len(adj[c] & comp_set) if c is not None else max(0, len(comp) - 1)

            clean_star_leaf_incidence_total += n_leaves
            clean_star_unique_leaves_total += n_leaves

            if 0 <= n_leaves <= MAX_LEAF_HISTOGRAM:
                clean_star_leaf_counts[n_leaves] = clean_star_leaf_counts.get(n_leaves, 0) + 1
            elif n_leaves > MAX_LEAF_HISTOGRAM:
                clean_star_leaves_over_100 += 1

        elif ctype.startswith("multistar_centers_"):
            multistar_centers_total += len(centers)
            multistar_center_counts.append(len(centers))

            center_set = set(centers)

            # Unique non-center nodes.
            n_unique_leaves = len(comp_set - center_set)

            # Leaf incidence: each center contributes its within-component degree.
            # This is the quantity needed for TDR-24F slot closure.
            leaf_incidence = sum(len(adj[c] & comp_set) for c in centers)

            multistar_unique_leaves_total += n_unique_leaves
            multistar_leaf_incidence_total += leaf_incidence

            # Keep the historical multistar_leaves_X histogram as unique-leaf count.
            # Use the explicit *_leaf_incidence_total fields for TDR-24F closure.
            if 0 <= n_unique_leaves <= MAX_LEAF_HISTOGRAM:
                multistar_leaf_counts[n_unique_leaves] = multistar_leaf_counts.get(n_unique_leaves, 0) + 1
            elif n_unique_leaves > MAX_LEAF_HISTOGRAM:
                multistar_leaves_over_100 += 1

    if sum(clean_star_leaf_counts.values()) + clean_star_leaves_over_100 != clean_star_components:
        raise AssertionError("clean-star histogram/component mismatch")
    if sum(multistar_leaf_counts.values()) + multistar_leaves_over_100 != multistar_components:
        raise AssertionError("multistar histogram/component mismatch")

    out = {
        "single_edge_components": single_edge_components,
        "path_components": path_components,
        "cycle_components": cycle_components,
        "clean_star_components": clean_star_components,
        "multistar_components": multistar_components,
        "ambiguous_components": ambiguous_components,
        "star_centers_total": star_centers_total,
        "multistar_centers_total": multistar_centers_total,
        "multistar_centers_mean": (
            sum(multistar_center_counts) / len(multistar_center_counts)
            if multistar_center_counts else 0.0
        ),
        "multistar_centers_max": max(multistar_center_counts) if multistar_center_counts else 0,
        "clean_star_leaf_incidence_total": clean_star_leaf_incidence_total,
        "multistar_leaf_incidence_total": multistar_leaf_incidence_total,
        "struct_leaf_incidence_total": (
            clean_star_leaf_incidence_total + multistar_leaf_incidence_total
        ),
        "clean_star_unique_leaves_total": clean_star_unique_leaves_total,
        "multistar_unique_leaves_total": multistar_unique_leaves_total,
        "struct_unique_leaves_total": (
            clean_star_unique_leaves_total + multistar_unique_leaves_total
        ),
        "struct_component_count": clean_star_components + multistar_components,
        "struct_center_count": star_centers_total + multistar_centers_total,
        "clean_star_leaves_over_100": clean_star_leaves_over_100,
        "multistar_leaves_over_100": multistar_leaves_over_100,
    }

    # Flatten histograms into row dictionary
    for n_leaves, count in multistar_leaf_counts.items():
        out[f'multistar_leaves_{n_leaves}'] = count

    for n_leaves, count in clean_star_leaf_counts.items():
        out[f'clean_star_leaves_{n_leaves}'] = count

    return out


# ------------------------------------------------------------
# Universe state
# ------------------------------------------------------------

@dataclass
class Universe:
    N: int
    k: int
    theta: dict[int, int]
    delta: dict[int, int]

    steps: int = 0
    births: int = 0
    star_births: int = 0
    ambiguous_events: int = 0

    multistar_seen: int = 0
    multistar_bound: int = 0
    multistar_resolved: int = 0
    multistar_births: int = 0
    multistar_trapped: int = 0

    orientation_ties: int = 0       
    path_ties_seen: int = 0         
    path_ties_bound: int = 0
    path_ties_failed: int = 0

    single_edge_swaps: int = 0
    path_interactions: int = 0
    bound_cycle_hits: int = 0

    defect_edge_sum: int = 0
    defect_density_sum: float = 0.0
    max_nodes: int = 4
    max_edges: int = 0
    max_births_in_step: int = 0
    hit_node_cap: bool = False

    # Telemetry-only fields. These do not participate in the event map.
    initial_state_hash: str = ""
    requested_T: int = 0
    stop_reason: str = "not_started"
    antipodal_endpoint_events: int = 0
    first_antipodal_endpoint_step: int | None = None
    first_antipodal_state_hash: str = ""
    first_antipodal_path_length: int = 0
    first_antipodal_endpoint_ids: tuple[int, int] | None = None
    largest_center_equal_degree_ties: int = 0
    first_largest_center_tie_step: int | None = None

    comp_type_counts: Counter = field(default_factory=Counter)
    ambiguous_type_counts: Counter = field(default_factory=Counter)

    birth_steps_list: list[int] = field(default_factory=list)
    node_history: list[int] = field(default_factory=list)
    edge_history: list[int] = field(default_factory=list)
    density_history: list[float] = field(default_factory=list)
    birth_history: list[int] = field(default_factory=list)


def init_universe(
    N: int,
    k: int,
    rng: random.Random,
    m0: int = 4,
    exclude_zero_delta: bool = False,
) -> Universe:
    if N % 2 != 0:
        raise ValueError("N must be even.")
    if not (k < N / 6):
        raise ValueError(f"Narrow-band violated: k={k}, N/6={N / 6}")

    theta = {i: rng.randrange(N) for i in range(m0)}
    delta = {
        i: rng.randrange(1, N) if exclude_zero_delta else rng.randrange(N)
        for i in range(m0)
    }

    return Universe(N=N, k=k, theta=theta, delta=delta)


# ------------------------------------------------------------
# Interaction laws
# ------------------------------------------------------------

def raw_ordered_path(comp: list[int], adj: dict[int, set[int]]) -> list[int] | None:
    s = set(comp)
    endpoints = sorted(v for v in comp if len(adj[v] & s) == 1)

    if len(endpoints) != 2:
        return None

    path = [endpoints[0]]
    prev = None
    cur = endpoints[0]

    while True:
        nxts = sorted(x for x in (adj[cur] & s) if x != prev)
        if not nxts:
            break

        nxt = nxts[0]
        path.append(nxt)
        prev, cur = cur, nxt

        if len(path) > len(comp):
            return None

    return path if len(path) == len(comp) else None


def orient_path(
    path: list[int],
    theta: dict[int, int],
    delta: dict[int, int],
    N: int,
    u: Universe,
) -> list[int] | None:
    if len(path) == 2:
        return path

    score = sum(
        signed_defect_error(theta[path[i]], theta[path[i + 1]], N)
        for i in range(len(path) - 1)
    )

    if score > 0:
        return path

    if score < 0:
        return list(reversed(path))

    u.orientation_ties += 1

    endpoint_residue = (delta[path[-1]] - delta[path[0]]) % N
    if endpoint_residue == N // 2:
        u.antipodal_endpoint_events += 1
        if u.first_antipodal_endpoint_step is None:
            u.first_antipodal_endpoint_step = u.steps + 1
            u.first_antipodal_state_hash = state_hash(u.N, u.k, u.theta, u.delta)
            u.first_antipodal_path_length = len(path)
            u.first_antipodal_endpoint_ids = (path[0], path[-1])

    endpoint_d = signed_centered(delta[path[-1]] - delta[path[0]], N)

    if endpoint_d > 0:
        return path

    if endpoint_d < 0:
        return list(reversed(path))

    u.path_ties_seen += 1
    return None


def apply_single_edge_swap(comp: list[int], delta: dict[int, int], u: Universe) -> bool:
    if len(comp) != 2:
        return False

    a, b = comp
    delta[a], delta[b] = delta[b], delta[a]
    u.single_edge_swaps += 1
    return True


def apply_path_cycle(
    comp: list[int],
    adj: dict[int, set[int]],
    u: Universe,
    bind_ties: bool = False,
) -> bool:
    path0 = raw_ordered_path(comp, adj)

    if path0 is None:
        return False

    path = orient_path(path0, u.theta, u.delta, u.N, u)

    if path is None:
        if bind_ties:
            u.path_ties_bound += 1
            return True
        u.path_ties_failed += 1
        return False

    old = {v: u.delta[v] for v in path}

    for i, v in enumerate(path):
        u.delta[v] = old[path[(i + 1) % len(path)]]

    u.path_interactions += 1
    return True


def blow_up_star_with_snapshot(
    u: Universe,
    center: int,
    theta_pre: dict[int, int],
    delta_pre: dict[int, int],
    next_id: int,
) -> int:
    old_d = delta_pre[center]

    u.theta[next_id] = (theta_pre[center] + u.N // 2) % u.N
    u.delta[next_id] = old_d
    u.delta[center] = (-old_d) % u.N

    u.births += 1
    u.star_births += 1
    u.birth_steps_list.append(u.steps)

    return next_id + 1


def choose_largest_center(comp: list[int], adj: dict[int, set[int]], centers: list[int]) -> int:
    s = set(comp)
    return sorted(centers, key=lambda c: (-len(adj[c] & s), c))[0]


# ------------------------------------------------------------
# Step
# ------------------------------------------------------------

def step_universe(
    u: Universe,
    multistar_policy: str = "trap",
    collect_motif: bool = False,
) -> dict[str, Any] | None:
    allowed = {
        "trap", "bound_multistar", "bound_path_tie",
        "bound_symmetric", "largest_center", "all_centers",
    }

    if multistar_policy not in allowed:
        raise ValueError(f"Unknown policy={multistar_policy}")

    N, k = u.N, u.k

    for x in list(u.theta.keys()):
        u.theta[x] = (u.theta[x] + u.delta[x]) % N

    nodes_pre = list(u.theta.keys())
    theta_pre = dict(u.theta)
    delta_pre = dict(u.delta)

    edges = graph_edges_for(nodes_pre, theta_pre, N, k)
    adj = build_adj(nodes_pre, edges)
    comps = connected_components(nodes_pre, adj)
    classified = [(comp, *classify_component(comp, adj)) for comp in comps]

    m_pre = len(nodes_pre)
    edge_density = len(edges) / comb(m_pre, 2) if m_pre >= 2 else 0.0

    motif: dict[str, Any] | None = None
    pre_births = u.births
    pre_path_seen = u.path_ties_seen
    pre_path_bound = u.path_ties_bound
    pre_path_failed = u.path_ties_failed
    pre_ms_seen = u.multistar_seen
    pre_ms_bound = u.multistar_bound
    pre_ms_resolved = u.multistar_resolved
    pre_ms_trapped = u.multistar_trapped
    pre_ms_births = u.multistar_births

    if collect_motif:
        motif = {
            "step": u.steps + 1,
            "M_pre": m_pre,
            "edges": len(edges),
            "rho": edge_density,
        }
        motif.update(step_motif_snapshot(classified, adj))
        motif.update(occupancy_diagnostics(nodes_pre, theta_pre, N, k, classified=classified))

    step_births = 0
    next_id = max(u.theta.keys()) + 1 if u.theta else 0

    bind_multistars = multistar_policy in {
        "bound_multistar", "bound_path_tie", "bound_symmetric",
    }
    bind_path_ties = multistar_policy in {
        "bound_path_tie", "bound_symmetric",
    }

    for comp, ctype, centers in classified:
        u.comp_type_counts[ctype] += 1

        if ctype == "isolated":
            continue

        if ctype.startswith("star_k1c_") and len(centers) == 1:
            before = u.births
            next_id = blow_up_star_with_snapshot(u, centers[0], theta_pre, delta_pre, next_id)
            step_births += u.births - before
            continue

        if ctype.startswith("multistar_centers_"):
            u.multistar_seen += 1

            if multistar_policy == "trap":
                u.multistar_trapped += 1
                u.ambiguous_events += 1
                u.ambiguous_type_counts["ms_trap_" + ctype] += 1

            elif bind_multistars:
                u.multistar_bound += 1

            elif multistar_policy == "largest_center":
                comp_set = set(comp)
                center_degrees = {c0: len(adj[c0] & comp_set) for c0 in centers}
                max_center_degree = max(center_degrees.values())
                if sum(1 for d0 in center_degrees.values() if d0 == max_center_degree) > 1:
                    u.largest_center_equal_degree_ties += 1
                    if u.first_largest_center_tie_step is None:
                        u.first_largest_center_tie_step = u.steps + 1
                c = choose_largest_center(comp, adj, centers)
                before = u.births
                next_id = blow_up_star_with_snapshot(u, c, theta_pre, delta_pre, next_id)
                step_births += u.births - before
                u.multistar_resolved += 1
                u.multistar_births += (u.births - before)

            elif multistar_policy == "all_centers":
                before = u.births
                for c in sorted(centers):
                    next_id = blow_up_star_with_snapshot(u, c, theta_pre, delta_pre, next_id)
                step_births += u.births - before
                u.multistar_resolved += 1
                u.multistar_births += (u.births - before)

            continue

        if ctype == "single_edge":
            if not apply_single_edge_swap(comp, u.delta, u):
                u.ambiguous_events += 1
                u.ambiguous_type_counts[ctype] += 1
            continue

        if ctype.startswith("path_p"):
            if not apply_path_cycle(comp, adj, u, bind_ties=bind_path_ties):
                u.ambiguous_events += 1
                u.ambiguous_type_counts[ctype] += 1
            continue

        if ctype.startswith("cycle_c") and ctype.endswith("_bound"):
            u.bound_cycle_hits += 1
            continue

        u.ambiguous_events += 1
        u.ambiguous_type_counts[ctype] += 1

    m_post = len(u.theta)

    u.steps += 1
    u.defect_edge_sum += len(edges)
    u.defect_density_sum += edge_density
    u.max_edges = max(u.max_edges, len(edges))
    u.max_nodes = max(u.max_nodes, m_post)
    u.max_births_in_step = max(u.max_births_in_step, step_births)

    u.node_history.append(m_post)
    u.edge_history.append(len(edges))
    u.density_history.append(edge_density)
    u.birth_history.append(step_births)

    if motif is not None:
        occ_clean_pairs = int(motif.get("occ_clean_pairs", 0) or 0)
        occ_in_clean_star = int(motif.get("occ_clean_pairs_in_clean_star", 0) or 0)
        clean_star_components = int(motif.get("clean_star_components", 0) or 0)

        motif.update({
            "M_post": m_post,
            "births_step": step_births,
            "path_ties_seen_step": u.path_ties_seen - pre_path_seen,
            "path_ties_bound_step": u.path_ties_bound - pre_path_bound,
            "path_ties_failed_step": u.path_ties_failed - pre_path_failed,
            "multistar_seen_step": u.multistar_seen - pre_ms_seen,
            "multistar_bound_step": u.multistar_bound - pre_ms_bound,
            "multistar_resolved_step": u.multistar_resolved - pre_ms_resolved,
            "multistar_trapped_step": u.multistar_trapped - pre_ms_trapped,
            "multistar_births_step": u.multistar_births - pre_ms_births,
            "occ_clean_birth_survival_rate": (step_births / occ_clean_pairs) if occ_clean_pairs else 0.0,
            "occ_clean_component_compression": (occ_in_clean_star / clean_star_components) if clean_star_components else 0.0,
        })

    return motif

# ------------------------------------------------------------
# Simulation
# ------------------------------------------------------------

def run_one(
    N: int = 120,
    k: int = 10,
    T: int = 500,
    seed: int | None = None,
    exclude_zero_delta: bool = False,
    multistar_policy: str = "trap",
    max_nodes: int = 600,
    motif_writer: csv.DictWriter | None = None,
    motif_stride: int = 1,
    run_id: str | int = 0,
    batch: int = 1,
    manifest_logger: ManifestLogger | None = None,
    run_meta: dict[str, Any] | None = None,
) -> Universe:
    rng = random.Random(seed)
    u = init_universe(N=N, k=k, rng=rng, exclude_zero_delta=exclude_zero_delta)
    u.initial_state_hash = state_hash(N, k, u.theta, u.delta)
    u.requested_T = T
    u.stop_reason = "running"

    if manifest_logger is not None and run_meta is not None:
        manifest_logger.write({
            "event": "run_start",
            **run_meta,
            "initial_state_hash": u.initial_state_hash,
        })

    for _ in range(T):
        if max_nodes > 0 and len(u.theta) >= max_nodes:
            u.hit_node_cap = True
            u.stop_reason = "node_cap_before_step"
            break

        next_step = u.steps + 1
        collect_motif = motif_writer is not None and motif_stride > 0 and (next_step % motif_stride == 0)
        motif = step_universe(u, multistar_policy=multistar_policy, collect_motif=collect_motif)

        if motif_writer is not None and motif is not None:
            # Ensure every field in MOTIF_FIELDS is present, initializing dynamic histograms to 0
            row = {field: 0 for field in MOTIF_FIELDS}
            row.update(motif)
            row.update({
                "run_id": run_id,
                "policy": multistar_policy,
                "N": N,
                "k": k,
                "k_over_N": k / N,
                "T_requested": T,
                "batch": batch,
            })
            motif_writer.writerow(row)

        if max_nodes > 0 and len(u.theta) >= max_nodes:
            u.hit_node_cap = True
            u.stop_reason = "horizon_and_node_cap" if u.steps >= T else "node_cap_after_step"
            break
    else:
        u.stop_reason = "horizon"

    if u.steps >= T and u.stop_reason == "running":
        u.stop_reason = "horizon"

    return u

# ------------------------------------------------------------
# Statistics
# ------------------------------------------------------------

def quantile(xs: list, q: float):
    ys = sorted(xs)
    if not ys:
        raise ValueError("empty list")
    return ys[int(q * (len(ys) - 1))]

def late_rate(node_history: list[int]) -> float:
    actual_T = len(node_history)
    if actual_T < 2:
        return 0.0
    mid = actual_T // 2
    steps = actual_T - mid
    return (node_history[-1] - node_history[mid - 1]) / steps

def summarize_universe(u: Universe) -> dict:
    final_nodes = len(u.theta)
    st = max(u.steps, 1)
    birth_step_count = sum(1 for x in u.birth_history if x > 0)

    return {
        "final_nodes": final_nodes,
        "births": u.births,
        "star_births": u.star_births,
        "steps_taken": u.steps,
        "r_N_late": late_rate(u.node_history),
        "birth_step_count": birth_step_count,
        "birth_step_fraction": birth_step_count / st,
        "path_interaction_rate": u.path_interactions / st,
        "single_edge_rate": u.single_edge_swaps / st,
        "bound_cycle_rate": u.bound_cycle_hits / st,
        "ambiguous_events": u.ambiguous_events,
        "had_ambiguous": int(u.ambiguous_events > 0),
        "orientation_ties": u.orientation_ties,
        "path_ties_seen": u.path_ties_seen,
        "path_ties_bound": u.path_ties_bound,
        "path_ties_failed": u.path_ties_failed,
        "multistar_seen": u.multistar_seen,
        "multistar_resolved": u.multistar_resolved,
        "multistar_trapped": u.multistar_trapped,
        "multistar_bound": u.multistar_bound,
        "multistar_births": u.multistar_births,
        "mean_defect_edges": u.defect_edge_sum / st,
        "mean_defect_density": u.defect_density_sum / st,
        "max_nodes": u.max_nodes,
        "max_edges": u.max_edges,
        "max_births_in_step": u.max_births_in_step,
        "hit_node_cap": int(u.hit_node_cap),
        "stop_reason": u.stop_reason,
        "completed": int(u.steps >= u.requested_T),
        "antipodal_endpoint_events": u.antipodal_endpoint_events,
        "first_antipodal_endpoint_step": u.first_antipodal_endpoint_step,
        "first_antipodal_state_hash": u.first_antipodal_state_hash,
        "first_antipodal_path_length": u.first_antipodal_path_length,
        "first_antipodal_endpoint_ids": u.first_antipodal_endpoint_ids,
        "largest_center_equal_degree_ties": u.largest_center_equal_degree_ties,
        "first_largest_center_tie_step": u.first_largest_center_tie_step,
        "initial_state_hash": u.initial_state_hash,
        "frozen": int(final_nodes <= 5),
        "strongly_inflating": int(final_nodes > 12),
        "gt100": int(final_nodes > 100),
        "gt200": int(final_nodes > 200),
        "gt500": int(final_nodes > 500),
        "component_counts": u.comp_type_counts,
        "ambiguous_counts": u.ambiguous_type_counts,
    }

def monte_carlo(
    N: int = 120,
    k: int = 10,
    T: int = 500,
    batch: int = 200,
    seed: int = 1,
    exclude_zero_delta: bool = False,
    multistar_policy: str = "trap",
    max_nodes: int = 600,
    motif_writer: csv.DictWriter | None = None,
    motif_stride: int = 1,
    master_seed: int | None = None,
    requested_ratio: float | None = None,
    manifest_logger: ManifestLogger | None = None,
    job_uuid: str | None = None,
    simulator_sha256: str | None = None,
) -> dict:
    cell_seed = seed
    rng = random.Random(cell_seed)
    run_seeds = [rng.randrange(10**12) for _ in range(batch)]

    if manifest_logger is not None:
        manifest_logger.write({
            "event": "cell_plan",
            "manifest_schema_version": MANIFEST_SCHEMA_VERSION,
            "job_uuid": job_uuid,
            "simulator_sha256": simulator_sha256,
            "parent_simulator_sha256": PARENT_SIMULATOR_SHA256,
            "convention_id": CONVENTION_ID,
            "policy": multistar_policy,
            "N": N,
            "k": k,
            "requested_ratio": requested_ratio,
            "realized_k_over_N": k / N,
            "band_width_over_N": (2 * k + 1) / N,
            "T_requested": T,
            "batch": batch,
            "master_seed": master_seed,
            "derived_cell_seed": cell_seed,
            "planned_runs": [
                {
                    "replicate_index": i,
                    "run_id": f"N{N}_k{k}_{multistar_policy}_r{i}",
                    "run_seed": rs,
                }
                for i, rs in enumerate(run_seeds)
            ],
        })

    finals, births, star_births = [], [], []
    rNs_late, rNs_late_birth, rNs_late_strong = [], [], []
    birth_step_counts, steps_l = [], []
    path_rates, edge_rates, cycle_rates = [], [], []
    ambigs, had_ambigs = [], []
    ties, path_seen, path_bound, path_failed = [], [], [], []
    ms_seen_l, ms_resolved_l, ms_trapped_l, ms_bound_l, ms_births_l = [], [], [], [], []
    mean_edges, mean_densities = [], []
    max_nodes_l, max_edges_l, max_births_step_l = [], [], []
    frozens, strong_inflatings, cap_hits = [], [], []
    gt100_l, gt200_l, gt500_l = [], [], []
    antipodal_events_l, largest_center_ties_l = [], []

    comp_counts = Counter()
    ambiguous_counts = Counter()

    for i, run_seed in enumerate(run_seeds):
        run_id = f"N{N}_k{k}_{multistar_policy}_r{i}"
        run_meta = {
            "manifest_schema_version": MANIFEST_SCHEMA_VERSION,
            "job_uuid": job_uuid,
            "simulator_sha256": simulator_sha256,
            "parent_simulator_sha256": PARENT_SIMULATOR_SHA256,
            "Python_version": platform.python_version(),
            "convention_id": CONVENTION_ID,
            "policy": multistar_policy,
            "path_tie_policy": "bind_E0" if multistar_policy in {"bound_path_tie", "bound_symmetric"} else "ambiguous_E0",
            "largest_center_tie_policy": LARGEST_CENTER_TIE_POLICY if multistar_policy == "largest_center" else "not_active",
            "all_centers_order_policy": ALL_CENTERS_ORDER_POLICY if multistar_policy == "all_centers" else "not_active",
            "N": N,
            "k": k,
            "requested_ratio": requested_ratio,
            "realized_k_over_N": k / N,
            "band_width_over_N": (2 * k + 1) / N,
            "T_requested": T,
            "motif_stride": motif_stride,
            "max_nodes": max_nodes,
            "exclude_zero_delta": exclude_zero_delta,
            "m0": 4,
            "master_seed": master_seed,
            "derived_cell_seed": cell_seed,
            "replicate_index": i,
            "run_id": run_id,
            "run_seed": run_seed,
            "batch": batch,
            "CSV_schema_version": CSV_SCHEMA_VERSION,
        }
        try:
            u = run_one(
                N=N, k=k, T=T, seed=run_seed,
                exclude_zero_delta=exclude_zero_delta,
                multistar_policy=multistar_policy,
                max_nodes=max_nodes, motif_writer=motif_writer,
                motif_stride=motif_stride, run_id=run_id, batch=batch,
                manifest_logger=manifest_logger, run_meta=run_meta,
            )
        except BaseException as exc:
            if manifest_logger is not None:
                manifest_logger.write({
                    "event": "run_error",
                    **run_meta,
                    "error_type": type(exc).__name__,
                    "error_message": str(exc),
                })
            raise

        s = summarize_universe(u)

        if manifest_logger is not None:
            manifest_logger.write({
                "event": "run_end",
                **run_meta,
                "initial_state_hash": u.initial_state_hash,
                "steps_taken": u.steps,
                "final_M": len(u.theta),
                "max_M": u.max_nodes,
                "hit_node_cap": bool(u.hit_node_cap),
                "stop_reason": u.stop_reason,
                "antipodal_endpoint_events": u.antipodal_endpoint_events,
                "first_antipodal_endpoint_step": u.first_antipodal_endpoint_step,
                "first_antipodal_state_hash": u.first_antipodal_state_hash or None,
                "first_antipodal_path_length": u.first_antipodal_path_length or None,
                "first_antipodal_endpoint_ids": list(u.first_antipodal_endpoint_ids) if u.first_antipodal_endpoint_ids is not None else None,
                "largest_center_equal_degree_ties": u.largest_center_equal_degree_ties,
                "first_largest_center_tie_step": u.first_largest_center_tie_step,
                "completed": bool(u.steps >= T),
                "source_CSV_hash": None,
            })

        finals.append(s["final_nodes"])
        births.append(s["births"])
        star_births.append(s["star_births"])
        rNs_late.append(s["r_N_late"])
        steps_l.append(s["steps_taken"])

        if s["births"] > 0: rNs_late_birth.append(s["r_N_late"])
        if s["strongly_inflating"]: rNs_late_strong.append(s["r_N_late"])
        birth_step_counts.append(s["birth_step_count"])

        path_rates.append(s["path_interaction_rate"])
        edge_rates.append(s["single_edge_rate"])
        cycle_rates.append(s["bound_cycle_rate"])

        ambigs.append(s["ambiguous_events"])
        had_ambigs.append(s["had_ambiguous"])

        ties.append(s["orientation_ties"])
        path_seen.append(s["path_ties_seen"])
        path_bound.append(s["path_ties_bound"])
        path_failed.append(s["path_ties_failed"])

        ms_seen_l.append(s["multistar_seen"])
        ms_resolved_l.append(s["multistar_resolved"])
        ms_trapped_l.append(s["multistar_trapped"])
        ms_bound_l.append(s["multistar_bound"])
        ms_births_l.append(s["multistar_births"])

        mean_edges.append(s["mean_defect_edges"])
        mean_densities.append(s["mean_defect_density"])

        max_nodes_l.append(s["max_nodes"])
        max_edges_l.append(s["max_edges"])
        max_births_step_l.append(s["max_births_in_step"])

        frozens.append(s["frozen"])
        strong_inflatings.append(s["strongly_inflating"])
        cap_hits.append(s["hit_node_cap"])

        gt100_l.append(s["gt100"])
        gt200_l.append(s["gt200"])
        gt500_l.append(s["gt500"])
        antipodal_events_l.append(s["antipodal_endpoint_events"])
        largest_center_ties_l.append(s["largest_center_equal_degree_ties"])

        comp_counts.update(s["component_counts"])
        ambiguous_counts.update(s["ambiguous_counts"])

    def mean_or_zero(xs: list) -> float: return sum(xs) / len(xs) if xs else 0.0

    total_births = sum(births)
    total_steps = sum(steps_l)
    total_birth_steps = sum(birth_step_counts)

    rN_T = total_births / (batch * T)
    rN_steps = total_births / max(total_steps, 1)
    birth_step_fraction_T = total_birth_steps / (batch * T)
    conditional_births_per_birth_step = total_births / total_birth_steps if total_birth_steps > 0 else 0.0
    rN_consistency_err = abs(rN_T - birth_step_fraction_T * conditional_births_per_birth_step)

    mean_steps = mean_or_zero(steps_l)
    mean_ambig = mean_or_zero(ambigs)
    ambig_rate = mean_ambig / mean_steps if mean_steps > 0 else 0.0
    active_counts = Counter({key: val for key, val in comp_counts.items() if key != "isolated"})

    return {
        "N": N, "k": k, "k_over_N": k / N, "T": T, "batch": batch,
        "master_seed": master_seed, "derived_cell_seed": cell_seed,
        "multistar_policy": multistar_policy, "max_nodes_cap": max_nodes,
        "birth_fraction": sum(x > 0 for x in births) / batch,
        "mean_final_nodes": mean_or_zero(finals),
        "q50_final": quantile(finals, 0.50), "q90_final": quantile(finals, 0.90),
        "q99_final": quantile(finals, 0.99), "max_final_nodes": max(finals),
        "mean_births": mean_or_zero(births), "mean_star_births": mean_or_zero(star_births),
        "rN_T": rN_T, "rN_steps": rN_steps, "rN_late_T": mean_or_zero(rNs_late),
        "rN_late_birth": mean_or_zero(rNs_late_birth), "rN_late_strong": mean_or_zero(rNs_late_strong),
        "rN_consistency_err": rN_consistency_err, "mean_birth_step_fraction": birth_step_fraction_T,
        "conditional_births_per_birth_step": conditional_births_per_birth_step, "mean_steps_taken": mean_steps,
        "mean_path_interaction_rate": mean_or_zero(path_rates), "mean_single_edge_rate": mean_or_zero(edge_rates),
        "mean_bound_cycle_rate": mean_or_zero(cycle_rates), "p_frozen": mean_or_zero(frozens),
        "p_strongly_inflating": mean_or_zero(strong_inflatings), "p_cap": mean_or_zero(cap_hits),
        "p_gt100": mean_or_zero(gt100_l), "p_gt200": mean_or_zero(gt200_l), "p_gt500": mean_or_zero(gt500_l),
        "mean_ambiguous_events": mean_ambig, "ambig_rate": ambig_rate, "p_ambig": mean_or_zero(had_ambigs),
        "mean_orientation_ties": mean_or_zero(ties), "mean_path_ties_seen": mean_or_zero(path_seen),
        "mean_path_ties_bound": mean_or_zero(path_bound), "mean_path_ties_failed": mean_or_zero(path_failed),
        "mean_multistar_seen": mean_or_zero(ms_seen_l), "mean_multistar_resolved": mean_or_zero(ms_resolved_l),
        "mean_multistar_trapped": mean_or_zero(ms_trapped_l), "mean_multistar_bound": mean_or_zero(ms_bound_l),
        "mean_multistar_births": mean_or_zero(ms_births_l),
        "mean_antipodal_endpoint_events": mean_or_zero(antipodal_events_l),
        "p_antipodal_endpoint_exposure": mean_or_zero([int(x > 0) for x in antipodal_events_l]),
        "mean_largest_center_equal_degree_ties": mean_or_zero(largest_center_ties_l),
        "p_largest_center_equal_degree_tie_exposure": mean_or_zero([int(x > 0) for x in largest_center_ties_l]),
        "multistar_births_per_event": (sum(ms_births_l) / max(sum(ms_resolved_l), 1)),
        "mean_defect_edges": mean_or_zero(mean_edges), "mean_defect_density": mean_or_zero(mean_densities),
        "max_nodes_seen": max(max_nodes_l), "max_edges_seen": max(max_edges_l), "max_births_in_step_seen": max(max_births_step_l),
        "top_component_types": comp_counts.most_common(10), "top_active_component_types": active_counts.most_common(10),
        "top_ambiguous_types": ambiguous_counts.most_common(10),
    }

# ------------------------------------------------------------
# Output
# ------------------------------------------------------------

def format_result(out: dict) -> str:
    top = ", ".join(f"{k}:{v}" for k, v in out["top_active_component_types"][:5])
    amb = ", ".join(f"{k}:{v}" for k, v in out["top_ambiguous_types"][:3])

    if out["p_ambig"] <= 0.05: tag = "[NUM]"
    elif out["ambig_rate"] < 0.005: tag = "[HEUR-weak]"
    else: tag = "[HEUR]"

    return (
        f"policy={out['multistar_policy']}, k={out['k']:3d}, k/N={out['k_over_N']:.4f} | "
        f"bf={out['birth_fraction']:.3f}, mf={out['mean_final_nodes']:.1f}, "
        f"q50={out['q50_final']}, q90={out['q90_final']}, q99={out['q99_final']}, "
        f"rN_T={out['rN_T']:.4f}, rN_s={out['rN_steps']:.4f}, rN_late={out['rN_late_T']:.4f}, "
        f"rN_err={out['rN_consistency_err']:.5f}, birth_steps={out['mean_birth_step_fraction']:.3f}, "
        f"b/step={out['conditional_births_per_birth_step']:.3f}, swap_rate={out['mean_single_edge_rate']:.4f}, "
        f"path_rate={out['mean_path_interaction_rate']:.4f}, cyc_rate={out['mean_bound_cycle_rate']:.4f}, "
        f"p_frz={out['p_frozen']:.3f}, p_strong={out['p_strongly_inflating']:.3f}, p_cap={out['p_cap']:.3f}, "
        f"steps={out['mean_steps_taken']:.0f}, p_ambig={out['p_ambig']:.3f}, ambig={out['mean_ambiguous_events']:.2f}, "
        f"ms_seen={out['mean_multistar_seen']:.1f}, ms_res={out['mean_multistar_resolved']:.1f}, "
        f"p_gt100={out['p_gt100']:.3f}, p_gt200={out['p_gt200']:.3f}, p_gt500={out['p_gt500']:.3f}, "
        f"rho={out['mean_defect_density']:.5f}, top=[{top}], amb=[{amb}] {tag}"
    )

def run_grid(
    grid_N: list[int],
    ratios: list[float],
    T: int = 500,
    batch: int = 200,
    seed: int = 42,
    exclude_zero_delta: bool = False,
    multistar_policy: str = "trap",
    max_nodes: int = 600,
    motif_writer: csv.DictWriter | None = None,
    motif_stride: int = 1,
    manifest_logger: ManifestLogger | None = None,
    job_uuid: str | None = None,
    simulator_sha256: str | None = None,
) -> None:
    for N in grid_N:
        if N <= 0 or N % 2 != 0:
            raise ValueError(f"N must be positive and even; got N={N}")

        k_to_ratio: dict[int, float] = {}
        for r in ratios:
            if not (r > 0):
                raise ValueError(f"ratio must be positive; got {r}")
            k = int(round(N * r))
            if not (0 <= k < N / 6):
                raise ValueError(f"Requested ratio {r} realizes k={k}, violating 0 <= k < N/6 for N={N}")
            if k in k_to_ratio and abs(k_to_ratio[k] - r) > 1e-15:
                raise ValueError(
                    f"Distinct requested ratios {k_to_ratio[k]} and {r} both realize k={k} at N={N}; "
                    "design would silently deduplicate."
                )
            k_to_ratio[k] = r

        print(f"\n=== N={N}, T={T}, batch={batch}, policy={multistar_policy}, max_nodes={max_nodes} ===", flush=True)

        for k in sorted(k_to_ratio):
            requested_ratio = k_to_ratio[k]
            cell_seed = seed + 1_000_003 * N + 9_176 * k
            out = monte_carlo(
                N=N, k=k, T=T, batch=batch, seed=cell_seed,
                exclude_zero_delta=exclude_zero_delta, multistar_policy=multistar_policy,
                max_nodes=max_nodes, motif_writer=motif_writer, motif_stride=motif_stride,
                master_seed=seed, requested_ratio=requested_ratio,
                manifest_logger=manifest_logger, job_uuid=job_uuid,
                simulator_sha256=simulator_sha256,
            )
            print(format_result(out), flush=True)

# ------------------------------------------------------------
# CLI
# ------------------------------------------------------------

def parse_ratio(x: str) -> float:
    x = x.strip()
    if "/" in x:
        a, b = x.split("/", 1)
        return float(a) / float(b)
    return float(x)

def parse_args():
    parser = argparse.ArgumentParser(description="Mode-B Monte Carlo for G_perm / TDR-G (telemetry-only legacy-convention successor).")
    parser.add_argument("--policy", nargs="+", default=["bound_symmetric"], choices=["trap", "bound_multistar", "bound_path_tie", "bound_symmetric", "largest_center", "all_centers"])
    parser.add_argument("--N", type=int, default=None)
    parser.add_argument("--k", type=int, default=None)
    parser.add_argument("--grid-N", nargs="+", type=int, default=[60, 120])
    parser.add_argument("--ratios", nargs="+", type=parse_ratio, default=[1 / 20, 1 / 15, 1 / 12])
    parser.add_argument("--T", type=int, default=1000)
    parser.add_argument("--batch", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42, help="Master seed. Cell seed remains master + 1_000_003*N + 9_176*k.")
    parser.add_argument("--max-nodes", "--cap", dest="max_nodes", type=int, default=1000)
    parser.add_argument("--exclude-zero-delta", action="store_true")
    parser.add_argument("--audit-trials", type=int, default=500)
    parser.add_argument("--motif-log", type=str, default=None)
    parser.add_argument("--motif-stride", type=int, default=1)
    parser.add_argument("--manifest-log", type=str, default=None, help="JSONL run manifest. Defaults to <motif-log>.manifest.jsonl when motif logging is enabled.")
    return parser.parse_args()


def validate_args(args: argparse.Namespace) -> None:
    if args.T <= 0:
        raise ValueError("--T must be positive")
    if args.batch <= 0:
        raise ValueError("--batch must be positive")
    if args.motif_stride <= 0:
        raise ValueError("--motif-stride must be positive")
    if args.max_nodes < 0:
        raise ValueError("--max-nodes must be >= 0 (0 means no cap)")
    if args.audit_trials < 0:
        raise ValueError("--audit-trials must be >= 0")

    Ns = [args.N] if args.N is not None else list(args.grid_N)
    for N in Ns:
        if N is None or N <= 0 or N % 2 != 0:
            raise ValueError(f"N must be positive and even; got {N}")

    if args.k is not None:
        if args.N is None:
            raise ValueError("Single-cell mode with --k requires --N.")
        if not (0 <= args.k < args.N / 6):
            raise ValueError(f"Narrow-band violated: require 0 <= k < N/6; got k={args.k}, N={args.N}")
    else:
        for r in args.ratios:
            if not (r > 0):
                raise ValueError(f"Ratios must be positive; got {r}")


def main():
    args = parse_args()
    validate_args(args)

    if args.audit_trials > 0:
        audit_fails = audit_graph_edges(n_trials=args.audit_trials)
        if audit_fails > 0:
            raise RuntimeError(f"graph_edges_for audit failed {audit_fails}/{args.audit_trials} trials")
        print(f"graph_edges_for audit: PASS ({args.audit_trials} trials)", flush=True)

    simulator_path = Path(__file__).resolve()
    simulator_sha256 = sha256_file(simulator_path)
    job_uuid = str(uuid.uuid4())

    motif_path = Path(args.motif_log).resolve() if args.motif_log else None
    if args.manifest_log:
        manifest_path = Path(args.manifest_log).resolve()
    elif motif_path is not None:
        manifest_path = Path(str(motif_path) + ".manifest.jsonl")
    else:
        manifest_path = None

    # Fail before creating anything if an output already exists.
    for p in [motif_path, manifest_path]:
        if p is not None and p.exists():
            raise FileExistsError(f"Refusing to overwrite existing output: {p}")

    motif_file = None
    motif_writer = None
    manifest_logger = None
    job_status = "completed"
    job_error: str | None = None

    try:
        if manifest_path is not None:
            manifest_logger = ManifestLogger(str(manifest_path))
            manifest_logger.write({
                "event": "job_start",
                "manifest_schema_version": MANIFEST_SCHEMA_VERSION,
                "job_uuid": job_uuid,
                "simulator_sha256": simulator_sha256,
                "parent_simulator_sha256": PARENT_SIMULATOR_SHA256,
                "Python_version": platform.python_version(),
                "python_implementation": platform.python_implementation(),
                "convention_id": CONVENTION_ID,
                "command": sys.argv,
                "cwd": os.getcwd(),
                "motif_log": str(motif_path) if motif_path is not None else None,
                "CSV_schema_version": CSV_SCHEMA_VERSION,
                "master_seed": args.seed,
            })

        if motif_path is not None:
            motif_file = open(motif_path, "x", newline="", encoding="utf-8")
            motif_writer = csv.DictWriter(motif_file, fieldnames=MOTIF_FIELDS)
            motif_writer.writeheader()

        if args.N is not None and args.k is not None:
            for policy in args.policy:
                print(f"\n=== N={args.N}, k={args.k}, T={args.T}, batch={args.batch}, policy={policy}, max_nodes={args.max_nodes} ===", flush=True)
                cell_seed = args.seed + 1_000_003 * args.N + 9_176 * args.k
                out = monte_carlo(
                    N=args.N, k=args.k, T=args.T, batch=args.batch, seed=cell_seed,
                    exclude_zero_delta=args.exclude_zero_delta, multistar_policy=policy,
                    max_nodes=args.max_nodes, motif_writer=motif_writer, motif_stride=args.motif_stride,
                    master_seed=args.seed, requested_ratio=None,
                    manifest_logger=manifest_logger, job_uuid=job_uuid,
                    simulator_sha256=simulator_sha256,
                )
                print(format_result(out), flush=True)

        elif args.N is not None and args.k is None:
            for policy in args.policy:
                run_grid(
                    grid_N=[args.N], ratios=args.ratios, T=args.T, batch=args.batch, seed=args.seed,
                    exclude_zero_delta=args.exclude_zero_delta, multistar_policy=policy,
                    max_nodes=args.max_nodes, motif_writer=motif_writer, motif_stride=args.motif_stride,
                    manifest_logger=manifest_logger, job_uuid=job_uuid,
                    simulator_sha256=simulator_sha256,
                )
        elif args.N is None and args.k is not None:
            raise ValueError("Single-cell mode with --k requires --N.")
        else:
            for policy in args.policy:
                run_grid(
                    grid_N=args.grid_N, ratios=args.ratios, T=args.T, batch=args.batch, seed=args.seed,
                    exclude_zero_delta=args.exclude_zero_delta, multistar_policy=policy,
                    max_nodes=args.max_nodes, motif_writer=motif_writer, motif_stride=args.motif_stride,
                    manifest_logger=manifest_logger, job_uuid=job_uuid,
                    simulator_sha256=simulator_sha256,
                )

    except BaseException as exc:
        job_status = "error"
        job_error = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        if motif_file is not None:
            motif_file.flush()
            motif_file.close()

        csv_hash = None
        if motif_path is not None and motif_path.exists():
            csv_hash = sha256_file(motif_path)

        if manifest_logger is not None:
            manifest_logger.write({
                "event": "job_end",
                "manifest_schema_version": MANIFEST_SCHEMA_VERSION,
                "job_uuid": job_uuid,
                "simulator_sha256": simulator_sha256,
                "parent_simulator_sha256": PARENT_SIMULATOR_SHA256,
                "convention_id": CONVENTION_ID,
                "status": job_status,
                "error": job_error,
                "source_CSV": str(motif_path) if motif_path is not None else None,
                "source_CSV_hash": csv_hash,
            })
            manifest_logger.close()


if __name__ == "__main__":
    main()
