#!/usr/bin/env python3
"""
rtg_dyad_audit.py  —  DSN v4.5 aligned

High-precision audit simulator for the isolated RTG dyadic map.

Map:
    rho' = rho - sin(eta)
    eta' = eta + (exp(rho) - 1) - sin(eta)

NEW IN v4.5 (OPEN 5 closure campaign):

  [v4.5-JOINT-1] joint_phi_star_fit() — nonlinear joint fit of (κ, Ã, φ*).
                  Model in block notation (m = n/6):
                      Q_m = 1/(m + κ) + Ã · m^{-3/2} · cos(τ · ln m + φ*)
                  Activated by --joint-fit flag.
                  Uses scipy.optimize.curve_fit on downsampled tail (≤2000 pts).
                  Bug corrected vs draft: model fits Q_m (not nQ_m) in block coords.
                  Requires scipy (pre-installed in repo environment).

  [v4.5-WIN-1]   --window-ratio (default 230) selects deep asymptotic tail.
                  Enforces Δ ln m ≥ 2π/τ ≈ 5.44 (one full log-period) regardless
                  of window-ratio setting. Both constraints applied simultaneously.

  [v4.5-PHI-1]   --extract-phi-star triggers comparison of empirical φ* (from
                  joint fit) against DSN §5.10 algebraic formula:
                      φ*(Q₀) = 2π/3 − τ ln(2 Q₀) + (τ/4) Q₀ + (τ/80) Q₀² + O(Q₀³)
                  τ = 2√3/3 exact; Q₀ = η₀² for canonical family (ρ₀=0, η₀>0).
                  Formula in block notation; φ* extracted in block notation.
                  Discrepancy reported mod 2π in both radians and degrees.

  Phase notation: all φ* values in this module are in BLOCK notation.
                  To convert to step notation: φ*_step = φ*_block − τ·ln 6.

Changes in v2.4.1 (approach_dir bug fix):

  [v2.4.1-APPDIR-1] transient_analysis() approach_dir fix.
                     Previous: used nq6_peak > 6 (first 20% of samples).
                     Bug: small-Q₀ below-approach ICs on long runs have their first
                     crossing within the first 20% window, making nq6_peak > 6 even
                     though the approach is genuinely from below (C_true > 0).
                     Fix: use nq6[0] (first 6-step sample value).
                       above: nq6[0] > 6 (large-Q₀ bursts above on first step)
                       below: nq6[0] < 6 (small-Q₀ starts near 0)
                     Downstream effects: correct KINEMATIC/SPIRAL labeling for
                     small-Q₀ ICs, correct winding debt interpretation.
                     DSN ⚠APPROACH_DIR_FIX.

Changes in v2.4 (exact constants, corrected basis, kinematic classification):

  [v2.4-CONST-1]  Exact algebraic constants block.
                   τ        = -Im(c₂₁) = 2√3/3
                   α_block  = τ/(2π) = √3/(3π)   ≈ 0.183776  [per 6-step block]
                   α_step   = α_block/6 = √3/(18π) ≈ 0.030629  [per step / Birkhoff twist]
                   R*       = exp(π/τ) = exp(3π/(2√3)) ≈ 15.19094  [exact crossing ratio]
                  All diagnostics now reference R* as primary target, with
                  the α-fit prediction exp(3/(6α)) as secondary.
                  DSN v2.4.1 §5.2 three-line α dictionary.

  [v2.4-BASIS-1]  spiral_phase_report() basis upgraded from
                   cos(2π·wind)/n  →  cos(τ·ln n)/√n
                   sin(2π·wind)/n  →  sin(τ·ln n)/√n
                  The O(n^{-1/2}) envelope is the correct asymptotic form
                  derived from the quintic correction (DSN v2.4.1 §5.4).
                  Closes ⊗O_PROJECTION_BASIS.
                  DSN ⚠BASIS_UPGRADE.

  [v2.4-KIN-1]   zero_crossing_report() now classifies each ASYMPTOTIC
                  crossing as KINEMATIC or SPIRAL based on approach direction.
                  DSN ≈A_KINEMATIC (v2.4).

  [v2.4-ONSET-1] transient_analysis() gains Q-based onset criterion alongside
                  the existing step-based rule.
                  DSN ⚠ONSET_Q_THRESHOLD.

  [v2.4-CEST-1]  Negative C_est handling in STATUS / n_eff block.
                  DSN ⊗O_C_SIGN.

  [v2.4-ALPHA-1] α output now reports all three quantities with exact labels.
                  Closes ⊗O_ALPHA_DERIVE.

Changes in v2.3 (large-IC transient classification & winding debt):
  [v2.3-TRN-1/2] transient_analysis(), zero_crossing_report() extensions.
  [v2.3-WND-1]   winding_debt_report().
  [v2.3-PD-1]    phase_deficit_report() updated.
  [v2.3-CNV-1]   Convergence STATUS reclassified.
  [v2.3-ARG-1]   New CLI args.

Inherited from v2.2:
  [v2.2-FIT-1..5]  linear_regression, asymptotic_fit_report,
                    spiral_phase_report, phase_deficit_report,
                    zero_crossing_report.
  [v2.2-CSV-1]  Extended CSV fields.
  [v2.2-WIN-1]  Multi-window C-drift table.

Inherited from v2.1:
  [v2.1-FIX-1]  Q_euc demoted to comparison diagnostic only.
  [v2.1-NEW-1]  --p2-eigvec mode.
  [v2.1-NEW-2]  Theoretical escape-time prediction.
  [v2.1-NEW-3]  Asymptotic-C rolling window tracker.
"""

from __future__ import annotations

import argparse
import ast
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
]


def write_csv_row(writer: csv.DictWriter, obs: Obs) -> None:
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
    })


# =============================================================================
# NEW v4.5: Joint (κ, Ã, φ*) nonlinear fit  [v4.5-JOINT-1]
# =============================================================================

def joint_phi_star_fit(
    q6_samples: List[Tuple[int, mp.mpf]],
    tau: float,
    window_ratio: float,
    Q0: float,
) -> Dict:
    """
    [v4.5-JOINT-1] Joint nonlinear fit of (κ, Ã, φ*) on deep asymptotic tail.

    Model in BLOCK notation (m = n/6):
        Q_m = 1/(m + κ) + Ã · m^{-3/2} · cos(τ · ln m + φ*)

    IMPORTANT CORRECTIONS vs draft (v4.5 specification):
    - Model fits Q_m directly (not nQ_m as in draft — that was a dimension error).
    - Block coordinates used throughout: m = n/6, Q_m from q6_samples.
    - Phase φ* is reported in BLOCK notation.
      Step-notation conversion: φ*_step = φ*_block − τ·ln 6.
    - Algebraic formula from DSN §5.10 is already in block notation.

    Window selection (two constraints, most conservative wins):
    1. Ratio: use last max(2000, total/window_ratio) blocks.
    2. Log-period: ensure ln(m_end/m_start) ≥ 2π/τ ≈ 5.44 (one full log-period).

    Downsamples to ≤2000 points for scipy speed while all reporting uses
    the full mpmath precision data.

    Returns dict with empirical φ*, algebraic §5.10 prediction, and discrepancy.
    φ* discrepancy is reported mod 2π, taking the shorter arc (≤ π).
    """
    if not _SCIPY_AVAILABLE:
        return {"status": "scipy_unavailable",
                "message": "numpy/scipy not installed; pip install scipy"}

    if len(q6_samples) < 1000:
        return {"status": "insufficient_data", "n_samples": len(q6_samples)}

    # --- Build block arrays (float64 for scipy) ---
    ms_all = np.array([float(n) / 6.0 for n, q in q6_samples], dtype=np.float64)
    Qs_all = np.array([float(q)         for n, q in q6_samples], dtype=np.float64)

    # --- Window selection: constraint 1 (ratio-based) ---
    n_total   = len(q6_samples)
    tail_len1 = max(2000, int(n_total / window_ratio))

    # --- Window selection: constraint 2 (log-period coverage) ---
    log_period    = 2.0 * math.pi / tau           # ≈ 5.441
    m_end         = ms_all[-1]
    m_start_lp    = m_end * math.exp(-log_period) # earliest m giving one log-period
    idx_lp        = int(np.searchsorted(ms_all, m_start_lp))
    tail_len2     = n_total - idx_lp              # blocks from m_start_lp onward

    # Use the larger tail (earlier start = more data = more conservative)
    tail_start = n_total - max(tail_len1, tail_len2)
    tail_start = max(0, tail_start)

    ms = ms_all[tail_start:]
    Qs = Qs_all[tail_start:]

    if len(ms) < 100:
        return {"status": "insufficient_tail",
                "tail_blocks": int(len(ms)),
                "message": "tail < 100 blocks after window constraints"}

    # --- Downsample to ≤2000 for scipy speed ---
    if len(ms) > 2000:
        idx_ds  = np.round(np.linspace(0, len(ms) - 1, 2000)).astype(int)
        ms_fit  = ms[idx_ds]
        Qs_fit  = Qs[idx_ds]
    else:
        ms_fit = ms
        Qs_fit = Qs

    # --- Model: Q_m = 1/(m + κ) + Ã · m^{-3/2} · cos(τ ln m + φ*) ---
    def model(m, kappa, A_tilde, phi_star):
        return 1.0 / (m + kappa) + A_tilde * m**(-1.5) * np.cos(tau * np.log(m) + phi_star)

    # --- Initial κ guess from naive estimator at final block ---
    kappa_guess = float(1.0 / Qs[-1] - ms[-1])
    if not math.isfinite(kappa_guess) or kappa_guess <= 0:
        kappa_guess = 1.0

    # --- Try four phase seeds to avoid local minima ---
    best_result  = None
    best_residual = math.inf
    two_pi = 2.0 * math.pi

    for phi_seed in [0.0, math.pi / 2, math.pi, 3 * math.pi / 2]:
        try:
            popt, pcov = curve_fit(
                model, ms_fit, Qs_fit,
                p0=[kappa_guess, 0.01, phi_seed],
                bounds=([0.0, -np.inf, -np.inf], [np.inf, np.inf, np.inf]),
                maxfev=20000,
                ftol=1e-12,
                xtol=1e-12,
            )
            residual = float(np.sum((model(ms_fit, *popt) - Qs_fit) ** 2))
            if residual < best_residual:
                best_residual = residual
                best_result   = (popt, pcov)
        except Exception:
            continue

    if best_result is None:
        return {"status": "fit_failed",
                "message": "curve_fit failed on all four phase seeds"}

    popt, pcov = best_result
    kappa_fit, A_fit, phi_raw = popt

    # Parameter uncertainties (1-sigma from covariance diagonal)
    try:
        perr = np.sqrt(np.diag(pcov))
    except Exception:
        perr = np.array([math.nan, math.nan, math.nan])

    # --- Normalise empirical φ* to [0, 2π) ---
    phi_empirical_rad = phi_raw % two_pi
    phi_empirical_deg = math.degrees(phi_empirical_rad)

    # --- Algebraic prediction (DSN §5.10, block notation) ---
    # φ*(Q₀) = 2π/3 − τ ln(2 Q₀) + (τ/4) Q₀ + (τ/80) Q₀² + O(Q₀³)
    phi_alg_raw = (
        (2.0 * math.pi / 3.0)
        - tau * math.log(2.0 * Q0)
        + (tau / 4.0) * Q0
        + (tau / 80.0) * Q0 * Q0
    )
    phi_alg_rad = phi_alg_raw % two_pi
    phi_alg_deg = math.degrees(phi_alg_rad)

    # --- Discrepancy mod 2π, shorter arc (≤ π) ---
    diff_rad = abs(phi_empirical_rad - phi_alg_rad)
    if diff_rad > math.pi:
        diff_rad = two_pi - diff_rad
    diff_deg = math.degrees(diff_rad)

    # --- Coverage diagnostics ---
    ln_coverage       = math.log(ms[-1] / ms[0]) if ms[0] > 0 else 0.0
    log_periods_covered = ln_coverage / log_period

    return {
        "status":                "success",
        # Fit parameters
        "kappa_fit":             float(kappa_fit),
        "kappa_err":             float(perr[0]),
        "A_fit":                 float(A_fit),
        "A_err":                 float(perr[1]),
        "phi_empirical_rad":     float(phi_empirical_rad),
        "phi_empirical_deg":     float(phi_empirical_deg),
        "phi_raw_err_rad":       float(perr[2]),
        # Algebraic comparison
        "phi_algebraic_rad":     float(phi_alg_rad),
        "phi_algebraic_deg":     float(phi_alg_deg),
        "discrepancy_rad":       float(diff_rad),
        "discrepancy_deg":       float(diff_deg),
        # Fit quality
        "residual_ss":           float(best_residual),
        # Window info
        "window_points":         int(len(ms_fit)),
        "tail_blocks":           int(len(ms)),
        "m_start":               float(ms[0]),
        "m_end":                 float(ms[-1]),
        "ln_coverage":           float(ln_coverage),
        "log_periods_covered":   float(log_periods_covered),
        "window_ratio_used":     float(window_ratio),
    }


def print_phi_star_extraction(
    result: Dict,
    Q0: float,
    tau: float,
) -> None:
    """[v4.5-PHI-1] Print joint φ* extraction report."""
    print("\n" + "=" * 78)
    print("JOINT φ* EXTRACTION  (DSN v4.5 §5.10)  [v4.5-JOINT-1 / v4.5-PHI-1]")
    print("=" * 78)
    print(f"  Q₀ = η₀²          : {Q0:.10f}")
    print(f"  τ  (exact)         : {tau:.10f}  (= 2√3/3)")
    print()

    if result["status"] != "success":
        print(f"  ✗ Fit did not succeed: {result.get('message', result['status'])}")
        return

    print(f"  Window             : {result['tail_blocks']} blocks"
          f"  [{result['m_start']:.1f} ≤ m ≤ {result['m_end']:.1f}]")
    print(f"  Fit points         : {result['window_points']}  (downsampled)")
    print(f"  Log-period coverage: {result['log_periods_covered']:.3f}  "
          f"(need ≥ 1.00 for clean φ* extraction)")
    if result["log_periods_covered"] < 1.0:
        print("  ⚠ Window spans < 1 log-period — φ* extraction may be unreliable.")
    print()

    print(f"  κ_fit              : {result['kappa_fit']:.8f}"
          f"  ± {result['kappa_err']:.2e}")
    print(f"  |Ã|                : {abs(result['A_fit']):.6e}"
          f"  ± {result['A_err']:.2e}")
    print()

    print(f"  φ* empirical (fit) : {result['phi_empirical_rad']:.8f} rad"
          f"  = {result['phi_empirical_deg']:.4f}°")
    print(f"  φ* algebraic §5.10 : {result['phi_algebraic_rad']:.8f} rad"
          f"  = {result['phi_algebraic_deg']:.4f}°")
    print(f"  Discrepancy        : {result['discrepancy_rad']:.6f} rad"
          f"  = {result['discrepancy_deg']:.4f}°  (mod 2π, shorter arc)")
    print()

    # Assess agreement
    d = result["discrepancy_deg"]
    if d < 1.0:
        verdict = "✓ EXCELLENT  — O(Q₀) correction confirmed to < 1°."
    elif d < 5.0:
        verdict = "~  GOOD  — residual likely from O(Q₀²) terms or detector offset."
    elif d < 20.0:
        verdict = "⚠  PARTIAL  — O(Q₀²) or higher-order burst corrections needed."
    else:
        verdict = "✗  LARGE DISCREPANCY  — check run length, window, or Q₀ range."

    print(f"  Verdict            : {verdict}")
    print()

    # Noise on φ* parameter
    if result.get("phi_raw_err_rad", 0) < 0.1:
        print(f"  φ* fit uncertainty : {result['phi_raw_err_rad']:.4f} rad"
              f"  (1σ from covariance)")
    else:
        print(f"  ⚠ φ* fit uncertainty is large ({result['phi_raw_err_rad']:.4f} rad)"
              f" — window may be too short or spiral contamination dominant.")

    print()
    print("  Note: φ* in BLOCK notation (m = n/6).")
    print(f"  Step-notation conversion: φ*_step = φ*_block − τ·ln 6"
          f"  ≈ φ*_block − {tau * math.log(6):.6f} rad")


# =============================================================================
# Printing
# =============================================================================

def print_header(args: argparse.Namespace) -> None:
    print("=" * 78)
    print("RTG DYAD AUDIT SIMULATOR  —  DSN v4.5")
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
        if c_spread < mp.mpf("50"):
            print("   ✓ C_est stable — asymptotic regime fully established.")
        elif c_spread < mp.mpf("500"):
            print("   ~ C_est drifting (late transient, nearly converged).")
        else:
            print("   ⚠ C_est strongly drifting — TRANSIENT ONGOING.")
            print(f"     Require n >> |C_est(10%)| ≈ {mpstr(abs(c_ests[0]),6)} steps.")
        c_est_late = c_ests[0]
        n_eff = n_final - float(c_est_late)
        if float(c_est_late) < 0:
            print(f"   n_eff = n_final − C_est(10%) = {n_final} − ({mpstr(c_est_late,6)}) = {n_eff:.0f}  (above-approach: n_eff > n_final)")
        else:
            print(f"   n_eff = n_final − C_est(10%) = {n_final} − {mpstr(c_est_late,6)} = {n_eff:.0f}")
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


# =============================================================================
# Args
# =============================================================================

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="RTG dyad audit — DSN v4.5  (joint-fit + φ* extraction)"
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

            if writer is not None and (step % args.csv_stride == 0 or step == args.steps):
                write_csv_row(writer, obs)

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
            # Q₀ = η₀² for canonical family (ρ₀=0, η₀>0)
            # Use initial Q_true from first observation as authoritative Q₀
            Q0_val = float(first_obs.q_true)
            tau_val = float(2 * math.sqrt(3) / 3)

            fit_result = joint_phi_star_fit(
                q6_samples   = q6_samples,
                tau          = tau_val,
                window_ratio = args.window_ratio,
                Q0           = Q0_val,
            )
            print_phi_star_extraction(fit_result, Q0=Q0_val, tau=tau_val)

    elif args.extract_phi_star and not args.joint_fit:
        print("\n⚠ --extract-phi-star requires --joint-fit to be set.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
