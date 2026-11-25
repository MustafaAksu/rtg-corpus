#!/usr/bin/env python3
import argparse
import numpy as np
import pandas as pd

def resid(y, x):
    X = np.column_stack([np.ones_like(x), x])
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return y - X @ beta

def budget_for_phi(df, phi, phi_tol=1e-9):
    # precise phi filter (NO rounding bins)
    sub = df[np.abs(df["phi"] - phi) <= phi_tol].copy()

    sub = sub[np.isfinite(sub["logA"]) & np.isfinite(sub["R_K"]) & np.isfinite(sub["logX"])].copy()
    sub = sub.reset_index(drop=True)

    if len(sub) == 0:
        raise RuntimeError(f"No rows found for phi={phi} within tol={phi_tol}. "
                           f"Check that df['phi'] is numeric and that the value exists in the CSV.")

    x = sub["logX"].to_numpy()
    rA = resid(sub["logA"].to_numpy(), x)
    rRK = resid(sub["R_K"].to_numpy(), x)

    c = rA * rRK
    sub["r_logA"] = rA
    sub["r_RK"] = rRK
    sub["c_i"] = c

    cov = float(np.mean((rA - rA.mean()) * (rRK - rRK.mean())))
    pcorr = float(np.corrcoef(rA, rRK)[0, 1])

    # Sorted by c_i (most negative first)
    out = sub[["case", "dt", "gamma", "R_K", "logX", "r_logA", "r_RK", "c_i"]].copy()
    out = out.sort_values("c_i", ascending=True)

    # Dominance fractions (for the most negative contributor)
    # NOTE: this is on raw c_i; your normalized version c_tilde is in normalized_cov_budget.py
    neg_pool = float(np.sum(np.abs(out.loc[out["c_i"] < 0, "c_i"])))
    dom = out.iloc[0]
    net_share = (dom["c_i"] / cov) if cov != 0 else np.nan
    gross_share = (abs(dom["c_i"]) / neg_pool) if neg_pool != 0 else np.nan

    extra = {
        "dominant_case": dom["case"],
        "dominant_dt": float(dom["dt"]),
        "dominant_gamma": float(dom["gamma"]),
        "dominant_c_i": float(dom["c_i"]),
        "gross_neg_pool": float(neg_pool),
        "gross_share_of_neg_pool": float(gross_share),
        # net_share here is relative to covariance (not pcorr); kept mostly as a diagnostic
        "net_share_of_cov": float(net_share),
    }

    return cov, pcorr, out, extra

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases_csv", required=True)
    ap.add_argument("--phi_a", type=float, required=True)
    ap.add_argument("--phi_b", type=float, required=True)
    ap.add_argument("--phi_tol", type=float, default=1e-9, help="Absolute tolerance for matching phi.")
    args = ap.parse_args()

    df = pd.read_csv(args.cases_csv)

    # Ensure numeric phi
    df["phi"] = pd.to_numeric(df["phi"], errors="coerce")

    for phi in [args.phi_a, args.phi_b]:
        cov, pc, out, extra = budget_for_phi(df, phi, phi_tol=args.phi_tol)
        print(f"\nphi={phi:.6f}: cov(r_logA,r_RK)={cov:+.6e}  pcorr={pc:+.4f}")
        print(f"dominant (most negative c_i): {extra['dominant_case']}  dt={extra['dominant_dt']:.2f}  "
              f"gamma={extra['dominant_gamma']:.1f}  c_i={extra['dominant_c_i']:+.6e}")
        if extra["gross_neg_pool"] > 0:
            print(f"gross negative pool sum|c_i|={extra['gross_neg_pool']:.6e}  "
                  f"gross share={100.0*extra['gross_share_of_neg_pool']:.1f}%")
        print(out.to_string(index=False))

if __name__ == "__main__":
    main()
