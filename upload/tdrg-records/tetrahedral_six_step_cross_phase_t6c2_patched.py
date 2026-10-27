#!/usr/bin/env python3
"""
RTG TRIADIC GENESIS: CROSS-PHASE SYNCHRONOUS EXTRACTION (T-6c2 Patched)
Module Status: [ENG / ALG diagnostic - invariant-closure extraction]
Derives the exact 6-step return for the cross-phase invariant (Delta I_sc) 
under the unrestricted generalized planar representative, preserving signed chirality.
"""

import sys
import json
import time
import sympy as sp

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def B_dot(u, v):
    """Dyadic B-Metric dot product."""
    return 2*u[0]*v[0] - u[0]*v[1] - u[1]*v[0] + 2*u[1]*v[1] + u[2]*v[2]

def truncate_total_degree(expr, variables, max_degree):
    expr = sp.expand(expr)
    if expr == 0: return sp.S.Zero
    poly = sp.Poly(expr, *variables, domain="EX")
    kept = sp.S.Zero
    for monom, coeff in poly.terms():
        if sum(monom) <= max_degree:
            term = coeff
            for v, p in zip(variables, monom):
                if p: term *= v**p
            kept += term
    return sp.expand(kept)

def graph_forces(S, C, D):
    Z = sp.Matrix([0, 0, 0])
    F0 = B_dot(S, S)*S + B_dot(C, C)*C + B_dot(D, D)*D
    F1 = B_dot(Z-S, Z-S)*(Z-S) + B_dot(C-S, C-S)*(C-S) + B_dot(D-S, D-S)*(D-S)
    F2 = B_dot(Z-C, Z-C)*(Z-C) + B_dot(S-C, S-C)*(S-C) + B_dot(D-C, D-C)*(D-C)
    F3 = B_dot(Z-D, Z-D)*(Z-D) + B_dot(S-D, S-D)*(S-D) + B_dot(C-D, C-D)*(C-D)
    return F1 - F0, F2 - F0, F3 - F0

def hex_step_pair(rho, eta, force_rho, force_eta):
    return rho - eta + force_rho, rho + force_eta

# ---------------------------------------------------------------------------
# Main Extraction
# ---------------------------------------------------------------------------
def run_cross_phase_extraction():
    t0 = time.time()
    STATE_TRUNC_DEGREE = 3
    DELTA_TRUNC_DEGREE = 4
    COMPOSITION_STEPS = 6

    # Coordinate Symbols
    s_rho, s_eta, c_rho, c_eta, r = sp.symbols("s_rho s_eta c_rho c_eta r", real=True)
    variables = [s_rho, s_eta, c_rho, c_eta, r]

    # Invariant Symbols (Using signed omega_sc)
    Qs, Qc, Isc, Omega = sp.symbols('Q_s Q_c I_sc omega_sc', real=True)

    # Initial State (Normalized Diagonal Gauge)
    S0 = sp.Matrix([s_rho, s_eta, 0])
    C0 = sp.Matrix([c_rho, c_eta, 0])
    D0 = sp.Matrix([-r / sp.sqrt(21), 2*r / sp.sqrt(21), r / sp.sqrt(3)])

    S, C, D = sp.Matrix(S0), sp.Matrix(C0), sp.Matrix(D0)

    for step in range(COMPOSITION_STEPS):
        print(f"[T6c2] step {step+1}/{COMPOSITION_STEPS} start", flush=True)
        Gs, Gc, Gd = graph_forces(S, C, D)
        next_s_rho, next_s_eta = hex_step_pair(S[0], S[1], Gs[0], Gs[1])
        next_c_rho, next_c_eta = hex_step_pair(C[0], C[1], Gc[0], Gc[1])
        next_d_rho, next_d_eta = hex_step_pair(D[0], D[1], Gd[0], Gd[1])
        next_d_z = D[2] + Gd[2]

        S = sp.Matrix([truncate_total_degree(next_s_rho, variables, STATE_TRUNC_DEGREE),
                       truncate_total_degree(next_s_eta, variables, STATE_TRUNC_DEGREE), 0])
        C = sp.Matrix([truncate_total_degree(next_c_rho, variables, STATE_TRUNC_DEGREE),
                       truncate_total_degree(next_c_eta, variables, STATE_TRUNC_DEGREE), 0])
        D = sp.Matrix([truncate_total_degree(next_d_rho, variables, STATE_TRUNC_DEGREE),
                       truncate_total_degree(next_d_eta, variables, STATE_TRUNC_DEGREE),
                       truncate_total_degree(next_d_z, variables, STATE_TRUNC_DEGREE)])
        
        print(f"[T6c2] step {step+1}/{COMPOSITION_STEPS} done elapsed={round(time.time()-t0, 3)}s", flush=True)

    # 1. Compute Raw Delta I_sc
    Isc_initial = B_dot(S0, C0)
    Isc_final = B_dot(S, C)
    Delta_Isc_raw = truncate_total_degree(sp.expand(Isc_final - Isc_initial), variables, DELTA_TRUNC_DEGREE)

    # 2. Generalized Axis Reduction Substitution
    s_rho_sub = sp.sqrt(Qs / 2)
    c_eta_sub = Omega / (sp.sqrt(3) * s_rho_sub)
    c_rho_sub = (c_eta_sub + (Isc / s_rho_sub)) / 2

    axis_subs = {
        s_eta: sp.S.Zero,
        s_rho: s_rho_sub,
        c_eta: c_eta_sub,
        c_rho: c_rho_sub
    }

    # 3. Strict Metric Audit (Pre-Substitution)
    S_axis = S0.subs(axis_subs)
    C_axis = C0.subs(axis_subs)
    
    audit_BSS = sp.simplify(B_dot(S_axis, S_axis) - Qs)
    audit_BSC = sp.simplify(B_dot(S_axis, C_axis) - Isc)
    audit_BCC = sp.simplify(B_dot(C_axis, C_axis) - ((Isc**2 + Omega**2)/Qs))

    Delta_Isc_reduced = sp.simplify(sp.expand(Delta_Isc_raw.subs(axis_subs)))

    # 4. Decompose by powers of r
    poly_Isc = sp.Poly(Delta_Isc_reduced, r)
    Isc_by_power = {
        f"r^{p}": str(sp.simplify(poly_Isc.coeff_monomial(r**p)))
        for p in range(poly_Isc.degree() + 1)
    }

    # 5. Strict Symbol Audit
    audit_locals = {
        's_rho': s_rho, 's_eta': s_eta, 'c_rho': c_rho, 'c_eta': c_eta,
        'Q_s': Qs, 'Q_c': Qc, 'I_sc': Isc, 'omega_sc': Omega, 'r': r, 'sqrt': sp.sqrt
    }
    
    all_reduced_exprs = [sp.sympify(v, locals=audit_locals) for v in Isc_by_power.values()]
    coordinate_symbols_survived = any(
        any(sym in expr.free_symbols for sym in [s_rho, s_eta, c_rho, c_eta])
        for expr in all_reduced_exprs
    )

    manifest = {
        "software_environment": {
            "python_version": sys.version.split()[0],
            "sympy_version": sp.__version__,
            "script_git_hash": "rtg_t6c2_cross_phase_extraction_v2"
        },
        "metric_audit": {
            "BSS_minus_Qs": str(audit_BSS),
            "BSC_minus_Isc": str(audit_BSC),
            "BCC_minus_implied_Qc": str(audit_BCC),
            "plucker_implied_Qc": "(I_sc**2 + omega_sc**2)/Q_s"
        },
        "reduced_parameters": {
            "Delta_Isc": Isc_by_power
        },
        "verification_status": {
            "coordinate_symbols_survived": bool(coordinate_symbols_survived),
            "status": "ALG diagnostic / invariant-closure extraction"
        }
    }
    
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    run_cross_phase_extraction()