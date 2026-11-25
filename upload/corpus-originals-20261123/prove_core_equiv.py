#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
prove_core_equiv.py — formal stress suite for PROP-AZ-CORE-EQUIV.

Claim: for a finite simple undirected graph exported in directed-both-orientations
form, the directed edges that lie on at least one NON-BACKTRACKING CLOSED WALK are
exactly the directed orientations of edges whose underlying undirected edge is in
the undirected 2-core.

Three independently-computed objects compared edge-for-edge:
  A = undirected 2-core, re-directed both orientations
  B = directed edges in a Hashimoto-transition SCC that contains a cycle
      (= edges on a non-backtracking closed walk)
  C = direct check: edge e is on a NB closed walk iff e is reachable from itself
      in the NB transition digraph (path e -> ... -> e of length >= 1)

Stress cases include the bridge-between-lobes cases the audit flagged:
barbell, lollipop, theta, figure-8.
"""
from __future__ import annotations
import sys, json, random, argparse
from collections import defaultdict


def directed_both(undirected_edges):
    out = []
    seen = set()
    for a, b in undirected_edges:
        if a == b:
            continue
        for e in ((a, b), (b, a)):
            if e not in seen:
                seen.add(e); out.append(e)
    return out


def undirected_2core_redirected(undirected_edges):
    adj = defaultdict(set)
    for a, b in undirected_edges:
        if a != b:
            adj[a].add(b); adj[b].add(a)
    changed = True
    while changed:
        changed = False
        for v in [v for v in list(adj) if len(adj[v]) <= 1]:
            for w in list(adj[v]):
                adj[w].discard(v)
            del adj[v]; changed = True
    core = set(adj)
    kept = []
    seenu = set()
    for a, b in undirected_edges:
        if a in core and b in core and a != b:
            u = tuple(sorted((a, b)))
            if u not in seenu:
                seenu.add(u); kept.append((a, b))
    return set(directed_both(kept))


def _nb_succ(directed_edges):
    idx = {e: i for i, e in enumerate(directed_edges)}
    out_from = defaultdict(list)
    for (u, v) in directed_edges:
        out_from[u].append((u, v))
    m = len(directed_edges)
    succ = [[] for _ in range(m)]
    for i, (u, v) in enumerate(directed_edges):
        for (v2, w) in out_from[v]:
            if w != u:
                succ[i].append(idx[(v2, w)])
    return idx, succ, m


def nb_scc_with_cycle(directed_edges):
    """Object B: edges in an SCC of the NB transition digraph that contains a cycle."""
    idx, succ, m = _nb_succ(directed_edges)
    index = [None]*m; low = [0]*m; onstack = [False]*m; stack = []; cnt = [0]; sccs = []
    sys.setrecursionlimit(1000000)
    def sc(v):
        index[v] = cnt[0]; low[v] = cnt[0]; cnt[0] += 1
        stack.append(v); onstack[v] = True
        for w in succ[v]:
            if index[w] is None:
                sc(w); low[v] = min(low[v], low[w])
            elif onstack[w]:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop(); onstack[w] = False; comp.append(w)
                if w == v: break
            sccs.append(comp)
    for v in range(m):
        if index[v] is None:
            sc(v)
    keep = set()
    for comp in sccs:
        if len(comp) > 1:
            keep.update(comp)
        else:
            v = comp[0]
            if v in succ[v]:
                keep.add(v)
    return set(directed_edges[i] for i in keep)


def nb_on_closed_walk(directed_edges):
    """Object C: edge e on a NB closed walk iff e reachable from itself (len>=1)."""
    idx, succ, m = _nb_succ(directed_edges)
    on = set()
    for start in range(m):
        # BFS/DFS from successors of start; can we get back to start?
        stack = list(succ[start]); seen = set(stack)
        found = (start in succ[start])
        while stack and not found:
            x = stack.pop()
            if x == start:
                found = True; break
            for y in succ[x]:
                if y == start:
                    found = True; break
                if y not in seen:
                    seen.add(y); stack.append(y)
        if found:
            on.add(directed_edges[start])
    return on


# ---- named stress graphs ----
def g_barbell(n=4, bridge_len=1):
    """Two K_n cliques joined by a path (bridge). Bridge edges are in the 2-core
    but on no simple cycle — the hard case."""
    e = []
    for base in (0, 100):
        nodes = [base+i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                e.append((nodes[i], nodes[j]))
    # bridge from 0 to 100 via intermediate nodes
    chain = [0] + [200+i for i in range(bridge_len-1)] + [100]
    for i in range(len(chain)-1):
        e.append((chain[i], chain[i+1]))
    return e


def g_lollipop(n=4, tail=3):
    e = []
    nodes = list(range(n))
    for i in range(n):
        for j in range(i+1, n):
            e.append((nodes[i], nodes[j]))
    chain = [0] + [100+i for i in range(tail)]
    for i in range(len(chain)-1):
        e.append((chain[i], chain[i+1]))
    return e


def g_theta():
    # two vertices joined by three internally-disjoint paths
    return [(0,1),(1,2),(2,9),
            (0,3),(3,4),(4,9),
            (0,5),(5,6),(6,9)]


def g_figure8():
    # two cycles sharing one vertex
    return [(0,1),(1,2),(2,0),
            (0,3),(3,4),(4,0)]


def check_graph(undirected_edges):
    de = directed_both(undirected_edges)
    A = undirected_2core_redirected(undirected_edges)
    B = nb_scc_with_cycle(de)
    C = nb_on_closed_walk(de)
    return (A == B == C), {"A": len(A), "B": len(B), "C": len(C),
                           "AB": A == B, "BC": B == C, "AC": A == C}


def random_simple_graph(rng, n):
    e = set()
    for _ in range(rng.randint(n, 3*n)):
        a, b = rng.randint(0, n-1), rng.randint(0, n-1)
        if a != b:
            e.add(tuple(sorted((a, b))))
    return list(e)


def exhaustive_graphs(n):
    """All simple graphs on n labeled vertices (up to the edge set)."""
    import itertools
    verts = list(range(n))
    all_pairs = list(itertools.combinations(verts, 2))
    for r in range(len(all_pairs)+1):
        for subset in itertools.combinations(all_pairs, r):
            yield list(subset)


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--exhaustive-n", type=int, default=0)
    ap.add_argument("--random", type=int, default=0)
    ap.add_argument("--include-barbell", action="store_true")
    ap.add_argument("--include-lollipop", action="store_true")
    ap.add_argument("--include-theta", action="store_true")
    ap.add_argument("--include-figure8", action="store_true")
    ap.add_argument("--export-report", default=None)
    args = ap.parse_args(argv)

    fails = []
    n_checked = 0

    named = []
    if args.include_barbell:
        for bl in (1, 2, 3):
            named.append((f"barbell_n4_bridge{bl}", g_barbell(4, bl)))
    if args.include_lollipop:
        named.append(("lollipop_n4_tail3", g_lollipop(4, 3)))
    if args.include_theta:
        named.append(("theta", g_theta()))
    if args.include_figure8:
        named.append(("figure8", g_figure8()))

    for name, g in named:
        ok, info = check_graph(g)
        n_checked += 1
        print(f"  {'PASS' if ok else 'FAIL'} {name}: {info}")
        if not ok:
            fails.append({"case": name, "info": info})

    if args.exhaustive_n:
        cnt = 0
        for g in exhaustive_graphs(args.exhaustive_n):
            ok, info = check_graph(g)
            n_checked += 1; cnt += 1
            if not ok:
                fails.append({"case": f"exhaustive_n{args.exhaustive_n}", "edges": g, "info": info})
        print(f"  exhaustive n={args.exhaustive_n}: {cnt} graphs checked")

    if args.random:
        rng = random.Random(12345)
        for _ in range(args.random):
            n = rng.randint(3, 14)
            g = random_simple_graph(rng, n)
            if not g:
                continue
            ok, info = check_graph(g)
            n_checked += 1
            if not ok:
                fails.append({"case": "random", "edges": g, "info": info})
        print(f"  random: {args.random} graphs checked")

    passed = len(fails) == 0
    print(f"\nTOTAL checked: {n_checked}  counterexamples: {len(fails)}")
    print(f"PROP-AZ-CORE-EQUIV stress suite: {'PASS' if passed else 'FAIL'}")

    if args.export_report:
        json.dump({"checked": n_checked, "counterexamples": fails, "passed": passed},
                  open(args.export_report, "w"), indent=2)
        print(f"report -> {args.export_report}")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
