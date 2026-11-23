#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RTG p-Horizon Core Module
=========================
Shared polynomial algebra and continuous-to-discrete map generator.
"""

import math
from typing import Dict, Tuple

Poly = Dict[Tuple[int, int], complex]

def nclean(poly: Poly, tol: float) -> Poly:
    return {k: v for k, v in poly.items() if abs(v) > tol}

def nadd(*ps: Poly) -> Poly:
    out: Poly = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, 0.0j) + v
    return nclean(out, 0.0)

def nscale(p: Poly, c: complex, tol: float) -> Poly:
    return nclean({k: c * v for k, v in p.items()}, tol)

def nmul(p: Poly, q: Poly, D: int, tol: float) -> Poly:
    out: Poly = {}
    for (a1, b1), c1 in p.items():
        for (a2, b2), c2 in q.items():
            if a1 + a2 + b1 + b2 <= D:
                k = (a1 + a2, b1 + b2)
                out[k] = out.get(k, 0.0j) + c1 * c2
    return nclean(out, tol)

def npow(p: Poly, n: int, D: int, tol: float) -> Poly:
    if n == 0: return {(0, 0): 1.0 + 0.0j}
    out = {(0, 0): 1.0 + 0.0j}
    for _ in range(n):
        out = nmul(out, p, D, tol)
    return nclean(out, tol)

def nsubst(poly: Poly, P: Poly, Q: Poly, D: int, tol: float) -> Poly:
    out: Poly = {}
    max_a = max((a for a, _ in poly), default=0)
    max_b = max((b for _, b in poly), default=0)
    
    Ppow = {0: {(0, 0): 1.0 + 0.0j}}
    Qpow = {0: {(0, 0): 1.0 + 0.0j}}
    for n in range(1, max_a + 1): Ppow[n] = nmul(Ppow[n - 1], P, D, tol)
    for n in range(1, max_b + 1): Qpow[n] = nmul(Qpow[n - 1], Q, D, tol)
        
    for (a, b), c in poly.items():
        term = nmul(Ppow[a], Qpow[b], D, tol)
        out = nadd(out, nscale(term, c, tol))
    return nclean(out, tol)

def nconstants(p: int):
    theta = 2.0 * math.pi / p
    lam = complex(math.cos(theta), math.sin(theta))
    lamb = complex(math.cos(theta), -math.sin(theta))
    K = 2.0 - 2.0 * math.cos(theta)
    gamma = (lam - 1.0) / K
    gammab = (lamb - 1.0) / K
    return lam, lamb, K, gamma, gammab

def build_1step_map(p: int, D: int, tol: float) -> Tuple[Poly, Poly]:
    lam, lamb, K, gamma, gammab = nconstants(p)
    P, Q = {(1, 0): 1.0 + 0.0j}, {(0, 1): 1.0 + 0.0j}
    
    denom = gamma - gammab
    eta = nscale(nadd(P, nscale(Q, -1.0, tol)), 1.0 / denom, tol)
    rho = nscale(nadd(nscale(Q, gamma, tol), nscale(P, -gammab, tol)), 1.0 / denom, tol)
    
    s, e = {}, {}
    for n in range(1, D + 1, 2):
        s = nadd(s, nscale(npow(eta, n, D, tol), ((-1)**((n-1)//2)) / math.factorial(n), tol))
    for n in range(1, D + 1):
        e = nadd(e, nscale(npow(rho, n, D, tol), 1.0 / math.factorial(n), tol))
    
    rho1 = nadd(rho, nscale(s, -1.0, tol))
    eta1 = nadd(eta, nscale(e, K, tol), nscale(s, -K, tol))
    
    W1 = nadd(rho1, nscale(eta1, gamma, tol))
    Wb1 = nadd(rho1, nscale(eta1, gammab, tol))
    return nclean(W1, tol), nclean(Wb1, tol)

def iterate_map(F: Tuple[Poly, Poly], n: int, D: int, tol: float) -> Tuple[Poly, Poly]:
    G = ({(1, 0): 1.0 + 0.0j}, {(0, 1): 1.0 + 0.0j})
    for _ in range(n):
        G = (nsubst(F[0], G[0], G[1], D, tol), nsubst(F[1], G[0], G[1], D, tol))
    return G