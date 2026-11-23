# -*- coding: utf-8 -*-
r"""
scripts/esm/07_patch_autoflux_shear_probe.py

Cluster patch biopsy v2.1 (ACTIVE-FACES CORRECT + LIFT GUARDS)

Fixes vs v2:
  ✅ Loads --lift and validates edges match auditpack (prevents silent mismatch).
  ✅ Computes holonomy loss / gap ONLY on active faces (where |F_local|>eps_F).
     (Previously, inactive faces were also constrained, biasing results.)
  ✅ Adds safety guards for empty active sets and near-zero K3 baseline.
  ✅ Keeps outputs identical schema, but now "gap_*" is the active-face max gap.

No SciPy. Pure NumPy/Pandas.
"""

from __future__ import annotations

import os
import json
import argparse
from collections import defaultdict, deque
from typing import Dict, List, Tuple, Optional

import numpy as np
import pandas as pd

from rtg.algebra.su2 import exp_su2, su2_log, fro_norm


# ----------------------------
# IO
# ----------------------------
def load_npz(path: str) -> np.lib.npyio.NpzFile:
    return np.load(path, allow_pickle=True)


def ensure_dir(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def save_json(path: str, data: Dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


# ----------------------------
# Geometry helpers
# ----------------------------
def _unit(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=float).reshape(3)
    n = float(np.linalg.norm(v))
    if n == 0.0:
        return np.array([0.0, 0.0, 1.0], dtype=float)
    return v / n


def face_nodes(face: np.ndarray) -> List[int]:
    return [int(x) for x in face]


def face_boundary_edges(face: np.ndarray) -> List[Tuple[int, int]]:
    ns = face_nodes(face)
    out = []
    for i in range(len(ns)):
        out.append((ns[i], ns[(i + 1) % len(ns)]))
    return out


def face_edges_undirected(face: np.ndarray) -> List[Tuple[int, int]]:
    ns = face_nodes(face)
    out = []
    for i in range(len(ns)):
        u, v = ns[i], ns[(i + 1) % len(ns)]
        out.append((min(u, v), max(u, v)))
    return out


def build_face_adjacency_by_edge(faces: np.ndarray) -> Dict[int, List[int]]:
    edge_to_faces = defaultdict(list)
    for f_idx in range(faces.shape[0]):
        for e in face_edges_undirected(faces[f_idx]):
            edge_to_faces[e].append(f_idx)

    adj = defaultdict(set)
    for _, flist in edge_to_faces.items():
        if len(flist) <= 1:
            continue
        for i in range(len(flist)):
            a = flist[i]
            for j in range(i + 1, len(flist)):
                b = flist[j]
                adj[a].add(b)
                adj[b].add(a)

    return {k: sorted(list(v)) for k, v in adj.items()}


def collect_patch_faces(start_face: int, adj: Dict[int, List[int]], rings: int, max_faces: int) -> List[int]:
    visited = set([start_face])
    q = deque([(start_face, 0)])
    order = [start_face]

    while q and len(order) < max_faces:
        u, d = q.popleft()
        if d >= rings:
            continue
        for v in adj.get(u, []):
            if v in visited:
                continue
            visited.add(v)
            order.append(v)
            q.append((v, d + 1))
            if len(order) >= max_faces:
                break
    return order


def build_edge_maps(edges: np.ndarray) -> Tuple[Dict[Tuple[int, int], int], Dict[Tuple[int, int], int]]:
    oriented = {}
    undirected = {}
    for i, e in enumerate(edges):
        u = int(e[0]); v = int(e[1])
        oriented[(u, v)] = i
        undirected[(min(u, v), max(u, v))] = i
    return oriented, undirected


# ----------------------------
# Local patch operators
# ----------------------------
def local_incidence_B(
    faces_global: np.ndarray,
    edges_global: np.ndarray,
    patch_face_ids: List[int],
) -> Tuple[np.ndarray, List[int], Dict[int, int]]:
    """
    Returns:
      B_local: (nF_local, nE_local)
      edge_ids_global: list of global edge indices in local patch
      global_edge_to_local: dict global_edge_idx -> local_edge_idx
    """
    oriented_map, undirected_map = build_edge_maps(edges_global)

    edge_set = set()
    for fid in patch_face_ids:
        for (u, v) in face_boundary_edges(faces_global[fid]):
            if (u, v) in oriented_map:
                edge_set.add(oriented_map[(u, v)])
            elif (v, u) in oriented_map:
                edge_set.add(oriented_map[(v, u)])
            else:
                ge = undirected_map.get((min(u, v), max(u, v)), None)
                if ge is not None:
                    edge_set.add(ge)

    edge_ids = sorted(list(edge_set))
    global_to_local = {ge: i for i, ge in enumerate(edge_ids)}

    B = np.zeros((len(patch_face_ids), len(edge_ids)), dtype=float)

    for lf, fid in enumerate(patch_face_ids):
        for (u, v) in face_boundary_edges(faces_global[fid]):
            if (u, v) in oriented_map:
                ge = oriented_map[(u, v)]
                sign = +1.0
            elif (v, u) in oriented_map:
                ge = oriented_map[(v, u)]
                sign = -1.0
            else:
                ge = undirected_map.get((min(u, v), max(u, v)), None)
                if ge is None:
                    continue
                u0 = int(edges_global[ge][0]); v0 = int(edges_global[ge][1])
                sign = +1.0 if (u, v) == (u0, v0) else -1.0

            if ge in global_to_local:
                B[lf, global_to_local[ge]] = sign

    return B, edge_ids, global_to_local


def pick_seed_edge_local_from_target_face(
    faces_global: np.ndarray,
    edges_global: np.ndarray,
    target_face_id: int,
    global_edge_to_local: Dict[int, int],
) -> int:
    """
    Choose a seed edge for autoflux: first boundary edge of target face that exists in local edge list.
    """
    oriented_map, undirected_map = build_edge_maps(edges_global)

    for (u, v) in face_boundary_edges(faces_global[target_face_id]):
        if (u, v) in oriented_map:
            ge = oriented_map[(u, v)]
        elif (v, u) in oriented_map:
            ge = oriented_map[(v, u)]
        else:
            ge = undirected_map.get((min(u, v), max(u, v)), None)
            if ge is None:
                continue
        if ge in global_edge_to_local:
            return int(global_edge_to_local[ge])

    return 0


def autoflux_F_local(B_local: np.ndarray, phi_full: float, seed_edge_local: int) -> np.ndarray:
    """
    a_seed[seed_edge] = phi_full/2   (half-angle scalar)
    F_local = 2*(B @ a_seed)         (full face angles)
    """
    E = B_local.shape[1]
    a_seed = np.zeros(E, dtype=float)
    a_seed[int(seed_edge_local)] = float(phi_full) / 2.0
    return 2.0 * (B_local @ a_seed)


def active_faces_from_F(F_local: np.ndarray, eps_F: float) -> List[int]:
    return [i for i in range(F_local.size) if abs(float(F_local[i])) > eps_F]


# ----------------------------
# Patch SU(2) loss / refinement
# ----------------------------
def edges_to_U_from_halfA(A_edges_half: np.ndarray) -> List[np.ndarray]:
    A = np.asarray(A_edges_half, dtype=float)
    return [exp_su2(2.0 * A[e]) for e in range(A.shape[0])]


def face_holonomy(U_edges: List[np.ndarray], B: np.ndarray, f: int) -> np.ndarray:
    H = np.eye(2, dtype=complex)
    # NOTE: left-multiply convention (consistent within this script)
    for e in range(B.shape[1]):
        c = B[f, e]
        if c == 0.0:
            continue
        U = U_edges[e]
        if c < 0.0:
            U = U.conj().T
        H = U @ H
    return H


def max_gap_patch(U_edges: List[np.ndarray], B: np.ndarray, F_faces: np.ndarray,
                  active_faces: Optional[List[int]] = None) -> float:
    faces_to_check = range(B.shape[0]) if (active_faces is None) else active_faces
    mg = 0.0
    for f in faces_to_check:
        Hf = face_holonomy(U_edges, B, f)
        tr_half = float(np.real(np.trace(Hf) / 2.0))
        tr_half = float(np.clip(tr_half, -1.0, 1.0))
        cos_half = float(np.cos(0.5 * float(F_faces[f])))
        mg = max(mg, abs(tr_half - cos_half))
    return float(mg)


def loss_components(
    A_edges: np.ndarray,
    B: np.ndarray,
    F_faces: np.ndarray,
    axes: List[np.ndarray],
    lam_energy: float,
    active_faces: Optional[List[int]] = None,
) -> Tuple[float, float, float]:
    A_edges = np.asarray(A_edges, dtype=float).reshape(B.shape[1], 3)
    U_edges = edges_to_U_from_halfA(A_edges)

    faces_to_use = range(B.shape[0]) if (active_faces is None) else active_faces

    # Target holonomies for used faces only
    Ht = {}
    for f in faces_to_use:
        n = _unit(axes[f])
        Ht[f] = exp_su2(float(F_faces[f]) * n)

    L_holo = 0.0
    for f in faces_to_use:
        Hc = face_holonomy(U_edges, B, f)
        diff = Ht[f].conj().T @ Hc
        X = su2_log(diff)
        L_holo += fro_norm(X) ** 2

    L_energy = float(np.sum(A_edges**2))
    return float(L_holo + lam_energy * L_energy), float(L_holo), float(L_energy)


def grad_fd_central(
    A_edges: np.ndarray,
    B: np.ndarray,
    F_faces: np.ndarray,
    axes: List[np.ndarray],
    lam_energy: float,
    eps: float,
    active_faces: Optional[List[int]] = None,
) -> np.ndarray:
    x = np.asarray(A_edges, dtype=float).reshape(-1)
    g = np.zeros_like(x)

    for k in range(x.size):
        xp = x.copy(); xp[k] += eps
        xm = x.copy(); xm[k] -= eps
        Lp, _, _ = loss_components(xp.reshape(B.shape[1], 3), B, F_faces, axes, lam_energy, active_faces=active_faces)
        Lm, _, _ = loss_components(xm.reshape(B.shape[1], 3), B, F_faces, axes, lam_energy, active_faces=active_faces)
        g[k] = (Lp - Lm) / (2.0 * eps)

    return g.reshape(B.shape[1], 3)


def refine_patch(
    A_init: np.ndarray,
    B: np.ndarray,
    F_faces: np.ndarray,
    axes: List[np.ndarray],
    lam_energy: float,
    iters: int,
    step0: float,
    fd_eps: float,
    active_faces: Optional[List[int]] = None,
) -> Tuple[np.ndarray, Dict[str, float]]:
    A = np.asarray(A_init, dtype=float).copy()
    step = float(step0)
    L, Lh, Le = loss_components(A, B, F_faces, axes, lam_energy, active_faces=active_faces)

    for _ in range(iters):
        g = grad_fd_central(A, B, F_faces, axes, lam_energy, fd_eps, active_faces=active_faces)
        gnorm = float(np.linalg.norm(g))
        if gnorm < 1e-9:
            break

        accepted = False
        for _ in range(25):
            A_try = A - step * g
            L_try, _, _ = loss_components(A_try, B, F_faces, axes, lam_energy, active_faces=active_faces)
            if L_try < L:
                A = A_try
                L = L_try
                accepted = True
                break
            step *= 0.5
            if step < 1e-6:
                break
        if not accepted:
            break

    Lf, Lhf, Lef = loss_components(A, B, F_faces, axes, lam_energy, active_faces=active_faces)
    stats = {"L_total": float(Lf), "L_holo": float(Lhf), "L_energy_half": float(Lef), "step_final": float(step)}
    return A, stats


def ls_halfangle_lift_patch(B: np.ndarray, F_faces: np.ndarray, axes: List[np.ndarray], lambda_reg: float) -> np.ndarray:
    F = np.asarray(F_faces, dtype=float).reshape(-1)
    axes_u = [_unit(a) for a in axes]

    C = np.kron(B, np.eye(3))
    b = np.zeros(3 * F.size, dtype=float)
    for f in range(F.size):
        b[3*f:3*f+3] = 0.5 * F[f] * axes_u[f]

    if lambda_reg == 0.0:
        A_flat, *_ = np.linalg.lstsq(C, b, rcond=None)
    else:
        CT = C.T
        M = CT @ C + float(lambda_reg) * np.eye(C.shape[1])
        rhs = CT @ b
        A_flat = np.linalg.solve(M, rhs)

    return A_flat.reshape(B.shape[1], 3)


# ----------------------------
# Axes for SAME vs OPP
# ----------------------------
def axes_same_opp(alpha: float, n_faces: int, active_faces: List[int], mode: str) -> List[np.ndarray]:
    mode = "same" if mode.lower() == "same" else "opp"
    n_plus = np.array([np.sin(alpha), 0.0, np.cos(alpha)], dtype=float)
    n_minus = np.array([-np.sin(alpha), 0.0, np.cos(alpha)], dtype=float)
    z = np.array([0.0, 0.0, 1.0], dtype=float)

    axes = [z.copy() for _ in range(n_faces)]
    act = sorted(active_faces)
    if not act:
        return axes

    if mode == "same":
        for f in act:
            axes[f] = n_plus.copy()
    else:
        axes[act[0]] = n_plus.copy()
        for f in act[1:]:
            axes[f] = n_minus.copy()
    return axes


def k3_iso_full_sum(F_local: np.ndarray, active_faces: List[int]) -> float:
    """
    K3 baseline full energy per face: F^2/3
    Region baseline: sum over active faces.
    """
    s = 0.0
    for f in active_faces:
        F = float(F_local[f])
        s += (F * F) / 3.0
    return float(s)


# ----------------------------
# Target selection
# ----------------------------
def pick_targets_from_components(components_csv: str, top_singletons: int) -> List[int]:
    df = pd.read_csv(components_csv)
    sizes = df["component_id"].value_counts()
    big = sizes[sizes >= 2].index.tolist()

    targets = []
    for cid in big:
        targets.extend(df[df["component_id"] == cid]["face_id"].astype(int).tolist())

    # add best singleton MATTER by lowest gap
    singletons = sizes[sizes == 1].index.tolist()
    if top_singletons > 0 and len(singletons) > 0:
        sdf = df[df["component_id"].isin(singletons)].copy()
        sdf = sdf.sort_values("gap", ascending=True)
        targets.extend(sdf.head(int(top_singletons))["face_id"].astype(int).tolist())

    # unique preserve order
    seen = set()
    out = []
    for t in targets:
        if int(t) not in seen:
            out.append(int(t))
            seen.add(int(t))
    return out


def parse_face_ids(face_ids: str) -> List[int]:
    if not face_ids.strip():
        return []
    parts = face_ids.replace(" ", "").split(",")
    return [int(p) for p in parts if p != ""]


# ----------------------------
# Lift/audit compatibility guard
# ----------------------------
def _edges_set(edges: np.ndarray) -> set:
    # use oriented pairs as stored; this should match if lift created from this audit
    return {tuple(map(int, e)) for e in edges}


def validate_lift_matches_audit(edges_audit: np.ndarray, edges_lift: np.ndarray) -> None:
    if edges_lift.shape != edges_audit.shape:
        raise SystemExit(f"[ERROR] lift edges shape {edges_lift.shape} != audit edges shape {edges_audit.shape}")
    if np.array_equal(edges_lift, edges_audit):
        print("[OK] lift edges match audit edges exactly.")
        return
    # fallback: set equality
    if _edges_set(edges_lift) != _edges_set(edges_audit):
        raise SystemExit("[ERROR] lift edges do not match audit edges (set mismatch).")
    print("[WARN] lift edges are a permutation of audit edges. "
          "Proceeding, but if any downstream assumes ordering, fix lift to match order.")


# ----------------------------
# Main
# ----------------------------
def main() -> None:
    ap = argparse.ArgumentParser(description="Patch autoflux shear probe (same vs opp) on cluster faces")

    ap.add_argument("--audit", required=True)
    ap.add_argument("--lift", required=True)
    ap.add_argument("--outdir", required=True)

    ap.add_argument("--components", default="", help="matter_components.csv (optional)")
    ap.add_argument("--face_ids", default="", help="comma-separated explicit face ids (optional)")
    ap.add_argument("--top_singletons", type=int, default=1)

    ap.add_argument("--rings", type=int, default=1)
    ap.add_argument("--max_faces", type=int, default=30)

    ap.add_argument("--phi_full", type=float, default=2.0948, help="seed twist angle for autoflux (full)")
    ap.add_argument("--eps_F", type=float, default=1e-9)

    ap.add_argument("--alpha", type=float, default=float(np.pi / 2.0))
    ap.add_argument("--lambda_reg_ls", type=float, default=0.0)

    ap.add_argument("--refine", action="store_true")
    ap.add_argument("--lam_energy", type=float, default=0.01)
    ap.add_argument("--refine_iters", type=int, default=80)
    ap.add_argument("--refine_step0", type=float, default=0.1)
    ap.add_argument("--refine_fd_eps", type=float, default=1e-7)

    args = ap.parse_args()
    ensure_dir(args.outdir)

    d_geo = load_npz(args.audit)
    edges = d_geo["edges"]
    faces = d_geo["faces"]

    d_lift = load_npz(args.lift)
    edges_lift = d_lift["edges"]
    validate_lift_matches_audit(edges, edges_lift)

    adj = build_face_adjacency_by_edge(faces)

    targets = []
    if args.components.strip():
        targets = pick_targets_from_components(args.components, int(args.top_singletons))
    if args.face_ids.strip():
        targets = parse_face_ids(args.face_ids)

    print("[probe] targets:", targets)
    if not targets:
        raise SystemExit("No targets selected. Provide --components or --face_ids.")

    rows = []

    for face_id in targets:
        patch_faces = collect_patch_faces(int(face_id), adj, rings=int(args.rings), max_faces=int(args.max_faces))
        if int(face_id) not in patch_faces:
            print(f"[WARN] face {face_id} not in its own patch list (unexpected). Skipping.")
            continue

        B_local, edge_ids_global, global_to_local = local_incidence_B(faces, edges, patch_faces)
        seed_edge_local = pick_seed_edge_local_from_target_face(faces, edges, int(face_id), global_to_local)

        # autoflux target (local)
        F_local = autoflux_F_local(B_local, float(args.phi_full), seed_edge_local)
        active_local = active_faces_from_F(F_local, float(args.eps_F))

        if len(active_local) == 0:
            print(f"[probe] face={face_id} patch(F={B_local.shape[0]},E={B_local.shape[1]}) active=0 → skipping (no flux).")
            continue

        # K3 baseline for active faces
        C_iso_full = k3_iso_full_sum(F_local, active_local)
        if C_iso_full < 1e-12:
            print(f"[probe] face={face_id} C_iso_full≈0 → skipping.")
            continue

        out = {
            "face_id": int(face_id),
            "patch_n_faces": int(B_local.shape[0]),
            "patch_n_edges": int(B_local.shape[1]),
            "seed_edge_local": int(seed_edge_local),
            "n_active_faces": int(len(active_local)),
            "C_iso_full": float(C_iso_full),
        }

        # Run SAME and OPP
        for mode in ["same", "opp"]:
            axes = axes_same_opp(float(args.alpha), B_local.shape[0], active_local, mode)

            # LS
            A_ls = ls_halfangle_lift_patch(B_local, F_local, axes, float(args.lambda_reg_ls))
            U_ls = edges_to_U_from_halfA(A_ls)
            gap_ls = max_gap_patch(U_ls, B_local, F_local, active_faces=active_local)
            E_ls_full = float(4.0 * np.sum(A_ls**2))

            out[f"E_ls_{mode}"] = float(E_ls_full)
            out[f"gap_ls_{mode}"] = float(gap_ls)
            out[f"kappa_ls_{mode}"] = float(E_ls_full / C_iso_full)

            if args.refine:
                A_ref, st_ref = refine_patch(
                    A_init=A_ls,
                    B=B_local,
                    F_faces=F_local,
                    axes=axes,
                    lam_energy=float(args.lam_energy),
                    iters=int(args.refine_iters),
                    step0=float(args.refine_step0),
                    fd_eps=float(args.refine_fd_eps),
                    active_faces=active_local,  # ✅ only active faces constrain loss
                )
                U_ref = edges_to_U_from_halfA(A_ref)
                gap_ref = max_gap_patch(U_ref, B_local, F_local, active_faces=active_local)
                E_ref_full = float(4.0 * np.sum(A_ref**2))

                out[f"E_ref_{mode}"] = float(E_ref_full)
                out[f"gap_ref_{mode}"] = float(gap_ref)
                out[f"kappa_ref_{mode}"] = float(E_ref_full / C_iso_full)
                out[f"L_holo_{mode}"] = float(st_ref["L_holo"])
                out[f"L_energy_half_{mode}"] = float(st_ref["L_energy_half"])
            else:
                out[f"E_ref_{mode}"] = float("nan")
                out[f"gap_ref_{mode}"] = float("nan")
                out[f"kappa_ref_{mode}"] = float("nan")
                out[f"L_holo_{mode}"] = float("nan")
                out[f"L_energy_half_{mode}"] = float("nan")

        # Ratios (only meaningful if refine)
        if args.refine:
            out["percolation_ratio_E"] = float(out["E_ref_opp"] / out["E_ref_same"]) if out["E_ref_same"] > 0 else float("nan")
            out["percolation_ratio_kappa"] = float(out["kappa_ref_opp"] / out["kappa_ref_same"]) if out["kappa_ref_same"] > 0 else float("nan")
            out["gap_ratio_ref"] = float(out["gap_ref_opp"] / out["gap_ref_same"]) if out["gap_ref_same"] > 0 else float("nan")

        rows.append(out)

        msg = f"[probe] face={face_id} patch(F={out['patch_n_faces']},E={out['patch_n_edges']}) active={out['n_active_faces']} "
        msg += f"| REF same E={out.get('E_ref_same', float('nan')):.3f} gap={out.get('gap_ref_same', float('nan')):.3e} "
        msg += f"| REF opp E={out.get('E_ref_opp', float('nan')):.3f} gap={out.get('gap_ref_opp', float('nan')):.3e} "
        if args.refine:
            msg += f"| ratio={out.get('percolation_ratio_E', float('nan')):.2f}x"
        print(msg)

    df_out = pd.DataFrame(rows)
    out_csv = os.path.join(args.outdir, "patch_autoflux_shear_results.csv")
    df_out.to_csv(out_csv, index=False)

    meta = {
        "audit": args.audit,
        "lift": args.lift,
        "targets": targets,
        "params": {
            "rings": int(args.rings),
            "max_faces": int(args.max_faces),
            "phi_full": float(args.phi_full),
            "alpha": float(args.alpha),
            "eps_F": float(args.eps_F),
            "lambda_reg_ls": float(args.lambda_reg_ls),
            "refine": bool(args.refine),
            "lam_energy": float(args.lam_energy),
            "refine_iters": int(args.refine_iters),
            "refine_step0": float(args.refine_step0),
            "refine_fd_eps": float(args.refine_fd_eps),
            "active_faces_only": True,
        },
    }
    save_json(os.path.join(args.outdir, "patch_autoflux_shear_summary.json"), meta)

    print("[save]", out_csv)
    print("[save]", os.path.join(args.outdir, "patch_autoflux_shear_summary.json"))


if __name__ == "__main__":
    main()
