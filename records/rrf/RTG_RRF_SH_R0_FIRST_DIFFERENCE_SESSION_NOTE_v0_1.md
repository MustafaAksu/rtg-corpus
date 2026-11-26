# RRF — Fixed finite `S_h` versus formal `R_0`: first divergent homogeneous degree

**Version:** v0.1 · **Date:** 19 October 2026  
**Status:** `[SESSION]` mathematical deduction, **not** a DYAD owner-adopted theorem and **not** a new RRF native profile.  
**Sources inspected directly:** `RTG_DYADIC_OSCILLATOR_DSN_v6_4_13.md` §§6.14–6.16, `DYAD-ALG-NF6-DEG10` and `DYAD-THM-FORMAL-INVOLUTION-UNIQUE`; adopted RRF v0.8.2 §§2.4–2.4b. No external artifact was rerun.

## Assumptions and distinct maps

Let `h_6` be the finite degree-six normalizing chart, `F=T^6`, and

\[
S_h=h_6\circ(-I)\circ h_6^{-1},\qquad R_0=T^3\circ F^{-1/2}.
\]

`S_h` is an exact *analytic* involution on the finite-chart domain; `R_0` is the unique *formal* involution commuting with `F`, with linear part `−I`. Owner and RRF records establish `j_{\le6}S_h=j_{\le6}R_0`. In `z` coordinates set

\[
G=h_6^{-1}\circ R_0\circ h_6=-I+E,\qquad \widehat F=h_6^{-1}\circ F\circ h_6=I+f_3+O(|z|^4).
\]

Then `G` is a formal involution commuting with `\widehat F` and `E=O(|z|^7)`. Owner VF-1 reports a nonzero *even* term in `\widehat F` at total degree ten (coefficient `z^5\bar z^5`): its degree-ten parity defect is nonzero. This is a fixed-`h_6` fact, not a general absence of odd charts.

## 1. Involution parity excludes degree seven

Assume `E_m` is the first nonzero homogeneous term of `E` at degree `m≥7`. From

\[
G^2(z)=z-E_m(z)+E_m(-z)+O(|z|^{m+1})=z
\]

we obtain `E_m(-z)=E_m(z)`. For a homogeneous term this requires `m` **even**. Thus the first mismatch between `G` and `−I` cannot have degree seven; if a mismatch exists, its degree is at least eight.

## 2. Degree-ten parity defect forces the mismatch by degree eight

Because `\widehat F=I+O(|z|^3)`, the nonlinear commutator of `E=O(|z|^m)` with `\widehat F` begins at homogeneous degree at least `m+2` (the identity part cancels). The identity `G\widehat F=\widehat FG` therefore implies

\[
(-I)\widehat F-\widehat F(-I)=O(|z|^{m+2}).
\]

The left side is the negative of `\widehat F(z)+\widehat F(-z)`, whose degree-ten term is **nonzero** by owner VF-1. Thus `m+2≤10`, i.e. `m≤8`. Combined with the even-degree requirement and `m≥7`, this gives exactly `m=8`.

Conjugation by a chart tangent to the identity preserves the leading homogeneous degree of the difference of two maps. Hence

\[
\boxed{j_{\le7}R_0=j_{\le7}S_h,\qquad j_8R_0\ne j_8S_h.}
\]

**[SESSION]** The *first divergent total homogeneous degree is eight* under the declared shared normalizer convention. This strengthens the previously proposed “degree seven or eight” scope without running a new eighth-order jet engine.

## Boundaries and recommended handling

- The argument uses two **owner-recorded premises**, the equality through sixth jet and the nonzero even degree-ten term in the fixed `h_6` chart. It does **not** claim an independently executed eighth-order coefficient or the full eighth-degree polynomial.
- The result says nothing about a possible *different* smooth or analytic odd chart. It does not contradict DYAD OPEN 20 and does not select physical pole exchange.
- Recommend owner cross-check if the degree-eight coefficient or a numerical certificate is needed. In the meantime retain this as a separate `[SESSION]` consequence, not a new DYAD RID or an adopted RRF theorem.
