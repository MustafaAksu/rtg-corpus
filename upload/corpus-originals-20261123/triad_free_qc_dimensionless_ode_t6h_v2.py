#!/usr/bin/env python3
"""
RTG TRIADIC GENESIS: FREE-Qc DIMENSIONLESS ODE (T-6h_v2)
Module Status: [ENG / NUM diagnostic - Interior Flow Audit]

Integrates the 5D free-Qc system (Qs, u, mu, nu, rho) using the corrected
rho_dot chain rule. Seeds are initialized strictly inside the physical 
interior (99% capacity) to bypass the t=0 startup event and test attraction.
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

    # 1. Base Delta Polynomials
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

    # 2. Map to Dimensionless Rates
    DQs = sp.simplify(Delta_Qs.subs(sub_map))
    DQc = sp.simplify(Delta_Qc.subs(sub_map))
    DIsc = sp.simplify(Delta_Isc.subs(sub_map))
    Dwsc = sp.simplify(Delta_wsc.subs(sub_map))
    DQd = sp.simplify(Delta_Qd.subs(sub_map))

    dot_u = (DQc - u * DQs) / Qs
    dot_mu = (DIsc / (Qs * sp.sqrt(u))) - 0.5 * mu * (DQs / Qs) - 0.5 * mu * (DQc / (u * Qs))
    dot_nu = (Dwsc / (Qs * sp.sqrt(u))) - 0.5 * nu * (DQs / Qs) - 0.5 * nu * (DQc / (u * Qs))
    
    # Corrected rho_dot mapping
    dot_rho = (DQd / (2 * rho * Qs)) - 0.5 * rho * (DQs / Qs)

    # 3. Compile Lambdas
    vars_tuple = (Qs, u, mu, nu, rho)
    funcs = {
        'dQs': sp.lambdify(vars_tuple, DQs, 'numpy'),
        'du': sp.lambdify(vars_tuple, sp.simplify(dot_u), 'numpy'),
        'dmu': sp.lambdify(vars_tuple, sp.simplify(dot_mu), 'numpy'),
        'dnu': sp.lambdify(vars_tuple, sp.simplify(dot_nu), 'numpy'),
        'drho': sp.lambdify(vars_tuple, sp.simplify(dot_rho), 'numpy')
    }
    return funcs

def execute_t6h_interior_ode():
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

    # Interior Seeding (99% capacity to avoid exact boundary trap)
    scale_factor = 0.99
    seeds = {
        "Class_Ia_Interior": [1.0, 0.1, 0.0, 1.0 * scale_factor, 0.1],
        "Class_III_Interior_1": [
            0.7, 9.0/0.7, 
            scale_factor * (1.0/np.sqrt(0.7*9.0)), 
            scale_factor * (np.sqrt(0.7*9.0 - 1.0**2)/np.sqrt(0.7*9.0)), 
            0.3/np.sqrt(0.7)
        ],
        "Class_III_Interior_2": [
            0.7, 15.0/0.7, 
            scale_factor * (1.5/np.sqrt(0.7*15.0)), 
            scale_factor * (np.sqrt(0.7*15.0 - 1.5**2)/np.sqrt(0.7*15.0)), 
            0.5/np.sqrt(0.7)
        ]
    }

    # Event Guards 
    def ev_Qs_collapse(t, y): return y[0] - 1e-6
    ev_Qs_collapse.terminal = True
    ev_Qs_collapse.direction = -1

    def ev_u_collapse(t, y): return y[1] - 1e-6
    ev_u_collapse.terminal = True
    ev_u_collapse.direction = -1

    # Relaxed Plucker Guard
    PLUCKER_EPS = 1e-6
    def ev_plucker_violation(t, y): return (1.0 + PLUCKER_EPS) - (y[2]**2 + y[3]**2)
    ev_plucker_violation.terminal = True
    ev_plucker_violation.direction = -1

    def ev_u_runaway(t, y): return 1e6 - y[1]
    ev_u_runaway.terminal = True
    ev_u_runaway.direction = -1

    results = {}

    for name, init_state in seeds.items():
        sol = solve_ivp(
            rhs, (0.0, 500.0), init_state, method='Radau', 
            events=[ev_Qs_collapse, ev_u_collapse, ev_plucker_violation, ev_u_runaway], 
            rtol=1e-8, atol=1e-10
        )
        
        final_Qs, final_u, final_mu, final_nu, final_rho = sol.y[:, -1]
        
        term_class = "active_state"
        if sol.status == 1:
            if len(sol.t_events[0]) > 0: term_class = "longitudinal_collapse"
            elif len(sol.t_events[1]) > 0: term_class = "chiral_collapse"
            elif len(sol.t_events[2]) > 0: term_class = "plucker_boundary_reached"
            elif len(sol.t_events[3]) > 0: term_class = "u_runaway"

        results[name] = {
            "terminal_class": term_class,
            "t_final": float(sol.t[-1]),
            "solver_success": bool(sol.success),
            "solver_message": str(sol.message),
            "telemetry": {
                "initial_plucker_disk": float(init_state[2]**2 + init_state[3]**2),
                "final_Qs": float(final_Qs),
                "final_u": float(final_u),
                "final_rho": float(final_rho),
                "final_mu": float(final_mu),
                "final_nu": float(final_nu),
                "final_capacity": float(final_mu**2 + final_nu**2)
            }
        }

    manifest = {
        "software_environment": {
            "script_git_hash": "rtg_t6h_interior_flow_v2"
        },
        "physics_model": "Free-Qc 5D Dimensionless ODE (Interior Seeds, rho_dot patched)",
        "trajectory_sweep": results,
        "verification_status": {
            "status": "NUM diagnostic / Interior tracking executed"
        }
    }
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    execute_t6h_interior_ode()