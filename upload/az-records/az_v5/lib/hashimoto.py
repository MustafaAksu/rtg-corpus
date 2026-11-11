#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
az/lib/hashimoto.py
===================
Non-backtracking (Hashimoto) matrix engine for the RTG Arithmetic Resonance
and Zeta study (Thread C).

Frozen conventions (per Phase 0 freeze + pre-execution audits):
  - Edge convention: directed. Both orientations of a symmetric pair are
    INDEPENDENT directed edges (AZ-OPEN-EDGE decision / ENG-blocker-3).
  - Hashimoto state space: directed edges. Transition (u->v) -> (v->w) is
    allowed iff w != u (no immediate backtracking).
  - This module asserts NO analytic spectral expectation. All spectral
    statistics are compared to empirical nulls elsewhere.

Status: [ENG] engineering module; spectra are [NUM] only after benchmark pass.
"""

from __future__ import annotations
import numpy as np
from typing import List, Tuple, Dict, Optional

DirectedEdge = Tuple[int, int]  # (tail, head)


def build_hashimoto(edges: List[DirectedEdge]) -> np.ndarray:
    """
    Build the non-backtracking (Hashimoto) matrix B for a directed-edge list.

    B is indexed by directed edges. B[e1, e2] = 1 iff edge e1 = (u,v),
    edge e2 = (v,w), and w != u (non-backtracking condition).

    Returns a dense float matrix. Use build_hashimoto_sparse for large graphs.
    """
    m = len(edges)
    B = np.zeros((m, m), dtype=float)
    # index edges by their tail for fast successor lookup
    by_tail: Dict[int, List[int]] = {}
    for idx, (u, v) in enumerate(edges):
        by_tail.setdefault(u, []).append(idx)
    for i, (u, v) in enumerate(edges):
        for j in by_tail.get(v, []):
            w = edges[j][1]
            if w != u:
                B[i, j] = 1.0
    return B


def build_hashimoto_sparse(edges: List[DirectedEdge]):
    """Sparse CSR version for large graphs (ENG-blocker-4)."""
    from scipy.sparse import csr_matrix
    m = len(edges)
    by_tail: Dict[int, List[int]] = {}
    for idx, (u, v) in enumerate(edges):
        by_tail.setdefault(u, []).append(idx)
    rows, cols = [], []
    for i, (u, v) in enumerate(edges):
        for j in by_tail.get(v, []):
            w = edges[j][1]
            if w != u:
                rows.append(i)
                cols.append(j)
    data = np.ones(len(rows), dtype=float)
    return csr_matrix((data, (rows, cols)), shape=(m, m))


def hashimoto_spectrum_full(edges: List[DirectedEdge]) -> np.ndarray:
    """Full eigenvalue spectrum (dense). Declares spectrum-mode: full-spectrum."""
    B = build_hashimoto(edges)
    if B.shape[0] == 0:
        return np.array([], dtype=complex)
    return np.linalg.eigvals(B)


def hashimoto_spectrum_leading(edges: List[DirectedEdge], K: int):
    """
    Leading-K eigenvalues via sparse ARPACK (CONV-AZ-SPECTRUM-MODE: leading-K).
    Returns up to K eigenvalues of largest magnitude. Statistic computed from
    this is R_q^(K), NOT full-spectrum R_q.
    """
    from scipy.sparse.linalg import eigs
    B = build_hashimoto_sparse(edges)
    m = B.shape[0]
    if m == 0:
        return np.array([], dtype=complex)
    k = min(K, m - 2) if m > 2 else m
    if k <= 0:
        return np.linalg.eigvals(B.toarray())
    try:
        vals = eigs(B, k=k, which='LM', return_eigenvectors=False)
        return vals
    except Exception:
        # fall back to dense for tiny/awkward matrices
        return np.linalg.eigvals(B.toarray())


# ----- circular q-harmonic statistic R_q (replaces invalid C_q) -----

def R_q(eigs: np.ndarray, q: int) -> float:
    """
    Circular q-harmonic concentration statistic:
        R_q = | (1/n) sum_l exp(i q theta_l) |,  theta_l = arg(lambda_l).
    Measures q-fold angular concentration of eigenvalue arguments.
    Uniform-angle null: E[R_q] ~ 1/sqrt(n).
    """
    if len(eigs) == 0:
        return 0.0
    theta = np.angle(eigs)
    return float(np.abs(np.mean(np.exp(1j * q * theta))))


def divisor_set(N: int, q_max: int = 24) -> List[int]:
    """Q_N = {q : q | N, 2 <= q <= q_max}.  Excludes q=1. Frozen q_max."""
    return [q for q in range(2, q_max + 1) if N % q == 0]


def R_max(eigs: np.ndarray, N: int, q_max: int = 24) -> Tuple[float, int]:
    """
    R_max = max over q in Q_N of R_q  (CONV-AZ-STATS-MULTITEST).
    Returns (value, argmax_q). Significance must be assessed against the
    null distribution of R_max, not individual R_q.
    """
    Q = divisor_set(N, q_max)
    if not Q:
        return 0.0, -1
    best_v, best_q = -1.0, -1
    for q in Q:
        v = R_q(eigs, q)
        if v > best_v:
            best_v, best_q = v, q
    return best_v, best_q


def spectral_radius(eigs: np.ndarray) -> float:
    if len(eigs) == 0:
        return 0.0
    return float(np.max(np.abs(eigs)))


def spectral_gap(eigs: np.ndarray) -> float:
    if len(eigs) < 2:
        return 0.0
    mags = np.sort(np.abs(eigs))[::-1]
    return float(mags[0] - mags[1])


# ----- trace-moment fallback (Contribution A) -----

def nonbacktracking_moments(edges: List[DirectedEdge], m_max: int = 12) -> np.ndarray:
    """
    Truncated non-backtracking closed-walk moments Tr(B^m), m=1..m_max.
    Fallback diagnostic when full eigenspectrum is infeasible
    (CONV-AZ-SPECTRUM-MODE: trace-moment).
    log zeta_B(u) = sum_{m>=1} Tr(B^m)/m * u^m.
    """
    from scipy.sparse import csr_matrix
    B = build_hashimoto_sparse(edges)
    moments = np.zeros(m_max, dtype=float)
    if B.shape[0] == 0:
        return moments
    # Tr(B^m) via repeated sparse matmul on a running power is O(m * nnz * dim);
    # for moments we use stochastic trace estimation only if huge; here exact.
    Bp = csr_matrix(B)
    cur = csr_matrix(B)
    moments[0] = cur.diagonal().sum()
    for i in range(1, m_max):
        cur = cur @ Bp
        moments[i] = cur.diagonal().sum()
    return moments
