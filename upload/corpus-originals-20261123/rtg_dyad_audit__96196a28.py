#!/usr/bin/env python3
"""
rtg_dyad_audit.py  —  DSN v5.0 aligned

High-precision audit simulator for the isolated RTG dyadic map.

Map:
    rho' = rho - sin(eta)
    eta' = eta + (exp(rho) - 1) - sin(eta)

Changes in v5.0 — ISP layer (Invariant Structure Principle, DSN §3.x):

  [v5.0-ISP-CONST-1]  New exact ISP constants:
                       α_proj = Π₀ = π − arctan(√15)  (eigenvector locked phase)
                       Q_c = (arcsin(ln 2))²           (critical ISP amplitude)
                       τ² relation 3τ²=4 used in eigenvalue check.

  [v5.0-ISP-OBS-1]    New per-step ISP observables in Obs dataclass:
                       Theta   = arg(W) ∈ (−π,π]       (ISP invariant phase)
                       V_anticorr = Im(W·e^{−iπ/6})    (anti-correlation coordinate)
                       isp_sector  = sector label       (pre-cross/growth/decay/axis)
                       R_overshoot = R(Q,Θ) when in pre-crossing sector, else NaN

  [v5.0-ISP-TRACK-1]  ISP sector tracking: at each 6-step sample, (Q,Θ) pair
                       is stored. Pre-crossing entries (Θ ∈ [−2π/3,−π/3)) are
                       flagged separately for the footprint report.

  [v5.0-ISP-DIAG-1]   New diagnostic section: ISP STRUCTURAL REPORT
                       — Θ distribution histogram (last 50% of 6-step samples)
                       — Sector fractions (pre-cross / growth / decay)
                       — Pre-crossing footprint: list of (Q,Θ,R) events
                       — Overshoot ceiling check: max R vs sin(√Q)
                       — Q_c safety: flag any Q > Q_c at pre-crossing entries

  [v5.0-ISP-CSV-1]    CSV extended with ISP columns:
                       Theta, V_anticorr, isp_sector, R_overshoot

  [v5.0-ALIAS-1]      φ* extraction enhanced with alias-function correction:
                       — Reports naive leading-order correction φ*_true ≈ φ*_fit − τ ln(m_c)
                       — Reports Π₀ comparison: φ_W + α_proj vs φ*_fit
                       — Prints ISP section header linking to DSN §3.x.13

  [v5.0-ISP-FLAG-1]   New flag --isp-report to print ISP structural section.
                       Default: on when --joint-fit active, off otherwise.

  [v5.0-ISP-PRIM-1]   Strict primitive pre-crossing predicate and wedge checks
                       (patch from peer review of v5.0-ISP-DIAG-1):
                       — isp_is_primitive_precross(): ρ<0 ∧ sinη<0 ∧ ρ−sinη≥0
                       — isp_wedge_checks(): η_wrap < ρ < 0 (ISP v7 primitive wedge)
                       — isp_safety_checks(): THREE separate criteria never fused:
                           ceiling_ok (R≤sin√Q), qc_ok (Q<Q_c), rho_lt_ln2 (R<ln2)
                       — print_isp_report() now has two separate tables:
                           (A) ISP PRE-CROSS SECTOR ENTRIES (angle only)
                           (B) PRIMITIVE PRE-CROSSING ENTRIES (canonical condition)
                       — Branch detection Γ₃/Γ₄ from first_n mod 6
                       — CSV extended with is_primitive_precross, wedge_ok columns
                       — Annotation mismatch (4-tuple vs 5-tuple) fixed

Changes in v4.5.5 (F1/F2 override bug fix):

  [v4.5.5-F1SKIP-1] F1 log-period floor no longer fires on manual window overrides.
                     Previous: --phi-star-m-start 500000 --phi-star-m-end 1000000
                     was silently expanded to [4334, 1000000] by F1 because
                     ln(1M/500k) = 0.693 < 5.44 (one log-period).
                     Bug: the entire point of the override is to test a specific
                     window; silent modification defeats the experiment.
                     Fix: F1 and F2 floors are bypassed when window_was_overridden.
                     A warning is printed if the override window spans < 1 log-period.
                     The fallback (degenerate window) still applies for safety.

  [v4.5.5-WARN-1]   print_phi_star_extraction() explicitly notes when override
                     window is short (< 1 log-period), with action suggestion.

Changes in v4.5.4 (manual window override):
  [v4.5.4-WINOVER-1] --phi-star-m-start / --phi-star-m-end flags.

Changes in v4.5.3 (two-stage fit, above-approach scoping):
Changes in v4.5.2 (negative-κ fix, duplicate STATUS fix):
Changes in v4.5.1 (six fixes from Q₀=0.01 diagnostic run):
Changes in v4.5 (OPEN 5 closure campaign — joint fit):
Changes in v2.4.1/v2.4/v2.3/v2.2/v2.1: see prior version headers.
"""
from __future__ import annotations

import argparse
import ast
import cmath
import csv
import math
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

import mpmath as mp

# v4.5: numpy and scipy for joint fit
try:
    import numpy as np
    from scipy.optimize import curve_fit
    _SCIPY_AVAILABLE = True
except ImportError:
    _SCIPY_AVAILABLE = False


# =============================================================================
# Exact algebraic constants  [v2.4-CONST-1]
# DSN v2.4.1 §5.2 three-line α dictionary derived from c₂₁ = -½ - (2√3/3)i
# =============================================================================

def _exact_constants():
    """Return (TAU, ALPHA_BLOCK, ALPHA_STEP, R_STAR) at current mp.dps."""
    tau         = 2 * mp.sqrt(3) / 3          # -Im(c₂₁) = 2√3/3
    alpha_block = tau / (2 * mp.pi)            # √3/(3π)  per 6-step block
    alpha_step  = alpha_block / 6              # √3/(18π) per step (Birkhoff twist)
    r_star      = mp.exp(mp.pi / tau)          # exp(3π/(2√3)) ≈ 15.19094
    return tau, alpha_block, alpha_step, r_star


# =============================================================================
# ISP constants and geometric functions  [v5.0-ISP-CONST-1]
# DSN §3.x — Invariant Structure Principle
# =============================================================================

def _isp_constants():
    """
    Return exact ISP constants at current mp.dps.
    α_proj = Π₀ = π − arctan(√15)   [ALG structure — eigenvector of matrix A]
    Q_c    = (arcsin(ln 2))²         [ALG — critical ISP amplitude, DSN §3.x.11g]
    """
    alpha_proj = mp.pi - mp.atan(mp.sqrt(15))   # ≈ 1.8235 rad ≈ 104.48°
    q_c        = mp.power(mp.asin(mp.log(2)), 2) # ≈ 0.5865
    return alpha_proj, q_c


# =============================================================================
# Birth / Φ_{2→3} markers  [v6.0-BIRTH-1]
# CONTINUOUS-BRANCH ONLY. These are PASSIVE markers, not a birth simulation.
#
# Source / scope (import-refs, all continuous branch):
#   - One-dimensional Φ_{2→3} birth kinematics, Q_c = κ² Q_s³:
#       RTG_GENESIS_GEOMETRY_DSN §6.3  [THM/ALG] [scope: conditional on generator T; SG-11]
#       κ_shear  = -2√3/3  → Q_c = (4/3) Q_s³
#       κ_recoil = -1/2    → Q_c = (1/4) Q_s³
#     Physical κ is NOT selected by dyad conventions alone (Genesis §6.3 [COR]),
#     so BOTH policy amplitudes are logged as a band, never one value.
#   - Fracture/escape band amplitude (HEUR operational default, reduced Race-A NUM):
#       RTG_TRIADIC_BIRTH_LIFT_DSN T-4h: Q_{s,*}^escape ≈ 0.6594477844  [NUM diagnostic]
#       (below the torsion turn Q_s^turn ≈ 0.715, Triadic §6.12)
#   - Cascade-route verdict (static): the certified J_Q birth route is OBSTRUCTED
#       (wrong Plücker pole), RTG_TRIADIC_BIRTH_LIFT_DSN §6.12 [RESULT]. No certified
#       successful birth even above threshold; flips only if OPEN-M resolves.
#
# FIREWALL: the discrete TDR-G star blow-up birth is NOT representable here
#   (SG-PROG-1; no bridge theorem; OPEN-P1). Nothing below imports discrete content.
# =============================================================================

BIRTH_THRESHOLD_DEFAULT = "0.6594477844"   # [HEUR default] backed by TRIAD-T4h [NUM]
CASCADE_ROUTE          = "obstructed_certified_JQ"
CASCADE_ROUTE_TAG      = ("[RESULT][from: ALG+NUM diagnostic]"
                          "[scope: certified J_Q birth route only]")
EXTRAPOLATION_TAG      = ("[extrapolation: birth-regime; "
                          "isolated-dyad model out of certified scope]")


def birth_qc_shear(q_s: mp.mpf) -> mp.mpf:
    """Q_c under shear policy κ_shear = -2√3/3.  Genesis §6.3 [ALG structure]."""
    return (mp.mpf(4) / 3) * q_s**3


def birth_qc_recoil(q_s: mp.mpf) -> mp.mpf:
    """Q_c under recoil policy κ_recoil = -1/2.  Genesis §6.3 [ALG structure]."""
    return (mp.mpf(1) / 4) * q_s**3


def annotate_birth_and_escape(
    obs: "Obs",
    birth_threshold: mp.mpf,
    marker_mode: str,
    p2_escaped: bool,
) -> None:
    """
    Set passive continuous-branch birth markers + P2-escape flag on obs.
    Q_s is the dyadic fracture amplitude = Q_true (s* = current Birkhoff state).
    """
    q_s = obs.q_true
    obs.Q_s = q_s
    if marker_mode in ("shear", "both"):
        obs.Qc_birth_shear = birth_qc_shear(q_s)
    if marker_mode in ("recoil", "both"):
        obs.Qc_birth_recoil = birth_qc_recoil(q_s)
    obs.birth_regime_entered = bool(q_s >= birth_threshold)
    obs.extrapolation_tag = EXTRAPOLATION_TAG if obs.birth_regime_entered else ""
    obs.p2_escape_flag = p2_escaped


def isp_theta(u: mp.mpf, v: mp.mpf) -> mp.mpf:
    """ISP invariant phase Θ = arg(W) ∈ (−π, π]. DSN §3.x.3."""
    if u == 0 and v == 0:
        return mp.mpf("0")
    return mp.atan2(v, u)


def isp_sector(theta: mp.mpf) -> str:
    """
    Classify ISP phase Θ into structural sectors. DSN §3.x.11.
      pre-cross : Θ ∈ [−2π/3, −π/3)   pre-crossing sector near P₁
      growth    : Θ ∈ (−π, 0) minus pre-cross   sin Θ < 0 → Δρ > 0
      decay     : Θ ∈ (0, π)                sin Θ > 0 → Δρ < 0
      axis      : Θ ∈ {0, ±π}              on sector boundary
    """
    t = float(theta)
    two_thirds_pi = 2 * math.pi / 3
    one_third_pi  = math.pi / 3
    if abs(t) < 1e-14 or abs(abs(t) - math.pi) < 1e-14:
        return "axis"
    if -two_thirds_pi <= t < -one_third_pi:
        return "pre-cross"
    if -math.pi < t < 0:
        return "growth"
    if 0 < t < math.pi:
        return "decay"
    return "axis"


def isp_overshoot(q: mp.mpf, theta: mp.mpf) -> mp.mpf:
    """
    Exact crossing-step overshoot R(Q,Θ) = (2/√3)√Q cos(Θ−π/6) − sin((2/√3)√Q sin Θ).
    DSN §3.x.11e. Valid in pre-crossing sector Θ ∈ [−2π/3, −π/3].
    """
    sq  = mp.sqrt(q)
    s3  = mp.sqrt(3)
    arg_cos = (2 / s3) * sq * mp.cos(theta - mp.pi / 6)
    arg_sin = (2 / s3) * sq * mp.sin(theta)
    return arg_cos - mp.sin(arg_sin)


def isp_overshoot_ceiling(q: mp.mpf) -> mp.mpf:
    """Universal ceiling R ≤ sin(√Q). DSN §3.x.11e [ALG]."""
    return mp.sin(mp.sqrt(q))


def isp_is_primitive_precross(rho: mp.mpf, sin_eta: mp.mpf) -> bool:
    """
    Strict primitive pre-crossing predicate. DSN §3.x.11c [ALG].
    Conditions: ρ < 0  AND  sin η < 0  AND  ρ − sin η ≥ 0.
    This is the canonical definition used in the Certificate program.
    Distinct from ISP sector membership (Θ ∈ [−2π/3, −π/3)),
    which is a necessary but not sufficient condition at finite Q.
    """
    return (rho < 0) and (sin_eta < 0) and ((rho - sin_eta) >= 0)


def isp_wedge_checks(rho: mp.mpf, eta_wrap: mp.mpf) -> dict:
    """
    Primitive wedge checks for OPEN 11 / ISP task 1. DSN §3.x.11c.
    ISP v7 reduces sector containment to: η_wrap < ρ < 0.
    Returns dict of boolean diagnostics.
    """
    rho_neg        = bool(rho < 0)
    wedge_eta_lt_rho = bool(eta_wrap < rho)
    wedge_ok       = rho_neg and wedge_eta_lt_rho
    return {
        "rho_neg":         rho_neg,
        "wedge_eta_lt_rho": wedge_eta_lt_rho,
        "wedge_ok":        wedge_ok,          # η_wrap < ρ < 0
    }


def isp_safety_checks(q: mp.mpf, R: mp.mpf) -> dict:
    """
    Three logically distinct safety criteria for pre-crossing states.
    DSN §3.x.11e,g. These must NOT be fused into a single boolean.

    ceiling_ok  : R ≤ sin(√Q)    — universal overshoot ceiling [ALG]
    qc_ok       : Q < Q_c        — sufficient for one-step critical-curve safety
    rho_lt_ln2  : R < ln 2       — direct critical-curve threshold check
    """
    _, q_c = _isp_constants()
    ceiling = isp_overshoot_ceiling(q)
    return {
        "ceiling_ok":  bool(R <= ceiling),
        "qc_ok":       bool(q < q_c),
        "rho_lt_ln2":  bool(R < mp.log(2)),
        "R_ceiling":   float(ceiling),
    }


def isp_V_anticorr(u: mp.mpf, v: mp.mpf) -> mp.mpf:
    """
    Anti-correlation coordinate V = Im(W·e^{−iπ/6}).
    V = (√3·v − u) / 2 = η_wrap − ρ/2.
    DSN §3.x.5 [ALG].
    Sign of V determines winding-kick direction (§3.x.9c).
    """
    return (mp.sqrt(3) * v - u) / 2


def alias_G_minus(U: float, tau: float) -> complex:
    """
    Exact alias function G₋(U) = 2sinh((−2+2iτ)U) / ((−2+2iτ)sinh(2U)).
    DSN §3.x.13a [ALG ✓].
    U = (1/2)ln(m₂/m₁) is the window half-width in ln-space.
    """
    if U < 1e-10:
        return complex(1, 0)
    c = complex(-2, 2 * tau)
    num = 2 * (cmath_sinh(c * U))
    den = c * cmath_sinh(complex(2 * U, 0))
    if abs(den) < 1e-300:
        return complex(1, 0)
    return num / den


def cmath_sinh(z: complex) -> complex:
    """Complex sinh."""
    import cmath
    return cmath.sinh(z)


def alias_phase_correction(phi_fit_rad: float, m_c: float, U: float, tau: float) -> dict:
    """
    Compute alias-function phase corrections for a short-window φ* fit.
    Returns dict with leading-order and exact (implicit) corrections.
    DSN §3.x.13a [ALG ✓].

    Leading-order (U→0 limit):
      φ*_true ≈ φ*_fit − τ·ln(m_c)   [mod 2π]

    Note: 10% excess over τ in observed rate is attributed to pre-asymptotic
    secondary m^{−5/2} mode contamination [OBS + HEUR], not a formula error.
    """
    import cmath
    two_pi = 2 * math.pi
    ln_mc  = math.log(m_c) if m_c > 0 else 0.0

    # Leading-order naive correction
    phi_true_naive = (phi_fit_rad - tau * ln_mc) % two_pi

    # Alias ratio for display
    G  = alias_G_minus(U, tau)
    mc_phase = cmath.exp(2j * tau * ln_mc)
    alias_ratio = mc_phase * G
    alias_arg   = cmath.phase(1 + alias_ratio * cmath.exp(2j * phi_fit_rad))

    return {
        "phi_true_naive_rad": phi_true_naive,
        "phi_true_naive_deg": math.degrees(phi_true_naive),
        "tau_ln_mc":          tau * ln_mc,
        "alias_G_abs":        abs(G),
        "alias_correction_rad": alias_arg,
        "U":                  U,
        "m_c":                m_c,
    }

# =============================================================================
# Safe symbolic parser
# =============================================================================

_ALLOWED_NAMES = {
    "pi":  lambda: mp.pi,
    "e":   lambda: mp.e,
    "phi": lambda: (1 + mp.sqrt(5)) / 2,
}

_ALLOWED_FUNCS = {
    "sqrt": mp.sqrt, "sin": mp.sin, "cos": mp.cos, "tan": mp.tan,
    "asin": mp.asin, "acos": mp.acos, "atan": mp.atan,
    "exp":  mp.exp,  "log": mp.log,
}


def parse_expr(expr: str) -> mp.mpf:
    tree = ast.parse(expr, mode="eval")

    def _eval(node):
        if isinstance(node, ast.Expression):      return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)): return mp.mpf(str(node.value))
            raise ValueError(f"Unsupported constant: {node.value!r}")
        if isinstance(node, ast.Name):
            if node.id in _ALLOWED_NAMES:            return _ALLOWED_NAMES[node.id]()
            raise ValueError(f"Unknown symbol: {node.id}")
        if isinstance(node, ast.BinOp):
            l, r = _eval(node.left), _eval(node.right)
            ops = {ast.Add: lambda a,b: a+b, ast.Sub: lambda a,b: a-b,
                   ast.Mult: lambda a,b: a*b, ast.Div: lambda a,b: a/b,
                   ast.Pow: lambda a,b: a**b}
            fn = ops.get(type(node.op))
            if fn is None: raise ValueError(f"Unsupported op: {type(node.op).__name__}")
            return fn(l, r)
        if isinstance(node, ast.UnaryOp):
            val = _eval(node.operand)
            if isinstance(node.op, ast.UAdd): return val
            if isinstance(node.op, ast.USub): return -val
            raise ValueError(f"Unsupported unary op: {type(node.op).__name__}")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name): raise ValueError("Only simple calls")
            nm = node.func.id
            if nm not in _ALLOWED_FUNCS: raise ValueError(f"Function not allowed: {nm}")
            if node.keywords: raise ValueError("Keyword arguments not allowed")
            return _ALLOWED_FUNCS[nm](*[_eval(a) for a in node.args])
        raise ValueError(f"Unsupported node: {type(node).__name__}")

    return _eval(tree)


# =============================================================================
# Utilities
# =============================================================================

def wrap_pm_pi(x: mp.mpf) -> mp.mpf:
    two_pi = 2 * mp.pi
    y = mp.fmod(x + mp.pi, two_pi)
    if y < 0:    y += two_pi
    y -= mp.pi
    if y <= -mp.pi: y += two_pi
    return y


def mpstr(x: mp.mpf, n: int = 16) -> str:
    return mp.nstr(x, n)


def euclid_dist(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    return mp.sqrt(a*a + b*b)


# =============================================================================
# Regression utilities  [v2.2-FIT-1]
# =============================================================================

def linear_regression(
    xs: List[mp.mpf],
    ys: List[mp.mpf],
) -> Tuple[mp.mpf, mp.mpf, mp.mpf]:
    n = len(xs)
    if n < 2:
        nan = mp.mpf("nan")
        return nan, nan, nan
    x_mean = sum(xs) / n
    y_mean = sum(ys) / n
    sxx = sum((x - x_mean)**2 for x in xs)
    sxy = sum((xs[i] - x_mean)*(ys[i] - y_mean) for i in range(n))
    syy = sum((y - y_mean)**2 for y in ys)
    if sxx == 0:
        nan = mp.mpf("nan")
        return nan, nan, nan
    slope     = sxy / sxx
    intercept = y_mean - slope * x_mean
    if syy == 0:
        r2 = mp.mpf("1")
    else:
        ss_res = sum((ys[i] - (slope*xs[i] + intercept))**2 for i in range(n))
        r2 = 1 - ss_res / syy
    return slope, intercept, r2


# =============================================================================
# P2 eigenvector utilities  [v2.1-NEW-1]
# =============================================================================

def p2_eigenvectors() -> Tuple[Tuple[mp.mpf, mp.mpf], Tuple[mp.mpf, mp.mpf]]:
    phi      = (1 + mp.sqrt(5)) / 2
    lam_plus = (3 + mp.sqrt(5)) / 2
    u_rho, u_eta = mp.mpf("1"), lam_plus - 1
    norm_u   = mp.sqrt(u_rho**2 + u_eta**2)
    v_u      = (u_rho/norm_u, u_eta/norm_u)
    lam_minus = (3 - mp.sqrt(5)) / 2
    s_rho, s_eta = mp.mpf("1"), lam_minus - 1
    norm_s   = mp.sqrt(s_rho**2 + s_eta**2)
    v_s      = (s_rho/norm_s, s_eta/norm_s)
    return v_u, v_s


def p2_escape_theory(eps: mp.mpf) -> mp.mpf:
    lam_plus = (3 + mp.sqrt(5)) / 2
    if eps <= 0: return mp.inf
    return mp.log(1/eps) / mp.log(lam_plus)


# =============================================================================
# Map state and observables
# =============================================================================

@dataclass
class State:
    rho: mp.mpf
    eta: mp.mpf


@dataclass
class Obs:
    step: int
    rho: mp.mpf
    eta_lift: mp.mpf
    eta_wrap: mp.mpf
    sin_eta: mp.mpf
    cos_eta: mp.mpf
    drift: mp.mpf
    remainder: mp.mpf
    u: mp.mpf
    v: mp.mpf
    q_true: mp.mpf
    q_euclid: mp.mpf
    tr_j: mp.mpf
    det_j: mp.mpf
    discr: mp.mpf
    eig_kind: str
    dist_p1: mp.mpf
    dist_p2: mp.mpf
    rotation_increment: mp.mpf
    winding_accum: mp.mpf
    n_times_q_true: mp.mpf
    q6_true: Optional[mp.mpf]
    n_times_q6_true: Optional[mp.mpf]
    # === ISP observables [v5.0-ISP-OBS-1] ===
    Theta: mp.mpf = mp.mpf("0")           # ISP invariant phase arg(W)
    V_anticorr: mp.mpf = mp.mpf("0")      # anti-correlation V = Im(W·e^{−iπ/6})
    isp_sector: str = "?"                  # pre-cross / growth / decay / axis
    R_overshoot: Optional[mp.mpf] = None  # R(Q,Θ) if in pre-cross sector, else None
    # === ISP primitive pre-crossing [v5.0-ISP-PRIM-1] ===
    is_primitive_precross: bool = False    # strict ρ<0, sinη<0, ρ−sinη≥0 condition
    wedge_ok: bool = False                 # η_wrap < ρ < 0  (ISP v7 primitive wedge)
    # === Birth / Φ_{2→3} passive markers [v6.0-BIRTH-1] (continuous branch) ===
    Q_s: mp.mpf = mp.mpf("0")              # dyadic fracture amplitude = Q_true
    Qc_birth_shear: mp.mpf = mp.mpf("0")   # (4/3)Q_s³  candidate birth amplitude
    Qc_birth_recoil: mp.mpf = mp.mpf("0")  # (1/4)Q_s³  candidate birth amplitude
    birth_regime_entered: bool = False     # Q_s ≥ birth_threshold (HEUR horizon)
    extrapolation_tag: str = ""            # set above threshold; empty below
    p2_escape_flag: bool = False           # running P2 separatrix-escape flag


@dataclass
class Flags:
    near_p1: bool = False
    near_p2: bool = False
    escaped_p2_band: bool = False
    near_critical_curve: bool = False
    large_positive_rho: bool = False
    large_negative_rho: bool = False
    huge_drift: bool = False
    q_jump: bool = False
    q6_jump: bool = False

    def alert(self) -> bool:
        return any([self.near_critical_curve, self.large_positive_rho,
                    self.large_negative_rho, self.huge_drift,
                    self.q_jump, self.q6_jump])

    def any_set(self) -> bool:
        return any(vars(self).values())


def dyad_step(st: State) -> State:
    s = mp.sin(st.eta)
    return State(st.rho - s, st.eta + (mp.exp(st.rho) - 1) - s)


def birkhoff_coords(rho: mp.mpf, eta_wrap: mp.mpf) -> Tuple[mp.mpf, mp.mpf, mp.mpf]:
    u = rho - eta_wrap / 2
    v = (mp.sqrt(3) / 2) * eta_wrap
    return u, v, u*u + v*v


def euclid_q(rho: mp.mpf, eta_wrap: mp.mpf) -> mp.mpf:
    return rho*rho + eta_wrap*eta_wrap


def jacobian_trace_det_discr(rho: mp.mpf, eta: mp.mpf) -> Tuple[mp.mpf, mp.mpf, mp.mpf]:
    c  = mp.cos(eta)
    er = mp.exp(rho)
    tr   = 2 - c
    det  = 1 + (er - 1) * c
    return tr, det, tr*tr - 4*det


def classify_eigs(discr: mp.mpf, tol: mp.mpf) -> str:
    if discr > tol:  return "real"
    if discr < -tol: return "complex"
    return "degenerate"


def compute_obs(
    step: int, st: State,
    prev_uv_angle: Optional[mp.mpf],
    winding_accum: mp.mpf,
    discr_tol: mp.mpf,
    q6_current: Optional[mp.mpf],
) -> Tuple[Obs, mp.mpf, mp.mpf]:
    eta_wrap = wrap_pm_pi(st.eta)
    s, c     = mp.sin(st.eta), mp.cos(st.eta)
    drift    = mp.exp(st.rho) - 1
    u, v, q_true = birkhoff_coords(st.rho, eta_wrap)
    q_euclid     = euclid_q(st.rho, eta_wrap)
    tr, det_j, discr = jacobian_trace_det_discr(st.rho, st.eta)
    eig_kind = classify_eigs(discr, discr_tol)
    dist_p1 = euclid_dist(st.rho, eta_wrap)
    dist_p2 = euclid_dist(st.rho, wrap_pm_pi(eta_wrap - mp.pi))
    uv_angle = mp.mpf("0") if (u == 0 and v == 0) else mp.atan2(v, u)
    rot_inc  = mp.mpf("0") if prev_uv_angle is None else wrap_pm_pi(uv_angle - prev_uv_angle)
    wind_next = winding_accum + rot_inc / (2 * mp.pi)
    nq = mp.mpf(step) * q_true if step > 0 else mp.mpf("0")
    nq6 = (mp.mpf(step) * q6_current
           if (q6_current is not None and step > 0 and step % 6 == 0) else None)
    obs = Obs(
        step=step, rho=st.rho, eta_lift=st.eta, eta_wrap=eta_wrap,
        sin_eta=s, cos_eta=c, drift=drift, remainder=drift - st.rho,
        u=u, v=v, q_true=q_true, q_euclid=q_euclid,
        tr_j=tr, det_j=det_j, discr=discr, eig_kind=eig_kind,
        dist_p1=dist_p1, dist_p2=dist_p2,
        rotation_increment=rot_inc, winding_accum=wind_next,
        n_times_q_true=nq,
        q6_true=q6_current if (step % 6 == 0 and step > 0) else None,
        n_times_q6_true=nq6,
    )
    # --- ISP observables [v5.0-ISP-OBS-1] ---
    obs.Theta      = isp_theta(u, v)
    obs.V_anticorr = isp_V_anticorr(u, v)
    obs.isp_sector = isp_sector(obs.Theta)
    if obs.isp_sector == "pre-cross" and q_true > 0:
        obs.R_overshoot = isp_overshoot(q_true, obs.Theta)
    # --- Primitive pre-crossing and wedge checks [v5.0-ISP-PRIM-1] ---
    obs.is_primitive_precross = isp_is_primitive_precross(st.rho, s)
    wc = isp_wedge_checks(st.rho, eta_wrap)
    obs.wedge_ok = wc["wedge_ok"]
    return obs, uv_angle, wind_next


# =============================================================================
# Diagnostics
# =============================================================================

def detect_flags(
    obs: Obs, prev_q: Optional[mp.mpf], prev_q6: Optional[mp.mpf],
    near_fp_tol: mp.mpf, crit_tol: mp.mpf, rho_warn: mp.mpf,
    drift_warn: mp.mpf, q_growth_warn: mp.mpf, q6_growth_warn: mp.mpf,
    p2_escape_radius: mp.mpf, was_near_p2: bool,
) -> Flags:
    flags = Flags()
    flags.near_p1             = obs.dist_p1 < near_fp_tol
    flags.near_p2             = obs.dist_p2 < near_fp_tol
    flags.near_critical_curve = abs(obs.det_j) < crit_tol
    flags.large_positive_rho  = obs.rho > rho_warn
    flags.large_negative_rho  = obs.rho < -rho_warn
    flags.huge_drift          = abs(obs.drift) > drift_warn
    flags.escaped_p2_band     = was_near_p2 and obs.dist_p2 > p2_escape_radius
    if prev_q is not None and prev_q != 0:
        if obs.q_true / prev_q > q_growth_warn: flags.q_jump = True
    if prev_q6 is not None and obs.q6_true is not None and prev_q6 != 0:
        if obs.q6_true / prev_q6 > q6_growth_warn: flags.q6_jump = True
    return flags


def format_flags(flags: Flags) -> str:
    xs = []
    if flags.near_p1:             xs.append("near_P1")
    if flags.near_p2:             xs.append("near_P2")
    if flags.escaped_p2_band:     xs.append("escaped_P2")
    if flags.near_critical_curve: xs.append("near_crit")
    if flags.large_positive_rho:  xs.append("rho>>0")
    if flags.large_negative_rho:  xs.append("rho<<0")
    if flags.huge_drift:          xs.append("huge_drift")
    if flags.q_jump:              xs.append("Q_jump")
    if flags.q6_jump:             xs.append("Q6_jump")
    return ",".join(xs) if xs else "-"


# =============================================================================
# Asymptotic-C tracker  [v2.1-NEW-3]
# =============================================================================

def asymptotic_c_stats(
    q6_samples: List[Tuple[int, mp.mpf]],
    window: int,
) -> Optional[Tuple[mp.mpf, mp.mpf, mp.mpf, int]]:
    tail = q6_samples[-window:] if len(q6_samples) >= window else q6_samples
    if len(tail) < 2: return None
    vals  = [mp.mpf(n) * q for n, q in tail]
    count = len(vals)
    mean  = sum(vals) / count
    var   = sum((v - mean)**2 for v in vals) / (count - 1)
    std   = mp.sqrt(var)
    xs    = [mp.mpf(i) for i in range(count)]
    xm    = sum(xs) / count
    num   = sum((xs[i]-xm)*(vals[i]-mean) for i in range(count))
    den   = sum((x-xm)**2 for x in xs)
    slope = num/den if den != 0 else mp.mpf("0")
    return mean, std, slope, count


# =============================================================================
# MODEL-DISCRIMINATION DIAGNOSTICS  [v2.2]
# =============================================================================

def asymptotic_fit_report(
    q6_samples: List[Tuple[int, mp.mpf]],
    winding_at_q6: List[mp.mpf],
    fracs: Tuple[float, ...] = (0.1, 0.2, 0.4, 0.8),
) -> Dict:
    """
    [v2.2-FIT-2] Three fit tests on multiple trailing windows.

    Fit-A:  1/Q_n  vs  n          →  slope ≈ 1/6,  C_est = 6·intercept/slope
    Fit-B:  (nQ-6) vs  1/n        →  slope = A in nQ = 6 + A/n + …
    C-drift: C_est stability across windows
    """
    results = {}
    for frac in fracs:
        start = int((1 - frac) * len(q6_samples))
        tail  = q6_samples[start:]
        if len(tail) < 4:
            results[frac] = None
            continue
        ns   = [mp.mpf(n) for n, q in tail if q > 0]
        qs   = [q          for n, q in tail if q > 0]
        if len(ns) < 4:
            results[frac] = None
            continue

        invQ  = [1/q for q in qs]
        invn  = [1/n for n in ns]
        dev6  = [ns[i]*qs[i] - 6 for i in range(len(ns))]

        sl_A, ic_A, r2_A = linear_regression(ns,   invQ)
        sl_B, ic_B, r2_B = linear_regression(invn, dev6)

        C_est = mp.mpf("6") * ic_A / sl_A if sl_A and sl_A != 0 else mp.mpf("nan")

        results[frac] = {
            "count":  len(ns),
            "fit_A":  {"slope": sl_A, "intercept": ic_A, "R2": r2_A, "C_est": C_est},
            "fit_B":  {"slope": sl_B, "intercept": ic_B, "R2": r2_B},
        }
    return results


def spiral_phase_report(
    q6_samples: List[Tuple[int, mp.mpf]],
    winding_at_q6: List[mp.mpf],
    frac: float = 0.5,
) -> Optional[Dict]:
    """
    [v2.4-BASIS-1] Spiral-phase projection — UPGRADED BASIS.
    Basis: cos(τ·ln n)/√n  and  sin(τ·ln n)/√n  [O(n^{-1/2}) envelope]
    τ = 2√3/3 = -Im(c₂₁).
    """
    if len(q6_samples) < 10 or len(winding_at_q6) < 10:
        return None

    start  = int((1 - frac) * len(q6_samples))
    tail_q = q6_samples[start:]
    if len(tail_q) < 4:
        return None

    ns = [mp.mpf(n) for n, q in tail_q if q > 0]
    qs = [q          for n, q in tail_q if q > 0]
    if len(ns) < 4:
        return None

    invQ = [1/q for q in qs]
    sl, ic, r2 = linear_regression(ns, invQ)
    C_fit = mp.mpf("6") * ic / sl if sl != 0 else mp.mpf("0")

    nq_hyp = [ns[i] * mp.mpf("6") / (ns[i] + C_fit) for i in range(len(ns))]
    nq_obs = [ns[i] * qs[i] for i in range(len(ns))]
    r_n    = [nq_obs[i] - nq_hyp[i] for i in range(len(ns))]

    tau = 2 * mp.sqrt(3) / 3
    cos_basis = [mp.cos(tau * mp.log(n)) / mp.sqrt(n) for n in ns]
    sin_basis = [mp.sin(tau * mp.log(n)) / mp.sqrt(n) for n in ns]

    def project(basis, signal):
        b2 = sum(b*b for b in basis)
        if b2 == 0:
            return mp.mpf("0"), mp.mpf("0")
        coef     = sum(basis[i]*signal[i] for i in range(len(basis))) / b2
        resid_var = sum((signal[i] - coef*basis[i])**2 for i in range(len(basis))) / len(basis)
        return coef, mp.sqrt(resid_var)

    A_cos, res_cos = project(cos_basis, r_n)
    A_sin, res_sin = project(sin_basis, r_n)
    r_var = sum(x*x for x in r_n) / len(r_n)
    r_rms = mp.sqrt(r_var)

    return {
        "C_fit":         C_fit,
        "r2_hyperbolic": r2,
        "A_cos":         A_cos,
        "A_sin":         A_sin,
        "residual_rms":  r_rms,
        "res_after_cos": res_cos,
        "res_after_sin": res_sin,
        "frac":          frac,
        "n_samples":     len(ns),
        "basis":         "cos(tau*ln(n))/sqrt(n)  [v2.4]",
    }


def transient_analysis(
    q6_samples: List[Tuple[int, mp.mpf]],
    q0: mp.mpf,
    q_onset_thr: mp.mpf = mp.mpf("2.0"),
) -> Dict:
    """
    [v2.4-ONSET-1] Detect and characterise the violent initial burst.
    [v2.4.1-APPDIR-1] Approach direction uses nq6[0], not nq6_peak.
    """
    if not q6_samples:
        return {"initial_regime": "unknown", "q0": float(q0),
                "approach_dir": "unknown",
                "n_onset_idx": 0, "n_onset_step": 0, "n_transient": 0,
                "onset_method": "none"}

    ns  = [mp.mpf(n) for n, q in q6_samples]
    qs  = [q for n, q in q6_samples]
    nq6 = [ns[i] * qs[i] for i in range(len(ns))]

    regime = "large" if q0 >= mp.mpf("1") else "small"

    early_end = max(1, len(nq6) // 5)
    peak_idx  = max(range(early_end), key=lambda i: nq6[i])
    nq6_peak  = nq6[peak_idx]

    # [v2.4.1-APPDIR-1] Use first sample, not peak
    approach_dir = "above" if float(nq6[0]) > 6.0 else "below"

    threshold    = 2 * q0 + mp.mpf("6")
    step_onset   = 0
    if regime == "large":
        last_above = -1
        for i in range(len(nq6)):
            if nq6[i] > threshold:
                last_above = i
        step_onset = last_above + 1

    q_onset = 0
    if regime == "large":
        for i in range(len(qs)):
            if qs[i] < q_onset_thr:
                q_onset = i
                break
        else:
            q_onset = len(qs)

    peak_onset = peak_idx + 1 if approach_dir == "above" else 0

    onset_idx = max(step_onset, q_onset, peak_onset)
    methods = []
    if step_onset >= q_onset and step_onset >= peak_onset and step_onset > 0:
        methods.append("step-based")
    if q_onset >= step_onset and q_onset >= peak_onset and q_onset > 0:
        methods.append("Q-based")
    if peak_onset >= step_onset and peak_onset >= q_onset and peak_onset > 0:
        methods.append("peak-based")
    onset_method = "+".join(methods) if methods else "none"

    onset_step = int(ns[onset_idx]) if onset_idx < len(ns) else (
        int(ns[-1]) + 6 if ns else 0)

    return {
        "initial_regime": regime,
        "approach_dir":   approach_dir,
        "q0":             float(q0),
        "n_peak_idx":     peak_idx,
        "n_peak_step":    int(ns[peak_idx]),
        "nq6_peak":       float(nq6_peak),
        "n_onset_idx":    onset_idx,
        "n_onset_step":   onset_step,
        "n_transient":    onset_idx,
        "onset_method":   onset_method,
    }


def winding_debt_report(
    q6_samples: List[Tuple[int, mp.mpf]],
    winding_final: mp.mpf,
    n_final: int,
) -> Dict:
    """[v2.3-WND-1] Cumulative winding deficit relative to exact resonance."""
    six = mp.mpf("6")
    expected = mp.mpf(n_final) / six
    debt     = expected - winding_final
    k_implied = int(mp.nint(debt))

    return {
        "n_final":          n_final,
        "winding_expected": float(expected),
        "winding_actual":   float(winding_final),
        "debt_rotations":   float(debt),
        "debt_fraction":    float(debt % 1),
        "k_implied":        k_implied,
    }


def phase_deficit_report(
    q6_samples: List[Tuple[int, mp.mpf]],
    winding_at_q6: List[mp.mpf],
    n_onset_idx: int = 0,
    prior_alpha: Optional[mp.mpf] = None,
) -> Optional[Dict]:
    """[v2.3-PD-1] Angular deficit from exact order-6 resonance."""
    if len(q6_samples) < 4 or len(winding_at_q6) < 4:
        return None

    n_arr = [mp.mpf(n) for n, q in q6_samples]
    q_arr = [q          for n, q in q6_samples]

    gaps  = [n_arr[i+1] - n_arr[i] for i in range(len(n_arr)-1)]
    dwind = [winding_at_q6[i+1] - winding_at_q6[i] for i in range(len(winding_at_q6)-1)]
    six   = mp.mpf("6")
    deficit = [dwind[i] - gaps[i]/six for i in range(len(gaps))]
    q_mid   = [(q_arr[i]+q_arr[i+1])/2 for i in range(len(gaps))]

    n_total = len(deficit)
    lo = max(n_onset_idx, max(2, n_total // 10))
    hi = min(n_total - 1, int(n_total * 0.85))
    alphas = []
    for i in range(lo, hi):
        if q_mid[i] > mp.mpf("1e-20"):
            alphas.append(-deficit[i] / q_mid[i])

    if not alphas:
        for i in range(max(2, n_total//10), min(n_total-1, int(n_total*0.85))):
            if q_mid[i] > mp.mpf("1e-20"):
                alphas.append(-deficit[i] / q_mid[i])
    if not alphas:
        return None

    alpha_sorted = sorted(alphas)
    alpha_med    = alpha_sorted[len(alphas) // 2]
    alpha_mean   = sum(alphas) / len(alphas)
    alpha_std    = mp.sqrt(sum((a - alpha_mean)**2 for a in alphas) / len(alphas))

    gap_sizes = [int(g) for g in gaps[lo:hi] if g > 0]
    gap_med   = sorted(gap_sizes)[len(gap_sizes)//2] if gap_sizes else 6
    alpha_NF  = alpha_mean / mp.mpf(gap_med)

    pred = {}
    for k in range(1, 4):
        if alpha_mean != 0:
            pred[k] = mp.exp(mp.mpf(k) / (six * alpha_mean))
        else:
            pred[k] = mp.mpf("nan")

    universality = None
    if prior_alpha is not None and prior_alpha > 0 and alpha_mean > 0:
        rel_diff = abs(alpha_mean - prior_alpha) / prior_alpha
        universality = {"prior_alpha": prior_alpha, "rel_diff": rel_diff}

    phi_sq     = ((1 + mp.sqrt(5)) / 2) ** 2
    six_phi_sq = six * phi_sq
    tau, alpha_block_exact, alpha_step_exact, r_star_exact = _exact_constants()

    alpha_theory_dev = abs(alpha_mean - alpha_block_exact) / alpha_block_exact

    return {
        "n_samples":            len(deficit),
        "n_onset_idx":          n_onset_idx,
        "lo_idx":               lo,
        "alpha_mean":           alpha_mean,
        "alpha_median":         alpha_med,
        "alpha_std":            alpha_std,
        "alpha_NF":             alpha_NF,
        "alpha_block_exact":    alpha_block_exact,
        "alpha_step_exact":     alpha_step_exact,
        "alpha_theory_dev":     alpha_theory_dev,
        "gap_median":           gap_med,
        "crossing_ratio_k1":    pred[1],
        "crossing_ratio_k2":    pred[2],
        "crossing_ratio_k3":    pred[3],
        "R_star_exact":         r_star_exact,
        "6phi2_reference":      six_phi_sq,
        "universality":         universality,
        "deficit_sample":   [(int(n_arr[i]), float(deficit[i]), float(q_mid[i]))
                             for i in range(min(10, len(deficit)))],
    }


def zero_crossing_report(
    q6_samples: List[Tuple[int, mp.mpf]],
    n_onset_step: int = 0,
    approach_dir: str = "unknown",
) -> Dict:
    """
    [v2.4-KIN-1] Zero-crossings of nQ6-6 with kinematic/spiral classification.
    R* = exp(π/τ) = exp(3π/(2√3)) ≈ 15.19094  [exact, v2.4-CONST-1]
    """
    ns  = [mp.mpf(n) for n, q in q6_samples]
    nq6 = [ns[i] * q6_samples[i][1] for i in range(len(ns))]
    dev = [v - 6 for v in nq6]

    if approach_dir == "unknown" and len(nq6) > 0:
        approach_dir = "above" if nq6[0] > mp.mpf("6") else "below"

    all_crossings = []
    for i in range(len(dev) - 1):
        if dev[i] * dev[i+1] < 0:
            t = ns[i] - dev[i] * (ns[i+1]-ns[i]) / (dev[i+1]-dev[i])
            if float(t) < n_onset_step:
                kind = "TRANSIENT"
            else:
                kind = "ASYMPTOTIC"
            all_crossings.append((t, kind))

    labeled = []
    asym_count = 0
    for t, kind in all_crossings:
        if kind == "TRANSIENT":
            labeled.append((t, "TRANSIENT"))
        else:
            asym_count += 1
            if asym_count == 1 and approach_dir == "below":
                labeled.append((t, "KINEMATIC"))
            else:
                labeled.append((t, "SPIRAL"))

    transient_c  = [t for t, k in labeled if k == "TRANSIENT"]
    kinematic_c  = [t for t, k in labeled if k == "KINEMATIC"]
    spiral_c     = [t for t, k in labeled if k == "SPIRAL"]

    def geometry(crossings):
        if len(crossings) < 2:
            return [], []
        ratios    = [crossings[i+1]/crossings[i] for i in range(len(crossings)-1)]
        log10_c   = [mp.log10(c) for c in crossings]
        spacings  = [log10_c[i+1]-log10_c[i] for i in range(len(log10_c)-1)]
        return ratios, spacings

    spiral_ratios, spiral_log10 = geometry(spiral_c)

    tau          = 2 * mp.sqrt(3) / 3
    r_star       = mp.exp(mp.pi / tau)
    phi_sq       = ((1 + mp.sqrt(5)) / 2) ** 2
    six_phi_sq   = mp.mpf("6") * phi_sq

    return {
        "n_onset_step":        n_onset_step,
        "approach_dir":        approach_dir,
        "all_crossings":       labeled,
        "n_crossings_total":   len(labeled),
        "n_transient":         len(transient_c),
        "n_kinematic":         len(kinematic_c),
        "n_spiral":            len(spiral_c),
        "transient_steps":     transient_c,
        "kinematic_steps":     kinematic_c,
        "spiral_steps":        spiral_c,
        "spiral_ratios":       spiral_ratios,
        "spiral_log10":        spiral_log10,
        "R_star":              r_star,
        "6phi2":               six_phi_sq,
        "spiral_ratio_vs_Rstar":  [r/r_star     for r in spiral_ratios],
        "spiral_ratio_vs_6phi2":  [r/six_phi_sq for r in spiral_ratios],
    }


# =============================================================================
# CSV  [v2.2-CSV-1: extended fields]
# =============================================================================

CSV_FIELDS = [
    "step", "rho", "eta_lift", "eta_wrap", "sin_eta", "cos_eta",
    "drift", "remainder", "u", "v",
    "Q_true", "Q_euclid",
    "invQ_true",
    "nQ_true", "Q6_true", "nQ6_true",
    "dev6",
    "invn",
    "trJ", "detJ", "discr", "eig_kind",
    "dist_P1", "dist_P2",
    "rotation_increment", "winding_accum",
    "phase_mod1",
    "cos_phase",
    "sin_phase",
    # === ISP columns [v5.0-ISP-CSV-1] ===
    "Theta",                 # ISP invariant phase arg(W)
    "V_anticorr",            # anti-correlation coordinate V = Im(W·e^{-iπ/6})
    "isp_sector",            # pre-cross / growth / decay / axis (angle-sector only)
    "R_overshoot",           # R(Q,Θ) when in ISP pre-cross sector
    "is_primitive_precross", # strict ρ<0 ∧ sinη<0 ∧ ρ−sinη≥0 (canonical condition)
    "wedge_ok",              # η_wrap < ρ < 0 (ISP v7 primitive wedge)
    # === Birth / Φ_{2→3} passive markers [v6.0-BIRTH-1] (per-step) ===
    "Q_s",                   # dyadic fracture amplitude = Q_true
    "Qc_birth_shear",        # (4/3)Q_s³  [Genesis §6.3, scope: conditional on T; SG-11]
    "Qc_birth_recoil",       # (1/4)Q_s³  [Genesis §6.3, scope: conditional on T; SG-11]
    "birth_threshold",       # active HEUR threshold (run constant)
    "birth_regime_entered",  # Q_s ≥ threshold
    "birth_action",          # off / warn / stop (run constant)
    "birth_threshold_source",# provenance string (run constant)
    "cascade_route",         # "obstructed_certified_JQ" (run constant)
    "cascade_route_tag",     # certified-scope tag (run constant)
    "extrapolation_tag",     # set above threshold, empty below
    "p2_escape_flag",        # running P2 separatrix-escape flag
]


def write_csv_row(writer: csv.DictWriter, obs: Obs, ctx: Optional[dict] = None) -> None:
    ctx = ctx or {}
    two_pi   = 2 * mp.pi
    phase_m1 = obs.winding_accum % 1
    invQ     = 1/obs.q_true if obs.q_true != 0 else mp.mpf("0")
    invn     = 1/mp.mpf(obs.step) if obs.step > 0 else mp.mpf("0")
    dev6_val = (obs.n_times_q6_true - 6
                if obs.n_times_q6_true is not None else mp.mpf("nan"))

    writer.writerow({
        "step":               obs.step,
        "rho":                mp.nstr(obs.rho, 50),
        "eta_lift":           mp.nstr(obs.eta_lift, 50),
        "eta_wrap":           mp.nstr(obs.eta_wrap, 50),
        "sin_eta":            mp.nstr(obs.sin_eta, 50),
        "cos_eta":            mp.nstr(obs.cos_eta, 50),
        "drift":              mp.nstr(obs.drift, 50),
        "remainder":          mp.nstr(obs.remainder, 50),
        "u":                  mp.nstr(obs.u, 50),
        "v":                  mp.nstr(obs.v, 50),
        "Q_true":             mp.nstr(obs.q_true, 50),
        "Q_euclid":           mp.nstr(obs.q_euclid, 50),
        "invQ_true":          mp.nstr(invQ, 50),
        "nQ_true":            mp.nstr(obs.n_times_q_true, 50),
        "Q6_true":            "" if obs.q6_true is None else mp.nstr(obs.q6_true, 50),
        "nQ6_true":           "" if obs.n_times_q6_true is None else mp.nstr(obs.n_times_q6_true, 50),
        "dev6":               "" if obs.n_times_q6_true is None else mp.nstr(dev6_val, 50),
        "invn":               mp.nstr(invn, 50),
        "trJ":                mp.nstr(obs.tr_j, 50),
        "detJ":               mp.nstr(obs.det_j, 50),
        "discr":              mp.nstr(obs.discr, 50),
        "eig_kind":           obs.eig_kind,
        "dist_P1":            mp.nstr(obs.dist_p1, 50),
        "dist_P2":            mp.nstr(obs.dist_p2, 50),
        "rotation_increment": mp.nstr(obs.rotation_increment, 50),
        "winding_accum":      mp.nstr(obs.winding_accum, 50),
        "phase_mod1":         mp.nstr(phase_m1, 50),
        "cos_phase":          mp.nstr(mp.cos(two_pi * phase_m1), 50),
        "sin_phase":          mp.nstr(mp.sin(two_pi * phase_m1), 50),
        # ISP columns [v5.0-ISP-CSV-1]
        "Theta":              mp.nstr(obs.Theta, 50),
        "V_anticorr":         mp.nstr(obs.V_anticorr, 50),
        "isp_sector":         obs.isp_sector,
        "R_overshoot":        "" if obs.R_overshoot is None else mp.nstr(obs.R_overshoot, 50),
        "is_primitive_precross": "1" if obs.is_primitive_precross else "0",
        "wedge_ok":           "1" if obs.wedge_ok else "0",
        # Birth / Φ_{2→3} passive markers [v6.0-BIRTH-1]
        "Q_s":                mp.nstr(obs.Q_s, 50),
        "Qc_birth_shear":     mp.nstr(obs.Qc_birth_shear, 50),
        "Qc_birth_recoil":    mp.nstr(obs.Qc_birth_recoil, 50),
        "birth_threshold":    ctx.get("birth_threshold", ""),
        "birth_regime_entered": "1" if obs.birth_regime_entered else "0",
        "birth_action":       ctx.get("birth_action", ""),
        "birth_threshold_source": ctx.get("birth_threshold_source", ""),
        "cascade_route":      CASCADE_ROUTE,
        "cascade_route_tag":  CASCADE_ROUTE_TAG,
        "extrapolation_tag":  obs.extrapolation_tag,
        "p2_escape_flag":     "1" if obs.p2_escape_flag else "0",
    })


# =============================================================================
# Regime classifier (per-cycle / 6-step strobe)  [v6.0-REGIME-1]
# OBSERVABLE-ALIGNMENT classifier ONLY — NOT a theorem about IC memory erasure.
# Kept on the block (cycle) layer; never mixed into the per-step CSV (SG-2).
# =============================================================================

CYCLE_CSV_FIELDS = [
    "cycle", "n", "Q_n", "Q_pred_backbone", "backbone_residual",
    "backbone_residual_scaled", "backbone_residual_tol",
    "regime", "alignment_onset_cycle",
    "alignment_window_start_n", "alignment_window_end_n",
    "kappa_fit", "C_est",
]


def classify_regime_cycles(
    q6_samples: List[Tuple[int, mp.mpf]],
    regime_tol: mp.mpf,
    regime_k: int,
    window_frac: float,
) -> Tuple[List[dict], Optional[int], Optional[int], Optional[int], mp.mpf, mp.mpf]:
    """
    Two-pass classifier:
      Pass 1 — fit κ on the trailing `window_frac` of blocks via the backbone
               1/Q_n = (1/6)(n + C):  slope≈1/6, C_est = intercept/slope, κ = C/6.
      Pass 2 — per-cycle scaled backbone residual r = (Q_n − Q_pred)/Q_n with
               Q_pred = 6/(n + C_est). Alignment onset = first block beginning a
               run of `regime_k` consecutive |r| < tol blocks.
    Returns (rows, onset_cycle, win_lo_n, win_hi_n, kappa_fit, C_est).
    """
    rows: List[dict] = []
    n_blk = len(q6_samples)
    nan = mp.mpf("nan")
    if n_blk < 2:
        return rows, None, None, None, nan, nan

    start = int((1 - window_frac) * n_blk)
    start = max(0, min(start, n_blk - 2))
    win = q6_samples[start:]
    win_lo_n, win_hi_n = win[0][0], win[-1][0]

    xs = [mp.mpf(n) for n, _ in win]
    ys = [1 / q if q != 0 else mp.mpf("0") for _, q in win]
    slope, intercept, _r2 = linear_regression(xs, ys)
    if slope == 0 or not mp.isfinite(slope):
        return rows, None, win_lo_n, win_hi_n, nan, nan
    C_est = intercept / slope
    kappa_fit = C_est / 6

    # Pass 2: residuals over all blocks
    scaled = []
    for n, q in q6_samples:
        q_pred = 6 / (mp.mpf(n) + C_est)
        resid = q - q_pred
        r = resid / q if q != 0 else mp.mpf("nan")
        scaled.append((n, q, q_pred, resid, r))

    # alignment onset: first index starting a run of regime_k aligned blocks
    onset_idx = None
    for i in range(n_blk - regime_k + 1):
        ok = True
        for j in range(i, i + regime_k):
            rj = scaled[j][4]
            if not (mp.isfinite(rj) and abs(rj) < regime_tol):
                ok = False
                break
        if ok:
            onset_idx = i
            break
    onset_cycle = (scaled[onset_idx][0] // 6) if onset_idx is not None else None

    for i, (n, q, q_pred, resid, r) in enumerate(scaled):
        if onset_idx is None:
            regime = "unclassified"
        elif i < onset_idx:
            regime = "early_ic_memory"
        else:
            regime = "late_aligned_backbone"
        rows.append({
            "cycle": n // 6, "n": n,
            "Q_n": mp.nstr(q, 50),
            "Q_pred_backbone": mp.nstr(q_pred, 50),
            "backbone_residual": mp.nstr(resid, 50),
            "backbone_residual_scaled": mp.nstr(r, 50),
            "backbone_residual_tol": mp.nstr(regime_tol, 12),
            "regime": regime,
            "alignment_onset_cycle": "" if onset_cycle is None else onset_cycle,
            "alignment_window_start_n": win_lo_n,
            "alignment_window_end_n": win_hi_n,
            "kappa_fit": mp.nstr(kappa_fit, 30),
            "C_est": mp.nstr(C_est, 30),
        })
    return rows, onset_cycle, win_lo_n, win_hi_n, kappa_fit, C_est


def write_cycle_csv(path: str, rows: List[dict]) -> None:
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CYCLE_CSV_FIELDS)
        w.writeheader()
        for row in rows:
            w.writerow(row)


# =============================================================================
# NEW v4.5: Two-stage joint (κ, Ã, φ*) fit  [v4.5-JOINT-1, v4.5.3-TWOSTAGE-1]
# =============================================================================

def joint_phi_star_fit(
    q6_samples: List[Tuple[int, mp.mpf]],
    tau: float,
    window_ratio: float,
    Q0: float,
    kappa_seed: Optional[float] = None,
    spiral_crossings: Optional[List[float]] = None,
    m_win_lo_override: Optional[float] = None,
    m_win_hi_override: Optional[float] = None,
) -> Dict:
    """
    [v4.5.3-TWOSTAGE-1] Two-stage joint fit of (kappa, A-tilde, phi*).

    Stage 1: fix kappa from kappa_seed (from Fit-A C_est/6). Not a free parameter.
    Stage 2: subtract backbone 1/(m+kappa_fixed); fit (A_tilde, phi*) on residual.

    Window selection (v4.5.4-WINOVER-1):
      If m_win_lo_override is set: bypass automatic [2κ,100κ] logic entirely.
        Use [m_win_lo_override, m_win_hi_override] (or [m_win_lo_override, m_end]).
        Log-period floor F1 and 500-block floor F2 still applied.
        Reported in output as "MANUAL OVERRIDE" for traceability.
      Otherwise (automatic):
        kappa > 0: [2κ, 100κ] blocks.
        kappa < 0: crossing-centred if spiral_crossings supplied, else [5|κ|, m_end].

    Formula scope: §5.10 applies to BELOW-APPROACH ICs only.
    """
    if not _SCIPY_AVAILABLE:
        return {"status": "scipy_unavailable",
                "message": "numpy/scipy not installed; pip install scipy"}

    if len(q6_samples) < 1000:
        return {"status": "insufficient_data", "n_samples": len(q6_samples)}

    ms_all = np.array([float(n) / 6.0 for n, q in q6_samples], dtype=np.float64)
    Qs_all = np.array([float(q)         for n, q in q6_samples], dtype=np.float64)

    log_period = 2.0 * math.pi / tau
    n_total    = len(q6_samples)
    m_end      = ms_all[-1]
    two_pi     = 2.0 * math.pi

    # -------------------------------------------------------------------------
    # STAGE 1: kappa fixed from seed
    # -------------------------------------------------------------------------
    if kappa_seed is not None and math.isfinite(kappa_seed) and kappa_seed != 0.0:
        kappa_fixed = kappa_seed
    else:
        mid_idx = max(0, int(0.9 * n_total))
        kappa_naive = float(1.0 / Qs_all[mid_idx] - ms_all[mid_idx])
        kappa_fixed = kappa_naive if math.isfinite(kappa_naive) else 1.0

    kappa_abs     = abs(kappa_fixed)
    above_approach = (kappa_fixed < 0)

    # -------------------------------------------------------------------------
    # WINDOW (v4.5.4-WINOVER-1)
    # -------------------------------------------------------------------------
    window_was_overridden = (m_win_lo_override is not None)

    if window_was_overridden:
        # Manual override: bypass [2κ,100κ] / crossing logic entirely
        m_win_lo = float(m_win_lo_override)
        m_win_hi = float(m_win_hi_override) if m_win_hi_override is not None else m_end
    elif above_approach:
        if spiral_crossings and len(spiral_crossings) >= 1:
            m_cross  = [c / 6.0 for c in spiral_crossings]
            m_win_lo = 0.5 * m_cross[0]
            m_win_hi = 5.0 * m_cross[-1]
        else:
            m_win_lo = 5.0 * kappa_abs
            m_win_hi = m_end
    else:
        m_win_lo = 2.0   * kappa_abs
        m_win_hi = 100.0 * kappa_abs

    m_win_hi = min(m_win_hi, m_end)
    m_win_lo = max(m_win_lo, ms_all[0])

    # Floor F1: one log-period minimum — SKIPPED if window was manually overridden.
    # [v4.5.5-F1SKIP-1] When --phi-star-m-start/end is set, the user's explicit
    # window boundaries are respected unconditionally. F1 would silently defeat
    # the override (e.g. [500k,1M] → [4k,1M]) because ln(1M/500k)=0.69 < 5.44.
    # We warn in print_phi_star_extraction but do NOT modify the window.
    if not window_was_overridden and m_win_hi > m_win_lo and m_win_lo > 0:
        if math.log(m_win_hi / m_win_lo) < log_period:
            pole_floor   = (5.0 * kappa_abs) if above_approach else ms_all[0]
            m_win_lo_lp  = m_win_hi * math.exp(-log_period)
            m_win_lo     = max(m_win_lo_lp, pole_floor, ms_all[0])

    idx_lo = int(np.searchsorted(ms_all, m_win_lo))
    idx_hi = int(np.searchsorted(ms_all, m_win_hi, side="right")) - 1
    idx_hi = min(idx_hi, n_total - 1)

    # Floor F2: 500 blocks minimum — also skipped for manual override.
    if not window_was_overridden and idx_hi - idx_lo < 500:
        pole_idx = int(np.searchsorted(ms_all, 5.0 * kappa_abs)) if above_approach else 0
        idx_lo   = max(pole_idx, idx_hi - 500)

    if idx_hi <= idx_lo:
        fallback_len = max(2000, int(n_total / window_ratio))
        idx_lo = max(0, n_total - fallback_len)
        idx_hi = n_total - 1

    ms = ms_all[idx_lo : idx_hi + 1]
    Qs = Qs_all[idx_lo : idx_hi + 1]

    if len(ms) < 100:
        return {"status": "insufficient_tail",
                "tail_blocks": int(len(ms)),
                "kappa_fixed": float(kappa_fixed),
                "message": "tail < 100 blocks after window constraints; run longer"}

    if len(ms) > 2000:
        idx_ds = np.round(np.linspace(0, len(ms) - 1, 2000)).astype(int)
        ms_fit = ms[idx_ds]
        Qs_fit = Qs[idx_ds]
    else:
        ms_fit = ms.copy()
        Qs_fit = Qs.copy()

    # -------------------------------------------------------------------------
    # STAGE 2: fit (A_tilde, phi*) on backbone-subtracted residual
    # -------------------------------------------------------------------------
    backbone     = 1.0 / (ms_fit + kappa_fixed)
    residual_sig = Qs_fit - backbone

    def spiral_model(m, A_tilde, phi_star):
        return A_tilde * m**(-1.5) * np.cos(tau * np.log(m) + phi_star)

    resid_rms = float(np.std(residual_sig))
    A_scale   = max(resid_rms * float(np.mean(ms_fit**1.5)), 1e-8)

    best_result2   = None
    best_residual2 = math.inf

    for phi_seed in [0.0, math.pi/2, math.pi, 3*math.pi/2]:
        for A_seed in [A_scale, -A_scale]:
            try:
                popt2, pcov2 = curve_fit(
                    spiral_model, ms_fit, residual_sig,
                    p0=[A_seed, phi_seed],
                    maxfev=30000,
                    ftol=1e-14,
                    xtol=1e-14,
                )
                res2 = float(np.sum((spiral_model(ms_fit, *popt2) - residual_sig)**2))
                if res2 < best_residual2:
                    best_residual2 = res2
                    best_result2   = (popt2, pcov2)
            except Exception:
                continue

    if best_result2 is None:
        return {"status": "fit_failed", "stage": 2,
                "kappa_fixed": float(kappa_fixed),
                "message": "Stage-2 curve_fit failed on all seeds"}

    popt2, pcov2 = best_result2
    A_fit, phi_raw = popt2
    try:
        perr2 = np.sqrt(np.diag(pcov2))
    except Exception:
        perr2 = np.array([math.nan, math.nan])

    phi_empirical_rad = phi_raw % two_pi
    phi_empirical_deg = math.degrees(phi_empirical_rad)

    # Spiral quality metrics
    resid_ss_before = float(np.sum(residual_sig**2))
    r2_spiral = 1.0 - best_residual2 / resid_ss_before if resid_ss_before > 0 else 0.0
    spiral_amp_rms = float(abs(A_fit) * np.mean(ms_fit**(-1.5)))
    snr = spiral_amp_rms / resid_rms if resid_rms > 0 else 0.0

    # -------------------------------------------------------------------------
    # ALGEBRAIC COMPARISON (S5.10 — below-approach only)
    # -------------------------------------------------------------------------
    phi_alg_rad = phi_alg_deg = diff_rad = diff_deg = math.nan
    formula_in_scope = not above_approach
    if formula_in_scope:
        phi_alg_raw = (
            (2.0 * math.pi / 3.0)
            - tau * math.log(2.0 * Q0)
            + (tau / 4.0) * Q0
            + (tau / 80.0) * Q0 * Q0
        )
        phi_alg_rad = phi_alg_raw % two_pi
        phi_alg_deg = math.degrees(phi_alg_rad)
        diff_rad    = abs(phi_empirical_rad - phi_alg_rad)
        if diff_rad > math.pi:
            diff_rad = two_pi - diff_rad
        diff_deg = math.degrees(diff_rad)

    ln_coverage         = math.log(ms[-1] / ms[0]) if ms[0] > 0 else 0.0
    log_periods_covered = ln_coverage / log_period

    return {
        "status":               "success",
        "above_approach":       above_approach,
        "formula_in_scope":     formula_in_scope,
        "kappa_fixed":          float(kappa_fixed),
        "A_fit":                float(A_fit),
        "A_err":                float(perr2[0]),
        "phi_empirical_rad":    float(phi_empirical_rad),
        "phi_empirical_deg":    float(phi_empirical_deg),
        "phi_raw_err_rad":      float(perr2[1]),
        "r2_spiral":            float(r2_spiral),
        "snr_spiral":           float(snr),
        "residual_rms":         float(resid_rms),
        "phi_algebraic_rad":    float(phi_alg_rad),
        "phi_algebraic_deg":    float(phi_alg_deg),
        "discrepancy_rad":      float(diff_rad),
        "discrepancy_deg":      float(diff_deg),
        "residual_ss":          float(best_residual2),
        "window_points":        int(len(ms_fit)),
        "tail_blocks":          int(len(ms)),
        "m_start":              float(ms[0]),
        "m_end":                float(ms[-1]),
        "ln_coverage":          float(ln_coverage),
        "log_periods_covered":  float(log_periods_covered),
        "window_was_overridden": window_was_overridden,
        "window_ratio_used":    float(window_ratio),
    }


def print_phi_star_extraction(
    result: Dict,
    Q0: float,
    tau: float,
) -> None:
    """[v4.5.3-TWOSTAGE-1] Print two-stage φ* extraction report."""
    print("\n" + "=" * 78)
    print("TWO-STAGE φ* EXTRACTION  (DSN v4.5 §5.10)  [v4.5.3-TWOSTAGE-1]")
    print("=" * 78)
    print(f"  Q₀ = η₀²          : {Q0:.10f}")
    print(f"  τ  (exact)         : {tau:.10f}  (= 2√3/3)")
    print()

    if result["status"] != "success":
        print(f"  ✗ Fit did not succeed: {result.get('message', result['status'])}")
        if "kappa_fixed" in result:
            print(f"    κ_fixed used      : {result['kappa_fixed']:.4f}")
        return

    above = result.get("above_approach", False)
    in_scope = result.get("formula_in_scope", True)

    if above:
        print("  ⚠ ABOVE-APPROACH IC (C_est < 0, nQ6 > 6 throughout).")
        print("    DSN §5.10 formula was derived for BELOW-APPROACH ICs only.")
        print("    Algebraic comparison suppressed — φ* reported for reference.")
    print()

    print(f"  Stage 1 — κ fixed  : {result['kappa_fixed']:.6f}"
          f"  (from Fit-A C_est/6, not fitted)")
    print()
    if result.get("window_was_overridden"):
        print(f"  ⚑ MANUAL WINDOW OVERRIDE active (--phi-star-m-start/end).")
        print(f"    Automatic [2κ,100κ] / crossing-centred logic bypassed.")
        print(f"    F1 (log-period floor) and F2 (500-block floor) suppressed.")
        lp = result["log_periods_covered"]
        if lp < 0.99:
            print(f"  ⚠ Override window spans only {lp:.3f} log-periods (< 1.00).")
            print(f"    φ* may be biased — consider widening the override range.")
    print(f"  Window             : {result['tail_blocks']} blocks"
          f"  [{result['m_start']:.1f} ≤ m ≤ {result['m_end']:.1f}]")
    print(f"  Fit points         : {result['window_points']}  (downsampled)")
    lp = result["log_periods_covered"]
    print(f"  Log-period coverage: {lp:.3f}  (need ≥ 1.00 for clean φ* extraction)")
    if lp < 0.99:
        print("  ⚠ Window spans < 1 log-period — φ* extraction may be unreliable.")
    print()

    print(f"  Stage 2 — spiral fit on backbone-subtracted residual:")
    print(f"    Residual RMS      : {result['residual_rms']:.4e}  (before spiral removal)")
    print(f"    |Ã|               : {abs(result['A_fit']):.6e}  ± {result['A_err']:.2e}")
    snr = result.get("snr_spiral", 0.0)
    r2  = result.get("r2_spiral",  0.0)
    print(f"    Spiral SNR        : {snr:.3f}  (spiral amplitude / residual RMS)")
    print(f"    R² (spiral fit)   : {r2:.6f}  (variance explained by spiral model)")
    if snr < 0.1:
        print("    ⚠ SNR < 0.1 — spiral too weak to resolve φ* reliably in this window.")
    print()

    print(f"  φ* empirical (fit) : {result['phi_empirical_rad']:.8f} rad"
          f"  = {result['phi_empirical_deg']:.4f}°")

    phi_err = result.get("phi_raw_err_rad", float("nan"))
    if math.isfinite(phi_err):
        if phi_err < 0.1:
            print(f"  φ* uncertainty     : {phi_err:.4f} rad  (1σ)")
        else:
            print(f"  ⚠ φ* uncertainty large: {phi_err:.4f} rad — fit poorly constrained.")
    print()

    if in_scope and math.isfinite(result.get("phi_algebraic_rad", float("nan"))):
        print(f"  φ* algebraic §5.10 : {result['phi_algebraic_rad']:.8f} rad"
              f"  = {result['phi_algebraic_deg']:.4f}°")
        d   = result["discrepancy_deg"]
        dr  = result["discrepancy_rad"]
        print(f"  Discrepancy        : {dr:.6f} rad  = {d:.4f}°  (mod 2π, shorter arc)")
        print()

        if snr < 0.1:
            verdict = "✗  UNRELIABLE  — spiral SNR < 0.1; φ* not resolved."
        elif lp < 0.99:
            verdict = "⚠  WINDOW SHORT  — < 1 log-period; φ* may be biased."
        elif d < 1.0:
            verdict = "✓ EXCELLENT  — O(Q₀) correction confirmed to < 1°."
        elif d < 5.0:
            verdict = "~  GOOD  — residual from O(Q₀²) terms or burst correction."
        elif d < 20.0:
            verdict = "⚠  PARTIAL  — higher-order burst corrections needed."
        else:
            verdict = "✗  LARGE DISCREPANCY  — check run length, window, or Q₀ range."
        print(f"  Verdict            : {verdict}")
    else:
        print("  [Algebraic comparison not applicable for above-approach ICs]")
        if snr < 0.1:
            print("  ⚠ SNR < 0.1 — φ* value unreliable regardless.")

    print()
    print("  Note: φ* in BLOCK notation (m = n/6).")
    print(f"  Step-notation: φ*_step = φ*_block − τ·ln 6"
          f"  ≈ φ*_block − {tau * math.log(6):.6f} rad")

    # [v5.0-ALIAS-1] ISP phase hierarchy supplement
    print_isp_phi_star_supplement(result, Q0=Q0, tau=tau)


# =============================================================================
# Printing
# =============================================================================

def print_header(args: argparse.Namespace) -> None:
    print("=" * 78)
    print("RTG DYAD AUDIT SIMULATOR  —  DSN v5.0")
    print("=" * 78)
    print(f"dps                 : {mp.mp.dps}")
    print(f"steps               : {args.steps}")
    print(f"rho0                : {args.rho0}")
    print(f"eta0                : {args.eta0}")
    if args.p2_eigvec:
        eps      = parse_expr(args.p2_eigvec_eps)
        t_theory = p2_escape_theory(eps)
        v_u, _   = p2_eigenvectors()
        print(f"p2_eigvec_mode      : ON  (eps={args.p2_eigvec_eps})")
        print(f"  unstable eigvec   : ({mpstr(v_u[0],8)}, {mpstr(v_u[1],8)})")
        print(f"  T_theory          : {mpstr(t_theory,10)} steps")
    print(f"print_every         : {args.print_every}")
    print(f"csv                 : {args.csv if args.csv else '(none)'}")
    print(f"csv_stride          : {args.csv_stride}")
    print(f"asymp_window        : {args.asymp_window}")
    print(f"stop_on_flag        : {args.stop_on_flag}")
    # v4.5 flags
    print(f"joint_fit           : {args.joint_fit}")
    print(f"window_ratio        : {args.window_ratio}")
    print(f"extract_phi_star    : {args.extract_phi_star}")
    isp_on = getattr(args, "isp_report", False) or args.joint_fit
    print(f"isp_report          : {isp_on}  {'(auto: joint-fit active)' if args.joint_fit and not getattr(args,'isp_report',False) else ''}")
    if args.phi_star_m_start is not None:
        print(f"phi_star_m_start    : {args.phi_star_m_start}  [MANUAL OVERRIDE]")
        print(f"phi_star_m_end      : {args.phi_star_m_end if args.phi_star_m_end else '(run end)'}")
    if not _SCIPY_AVAILABLE and (args.joint_fit or args.extract_phi_star):
        print("  ⚠ numpy/scipy not available — joint-fit and phi* extraction disabled.")
    print("=" * 78)
    print("NOTE: Q_euclid is a COMPARISON DIAGNOSTIC ONLY (DSN v4.5).")
    print("      All primary radial claims use Q_true only.")
    print("=" * 78)


def print_obs(obs: Obs, flags: Flags, show_q6: bool) -> None:
    line = (
        f"[{obs.step:7d}] "
        f"rho={mpstr(obs.rho,12):>14}  "
        f"eta_wrap={mpstr(obs.eta_wrap,12):>14}  "
        f"Qtrue={mpstr(obs.q_true,12):>14}  "
        f"Qeuc={mpstr(obs.q_euclid,12):>14}  "
        f"detJ={mpstr(obs.det_j,12):>14}  "
        f"eig={obs.eig_kind:>9}  "
        f"wind={mpstr(obs.winding_accum,8):>10}"
    )
    if show_q6 and obs.q6_true is not None:
        line += (f"  Q6={mpstr(obs.q6_true,10):>12}"
                 f"  nQ6={mpstr(obs.n_times_q6_true,10):>12}")
    line += f"  flags={format_flags(flags)}"
    print(line)


def print_model_discrimination(
    q6_samples: List[Tuple[int, mp.mpf]],
    winding_at_q6: List[mp.mpf],
    q0: mp.mpf,
    winding_final: mp.mpf,
    n_final: int,
    prior_alpha: Optional[mp.mpf] = None,
    q_onset_thr: mp.mpf = mp.mpf("2.0"),
) -> None:
    print("\n" + "=" * 78)
    print("MODEL DISCRIMINATION DIAGNOSTICS  (DSN v4.5)")
    print("=" * 78)

    tau, alpha_block_exact, alpha_step_exact, r_star_exact = _exact_constants()
    print(f"\n── EXACT ALGEBRAIC CONSTANTS  [v2.4-CONST-1] ──")
    print(f"   τ         = -Im(c₂₁) = 2√3/3        = {mpstr(tau, 10)}")
    print(f"   α_block   = τ/(2π) = √3/(3π)         = {mpstr(alpha_block_exact, 10)}  [per 6-step block]")
    print(f"   α_step    = α_block/6 = √3/(18π)     = {mpstr(alpha_step_exact, 10)}  [per step / Birkhoff twist]")
    print(f"   R*        = exp(π/τ) = exp(3π/(2√3)) = {mpstr(r_star_exact, 10)}  [exact crossing ratio]")

    trn = transient_analysis(q6_samples, q0, q_onset_thr=q_onset_thr)
    n_onset_step = trn["n_onset_step"]
    n_onset_idx  = trn["n_onset_idx"]
    approach_dir = trn.get("approach_dir", "unknown")

    print(f"\n── INITIAL REGIME & TRANSIENT DETECTION  [v2.4-ONSET-1] ──")
    print(f"   IC regime     : {trn['initial_regime'].upper()}-Q₀  (Q₀ = {trn['q0']:.6f})")
    print(f"   Approach dir  : nQ6 initially {'> 6  (ABOVE)' if approach_dir == 'above' else '< 6  (BELOW)'}")
    if trn["initial_regime"] == "large":
        print(f"   Peak nQ6      : {trn['nq6_peak']:.4f}  at n = {trn['n_peak_step']}")
        print(f"   Onset method  : {trn['onset_method']}  (Q_onset_thr = {mpstr(q_onset_thr, 4)})")
        print(f"   Asymptotic onset: n ≈ {n_onset_step}  ({trn['n_transient']} transient 6-step samples excluded)")
        if approach_dir == "below":
            print(f"   NOTE: below-approach → first asymptotic crossing is KINEMATIC.")
        else:
            print(f"   NOTE: above-approach → all asymptotic crossings are SPIRAL.")
            print(f"         Pre-onset oscillations (Q >> 1) filtered by Q-based onset.")
    else:
        print(f"   No violent burst detected. Asymptotic regime from n ≈ 0.")

    print("\n── FIT QUALITY: hyperbolic backbone Q ~ 6/(n+C) ──")
    print("   (Fit-A: 1/Q vs n → slope≈1/6;  Fit-B: nQ-6 vs 1/n → slope=A)")
    print(f"   {'window':>8}  {'n_pts':>6}  {'slope_A':>14}  {'C_est':>12}  "
          f"{'R²_A':>14}  {'slope_B(A)':>14}  {'intercept_B':>14}  {'R²_B':>12}")
    fit_results = asymptotic_fit_report(q6_samples, winding_at_q6)
    for frac, res in sorted(fit_results.items()):
        if res is None:
            print(f"   {'last '+str(int(frac*100))+'%':>8}  (insufficient data)")
            continue
        fA, fB = res["fit_A"], res["fit_B"]
        c_sign = "+" if float(fA["C_est"]) >= 0 else ""
        print(f"   {'last '+str(int(frac*100))+'%':>8}  {res['count']:>6}  "
              f"{mpstr(fA['slope'],10):>14}  {c_sign}{mpstr(fA['C_est'],8):>11}  "
              f"{mpstr(fA['R2'],12):>14}  {mpstr(fB['slope'],10):>14}  "
              f"{mpstr(fB['intercept'],8):>14}  {mpstr(fB['R2'],10):>12}")

    c_ests = [res["fit_A"]["C_est"] for res in fit_results.values() if res is not None]
    if len(c_ests) >= 2:
        c_spread = max(c_ests) - min(c_ests)
        c_signs  = set("neg" if float(c) < 0 else "pos" for c in c_ests)
        print(f"\n   C_est spread across windows: {mpstr(c_spread, 8)}")
        if "neg" in c_signs:
            print(f"   ⚠ C_est NEGATIVE — orbit approaches P₁ from ABOVE asymptotic curve")
            print(f"     (nQ₆ > 6 throughout; pole of Q~6/(n+C) lies at n=|C| in the past)")
        # [v4.5.2-STATUS-2] LOG-DRIFT fix: same logic as print_summary().
        # Compute std(nQ6) over the last 100 samples to detect log-drift vs transient.
        _cstats = asymptotic_c_stats(q6_samples, 100)
        _std_nq6 = float(_cstats[1]) if _cstats is not None else math.inf
        if c_spread < mp.mpf("50"):
            print("   ✓ C_est stable — asymptotic regime fully established.")
        elif c_spread < mp.mpf("500"):
            print("   ~ C_est drifting (late transient, nearly converged).")
        elif _std_nq6 < 1e-4:
            print("   LOG-DRIFT  (C_est spreading due to 7/54·ln M physics —")
            print("     asymptotic regime IS established; use joint fit for precise κ)")
        else:
            print("   ⚠ C_est strongly drifting — TRANSIENT ONGOING.")
            print(f"     Require n >> |C_est(10%)| ≈ {mpstr(abs(c_ests[0]),6)} steps.")
        c_est_late = c_ests[0]
        n_eff = n_final - float(c_est_late)
        if float(c_est_late) < 0:
            print(f"   n_eff = n_final − C_est(10%) = {n_final} − ({mpstr(c_est_late,6)}) = {n_eff:.0f}  (above-approach: n_eff > n_final)")
        else:
            print(f"   n_eff = n_final − C_est(10%) = {n_final} − {mpstr(c_est_late,6)} = {n_eff:.0f}")
            if n_eff < 0:
                print(f"   (negative → still inside transient)")

    print("\n── WINDING DEBT  [v2.3-WND-1] ──")
    wd = winding_debt_report(q6_samples, winding_final, n_final)
    print(f"   Expected winding (n/6)  : {wd['winding_expected']:.6f}")
    print(f"   Actual winding          : {wd['winding_actual']:.6f}")
    print(f"   Debt (deficit)          : {wd['debt_rotations']:.6f} rot  ({wd['debt_fraction']:.4f} frac)")
    print(f"   k_implied (≈ debt)      : {wd['k_implied']}")
    if approach_dir == "below":
        print(f"   → below-approach: 1 kinematic + {max(0,wd['k_implied']-1)} spiral crossings predicted.")
    else:
        print(f"   → above-approach: {wd['k_implied']} spiral crossings predicted (no kinematic).")

    print("\n── ZERO CROSSINGS OF nQ6 − 6  [v2.4-KIN-1] ──")
    zr = zero_crossing_report(q6_samples, n_onset_step, approach_dir=approach_dir)
    print(f"   n_onset: {n_onset_step}   approach: {approach_dir.upper()}")
    print(f"   Total: {zr['n_crossings_total']}  ({zr['n_transient']} TRANSIENT, "
          f"{zr['n_kinematic']} KINEMATIC, {zr['n_spiral']} SPIRAL)")
    for step, kind in zr["all_crossings"]:
        markers = {"TRANSIENT": "⚠ ", "KINEMATIC": "⬡ ", "SPIRAL": "✓ "}
        print(f"   {markers.get(kind,'  ')}Crossing at n ≈ {float(step):.0f}  [{kind}]")

    if zr["n_spiral"] >= 2:
        print(f"\n   SPIRAL crossing ratios (target R* = {mpstr(r_star_exact, 8)}):")
        for i, r in enumerate(zr["spiral_ratios"]):
            err_pct = (float(zr["spiral_ratio_vs_Rstar"][i]) - 1) * 100
            print(f"     r{i+1}{i+2} = {mpstr(r,6):>10}   vs R*: {err_pct:+.2f}%   "
                  f"vs 6φ²: {float(zr['spiral_ratio_vs_6phi2'][i]):.4f}")
        print(f"   log₁₀ spacings : {[f'{float(s):.4f}' for s in zr['spiral_log10']]}")
        print(f"   6φ² = {mpstr(zr['6phi2'],8)}  (SUPERSEDED — R* is the correct target)")
    elif zr["n_spiral"] == 1:
        print(f"   Only 1 spiral crossing — need longer run for ratio.")
    else:
        print(f"   No spiral crossings yet.")

    print("\n── SPIRAL PHASE DEFICIT & α  [v2.4-ALPHA-1] ──")
    pdr = phase_deficit_report(q6_samples, winding_at_q6, n_onset_idx=n_onset_idx, prior_alpha=prior_alpha)
    if pdr is None:
        print("   Insufficient data.")
    else:
        print(f"   α_block  measured = {mpstr(pdr['alpha_mean'], 10)}  ± {mpstr(pdr['alpha_std'], 6)}")
        print(f"   α_block  theory   = {mpstr(pdr['alpha_block_exact'], 10)}  [√3/(3π), exact]")
        print(f"   deviation         = {mpstr(pdr['alpha_theory_dev']*100, 4)}%  (O(Q^{{3/2}}) bias)")
        print(f"   α_step   measured = {mpstr(pdr['alpha_NF'], 10)}  [= α_block/6]")
        print(f"   α_step   theory   = {mpstr(pdr['alpha_step_exact'], 10)}  [√3/(18π), CLOSED]")
        print(f"   Fit range idx [{pdr['lo_idx']}, n]  (onset excluded: first {pdr['n_onset_idx']})")
        print()
        print(f"   Crossing ratio predictions:")
        print(f"     R* (exact)   = {mpstr(pdr['R_star_exact'], 8)}  ← PRIMARY TARGET")
        print(f"     k=3 (α-fit)  = {mpstr(pdr['crossing_ratio_k3'], 8)}  exp(3/(6α_block))")
        print(f"     k=2          = {mpstr(pdr['crossing_ratio_k2'], 8)}")
        print(f"     k=1          = {mpstr(pdr['crossing_ratio_k1'], 8)}")
        print(f"   Observed SPIRAL ratios : {[f'{float(r):.4f}' for r in zr['spiral_ratios']]}")
        print(f"   6φ² (SUPERSEDED)       : {mpstr(pdr['6phi2_reference'], 8)}")
        if pdr["universality"] is not None:
            u = pdr["universality"]
            print(f"\n   Universality: α_prior={mpstr(u['prior_alpha'],8)}, "
                  f"|Δ|/prior={mpstr(u['rel_diff'],6)}")
            if float(u["rel_diff"]) < 0.02:
                print(f"     ✓ α universal to {float(u['rel_diff'])*100:.2f}%")
            else:
                print(f"     ⚠ >2% difference — check transient exclusion.")
        print(f"\n   First 10 deficit samples (n, deficit, Q_mid, deficit/Q):")
        for n_s, d_s, q_s in pdr["deficit_sample"]:
            ratio_s = -d_s/q_s if q_s != 0 else float("nan")
            print(f"     n={n_s:8d}  deficit={d_s:+.6f}  Q={q_s:.4e}  deficit/Q={ratio_s:+.4f}")

    print("\n── SPIRAL-PHASE PROJECTION  [v2.4-BASIS-1] ──")
    print("   Basis: cos(τ·ln n)/√n  and  sin(τ·ln n)/√n  [O(n^{-1/2}) envelope]")
    spr = spiral_phase_report(q6_samples, winding_at_q6, frac=0.5)
    if spr is None:
        print("   Insufficient data.")
    else:
        rms    = spr["residual_rms"]
        Ac_rel = abs(spr["A_cos"]) / rms if rms != 0 else mp.mpf("0")
        As_rel = abs(spr["A_sin"]) / rms if rms != 0 else mp.mpf("0")
        A_combined = mp.sqrt(spr["A_cos"]**2 + spr["A_sin"]**2)
        spiral_phase_angle = mp.atan2(spr["A_sin"], spr["A_cos"]) * 180 / mp.pi
        print(f"   C_fit (last 50%)   : {mpstr(spr['C_fit'], 10)}")
        print(f"   R² hyperbolic       : {mpstr(spr['r2_hyperbolic'], 12)}")
        print(f"   Residual RMS        : {mpstr(rms, 8)}")
        print(f"   |A| combined        : {mpstr(A_combined, 8)}")
        print(f"   Spiral phase angle  : {mpstr(spiral_phase_angle, 6)}°")
        print(f"   |A_cos|/RMS = {mpstr(Ac_rel, 6)}   |A_sin|/RMS = {mpstr(As_rel, 6)}")
        if float(Ac_rel) > 0.1 or float(As_rel) > 0.1:
            print("   → Residual IS phase-locked to τ·ln n spiral.  Confirms DSN ⊕C.")
        else:
            print("   → Spiral component negligible; residual dominantly algebraic.")


def print_summary(
    first_obs: Obs,
    last_obs: Obs,
    q6_samples: List[Tuple[int, mp.mpf]],
    winding_at_q6: List[mp.mpf],
    asymp_window: int,
    p2_escape_step: Optional[int],
    p2_init_eps: Optional[mp.mpf],
    converge_tol: mp.mpf,
    c_spread_tol: mp.mpf,
    prior_alpha: Optional[mp.mpf] = None,
    q_onset_thr: mp.mpf = mp.mpf("2.0"),
) -> None:
    print("\n" + "=" * 78)
    print("SUMMARY")
    print("=" * 78)
    print(f"initial Q_true      : {mp.nstr(first_obs.q_true, 20)}")
    print(f"final Q_true        : {mp.nstr(last_obs.q_true, 20)}")
    print(f"  [comparison] init Q_euclid : {mp.nstr(first_obs.q_euclid, 20)}")
    print(f"  [comparison] final Q_euclid: {mp.nstr(last_obs.q_euclid, 20)}")
    print(f"final winding       : {mp.nstr(last_obs.winding_accum, 20)}")
    print(f"final rho           : {mp.nstr(last_obs.rho, 20)}")
    print(f"final eta_wrap      : {mp.nstr(last_obs.eta_wrap, 20)}")
    print(f"final detJ          : {mp.nstr(last_obs.det_j, 20)}")
    print(f"dist to P1          : {mp.nstr(last_obs.dist_p1, 20)}")
    print(f"dist to P2          : {mp.nstr(last_obs.dist_p2, 20)}")

    if p2_escape_step is not None:
        print(f"\nP2 escape measured  : step {p2_escape_step}")
        if p2_init_eps is not None and p2_init_eps > 0:
            t_theory = p2_escape_theory(p2_init_eps)
            ratio    = mp.mpf(p2_escape_step) / t_theory
            print(f"P2 escape theory    : {mp.nstr(t_theory, 10)} steps")
            print(f"measured / theory   : {mp.nstr(ratio, 8)}")
    else:
        print("\nP2 escape          : not detected")

    if q6_samples:
        print(f"\n6-step Q_true samples (first 8, last 1):")
        for n, q in q6_samples[:8]:
            print(f"  n={n:7d}  Q={mp.nstr(q,16):>22}  n*Q={mp.nstr(mp.mpf(n)*q,16):>22}")
        if len(q6_samples) > 8:
            n, q = q6_samples[-1]
            print(f"  ...  n={n:7d}  Q={mp.nstr(q,16):>22}  n*Q={mp.nstr(mp.mpf(n)*q,16):>22}")

    result = asymptotic_c_stats(q6_samples, asymp_window)
    fit_results = asymptotic_fit_report(q6_samples, winding_at_q6)
    c_ests = [res["fit_A"]["C_est"] for res in fit_results.values() if res is not None]
    c_spread = max(c_ests) - min(c_ests) if len(c_ests) >= 2 else mp.mpf("inf")

    print(f"\nAsymptotic-C rolling window (last {asymp_window} samples):")
    if result is None:
        print("  Insufficient samples.")
    else:
        mean_c, std_c, slope, count = result
        dev = abs(mean_c - 6)
        print(f"  mean(nQ6)      = {mp.nstr(mean_c, 12)}")
        print(f"  std(nQ6)       = {mp.nstr(std_c, 12)}")
        print(f"  |mean − 6|     = {mp.nstr(dev, 8)}  (threshold: {mp.nstr(converge_tol, 4)})")
        sign = "rising ↑" if slope > 0 else ("falling ↓" if slope < 0 else "flat")
        print(f"  trend/sample   = {mp.nstr(slope, 8)}  [{sign}]")
        print(f"  C_est spread   = {mp.nstr(c_spread, 8)}  (threshold: {mp.nstr(c_spread_tol, 4)})")

        if c_spread < c_spread_tol and dev < converge_tol:
            status = "CONVERGED ✓  (C_est stable, |mean−6| < tol)"
        elif c_spread < c_spread_tol:
            status = f"C_EST STABLE but |mean−6|={mp.nstr(dev,4)} still > tol"
        elif c_spread < mp.mpf("500"):
            status = "LATE TRANSIENT  (C_est drifting, nearly converged)"
        else:
            # Distinguish log-drift (deep asymptotic) from genuine transient.
            # For low-Q₀ ICs: C = 6κ ~ 6/Q₀ >> 1 and κ drifts logarithmically
            # as (7/54)·ln(M·Q₆) — this is PHYSICS, not transient contamination.
            # Signature: std(nQ6) tiny (< 1e-4) despite large C_est spread.
            if float(std_c) < 1e-4:
                status = ("LOG-DRIFT  (C_est spreading due to 7/54·ln M physics — "
                          "asymptotic regime IS established; use joint fit for κ)")
            else:
                status = ("TRANSIENT ONGOING  ⚠  "
                          "— run length insufficient for this IC amplitude\n"
                          "    Large-Q₀ ICs require n >> C_est(last 10%)")
        print(f"  STATUS: {status}")

    print_model_discrimination(
        q6_samples=q6_samples,
        winding_at_q6=winding_at_q6,
        q0=first_obs.q_true,
        winding_final=last_obs.winding_accum,
        n_final=last_obs.step,
        prior_alpha=prior_alpha,
        q_onset_thr=q_onset_thr,
    )


def print_isp_report(
    q6_samples: List[Tuple[int, mp.mpf]],
    isp_theta_samples: List[Tuple],  # 6-tuple: (n, Q, sector, R, Θ, is_prim_precross)
) -> None:
    """
    [v5.0-ISP-DIAG-1] ISP Structural Report.  DSN §3.x.11–13.

    Distinguishes two conceptually separate objects:
      (A) ISP PRE-CROSS SECTOR ENTRIES  — Θ ∈ [−2π/3, −π/3) (angle condition only)
      (B) PRIMITIVE PRE-CROSSING ENTRIES — ρ<0 ∧ sinη<0 ∧ ρ−sinη≥0 (canonical)

    Safety checks are NOT fused:
      ceiling_ok  : R ≤ sin(√Q)   [universal overshoot ceiling, ALG]
      qc_ok       : Q < Q_c       [sufficient for one-step safety]
      rho_lt_ln2  : R < ln 2      [direct critical-curve threshold]
    """
    print("\n" + "=" * 78)
    print("ISP STRUCTURAL REPORT  (DSN §3.x)  [v5.0-ISP-DIAG-1]")
    print("=" * 78)

    alpha_proj, q_c = _isp_constants()
    tau, *_ = _exact_constants()
    ln2 = math.log(2)

    print(f"\n── ISP CONSTANTS ──")
    print(f"   α_proj = Π₀ = π − arctan(√15)  = {float(alpha_proj):.6f} rad"
          f"  = {math.degrees(float(alpha_proj)):.4f}°  [ALG structure, DSN §3.x.13]")
    print(f"   Q_c    = (arcsin(ln 2))²         = {float(q_c):.6f}  [ALG, DSN §3.x.11g]")
    print(f"   ln 2   = critical-curve threshold = {ln2:.6f}")
    print(f"   τ      = 2√3/3                   = {float(tau):.10f}")
    print(f"\n   Note: safety checks use THREE separate criteria (never fused):")
    print(f"     ceiling_ok  : R ≤ sin(√Q)  — universal overshoot ceiling")
    print(f"     qc_ok       : Q < Q_c      — sufficient for one-step safety")
    print(f"     rho_lt_ln2  : R < ln 2     — direct critical-curve bound")

    if not isp_theta_samples:
        print("\n  No ISP samples collected.")
        return

    # Unpack 6-tuples
    n_total = len(isp_theta_samples)
    tail_start = n_total // 2
    tail   = isp_theta_samples[tail_start:]
    thetas = [float(th)  for _, _, _, _, th, _ in tail]
    sectors= [sec        for _, _, sec, _, _, _ in tail]

    # Sector fractions (last 50%)
    n_pre  = sectors.count("pre-cross")
    n_grow = sectors.count("growth")
    n_dec  = sectors.count("decay")
    n_ax   = sectors.count("axis")
    n_tot  = len(sectors)

    print(f"\n── SECTOR DISTRIBUTION (last 50% of 6-step samples, n={n_tot}) ──")
    print(f"   [Angle-sector only: Θ ∈ canonical intervals, not primitive conditions]")
    for label, count in [("pre-cross", n_pre), ("growth", n_grow),
                          ("decay", n_dec), ("axis", n_ax)]:
        bar = "█" * min(40, int(40 * count / max(n_tot, 1)))
        print(f"   {label:10s}  {count:6d} ({100*count/max(n_tot,1):5.1f}%)  {bar}")

    # Θ statistics
    if thetas:
        th_mean = sum(thetas) / len(thetas)
        th_min  = min(thetas)
        th_max  = max(thetas)
        print(f"\n── Θ STATISTICS (last 50%) ──")
        print(f"   mean Θ  = {math.degrees(th_mean):+.3f}°  =  {th_mean:+.4f} rad")
        print(f"   min  Θ  = {math.degrees(th_min):+.3f}°  =  {th_min:+.4f} rad")
        print(f"   max  Θ  = {math.degrees(th_max):+.3f}°  =  {th_max:+.4f} rad")
        print(f"   pre-cross sector bounds  : [−120.0°, −60.0°)")

    # -------------------------------------------------------------------------
    # Table A: ISP PRE-CROSS SECTOR ENTRIES (angle condition only)
    # -------------------------------------------------------------------------
    sector_entries = [(n, q, r, th) for n, q, sec, r, th, _ in isp_theta_samples
                      if sec == "pre-cross"]

    print(f"\n── (A) ISP PRE-CROSS SECTOR ENTRIES  (Θ ∈ [−2π/3,−π/3), full run) ──")
    print(f"   Definition: angle-sector only. NOT the canonical footprint (see B below).")
    print(f"   Total: {len(sector_entries)}")
    if sector_entries:
        print(f"\n   {'n':>9}  {'Q':>12}  {'Θ (°)':>10}  {'R':>14}"
              f"  {'ceiling_ok':>10}  {'qc_ok':>7}  {'R<ln2':>7}")
        n_unsafe_ceil = n_unsafe_qc = n_unsafe_ln2 = 0
        for (n, q, r_val, th) in sector_entries[:25]:
            q_f = float(q)
            th_f = float(th)
            r_f  = float(r_val) if r_val is not None else float("nan")
            sc   = isp_safety_checks(q, r_val if r_val is not None else mp.mpf("0"))
            if not sc["ceiling_ok"]: n_unsafe_ceil += 1
            if not sc["qc_ok"]:      n_unsafe_qc   += 1
            if not sc["rho_lt_ln2"]: n_unsafe_ln2  += 1
            c_ok = "✓" if sc["ceiling_ok"] else "⚠"
            q_ok = "✓" if sc["qc_ok"]      else "—"
            r_ok = "✓" if sc["rho_lt_ln2"] else "⚠"
            print(f"   {n:>9d}  {q_f:>12.6e}  {math.degrees(th_f):>10.3f}"
                  f"  {r_f:>14.6e}  {c_ok:>10}  {q_ok:>7}  {r_ok:>7}")
        if len(sector_entries) > 25:
            print(f"   ... ({len(sector_entries)-25} more sector entries not shown)")
        print(f"\n   ceiling_ok violations : {n_unsafe_ceil}")
        print(f"   Q > Q_c  (qc_ok=—)   : {n_unsafe_qc}  (not a violation — Q_c is sufficient, not necessary)")
        print(f"   R ≥ ln 2 violations   : {n_unsafe_ln2}")
        if n_unsafe_ceil == 0:
            print(f"   ✓ All sector entries satisfy overshoot ceiling R ≤ sin(√Q).")

    # -------------------------------------------------------------------------
    # Table B: PRIMITIVE PRE-CROSSING ENTRIES (canonical condition)
    # -------------------------------------------------------------------------
    prim_entries = [(n, q, r, th) for n, q, sec, r, th, is_prim in isp_theta_samples
                    if is_prim]

    print(f"\n── (B) PRIMITIVE PRE-CROSSING ENTRIES  (ρ<0 ∧ sinη<0 ∧ ρ−sinη≥0, full run) ──")
    print(f"   Definition: strict canonical pre-crossing condition. DSN §3.x.11c [ALG].")
    print(f"   This is the object relevant to the Certificate program (OPEN 11).")
    print(f"   Total: {len(prim_entries)}")

    if prim_entries:
        # Branch detection: for canonical family (rho0=0, eta0=q),
        # the primitive pre-crossing occurs at step 3 (Γ₃) or step 4 (Γ₄)
        # within the first 6-step block. At 6-step sampling, n is a multiple
        # of 6, so the sub-step index is determined by the first primitive
        # pre-crossing step divided by the 6-step block.
        # Heuristic: if first_n/6 == 1008 and block 1 (n=1..6) contains the
        # crossing, that's Γ₃. For small-Q₀ ICs this is always block 1 step 3.
        # We use the modular position of first_n within a 6-step window:
        # if first_n is the 6-step multiple just after the crossing, the
        # crossing was at first_n - 3 (Γ₃) or first_n - 2 (Γ₄).
        # For the canonical family with small Q₀: always Γ₃ (n_pre = 3).
        # For now: report numeric value and leave formal branch certification
        # to the primitive footprint study (ISP task 1).

        first_n = isp_theta_samples[0][0] if isp_theta_samples else 0
        branch_n = first_n  # step of first sampled pre-cross / diagnostic anchor

        branch = f"n={branch_n}"
        print(f"   First primitive pre-crossing at n = {first_n}  →  branch: {branch}")

        print(f"\n   {'n':>9}  {'Q':>12}  {'Θ (°)':>10}  {'R':>14}"
              f"  {'ceiling_ok':>10}  {'qc_ok':>7}  {'R<ln2':>7}  {'branch':>7}")
        n_unsafe_ceil = n_unsafe_ln2 = 0
        for (n, q, r_val, th) in prim_entries[:25]:
            q_f  = float(q)
            th_f = float(th)
            r_f  = float(r_val) if r_val is not None else float("nan")
            # For primitive pre-crossing, compute R from ISP formula if not already in sector
            if r_val is None and q > 0:
                r_val = isp_overshoot(q, mp.mpf(str(th)))
                r_f   = float(r_val)
            sc  = isp_safety_checks(q, r_val if r_val is not None else mp.mpf("0"))
            if not sc["ceiling_ok"]: n_unsafe_ceil += 1
            if not sc["rho_lt_ln2"]: n_unsafe_ln2 += 1
            c_ok = "✓" if sc["ceiling_ok"] else "⚠"
            q_ok = "✓" if sc["qc_ok"]      else "—"
            r_ok = "✓" if sc["rho_lt_ln2"] else "⚠"
            br   = f"n%6={n%6}"
            print(f"   {n:>9d}  {q_f:>12.6e}  {math.degrees(th_f):>10.3f}"
                  f"  {r_f:>14.6e}  {c_ok:>10}  {q_ok:>7}  {r_ok:>7}  {br:>7}")
        if len(prim_entries) > 25:
            print(f"   ... ({len(prim_entries)-25} more primitive pre-crossing entries not shown)")
        print(f"\n   ceiling_ok violations : {n_unsafe_ceil}")
        print(f"   R ≥ ln 2 violations   : {n_unsafe_ln2}")
        q_above_qc = sum(1 for _, q, _, _ in prim_entries if float(q) >= float(q_c))
        print(f"   Entries with Q ≥ Q_c  : {q_above_qc}  "
              f"(one-step safety not guaranteed by Q_c criterion alone)")
        if n_unsafe_ceil == 0 and n_unsafe_ln2 == 0:
            print(f"   ✓ All primitive pre-crossing entries satisfy ceiling and R < ln 2.")
        elif n_unsafe_ceil > 0:
            print(f"   ⚠ {n_unsafe_ceil} primitive pre-crossing entries VIOLATED the overshoot ceiling!")
    else:
        print("   No primitive pre-crossing entries in this run.")

    # Anti-correlation / winding-kick note
    print(f"\n── WINDING-KICK SIGN INDICATOR  (DSN §3.x.9c) ──")
    print(f"   V_anticorr > 0  (decay branch) : winding kicks contract Q")
    print(f"   V_anticorr < 0  (growth branch): winding kicks pump Q")
    print(f"   Track 'V_anticorr' and 'is_primitive_precross' columns in CSV.")
    print(f"   Track 'wedge_ok' column to audit η_wrap < ρ < 0 (ISP v7 wedge).")


def print_isp_phi_star_supplement(
    result: Dict,
    Q0: float,
    tau: float,
) -> None:
    """
    [v5.0-ALIAS-1] ISP phase hierarchy supplement to φ* extraction.
    Prints alias-function correction and Π₀ comparison.
    DSN §3.x.13, §3.x.13a.
    """
    if result.get("status") != "success":
        return
    if result.get("above_approach", False):
        return  # formula not in scope

    import math as _m
    two_pi = 2 * _m.pi
    tau_val = tau
    alpha_proj, _ = _isp_constants()
    alpha_proj_f  = float(alpha_proj)

    phi_fit = result.get("phi_empirical_rad", float("nan"))
    phi_alg = result.get("phi_algebraic_rad", float("nan"))  # φ_W
    m_start = result.get("m_start", 0.0)
    m_end   = result.get("m_end", 0.0)
    lp      = result.get("log_periods_covered", 0.0)

    if not (_m.isfinite(phi_fit) and _m.isfinite(phi_alg) and m_start > 0 and m_end > 0):
        return

    m_c = _m.sqrt(m_start * m_end)
    U   = 0.5 * _m.log(m_end / m_start) if m_end > m_start else 0.0

    print(f"\n── ISP PHASE HIERARCHY  (DSN §3.x.13 / §3.x.13a) ──")
    print(f"   α_proj = Π₀ = π − arctan(√15) = {_m.degrees(alpha_proj_f):.4f}°"
          f"  [ALG structure]")
    print()

    # Formula comparison: φ_W + Π₀ vs φ*_fit
    pred_deg = (_m.degrees(phi_alg) + _m.degrees(alpha_proj_f)) % 360
    fit_deg  = _m.degrees(phi_fit) % 360
    gap_deg  = ((fit_deg - pred_deg + 180) % 360) - 180  # signed shorter arc
    print(f"   φ_W (§5.10 formula)           = {_m.degrees(phi_alg) % 360:.4f}°")
    print(f"   φ_W + Π₀  (predicted φ*_Q)    = {pred_deg:.4f}°")
    print(f"   φ*_fit    (measured)           = {fit_deg:.4f}°")
    print(f"   Gap = φ*_fit − (φ_W + Π₀)     = {gap_deg:+.4f}°  ({_m.radians(gap_deg):.4f} rad)")
    if abs(gap_deg) < 2.0:
        print(f"   → Gap within 2° — Π₀ captures dominant projection  ✓")
    elif abs(gap_deg) < 10.0:
        print(f"   → Gap 2°–10° — O(Q₀) correction to Π expected (task 9 [OPEN])")
    else:
        print(f"   → Gap > 10° — pre-asymptotic window bias likely dominant")

    # Alias correction (only meaningful for short windows)
    if lp < 0.99 and U > 0:
        corr = alias_phase_correction(phi_fit, m_c, U, tau_val)
        phi_naive_deg = corr["phi_true_naive_deg"] % 360
        print()
        print(f"   Window spans {lp:.3f} log-periods (< 1.00 — alias correction relevant)")
        print(f"   m_c (window geometric mean)    = {m_c:.0f} blocks")
        print(f"   τ·ln(m_c)                      = {_m.degrees(corr['tau_ln_mc']) % 360:.3f}°")
        print(f"   φ*_fit − τ·ln(m_c)  (naive)   = {phi_naive_deg:.4f}°")
        print(f"   |G₋(U)|  (alias strength)      = {corr['alias_G_abs']:.4f}")
        print(f"   Note: 10% rate excess over τ is [OBS+HEUR] — pre-asymptotic")
        print(f"         secondary mode; decays as run length increases.")
    elif lp >= 0.99:
        print(f"   Window spans ≥ 1 log-period — alias correction suppressed ✓")
        print(f"   φ*_fit is alias-free; use directly as φ*_Q,true estimate.")


# =============================================================================
# Args
# =============================================================================
def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="RTG dyad audit — DSN v5.0  (ISP layer: Θ, sectors, overshoot, alias correction)"
    )
    p.add_argument("--rho0",           type=str, required=True)
    p.add_argument("--eta0",           type=str, required=True)
    p.add_argument("--p2-eigvec",      action="store_true")
    p.add_argument("--p2-eigvec-eps",  type=str, default="1e-20")
    p.add_argument("--steps",          type=int, default=1000)
    p.add_argument("--dps",            type=int, default=80)
    p.add_argument("--print-every",    type=int, default=50)
    p.add_argument("--asymp-window",   type=int, default=100)
    p.add_argument("--csv",            type=str, default="")
    p.add_argument("--csv-stride",     type=int, default=1)
    p.add_argument("--stop-on-flag",   action="store_true")
    p.add_argument("--show-q6-live",   action="store_true")
    # [v2.3-CNV-1] Convergence thresholds
    p.add_argument("--converge-tol",   type=str, default="0.005")
    p.add_argument("--c-spread-tol",   type=str, default="50")
    # [v2.4-ONSET-1]
    p.add_argument("--q-onset-thr",    type=str, default="2.0")
    # [v2.3-ARG-1] Universality comparison
    p.add_argument("--prior-alpha",    type=str, default="")
    p.add_argument("--near-fp-tol",    type=str, default="1e-30")
    p.add_argument("--crit-tol",       type=str, default="1e-30")
    p.add_argument("--rho-warn",       type=str, default="5.0")
    p.add_argument("--drift-warn",     type=str, default="100.0")
    p.add_argument("--q-growth-warn",  type=str, default="10.0")
    p.add_argument("--q6-growth-warn", type=str, default="10.0")
    p.add_argument("--p2-escape-radius", type=str, default="0.1")
    # === NEW v4.5 FLAGS ===
    p.add_argument("--joint-fit",      action="store_true",
                   help="[v4.5] Enable joint nonlinear fit of (κ, Ã, φ*) "
                        "on deep asymptotic tail. Requires scipy.")
    p.add_argument("--window-ratio",   type=float, default=230.0,
                   help="[v4.5] Deep-window ratio for φ* extraction. "
                        "Default 230 ensures Δln m ≥ 2π/τ ≈ 5.44. "
                        "One log-period coverage also enforced independently.")
    p.add_argument("--extract-phi-star", action="store_true",
                   help="[v4.5] After simulation, extract empirical φ* via "
                        "joint fit and compare to DSN §5.10 algebraic formula. "
                        "Requires --joint-fit and scipy.")
    # === NEW v4.5.4 FLAGS ===
    p.add_argument("--phi-star-m-start", type=float, default=None,
                   help="[v4.5.4] Manual window start in BLOCK units (m = n/6). "
                        "When set, bypasses automatic [2κ,100κ] window selection. "
                        "Use to compare φ* at identical m-ranges across Q₀ values. "
                        "Log-period floor and 500-block floor still applied.")
    p.add_argument("--phi-star-m-end",   type=float, default=None,
                   help="[v4.5.4] Manual window end in BLOCK units. "
                        "Requires --phi-star-m-start. Default: end of run.")
    # === NEW v5.0 FLAGS ===
    p.add_argument("--isp-report",     action="store_true",
                   help="[v5.0] Print ISP Structural Report: Θ distribution, "
                        "sector fractions, pre-crossing footprint, overshoot "
                        "ceiling check, and alias-function phase correction. "
                        "Auto-enabled when --joint-fit is active.")
    # === Birth / Φ_{2→3} markers + regime classifier [v6.0-BIRTH-1] ===
    p.add_argument("--birth-threshold", type=str, default=BIRTH_THRESHOLD_DEFAULT,
                   help="[HEUR default 0.6594477844] Q_s fracture/escape horizon. "
                        "Backed by TRIAD-T4h reduced Race-A [NUM diagnostic]; NOT a "
                        "certified fracture trigger.")
    p.add_argument("--birth-threshold-source", type=str,
                   default="TRIAD-T4h reduced Race-A NUM diagnostic / HEUR operational default",
                   help="Provenance string stamped into the CSV.")
    p.add_argument("--birth-action", type=str, default="warn",
                   choices=["off", "warn", "stop"],
                   help="off: markers only; warn (default): markers + one-time stderr "
                        "notice on first crossing; stop: halt at first crossing "
                        "(certified-isolated-window production scans only).")
    p.add_argument("--birth-marker-mode", type=str, default="both",
                   choices=["none", "shear", "recoil", "both"],
                   help="Which candidate Q_c policy amplitude(s) to log (default both; "
                        "κ is not physically selected, Genesis §6.3 [COR]).")
    p.add_argument("--cycle-csv", type=str, default="",
                   help="[v6.0] Separate per-cycle (6-step strobe) CSV with regime "
                        "classifier, backbone residual, and alignment onset. Kept "
                        "distinct from the per-step CSV (SG-2: no step/block mixing).")
    p.add_argument("--regime-tol", type=str, default="0.05",
                   help="[v6.0] |scaled backbone residual| tolerance for alignment.")
    p.add_argument("--regime-k", type=int, default=10,
                   help="[v6.0] consecutive aligned blocks required to declare onset.")
    p.add_argument("--regime-window-frac", type=float, default=0.2,
                   help="[v6.0] trailing fraction of blocks used to fit κ for the "
                        "backbone reference (SG-7 window-stamped).")
    return p.parse_args()


# =============================================================================
# Main
# =============================================================================

def main() -> int:
    args = parse_args()
    mp.mp.dps = args.dps

    p2_init_eps: Optional[mp.mpf] = None
    if args.p2_eigvec:
        eps        = parse_expr(args.p2_eigvec_eps)
        p2_init_eps = eps
        v_u, _     = p2_eigenvectors()
        rho0 = mp.mpf("0") + eps * v_u[0]
        eta0 = mp.pi        + eps * v_u[1]
        args.rho0  = mp.nstr(rho0, 8)
        args.eta0  = mp.nstr(eta0, 8)
    else:
        rho0 = parse_expr(args.rho0)
        eta0 = parse_expr(args.eta0)

    near_fp_tol    = parse_expr(args.near_fp_tol)
    crit_tol       = parse_expr(args.crit_tol)
    rho_warn       = parse_expr(args.rho_warn)
    drift_warn     = parse_expr(args.drift_warn)
    q_growth_warn  = parse_expr(args.q_growth_warn)
    q6_growth_warn = parse_expr(args.q6_growth_warn)
    p2_escape_radius = parse_expr(args.p2_escape_radius)
    converge_tol   = parse_expr(args.converge_tol)
    c_spread_tol   = parse_expr(args.c_spread_tol)
    prior_alpha    = parse_expr(args.prior_alpha) if args.prior_alpha else None
    q_onset_thr    = parse_expr(args.q_onset_thr)
    discr_tol = mp.power(10, -(max(20, args.dps // 2)))

    # === Birth / regime params [v6.0-BIRTH-1] ===
    birth_threshold = parse_expr(args.birth_threshold)
    regime_tol      = parse_expr(args.regime_tol)
    csv_ctx = {
        "birth_threshold":        mp.nstr(birth_threshold, 20),
        "birth_action":           args.birth_action,
        "birth_threshold_source": args.birth_threshold_source,
    }
    birth_warned = False

    st = State(rho=rho0, eta=eta0)
    print_header(args)

    csv_file, writer = None, None
    if args.csv:
        csv_file = open(args.csv, "w", newline="", encoding="utf-8")
        writer   = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
        writer.writeheader()

    prev_uv_angle = None
    winding_accum = mp.mpf("0")
    prev_q = prev_q6 = None
    current_q6 = None
    q6_samples:     List[Tuple[int, mp.mpf]] = []
    winding_at_q6:  List[mp.mpf]             = []
    # [v5.0-ISP-TRACK-1] ISP (n, Q, sector, R_overshoot, Θ, is_primitive_precross)
    # 6-tuple: int, mp.mpf, str, Optional[mp.mpf], mp.mpf, bool
    isp_theta_samples: List[Tuple] = []

    first_obs = last_obs = None
    p2_escape_step: Optional[int] = None
    prev_near_p1 = prev_near_p2 = prev_escaped_p2 = False
    was_near_p2 = False

    try:
        for step in range(args.steps + 1):
            if step % 6 == 0 and step > 0:
                eta_wrap_tmp = wrap_pm_pi(st.eta)
                _, _, current_q6 = birkhoff_coords(st.rho, eta_wrap_tmp)
                q6_samples.append((step, current_q6))
                _record_wind = True
            else:
                _record_wind = False

            obs, prev_uv_angle, winding_accum = compute_obs(
                step=step, st=st,
                prev_uv_angle=prev_uv_angle,
                winding_accum=winding_accum,
                discr_tol=discr_tol,
                q6_current=current_q6,
            )

            if _record_wind:
                winding_at_q6.append(obs.winding_accum)
                # [v5.0-ISP-TRACK-1] 6-tuple: (n, Q, sector, R_overshoot, Θ, is_prim_precross)
                isp_theta_samples.append((
                    step, obs.q_true, obs.isp_sector,
                    obs.R_overshoot, obs.Theta, obs.is_primitive_precross
                ))

            if first_obs is None: first_obs = obs
            last_obs = obs

            flags = detect_flags(
                obs=obs, prev_q=prev_q, prev_q6=prev_q6,
                near_fp_tol=near_fp_tol, crit_tol=crit_tol,
                rho_warn=rho_warn, drift_warn=drift_warn,
                q_growth_warn=q_growth_warn, q6_growth_warn=q6_growth_warn,
                p2_escape_radius=p2_escape_radius, was_near_p2=was_near_p2,
            )
            if flags.near_p2: was_near_p2 = True

            # --- Birth / Φ_{2→3} passive markers + P2-escape flag [v6.0-BIRTH-1] ---
            p2_escaped_now = flags.escaped_p2_band or (p2_escape_step is not None)
            annotate_birth_and_escape(
                obs, birth_threshold, args.birth_marker_mode, p2_escaped_now
            )
            if (obs.birth_regime_entered and not birth_warned
                    and args.birth_action in ("warn", "stop")):
                birth_warned = True
                import sys
                print(
                    f"\n⚠ [v6.0-BIRTH] Q_s={mp.nstr(obs.Q_s, 8)} ≥ birth_threshold="
                    f"{mp.nstr(birth_threshold, 8)} at step {step}.\n"
                    f"  Entered birth/escape regime [HEUR; TRIAD-T4h reduced Race-A NUM].\n"
                    f"  Isolated-dyad observables beyond here are EXTRAPOLATION "
                    f"(not certified). Certified J_Q cascade route is obstructed.",
                    file=sys.stderr,
                )

            if writer is not None and (step % args.csv_stride == 0 or step == args.steps):
                write_csv_row(writer, obs, csv_ctx)

            state_transition = (
                (flags.near_p1    and not prev_near_p1)
                or (flags.near_p2 and not prev_near_p2)
                or (flags.escaped_p2_band and not prev_escaped_p2)
            )
            if p2_escape_step is None and flags.escaped_p2_band:
                p2_escape_step = step

            prev_near_p1    = flags.near_p1
            prev_near_p2    = flags.near_p2
            prev_escaped_p2 = flags.escaped_p2_band

            if (step == 0 or step % args.print_every == 0
                    or flags.alert() or state_transition):
                print_obs(obs, flags, show_q6=args.show_q6_live)

            if args.stop_on_flag and step > 0 and flags.any_set():
                print("\nStopped: stop-on-flag.")
                break

            if (args.birth_action == "stop" and step > 0
                    and obs.birth_regime_entered):
                print(f"\nStopped: birth-action=stop at Q_s ≥ birth_threshold "
                      f"(step {step}).")
                break

            prev_q = obs.q_true
            if obs.q6_true is not None: prev_q6 = obs.q6_true
            if step < args.steps: st = dyad_step(st)

    finally:
        if csv_file is not None: csv_file.close()

    assert first_obs is not None and last_obs is not None
    print_summary(
        first_obs=first_obs, last_obs=last_obs,
        q6_samples=q6_samples,
        winding_at_q6=winding_at_q6,
        asymp_window=args.asymp_window,
        p2_escape_step=p2_escape_step,
        p2_init_eps=p2_init_eps,
        converge_tol=converge_tol,
        c_spread_tol=c_spread_tol,
        prior_alpha=prior_alpha,
        q_onset_thr=q_onset_thr,
    )

    # =========================================================================
    # NEW v4.5: Joint φ* extraction  [v4.5-JOINT-1 / v4.5-PHI-1]
    # =========================================================================
    if args.extract_phi_star and args.joint_fit:
        if not _SCIPY_AVAILABLE:
            print("\n⚠ --extract-phi-star requested but numpy/scipy not available.")
            print("  Install with: pip install scipy")
        elif len(q6_samples) < 1000:
            print(f"\n⚠ --extract-phi-star: only {len(q6_samples)} 6-step samples collected.")
            print("  Need ≥ 1000 blocks for a meaningful joint fit.")
            print(f"  Minimum recommended run: --steps {6 * 1000 * int(args.window_ratio)}")
        else:
            # Q₀ = initial Q_true (authoritative for all IC types)
            Q0_val  = float(first_obs.q_true)
            tau_val = float(2 * math.sqrt(3) / 3)

            # κ seed from Fit-A last-10% C_est / 6  (v4.5.1-KSEED-1, v4.5.2-KSEED-2)
            # C_est may be negative for above-approach ICs (M2 morphology) — that is
            # correct physics; kappa_seed = C_est/6 < 0 is the right seed.
            # Requiring kappa_seed > 0 was the v4.5.1 bug that collapsed the window.
            kappa_seed_val: Optional[float] = None
            try:
                _fr = asymptotic_fit_report(q6_samples, winding_at_q6)
                _c  = _fr.get(0.1)
                if _c is not None:
                    _c_est = float(_c["fit_A"]["C_est"])
                    if math.isfinite(_c_est) and _c_est != 0.0:
                        kappa_seed_val = _c_est / 6.0
            except Exception:
                pass

            fit_result = joint_phi_star_fit(
                q6_samples        = q6_samples,
                tau               = tau_val,
                window_ratio      = args.window_ratio,
                Q0                = Q0_val,
                kappa_seed        = kappa_seed_val,
                spiral_crossings  = [float(t) for t, k in
                                     zero_crossing_report(q6_samples).get("all_crossings", [])
                                     if k == "SPIRAL"],
                m_win_lo_override = args.phi_star_m_start,
                m_win_hi_override = args.phi_star_m_end,
            )
            print_phi_star_extraction(fit_result, Q0=Q0_val, tau=tau_val)

    elif args.extract_phi_star and not args.joint_fit:
        print("\n⚠ --extract-phi-star requires --joint-fit to be set.")

    # =========================================================================
    # ISP STRUCTURAL REPORT  [v5.0-ISP-DIAG-1]
    # Auto-enabled when --joint-fit is active, or explicit --isp-report flag.
    # =========================================================================
    run_isp = getattr(args, "isp_report", False) or args.joint_fit
    if run_isp:
        print_isp_report(q6_samples, isp_theta_samples)

    # === Per-cycle regime classification + strobe CSV [v6.0-REGIME-1] ===
    if args.cycle_csv:
        rows, onset, win_lo, win_hi, kappa_fit, c_est = classify_regime_cycles(
            q6_samples, regime_tol, args.regime_k, args.regime_window_frac
        )
        if rows:
            write_cycle_csv(args.cycle_csv, rows)
            n_early = sum(1 for r in rows if r["regime"] == "early_ic_memory")
            n_late  = sum(1 for r in rows if r["regime"] == "late_aligned_backbone")
            n_unc   = sum(1 for r in rows if r["regime"] == "unclassified")
            print("\n" + "=" * 70)
            print("REGIME CLASSIFIER (observable-alignment only; NOT memory-erasure) "
                  "[v6.0]")
            print("=" * 70)
            print(f"  κ_fit = {mp.nstr(kappa_fit, 12)}   C_est = {mp.nstr(c_est, 12)}"
                  f"   (window n∈[{win_lo},{win_hi}], SG-7 stamped)")
            print(f"  alignment_onset_cycle = {onset if onset is not None else 'NONE'}"
                  f"   (tol={mp.nstr(regime_tol,6)}, k={args.regime_k})")
            print(f"  early_ic_memory={n_early}  late_aligned_backbone={n_late}  "
                  f"unclassified={n_unc}")
            print(f"  → per-cycle CSV written: {args.cycle_csv}")
        else:
            print("\n[v6.0-REGIME] insufficient 6-step blocks to classify regime.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())