# DZT v0.7 working note — closed-form Case-V norm iteration

**Status:** DZT-side working note produced from the Dyadic-imported closed form for the q=4,(0,3) cascade.  
**Artifact:** `dzt_casev_norm_from_closed_form.py`  
**Scope:** finite closed-form audit, p = 8..1000, 4|p.  
**Tag discipline:** finite-horizon algebraic computation plus heuristic pattern; not an all-p theorem.

## Dyadic import assumed

For p=4s, s>=2, with L=zeta_p and I=L^(p/4)=i,

\[
Q(L,I)=\frac{L^5(IL^2+I-L^2+1)}{2(L+1)^4(L^2+L+1)}
\]

and the Dyadic certificate proves

\[
\sigma_{-1}(Q)=-L^{-6}Q,\qquad
M_p=\frac{Q_p}{i\zeta_p^3}\in\mathbb Q(\zeta_p)^+.
\]

DZT imports this as Dyadic-owned; DZT owns the norm audit.

## Closed-form norm computation

Using

\[
M_p = \text{unit}\cdot
\frac{A_s(L)}{2(L+1)^4(L^2+L+1)},\qquad
A_s(L)=L^{s+2}+L^s-L^2+1,
\]

the script computes

\[
N_{\mathbb Q(\zeta_p)/\mathbb Q}(M_p)
=
\frac{
\operatorname{Res}(\Phi_p,A_s)
}{
2^{\varphi(p)}
\operatorname{Res}(\Phi_p,L+1)^4
\operatorname{Res}(\Phi_p,L^2+L+1)
}
\]

and then takes the exact rational square root to obtain

\[
N_+(M_p)=N_{\mathbb Q(\zeta_p)^+/\mathbb Q}(M_p).
\]

## Results through p=1000

Audited points: 249 values p=8,12,...,1000.

Odd-prime anomalies: 20 values.

First anomalies:
\[
p=40,72,104,136,200,232,296,328,392,424,\dots
\]

The v0.6 statement "p=40 is sole anomaly across p=12..64" remains correct only on that horizon. It is superseded as a global diagnostic by the closed-form audit: p=72 is the next anomaly.

## Observed diagnostic pattern, not theorem

In the p<=1000 audit, every anomaly has

\[
p=8q,\qquad q=\ell^a
\]

for an odd prime power q. In those cases,

\[
N_+(M_p)=\frac{\ell^2}{2^{\varphi(q)}}.
\]

Examples:
\[
p=40=8\cdot5:\quad N_+=25/16,
\]
\[
p=72=8\cdot3^2:\quad N_+=9/64,
\]
\[
p=104=8\cdot13:\quad N_+=169/4096,
\]
\[
p=136=8\cdot17:\quad N_+=289/65536.
\]

For audited p=8q with q odd and not an odd prime power, the observed value is

\[
N_+(M_p)=2^{-\varphi(q)}.
\]

This is a [HEUR diagnostic] / conjectural DZT pattern until proven by a resultant identity.

## DSN consequence

v0.7 should replace the v0.6 "p=40 isolated" frontier with:

[OPEN] DZT-OPEN-0B-R: prove or reject the resultant pattern for \(A_s\):
odd-prime numerator support appears exactly when \(p=8\ell^a\), and the numerator is \(\ell^2\).

No zeta-continuation, prime-distribution, OPEN-M, or Dyadic-dynamics claim follows.
