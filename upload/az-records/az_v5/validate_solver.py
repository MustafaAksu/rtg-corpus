#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
az/validate_solver.py
=====================
ENG-blocker-4 acceptance: sparse ARPACK leading-K agrees with dense full
spectrum on the largest-magnitude eigenvalues, and trace-moment fallback
is self-consistent with Tr(B^m) = sum lambda^m.
"""
import sys, os, time
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "lib"))
from hashimoto import (build_hashimoto, build_hashimoto_sparse,
                       hashimoto_spectrum_full, hashimoto_spectrum_leading,
                       nonbacktracking_moments)
import graphgen as gg


def make_test_graph(n_cycles, L):
    # a moderately sized graph: several interlocking bouquets
    edges = []
    base = 0
    for c in range(n_cycles):
        edges += gg.gen_bouquet(2, L, hub=base)
        base += L * 2
    return edges


def main():
    print("ENG-blocker-4 acceptance: sparse vs dense")
    edges = make_test_graph(n_cycles=20, L=5)
    m = len(edges)
    print(f"  graph: {m} directed edges")

    t0 = time.time()
    full = hashimoto_spectrum_full(edges)
    t_dense = time.time() - t0

    t0 = time.time()
    K = 10
    lead = hashimoto_spectrum_leading(edges, K)
    t_sparse = time.time() - t0

    full_top = np.sort(np.abs(full))[::-1][:K]
    lead_top = np.sort(np.abs(lead))[::-1][:len(lead)]
    kcmp = min(len(full_top), len(lead_top))
    err = float(np.max(np.abs(full_top[:kcmp] - lead_top[:kcmp])))
    print(f"  dense full: {len(full)} eigs in {t_dense:.3f}s")
    print(f"  sparse leading-{K}: {len(lead)} eigs in {t_sparse:.3f}s")
    print(f"  max |mag| diff on top-{kcmp}: {err:.2e}  -> {'PASS' if err < 1e-8 else 'CHECK'}")

    print("\nTrace-moment fallback self-consistency: Tr(B^m) vs sum(lambda^m)")
    moments = nonbacktracking_moments(edges, m_max=8)
    ok_all = True
    for mm in range(1, 9):
        from_eigs = float(np.real(np.sum(full ** mm)))
        from_trace = moments[mm - 1]
        d = abs(from_eigs - from_trace)
        ok = d < 1e-6 * max(1.0, abs(from_eigs))
        ok_all &= ok
        print(f"  m={mm}: Tr(B^m)={from_trace:.4f}  sum(l^m)={from_eigs:.4f}  diff={d:.2e}  {'ok' if ok else 'FAIL'}")

    print("\nResult:", "PASS" if (err < 1e-8 and ok_all) else "CHECK")
    sys.exit(0 if (err < 1e-8 and ok_all) else 1)


if __name__ == "__main__":
    main()
