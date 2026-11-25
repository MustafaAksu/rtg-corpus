#!/usr/bin/env python3
"""
RTG TRIADIC GENESIS: SAFE-ARC BASIN SEARCH (T-6j)
Module Status: [ENG / NUM diagnostic - Basin of Attraction Map]

Initializes a grid of phase angles deep in the interior phase space (K=0.25).
Integrates the 5D free-Qc flow to the Plucker boundary (K=1.0) and evaluates 
whether the trajectory impacts a safe reflecting sector or a fatal transpiercing sector.
"""

import sys
import json
import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp

def compile_dimensionless_vector_field():
    Qs, Qc, Isc, wsc, r = sp.symbols('Q_s Q_c I_sc omega_sc r', real=True)
    syms = {s.name: s for s in (Qs, Qc, Isc, wsc, r)}
    u, mu, nu, rho = sp.symbols('u mu nu rho', real=True)
    
    sub_map = {
        Qc: u * Qs,
        Isc: mu * sp.sqrt(u) * Qs,
        wsc: nu * sp.sqrt(u) * Qs,
        r: rho * sp.sqrt(Qs)
    }

    # Base Delta Polynomials
    Qs_r0 = -18*Isc**2 + 18*Isc*Qs - 12*sp.sqrt(3)*Isc*wsc - 24*Qs**2 + 6*sp.sqrt(3)*Qs*wsc - 6*wsc**2
    Qs_r1 = -6*sp.sqrt(42)*(Qs**(sp.Rational(3,2)))/7
    Qs_r2 = -26*Qs/7
    Delta_Qs = Qs_r0 + r*Qs_r1 + (r**2)*Qs_r2

    term1 = -4*Isc**4 - 8*(Isc**2)*(wsc**2)
    term2 = (Qs**2) * (-3*Isc**2 + 2*sp.sqrt(3)*Isc*wsc - wsc**2)
    term3 = Qs * (3*Isc**3 - sp.sqrt(3)*(Isc**2)*wsc + 3*Isc*(wsc**2) - sp.sqrt(3)*(wsc**3))
    term4 = -4*wsc**4
    Qc_r0 = (6 / Qs**2) * (term1 + term2 + term3 + term4)
    Qc_r1 = (6 / (7 * Qs**(sp.Rational(3,2)))) * (-sp.sqrt(42)*Isc**3 + 5*sp.sqrt(14)*(Isc**2)*wsc - sp.sqrt(42)*Isc*(wsc**2) + 5*sp.sqrt(14)*(wsc**3))
    Qc_r2 = (2 / (7 * Qs)) * (-13*Isc**2 + 20*sp.sqrt(3)*Isc*wsc - 57*wsc**2)
    Delta_Qc = Qc_r0 + r*Qc_r1 + (r**2)*Qc_r2

    term_isc1 = -7*Isc**3 - 3*sp.sqrt(3)*(Isc**2)*wsc - 7*Isc*(wsc**2)
    term_isc2 = Qs * (6*Isc**2 - 7*Isc*Qs + 3*sp.sqrt(3)*Qs*wsc + 2*wsc**2)
    term_isc3 = -3*sp.sqrt(3)*(wsc**3)
    Isc_r0 = (3 / Qs) * (term_isc1 + term_isc2 + term_isc3)
    Isc_r1 = (1 / (7 * sp.sqrt(Qs))) * (-3*sp.sqrt(42)*Isc**2 - 6*sp.sqrt(14)*Isc*wsc + 3*Qs*(-sp.sqrt(42)*Isc + 7*sp.sqrt(14)*wsc) + 7*sp.sqrt(42)*wsc**2)
    Isc_r2 = -(26 / 7)*Isc + (20*sp.sqrt(3) / 7)*wsc
    Delta_Isc = Isc_r0 + r*Isc_r1 + (r**2)*Isc_r2

    w_r0 = (-3*Isc**3 + 5*sp.sqrt(3)*(Isc**2)*wsc - 3*Isc*(wsc**2) + Qs*(3*Isc*Qs - 4*sp.sqrt(3)*Isc*wsc + 5*sp.sqrt(3)*Qs*wsc) + 5*sp.sqrt(3)*(wsc**3))/Qs
    w_r1 = (-7*sp.sqrt(42)*(Isc**2) + 10*sp.sqrt(14)*Isc*wsc + Qs*(7*sp.sqrt(42)*Isc + 3*sp.sqrt(14)*wsc) - 5*sp.sqrt(42)*(wsc**2))/(7*sp.sqrt(Qs))
    w_r2 = 10*sp.sqrt(3)*wsc/3
    Delta_wsc = w_r0 + r*w_r1 + (r**2)*w_r2

    Qd_r2 = 8*(-17*Isc**2 + 3*sp.sqrt(3)*Isc*wsc - 17*Qs**2 - 4*wsc**2)/(7*Qs)
    Qd_r3 = 2*(-31*sp.sqrt(42)*Isc - 31*sp.sqrt(42)*Qs + 15*sp.sqrt(14)*wsc)/(21*sp.sqrt(Qs))
    Qd_r4 = -32
    Delta_Qd = (r**2)*Qd_r2 + (r**3)*Qd_r3 + (r**4)*Qd_r4

    # Dimensionless Rates
    DQs = sp.simplify(Delta_Qs.subs(sub_map))
    DQc = sp.simplify(Delta_Qc.subs(sub_map))
    DIsc = sp.simplify(Delta_Isc.subs(sub_map))
    Dwsc = sp.simplify(Delta_wsc.subs(sub_map))
    DQd = sp.simplify(Delta_Qd.subs(sub_map))

    dot_u = (DQc - u * DQs) / Qs
    dot_mu = (DIsc / (Qs * sp.sqrt(u))) - 0.5 * mu * (DQs / Qs) - 0.5 * mu * (DQc / (u * Qs))
    dot_nu = (Dwsc / (Qs * sp.sqrt(u))) - 0.5 * nu * (DQs / Qs) - 0.5 * nu * (DQc / (u * Qs))
    dot_rho = (DQd / (2 * rho * Qs)) - 0.5 * rho * (DQs / Qs)
    
    # Radial Flow K_dot
    dot_K = sp.simplify(2 * mu * dot_mu + 2 * nu * dot_nu)

    vars_tuple = (Qs, u, mu, nu, rho)
    funcs = {
        'dQs': sp.lambdify(vars_tuple, DQs, 'numpy'),
        'du': sp.lambdify(vars_tuple, sp.simplify(dot_u), 'numpy'),
        'dmu': sp.lambdify(vars_tuple, sp.simplify(dot_mu), 'numpy'),
        'dnu': sp.lambdify(vars_tuple, sp.simplify(dot_nu), 'numpy'),
        'drho': sp.lambdify(vars_tuple, sp.simplify(dot_rho), 'numpy'),
        'dK': sp.lambdify(vars_tuple, sp.simplify(dot_K), 'numpy')
    }
    return funcs

def execute_t6j_basin_search():
    funcs = compile_dimensionless_vector_field()
    
    def rhs(t, y):
        Qs, u, mu, nu, rho = y
        Qs = max(float(Qs), 1e-12)
        u = max(float(u), 1e-12)
        rho = max(float(rho), 1e-12)
        args = (Qs, u, mu, nu, rho)
        return np.array([
            funcs['dQs'](*args), funcs['du'](*args),
            funcs['dmu'](*args), funcs['dnu'](*args), funcs['drho'](*args)
        ], dtype=float)

    # Event Guards
    PLUCKER_EPS = 1e-6
    def ev_plucker_boundary(t, y): return (1.0 + PLUCKER_EPS) - (y[2]**2 + y[3]**2)
    ev_plucker_boundary.terminal = True
    ev_plucker_boundary.direction = -1

    def ev_u_runaway(t, y): return 1e6 - y[1]
    ev_u_runaway.terminal = True
    ev_u_runaway.direction = -1
    
    def ev_Qs_collapse(t, y): return y[0] - 1e-6
    ev_Qs_collapse.terminal = True
    ev_Qs_collapse.direction = -1

    # Safe sector boundary from T-6i2 (High Chiral Load 2 approximation)
    THETA_SAFE_MAX = 0.3972 

    # Sweeping initial conditions from the deep interior
    K_init = 0.25
    theta_inits = np.linspace(0.01, 1.56, 15)  # Avoid exact 0 or pi/2 for numerical safety
    
    # Representative High Chiral Load background parameters
    Qs_0 = 0.7
    u_0 = 21.4
    rho_0 = 0.60
    
    results = {}
    
    for t_init in theta_inits:
        mu_0 = np.sqrt(K_init) * np.cos(t_init)
        nu_0 = np.sqrt(K_init) * np.sin(t_init)
        
        init_state = [Qs_0, u_0, mu_0, nu_0, rho_0]
        
        sol = solve_ivp(
            rhs, (0.0, 100.0), init_state, method='Radau', 
            events=[ev_plucker_boundary, ev_u_runaway, ev_Qs_collapse], 
            rtol=1e-8, atol=1e-10
        )
        
        final_Qs, final_u, final_mu, final_nu, final_rho = sol.y[:, -1]
        final_theta = np.arctan2(final_nu, final_mu)
        final_K_dot = funcs['dK'](final_Qs, final_u, final_mu, final_nu, final_rho)
        
        term_class = "active_state"
        if sol.status == 1:
            if len(sol.t_events[0]) > 0: term_class = "plucker_boundary_reached"
            elif len(sol.t_events[1]) > 0: term_class = "u_runaway"
            elif len(sol.t_events[2]) > 0: term_class = "longitudinal_collapse"
            
        status = "Transpierced (Fatal Sector)"
        if final_theta <= THETA_SAFE_MAX and final_K_dot <= 0:
            status = "Reflected (Safe Sector)"
            
        results[f"theta_init_{t_init:.2f}"] = {
            "impact_theta": float(final_theta),
            "final_K_dot": float(final_K_dot),
            "sector_status": status,
            "terminal_event": term_class
        }

    manifest = {
        "software_environment": {"script_git_hash": "rtg_t6j_basin_search"},
        "physics_model": f"Deep Interior Phase Sweep (K_init={K_init})",
        "basin_map": results,
        "verification_status": {"status": "NUM diagnostic / Basin of Attraction Executed"}
    }
    
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    execute_t6j_basin_search()