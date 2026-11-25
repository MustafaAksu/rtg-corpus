---
from: SAT
to: PREL
date: 2026-11-11
kind: finding
object: three mathematical points in the publication "Dynamical Genesis of Complex Structure on Graphs" v3.0 (Zenodo concept DOI 10.5281/zenodo.17568896) bearing on PREL §1.12 "K₄ NS mechanism" and the §4 / §7.2 rows "NS bifurcation → 4D torus"
tags: [prelegacy-v0.8]
state: open
---
**Who / status:** filed by the COIL co-owner sessions of `rtg-sat` (Claude owner, ChatGPT co-owner) on the PI's instruction of 11 Nov 2026. A satellite finding carries no RTG authority and is no COIL result (SG-PROG-4); the receiver decides. Source read: the v3.0 PDF, 7 pages, SHA-256 `775d274343ca0386a4739d8211a0ab535ad2b4ad555694ba2fd8957e9e17e8b0` (received from the PI; a search of `dsn/` at `main` for this title and DOI finds no entry).
**1. Symmetric K₃ is not a single-pair crossing.** The paper's own proof of Proposition 5.1 (p. 3) gives the stiffness eigenvalues 0 and −1.5K cos δ* **with multiplicity 2**. At K* two complex pairs therefore reach |λ| = 1 together: the critical space is 4 real dimensions. Theorem 2.1 (p. 2) assumes a *simple* pair and a 2D centre manifold, so it does not apply to the symmetric backbone as stated; the threshold formula K* is unaffected. The paper's numerical K₃ case (Remark 5.2: detuned, directed) is a perturbation that can split the degeneracy. This bears on the contrast "K₄ double-NS → 4D, not K₃ (single-NS, 2D torus)" in PREL §1.12.
**2. Definition of J in Theorem 2.1.** "The rotation matrix J … 𝒥 := J/ω, 𝒥² = −I" is false for a rotation matrix R(ω) and true if J denotes its generator; the text does not say which. A direct construction on a simple 2×2 critical block A (det A = 1, tr A = 2 cos ω): 𝒥 = (A − cos ω·I)/sin ω, 𝒥² = −I by Cayley–Hamilton. This is the linear complex structure only; the nonlinear invariant-circle statement needs the usual non-resonance and normal-form conditions.
**3. Branch of the SU(2) lift.** Definition 4.2 requires ½ Tr H = cos(F/2) while §3 defines F only mod 2π; cos(F/2) changes sign under F → F + 2π. The trace-gap diagnostic (Definition 4.3, Table 1) therefore needs a stated lift convention.
**Independent support available in `rtg-sat` (not RTG results):** at tag `coil-v0.6`, `evidence/coil/prereg/PREREG-MM1-ICID-v1.0.md` §4 derives for the degree-normalised sine triangle the blocks J_∥ = [[1,1],[−aκ cos q, 1−a]] and J_⊥ = [[1,1],[−(aκ/3)(2+cos q), 1−a]]; they coincide at the synchronised state q = 0, which is point 1 in COIL's coordinates. Points 2 and 3 are elementary and were checked by both sessions.
**Asked of the receiver:** nothing is required. If PREL (or the stream it routes NS items to) records the paper, these three points are offered for its scope lines; whether they affect any `[HEUR]` row is the receiver's judgment.
