#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
az/lib/graphio.py
=================
Graph ingestion for TDR-G / external defect graphs (ENG-blocker-2, -3).

Frozen semantics (AZ-1B):
  - Defect graphs are loaded as DIRECTED edge lists.
  - Both orientations of a symmetric pair are independent directed edges
    (the exporter is responsible for emitting both; the loader does NOT
    auto-symmetrize, to avoid the silent-core-empty failure mode).
  - MULTIEDGE / SELF-LOOP policy is explicit in the schema and recorded in
    the manifest. Default: simple directed graph (no multiedges, no self-loops);
    the Hashimoto rule is VERTEX-LEVEL non-backtracking ((u,v)->(v,w) iff w!=u).
  - The old gen_from_json operator-precedence bug is avoided by explicit
    parenthesization and schema validation with unit tests.

Status: [ENG].
"""

from __future__ import annotations
import json
from typing import List, Tuple, Dict, Any

DirectedEdge = Tuple[int, int]

REQUIRED_KEYS = {"directed", "edges"}


class GraphSchemaError(ValueError):
    pass


def load_graph_json(path: str) -> Tuple[List[DirectedEdge], Dict[str, Any]]:
    """
    Load a directed-edge graph from JSON with schema validation.

    Expected schema:
      {
        "directed": true,
        "multiedges_allowed": false,        # optional, default false
        "selfloops_allowed": false,         # optional, default false
        "edges": [[u, v], [v, u], ...]      # list of [tail, head] pairs
      }

    Returns (edges, meta). Raises GraphSchemaError on any violation.
    """
    with open(path) as f:
        obj = json.load(f)
    return parse_graph_obj(obj)


def parse_graph_obj(obj: Dict[str, Any]) -> Tuple[List[DirectedEdge], Dict[str, Any]]:
    if not isinstance(obj, dict):
        raise GraphSchemaError("top-level JSON must be an object")
    missing = REQUIRED_KEYS - set(obj.keys())
    if missing:
        raise GraphSchemaError(f"missing required keys: {sorted(missing)}")
    # explicit parenthesization (the old precedence bug was here)
    if not (obj["directed"] is True):
        raise GraphSchemaError("only directed graphs supported; 'directed' must be true")

    multiedges = bool(obj.get("multiedges_allowed", False))
    selfloops = bool(obj.get("selfloops_allowed", False))

    raw = obj["edges"]
    if not isinstance(raw, list):
        raise GraphSchemaError("'edges' must be a list")

    edges: List[DirectedEdge] = []
    seen = set()
    for i, e in enumerate(raw):
        if (not isinstance(e, (list, tuple))) or (len(e) != 2):
            raise GraphSchemaError(f"edge {i} is not a [tail, head] pair: {e!r}")
        u, v = e
        if not (isinstance(u, int) and isinstance(v, int)):
            raise GraphSchemaError(f"edge {i} endpoints must be ints: {e!r}")
        if (u == v) and (not selfloops):
            raise GraphSchemaError(f"edge {i} is a self-loop but selfloops_allowed=false")
        key = (u, v)
        if (key in seen) and (not multiedges):
            raise GraphSchemaError(f"edge {i} is a duplicate {key} but multiedges_allowed=false")
        seen.add(key)
        edges.append((u, v))

    meta = {
        "directed": True,
        "multiedges_allowed": multiedges,
        "selfloops_allowed": selfloops,
        "n_edges": len(edges),
        "n_vertices": len({x for e in edges for x in e}),
    }
    return edges, meta


def save_graph_json(path: str, edges: List[DirectedEdge],
                    multiedges_allowed: bool = False,
                    selfloops_allowed: bool = False) -> None:
    obj = {
        "directed": True,
        "multiedges_allowed": multiedges_allowed,
        "selfloops_allowed": selfloops_allowed,
        "edges": [[int(u), int(v)] for (u, v) in edges],
    }
    with open(path, "w") as f:
        json.dump(obj, f, indent=2)
