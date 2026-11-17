# DZT-THM-CASCADE-DENOMINATOR — proof note

**Statement.** For the channel $q=4,(0,3)$, $p=4s\ge12$, the denominator of $N_+(M_p)$ is a pure
power of 2 with exponent
$$d_p = v_2\big(\mathrm{denom}\,N_+(M_p)\big) = \frac{\varphi(p)}{4} + [\,p=2^k\,] + [\,p=3\cdot2^k\,].$$

**Setup.** $M_p = Q/(i\zeta_p^3)$ with the certified closed form
$Q = L^5(IL^2+I-L^2+1)/[2(L+1)^4(L^2+L+1)]$, $L=\zeta_p$, $I=\zeta_p^{p/4}=i$.
$M_p$ lies in the real subfield $K^+=\mathbb{Q}(\zeta_p)^+$ ($[K^+:\mathbb{Q}]=\varphi/2$), and
$N_{\mathbb{Q}(\zeta_p)/\mathbb{Q}}(M_p)=N_{K^+/\mathbb{Q}}(M_p)^2$, so
$$d_p=\tfrac12\,v_2\big(\mathrm{denom}\,N_{\mathbb{Q}(\zeta_p)/\mathbb{Q}}(M_p)\big).$$
The roots of unity $i,\zeta_p^3,L^5$ have norm $\pm1$ (contribute no 2). So
$$2\,d_p = v_2 N(2(L+1)^4(L^2+L+1)) - v_2 N(IL^2+I-L^2+1).$$

**Numerator factorization.** $IL^2+I-L^2+1=(I-1)(L^2-I)$ (using $I^2=-1$) — the founding $A_s$.

**Norm valuations (each closed-form).**
- $N(2)=2^{\varphi}$ ⟹ $v_2=\varphi$.
- $N(1+L)=\Phi_p(-1)$; $\Phi_{2^k}(x)=x^{2^{k-1}}+1\Rightarrow\Phi_{2^k}(-1)=2$, so $v_2 N(1+L)=[\,p=2^k\,]$
  (and $\Phi_p(-1)$ is odd for odd-part $\ge3$ by the standard $\Phi_n(-1)$ classification). The factor
  is raised to the 4th power: contributes $4[\,p=2^k\,]$.
- $N(L^2+L+1)=N(\Phi_3(L))=\mathrm{Res}(\Phi_p,\Phi_3)$. By **Apostol's resultant theorem**,
  $\mathrm{Res}(\Phi_p,\Phi_3)=q^{\varphi(3)}=q^2$ iff $p=3q^k$ (prime $q$), else $1$; for $p=4s$ the only
  even case is $q=2$, i.e. $p=3\cdot2^k$, giving $v_2=2[\,p=3\cdot2^k\,]$.
- $N(I-1)$: $i-1\in\mathbb{Q}(i)$, $N_{\mathbb{Q}(i)/\mathbb{Q}}(i-1)=2$, $[\mathbb{Q}(\zeta_p):\mathbb{Q}(i)]=\varphi/2$,
  so $N(I-1)=2^{\varphi/2}$, $v_2=\varphi/2$.
- $N(L^2-I)$: $L^2-I=\zeta_p^{p/4}(\zeta_p^{e}-1)$, $e\equiv2-p/4$. Using
  $N_{\mathbb{Q}(\zeta_p)/\mathbb{Q}}(\zeta_p^e-1)=\Phi_d(1)^{\varphi(p)/\varphi(d)}$, $d=p/\gcd(e,p)$, and
  $\Phi_d(1)=\ell$ iff $d=\ell^j$ (else 1): $v_2\ne0$ requires $d$ a 2-power, i.e. odd-part$(p)\mid e$,
  which (since $e=2-2^{k-2}m$) forces $m=1$, i.e. $p=2^k$; then $d=2^{k-1}$,
  $\varphi(p)/\varphi(d)=2$, $v_2\Phi_{2^{k-1}}(1)=1$, giving $v_2 N(L^2-I)=2[\,p=2^k\,]$.

**Assembly.**
$$2d_p = \big(\varphi + 4[\,p{=}2^k\,] + 2[\,p{=}3\cdot2^k\,]\big) - \big(\tfrac{\varphi}{2} + 2[\,p{=}2^k\,]\big)
= \tfrac{\varphi}{2} + 2[\,p{=}2^k\,] + 2[\,p{=}3\cdot2^k\,],$$
hence $d_p=\varphi/4+[\,p{=}2^k\,]+[\,p{=}3\cdot2^k\,]$. $\;\blacksquare$

All steps are closed-form identities or standard theorems (Apostol; the $\Phi_d(1)$ norm formula);
each intermediate valuation also verified computationally on $p=12$–$1000$.
Scope: $q=4,(0,3)$, denominator / 2-adic exponent only. No anomaly-law change, no zeta/RH reading.
