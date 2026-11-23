#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RTG p-Horizon Subgroup Module
=============================
Computes raw subgroup extra jets, mass, and cancellation invariants.
Status: [ENG/NUM diagnostic under raw Birkhoff-strobe convention]
"""

import math
from typing import Set, Dict, List, Tuple, Any
import rtg_p_core as core

def charge(a: int, b: int, p: int) -> int:
    return (a - b - 1) % p

def get_proper_subgroup_orders(p: int) -> List[int]:
    return [q for q in range(2, p) if p % q == 0]

def extra_charges_for_subgroup(p: int, q: int) -> Set[int]:
    if p % q != 0 or not (1 < q < p):
        raise ValueError(f"q={q} must be a proper subgroup order of p={p}")
    return set(range(q, p, q))

def project_by_charge(poly: core.Poly, p: int, allowed_charges: Set[int]) -> core.Poly:
    return {
        (a, b): c for (a, b), c in poly.items() 
        if charge(a, b, p) in allowed_charges
    }

def compute_reachable_basis(f1: Tuple[core.Poly, core.Poly], p: int, D: int, tol: float) -> Set[Tuple[int, int]]:
    basis = set()
    lam, _, _, _, _ = core.nconstants(p)
    for s in range(1, p):
        fs = core.iterate_map(f1, s, D, tol)
        R = core.nscale(fs[0], lam**(-s), tol)
        R[(1, 0)] = R.get((1, 0), 0.0j) - 1.0
        R = core.nclean(R, tol)
        for k in R.keys():
            if sum(k) >= 2:
                basis.add(k)
    return basis

def analyze_subgroups(p: int, D: int, tol: float) -> Dict[str, Any]:
    subgroups = get_proper_subgroup_orders(p)
    f1 = core.build_1step_map(p, D, tol)
    basis = compute_reachable_basis(f1, p, D, tol)
    
    result = {
        "p": p,
        "is_prime": len(subgroups) == 0,
        "subgroups": subgroups,
        "basis_size": len(basis),
        "C_sub_mult": 0,
        "C_sub_uniq": 0,
        "Delta_overlap": 0,
        "mass_mult_L1": 0.0,
        "mass_mult_L2": 0.0,
        "q_data": {}
    }
    
    if result["is_prime"]:
        return result
        
    global_supp = set()
    lam, _, _, _, _ = core.nconstants(p)
    
    for q in subgroups:
        s = p // q
        fs = core.iterate_map(f1, s, D, tol)
        
        R_raw = core.nscale(fs[0], lam**(-s), 0.0)
        R_raw[(1, 0)] = R_raw.get((1, 0), 0.0j) - 1.0
        R = core.nclean(R_raw, tol)
        R = {k: v for k, v in R.items() if sum(k) >= 2}
        
        allowed_charges = extra_charges_for_subgroup(p, q)
        J_extra = project_by_charge(R, p, allowed_charges)
        B_extra = {k for k in basis if charge(k[0], k[1], p) in allowed_charges}
        
        supp = len(J_extra)
        Z_miss = len(B_extra) - supp
        R_occ = supp / len(B_extra) if len(B_extra) > 0 else 0.0
        
        L1 = sum(abs(c) for c in J_extra.values())
        L2 = math.sqrt(sum(abs(c)**2 for c in J_extra.values()))
        missing_slots = sorted(B_extra - set(J_extra.keys()), key=lambda k: (sum(k), k))
        active_slots = sorted(J_extra.keys(), key=lambda k: (sum(k), k))
        
        # Inclusion Sanity Check
        outside = sorted(set(J_extra.keys()) - B_extra, key=lambda k: (sum(k), k))
        sanity_pass = len(outside) == 0
        
        global_supp.update(J_extra.keys())
        result["C_sub_mult"] += supp
        result["mass_mult_L1"] += L1
        result["mass_mult_L2"] += L2
        
        result["q_data"][q] = {
            "s": s,
            "K_extra": allowed_charges,
            "B_extra_size": len(B_extra),
            "supp": supp,
            "sanity_pass": sanity_pass,
            "outside_slots": outside,
            "Z_miss": Z_miss,
            "R_occ": R_occ,
            "mass_L1": L1,
            "mass_L2": L2,
            "missing_slots": missing_slots,
            "active_slots": active_slots
        }
        
    result["C_sub_uniq"] = len(global_supp)
    result["Delta_overlap"] = result["C_sub_mult"] - result["C_sub_uniq"]
    
    return result