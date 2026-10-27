# genesis_mode_b_mc.py
# v7.3 strict: multistar-safe, locality-respecting Mode-B Monte Carlo for G_perm / TDR-G

from __future__ import annotations

import random
from collections import Counter, deque
from dataclasses import dataclass, field
from itertools import combinations
from math import comb


# ------------------------------------------------------------
# Z_N geometry
# ------------------------------------------------------------

def signed_centered(x: int, N: int) -> int:
    """
    Return representative in (-N/2, N/2].
    Assumes N is even for antipodal geometry.
    """
    y = x % N
    if y > N // 2:
        y -= N
    return y


def signed_defect_error(theta_i: int, theta_j: int, N: int) -> int:
    """
    Signed distance of Delta_ij from the antipode N/2.
    Used for path orientation; antisymmetric on defect pairs.
    """
    delta = (theta_i - theta_j) % N
    return signed_centered(delta - N // 2, N)


def is_defect(theta_i: int, theta_j: int, N: int, k: int) -> bool:
    return abs(signed_defect_error(theta_i, theta_j, N)) <= k


# ------------------------------------------------------------
# Graph construction
# ------------------------------------------------------------

def graph_edges_for(nodes: list[int], theta: dict[int, int], N: int, k: int) -> list[tuple[int, int]]:
    return [
        (a, b)
        for a, b in combinations(nodes, 2)
        if is_defect(theta[a], theta[b], N, k)
    ]


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
    """
    Return ALL valid K_{1,c} star centers to preserve symmetry.
    A valid center has >=3 leaves in the component,
    and the leaves are mutually non-defective (independent set).
    """
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


def classify_component(comp: list[int], adj: dict[int, set[int]]) -> tuple[str, int | None]:
    """
    Returns (component_type, unique_star_center_if_any)
    """
    n = len(comp)
    e = component_edge_count(comp, adj)
    deg = component_degree_sequence(comp, adj)

    if e == 0:
        return "isolated", None

    if n == 2 and e == 1:
        return "single_edge", None

    centers = star_centers(comp, adj)
    if len(centers) == 1:
        c = centers[0]
        return f"star_k1c_c{len(adj[c] & set(comp))}", c
    if len(centers) > 1:
        return f"ambiguous_multistar_centers_{len(centers)}", None

    if is_path_component(comp, adj):
        return f"path_p{n}", None

    if is_cycle_component(comp, adj):
        return f"cycle_c{n}_bound", None

    if n == 3 and e == 3:
        return "triangle_forbidden_or_wideband", None

    return f"ambiguous_n{n}_e{e}_deg{'-'.join(map(str, deg))}", None


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
    multistar_ambiguities: int = 0

    orientation_ties: int = 0
    unresolved_path_ties: int = 0

    single_edge_swaps: int = 0
    path_interactions: int = 0
    bound_cycle_hits: int = 0

    defect_edge_sum: int = 0
    defect_density_sum: float = 0.0

    max_nodes: int = 4
    max_edges: int = 0
    max_births_in_step: int = 0

    comp_type_counts: Counter = field(default_factory=Counter)
    ambiguous_type_counts: Counter = field(default_factory=Counter)

    birth_steps: list[int] = field(default_factory=list)
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
    """
    Deterministic path reconstruction from endpoints.
    Physical orientation is handled later; this only recovers adjacency order.
    """
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


def orient_path(path: list[int], theta: dict[int, int], delta: dict[int, int], N: int, u: Universe) -> list[int] | None:
    """
    Orientation rule:
    1. signed topological gradient (sum of signed defect errors)
    2. endpoint relative advance
    3. if still tied -> unresolved (no label fallback)
    """
    # For a 2-node path, orientation is irrelevant: swap is the same either way.
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

    endpoint_d = signed_centered(delta[path[-1]] - delta[path[0]], N)
    if endpoint_d > 0:
        return path
    if endpoint_d < 0:
        return list(reversed(path))

    u.unresolved_path_ties += 1
    return None


def apply_single_edge_swap(comp: list[int], delta: dict[int, int], u: Universe) -> bool:
    if len(comp) != 2:
        return False
    a, b = comp
    delta[a], delta[b] = delta[b], delta[a]
    u.single_edge_swaps += 1
    return True


def apply_path_cycle(comp: list[int], adj: dict[int, set[int]], u: Universe) -> bool:
    path0 = raw_ordered_path(comp, adj)
    if path0 is None:
        return False

    path = orient_path(path0, u.theta, u.delta, u.N, u)
    if path is None:
        return False

    old = {v: u.delta[v] for v in path}
    for i, v in enumerate(path):
        u.delta[v] = old[path[(i + 1) % len(path)]]

    u.path_interactions += 1
    return True


def blow_up_star(u: Universe, center: int) -> None:
    """
    Star inversion blow-up:
    theta_E = theta_A + N/2
    delta_E = delta_A
    delta_A -> -delta_A
    """
    new_id = max(u.theta.keys()) + 1
    old_d = u.delta[center]

    u.theta[new_id] = (u.theta[center] + u.N // 2) % u.N
    u.delta[new_id] = old_d
    u.delta[center] = (-old_d) % u.N

    u.births += 1
    u.star_births += 1
    u.birth_steps.append(u.steps)


def step_universe(u: Universe) -> None:
    N, k = u.N, u.k

    # 1. Kinematics
    for x in list(u.theta.keys()):
        u.theta[x] = (u.theta[x] + u.delta[x]) % N

    # 2. Defect graph on pre-interaction snapshot
    nodes_pre = list(u.theta.keys())
    edges = graph_edges_for(nodes_pre, u.theta, N, k)
    adj = build_adj(nodes_pre, edges)
    comps = connected_components(nodes_pre, adj)

    classified = [(comp, *classify_component(comp, adj)) for comp in comps]
    # each item = (comp, ctype, center_or_None)

    step_births = 0

    # 3. Strict locality: all disjoint components resolved in parallel on snapshot.
    for comp, ctype, center in classified:
        u.comp_type_counts[ctype] += 1

        if ctype == "isolated":
            continue

        if ctype.startswith("star"):
            if center is not None:
                before = u.births
                blow_up_star(u, center)
                step_births += u.births - before
            else:
                u.ambiguous_events += 1
                u.multistar_ambiguities += 1
                u.ambiguous_type_counts[ctype] += 1
            continue

        if ctype.startswith("ambiguous_multistar_"):
            u.ambiguous_events += 1
            u.multistar_ambiguities += 1
            u.ambiguous_type_counts[ctype] += 1
            continue

        if ctype == "single_edge":
            if not apply_single_edge_swap(comp, u.delta, u):
                u.ambiguous_events += 1
                u.ambiguous_type_counts[ctype] += 1
            continue

        if ctype.startswith("path_p"):
            if not apply_path_cycle(comp, adj, u):
                u.ambiguous_events += 1
                u.ambiguous_type_counts[ctype] += 1
            continue

        if ctype.startswith("cycle_c") and ctype.endswith("_bound"):
            u.bound_cycle_hits += 1
            continue

        # triangle/wideband or genuinely dense unresolved component
        u.ambiguous_events += 1
        u.ambiguous_type_counts[ctype] += 1

    # 4. Observables
    m_pre = len(nodes_pre)
    edge_density = len(edges) / comb(m_pre, 2) if m_pre >= 2 else 0.0
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


# ------------------------------------------------------------
# Simulation
# ------------------------------------------------------------

def run_one(N=120, k=10, T=500, seed=None, exclude_zero_delta=False) -> Universe:
    rng = random.Random(seed)
    u = init_universe(N=N, k=k, rng=rng, exclude_zero_delta=exclude_zero_delta)

    for _ in range(T):
        step_universe(u)

    return u


# ------------------------------------------------------------
# Statistics
# ------------------------------------------------------------

def quantile(xs, q):
    ys = sorted(xs)
    if not ys:
        raise ValueError("empty list")
    idx = int(q * (len(ys) - 1))
    return ys[idx]


def late_rate(node_history, T):
    """
    node_history[t-1] = post-step state after step t
    Second-half window = steps mid+1..T, length T-mid
    starts from post-step mid = node_history[mid-1]
    """
    if T < 2 or len(node_history) < T:
        return 0.0

    mid = T // 2
    steps = T - mid
    return (node_history[-1] - node_history[mid - 1]) / steps


def summarize_universe(u: Universe, T: int):
    final_nodes = len(u.theta)
    birth_step_count = sum(1 for x in u.birth_history if x > 0)
    mean_births_per_birth_step = (u.births / birth_step_count) if birth_step_count > 0 else 0.0

    return {
        "final_nodes": final_nodes,
        "births": u.births,
        "star_births": u.star_births,

        "r_N": (final_nodes - 4) / T,
        "r_N_late": late_rate(u.node_history, T),

        "birth_step_count": birth_step_count,
        "birth_step_fraction": birth_step_count / T if T > 0 else 0.0,
        "mean_births_per_birth_step": mean_births_per_birth_step,

        "path_interaction_rate": u.path_interactions / T,
        "single_edge_rate": u.single_edge_swaps / T,
        "bound_cycle_rate": u.bound_cycle_hits / T,

        "ambiguous_events": u.ambiguous_events,
        "had_ambiguous": int(u.ambiguous_events > 0),

        "orientation_ties": u.orientation_ties,
        "unresolved_path_ties": u.unresolved_path_ties,
        "multistar_ambiguities": u.multistar_ambiguities,

        "mean_defect_edges": u.defect_edge_sum / T,
        "mean_defect_density": u.defect_density_sum / T,

        "max_nodes": u.max_nodes,
        "max_edges": u.max_edges,
        "max_births_in_step": u.max_births_in_step,

        "frozen": int(final_nodes <= 5),
        "strongly_inflating": int(final_nodes > 12),

        "component_counts": u.comp_type_counts,
        "ambiguous_counts": u.ambiguous_type_counts,
    }


def monte_carlo(N=120, k=10, T=500, batch=500, seed=1, exclude_zero_delta=False):
    rng = random.Random(seed)

    finals, births, star_births = [], [], []
    rNs, rNs_late = [], []
    rNs_late_birth, rNs_late_strong = [], []

    birth_step_counts, births_per_birth_step = [], []
    path_rates, edge_rates, cycle_rates = [], [], []

    ambigs, had_ambigs = [], []
    ties, unresolved_path_ties, multistar_ambigs = [], [], []
    mean_edges, mean_densities = [], []
    max_nodes_l, max_edges_l, max_births_step_l = [], [], []
    frozens, strong_inflatings = [], []

    comp_counts = Counter()
    ambiguous_counts = Counter()

    for _ in range(batch):
        u = run_one(
            N=N,
            k=k,
            T=T,
            seed=rng.randrange(10**12),
            exclude_zero_delta=exclude_zero_delta,
        )
        s = summarize_universe(u, T)

        finals.append(s["final_nodes"])
        births.append(s["births"])
        star_births.append(s["star_births"])

        rNs.append(s["r_N"])
        rNs_late.append(s["r_N_late"])

        if s["births"] > 0:
            rNs_late_birth.append(s["r_N_late"])
        if s["strongly_inflating"]:
            rNs_late_strong.append(s["r_N_late"])

        birth_step_counts.append(s["birth_step_count"])
        births_per_birth_step.append(s["mean_births_per_birth_step"])

        path_rates.append(s["path_interaction_rate"])
        edge_rates.append(s["single_edge_rate"])
        cycle_rates.append(s["bound_cycle_rate"])

        ambigs.append(s["ambiguous_events"])
        had_ambigs.append(s["had_ambiguous"])

        ties.append(s["orientation_ties"])
        unresolved_path_ties.append(s["unresolved_path_ties"])
        multistar_ambigs.append(s["multistar_ambiguities"])

        mean_edges.append(s["mean_defect_edges"])
        mean_densities.append(s["mean_defect_density"])

        max_nodes_l.append(s["max_nodes"])
        max_edges_l.append(s["max_edges"])
        max_births_step_l.append(s["max_births_in_step"])

        frozens.append(s["frozen"])
        strong_inflatings.append(s["strongly_inflating"])

        comp_counts.update(s["component_counts"])
        ambiguous_counts.update(s["ambiguous_counts"])

    def mean_or_zero(xs):
        return sum(xs) / len(xs) if xs else 0.0

    total_birth_steps = sum(birth_step_counts)
    cond_births_per_birth_step = (sum(births) / total_birth_steps) if total_birth_steps > 0 else 0.0

    active_counts = Counter({k: v for k, v in comp_counts.items() if k != "isolated"})

    return {
        "N": N,
        "k": k,
        "k_over_N": k / N,
        "T": T,
        "batch": batch,

        "birth_fraction": sum(x > 0 for x in births) / batch,
        "mean_final_nodes": mean_or_zero(finals),
        "q50_final": quantile(finals, 0.50),
        "q90_final": quantile(finals, 0.90),
        "q99_final": quantile(finals, 0.99),
        "max_final_nodes": max(finals),

        "mean_births": mean_or_zero(births),
        "mean_star_births": mean_or_zero(star_births),

        "mean_r_N": mean_or_zero(rNs),
        "mean_r_N_late": mean_or_zero(rNs_late),
        "mean_r_N_late_birth": mean_or_zero(rNs_late_birth),
        "mean_r_N_late_strong": mean_or_zero(rNs_late_strong),

        "mean_birth_step_fraction": mean_or_zero([b / T for b in birth_step_counts]),
        "conditional_births_per_birth_step": cond_births_per_birth_step,

        "mean_path_interaction_rate": mean_or_zero(path_rates),
        "mean_single_edge_rate": mean_or_zero(edge_rates),
        "mean_bound_cycle_rate": mean_or_zero(cycle_rates),

        "p_frozen": mean_or_zero(frozens),
        "p_strongly_inflating": mean_or_zero(strong_inflatings),

        "mean_ambiguous_events": mean_or_zero(ambigs),
        "p_ambig": mean_or_zero(had_ambigs),

        "mean_orientation_ties": mean_or_zero(ties),
        "mean_unresolved_path_ties": mean_or_zero(unresolved_path_ties),
        "mean_multistar_ambiguities": mean_or_zero(multistar_ambigs),

        "mean_defect_edges": mean_or_zero(mean_edges),
        "mean_defect_density": mean_or_zero(mean_densities),

        "max_nodes_seen": max(max_nodes_l),
        "max_edges_seen": max(max_edges_l),
        "max_births_in_step_seen": max(max_births_step_l),

        "top_component_types": comp_counts.most_common(10),
        "top_active_component_types": active_counts.most_common(10),
        "top_ambiguous_types": ambiguous_counts.most_common(10),
    }


# ------------------------------------------------------------
# Output
# ------------------------------------------------------------

def format_result(out):
    top = ", ".join([f"{k}:{v}" for k, v in out["top_active_component_types"][:5]])
    amb = ", ".join([f"{k}:{v}" for k, v in out["top_ambiguous_types"][:3]])
    tag = "[HEUR]" if out["p_ambig"] > 0.05 else "[NUM]"

    return (
        f"k={out['k']:3d}, k/N={out['k_over_N']:.4f} | "
        f"bf={out['birth_fraction']:.3f}, "
        f"mf={out['mean_final_nodes']:.1f}, "
        f"q50={out['q50_final']}, q90={out['q90_final']}, q99={out['q99_final']}, "
        f"rN={out['mean_r_N']:.4f}, "
        f"rN_late={out['mean_r_N_late']:.4f}, "
        f"rN_late_birth={out['mean_r_N_late_birth']:.4f}, "
        f"rN_late_strong={out['mean_r_N_late_strong']:.4f}, "
        f"birth_steps={out['mean_birth_step_fraction']:.3f}, "
        f"b/step={out['conditional_births_per_birth_step']:.3f}, "
        f"swap_rate={out['mean_single_edge_rate']:.4f}, "
        f"path_rate={out['mean_path_interaction_rate']:.4f}, "
        f"cyc_rate={out['mean_bound_cycle_rate']:.4f}, "
        f"p_frz={out['p_frozen']:.3f}, "
        f"p_strong={out['p_strongly_inflating']:.3f}, "
        f"p_ambig={out['p_ambig']:.3f}, "
        f"ambig={out['mean_ambiguous_events']:.2f}, "
        f"tie={out['mean_orientation_ties']:.2f}, "
        f"path_tie_fail={out['mean_unresolved_path_ties']:.2f}, "
        f"multistar={out['mean_multistar_ambiguities']:.2f}, "
        f"rho={out['mean_defect_density']:.5f}, "
        f"top=[{top}], amb=[{amb}] {tag}"
    )


def run_grid(grid_N, ratios, T=500, batch=200, seed=42, exclude_zero_delta=False):
    for N in grid_N:
        ks = sorted({
            max(1, int(round(N * r)))
            for r in ratios
            if max(1, int(round(N * r))) < N / 6
        })

        print(f"\n=== N={N}, T={T}, batch={batch} ===", flush=True)

        for k in ks:
            out = monte_carlo(
                N=N,
                k=k,
                T=T,
                batch=batch,
                seed=seed + 1_000_003 * N + 9_176 * k,
                exclude_zero_delta=exclude_zero_delta,
            )
            print(format_result(out), flush=True)


if __name__ == "__main__":
    run_grid(
        grid_N=[30, 60, 90, 120],
        ratios=[1 / 30, 1 / 20, 1 / 15, 1 / 12],
        T=500,
        batch=200,
        seed=42,
        exclude_zero_delta=False,
    )