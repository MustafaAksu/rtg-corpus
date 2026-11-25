#!/usr/bin/env python3
"""
RTG TRIADIC GENESIS: DIRECT ORIENTATION ODE (T-6f_v2)
Module Status: [ENG / NUM diagnostic - Explicit Runaway Tracking]

Executes the constrained 4D system (Qs, Isc, w_sc, r) with Qc substituted dynamically.
Tracks explicit solver success flags, messages, and bounds the integration 
with strict validity guards to accurately classify orientation avalanches.
"""

import sys
import json
import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp

def compile_vector_field():
    Qs, Qc, Isc, Omega, r = sp.symbols('Q_s Q_c I_sc omega_sc r', real=True)
    syms = (Qs, Qc, Isc, Omega, r)
    locs = {s.name: s for s in syms}
    
    # Delta Qs
    Qs_r0 = "-18*I_sc**2 + 18*I_sc*Q_s - 12*sqrt(3)*I_sc*omega_sc - 24*Q_s**2 + 6*sqrt(3)*Q_s*omega_sc - 6*omega_sc**2"
    Qs_r1 = "-6*sqrt(42)*Q_s**(3/2)/7"
    Qs_r2 = "-26*Q_s/7"
    
    # Delta Isc
    Isc_r0 = "3*(-7*I_sc**3 - 3*sqrt(3)*I_sc**2*omega_sc - 7*I_sc*omega_sc**2 + Q_s*(6*I_sc**2 - 7*I_sc*Q_s + 3*sqrt(3)*Q_s*omega_sc + 2*omega_sc**2) - 3*sqrt(3)*omega_sc**3)/Q_s"
    Isc_r1 = "(-3*sqrt(42)*I_sc**2 - 6*sqrt(14)*I_sc*omega_sc + 3*Q_s*(-sqrt(42)*I_sc + 7*sqrt(14)*omega_sc) + 7*sqrt(42)*omega_sc**2)/(7*sqrt(Q_s))"
    Isc_r2 = "-26*I_sc/7 + 20*sqrt(3)*omega_sc/7"

    # Delta omega_sc (T-6e)
    w_r0 = "(-3*I_sc**3 + 5*sqrt(3)*I_sc**2*omega_sc - 3*I_sc*omega_sc**2 + Q_s*(3*I_sc*Q_s - 4*sqrt(3)*I_sc*omega_sc + 5*sqrt(3)*Q_s*omega_sc) + 5*sqrt(3)*omega_sc**3)/Q_s"
    w_r1 = "(-7*sqrt(42)*I_sc**2 + 10*sqrt(14)*I_sc*omega_sc + Q_s*(7*sqrt(42)*I_sc + 3*sqrt(14)*omega_sc) - 5*sqrt(42)*omega_sc**2)/(7*sqrt(Q_s))"
    w_r2 = "10*sqrt(3)*omega_sc/3"

    # Delta Qd
    Qd_r2 = "8*(-17*I_sc**2 + 3*sqrt(3)*I_sc*omega_sc - 17*Q_s**2 - 4*omega_sc**2)/(7*Q_s)"
    Qd_r3 = "2*(-31*sqrt(42)*I_sc - 31*sqrt(42)*Q_s + 15*sqrt(14)*omega_sc)/(21*sqrt(Q_s))"
    Qd_r4 = "-32"
    
    funcs = {
        'Qs': [sp.lambdify(syms, sp.sympify(eq, locals=locs), 'numpy') for eq in (Qs_r0, Qs_r1, Qs_r2)],
        'Isc': [sp.lambdify(syms, sp.sympify(eq, locals=locs), 'numpy') for eq in (Isc_r0, Isc_r1, Isc_r2)],
        'w': [sp.lambdify(syms, sp.sympify(eq, locals=locs), 'numpy') for eq in (w_r0, w_r1, w_r2)],
        'Qd': [sp.lambdify(syms, sp.sympify(eq, locals=locs), 'numpy') for eq in (Qd_r2, Qd_r3, Qd_r4)]
    }
    return funcs

def execute_t6f_v2():
    funcs = compile_vector_field()
    
    def rhs_4D(t, y):
        Qs, Isc, w, r = y
        Qs = max(float(Qs), 1e-12)
        r  = max(float(r), 1e-12)
        
        Qc = (Isc**2 + w**2) / Qs
        args = (Qs, Qc, Isc, w, r)
        
        dQs = funcs['Qs'][0](*args) + r*funcs['Qs'][1](*args) + (r**2)*funcs['Qs'][2](*args)
        dIsc = funcs['Isc'][0](*args) + r*funcs['Isc'][1](*args) + (r**2)*funcs['Isc'][2](*args)
        dw = funcs['w'][0](*args) + r*funcs['w'][1](*args) + (r**2)*funcs['w'][2](*args)
        dQd = (r**2)*funcs['Qd'][0](*args) + (r**3)*funcs['Qd'][1](*args) + (r**4)*funcs['Qd'][2](*args)
        
        return np.array([dQs, dIsc, dw, dQd / (2.0 * r)])

    # Event Guards
    def event_omega_runaway(t, y): return 1e3 - np.abs(y[2])
    event_omega_runaway.terminal = True
    event_omega_runaway.direction = -1

    def event_Qc_runaway(t, y):
        Qs_safe = max(y[0], 1e-12)
        Qc_implied = (y[1]**2 + y[2]**2) / Qs_safe
        return 1e6 - Qc_implied
    event_Qc_runaway.terminal = True
    event_Qc_runaway.direction = -1

    def event_r_collapse(t, y): return y[3] - 1e-6
    event_r_collapse.terminal = True
    event_r_collapse.direction = -1

    def event_Qs_collapse(t, y): return y[0] - 1e-6
    event_Qs_collapse.terminal = True
    event_Qs_collapse.direction = -1

    seeds = {
        "Class_Ia_Perturbative": [1.0, 0.0, np.sqrt(0.1), 0.1],
        "Class_III_Sensitive_1": [0.7, 1.0, np.sqrt(0.7*9.0 - 1.0**2), 0.3],
        "Class_III_Sensitive_2": [0.7, 1.5, np.sqrt(0.7*15.0 - 1.5**2), 0.5]
    }

    results = {}

    for name, init_4D in seeds.items():
        sol = solve_ivp(
            rhs_4D, (0.0, 200.0), init_4D, method='Radau', 
            events=[event_omega_runaway, event_Qc_runaway, event_r_collapse, event_Qs_collapse], 
            rtol=1e-8, atol=1e-10
        )
        
        final_Qs, final_Isc, final_w, final_r = sol.y[:, -1]
        final_implied_Qc = (final_Isc**2 + final_w**2) / max(final_Qs, 1e-12)
        max_abs_omega = np.max(np.abs(sol.y[2, :]))
        max_implied_Qc = np.max((sol.y[1, :]**2 + sol.y[2, :]**2) / np.maximum(sol.y[0, :], 1e-12))
        
        # Determine Classification
        terminal_class = "solver_stiff_abort"
        if sol.status == 1:
            if len(sol.t_events[0]) > 0 or len(sol.t_events[1]) > 0:
                terminal_class = "orientation_runaway"
            elif len(sol.t_events[2]) > 0 or len(sol.t_events[3]) > 0:
                terminal_class = "boundary_decay"
            else:
                terminal_class = "unknown_event"
        elif sol.status == 0:
            terminal_class = "active_state"

        results[name] = {
            "terminal_class": terminal_class,
            "t_final": float(sol.t[-1]),
            "solver_success": bool(sol.success),
            "solver_status": int(sol.status),
            "solver_message": str(sol.message),
            "diagnostics": {
                "final_Qs": float(final_Qs),
                "final_r": float(final_r),
                "final_implied_Qc": float(final_implied_Qc),
                "max_abs_omega": float(max_abs_omega),
                "max_implied_Qc": float(max_implied_Qc)
            }
        }

    manifest = {
        "software_environment": {
            "python_version": sys.version.split()[0],
            "script_git_hash": "rtg_t6f_v2_direct_orientation"
        },
        "physics_model": "Constrained 4D Direct Orientation with Runaway Guards",
        "trajectory_sweep": results,
        "verification_status": {
            "status": "NUM diagnostic / Event and Solver Diagnostics Patched"
        }
    }
    
    print(json.dumps(manifest, indent=2))

if __name__ == "__main__":
    execute_t6f_v2()