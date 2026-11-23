# -*- coding: utf-8 -*-
"""
run_k3_scan.py

Same as before, but now SAFE:
- automatically caps requested face range to auditpack face count
- prevents IndexError when a seed has fewer faces than --face-max
"""

from __future__ import annotations

import argparse
import glob
import os
import subprocess
import sys
from pathlib import Path
from typing import List, Optional

import numpy as np
import pandas as pd


DEFAULT_SCRIPT = Path("scripts/esm/07_patch_autoflux_shear_probe.py")


def _resolve_one(run_dir: Path, patterns: List[str], required: bool = True) -> Optional[Path]:
    matches: List[Path] = []
    for pat in patterns:
        matches.extend(Path(p).resolve() for p in glob.glob(str(run_dir / pat)))
    matches = [p for p in matches if p.exists()]
    if not matches:
        if required:
            raise FileNotFoundError(f"No match in {run_dir} for patterns={patterns}")
        return None
    matches.sort(key=lambda p: p.stat().st_mtime, reverse=True)
    return matches[0]


def _audit_face_count(audit_npz: Path) -> int:
    npz = np.load(audit_npz, allow_pickle=True)
    if "faces" not in npz.files:
        raise KeyError(f"'faces' not found in auditpack {audit_npz}. Keys={npz.files}")
    faces = npz["faces"]
    if faces.ndim != 2 or faces.shape[1] != 3:
        raise ValueError(f"Unexpected faces shape {faces.shape} in {audit_npz}")
    return int(faces.shape[0])


def run_probe_for_seed(
    seed: int,
    run_dir: Path,
    out_dir: Path,
    requested_face_max: int,
    phi_full: float,
    alpha: float,
    rings: int,
    max_faces: int,
    refine: bool,
    lam_energy: float,
    refine_iters: int,
    refine_step0: float,
    refine_fd_eps: float,
    probe_script: Path,
    python_exe: str,
) -> Path:
    audit = _resolve_one(run_dir, ["*auditpack.npz", "auditpack.npz"])
    lift = _resolve_one(run_dir, ["*su2_lift*.npz", "su2_lift.npz"])

    n_faces_total = _audit_face_count(audit)
    face_max = min(int(requested_face_max), n_faces_total)
    if face_max <= 0:
        raise ValueError(f"[seed {seed}] auditpack has no faces? n_faces_total={n_faces_total}")

    face_ids = list(range(face_max))
    face_str = ",".join(str(x) for x in face_ids)

    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        python_exe, str(probe_script),
        "--audit", str(audit),
        "--lift", str(lift),
        "--outdir", str(out_dir),
        "--face_ids", face_str,
        "--rings", str(rings),
        "--max_faces", str(max_faces),
        "--phi_full", str(phi_full),
        "--alpha", str(alpha),
        "--lam_energy", str(lam_energy),
        "--refine_iters", str(refine_iters),
        "--refine_step0", str(refine_step0),
        "--refine_fd_eps", str(refine_fd_eps),
    ]
    if refine:
        cmd.append("--refine")

    print(f"\n[seed {seed}] run_dir={run_dir}")
    print(f"[seed {seed}] audit={audit.name} | lift={lift.name}")
    print(f"[seed {seed}] faces_total={n_faces_total} | requested_face_max={requested_face_max} | using_face_max={face_max}")
    print(f"[seed {seed}] running probe on {face_max} faces → {out_dir}")

    subprocess.run(cmd, check=True)

    csv_path = out_dir / "patch_autoflux_shear_results.csv"
    if not csv_path.exists():
        raise FileNotFoundError(f"Probe did not produce expected CSV: {csv_path}")
    return csv_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seeds", nargs="+", type=int, required=True)
    ap.add_argument("--face-max", type=int, default=80)
    ap.add_argument("--output-dir", type=str, default="data_phase3")
    ap.add_argument("--run-dir-template", type=str, default="validation_runs/locked_run_{seed}_rank_0")
    ap.add_argument("--probe-script", type=str, default=str(DEFAULT_SCRIPT))
    ap.add_argument("--python", type=str, default=sys.executable)

    ap.add_argument("--phi-full", type=float, default=2.0948)
    ap.add_argument("--alpha", type=float, default=1.57079632679)
    ap.add_argument("--rings", type=int, default=2)
    ap.add_argument("--max-faces", type=int, default=80)
    ap.add_argument("--refine", action="store_true", default=True)
    ap.add_argument("--no-refine", dest="refine", action="store_false")
    ap.add_argument("--lam-energy", type=float, default=0.01)
    ap.add_argument("--refine-iters", type=int, default=120)
    ap.add_argument("--refine-step0", type=float, default=0.1)
    ap.add_argument("--refine-fd-eps", type=float, default=1e-7)
    ap.add_argument("--probe-out-root", type=str, default="experiments/esm/phase3_pi2")

    args = ap.parse_args()

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    probe_script = Path(args.probe_script).resolve()
    if not probe_script.exists():
        raise FileNotFoundError(f"Probe script not found: {probe_script}")

    for seed in args.seeds:
        run_dir = Path(args.run_dir_template.format(seed=seed)).resolve()
        if not run_dir.exists():
            raise FileNotFoundError(f"Run dir does not exist: {run_dir}")

        probe_out = (Path(args.probe_out_root) / f"seed_{seed:02d}").resolve()

        csv_path = run_probe_for_seed(
            seed=seed,
            run_dir=run_dir,
            out_dir=probe_out,
            requested_face_max=args.face_max,
            phi_full=args.phi_full,
            alpha=args.alpha,
            rings=args.rings,
            max_faces=args.max_faces,
            refine=args.refine,
            lam_energy=args.lam_energy,
            refine_iters=args.refine_iters,
            refine_step0=args.refine_step0,
            refine_fd_eps=args.refine_fd_eps,
            probe_script=probe_script,
            python_exe=args.python,
        )

        df = pd.read_csv(csv_path)
        df.insert(0, "seed", seed)

        out_csv = output_dir / f"k3_scan_seed{seed}.csv"
        df.to_csv(out_csv, index=False)
        print(f"[seed {seed}] wrote: {out_csv} (rows={len(df)})")

    print("\nDone.")


if __name__ == "__main__":
    main()
