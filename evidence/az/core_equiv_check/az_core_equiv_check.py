#!/usr/bin/env python3
"""Finite check of PROP-AZ-CORE-EQUIV, written on 12 Nov 2026.

[SESSION] A new check. It is NOT the lost certificate AZ-ART-PROP-CORE-EQUIV
(`prove_core_equiv.py`, `CORE_EQUIV_CERT_*.json`), which is not in the
repository, and it does not claim to reproduce it.

Statement checked, for finite simple undirected graphs G exported with both
orientations:

    R(G)  ==  both orientations of E(core_2(G))

where R(G) is the set of directed edges that lie on a directed cycle of the
Hashimoto transition digraph (DEF-AZ-CORE as written in the deposited
`CONVENTIONS_FROZEN.md`), and core_2(G) is the 2-core.

Three implementations are compared on every graph:
  own_R      this file: transitions from the definition, strongly connected
             components by an iterative Tarjan; an edge is recurrent iff its
             component has more than one member (a Hashimoto digraph of a
             simple graph has no self-transition).
  own_core   this file: 2-core by leaf stripping on edge sets.
  exp_core   the deposited exporter's `recurrent_core_directed` (optional).
and, on the small part, own transitions against the deposited library's
`build_hashimoto` (optional).

Usage:
  python3 -I az_core_equiv_check.py --nmax 7 [--jobs J]
      [--hashimoto PATH/lib/hashimoto.py] [--exporter PATH/conv_az_graph_export.py]

Exit code 0 only if no mismatch is found and every negative control fails as
it must.
"""
import argparse
import hashlib
import importlib.util
import itertools
import multiprocessing
import sys


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def pairs_of(n):
    return list(itertools.combinations(range(n), 2))


def graph_from_mask(pairs, mask):
    return [p for i, p in enumerate(pairs) if (mask >> i) & 1]


def both_orientations(und):
    out = []
    for a, b in und:
        out.append((a, b))
        out.append((b, a))
    return out


def transitions(directed):
    """succ[i] = indices j with head(e_i) == tail(e_j) and e_j != reverse(e_i)."""
    by_tail = {}
    for j, (u, v) in enumerate(directed):
        by_tail.setdefault(u, []).append(j)
    succ = []
    for (u, v) in directed:
        succ.append([j for j in by_tail.get(v, ()) if directed[j][1] != u])
    return succ


def scc_sizes(succ):
    """Iterative Tarjan. Returns comp[i] and the size of each component."""
    n = len(succ)
    index = [-1] * n
    low = [0] * n
    on = [False] * n
    comp = [-1] * n
    sizes = []
    stack = []
    counter = 0
    for root in range(n):
        if index[root] != -1:
            continue
        work = [(root, 0)]
        index[root] = low[root] = counter
        counter += 1
        stack.append(root)
        on[root] = True
        while work:
            v, k = work[-1]
            if k < len(succ[v]):
                work[-1] = (v, k + 1)
                w = succ[v][k]
                if index[w] == -1:
                    index[w] = low[w] = counter
                    counter += 1
                    stack.append(w)
                    on[w] = True
                    work.append((w, 0))
                elif on[w]:
                    if index[w] < low[v]:
                        low[v] = index[w]
            else:
                work.pop()
                if work:
                    p = work[-1][0]
                    if low[v] < low[p]:
                        low[p] = low[v]
                if low[v] == index[v]:
                    c = len(sizes)
                    size = 0
                    while True:
                        w = stack.pop()
                        on[w] = False
                        comp[w] = c
                        size += 1
                        if w == v:
                            break
                    sizes.append(size)
    return comp, sizes


def own_R(und):
    directed = both_orientations(und)
    succ = transitions(directed)
    comp, sizes = scc_sizes(succ)
    return frozenset(e for i, e in enumerate(directed) if sizes[comp[i]] > 1)


def own_core(und):
    edges = set(und)
    while True:
        deg = {}
        for a, b in edges:
            deg[a] = deg.get(a, 0) + 1
            deg[b] = deg.get(b, 0) + 1
        drop = {e for e in edges if deg[e[0]] <= 1 or deg[e[1]] <= 1}
        if not drop:
            break
        edges -= drop
    return frozenset(both_orientations(sorted(edges)))


def tailed_R(und):
    """A deliberately wider object, for the negative control: the recurrent edges
    together with every directed edge e such that e is reachable from a recurrent
    edge and reverse(e) reaches one, or the other way round. These are the edges
    of closed walks that run out along a pendant path, around a cycle and back,
    i.e. walks that are non-backtracking except at their closing point."""
    directed = both_orientations(und)
    succ = transitions(directed)
    pred = [[] for _ in directed]
    for i, s in enumerate(succ):
        for j in s:
            pred[j].append(i)
    comp, sizes = scc_sizes(succ)
    rec = {i for i in range(len(directed)) if sizes[comp[i]] > 1}

    def closure(start, nxt):
        seen = set(start)
        todo = list(start)
        while todo:
            i = todo.pop()
            for j in nxt[i]:
                if j not in seen:
                    seen.add(j)
                    todo.append(j)
        return seen

    fwd = closure(rec, succ)
    bwd = closure(rec, pred)
    idx = {e: i for i, e in enumerate(directed)}
    out = set(rec)
    for i, (u, v) in enumerate(directed):
        r = idx[(v, u)]
        if (i in fwd and r in bwd) or (i in bwd and r in fwd):
            out.add(i)
    return frozenset(directed[i] for i in out)


def check_range(args):
    n, lo, hi = args
    pairs = pairs_of(n)
    bad = []
    nonempty = 0
    bridged = 0
    for mask in range(lo, hi):
        und = graph_from_mask(pairs, mask)
        r = own_R(und)
        c = own_core(und)
        if r != c:
            bad.append((n, mask))
        if c:
            nonempty += 1
    return hi - lo, nonempty, bad


def named_cases():
    tri = [(0, 1), (1, 2), (0, 2)]
    return {
        "triangle": tri,
        "path_P4": [(0, 1), (1, 2), (2, 3)],
        "lollipop (triangle + pendant path of 2)": tri + [(2, 3), (3, 4)],
        "barbell (two triangles joined by an edge)": tri + [(3, 4), (4, 5), (3, 5), (2, 3)],
        "dumbbell (two triangles joined by a path of 3)": tri + [(4, 5), (5, 6), (4, 6), (2, 3), (3, 4)],
        "theta (two vertices joined by three paths)": [(0, 2), (2, 1), (0, 3), (3, 1), (0, 4), (4, 1)],
        "figure-8 (two triangles sharing a vertex)": tri + [(2, 3), (3, 4), (2, 4)],
        "K4": pairs_of(4),
        "tree with a 4-cycle hanging on a bridge": [(0, 1), (1, 2), (1, 3), (3, 4), (4, 5), (5, 6), (6, 3)],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=6)
    ap.add_argument("--jobs", type=int, default=1)
    ap.add_argument("--hashimoto")
    ap.add_argument("--exporter")
    a = ap.parse_args()

    print("az_core_equiv_check: finite check of PROP-AZ-CORE-EQUIV ([SESSION], new check)")
    print("script sha256:", sha256_file(__file__))
    print("python:", sys.version.split()[0])
    ok = True

    hm = ex = None
    if a.hashimoto:
        hm = load_module(a.hashimoto, "dep_hashimoto")
        print("deposited hashimoto.py sha256:", sha256_file(a.hashimoto))
    if a.exporter:
        ex = load_module(a.exporter, "dep_exporter")
        print("deposited exporter sha256:", sha256_file(a.exporter))

    # 1. named cases
    print("\n[1] named cases: |R|, |core|, equal")
    for name, und in named_cases().items():
        r, c = own_R(und), own_core(und)
        print("  %-48s %3d %3d %s" % (name, len(r), len(c), r == c))
        ok &= (r == c)

    # 2. cross-implementation part: all labelled graphs on n <= 5 vertices
    print("\n[2] cross-implementation, all labelled simple graphs, n = 1..5")
    n_cross = bad_tr = bad_ex = 0
    for n in range(1, 6):
        pairs = pairs_of(n)
        for mask in range(1 << len(pairs)):
            und = graph_from_mask(pairs, mask)
            n_cross += 1
            if hm is not None and und:
                directed = both_orientations(und)
                B = hm.build_hashimoto(directed)
                succ = transitions(directed)
                mine = {(i, j) for i, s in enumerate(succ) for j in s}
                theirs = {(i, j) for i in range(len(directed)) for j in range(len(directed)) if B[i, j] != 0}
                if mine != theirs:
                    bad_tr += 1
            if ex is not None:
                theirs = frozenset(tuple(e) for e in ex.recurrent_core_directed(und))
                if theirs != own_core(und) or theirs != own_R(und):
                    bad_ex += 1
    print("  graphs: %d" % n_cross)
    print("  own transitions vs deposited build_hashimoto: %s" %
          ("not run" if hm is None else "%d mismatches" % bad_tr))
    print("  deposited recurrent_core_directed vs own_core and own_R: %s" %
          ("not run" if ex is None else "%d mismatches" % bad_ex))
    ok &= (bad_tr == 0 and bad_ex == 0)

    # 3. exhaustive part
    print("\n[3] exhaustive, all labelled simple graphs: own_R == own_core")
    total = 0
    for n in range(1, a.nmax + 1):
        m = n * (n - 1) // 2
        count = 1 << m
        chunk = max(1, count // (a.jobs * 8)) if a.jobs > 1 else count
        tasks = [(n, lo, min(count, lo + chunk)) for lo in range(0, count, chunk)]
        if a.jobs > 1 and count > 4096:
            with multiprocessing.Pool(a.jobs) as pool:
                res = pool.map(check_range, tasks)
        else:
            res = [check_range(t) for t in tasks]
        g = sum(r[0] for r in res)
        ne = sum(r[1] for r in res)
        bad = [b for r in res for b in r[2]]
        total += g
        print("  n = %d: graphs %8d, with non-empty 2-core %8d, mismatches %d" % (n, g, ne, len(bad)))
        if bad:
            print("    first mismatches (n, edge mask):", bad[:5])
            ok = False
    print("  total graphs: %d" % total)

    # 4. negative controls: the comparison must be able to fail
    print("\n[4] negative controls (each must report a difference)")
    lol = named_cases()["lollipop (triangle + pendant path of 2)"]
    d1 = tailed_R(lol) != own_core(lol)
    print("  closed walks allowed to backtrack at the closing point, lollipop: differs = %s" % d1)
    p4 = named_cases()["path_P4"]
    d2 = frozenset(both_orientations(p4)) != own_R(p4)
    print("  no stripping (all edges kept), path P4: differs = %s" % d2)
    tri_one = [(0, 1), (1, 2), (2, 0)]          # one directed edge per pair: a directed 3-cycle
    succ = transitions(tri_one)
    comp, sizes = scc_sizes(succ)
    rec_one = frozenset(e for i, e in enumerate(tri_one) if sizes[comp[i]] > 1)
    d3 = rec_one != own_core([(0, 1), (1, 2), (0, 2)])
    print("  one directed edge per pair instead of both orientations, triangle: differs = %s" % d3)
    n_diff = 0
    for mask in range(1 << 10):
        und = graph_from_mask(pairs_of(5), mask)
        if tailed_R(und) != own_core(und):
            n_diff += 1
    d4 = n_diff > 0
    print("  tailed definition over all labelled graphs on 5 vertices: differs on %d of 1024" % n_diff)
    ok &= (d1 and d2 and d3 and d4)

    print("\nRESULT:", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
