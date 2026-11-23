#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
spectral_radius_patch.py  —  drop-in replacement for
spectral_baseline.hashimoto_spectral_radius.

AUDIT FINDING (Zeta-side independent cross-check against certified az_v5 engine):
the original power-iteration implementation can UNDER-report the spectral radius
whenever the dominant spectral subspace is NOT a single positive Perron direction.
This includes BOTH complex-conjugate dominant pairs AND real +-R dominant pairs.

  Failing example 1 (synthetic, complex pair): bouquet(k=2,L=4)
    original power-iteration : 1.000000   true (dense+az_v5): 2^(1/4)=1.189207
  Failing example 2 (REAL DATA, real +-R pair): N=120 k=8 seed1 Core(G_T)
    original power-iteration : 2.879301   true (dense+az_v5): 3.305845

Root cause: a real start vector under max-abs normalization, with an
|norm-last|<tol early-exit, settles on a subdominant plateau whenever the leading
magnitude is shared by a +-R pair (real or complex). The iterate's max-abs ratio
then oscillates (e.g. 8.0, 2.5, 3.45, 3.12, 4.04, 2.82, ...) and the early-exit
fires below the true radius. This is generic for non-backtracking operators on
near-bipartite/symmetric graphs and on the cyclically symmetric graphs the study
is built to detect, so it systematically biases R_max DOWNWARD on exactly the
structured graphs that carry a signal.

Impact:
  - G_cumulative (dense, real Perron-dominant): original is usually CORRECT, but
    must be re-certified with this function.
  - Core(G_T) / small structured cores (often complex-dominant): original is
    UNRELIABLE and can mask a real signal by under-reporting R_max.

Fix: ARPACK largest-magnitude eigenvalues (which='LM'), dense fallback for tiny
matrices. Certified to match the dense spectrum to <1e-6 on the full benchmark
ladder (AUDIT_SPECTRAL_RADIUS_CERT.json).
"""
from __future__ import annotations
from collections import defaultdict
import numpy as np


def _build_sparse(directed_edges):
    from scipy.sparse import csr_matrix
    m = len(directed_edges)
    idx = {e: i for i, e in enumerate(directed_edges)}
    out_from = defaultdict(list)
    for (u, v) in directed_edges:
        out_from[u].append((u, v))
    rows, cols = [], []
    for i, (u, v) in enumerate(directed_edges):
        for (v2, w) in out_from[v]:
            if w != u:
                rows.append(i)
                cols.append(idx[(v2, w)])
    data = np.ones(len(rows))
    return csr_matrix((data, (rows, cols)), shape=(m, m))


def hashimoto_spectral_radius(directed_edges, k_eigs: int = 6) -> float:
    """Corrected: largest |eigenvalue| of the non-backtracking operator via ARPACK."""
    directed_edges = [(int(a), int(b)) for a, b in directed_edges]
    # multiedge guard: endpoint-pair indexing collapses duplicates, so this patch
    # is only valid for simple directed graphs. Fail loudly otherwise.
    if len(set(directed_edges)) != len(directed_edges):
        raise ValueError("multiedges not supported by spectral_radius_patch "
                         "(endpoint-pair indexing); use edge-ID indexing for multigraphs")
    m = len(directed_edges)
    if m == 0:
        return 0.0
    B = _build_sparse(directed_edges)
    if m <= 3:
        return float(np.max(np.abs(np.linalg.eigvals(B.toarray()))))
    from scipy.sparse.linalg import eigs
    try:
        vals = eigs(B, k=min(k_eigs, m - 2), which='LM', return_eigenvectors=False)
        return float(np.max(np.abs(vals)))
    except Exception:
        return float(np.max(np.abs(np.linalg.eigvals(B.toarray()))))
