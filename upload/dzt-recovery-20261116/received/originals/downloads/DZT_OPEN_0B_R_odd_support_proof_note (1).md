# DZT-OPEN-0B-R proof note — odd-prime anomaly support

**Status:** draft proof note for DZT v0.9 integration.  
**Scope:** q=4,(0,3) Case-V cascade, assuming the Dyadic-imported closed form and all-p phase/factorization theorem.  
**Claim proven here:** odd-prime support in \(N_+(M_p)\), and the odd numerator \(\ell^2\), not a full denominator formula.

## Theorem

Let \(p=4s\), \(s\ge 2\), \(L=\zeta_p\), \(I=L^s=i\). For \(p=8\), the cascade is the zero-degeneracy case. For \(p\ge 12\), let

\[
Q(L,I)=
\frac{L^5(IL^2+I-L^2+1)}
{2(L+1)^4(L^2+L+1)}
\]

and

\[
M_p=\frac{Q_p}{i\zeta_p^3}\in \mathbb Q(\zeta_p)^+
\]

by the Dyadic all-\(p\) phase theorem.

Then the odd-prime part of \(N_+(M_p)\) is nontrivial if and only if

\[
p=8q,\qquad q=\ell^a,\qquad q\equiv1\pmod 4,
\]

where \(\ell\) is an odd prime. In that case, the odd numerator contribution is exactly

\[
\ell^2.
\]

Equivalently, the DZT finite-horizon rule
\[
p=8\ell^a,\quad \ell^a\equiv1\pmod4
\]
is the all-\(p\) odd-prime-support rule. No denominator formula is asserted here.

## Proof

Write

\[
A_s=IL^2+I-L^2+1.
\]

Since \(I^2=-1\),

\[
A_s=(I-1)(L^2-I),
\]

because

\[
(I-1)(L^2-I)=IL^2-I^2-L^2+I=IL^2+1-L^2+I.
\]

The unit factor in \(M_p\) has absolute norm \(1\), so the odd-prime support of \(N_+(M_p)\) can only come from the full norm of \(A_s\) and not from roots-of-unity units.

The first factor is fixed:

\[
N_{\mathbb Q(\zeta_p)/\mathbb Q}(I-1)=
N_{\mathbb Q(i)/\mathbb Q}(i-1)^{[\mathbb Q(\zeta_p):\mathbb Q(i)]}
=2^{\varphi(p)/2}.
\]

Thus it contributes only the prime \(2\).

For the second factor,

\[
L^2-I=L^2(1-L^{s-2})\cdot(\text{unit}),
\]

so its absolute norm is the norm of \(1-L^{s-2}\). Let

\[
n=\operatorname{ord}(L^{s-2})=\frac{p}{\gcd(p,s-2)}.
\]

Then

\[
\left|N_{\mathbb Q(\zeta_p)/\mathbb Q}(1-L^{s-2})\right|
=
\Phi_n(1)^{\varphi(p)/\varphi(n)}.
\]

The standard cyclotomic fact is

\[
\Phi_n(1)=
\begin{cases}
r, & n=r^b \text{ is a prime power},\\
1, & n \text{ is not a prime power}.
\end{cases}
\]

For odd-prime support, \(n\) must be an odd prime power. We now characterize when \(n\) is odd.

Write \(p=2^\alpha m\), \(m\) odd, \(\alpha\ge2\), and \(s=2^{\alpha-2}m\).

- If \(\alpha=2\), then \(s=m\) is odd and \(s-2\) is odd, so \(n\) is even.
- If \(\alpha\ge4\), then
  \[
  s-2=2(2^{\alpha-3}m-1)
  \]
  has exactly one factor of \(2\), so \(n\) is even.
- If \(\alpha=3\), then \(p=8q\), \(s=2q\), and
  \[
  s-2=2(q-1).
  \]
  The full \(2^3\) in \(p\) divides \(s-2\) if and only if \(q\equiv1\pmod4\). In that case
  \[
  n=q.
  \]
  If \(q\equiv3\pmod4\), then \(n=2q\), hence \(n\) is not an odd prime power.

Therefore \(n\) is an odd prime power exactly when

\[
p=8q,\qquad q=\ell^a,\qquad q\equiv1\pmod4.
\]

In that case \(n=q=\ell^a\), and

\[
\frac{\varphi(p)}{\varphi(n)}
=
\frac{\varphi(8q)}{\varphi(q)}
=
4.
\]

Thus the odd part of the full norm is

\[
\ell^4.
\]

Since \(M_p\in \mathbb Q(\zeta_p)^+\), the full norm satisfies

\[
N_{\mathbb Q(\zeta_p)/\mathbb Q}(M_p)=N_+(M_p)^2.
\]

Therefore the odd numerator contribution in \(N_+(M_p)\) is

\[
\ell^2.
\]

This proves the all-\(p\) odd-prime-support rule.

## Denominator and 2-adic terms

The proof intentionally does not claim a closed denominator formula. The remaining factors

\[
2^{\varphi(p)},\quad
N(L+1)^4,\quad
N(L^2+L+1)
\]

contribute only powers of \(2\) in the \(4\mid p\) regime:

- \(N(L+1)=|\Phi_p(-1)|=1\) for \(4\mid p\);
- \(N(L^2+L+1)=|\operatorname{Res}(\Phi_p,\Phi_3)|\) is either \(1\) or a power of \(2\) in this regime.

Thus these factors cannot alter the odd-prime support rule above, though they do control the denominator exponent.

## DSN consequence

DZT-OPEN-0B-R can be closed at the following scope:

\[
[\mathrm{THM/ALG\ all\text{-}p}]
\]

for the odd-prime support and numerator law:

\[
\operatorname{OddPartNum}\,N_+(M_p)
=
\begin{cases}
\ell^2, & p=8\ell^a,\ \ell^a\equiv1\pmod4,\\
1, & \text{otherwise}.
\end{cases}
\]

The full denominator law remains outside this theorem unless separately proved.
