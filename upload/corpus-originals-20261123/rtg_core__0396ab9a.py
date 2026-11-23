# rtg_core.py
# Core math, model, stability analysis, diagnostics (plots & Lyapunov).
# Merged from rtg_core_old.py + rtg_core_new.py.
# Numpy + Matplotlib only. ASCII console; UTF-8 files.
#
# Merge notes
# -----------
# - New file is primary throughout (all L1/NS diagnostic machinery preserved).
# - Old-only functions appended in clearly labelled sections.
# - Conflicts resolved:
#     step_inertial : noise=0.0 added (old compat); arg name v used (new)
#     lyap_qr       : new signature (returns Dict, fixed gauge-free) is primary;
#                     old multi-exponent version kept as lyap_qr_multi()
#     GraphSpec     : eps_asym, F_triangle fields added with old defaults
#     Params        : all old sweep/post-NS/lyap fields added with their defaults
#     _leading_eigs_reduced: new (crude, fast) is primary;
#                     _leading_eigs_proper + gauge_free_basis_theta available
#                     for old K3 workflows
#     plot_grid_overview: unified to handle both 1-D and 2-D rho arrays

from __future__ import annotations
import os, math, time, json
from dataclasses import dataclass, field
from typing import Optional, Tuple, List, Dict
import numpy as np
import matplotlib.pyplot as plt


# ============================================================
# Utilities
# ============================================================

def _block_diag(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Private block-diagonal helper (new convention)."""
    n = A.shape[0]; m = B.shape[0]
    Z1 = np.zeros((n, m), dtype=float); Z2 = np.zeros((m, n), dtype=float)
    return np.block([[A, Z1], [Z2, B]])


def now_tag() -> str:
    return time.strftime("%Y%m%d_%H%M%S")


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save_json(obj: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True)


def wrap_pi(x: np.ndarray | float) -> np.ndarray | float:
    return (x + np.pi) % (2 * np.pi) - np.pi


def default_Delta() -> np.ndarray:
    return np.array([0.01, 0.0, -0.01], dtype=float)


def gauge_free_basis_theta(n: int) -> np.ndarray:
    """Orthonormal basis for the subspace orthogonal to the all-ones vector.

    Returns (n, n-1) matrix. Used by proper gauge-free projection (old K3 workflow).
    """
    assert n >= 2
    e   = np.eye(n)
    one = np.ones((n, 1)) / np.sqrt(n)
    cols = []
    for k in range(n):
        v = e[:, k:k+1]
        v = v - one @ (one.T @ v)
        for c in cols:
            v = v - c @ (c.T @ v)
        nv = np.linalg.norm(v)
        if nv > 1e-12:
            cols.append(v / nv)
        if len(cols) == n - 1:
            break
    return np.hstack(cols)


def block_diag(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Public block-diagonal helper — used by gauge_free_basis_theta workflows."""
    Z1 = np.zeros((A.shape[0], B.shape[1]))
    Z2 = np.zeros((B.shape[0], A.shape[1]))
    return np.block([[A, Z1], [Z2, B]])


# ============================================================
# Model specs
# ============================================================

@dataclass
class GraphSpec:
    n: int = 3
    directed: bool = True
    deg_norm: bool = False
    kappa:   np.ndarray = field(default_factory=lambda: np.ones((3, 3), dtype=float))
    alphas:  np.ndarray = field(default_factory=lambda: np.zeros((3, 3), dtype=float))
    deg_vec: np.ndarray = field(default_factory=lambda: np.ones(3, dtype=float))
    # Legacy fields (retained for old K3 compat)
    eps_asym:   float = 0.2
    F_triangle: float = 0.0

    def __post_init__(self):
        self.kappa  = np.array(self.kappa,  dtype=float)
        self.alphas = np.array(self.alphas, dtype=float)
        if self.deg_vec is None or len(np.atleast_1d(self.deg_vec)) != self.n:
            self.deg_vec = np.sum(np.abs(self.kappa), axis=1).astype(float)
        self.deg_vec = np.array(self.deg_vec, dtype=float)
        self.deg_vec[self.deg_vec == 0] = 1.0


@dataclass
class Params:
    # ---- Core integrator ----
    dt:      float = 0.1
    gamma:   float = 1.0
    scheme:  str   = "explicit"
    deg_norm: bool = False

    # ---- Legacy fields (old sweep / post-NS / Lyapunov workflows) ----
    family:   str   = "inertial"
    directed: bool  = True
    eps_asym: float = 0.2
    Delta: np.ndarray = field(default_factory=default_Delta)
    K_min:    float = 1.0
    K_max:    float = 6.0
    K_pts:    int   = 80
    ang_tol:  float = 0.10
    outdir:   Optional[str] = None
    post_ns:  bool  = False
    deltaK:   float = 0.03
    T_diag:   int   = 60000
    burn_diag: int  = 30000
    noise:    float = 0.0
    lyap_demo: bool = False
    le_q:     int   = 1


# ============================================================
# K3 topology builder (old)
# ============================================================

def build_k3_spec(p: Params) -> GraphSpec:
    """Build a directed 3-node ring GraphSpec (old K3 workflow)."""
    n = 3
    kappa = np.zeros((n, n), dtype=float)
    for i in range(n):
        j = (i + 1) % n
        kappa[i, j] = 1.0 + (p.eps_asym if p.directed else 0.0)
        kappa[j, i] = 1.0 - (p.eps_asym if p.directed else 0.0)
    np.fill_diagonal(kappa, 0.0)
    alphas = np.zeros((n, n), dtype=float)
    alphas[2, 0] = +2.0 * np.pi / 3.0
    deg_vec = np.sum(np.abs(kappa), axis=1)
    if not p.deg_norm:
        deg_vec = np.ones_like(deg_vec)
    return GraphSpec(n=n, directed=p.directed, eps_asym=p.eps_asym,
                     F_triangle=-2.0 * np.pi / 3.0,
                     kappa=kappa, alphas=alphas,
                     deg_vec=deg_vec, deg_norm=p.deg_norm)


# ============================================================
# Linearisation & Jacobians
# ============================================================

def M_coupling_linear(theta: Optional[np.ndarray],
                      K: float, spec: GraphSpec) -> np.ndarray:
    """Linear coupling matrix for small perturbations around theta (default 0)."""
    n = spec.n
    if theta is None:
        theta = np.zeros(n, dtype=float)
    C = np.zeros((n, n), dtype=float)
    for i in range(n):
        row_sum = 0.0
        for j in range(n):
            if i == j:
                continue
            c = (spec.kappa[i, j] / spec.deg_vec[i]) * \
                np.cos(theta[j] - theta[i] - spec.alphas[i, j])
            C[i, j]  = K * c
            row_sum += K * c
        C[i, i] = -row_sum
    return C


def coupling_cos_terms(theta: Optional[np.ndarray], spec: GraphSpec) -> np.ndarray:
    """Per-edge cosine linearisation terms WITHOUT the global K factor.

    term_ij = (kappa_ij / deg_i) * cos(theta_j - theta_i - alpha_ij)  for i != j
    Diagonal is zero. Used by jacobian_factor_stats() for L1 beta-pathway diagnostics.
    """
    n = spec.n
    if theta is None:
        theta = np.zeros(n, dtype=float)
    T = np.zeros((n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            T[i, j] = (spec.kappa[i, j] / spec.deg_vec[i]) * \
                       np.cos(theta[j] - theta[i] - spec.alphas[i, j])
    return T


def jacobian_factor_stats(theta: Optional[np.ndarray], spec: GraphSpec,
                           eps: float = 1e-15,
                           quantiles: Tuple[float, float, float] = (0.05, 0.50, 0.95)
                           ) -> Dict[str, float]:
    """Portable per-case statistics for the Jacobian cosine terms.

    Intended for L1 beta-pathway diagnostics (network amplification tests).
    Statistics over directed off-diagonal edges with nonzero kappa.
    Returns flat dict suitable for CSV/JSON logging.
    """
    T    = coupling_cos_terms(theta, spec)
    vals: List[float] = []
    n = spec.n
    for i in range(n):
        for j in range(n):
            if i == j or spec.kappa[i, j] == 0:
                continue
            vals.append(T[i, j])

    if len(vals) == 0:
        return {"n_terms": 0, "mean_log_abs": float("nan"), "var_log_abs": float("nan"),
                "mean_abs": float("nan"), "p05_abs": float("nan"), "p50_abs": float("nan"),
                "p95_abs": float("nan"), "mean_raw": float("nan"), "var_raw": float("nan")}

    v       = np.asarray(vals, dtype=float)
    abs_v   = np.abs(v)
    log_abs = np.log(np.maximum(abs_v, eps))
    p       = np.quantile(abs_v, quantiles)
    return {
        "n_terms":      int(v.size),
        "mean_log_abs": float(np.mean(log_abs)),
        "var_log_abs":  float(np.var(log_abs)),
        "mean_abs":     float(np.mean(abs_v)),
        f"p{int(quantiles[0]*100):02d}_abs": float(p[0]),
        f"p{int(quantiles[1]*100):02d}_abs": float(p[1]),
        f"p{int(quantiles[2]*100):02d}_abs": float(p[2]),
        "mean_raw": float(np.mean(v)),
        "var_raw":  float(np.var(v)),
    }


def jacobian_inertial(K: float, p: Params, spec: GraphSpec,
                      theta: Optional[np.ndarray] = None) -> np.ndarray:
    """2n x 2n Jacobian of the inertial map around theta (default 0)."""
    n = spec.n
    dt, gamma = p.dt, p.gamma
    A = 1.0 - gamma * dt
    M = M_coupling_linear(theta, K, spec)
    I = np.eye(n)
    if p.scheme.lower() in ("explicit", "e", "exp"):
        return np.block([[I,      dt * I],
                         [dt * M, A  * I]])
    elif p.scheme.lower() in ("ec", "euler_cromer", "euler-cromer"):
        return np.block([[I + (dt * dt) * M, dt * A * I],
                         [dt * M,             A   * I  ]])
    else:
        raise ValueError(f"Unknown scheme: {p.scheme}")


# ============================================================
# Gauge-free eigen analysis
# ============================================================

def _leading_eigs_reduced(J: np.ndarray, n: int) -> np.ndarray:
    """Eigenvalues on the gauge-free subspace — fast primary implementation.

    Drops the theta_0 row/col as a gauge fix. Sufficient for K4 / ringdiag.
    Returns eigenvalues sorted by descending magnitude.
    """
    idx = list(range(2 * n))
    idx.remove(0)
    Jr = J[np.ix_(idx, idx)]
    w  = np.linalg.eigvals(Jr)
    return w[np.argsort(-np.abs(w))]


def _leading_eigs_proper(J: np.ndarray, n: int) -> np.ndarray:
    """Proper gauge-free projection using orthonormal basis (old K3 workflow).

    Projects out the full uniform-theta-shift direction via gauge_free_basis_theta.
    More expensive but correct for any topology.
    """
    Qtheta = gauge_free_basis_theta(n)
    Q      = block_diag(Qtheta, Qtheta)
    Jr     = Q.T @ J @ Q
    w      = np.linalg.eigvals(Jr)
    return w[np.argsort(-np.abs(w))]


def leading_eig(J: np.ndarray, n: int,
                proper: bool = False) -> Tuple[complex, float]:
    """Largest-modulus eigenvalue and its angle in [0, pi].

    proper=True  -> full gauge_free_basis_theta projection (old K3 workflow).
    proper=False -> fast theta_0 removal (K4/ringdiag, default).
    """
    w   = _leading_eigs_proper(J, n) if proper else _leading_eigs_reduced(J, n)
    lam = w[0]
    ang = abs(np.angle(lam))
    if ang > np.pi:
        ang = 2 * np.pi - ang
    return lam, ang


def leading_modes(K: float, p: Params, spec: GraphSpec,
                  theta: Optional[np.ndarray] = None,
                  topk: int = 4) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return top-k eigenvalues (complex), magnitudes, and angles."""
    J = jacobian_inertial(K, p, spec, theta=theta)
    w = _leading_eigs_reduced(J, spec.n)
    w = w[:topk]
    return w, np.abs(w), np.angle(w)


def classify_mode(lam: complex, ang: float, ang_tol: float) -> str:
    if abs(lam.imag) < 1e-9:
        return "real+" if lam.real >= 0 else "real-"
    near_0  = ang < ang_tol
    near_pi = abs(ang - np.pi) < ang_tol
    return "complex-near-real" if (near_0 or near_pi) else "complex"


# ============================================================
# Inertial step map
# ============================================================

def step_inertial(theta: np.ndarray, v: np.ndarray,
                  K: float, p: Params, spec: GraphSpec,
                  noise: float = 0.0) -> Tuple[np.ndarray, np.ndarray]:
    """One step of the discrete inertial map (explicit or Euler-Cromer).

    noise > 0 adds Gaussian noise to theta after the step (old K3 diagnostics).
    """
    dt, gamma = p.dt, p.gamma
    A = 1.0 - gamma * dt
    n = spec.n
    f = np.zeros(n, dtype=float)
    for i in range(n):
        s = 0.0
        for j in range(n):
            if i == j:
                continue
            s += spec.kappa[i, j] * np.sin(theta[j] - theta[i] - spec.alphas[i, j])
        f[i] = s / spec.deg_vec[i]

    if p.scheme.lower() in ("explicit", "e", "exp"):
        theta2 = theta + dt * v
        v2     = A * v + (dt * K) * f
    else:
        v2     = A * v + (dt * K) * f
        theta2 = theta + dt * v2

    if noise > 0.0:
        theta2 = theta2 + np.random.normal(0.0, noise, size=theta.shape)

    return theta2, v2


# ============================================================
# K3 nonlinear diagnostics (old workflow)
# ============================================================

def triangle_flux(theta: np.ndarray, spec: GraphSpec) -> float:
    """Flux around (0,1,2) triangle; used in K3 post-NS demos."""
    if spec.n < 3:
        return 0.0
    F = ((theta[1] - theta[0] - spec.alphas[0, 1]) +
         (theta[2] - theta[1] - spec.alphas[1, 2]) +
         (theta[0] - theta[2] - spec.alphas[2, 0]))
    return float(wrap_pi(F))


def post_ns_demo(K_star: float, p: Params, spec: GraphSpec,
                 outdir: str, deltaK: float,
                 T: int, burn: int, noise: float) -> Dict[str, float]:
    """Run post-NS nonlinear diagnostics for K3 and save plots."""
    n     = spec.n
    theta = np.zeros(n, dtype=float)
    vel   = np.zeros(n, dtype=float)
    K_run = K_star + deltaK

    r_series: List[float] = []
    F_series: List[float] = []
    xy_series: List[List[float]] = []

    for t in range(T):
        theta, vel = step_inertial(theta, vel, K_run, p, spec, noise=noise)
        if t >= burn:
            z = np.exp(1j * theta).mean()
            r_series.append(abs(z))
            F_series.append(triangle_flux(theta, spec))
            xy_series.append([wrap_pi(theta[0] - theta[1]),
                               wrap_pi(theta[1] - theta[2])])

    r_arr  = np.asarray(r_series)  if r_series  else np.array([])
    F_arr  = np.asarray(F_series)  if F_series  else np.array([])
    xy_arr = np.asarray(xy_series) if xy_series else np.zeros((0, 2))

    f_meas = 0.0
    if r_arr.size > 0:
        plt.figure(); plt.plot(r_arr, lw=0.8)
        plt.title(f"r(t) at K={K_run:.6f}"); plt.xlabel("time (steps)"); plt.ylabel("r")
        plt.tight_layout(); plt.savefig(os.path.join(outdir, "ns_confirm_series.png"), dpi=150); plt.close()

        N = len(r_arr); r0 = r_arr - r_arr.mean()
        R = np.fft.rfft(r0); freqs = np.fft.rfftfreq(N, d=1.0)
        PSD = (R.conj() * R).real / max(1, N)
        plt.figure(); plt.plot(freqs, PSD, lw=0.8)
        plt.title(f"PSD of r(t) at K={K_run:.6f}"); plt.xlabel("frequency (cycles/step)"); plt.ylabel("power")
        plt.tight_layout(); plt.savefig(os.path.join(outdir, "ns_confirm_psd.png"), dpi=150); plt.close()

        if xy_arr.shape[0] > 0:
            plt.figure(figsize=(5, 5)); plt.plot(xy_arr[:, 0], xy_arr[:, 1], lw=0.6)
            plt.xlabel("theta1-theta2"); plt.ylabel("theta2-theta3")
            plt.title(f"Phase portrait at K={K_run:.6f}")
            plt.tight_layout(); plt.savefig(os.path.join(outdir, "ns_confirm_phase.png"), dpi=150); plt.close()

        if F_arr.size > 0:
            plt.figure(); plt.plot(F_arr, lw=0.8)
            plt.title("Triangle flux F"); plt.xlabel("time (steps)"); plt.ylabel("F (rad)")
            plt.tight_layout(); plt.savefig(os.path.join(outdir, "flux_su2_series.png"), dpi=150); plt.close()

        k_peak = int(np.argmax(PSD[1:])) + 1 if PSD.size > 1 else 0
        f_meas = float(freqs[k_peak]) if PSD.size > 1 else 0.0

    return {"K_run": float(K_run),
            "r_mean": float(r_arr.mean() if r_arr.size else 0.0),
            "r_std":  float(r_arr.std()  if r_arr.size else 0.0),
            "f_peak_per_step": f_meas}


# ============================================================
# K3 NS scan & refinement (old workflow)
# ============================================================

def scan_sweep(p: Params, spec: GraphSpec) -> Dict[str, np.ndarray | List[str]]:
    """K3 spectrum sweep over [K_min, K_max] using proper gauge-free projection."""
    K_grid = np.linspace(p.K_min, p.K_max, p.K_pts)
    rho = np.zeros_like(K_grid); ang = np.zeros_like(K_grid); lbl: List[str] = []
    for i, K in enumerate(K_grid):
        J      = jacobian_inertial(K, p, spec, theta=None)
        lam, a = leading_eig(J, spec.n, proper=True)
        rho[i] = abs(lam); ang[i] = a
        lbl.append(classify_mode(lam, a, p.ang_tol))
    return {"K": K_grid, "rho": rho, "ang": ang, "label": lbl}


def find_ns_bracket(K: np.ndarray, rho: np.ndarray, ang: np.ndarray,
                    lbl: List[str], ang_tol: float) -> Optional[Tuple[float, float]]:
    """Find a bracketing interval where |lambda| crosses 1 as a complex mode."""
    for i in range(len(K) - 1):
        ci = ("complex" in lbl[i])   and ang[i]   > ang_tol and abs(ang[i]   - np.pi) > ang_tol
        cj = ("complex" in lbl[i+1]) and ang[i+1] > ang_tol and abs(ang[i+1] - np.pi) > ang_tol
        if ci and cj and (rho[i] - 1.0) * (rho[i+1] - 1.0) <= 0.0:
            return (K[i], K[i+1])
    return None


def refine_ns(K_lo: float, K_hi: float, p: Params, spec: GraphSpec,
              iters: int = 32) -> Tuple[float, float, float, str]:
    """Bisection refinement of K_spark in bracket [K_lo, K_hi]."""
    bestK = bestR = bestA = bestL = None  # type: ignore[assignment]
    for _ in range(iters):
        K_mid  = 0.5 * (K_lo + K_hi)
        J      = jacobian_inertial(K_mid, p, spec, theta=None)
        lam, a = leading_eig(J, spec.n, proper=True)
        r = abs(lam); lbl = classify_mode(lam, a, p.ang_tol)
        bestK, bestR, bestA, bestL = K_mid, r, a, lbl
        if r >= 1.0: K_hi = K_mid
        else:        K_lo = K_mid
    return bestK, bestR, bestA, bestL


def drho_dK_numeric(K: float, p: Params, spec: GraphSpec,
                    h: float = 1e-3) -> float:
    """Numeric derivative d|lambda|/dK via central difference."""
    J1 = jacobian_inertial(K - h, p, spec, theta=None)
    J2 = jacobian_inertial(K + h, p, spec, theta=None)
    lam1, _ = leading_eig(J1, spec.n, proper=True)
    lam2, _ = leading_eig(J2, spec.n, proper=True)
    return (abs(lam2) - abs(lam1)) / (2 * h)


# ============================================================
# Lyapunov exponents
# ============================================================

def lyap_qr(K: float, p: Params, spec: GraphSpec,
            T: int = 8000, burn: int = 2000,
            seed: int = 0,
            theta0: Optional[np.ndarray] = None,
            v0: Optional[np.ndarray] = None,
            qr_every: int = 5,
            gauge_free: bool = True) -> Dict[str, float]:
    """Maximal Lyapunov exponent via QR method — primary version (returns Dict).

    gauge_free=True operates permanently in the (2n-1)-dim subspace by dropping
    the uniform theta-shift mode, avoiding the progressive dimension-shrink bug.
    """
    rng = np.random.default_rng(seed)
    n   = spec.n; dim = 2 * n

    theta = rng.uniform(-np.pi, np.pi, n) if theta0 is None else np.array(theta0, dtype=float)
    v     = rng.normal(0.0, 0.1, n)       if v0     is None else np.array(v0,     dtype=float)

    gf_idx  = list(range(1, dim)) if gauge_free else list(range(dim))
    dim_eff = len(gf_idx)
    Q = np.eye(dim_eff); le_sum = 0.0; count = 0

    for _ in range(burn):
        theta, v = step_inertial(theta, v, K, p, spec)

    for t in range(T):
        theta, v = step_inertial(theta, v, K, p, spec)
        J = jacobian_inertial(K, p, spec, theta=theta)[np.ix_(gf_idx, gf_idx)]
        Q = J @ Q
        if (t + 1) % qr_every == 0:
            Q, R  = np.linalg.qr(Q)
            diag  = np.abs(np.diag(R)); diag[diag == 0] = 1e-300
            le_sum += np.sum(np.log(diag)); count += 1

    lmax = le_sum / (count * qr_every * p.dt)
    return {"lmax": float(lmax), "count": int(count), "qr_every": int(qr_every),
            "T": int(T), "burn": int(burn), "seed": int(seed)}


def lyap_qr_multi(K: float, p: Params, spec: GraphSpec,
                  T: int = 30000, burn: int = 10000,
                  q: int = 3, noise: float = 0.0) -> np.ndarray:
    """Top-q Lyapunov exponents (per step) — old multi-exponent version.

    Returns np.ndarray of shape (q,). Retained for legacy K3 workflows.
    """
    n = spec.n; theta = np.zeros(n); vel = np.zeros(n); D = 2 * n
    rng = np.random.default_rng(42)
    Q   = rng.normal(size=(D, q)); Q, _ = np.linalg.qr(Q, mode="reduced")
    sums = np.zeros(q); cnt = 0

    for t in range(T):
        J     = jacobian_inertial(K, p, spec, theta=theta)
        Q, R  = np.linalg.qr(J @ Q, mode="reduced")
        if t >= burn:
            diag = np.abs(np.diag(R)); diag[diag == 0.0] = 1e-30
            sums += np.log(diag); cnt += 1
        theta, vel = step_inertial(theta, vel, K, p, spec, noise=noise)

    return sums / cnt if cnt > 0 else np.zeros(q)


def largest_lyap(K: float, p: Params, spec: GraphSpec,
                 T: int = 30000, burn: int = 10000,
                 noise: float = 0.0) -> float:
    """Maximal Lyapunov exponent (per step) — thin wrapper around lyap_qr_multi."""
    return float(lyap_qr_multi(K, p, spec, T=T, burn=burn, q=1, noise=noise)[0])


# ============================================================
# Topology builders
# ============================================================

def build_ringdiag_spec(n: int, phi: float,
                        eps_asym: float = 0.25,
                        deg_norm: bool = False) -> GraphSpec:
    """Build directed ring+diagonal GraphSpec for DSN sec.1 substrate.

    Coupling convention (DSN sec.1):
        theta_dot_i = omega_i + K * sum_j kappa_ij
                      * [sin(theta_j-theta_i) + eps_asym*sin(theta_j-theta_i+phi)]
                      / deg_i

    The asymmetric phase-shifted term is encoded via alpha_ij = -phi.
    For n > 4 nodes: ring forward/backward + skip-1 diagonals.
    """
    adj = set()
    for i in range(n):
        adj.add((i, (i + 1) % n)); adj.add((i, (i - 1) % n))
        if n > 4:
            adj.add((i, (i + 2) % n)); adj.add((i, (i - 2) % n))

    kappa = np.zeros((n, n)); alphas = np.zeros((n, n))
    for (i, j) in adj:
        if i == j: continue
        kappa[i, j]  = 1.0 + eps_asym
        alphas[i, j] = -phi

    spec = GraphSpec(n=n, directed=True, deg_norm=deg_norm, kappa=kappa, alphas=alphas)
    spec._phi      = phi       # type: ignore[attr-defined]
    spec._eps_asym = eps_asym  # type: ignore[attr-defined]
    return spec


# ============================================================
# Fixed-point finder
# ============================================================

def find_fixed_point(omega: np.ndarray, K: float, spec: GraphSpec,
                     theta0: Optional[np.ndarray] = None,
                     max_iter: int = 3000, tol: float = 1e-9,
                     lr: float = 0.03) -> Tuple[np.ndarray, bool]:
    """Find synchronised fixed point via damped gradient descent.

    Returns (theta_fp, converged).
    """
    n   = spec.n
    rng = np.random.default_rng(17)
    theta = rng.uniform(-np.pi, np.pi, n) if theta0 is None \
            else np.array(theta0, dtype=float).copy()

    def _res(th: np.ndarray) -> np.ndarray:
        f = np.zeros(n)
        for i in range(n):
            s = sum(spec.kappa[i, j] * np.sin(th[j] - th[i] - spec.alphas[i, j])
                    for j in range(n) if j != i)
            f[i] = s / spec.deg_vec[i]
        return omega + K * f

    for _ in range(max_iter):
        res = _res(theta)
        if np.max(np.abs(res)) < tol:
            return theta, True
        M    = M_coupling_linear(theta, K, spec)
        diag = np.diag(M).copy(); diag[np.abs(diag) < 1e-12] = -1.0
        theta -= lr * res / np.abs(diag)

    return theta, np.max(np.abs(_res(theta))) < tol * 1e3


# ============================================================
# Spectrum sweep (multi-mode)
# ============================================================

def scan_spectrum(K_arr: np.ndarray, p: Params, spec: GraphSpec,
                  omega: Optional[np.ndarray] = None,
                  topk: int = 4, find_fp: bool = True,
                  fp_tol: float = 1e-8) -> Dict[str, np.ndarray]:
    """Sweep K_arr and collect leading Floquet eigenvalues.

    Returns dict: K (nK,), rho (nK, topk), ang (nK, topk), fp_ok (nK,), theta_fp (nK, n).
    """
    nK, n = len(K_arr), spec.n
    rho_arr = np.full((nK, topk), np.nan); ang_arr = np.full((nK, topk), np.nan)
    fp_ok = np.zeros(nK, dtype=bool); theta_fp_arr = np.zeros((nK, n))
    if omega is None: omega = np.zeros(n)

    theta_prev = None
    for ki, K in enumerate(K_arr):
        if find_fp:
            th_fp, ok = find_fixed_point(omega, K, spec, theta0=theta_prev, tol=fp_tol)
            fp_ok[ki] = ok; theta_use = th_fp if ok else np.zeros(n); theta_prev = th_fp
        else:
            theta_use = np.zeros(n)
        theta_fp_arr[ki] = theta_use
        _, rho, ang = leading_modes(K, p, spec, theta=theta_use, topk=topk)
        rho_arr[ki, :len(rho)] = rho; ang_arr[ki, :len(ang)] = ang

    return {"K": K_arr, "rho": rho_arr, "ang": ang_arr,
            "fp_ok": fp_ok, "theta_fp": theta_fp_arr}


# ============================================================
# NS bifurcation search
# ============================================================

_SPARK_NAN = {
    "K_spark": float("nan"), "lam1_rho": float("nan"), "lam1_ang": float("nan"),
    "lam2_rho": float("nan"), "lam2_ang": float("nan"),
    "spectral_gap": float("nan"), "ang_separation": float("nan"), "fp_ok": False,
}


def find_k_spark(p: Params, spec: GraphSpec,
                 omega: Optional[np.ndarray] = None,
                 K_lo: float = 0.01, K_hi: float = 10.0,
                 tol: float = 1e-5, max_iter: int = 60,
                 fp_tol: float = 1e-8) -> Dict[str, float]:
    """Binary search for K_spark (|lambda_1| first crosses 1).

    Always returns a complete dict (NaN-filled on failure).
    """
    n = spec.n
    if omega is None: omega = np.zeros(n)

    def _eval(K: float) -> Tuple[float, float, float, float, bool]:
        th, ok = find_fixed_point(omega, K, spec, tol=fp_tol)
        theta_use = th if ok else np.zeros(n)
        _, rho, ang = leading_modes(K, p, spec, theta=theta_use, topk=4)
        r1 = float(rho[0]) if len(rho) > 0 else 0.0
        a1 = float(ang[0]) if len(ang) > 0 else 0.0
        r2 = float(rho[1]) if len(rho) > 1 else 0.0
        a2 = float(ang[1]) if len(ang) > 1 else 0.0
        return r1, a1, r2, a2, ok

    r_lo, *_ = _eval(K_lo); r_hi, *_ = _eval(K_hi)
    if r_lo >= 1.0: return {**_SPARK_NAN, "error": "rho1>=1 at K_lo; lower K_lo"}
    if r_hi < 1.0:
        for _ in range(8):
            K_hi *= 2.0; r_hi, *_ = _eval(K_hi)
            if r_hi >= 1.0: break
        if r_hi < 1.0: return {**_SPARK_NAN, "error": "rho1<1 even at K_hi*256; increase K_hi"}

    for _ in range(max_iter):
        K_mid = 0.5 * (K_lo + K_hi); r_mid, *_ = _eval(K_mid)
        K_lo, K_hi = (K_mid, K_hi) if r_mid < 1.0 else (K_lo, K_mid)
        if K_hi - K_lo < tol: break

    K_spark = 0.5 * (K_lo + K_hi)
    r1, a1, r2, a2, ok = _eval(K_spark)
    return {"K_spark": float(K_spark), "lam1_rho": r1, "lam1_ang": a1,
            "lam2_rho": r2, "lam2_ang": a2,
            "spectral_gap": float(1.0 - r2), "ang_separation": float(abs(a1 - a2)),
            "fp_ok": bool(ok)}


# ============================================================
# Threshold-free lam2 extrapolation
# ============================================================

def k_lam2_hit_extrapolated(scan: Dict[str, np.ndarray],
                              K_spark: float) -> float:
    """Linear extrapolation of K where |lam2|=1 (threshold-free).

    DSN V_B1_MODE_COMPETITION_PRIMARY: Lambda_comp = K_fracture - K_lam2_hit_pred.
    Negative Lambda_comp => competitor crossed |lam|=1 before fracture => B1.
    """
    K_arr = scan["K"]; rho = scan["rho"]
    mask = (K_arr > K_spark) & np.isfinite(rho[:, 1])
    if mask.sum() < 3: return float("nan")
    coeffs = np.polyfit(K_arr[mask], rho[mask, 1], 1)
    if abs(coeffs[0]) < 1e-14: return float("nan")
    return float((1.0 - coeffs[1]) / coeffs[0])


# ============================================================
# Fracture detection
# ============================================================

def find_k_fracture(p: Params, spec: GraphSpec,
                    omega: Optional[np.ndarray] = None,
                    K_spark: float = 1.0, K_hi: float = 20.0,
                    rho_threshold: float = 1.5, comp_threshold: float = 0.995,
                    n_steps: int = 500, fp_tol: float = 1e-8) -> Dict[str, float]:
    """Scan K from K_spark to K_hi and detect NS circle fracture.

    Fracture criteria (first triggered wins):
        1. comp_ratio = |lam2|/|lam1| > comp_threshold (mode competition B1)
        2. |lam1| > rho_threshold (amplitude explosion)
    """
    n = spec.n
    if omega is None: omega = np.zeros(n)
    nan_r: Dict[str, float] = {"K_fracture": float("nan"), "comp_ratio": float("nan"),
                                "lam1_rho": float("nan"), "lam2_rho": float("nan"),
                                "lam1_ang": float("nan"), "lam2_ang": float("nan"),
                                "K_lam2_hit": float("nan"), "method": "none"}

    K_lam2_hit = float("nan"); K_fracture = float("nan")
    frac = dict(nan_r); theta_prev = None; prev_r2 = 0.0; lam2_seen = False

    for K in np.linspace(K_spark, K_hi, n_steps):
        th, ok = find_fixed_point(omega, K, spec, theta0=theta_prev, tol=fp_tol)
        theta_use = th if ok else np.zeros(n); theta_prev = th
        _, rho, ang = leading_modes(K, p, spec, theta=theta_use, topk=4)
        r1 = float(rho[0]) if len(rho) > 0 else 1.0
        r2 = float(rho[1]) if len(rho) > 1 else 0.0
        a1 = float(ang[0]) if len(ang) > 0 else 0.0
        a2 = float(ang[1]) if len(ang) > 1 else 0.0

        if not lam2_seen and prev_r2 < 1.0 <= r2:
            K_lam2_hit = float(K); lam2_seen = True
        prev_r2 = r2

        if math.isnan(K_fracture):
            comp = r2 / r1 if r1 > 1e-12 else 0.0
            if comp > comp_threshold or r1 > rho_threshold:
                K_fracture = float(K)
                frac.update({"K_fracture": K_fracture, "comp_ratio": comp,
                              "lam1_rho": r1, "lam2_rho": r2,
                              "lam1_ang": a1, "lam2_ang": a2,
                              "method": "comp_ratio" if comp > comp_threshold else "amplitude"})

    if math.isnan(K_fracture) and not math.isnan(K_lam2_hit):
        frac["K_fracture"] = K_lam2_hit; frac["method"] = "lam2_crossing_fallback"
    frac["K_lam2_hit"] = K_lam2_hit
    return frac


# ============================================================
# Resonance gap
# ============================================================

def compute_res_gap(lam1_ang: float, lam2_ang: float,
                    max_p: int = 10, max_q: int = 10) -> Dict[str, float]:
    """Distance from lam1_ang to nearest p:q rational rotation.

    DSN: V_C_PROTECTIVE_MODULATOR, H_RATIONAL_STRUCTURE_PREFERRED.
    """
    norm = (lam1_ang / (2.0 * np.pi)) % 1.0
    best, best_p, best_q = float("inf"), 1, 1
    for q in range(1, max_q + 1):
        for pp in range(1, min(q, max_p) + 1):
            d = abs(norm - pp / q); d = min(d, 1.0 - d)
            if d < best: best, best_p, best_q = d, pp, q

    inter = abs(lam1_ang - lam2_ang) % np.pi
    if inter > np.pi / 2: inter = np.pi - inter

    return {"single_mode_gap": float(best * 2.0 * np.pi), "inter_modal_gap": float(inter),
            "res_gap_p": int(best_p), "res_gap_q": int(best_q), "dQ": float(best)}


# ============================================================
# Mode competition metrics
# ============================================================

def mode_competition_metrics(scan: Dict[str, np.ndarray],
                              K_spark: float, K_fracture: float) -> Dict[str, float]:
    """B1 evidence metrics from spectrum scan.  DSN: V_B1_MODE_COMPETITION_PRIMARY."""
    K_arr = scan["K"]; rho = scan["rho"]; ang = scan["ang"]

    def _at(K_t: float, col: int, arr: np.ndarray) -> float:
        idx = int(np.argmin(np.abs(K_arr - K_t)))
        return float(arr[idx, col]) if arr.shape[1] > col else float("nan")

    r1_f = _at(K_fracture, 0, rho); r2_f = _at(K_fracture, 1, rho)
    a1_f = _at(K_fracture, 0, ang); a2_f = _at(K_fracture, 1, ang)
    comp_ratio  = r2_f / r1_f if r1_f > 1e-12 else float("nan")
    K_lam2_pred = k_lam2_hit_extrapolated(scan, K_spark)
    Lambda_comp = K_fracture - K_lam2_pred
    idx_sp = int(np.argmin(np.abs(K_arr - K_spark)))
    gap_sp = float(1.0 - rho[idx_sp, 1]) if rho.shape[1] > 1 else float("nan")

    return {"comp_ratio_at_fracture": comp_ratio,
            "lam1_rho_fracture": r1_f, "lam2_rho_fracture": r2_f,
            "lam1_ang_fracture": a1_f, "lam2_ang_fracture": a2_f,
            "K_lam2_hit_pred": K_lam2_pred, "Lambda_comp": Lambda_comp,
            "spectral_gap_at_spark": gap_sp, "b1_supported": bool(Lambda_comp < 0)}


# ============================================================
# NS circle amplitude
# ============================================================

def ns_circle_radius(theta0: np.ndarray, v0: np.ndarray,
                     K: float, p: Params, spec: GraphSpec,
                     n_burn: int = 600, n_measure: int = 600) -> float:
    """RMS velocity amplitude on the NS circle (proxy for circle radius H)."""
    theta, v = np.array(theta0), np.array(v0)
    for _ in range(n_burn): theta, v = step_inertial(theta, v, K, p, spec)
    acc = 0.0
    for _ in range(n_measure):
        theta, v = step_inertial(theta, v, K, p, spec)
        acc += float(np.sqrt(np.mean(v**2)))
    return acc / n_measure


def measure_window(p: Params, spec: GraphSpec,
                   omega: Optional[np.ndarray] = None,
                   K_spark: float = 1.0, K_fracture: float = 5.0,
                   n_burn: int = 800, n_measure: int = 800,
                   seed: int = 0) -> Dict[str, float]:
    """Measure delta_H_obs and W_obs = delta_H_obs * gamma^2 / K_spark.  DSN: THM_SPECTRAL_WINDOW."""
    n = spec.n
    if omega is None: omega = np.zeros(n)
    rng = np.random.default_rng(seed)

    def _H(K: float) -> float:
        th_fp, _ = find_fixed_point(omega, K, spec)
        return ns_circle_radius(th_fp, rng.normal(0.0, 0.05, n), K, p, spec,
                                n_burn=n_burn, n_measure=n_measure)

    H_lo = _H(K_spark * 1.02); H_hi = _H(K_fracture * 0.98)
    dH = H_hi - H_lo; W = dH * p.gamma**2 / K_spark
    return {"W_obs": float(W), "delta_H": float(dH),
            "H_spark": float(H_lo), "H_fracture": float(H_hi),
            "K_spark": float(K_spark), "K_fracture": float(K_fracture),
            "K_lo_measured": float(K_spark * 1.02), "K_hi_measured": float(K_fracture * 0.98)}


# ============================================================
# Full per-case diagnosis export
# ============================================================

def export_diagnosis_point(phi: float, dt: float, gamma: float,
                            p: Params, spec: GraphSpec,
                            omega: Optional[np.ndarray] = None,
                            K_lo: float = 0.01,
                            K_hi_spark: float = 15.0,
                            K_hi_frac: float = 30.0,
                            n_scan: int = 300,
                            fp_tol: float = 1e-8) -> Dict:
    """Full per-case diagnostic — computes all L1 DSN quantities in one call.

    Quantities: K_spark, lam_angs, spectral_gap, K_fracture, comp_ratio,
    Lambda_comp, K_lam2_hit_pred, res_gap, inter_modal_gap, dQ,
    Jacobian cos-term stats, R_K, X.
    Returns flat dict suitable for diagnosis_points.csv row.
    """
    n = spec.n
    if omega is None: omega = np.zeros(n)
    out: Dict = {"phi": phi, "dt": dt, "gamma": gamma, "n_nodes": n}

    spark = find_k_spark(p, spec, omega=omega, K_lo=K_lo, K_hi=K_hi_spark, fp_tol=fp_tol)
    out.update({f"spark_{k}": v for k, v in spark.items()})
    K_spark = spark.get("K_spark", float("nan"))
    if math.isnan(K_spark): out["error"] = "K_spark not found"; return out

    K_scan = np.linspace(max(K_lo, K_spark * 0.95), K_hi_frac, n_scan)
    scan   = scan_spectrum(K_scan, p, spec, omega=omega, topk=4, fp_tol=fp_tol)

    frac       = find_k_fracture(p, spec, omega=omega, K_spark=K_spark, K_hi=K_hi_frac, fp_tol=fp_tol)
    out.update({f"frac_{k}": v for k, v in frac.items()})
    K_fracture = frac.get("K_fracture", float("nan"))

    if not math.isnan(K_fracture):
        mc = mode_competition_metrics(scan, K_spark, K_fracture)
        out.update({f"mc_{k}": v for k, v in mc.items()})
        out["R_K"] = (K_fracture - K_spark) / K_spark
        out["X"]   = K_spark / gamma**2 if gamma != 0 else float("nan")

    rg = compute_res_gap(spark.get("lam1_ang", 0.0), spark.get("lam2_ang", 0.0))
    out.update({f"rg_{k}": v for k, v in rg.items()})

    th_fp, _ = find_fixed_point(omega, K_spark, spec, tol=fp_tol)
    jac = jacobian_factor_stats(th_fp, spec)
    out.update({f"jac_{k}": v for k, v in jac.items()})
    return out


# ============================================================
# Plot helpers
# ============================================================

def plot_spectrum(K: np.ndarray, rho: np.ndarray, ang: np.ndarray,
                  lbl: List[str], outdir: str, tag: str) -> None:
    """Plot multi-mode Floquet magnitudes and angles vs K."""
    plt.figure(figsize=(6, 4))
    for i in range(rho.shape[1]):
        plt.plot(K, rho[:, i], lw=1.0, label=lbl[i] if i < len(lbl) else f"mode{i}")
    plt.axhline(1.0, color="k", lw=0.8, ls="--")
    plt.xlabel("K"); plt.ylabel("|lambda|"); plt.title("Leading Floquet magnitudes")
    plt.legend(loc="best", fontsize=8); plt.tight_layout()
    plt.savefig(os.path.join(outdir, f"{tag}_rho.png"), dpi=150); plt.close()

    plt.figure(figsize=(6, 4))
    for i in range(ang.shape[1]):
        plt.plot(K, ang[:, i], lw=1.0, label=lbl[i] if i < len(lbl) else f"mode{i}")
    plt.xlabel("K"); plt.ylabel("arg(lambda)"); plt.title("Leading Floquet angles")
    plt.legend(loc="best", fontsize=8); plt.tight_layout()
    plt.savefig(os.path.join(outdir, f"{tag}_ang.png"), dpi=150); plt.close()


def plot_grid_overview(K: np.ndarray, rho: np.ndarray, ang: np.ndarray,
                       lbl: List[str], outdir: str, tag: str) -> None:
    """Spectral radius overview — accepts 1-D or 2-D rho arrays."""
    rho_plot = rho[:, 0] if rho.ndim == 2 else rho
    plt.figure(figsize=(6, 4)); plt.plot(K, rho_plot, lw=1.0, label="|lambda|max")
    plt.axhline(1.0, color="k", lw=0.8, ls="--")
    plt.xlabel("K"); plt.ylabel("spectral radius"); plt.title("Grid overview (leading mode)")
    plt.tight_layout(); plt.savefig(os.path.join(outdir, f"{tag}_grid_overview.png"), dpi=150); plt.close()


def plot_angle_vs_K(K: np.ndarray, ang: np.ndarray, outdir: str, tag: str) -> None:
    """Leading eigen-angle vs K (1-D ang, old K3 workflow)."""
    plt.figure(); plt.plot(K, ang, lw=1.0)
    plt.xlabel("K"); plt.ylabel("angle (rad)"); plt.title("Leading eigen-angle vs K")
    plt.tight_layout(); plt.savefig(os.path.join(outdir, f"{tag}_angle_vs_K.png"), dpi=150); plt.close()


def plot_mode_competition(scan: Dict[str, np.ndarray],
                           K_spark: float, K_fracture: float,
                           outdir: str, tag: str) -> None:
    """Plot |lam1| and |lam2| vs K.  DSN: V_B1_MODE_COMPETITION_PRIMARY."""
    K_arr = scan["K"]; rho = scan["rho"]
    plt.figure(figsize=(7, 4))
    plt.plot(K_arr, rho[:, 0], lw=1.2, label="|lambda_1| primary")
    if rho.shape[1] > 1:
        plt.plot(K_arr, rho[:, 1], lw=1.2, ls="--", label="|lambda_2| competitor")
    plt.axhline(1.0, color="k", lw=0.8, ls=":", alpha=0.6)
    plt.axvline(K_spark,    color="b", lw=0.9, ls=":", alpha=0.7, label=f"K_spark={K_spark:.3f}")
    plt.axvline(K_fracture, color="r", lw=0.9, ls=":", alpha=0.7, label=f"K_frac={K_fracture:.3f}")
    plt.xlabel("K"); plt.ylabel("|lambda|"); plt.title("Mode competition: primary vs competitor")
    plt.legend(loc="best", fontsize=8); plt.tight_layout()
    plt.savefig(os.path.join(outdir, f"{tag}_mode_competition.png"), dpi=150); plt.close()