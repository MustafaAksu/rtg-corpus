#!/usr/bin/env python3
"""Operating characteristics of the registered Stage 2 reading rule - design computation, [SESSION]; no campaign data.

For one contrast of the family of ten at the registered size (1,500 pairs): the probability of each reading under
assumed risks of the resonant arm (p1) and of the detuned arm (p0), the two arms taken as independent within a pair.
The rule is the one of az_tokres_s2_analyse.py: SUPPORTED iff Holm p < 0.05 and the lower limit of the 99.5 % two-sided
Agresti-Min interval exceeds 0.05; NOT SUPPORTED iff the upper limit is below 0.05; else INCONCLUSIVE. Holm's adjusted
p is replaced here by its upper bound 10 p (Bonferroni), so the SUPPORTED rates are lower bounds.

usage  python power_table.py --analysis-s1 PATH --analysis-s2 PATH      (needs numpy; seed fixed)
"""
import argparse, importlib.util, math, sys
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("--analysis-s1", required=True)
ap.add_argument("--analysis-s2", required=True)
a = ap.parse_args()
sys.dont_write_bytecode = True


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


s1, s2 = load(a.analysis_s1, "s1"), load(a.analysis_s2, "s2")
n = s2.REGISTRY["S2-C240"]["n_base"]
z, dstar, fam = s2.Z_FAMILY, s2.DELTA_STAR, s2.FAMILY_SIZE
rng = np.random.default_rng(20261113)
print("pairs per contrast n = %d; family of %d; interval quantile z = %.6f; delta* = %.2f; numpy seed 20261113" % (n, fam, z, dstar))
print("%-34s %8s %9s %10s %12s %13s  %s" % ("scenario", "true RD", "reps", "SUPPORTED", "NOT SUPP.", "INCONCLUSIVE", "mean half-width"))
SC = [("Stage 1 PC1 risks", 0.258, 0.015, 20000), ("Stage 1 PC2 risks", 0.185, 0.024, 20000), ("Stage 1 PC3 risks (N = 122)", 0.231, 0.011, 20000),
      ("half of the Stage 1 PC2 effect", 0.105, 0.024, 20000), ("RD 0.10", 0.12, 0.02, 20000), ("RD 0.08", 0.10, 0.02, 20000),
      ("RD 0.07", 0.09, 0.02, 20000), ("RD 0.06", 0.08, 0.02, 20000),
      ("RD = delta* (boundary), base 0.02", 0.07, 0.02, 400000), ("RD = delta* (boundary), base 0.005", 0.055, 0.005, 400000),
      ("RD 0.03", 0.05, 0.02, 20000), ("RD 0.02", 0.04, 0.02, 20000), ("no effect, base 0.02", 0.02, 0.02, 20000),
      ("no effect, base 0.005", 0.005, 0.005, 20000)]
for name, p1, p0, reps in SC:
    pr = [p1 * p0, p1 * (1 - p0), (1 - p1) * p0, (1 - p1) * (1 - p0)]
    cnt = rng.multinomial(n, pr, size=reps)
    b, c = cnt[:, 1].astype(float), cnt[:, 2].astype(float)
    ba, ca, na = b + 0.5, c + 0.5, n + 2.0
    mid = (ba - ca) / na
    se = np.sqrt(ba + ca - (ba - ca) ** 2 / na) / na
    lo, hi = mid - z * se, mid + z * se
    cand = np.nonzero(lo > dstar)[0]
    sup = sum(1 for i in cand if min(1.0, fam * s1.mcnemar_exact(int(b[i]), int(c[i]))) < 0.05)
    nots = int(np.sum(hi < dstar))
    print("%-34s %+8.3f %9d %10.4f %12.4f %13.4f  %.4f" % (name, p1 - p0, reps, sup / reps, nots / reps, (reps - sup - nots) / reps, float(np.mean(z * se))))
print("At the boundary RD = delta* a SUPPORTED reading is an error of the minimum-effect rule; the nominal one-sided rate")
print("per contrast is 0.05 / (2 x %d) = %.4f, and the Monte Carlo standard error of a rate near it with 400,000 repetitions is %.5f." % (
    fam, 0.05 / (2 * fam), math.sqrt(0.0025 * 0.9975 / 400000)))
