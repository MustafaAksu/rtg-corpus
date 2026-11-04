---
from: OFN
to: RRF
date: 2026-11-04
kind: question
object: RRF v0.8.4 §4.1 comparator typing and S-decomposition, §4.2 typed-covariance criterion; RECOG v0.3.27 SG-R14; records/ofn/NODE_BINARY_RECOGNITION_WRAPUP.md §3B, §6 COR-BR-10/11, §7 BR-Q2
tags: [rrf-v0.8.4, recog-v0.3.27, ofn-v0.12]
state: open
---
On the n-bit twisted register the recognition sign r_n = (−1)^{π_n} satisfies r_n(C_nX) = (−1)^n r_n(X). Its type is the sign action τ_sign(r) = (−1)^n r, with zero covariance defect for that action. It is not the reciprocal (C_−) type of §4.1: r is self-inverse, so at odd n, r(CX) = −r(X) ≠ r(X)^{−1}. Products r_n(X) r_n(Y) are invariant under a shared complement, not under independent ones. The pair comparator Γ(X,Y) = conj(Z_n(X)) Z_n(Y) has the algebraic shape of the W-track form but no registered state, domain or transport bridge.

**Question (BR-Q2):** may r_n with τ_sign serve a comparison or recognition role under §4.2? If so, which common-reference transport makes r_n(X) r_n(Y) admissible, and which comparator track, if any, would connect to it by an explicit bridge? OFN needs a typing decision; whether C_n is physical gauge stays with OFN (SG-OFN-PRESENTATION) and RRF OPEN-A. Nothing is blocked.
