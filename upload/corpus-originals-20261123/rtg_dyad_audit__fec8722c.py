#!/usr/bin/env python3
"""
rtg_dyad_audit.py  —  DSN v2.1 aligned

High-precision audit simulator for the isolated RTG dyadic map.

Map:
    rho' = rho - sin(eta)
    eta' = eta + (exp(rho) - 1) - sin(eta)

Changes from previous version (aligned with RTG_DYAD_AUDIT_DSN_v2.1):

  [v2.1-FIX-1]  Q_euc is a comparison-only diagnostic; Q_true is the sole
                 primary radial observable.  (DSN ⊕T3, CLOSURE-1)

  [v2.1-NEW-1]  --p2-eigvec mode: initialise perturbation along the exact
                 unstable eigenvector of P2 rather than raw (rho, eta) coords.
                 Required for clean O1 escape-time prefactor measurement.
                 (DSN ⊗O1)

  [v2.1-NEW-2]  Theoretical escape-time prediction T_theory printed alongside
                 measured escape step whenever P2 escape is detected.
                 (DSN ≈A1, V6)

  [v2.1-NEW-3]  Asymptotic-C tracker: rolling window mean/std of nQ6 samples
                 printed in summary, supporting approach to C ≈ 6.
                 (DSN ≈A4, ⊗O2, controlled by --asymp-window)

  [v2.1-DOC-1]  birkhoff_coords docstring corrected to use eta_wrap notation.
  [v2.1-DOC-2]  P2 eigenvalue noted as lambda+ = phi^2 (golden ratio squared).
  [v2.1-DOC-3]  Version banner updated.
"""

from __future__ import annotations

import argparse
import ast
import csv
import math
from dataclasses import dataclass
from typing import List, Optional, Tuple

import mpmath as mp


# =============================================================================
# Safe symbolic parser
# =============================================================================

_ALLOWED_NAMES = {
    "pi":  lambda: mp.pi,
    "e":   lambda: mp.e,
    "phi": lambda: (1 + mp.sqrt(5)) / 2,
}

_ALLOWED_FUNCS = {
    "sqrt": mp.sqrt,
    "sin":  mp.sin,
    "cos":  mp.cos,
    "tan":  mp.tan,
    "asin": mp.asin,
    "acos": mp.acos,
    "atan": mp.atan,
    "exp":  mp.exp,
    "log":  mp.log,
}


def parse_expr(expr: str) -> mp.mpf:
    """Safely parse a small arithmetic expression into an mp.mpf."""
    tree = ast.parse(expr, mode="eval")

    def _eval(node):
        if isinstance(node, ast.Expression):
            return _eval(node.body)
        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return mp.mpf(str(node.value))
            raise ValueError(f"Unsupported constant: {node.value!r}")
        if isinstance(node, ast.Name):
            if node.id in _ALLOWED_NAMES:
                return _ALLOWED_NAMES[node.id]()
            raise ValueError(f"Unknown symbol: {node.id}")
        if isinstance(node, ast.BinOp):
            left  = _eval(node.left)
            right = _eval(node.right)
            ops = {
                ast.Add:  lambda a, b: a + b,
                ast.Sub:  lambda a, b: a - b,
                ast.Mult: lambda a, b: a * b,
                ast.Div:  lambda a, b: a / b,
                ast.Pow:  lambda a, b: a ** b,
            }
            op_fn = ops.get(type(node.op))
            if op_fn is None:
                raise ValueError(f"Unsupported binary operator: {type(node.op).__name__}")
            return op_fn(left, right)
        if isinstance(node, ast.UnaryOp):
            val = _eval(node.operand)
            if isinstance(node.op, ast.UAdd): return val
            if isinstance(node.op, ast.USub): return -val
            raise ValueError(f"Unsupported unary operator: {type(node.op).__name__}")
        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Only simple function calls are allowed")
            name = node.func.id
            if name not in _ALLOWED_FUNCS:
                raise ValueError(f"Function not allowed: {name}")
            if node.keywords:
                raise ValueError("Keyword arguments not allowed")
            return _ALLOWED_FUNCS[name](*[_eval(a) for a in node.args])
        raise ValueError(f"Unsupported expression node: {type(node).__name__}")

    return _eval(tree)


# =============================================================================
# Utility
# =============================================================================

def wrap_pm_pi(x: mp.mpf) -> mp.mpf:
    """Wrap angle to (-pi, pi]."""
    two_pi = 2 * mp.pi
    y = mp.fmod(x + mp.pi, two_pi)
    if y < 0:
        y += two_pi
    y -= mp.pi
    if y <= -mp.pi:
        y += two_pi
    return y


def mpstr(x: mp.mpf, n: int = 16) -> str:
    return mp.nstr(x, n)


def euclid_dist(a: mp.mpf, b: mp.mpf) -> mp.mpf:
    return mp.sqrt(a * a + b * b)


# =============================================================================
# P2 eigenvector utilities   [v2.1-NEW-1]
# =============================================================================
#
# J(P2) = [[1, 1], [1, 2]]
# Characteristic polynomial: lambda^2 - 3*lambda + 1 = 0
# lambda+ = (3 + sqrt(5)) / 2  =  phi^2  ≈ 2.6180339887...   (unstable)
# lambda- = (3 - sqrt(5)) / 2  =  1/phi^2 ≈ 0.3819660113...  (stable)
#
# Unstable eigenvector (unnormalised): v = (1, lambda+ - 1) = (1, phi^2 - 1)
#   since (lambda+ - 1) = (1 + sqrt(5))/2 = phi
# Normalised: v_u = (1, phi) / ||(1, phi)||
#
# Stable eigenvector (unnormalised): v = (1, lambda- - 1) = (1, -1/phi)
# Normalised: v_s = (1, -1/phi) / ||(1, -1/phi)||

def p2_eigenvectors() -> Tuple[Tuple[mp.mpf, mp.mpf], Tuple[mp.mpf, mp.mpf]]:
    """
    Return (unstable_unit_vec, stable_unit_vec) for the P2 = (0, pi) saddle.

    Each vector is in (delta_rho, delta_eta) coordinates relative to P2.
    DSN v2.1 ⊕T2, ⊗O1.
    """
    phi = (1 + mp.sqrt(5)) / 2      # golden ratio
    lam_plus  = (3 + mp.sqrt(5)) / 2  # = phi^2

    # Unstable: direction (1, lam+ - 1) = (1, phi)
    u_rho = mp.mpf("1")
    u_eta = lam_plus - 1             # = phi
    norm_u = mp.sqrt(u_rho**2 + u_eta**2)
    v_unstable = (u_rho / norm_u, u_eta / norm_u)

    # Stable: direction (1, lam- - 1) = (1, -1/phi)
    lam_minus = (3 - mp.sqrt(5)) / 2
    s_rho = mp.mpf("1")
    s_eta = lam_minus - 1            # = -1/phi
    norm_s = mp.sqrt(s_rho**2 + s_eta**2)
    v_stable = (s_rho / norm_s, s_eta / norm_s)

    return v_unstable, v_stable


def p2_escape_theory(eps: mp.mpf) -> mp.mpf:
    """
    Theoretical escape time from P2 for perturbation amplitude eps.

        T_theory = ln(1/eps) / ln(lambda+)
                 ≈ 1.039043... * ln(1/eps)

    DSN v2.1 ≈A1.
    """
    lam_plus = (3 + mp.sqrt(5)) / 2
    if eps <= 0:
        return mp.inf
    return mp.log(1 / eps) / mp.log(lam_plus)


# =============================================================================
# Map state and observables
# =============================================================================

@dataclass
class State:
    rho: mp.mpf
    eta: mp.mpf   # lifted angle


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
    q_euclid: mp.mpf          # comparison diagnostic only (DSN ⊕T5, ⚠C1)
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
    # --- persistent state flags (printed once on transition, not every step) ---
    near_p1: bool = False
    near_p2: bool = False
    escaped_p2_band: bool = False

    # --- transient alert flags (always override --print-every) ---
    near_critical_curve: bool = False
    large_positive_rho: bool = False
    large_negative_rho: bool = False
    huge_drift: bool = False
    q_jump: bool = False
    q6_jump: bool = False

    def alert(self) -> bool:
        """True if any transient alert flag is set (overrides --print-every)."""
        return any([
            self.near_critical_curve,
            self.large_positive_rho,
            self.large_negative_rho,
            self.huge_drift,
            self.q_jump,
            self.q6_jump,
        ])

    def any_set(self) -> bool:
        """True if any flag is set (used for --stop-on-flag)."""
        return any(vars(self).values())


def dyad_step(st: State) -> State:
    s = mp.sin(st.eta)
    rho_next = st.rho - s
    eta_next = st.eta + (mp.exp(st.rho) - 1) - s
    return State(rho_next, eta_next)


def birkhoff_coords(rho: mp.mpf, eta_wrap: mp.mpf) -> Tuple[mp.mpf, mp.mpf, mp.mpf]:
    """
    Birkhoff (Euclidean) coordinates for the P1 elliptic resonance.

    The linearised map at P1 = (0,0) is a 60° rotation in these coordinates:

        u = rho - eta_wrap / 2
        v = (sqrt(3) / 2) * eta_wrap

    Primary radial invariant (DSN v2.1 ⊕T3, CLOSURE-1):

        Q_true = u^2 + v^2
               = rho^2 - rho*eta_wrap + eta_wrap^2

    NOTE: Q_euc = rho^2 + eta_wrap^2 is kept only as a comparison diagnostic
    and must NOT be used as the primary radial observable (DSN ⚠C1).
    """
    u = rho - eta_wrap / 2
    v = (mp.sqrt(3) / 2) * eta_wrap
    q_true = u * u + v * v
    return u, v, q_true


def euclid_q(rho: mp.mpf, eta_wrap: mp.mpf) -> mp.mpf:
    """Q_euc — comparison diagnostic only. See DSN v2.1 ⚠C1."""
    return rho * rho + eta_wrap * eta_wrap


def jacobian_trace_det_discr(
    rho: mp.mpf, eta_lift: mp.mpf
) -> Tuple[mp.mpf, mp.mpf, mp.mpf]:
    c  = mp.cos(eta_lift)
    er = mp.exp(rho)
    tr   = 2 - c
    det  = 1 + (er - 1) * c
    discr = tr * tr - 4 * det
    return tr, det, discr


def classify_eigs(discr: mp.mpf, tol: mp.mpf) -> str:
    if discr > tol:  return "real"
    if discr < -tol: return "complex"
    return "degenerate"


def compute_obs(
    step: int,
    st: State,
    prev_uv_angle: Optional[mp.mpf],
    winding_accum: mp.mpf,
    discr_tol: mp.mpf,
    q6_current: Optional[mp.mpf],
) -> Tuple[Obs, mp.mpf, mp.mpf]:
    eta_wrap = wrap_pm_pi(st.eta)
    s = mp.sin(st.eta)
    c = mp.cos(st.eta)
    drift     = mp.exp(st.rho) - 1
    remainder = drift - st.rho

    u, v, q_true = birkhoff_coords(st.rho, eta_wrap)
    q_euclid     = euclid_q(st.rho, eta_wrap)

    tr, det_j, discr = jacobian_trace_det_discr(st.rho, st.eta)
    eig_kind = classify_eigs(discr, discr_tol)

    dist_p1 = euclid_dist(st.rho, eta_wrap)
    dist_p2 = euclid_dist(st.rho, wrap_pm_pi(eta_wrap - mp.pi))

    uv_angle = mp.mpf("0") if (u == 0 and v == 0) else mp.atan2(v, u)

    if prev_uv_angle is None:
        rot_inc = mp.mpf("0")
    else:
        rot_inc = wrap_pm_pi(uv_angle - prev_uv_angle)

    winding_next = winding_accum + rot_inc / (2 * mp.pi)

    n_times_q_true  = mp.mpf(step) * q_true if step > 0 else mp.mpf("0")
    n_times_q6_true = (
        mp.mpf(step) * q6_current
        if (q6_current is not None and step > 0 and step % 6 == 0)
        else None
    )

    obs = Obs(
        step=step,
        rho=st.rho, eta_lift=st.eta, eta_wrap=eta_wrap,
        sin_eta=s, cos_eta=c, drift=drift, remainder=remainder,
        u=u, v=v,
        q_true=q_true, q_euclid=q_euclid,
        tr_j=tr, det_j=det_j, discr=discr, eig_kind=eig_kind,
        dist_p1=dist_p1, dist_p2=dist_p2,
        rotation_increment=rot_inc, winding_accum=winding_next,
        n_times_q_true=n_times_q_true,
        q6_true=q6_current if (step % 6 == 0 and step > 0) else None,
        n_times_q6_true=n_times_q6_true,
    )
    return obs, uv_angle, winding_next


# =============================================================================
# Diagnostics
# =============================================================================

def detect_flags(
    obs: Obs,
    prev_q: Optional[mp.mpf],
    prev_q6: Optional[mp.mpf],
    near_fp_tol: mp.mpf,
    crit_tol: mp.mpf,
    rho_warn: mp.mpf,
    drift_warn: mp.mpf,
    q_growth_warn: mp.mpf,
    q6_growth_warn: mp.mpf,
    p2_escape_radius: mp.mpf,
    was_near_p2: bool,
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
        if obs.q_true / prev_q > q_growth_warn:
            flags.q_jump = True
    if prev_q6 is not None and obs.q6_true is not None and prev_q6 != 0:
        if obs.q6_true / prev_q6 > q6_growth_warn:
            flags.q6_jump = True
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
# Asymptotic-C tracker   [v2.1-NEW-3]
# =============================================================================

def asymptotic_c_stats(
    q6_samples: List[Tuple[int, mp.mpf]],
    window: int,
) -> Optional[Tuple[mp.mpf, mp.mpf, mp.mpf, int]]:
    """
    Compute mean, std, and linear trend slope of n*Q6_true over the last
    `window` 6-step samples.

    Returns (mean_nQ6, std_nQ6, slope_per_sample, count) or None if < 2 samples.
    DSN v2.1 ≈A4, ⊗O2: tracks convergence of empirical C toward ~6.
    """
    tail = q6_samples[-window:] if len(q6_samples) >= window else q6_samples
    if len(tail) < 2:
        return None
    vals = [mp.mpf(n) * q for n, q in tail]
    count = len(vals)
    mean = sum(vals) / count
    variance = sum((v - mean) ** 2 for v in vals) / (count - 1)
    std = mp.sqrt(variance)

    # Linear trend: slope via simple linear regression over index
    xs = [mp.mpf(i) for i in range(count)]
    x_mean = sum(xs) / count
    num = sum((xs[i] - x_mean) * (vals[i] - mean) for i in range(count))
    den = sum((x - x_mean) ** 2 for x in xs)
    slope = num / den if den != 0 else mp.mpf("0")

    return mean, std, slope, count


# =============================================================================
# CSV
# =============================================================================

CSV_FIELDS = [
    "step", "rho", "eta_lift", "eta_wrap", "sin_eta", "cos_eta",
    "drift", "remainder", "u", "v",
    "Q_true", "Q_euclid",           # Q_euclid = comparison diagnostic only
    "nQ_true", "Q6_true", "nQ6_true",
    "trJ", "detJ", "discr", "eig_kind",
    "dist_P1", "dist_P2", "rotation_increment", "winding_accum",
]


def write_csv_row(writer: csv.DictWriter, obs: Obs) -> None:
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
        "nQ_true":            mp.nstr(obs.n_times_q_true, 50),
        "Q6_true":            "" if obs.q6_true is None else mp.nstr(obs.q6_true, 50),
        "nQ6_true":           "" if obs.n_times_q6_true is None else mp.nstr(obs.n_times_q6_true, 50),
        "trJ":                mp.nstr(obs.tr_j, 50),
        "detJ":               mp.nstr(obs.det_j, 50),
        "discr":              mp.nstr(obs.discr, 50),
        "eig_kind":           obs.eig_kind,
        "dist_P1":            mp.nstr(obs.dist_p1, 50),
        "dist_P2":            mp.nstr(obs.dist_p2, 50),
        "rotation_increment": mp.nstr(obs.rotation_increment, 50),
        "winding_accum":      mp.nstr(obs.winding_accum, 50),
    })


# =============================================================================
# Printing
# =============================================================================

def print_header(args: argparse.Namespace) -> None:
    print("=" * 78)
    print("RTG DYAD AUDIT SIMULATOR  —  DSN v2.1 aligned")
    print("=" * 78)
    print(f"dps                 : {mp.mp.dps}")
    print(f"steps               : {args.steps}")
    print(f"rho0                : {args.rho0}")
    print(f"eta0                : {args.eta0}")
    if args.p2_eigvec:
        eps = parse_expr(args.p2_eigvec_eps)
        t_theory = p2_escape_theory(eps)
        v_u, _ = p2_eigenvectors()
        print(f"p2_eigvec_mode      : ON  (eps={args.p2_eigvec_eps})")
        print(f"  unstable eigvec   : ({mpstr(v_u[0],8)}, {mpstr(v_u[1],8)})")
        print(f"  T_theory          : {mpstr(t_theory, 10)} steps  "
              f"[= ln(1/eps)/ln(phi^2)]")
    print(f"print_every         : {args.print_every}")
    print(f"csv                 : {args.csv if args.csv else '(none)'}")
    print(f"csv_stride          : {args.csv_stride}")
    print(f"asymp_window        : {args.asymp_window}")
    print(f"stop_on_flag        : {args.stop_on_flag}")
    print("=" * 78)
    print("NOTE: Q_euclid is a COMPARISON DIAGNOSTIC ONLY (DSN v2.1 ⚠C1).")
    print("      All primary radial claims use Q_true only.")
    print("=" * 78)


def print_obs(obs: Obs, flags: Flags, show_q6: bool) -> None:
    line = (
        f"[{obs.step:7d}] "
        f"rho={mpstr(obs.rho, 12):>14}  "
        f"eta_wrap={mpstr(obs.eta_wrap, 12):>14}  "
        f"Qtrue={mpstr(obs.q_true, 12):>14}  "
        f"Qeuc={mpstr(obs.q_euclid, 12):>14}  "
        f"detJ={mpstr(obs.det_j, 12):>14}  "
        f"eig={obs.eig_kind:>9}  "
        f"wind={mpstr(obs.winding_accum, 8):>10}"
    )
    if show_q6 and obs.q6_true is not None:
        line += (f"  Q6={mpstr(obs.q6_true, 10):>12}"
                 f"  nQ6={mpstr(obs.n_times_q6_true, 10):>12}")
    line += f"  flags={format_flags(flags)}"
    print(line)


def print_summary(
    first_obs: Obs,
    last_obs: Obs,
    q6_samples: List[Tuple[int, mp.mpf]],
    asymp_window: int,
    p2_escape_step: Optional[int],
    p2_init_eps: Optional[mp.mpf],
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
    print(f"final eig_kind      : {last_obs.eig_kind}")
    print(f"dist to P1          : {mp.nstr(last_obs.dist_p1, 20)}")
    print(f"dist to P2          : {mp.nstr(last_obs.dist_p2, 20)}")

    # ------------------------------------------------------------------
    # P2 escape time: measured vs theoretical  [v2.1-NEW-2]
    # ------------------------------------------------------------------
    if p2_escape_step is not None:
        print(f"\nP2 escape measured  : step {p2_escape_step}")
        if p2_init_eps is not None and p2_init_eps > 0:
            t_theory = p2_escape_theory(p2_init_eps)
            ratio = mp.mpf(p2_escape_step) / t_theory
            print(f"P2 escape theory    : {mp.nstr(t_theory, 10)} steps  "
                  f"[ln(1/eps)/ln(phi^2), eps={mp.nstr(p2_init_eps, 8)}]")
            print(f"measured / theory   : {mp.nstr(ratio, 8)}")
            print("  (ratio ≈ 1.0 confirms logarithmic escape law; DSN ≈A1)")
    else:
        print("\nP2 escape          : not detected in this run")

    # ------------------------------------------------------------------
    # 6-step Q_true diagnostics
    # ------------------------------------------------------------------
    if q6_samples:
        print(f"\n6-step Q_true diagnostics (primary radial observable; DSN ⊕T3):")
        preview = q6_samples[:12]
        for n, q in preview:
            nq = mp.mpf(n) * q
            print(f"  n={n:7d}  Q={mp.nstr(q, 16):>22}  n*Q={mp.nstr(nq, 16):>22}")
        if len(q6_samples) > 12:
            n, q = q6_samples[-1]
            nq = mp.mpf(n) * q
            print("  ...")
            print(f"  n={n:7d}  Q={mp.nstr(q, 16):>22}  n*Q={mp.nstr(nq, 16):>22}")

    # ------------------------------------------------------------------
    # Asymptotic-C rolling statistics   [v2.1-NEW-3]
    # ------------------------------------------------------------------
    result = asymptotic_c_stats(q6_samples, asymp_window)
    print(f"\nAsymptotic-C analysis (window={asymp_window} 6-step samples):")
    print("  Target: C = n*Q_true → ~6  (DSN ≈A4; exact theorem ⊗O2)")
    if result is None:
        print("  Insufficient samples for statistics.")
    else:
        mean_c, std_c, slope, count = result
        deviation = abs(mean_c - 6)
        print(f"  samples in window   : {count}")
        print(f"  mean(n*Q6_true)     : {mp.nstr(mean_c, 12)}")
        print(f"  std(n*Q6_true)      : {mp.nstr(std_c, 12)}")
        print(f"  |mean - 6|          : {mp.nstr(deviation, 8)}")
        if std_c > 0:
            print(f"  std/mean            : {mp.nstr(std_c / mean_c, 8)}")
        # Trend direction is more informative than absolute distance at finite horizon
        slope_sign = "rising ↑" if slope > 0 else ("falling ↓" if slope < 0 else "flat")
        print(f"  trend (slope/sample): {mp.nstr(slope, 8)}  [{slope_sign}]")
        if deviation < mp.mpf("0.05"):
            print("  STATUS: converged to C ≈ 6  ✓")
        elif slope > 0 and mean_c < 6:
            steps_remaining = deviation / slope if slope > 0 else mp.inf
            print(f"  STATUS: still rising toward C ≈ 6  "
                  f"(~{mp.nstr(steps_remaining, 4)} window-samples to go at current rate)")
        elif slope <= 0 and deviation > mp.mpf("0.1"):
            print("  STATUS: ⚠ not converging — check for frozen orbit or insufficient run length")
        else:
            print("  STATUS: approaching C ≈ 6")


# =============================================================================
# Args
# =============================================================================

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="High-precision RTG dyad audit simulator — DSN v2.1 aligned"
    )

    # Initial conditions
    p.add_argument("--rho0", type=str, required=True,
                   help="Initial rho (symbolic expressions supported)")
    p.add_argument("--eta0", type=str, required=True,
                   help="Initial eta (symbolic expressions supported)")

    # P2 eigenvector mode  [v2.1-NEW-1]
    p.add_argument("--p2-eigvec", action="store_true",
                   help="Override --rho0/--eta0: initialise at P2 + epsilon * "
                        "unstable eigenvector. Enables clean O1 escape-time "
                        "measurement (DSN v2.1 ⊗O1).")
    p.add_argument("--p2-eigvec-eps", type=str, default="1e-20",
                   help="Perturbation amplitude for --p2-eigvec mode (default 1e-20)")

    # Run parameters
    p.add_argument("--steps",       type=int, default=1000)
    p.add_argument("--dps",         type=int, default=80,
                   help="Decimal precision (mpmath dps)")
    p.add_argument("--print-every", type=int, default=50)

    # Asymptotic C window  [v2.1-NEW-3]
    p.add_argument("--asymp-window", type=int, default=100,
                   help="Number of trailing 6-step samples for asymptotic-C "
                        "statistics (default 100; DSN v2.1 ⊗O2)")

    # Output
    p.add_argument("--csv",        type=str, default="")
    p.add_argument("--csv-stride", type=int, default=1)
    p.add_argument("--stop-on-flag",   action="store_true")
    p.add_argument("--show-q6-live",   action="store_true",
                   help="Show Q6_true and nQ6_true in live output when available")

    # Thresholds
    p.add_argument("--near-fp-tol",      type=str, default="1e-30")
    p.add_argument("--crit-tol",         type=str, default="1e-30")
    p.add_argument("--rho-warn",         type=str, default="5.0")
    p.add_argument("--drift-warn",       type=str, default="100.0")
    p.add_argument("--q-growth-warn",    type=str, default="10.0")
    p.add_argument("--q6-growth-warn",   type=str, default="10.0")
    p.add_argument("--p2-escape-radius", type=str, default="0.1",
                   help="Macroscopic threshold distance from P2 for escape timing")
    return p.parse_args()


# =============================================================================
# Main
# =============================================================================

def main() -> int:
    args = parse_args()
    mp.mp.dps = args.dps

    # Resolve initial conditions
    # --p2-eigvec overrides --rho0/--eta0  [v2.1-NEW-1]
    p2_init_eps: Optional[mp.mpf] = None
    if args.p2_eigvec:
        eps = parse_expr(args.p2_eigvec_eps)
        p2_init_eps = eps
        v_u, _ = p2_eigenvectors()
        # P2 = (rho=0, eta=pi)
        rho0 = mp.mpf("0") + eps * v_u[0]
        eta0 = mp.pi          + eps * v_u[1]
        # Patch args for display
        args.rho0 = mp.nstr(rho0, 8)
        args.eta0 = mp.nstr(eta0, 8)
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

    discr_tol = mp.power(10, -(max(20, args.dps // 2)))

    st = State(rho=rho0, eta=eta0)

    print_header(args)

    csv_file = None
    writer   = None
    if args.csv:
        csv_file = open(args.csv, "w", newline="", encoding="utf-8")
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FIELDS)
        writer.writeheader()

    prev_uv_angle  = None
    winding_accum  = mp.mpf("0")
    prev_q         = None
    prev_q6        = None
    current_q6     = None
    q6_samples: List[Tuple[int, mp.mpf]] = []

    first_obs: Optional[Obs] = None
    last_obs:  Optional[Obs] = None
    p2_escape_step: Optional[int] = None

    # Track previous persistent-flag states to detect transitions only
    prev_near_p1    = False
    prev_near_p2    = False
    prev_escaped_p2 = False
    was_near_p2     = False   # latched True once near_p2 has ever been True

    try:
        for step in range(args.steps + 1):
            if step % 6 == 0 and step > 0:
                eta_wrap_tmp = wrap_pm_pi(st.eta)
                _, _, current_q6 = birkhoff_coords(st.rho, eta_wrap_tmp)
                q6_samples.append((step, current_q6))

            obs, prev_uv_angle, winding_accum = compute_obs(
                step=step,
                st=st,
                prev_uv_angle=prev_uv_angle,
                winding_accum=winding_accum,
                discr_tol=discr_tol,
                q6_current=current_q6,
            )

            if first_obs is None:
                first_obs = obs
            last_obs = obs

            flags = detect_flags(
                obs=obs,
                prev_q=prev_q,
                prev_q6=prev_q6,
                near_fp_tol=near_fp_tol,
                crit_tol=crit_tol,
                rho_warn=rho_warn,
                drift_warn=drift_warn,
                q_growth_warn=q_growth_warn,
                q6_growth_warn=q6_growth_warn,
                p2_escape_radius=p2_escape_radius,
                was_near_p2=was_near_p2,
            )

            # Latch: once near P2, remember it forever
            if flags.near_p2:
                was_near_p2 = True

            if p2_escape_step is None and prev_near_p2 and obs.dist_p2 > p2_escape_radius:
                p2_escape_step = step

            if writer is not None and (step % args.csv_stride == 0 or step == args.steps):
                write_csv_row(writer, obs)

            # Detect transitions in persistent state flags (print once on entry)
            state_transition = (
                (flags.near_p1       and not prev_near_p1)
                or (flags.near_p2    and not prev_near_p2)
                or (flags.escaped_p2_band and not prev_escaped_p2)
            )
            prev_near_p1    = flags.near_p1
            prev_near_p2    = flags.near_p2
            prev_escaped_p2 = flags.escaped_p2_band

            should_print = (
                step == 0
                or step % args.print_every == 0
                or flags.alert()        # transient alerts always print
                or state_transition     # persistent flags print only on entry
            )
            if should_print:
                print_obs(obs, flags, show_q6=args.show_q6_live)

            if args.stop_on_flag and step > 0 and flags.any_set():
                print("\nStopped due to stop-on-flag.")
                break

            prev_q = obs.q_true
            if obs.q6_true is not None:
                prev_q6 = obs.q6_true

            if step < args.steps:
                st = dyad_step(st)

    finally:
        if csv_file is not None:
            csv_file.close()

    assert first_obs is not None and last_obs is not None
    print_summary(
        first_obs=first_obs,
        last_obs=last_obs,
        q6_samples=q6_samples,
        asymp_window=args.asymp_window,
        p2_escape_step=p2_escape_step,
        p2_init_eps=p2_init_eps,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
