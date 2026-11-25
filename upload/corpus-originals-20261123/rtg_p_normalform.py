#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RTG p-Horizon Normal Form Module
================================
Computes 1-step homological normal forms, resonant channels, and bridge gaps.
Status: [ALG structure / NUM]
"""

import math
from typing import Dict, Any, Tuple
import rtg_p_core as core

def charge(a: int, b: int, p: int) -> int:
    return (a - b - 1) % p

def solve_1step_normal_form(p: int, D: int, tol: float) -> Tuple[core.Poly, core.Poly]:
    f_W, _ = core.build_1step_map(p, D, tol)
    lam, lamb, _, _, _ = core.nconstants(p)
    
    H = {(1, 0): 1.0 + 0.0j}
    Hb = {(0, 1): 1.0 + 0.0j}
    N = {(1, 0): lam}
    Nb = {(0, 1): lamb}
    
    for d in range(2, D + 1):
        f_H = core.nsubst(f_W, H, Hb, D, tol)
        H_N = core.nsubst(H, N, Nb, D, tol)
        
        mismatch = core.nadd(f_H, core.nscale(H_N, -1.0, tol))
        mismatch_d = {k: v for k, v in mismatch.items() if sum(k) == d}
        
        for (a, b), c in mismatch_d.items():
            if abs(c) <= tol: continue
            
            eigenval_diff = (lam**a * lamb**b) - lam
            
            if charge(a, b, p) == 0 or abs(eigenval_diff) < 1e-9:
                N[(a, b)] = c
                Nb[(b, a)] = c.conjugate()
            else:
                h_ab = c / eigenval_diff
                H[(a, b)] = h_ab
                Hb[(b, a)] = h_ab.conjugate()
                
    return core.nclean(N, tol), core.nclean(H, tol)

def analyze_normal_form(p: int, D: int, tol: float, backend: str = "native-float", dps: int = 80) -> Dict[str, Any]:
    f1, f1b = core.build_1step_map(p, D, tol)
    N1, H1 = solve_1step_normal_form(p, D, tol)
    
    F_raw, _ = core.iterate_map((f1, f1b), p, D, tol)
    
    Nb1 = {(b, a): c.conjugate() for (a, b), c in N1.items()}
    F_1p, _ = core.iterate_map((N1, Nb1), p, D, tol)
    
    G_bridge = core.nadd(F_1p, core.nscale(F_raw, -1.0, tol))
    
    raw_retained = {k: v for k, v in f1.items() if sum(k) >= 2 and charge(k[0], k[1], p) == 0}
    nf_retained = {k: v for k, v in N1.items() if sum(k) >= 2}
    
    gap_32 = abs(G_bridge.get((3, 2), 0.0j)) if p != 6 else 0.0 
    gap_lattice = abs(G_bridge.get((0, p - 1), 0.0j)) if D >= p - 1 else None
    
    return {
        "p": p,
        "backend": backend,
        "dps": dps,
        "raw_retained_coeffs": raw_retained,
        "nf_retained_coeffs": nf_retained,
        "bridge_gap": G_bridge,
        "gap_32": gap_32,
        "gap_lattice": gap_lattice,
        "lattice_visible": D >= p - 1
    }