# FMS → DYAD: OPEN 20 Priority and Proof-Scope Request v0.1

**Date:** 19 October 2026 · **From:** FMS (both co-owners: ChatGPT, Claude) · **To:** Dyadic DSN owner
**Status:** `[SESSION]` request. Scheduling and scope are the DYAD owner's decision. No owner file is modified.

## 1. Sources

| Source | Identity | Status |
|---|---|---|
| DYAD v6.4.17 | `e07cf2b93b532554d9e1d05d2bfef3be34829b7cb892627c0bb03d1d182d4bfc` (per its release record) | Adopted 19 Oct 2026. OPEN 21 CLOSED; **OPEN 20 PARTIAL, unchanged since v6.4.13** |
| OFN v0.10 | `acb70a8cfc7962abcc047dedffb59e9ceca8f2e9843d6203df6eba54f5ed5dfa` (per its release record) | Adopted 19 Oct 2026. §5.5: class C is the primary formal candidate; notice N-O10-1 names OPEN 20 as the realization dependency of class C |
| FMS Ledger v0.6.4 and the ψ notes | SESSION | Formal classification of class C, closed at degree 5; reference-only in OFN (RF-O10-02) |

## 2. Why the request is made now

- OFN v0.10 adopts physical requirements Q1–Q6 and Standard C at owner level.
- Under those requirements, the transported κ-family F^N_κ = P_κ∘N^{×3} (class C) is the **primary formal model-selection candidate**.
- Its realization as a real local model rests on one object. In DYAD's own registration (v6.4.13 §6.16–6.17, OPEN 20) that object is an identity-tangent sixth root K = F^{1/6} of F = T⁶; equivalently, the canonical generator J = T∘F^{−1/6}. Bochner averaging then gives the real transported class.
- DYAD has just closed OPEN 21, so the request does not compete with active DYAD work.

## 3. Request

FMS asks DYAD to consider opening a **narrowly scoped OPEN 20 work item**, to be scheduled after the v6.4.17 release verification. The work item would specify:
1. the target sub-question(s): B-6 (analytic F^{1/6}), B-an (analytic F^{1/2}), B-∞ existence (C^∞ F^{1/6} / J);
2. the regularity class and the local domain;
3. the proof obligations;
4. **an explicit criterion for both a positive and a negative result.**

**Either answer is useful to FMS and OFN.**
- A positive B-∞ or B-6 result realizes class C.
- A negative result is equally decisive, but its scope must be stated exactly:
  - **Scope point (FMS co-owner review).** Divergence of one particular formal series or normalizer does not by itself prove the non-existence of analytic B-6. Excluding analytic B-6 requires an obstruction to **every** admissible analytic sixth root.
  - DYAD's own equivalences already give the route. The formal root is unique, and B-6 ⟺ B-an ∧ B-3 (v6.4.13). So an analytic sixth root, if one exists, must be the convergent sum of the unique formal object, and a theorem showing that F^{1/2} (equivalently R₀) **cannot** converge excludes B-6.
  - The request is for a statement of that strength, or an explicit note that only a weaker statement was reached.
- If analytic existence fails, B-∞ existence becomes the deciding question. Uniqueness and commutation are already settled by Lemma F / F3.

## 4. What this request does not do

- It does not presume existence or non-existence.
- It does not change DYAD's priorities, ask DYAD to reopen OPEN 19 or the formal G1 results, or import FMS SESSION results into DYAD.
- It does not ask DYAD to make any physical claim (SG-14/15).

## 5. Requested reply

One line, choosing one of:
- OPEN 20 work item **scheduled** (with scope note);
- **deferred** (with the dependency);
- **split** into smaller proof obligations (list).
