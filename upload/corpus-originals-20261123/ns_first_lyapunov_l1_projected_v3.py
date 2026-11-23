#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
ns_first_lyapunov_l1_projected_v3.py

Neimark–Sacker first Lyapunov coefficient l1 (K4 inertial map), with a robust
center-subspace projector built from the *actual* conjugate eigenpair.

v3 fix:
-------
Instead of assuming qbar == conj(q) (and pbar == conj(p)), we:
- compute right eigenvectors q1 (for λ) and q2 (for λ̄) from eig(J)
- compute left eigenvectors p1 (for λ) and p2 (for λ̄) from eig(J^T)
- biorthonormalize so that P^H Q = I2
- set Pc = Q P^H which is idempotent by construction

Then use:
  q = q1, qbar = q2, p = p1 (after biorthonormalization)

We still:
- evaluate only real map states (step_inertial uses math.sin)
- compute B,C via real FD and extend multilinearly

Outputs:
  experiments/k4/ns_l1_projected_v3/<run_name>/ns_l1_projected_v3.json
"""

from __future__ import annotations

import argparse
import json
import os
from typing import Any, Dict, Tuple

import numpy as np

from rtg.core.rtg_core import scan_sweep, find_ns_bracket, refine_ns
from rtg.core.rtg_core import step_inertial
from rtg.k4.topology import K4Params, build_k4_spec


# -------------------------
# utils
# -------------------------
def ensure_dir(p: str) -> None:
    if p:
        os.makedirs(p, exist_ok=True)


def parse_bool(x: str) -> bool:
    return str(x).strip().lower() in ("1", "true", "t", "yes", "y")


def gauge_free_basis(n: int) -> np.ndarray:
    one = np.ones((n, 1))
    A = np.concatenate([one, np.eye(n)], axis=1)
    Qfull, _ = np.linalg.qr(A)
    return Qfull[:, 1:n]  # n x (n-1)


def pack(theta: np.ndarray, vel: np.ndarray, Q: np.ndarray) -> np.ndarray:
    return np.concatenate([Q.T @ theta, Q.T @ vel], axis=0)


def unpack(y: np.ndarray, Q: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    n1 = Q.shape[1]
    return Q @ y[:n1], Q @ y[n1:]


def find_spark(p: Any, spec: Any, ang_tol: float, bisect_iters: int) -> Tuple[float, float, float, str]:
    sweep = scan_sweep(p, spec)
    K = np.asarray(sweep["K"], dtype=float)
    rho = np.asarray(sweep["rho"], dtype=float)
    ang = np.asarray(sweep.get("ang", np.zeros_like(rho)), dtype=float)
    lbl = list(sweep.get("label", [""] * len(rho)))

    bracket = find_ns_bracket(K, rho, ang, lbl, ang_tol)
    if bracket is None:
        raise RuntimeError("spark_failed: find_ns_bracket returned None (no crossing).")

    K_spark, rho_star, omega_star, label = refine_ns(bracket[0], bracket[1], p, spec, iters=bisect_iters)
    return float(K_spark), float(rho_star), float(omega_star), str(label)


# -------------------------
# reduced real map
# -------------------------
def F_map_real(y_real: np.ndarray, K: float, p: Any, spec: Any, Q: np.ndarray) -> np.ndarray:
    y_real = np.asarray(y_real, dtype=float)
    theta, vel = unpack(y_real, Q)
    theta2, vel2 = step_inertial(theta, vel, K, p, spec, noise=0.0)
    return pack(theta2, vel2, Q).astype(float)


def jacobian_fd(F, y0: np.ndarray, h: float) -> np.ndarray:
    n = y0.size
    J = np.zeros((n, n), dtype=float)
    for i in range(n):
        e = np.zeros(n, dtype=float)
        e[i] = 1.0
        fp = F(y0 + h * e)
        fm = F(y0 - h * e)
        J[:, i] = (fp - fm) / (2.0 * h)
    return J


# -------------------------
# multilinear forms (real map) + complex extension
# -------------------------
def B_real(F, y0: np.ndarray, u: np.ndarray, v: np.ndarray, h2: float) -> np.ndarray:
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    fpp = F(y0 + h2 * (u + v))
    fpm = F(y0 + h2 * (u - v))
    fmp = F(y0 + h2 * (-u + v))
    fmm = F(y0 - h2 * (u + v))
    return (fpp - fpm - fmp + fmm) / (4.0 * h2 * h2)


def C_real(F, y0: np.ndarray, u: np.ndarray, v: np.ndarray, w: np.ndarray, h3: float) -> np.ndarray:
    u = np.asarray(u, dtype=float)
    v = np.asarray(v, dtype=float)
    w = np.asarray(w, dtype=float)
    acc = np.zeros_like(y0, dtype=float)
    for su in (-1.0, 1.0):
        for sv in (-1.0, 1.0):
            for sw in (-1.0, 1.0):
                s = su * sv * sw
                acc += s * F(y0 + h3 * (su * u + sv * v + sw * w))
    return acc / (8.0 * h3**3)


def split_complex(z: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    z = np.asarray(z, dtype=complex)
    return np.real(z).astype(float), np.imag(z).astype(float)


def B_complex(F, y0: np.ndarray, u: np.ndarray, v: np.ndarray, h2: float) -> np.ndarray:
    a, b = split_complex(u)
    c, d = split_complex(v)
    Bac = B_real(F, y0, a, c, h2)
    Bbd = B_real(F, y0, b, d, h2)
    Bad = B_real(F, y0, a, d, h2)
    Bbc = B_real(F, y0, b, c, h2)
    return (Bac - Bbd).astype(complex) + 1j * (Bad + Bbc).astype(complex)


def C_complex(F, y0: np.ndarray, u: np.ndarray, v: np.ndarray, w: np.ndarray, h3: float) -> np.ndarray:
    u0, u1 = split_complex(u)
    v0, v1 = split_complex(v)
    w0, w1 = split_complex(w)

    parts = {
        (0,0,0): C_real(F, y0, u0, v0, w0, h3),
        (0,0,1): C_real(F, y0, u0, v0, w1, h3),
        (0,1,0): C_real(F, y0, u0, v1, w0, h3),
        (0,1,1): C_real(F, y0, u0, v1, w1, h3),
        (1,0,0): C_real(F, y0, u1, v0, w0, h3),
        (1,0,1): C_real(F, y0, u1, v0, w1, h3),
        (1,1,0): C_real(F, y0, u1, v1, w0, h3),
        (1,1,1): C_real(F, y0, u1, v1, w1, h3),
    }

    out = np.zeros_like(y0, dtype=complex)
    for su in (0,1):
        for sv in (0,1):
            for sw in (0,1):
                out += (1j)**(su+sv+sw) * parts[(su,sv,sw)].astype(complex)
    return out


# -------------------------
# eigen / biorthonormal projector
# -------------------------
def pick_conjugate_pair(J: np.ndarray, omega_target: float) -> Tuple[complex, complex, np.ndarray, np.ndarray]:
    """
    Returns (lam, lam_bar, q, qbar) from eig(J) as actual conjugate pair vectors.
    """
    evals, evecs = np.linalg.eig(J.astype(float))
    evals = evals.astype(complex)

    # choose best eigenvalue near unit circle and target omega with Im>0
    cand = []
    for i, lam in enumerate(evals):
        if np.imag(lam) <= 1e-12:
            continue
        score = abs(abs(lam) - 1.0) + 0.5 * abs(abs(np.angle(lam)) - abs(omega_target))
        cand.append((score, i, lam))

    if not cand:
        raise RuntimeError("No Im>0 eigenvalue found; NS pair not detected.")

    cand.sort(key=lambda t: t[0])
    _, i, lam = cand[0]

    # find its conjugate partner by nearest to conj(lam)
    j = int(np.argmin(np.abs(evals - np.conjugate(lam))))

    q = evecs[:, i].astype(complex)
    qbar = evecs[:, j].astype(complex)

    # normalize each to unit norm (scale free)
    q /= np.linalg.norm(q)
    qbar /= np.linalg.norm(qbar)

    return lam, evals[j], q, qbar


def pick_left_for(J: np.ndarray, target: complex, q_ref: np.ndarray, tol: float) -> Tuple[np.ndarray, int, float]:
    """
    Pick left eigenvector p from eig(J^T) whose eigenvalue is near target and has max |<p,q_ref>|.
    Returns (p_raw, idx, overlap_abs).
    """
    evals, evecs = np.linalg.eig(J.T)
    evals = evals.astype(complex)

    d = np.abs(evals - target)
    cand = np.where(d <= tol)[0]
    if cand.size == 0:
        cand = np.argsort(d)[:5]

    best = None
    for i in cand:
        p = evecs[:, i].astype(complex)
        ov = np.vdot(p, q_ref)
        sc = abs(ov)
        if best is None or sc > best[0]:
            best = (sc, i, p)
    assert best is not None
    sc, idx, p = best
    return p, int(idx), float(sc)


def biorthonormalize(Qm: np.ndarray, Pm: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Given Qm=[q1 q2], Pm=[p1 p2] (columns), build Pn so that Pn^H Qm = I.
    Returns (Qm, Pn, M) where M = Pm^H Qm.
    """
    M = Pm.conj().T @ Qm
    if np.linalg.cond(M) > 1e12:
        raise RuntimeError(f"Biorthonormalization ill-conditioned: cond(M)={np.linalg.cond(M):.3e}")
    Pn = Pm @ np.linalg.inv(M.conj().T)
    # check
    chk = Pn.conj().T @ Qm
    return Qm, Pn, chk


def ls_solve(A: np.ndarray, b: np.ndarray) -> Tuple[np.ndarray, float]:
    x, *_ = np.linalg.lstsq(A, b, rcond=None)
    res = np.linalg.norm(A @ x - b)
    return x, float(res)


# -------------------------
# main
# -------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description="NS l1 with biorthonormal center projector (v3).")
    ap.add_argument("--run_name", default=None)

    ap.add_argument("--dt", type=float, required=True)
    ap.add_argument("--gamma", type=float, required=True)

    ap.add_argument("--topology", default="ringdiag")
    ap.add_argument("--directed", action="store_true")
    ap.add_argument("--eps_asym", type=float, default=0.25)
    ap.add_argument("--deg_norm", default="false")
    ap.add_argument("--w_diag", type=float, default=0.85)
    ap.add_argument("--sigma2", type=float, default=0.5)
    ap.add_argument("--triad_phi", type=float, default=1.2)

    ap.add_argument("--ang_tol", type=float, default=1e-3)
    ap.add_argument("--bisect_iters", type=int, default=60)

    ap.add_argument("--hJ", type=float, default=1e-7)
    ap.add_argument("--h2", type=float, default=5e-5)
    ap.add_argument("--h3", type=float, default=1e-4)

    ap.add_argument("--left_tol", type=float, default=1e-6, help="Eigenvalue tolerance for left eigenvector selection.")
    ap.add_argument("--outdir", default="experiments/k4/ns_l1_projected_v3")
    args = ap.parse_args()

    deg_norm = parse_bool(args.deg_norm)
    run_name = args.run_name or f"l1proj_v3_phi{str(args.triad_phi).replace('.','p')}_dt{str(args.dt).replace('.','p')}_g{str(args.gamma).replace('.','p')}"

    k4p = K4Params(
        dt=args.dt, gamma=args.gamma,
        directed=args.directed, eps_asym=args.eps_asym, deg_norm=deg_norm,
        topology=args.topology, w_diag=args.w_diag, sigma2=args.sigma2, triad_phi=args.triad_phi,
    )
    spec = build_k4_spec(k4p)
    p = k4p

    ensure_dir(args.outdir)
    run_dir = os.path.join(args.outdir, run_name)
    ensure_dir(run_dir)

    K_spark, rho_star, omega_star, label = find_spark(p, spec, args.ang_tol, args.bisect_iters)
    print(f"[spark] K*={K_spark:.6g} rho={rho_star:.6g} omega={omega_star:.6g} label={label}")

    Q = gauge_free_basis(4)
    y0 = np.zeros(2 * Q.shape[1], dtype=float)

    def F(y_real: np.ndarray) -> np.ndarray:
        return F_map_real(y_real, K_spark, p, spec, Q)

    J = jacobian_fd(F, y0, args.hJ)
    lam, lam2, q, qbar = pick_conjugate_pair(J, omega_target=omega_star)

    # left eigenvectors for each right eigenvalue:
    # left eigenvector for λ solves J^T p = λ p? (for real J, left eigenvalues match λ)
    # We directly match eigenvalue λ in J^T for pλ, and λ̄ for pλ̄.
    p1_raw, i1, ov1 = pick_left_for(J, target=lam, q_ref=q, tol=args.left_tol)
    p2_raw, i2, ov2 = pick_left_for(J, target=lam2, q_ref=qbar, tol=args.left_tol)

    Qm = np.column_stack([q, qbar])
    Pm = np.column_stack([p1_raw, p2_raw])

    Qm, Pn, chk = biorthonormalize(Qm, Pm)

    Pc = Qm @ Pn.conj().T
    Ps = np.eye(J.shape[0], dtype=complex) - Pc

    Pc_norm = float(np.linalg.norm(Pc))
    idem = float(np.linalg.norm(Pc @ Pc - Pc))

    print(f"[J] λ={abs(lam):.12g}∠{float(np.angle(lam)):.6g}  λ2={abs(lam2):.12g}∠{float(np.angle(lam2)):.6g}")
    print(f"[left] idx=({i1},{i2}) overlap_abs=({ov1:.3e},{ov2:.3e})")
    print(f"[biorth] P^H Q ≈\n{chk}")
    print(f"[proj] ||Pc||_F={Pc_norm:.6g}  ||Pc^2-Pc||_F={idem:.6g}")

    # Choose p corresponding to q (first column after biorthonormalization)
    pvec = Pn[:, 0].astype(complex)

    # multilinear
    Bqq = B_complex(F, y0, q, q, args.h2)
    Bqqb = B_complex(F, y0, q, qbar, args.h2)
    Cqqqb = C_complex(F, y0, q, q, qbar, args.h3)

    I = np.eye(J.shape[0], dtype=complex)
    A11 = (I - J.astype(complex))
    A20 = (np.exp(2j * np.angle(lam)) * I - J.astype(complex))

    rhs11 = Ps @ Bqqb
    rhs20 = Ps @ Bqq

    h11, res11 = ls_solve(A11, rhs11)
    h20, res20 = ls_solve(A20, rhs20)

    h11 = Ps @ h11
    h20 = Ps @ h20

    term = Cqqqb + 2.0 * B_complex(F, y0, q, h11, args.h2) + B_complex(F, y0, qbar, h20, args.h2)
    c_raw = 0.5 * np.vdot(pvec, term)

    omega = float(np.angle(lam))
    c1 = 0.5 * np.exp(-1j * omega) * c_raw

    out: Dict[str, Any] = {
        "run_name": run_name,
        "dt": float(args.dt),
        "gamma": float(args.gamma),
        "triad_phi": float(args.triad_phi),
        "topology": args.topology,
        "directed": bool(args.directed),
        "eps_asym": float(args.eps_asym),
        "deg_norm": bool(deg_norm),
        "w_diag": float(args.w_diag),
        "sigma2": float(args.sigma2),
        "spark": {"K_spark": K_spark, "rho": rho_star, "omega_target": omega_star, "label": label},
        "fd_steps": {"hJ": args.hJ, "h2": args.h2, "h3": args.h3},
        "eig": {
            "lambda_re": float(np.real(lam)),
            "lambda_im": float(np.imag(lam)),
            "lambda_abs": float(abs(lam)),
            "lambda_arg": float(np.angle(lam)),
            "lambda2_re": float(np.real(lam2)),
            "lambda2_im": float(np.imag(lam2)),
            "Pc_norm": Pc_norm,
            "Pc_idempotence_norm": idem,
            "left_indices": [i1, i2],
            "left_overlap_abs": [ov1, ov2],
            "biorth_check": [[float(np.real(chk[0,0])), float(np.imag(chk[0,0]))],
                             [float(np.real(chk[0,1])), float(np.imag(chk[0,1]))],
                             [float(np.real(chk[1,0])), float(np.imag(chk[1,0]))],
                             [float(np.real(chk[1,1])), float(np.imag(chk[1,1]))]],
        },
        "resolvent": {
            "res11_norm": res11,
            "res20_norm": res20,
            "cond_I_minus_J": float(np.linalg.cond(A11)),
            "cond_e2iwI_minus_J": float(np.linalg.cond(A20)),
        },
        "coefficients": {
            "c_raw_re": float(np.real(c_raw)),
            "c_raw_im": float(np.imag(c_raw)),
            "l1_raw": float(np.real(c_raw)),
            "c1_re": float(np.real(c1)),
            "c1_im": float(np.imag(c1)),
            "l1_c1": float(np.real(c1)),
        },
        "note": "This version uses biorthonormal center projector from actual conjugate eigenvectors.",
    }

    out_path = os.path.join(run_dir, "ns_l1_projected_v3.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print(f"[l1] c_raw={out['coefficients']['c_raw_re']:.6g}{out['coefficients']['c_raw_im']:+.6g}i  l1_raw={out['coefficients']['l1_raw']:.6g}")
    print(f"[l1] c1   ={out['coefficients']['c1_re']:.6g}{out['coefficients']['c1_im']:+.6g}i  l1_c1 ={out['coefficients']['l1_c1']:.6g}")
    print(f"[res] res11={res11:.3g} res20={res20:.3g} cond11={out['resolvent']['cond_I_minus_J']:.3g} cond20={out['resolvent']['cond_e2iwI_minus_J']:.3g}")
    print(f"[OK] wrote {out_path}")


if __name__ == "__main__":
    main()
