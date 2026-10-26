#!/usr/bin/env python3
# =============================================================================
# N-5A-S1 — SECOND-STREAM SECTION-CROSSING SEARCH  v1
# =============================================================================
# Module: N-5A-S1 under the N-4 umbrella (PI directive 2026-08-28).
# Question: can the exact dyad furnish a second repeatable relational event
# stream B that is NOT merely T^m?
#
# Candidate B: oriented crossing of the declared relational section
#     Sigma = { Theta = 0 (mod 2pi) },
#     Theta = atan2(sqrt3 * eta_wrap, 2 rho - eta_wrap)
# [ISP angle, RTG_DYADIC_OSCILLATOR_DSN_v6.4.9 §6.x; imported observable,
#  ownership remains Dyadic]
#
# FALSIFICATION-FIRST: gate 5 (independence / non-relabeling) is the cheapest
# falsifier, so it is run FIRST. If the primitive return-gap word tau_1,
# tau_2, ... is identically a fixed m, the candidate is merely re-blocking
# (NG-8B territory) and N-5A-S1 FAILS for this section.
#
# PRE-REGISTERED HYPOTHESIS (stated before the run):
#   HYP-N5AS1-GAP: because the P_1 linearization is the order-6 elliptic
#   rotation lambda = exp(+- i pi/3), and Q_true contracts to 0 under L1, the
#   rotation per primitive step tends to exactly pi/3 as the orbit contracts.
#   PREDICTION: the return-gap word converges to the constant word 6, i.e.
#   B -> T^6 = F asymptotically. If so, the candidate FAILS gate 5 in the
#   asymptotic regime and can only survive, if at all, in a transient
#   large-amplitude regime that lies OUTSIDE the certified L1 tube.
#   FALSIFIER of the prediction: a persistent non-constant gap word inside
#   the certified small-amplitude regime.
#
# This script does not close N-5A. It executes the first independence gate
# and reports the verdict either way. Exit code 0 = the search ran and its
# verdict is recorded (a NEGATIVE verdict is a valid, informative outcome).
# =============================================================================

import sys
import mpmath as mp

mp.mp.dps = 50
SQ3 = mp.sqrt(3)


def Tmap(p):
    rho, eta = p
    return (rho - mp.sin(eta), eta + (mp.e ** rho - 1) - mp.sin(eta))


def wrap(a):
    return mp.fmod(a + mp.pi, 2 * mp.pi) - mp.pi


def Q_true(p):
    rho, eta = p
    w = wrap(eta)
    return rho ** 2 - rho * w + w ** 2


def Theta(p):
    rho, eta = p
    w = wrap(eta)
    return mp.atan2(SQ3 * w, 2 * rho - w)


def orbit(seed, n):
    o, p = [seed], seed
    for _ in range(n):
        p = Tmap(p)
        o.append(p)
    return o


def gap_word(o):
    """Unwrap Theta, find oriented crossings of Sigma (Theta = 0 mod 2pi),
    return the word of primitive-step gaps between successive crossings."""
    th = [Theta(p) for p in o]
    phi = [th[0]]
    for i in range(1, len(th)):
        phi.append(phi[-1] + wrap(th[i] - th[i - 1]))
    total = phi[-1] - phi[0]
    if total == 0:
        return [], 0
    s = 1 if total > 0 else -1            # intrinsic orientation of the flow
    cross = []
    for i in range(len(phi) - 1):
        a, b = s * phi[i], s * phi[i + 1]
        k = mp.floor(a / (2 * mp.pi))
        if b >= (k + 1) * 2 * mp.pi:      # oriented crossing in step i -> i+1
            cross.append(i + 1)
    return [cross[i + 1] - cross[i] for i in range(len(cross) - 1)], s


print("=" * 70)
print("N-5A-S1 GATE 5 (independence / non-relabeling) — RUN FIRST")
print("Pre-registered prediction: gap word -> constant 6 (i.e. B -> T^6)")
print("=" * 70)

# --- regime 1: inside the certified small-amplitude tube -------------------
SMALL = [(mp.mpf("0.010"), mp.mpf("0.004")),
         (mp.mpf("-0.008"), mp.mpf("0.011")),
         (mp.mpf("0.006"), mp.mpf("-0.009")),
         (mp.mpf("0.013"), mp.mpf("0.013")),
         (mp.mpf("-0.012"), mp.mpf("-0.005"))]

small_words = []
for s in SMALL:
    o = orbit(s, 240)
    w, sgn = gap_word(o)
    small_words.append(w)
    q0, q1 = Q_true(o[0]), Q_true(o[-1])
    print(f"seed {[mp.nstr(c, 4) for c in s]}  orient={sgn:+d}  "
          f"Q: {mp.nstr(q0, 4)} -> {mp.nstr(q1, 4)}  "
          f"gaps(first 18)={w[:18]}  distinct={sorted(set(w))}")

all_small = [g for w in small_words for g in w]
constant_small = len(set(all_small)) == 1 and all_small[0] == 6

# --- regime 2: larger amplitude (exploratory; OUTSIDE certified tube) ------
print("-" * 70)
BIG = [(mp.mpf("0.45"), mp.mpf("0.30")),
       (mp.mpf("0.80"), mp.mpf("-0.50")),
       (mp.mpf("1.10"), mp.mpf("0.75")),
       (mp.mpf("-0.90"), mp.mpf("0.60"))]
big_words = []
for s in BIG:
    o = orbit(s, 240)
    w, sgn = gap_word(o)
    big_words.append(w)
    print(f"seed {[mp.nstr(c, 4) for c in s]}  orient={sgn:+d}  "
          f"Q: {mp.nstr(Q_true(o[0]), 4)} -> {mp.nstr(Q_true(o[-1]), 4)}  "
          f"gaps(first 18)={w[:18]}  distinct={sorted(set(w))}")

all_big = [g for w in big_words for g in w]

# --- tail behaviour: does a non-constant word persist or die out? ----------
print("-" * 70)
tail_report = []
for s, w in zip(BIG, big_words):
    if len(w) >= 8:
        head, tail = w[:len(w) // 2], w[len(w) // 2:]
        tail_report.append((sorted(set(head)), sorted(set(tail))))
        print(f"seed {[mp.nstr(c, 4) for c in s]}  head-distinct={sorted(set(head))}  "
              f"tail-distinct={sorted(set(tail))}")

print("=" * 70)
print("VERDICT")
print("=" * 70)

if constant_small:
    print("GATE 5: FAILED for section Sigma = {Theta = 0 mod 2pi} inside the")
    print("  certified small-amplitude tube. The return-gap word is the")
    print("  constant word 6, i.e. B coincides with F = T^6 there. This is")
    print("  re-blocking of the single Track-A stream (NG-8B), NOT a second")
    print("  independently certified event type. SG-NG-20 is not discharged.")
else:
    print("GATE 5: NOT falsified inside the tube — the gap word is")
    print(f"  non-constant: distinct gaps {sorted(set(all_small))}.")
    print("  Candidate proceeds to gates 1-4 (relational definition,")
    print("  repeatability, co-realization, common order).")

print()
print(f"Large-amplitude exploratory regime: distinct gaps {sorted(set(all_big))}")
if len(set(all_big)) > 1:
    persist = all(len(t) > 1 for _, t in tail_report) if tail_report else False
    print("  A non-constant gap word DOES occur at large amplitude, but this")
    print("  regime is OUTSIDE the certified L1 tube, so it cannot be used")
    print("  for N-5A without first extending the certified domain (N-4).")
    print(f"  Non-constancy persists into the orbit tail: {persist}")
    print("  -> This is the N-4 / N-5A coupling made concrete: a second")
    print("     stream candidate exists only where the certified domain")
    print("     does not yet reach.")
else:
    print("  Gap word is constant at large amplitude too.")

print()
print("PREDICTION CHECK: HYP-N5AS1-GAP predicted the constant word 6 inside")
print(f"  the tube. Observed constant-6 inside tube: {constant_small}")
print("  -> prediction CONFIRMED" if constant_small else "  -> prediction FALSIFIED")
sys.exit(0)
