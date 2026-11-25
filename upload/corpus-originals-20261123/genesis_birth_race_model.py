#!/usr/bin/env python3
"""
Genesis II primitive K4 birth-race model
========================================

Deterministic scalar closure wrapper for the Genesis II K4-shadow primitive
birth-race problem. This script is intentionally a *wrapper*, not a new
coefficient-certification engine. Coefficients are imported from the verified
Genesis II route-census layer and from the closed primitive Q_d polynomial.

State variables are six-step block amplitudes:
    Qs, Qc, Qd

Default model: tetrahedral-shadow K4 race at transverse birth gauge I_sc=0.
    dQs = 1/4 Qs^2 + 5/9 Qs Qc
    dQc = 5/12 Qs Qc + 1/3 Qc^2
    Qd seed after the first vector block = 7/1024 Qs0^3 + optional c^3 seed

Closures:
    uniform   : closed negative control, always a sink
    angles    : deterministic phase-angle substitution into the full P4 law
    parametric: reduced scalar growth model dQd = alpha Qs Qd + beta Qc Qd - gamma Qd^2

Important scope notes:
  * The dyadic plateau phase law is not assumed here. If you use --closure angles,
    you must provide angles or an external phase-update policy.
  * The model reports first threshold crossing for Qs/Qc primitive-control loss
    and Qd cascade. It does not claim physical phase closure.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Literal, Optional, Tuple

SQRT3 = math.sqrt(3.0)

ClosureName = Literal["uniform", "angles", "parametric", "frozen"]
ModelName = Literal["shadow", "standalone_c"]


def kappa_value(name_or_value: str) -> float:
    """Parse kappa preset or numeric value."""
    key = name_or_value.strip().lower()
    if key == "shear":
        return -2.0 * SQRT3 / 3.0
    if key == "recoil":
        return -0.5
    return float(name_or_value)


@dataclass(frozen=True)
class RaceConfig:
    qs0: float = 1.0e-2
    kappa: float = -2.0 * SQRT3 / 3.0
    model: ModelName = "shadow"
    closure: ClosureName = "uniform"
    max_blocks: int = 200_000
    qs_ctrl: float = 0.1
    qc_ctrl: float = 0.1
    qd_threshold: float = 0.05
    include_c3_seed: bool = True
    # Angle-closure parameters, radians. Default phi_sc=pi/2 encodes I_sc=0.
    phi_ds: float = 0.0
    phi_dc: float = 0.0
    phi_sc: float = math.pi / 2.0
    # Parametric closure coefficients.
    alpha: float = 0.0
    beta: float = 0.0
    gamma: float = 1.0
    clamp_nonnegative: bool = True


@dataclass
class RaceState:
    n: int
    qs: float
    qc: float
    qd: float
    dqs: float = 0.0
    dqc: float = 0.0
    dqd: float = 0.0
    event: str = ""


def initial_state(cfg: RaceConfig) -> RaceState:
    """Initialize after the vector d-seeding block is inserted."""
    qs0 = cfg.qs0
    qc0 = (cfg.kappa * cfg.kappa) * qs0**3
    qd1 = (7.0 / 1024.0) * qs0**3
    if cfg.include_c3_seed:
        qd1 += (61.0 / 34992.0) * qc0**3
    return RaceState(n=1, qs=qs0, qc=qc0, qd=qd1, event="seeded")


def qc_mixed_coefficient(model: ModelName) -> float:
    if model == "shadow":
        return 5.0 / 12.0
    if model == "standalone_c":
        return 3.0 / 4.0
    raise ValueError(f"unknown model: {model}")


def base_dqs(qs: float, qc: float) -> float:
    """K4-shadow birth-gauge Delta Q_s at I_sc=0."""
    return 0.25 * qs * qs + (5.0 / 9.0) * qs * qc


def base_dqc(qs: float, qc: float, model: ModelName = "shadow") -> float:
    """Birth-gauge Delta Q_c. Shadow uses 5/12; standalone comparison uses 3/4."""
    return qc_mixed_coefficient(model) * qs * qc + (1.0 / 3.0) * qc * qc


def uniform_closure(qs: float, qc: float, qd: float, cfg: RaceConfig) -> float:
    """Uniform independent phase average: closed negative control."""
    return -qd * qd - (1.0 / 12.0) * qd * qs - (1.0 / 9.0) * qd * qc


def invariant_from_angle(qa: float, qb: float, phi: float) -> Tuple[float, float]:
    """
    Return (I_ab, omega_ab) using the Genesis B-phase convention:
        I_ab = sqrt(Qa Qb) cos(phi)
        (sqrt(3)/2) omega_ab = sqrt(Qa Qb) sin(phi)
    so omega_ab = 2/sqrt(3) sqrt(Qa Qb) sin(phi).
    """
    amp = math.sqrt(max(qa, 0.0) * max(qb, 0.0))
    return amp * math.cos(phi), (2.0 / SQRT3) * amp * math.sin(phi)


def p4_full(
    qs: float,
    qc: float,
    qd: float,
    ids: float,
    wds: float,
    idc: float,
    wdc: float,
    isc: float,
    wsc: float,
) -> float:
    """Closed primitive Q_d quartic drift polynomial P4(s,c,d)."""
    return (
        -qd * qd
        - (1.0 / 8.0) * qs * ids
        - (3.0 / 32.0) * qs * wds
        - (1.0 / 27.0) * qc * idc
        + (7.0 / 108.0) * qc * wdc
        - (5.0 / 12.0) * wds * ids
        - (1.0 / 8.0) * wds * wds
        - (5.0 / 9.0) * wdc * idc
        - (1.0 / 6.0) * wdc * wdc
        + (1.0 / 36.0) * qs * idc
        - (7.0 / 48.0) * qs * wdc
        + (1.0 / 18.0) * ids * isc
        + (7.0 / 72.0) * ids * wsc
        + (1.0 / 6.0) * qc * ids
        + (3.0 / 8.0) * qc * wds
        + (1.0 / 3.0) * idc * isc
        + (1.0 / 4.0) * idc * wsc
    )


def angle_closure(qs: float, qc: float, qd: float, cfg: RaceConfig) -> float:
    ids, wds = invariant_from_angle(qd, qs, cfg.phi_ds)
    idc, wdc = invariant_from_angle(qd, qc, cfg.phi_dc)
    isc, wsc = invariant_from_angle(qs, qc, cfg.phi_sc)
    return p4_full(qs, qc, qd, ids, wds, idc, wdc, isc, wsc)


def parametric_closure(qs: float, qc: float, qd: float, cfg: RaceConfig) -> float:
    """Exploratory scalar closure for sensitivity scans."""
    return cfg.alpha * qs * qd + cfg.beta * qc * qd - cfg.gamma * qd * qd


def frozen_closure(qs: float, qc: float, qd: float, cfg: RaceConfig) -> float:
    return 0.0


def closure_delta(qs: float, qc: float, qd: float, cfg: RaceConfig) -> float:
    if cfg.closure == "uniform":
        return uniform_closure(qs, qc, qd, cfg)
    if cfg.closure == "angles":
        return angle_closure(qs, qc, qd, cfg)
    if cfg.closure == "parametric":
        return parametric_closure(qs, qc, qd, cfg)
    if cfg.closure == "frozen":
        return frozen_closure(qs, qc, qd, cfg)
    raise ValueError(f"unknown closure: {cfg.closure}")


def classify_event(qs: float, qc: float, qd: float, cfg: RaceConfig) -> str:
    events = []
    if qd >= cfg.qd_threshold:
        events.append("cascade")
    if qs >= cfg.qs_ctrl:
        events.append("Qs_ctrl")
    if qc >= cfg.qc_ctrl:
        events.append("Qc_ctrl")
    if not (math.isfinite(qs) and math.isfinite(qc) and math.isfinite(qd)):
        events.append("nonfinite")
    return "+".join(events)


def step_state(st: RaceState, cfg: RaceConfig) -> RaceState:
    dqs = base_dqs(st.qs, st.qc)
    dqc = base_dqc(st.qs, st.qc, cfg.model)
    dqd = closure_delta(st.qs, st.qc, st.qd, cfg)
    qs = st.qs + dqs
    qc = st.qc + dqc
    qd = st.qd + dqd
    if cfg.clamp_nonnegative:
        qs = max(qs, 0.0)
        qc = max(qc, 0.0)
        qd = max(qd, 0.0)
    event = classify_event(qs, qc, qd, cfg)
    return RaceState(n=st.n + 1, qs=qs, qc=qc, qd=qd, dqs=dqs, dqc=dqc, dqd=dqd, event=event)


def simulate(cfg: RaceConfig, keep_every: int = 1) -> Tuple[List[RaceState], Dict[str, Optional[int]]]:
    st = initial_state(cfg)
    history: List[RaceState] = [st]
    first_events: Dict[str, Optional[int]] = {"cascade": None, "Qs_ctrl": None, "Qc_ctrl": None, "nonfinite": None}

    # Check initial seed against thresholds too.
    initial_event = classify_event(st.qs, st.qc, st.qd, cfg)
    if initial_event:
        for ev in initial_event.split("+"):
            first_events[ev] = st.n

    for _ in range(cfg.max_blocks):
        if any(first_events.values()):
            break
        st = step_state(st, cfg)
        if st.n % keep_every == 0 or st.event:
            history.append(st)
        if st.event:
            for ev in st.event.split("+"):
                if first_events.get(ev) is None:
                    first_events[ev] = st.n
            break
    else:
        # Ensure final state is present if not already kept.
        if history[-1].n != st.n:
            history.append(st)

    return history, first_events


def analytic_shadow_leading(qs0: float, qc0: float, t: float) -> Tuple[float, float]:
    """Leading continuous shadow solution with dQs=1/4 Qs^2, dQc=5/12 Qs Qc."""
    denom = 1.0 - 0.25 * qs0 * t
    if denom <= 0:
        return math.inf, math.inf
    qs = qs0 / denom
    qc = qc0 * denom ** (-5.0 / 3.0)
    return qs, qc


def write_csv(path: str, history: Iterable[RaceState]) -> None:
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["n", "Qs", "Qc", "Qd", "dQs", "dQc", "dQd", "event"])
        for st in history:
            writer.writerow([st.n, st.qs, st.qc, st.qd, st.dqs, st.dqc, st.dqd, st.event])


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Genesis II K4 primitive birth-race scalar wrapper")
    p.add_argument("--qs0", type=float, default=1.0e-2)
    p.add_argument("--kappa", default="shear", help="shear, recoil, or numeric")
    p.add_argument("--model", choices=["shadow", "standalone_c"], default="shadow")
    p.add_argument("--closure", choices=["uniform", "angles", "parametric", "frozen"], default="uniform")
    p.add_argument("--max-blocks", type=int, default=200_000)
    p.add_argument("--qs-ctrl", type=float, default=0.1)
    p.add_argument("--qc-ctrl", type=float, default=0.1)
    p.add_argument("--qd-threshold", type=float, default=0.05)
    p.add_argument("--no-c3-seed", action="store_true")
    p.add_argument("--phi-ds", type=float, default=0.0)
    p.add_argument("--phi-dc", type=float, default=0.0)
    p.add_argument("--phi-sc", type=float, default=math.pi / 2.0)
    p.add_argument("--alpha", type=float, default=0.0)
    p.add_argument("--beta", type=float, default=0.0)
    p.add_argument("--gamma", type=float, default=1.0)
    p.add_argument("--allow-negative", action="store_true")
    p.add_argument("--keep-every", type=int, default=1)
    p.add_argument("--csv", default="")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    cfg = RaceConfig(
        qs0=args.qs0,
        kappa=kappa_value(args.kappa),
        model=args.model,
        closure=args.closure,
        max_blocks=args.max_blocks,
        qs_ctrl=args.qs_ctrl,
        qc_ctrl=args.qc_ctrl,
        qd_threshold=args.qd_threshold,
        include_c3_seed=not args.no_c3_seed,
        phi_ds=args.phi_ds,
        phi_dc=args.phi_dc,
        phi_sc=args.phi_sc,
        alpha=args.alpha,
        beta=args.beta,
        gamma=args.gamma,
        clamp_nonnegative=not args.allow_negative,
    )
    history, events = simulate(cfg, keep_every=max(1, args.keep_every))
    if args.csv:
        write_csv(args.csv, history)

    st0 = history[0]
    stf = history[-1]
    print("Genesis II K4 primitive birth-race wrapper")
    print("==========================================")
    print(f"model          : {cfg.model}")
    print(f"closure        : {cfg.closure}")
    print(f"kappa          : {cfg.kappa:.16g}")
    print(f"initial Qs     : {st0.qs:.16g}")
    print(f"initial Qc     : {st0.qc:.16g}")
    print(f"seeded Qd      : {st0.qd:.16g}")
    print(f"final n        : {stf.n}")
    print(f"final Qs       : {stf.qs:.16g}")
    print(f"final Qc       : {stf.qc:.16g}")
    print(f"final Qd       : {stf.qd:.16g}")
    print(f"last deltas    : dQs={stf.dqs:.6g}, dQc={stf.dqc:.6g}, dQd={stf.dqd:.6g}")
    print("first events   : " + ", ".join(f"{k}={v}" for k, v in events.items()))
    if cfg.model == "shadow":
        # This is just a leading continuous comparison at final time.
        qs_a, qc_a = analytic_shadow_leading(st0.qs, st0.qc, float(stf.n - st0.n))
        print(f"leading ODE cmp: Qs={qs_a:.16g}, Qc={qc_a:.16g}")
    if args.csv:
        print(f"wrote CSV      : {args.csv}")


if __name__ == "__main__":
    main()
