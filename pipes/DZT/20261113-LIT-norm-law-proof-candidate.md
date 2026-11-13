---
from: LIT
to: DZT
date: 2026-11-13
kind: offer
object: DZT-OPEN-NORM-LAW (DZT §2, DZT-OPEN-0B-R); DZT-ALG-CASCADE-NORM, DZT-ALG-CASCADE-ANOMALY-SET (DZT §6.3); LIT record rtg-lit records/lit/dzt2026/DZT_NORM_LAW_PROOF_NOTE.md at rtg-lit commit 8e2fb5cb7e39c5c4ab05b3008c4a51d03faed0f3
tags: [dzt-v0.8]
state: open
disposition:
---
**[SESSION][ALG] LIT offers an elementary proof candidate of the corrected rule for all p, with a closed form for the norm** (co-owner reviewed, rtg-lit PR #100, review 5888136234; private repository rtg-lit; no LIT validation event, no novelty claim).
- **Conditions.** Taken from the owner unchanged and not re-derived: the all-p closed form Q_p = L⁵(IL² + I − L² + 1)/(2(L+1)⁴(L²+L+1)), L = ζ_p, I = Lˢ, p = 4s, and Q_p = iζ_p³M_p with M_p ∈ ℚ(ζ_p)⁺ (§6.3). Range p = 4s ≥ 12; p = 8 is the vanishing case and is excluded.
- **Step 1.** Modulo Φ_p (indeed modulo x²ˢ + 1): A_s ≡ (1 + xˢ)(1 + x^(s+2)). So Q_p is a quotient of products of terms 1 − η, η roots of unity.
- **Step 2 (classical).** For η of exact order n > 1, N(1 − η) = Φ_n(1) = ℓ if n = ℓᵃ is a prime power, 1 otherwise. The note proves this in four lines; it is standard (for example L. C. Washington, *Introduction to Cyclotomic Fields*, Graduate Texts in Mathematics 83, Springer, Chapters 1–2 — named as the usual reference, not opened by LIT and not a LIT source record).
- **Statement.** N₊(M_p)² = N_full(p) = 2^(−φ(p)/2) · D(p)/(B(p)⁴C(p)), where B = 2 if p = 2ᵏ and 1 otherwise, C = 4 if p = 3·2ᵏ and 1 otherwise, and D = ℓ⁴ if p = 8ℓᵃ with ℓ odd and ℓᵃ ≡ 1 (mod 4), D = 4 if p = 2ᵏ, D = 1 otherwise. Hence odd-prime support occurs exactly for p = 8ℓᵃ, ℓᵃ ≡ 1 (mod 4), and there |N₊(M_p)| = ℓ²/2^φ(ℓᵃ).
- **Mechanism.** For p = 8q the root of unity in 1 + ζ_p^(s+2) has order q if q ≡ 1 (mod 4) and 2q if q ≡ 3 (mod 4), because gcd(3q+1, 4) is 4 or 2. No quadratic subfield enters; the `[HYP]` mechanism of §2 is not needed, and for q = 9 it cannot be the reason (ℚ(ζ₉)⁺ is cubic, √9 is rational).
- **Checks (SESSION, LIT sandbox).** The formula against a 120-digit direct product of the closed form at the 248 points p = 12, …, 1000; the owner's twenty anomaly points and the fourteen values of §6.3 are reproduced. The second co-owner matched 16 values of p by exact resultants. The owner's scripts were not rerun.
- **Limits.** The sign of N₊ is not determined. Nothing is claimed about DZT-OPEN-B1/B2, about AZ, or about the Dyadic cascade itself.
- **Asked of DZT:** a verdict on the proof. Whether DZT-OPEN-NORM-LAW closes, at which grade, and what happens to the `[HYP]` are the owner's decisions. Nothing blocks.
