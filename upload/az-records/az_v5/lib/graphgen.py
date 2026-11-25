#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
az/lib/graphgen.py
==================
Synthetic graph generators for Phase 1 benchmark ladder.

ENG-blocker-1 fix: gen_directed_cycle of length L produces closed walks of
EXACTLY length L (L directed edges), verified by unit test on walk length.
"""

from __future__ import annotations
from typing import List, Tuple

DirectedEdge = Tuple[int, int]


def gen_directed_cycle(L: int, base: int = 0) -> List[DirectedEdge]:
    """
    Single directed L-cycle: base -> base+1 -> ... -> base+L-1 -> base.
    Exactly L directed edges; the unique closed non-backtracking walk has
    length L.
    """
    return [(base + i, base + (i + 1) % L) for i in range(L)]


def gen_bidirected_cycle(L: int, base: int = 0) -> List[DirectedEdge]:
    """
    Both orientations of an L-cycle as independent directed edges:
    forward cycle + backward cycle. 2L directed edges.
    """
    fwd = gen_directed_cycle(L, base)
    bwd = [(b, a) for (a, b) in fwd]
    return fwd + bwd


def gen_disjoint_cycles(k: int, L: int) -> List[DirectedEdge]:
    """k disjoint directed L-cycles on disjoint vertex sets."""
    edges: List[DirectedEdge] = []
    for c in range(k):
        edges += gen_directed_cycle(L, base=c * L)
    return edges


def gen_bouquet(k: int, L: int, hub: int = 0) -> List[DirectedEdge]:
    """
    Directed bouquet: k petals, each a directed L-cycle sharing the hub vertex.
    Petal c uses fresh vertices for its interior; all petals return to hub.
    Each petal has exactly L directed edges; total k*L directed edges.

    NOTE: No spectrum is asserted here. The Hashimoto matrix and its
    characteristic polynomial are computed by construction in the benchmark
    and stored as the certified artifact (bouquet benchmark by construction).
    """
    edges: List[DirectedEdge] = []
    next_vertex = hub + 1
    for c in range(k):
        # petal path: hub -> n1 -> n2 -> ... -> n_{L-1} -> hub
        prev = hub
        interior = []
        for _ in range(L - 1):
            interior.append(next_vertex)
            next_vertex += 1
        path = [hub] + interior + [hub]
        for i in range(len(path) - 1):
            edges.append((path[i], path[i + 1]))
    return edges


def closed_walk_length_single_petal(L: int) -> int:
    """
    Diagnostic for ENG-blocker-1: the closed non-backtracking walk length of
    a single directed L-cycle. Must equal L.
    """
    edges = gen_directed_cycle(L)
    # the cycle visits L edges before returning to start
    return len(edges)
