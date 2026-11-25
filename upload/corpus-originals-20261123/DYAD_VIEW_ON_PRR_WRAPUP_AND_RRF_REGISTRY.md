# Dyadic-stream assessment of the PRR Wrap-up v0.2 and RRF Representation Registry v0.3
**Author:** Claude (Dyadic DSN editor) · **Date:** 24 Sep 2026 · **Inputs:** `RTG_PRIMORDIAL_RELATIONAL_REPRESENTATION_WRAPUP_v0_2.md`, `RTG_RRF_REPRESENTATION_REGISTRY_v0_3.md`, adopted `RTG_DYADIC_OSCILLATOR_DSN_v6.4.10`
**Status:** working assessment; not a DSN amendment. Contains one deliverable for the registry editor (§1) and a queue for Dyadic v6.4.11 (§4).

## 1. Deliverable: the `Claude-check pending` gate is closed
The registry marks three exact-algebra items `participant-rechecked; Claude-check pending`. All three are now re-derived by me from the adopted normalizer convention (homological solve from $T$, exact $\mathbb Q(i\sqrt3)$), independent of the participant's code:

| Registry item | My check | Result |
|---|---|---|
| `RRF-DYAD-W` relabeling candidate: $\mathcal J_{\le6}(S_6^2-I)=0$, $\mathcal J_{\le6}(f\circ S_6-S_6\circ f)=0$, $S_6=h\circ(-I)\circ h^{-1}$ | built $h^{-1}$ to degree 6 (verified $h\circ h^{-1}=\mathrm{id}$), composed | **both identities exact through degree 6** |
| $s_2=-\tfrac{1+i\sqrt3}{6}W^2-\tfrac23W\bar W+\tfrac{1-i\sqrt3}{12}\bar W^2$ | read off $S_6$; also $s_2=2h_2$ identically | **exact** |
| Covariance of $C_W=\bar W_aW_b$: $C_W(SW_a,SW_b)-C_W=O(3)$, $C_W(SW_a,W_b)=-C_W+O(3)$ | symbolic in $(W_a,\bar W_a,W_b,\bar W_b)$ | **degree-$\le2$ parts vanish exactly; both claims hold** |
| `RRF-DYAD-LIFT`: $S_{\rm lift}=\mathcal L^{-1}S_6\mathcal L$ | follows by exactness of $\mathcal L$ from the above | **holds** |

Also re-verified (registry `Claude-checked` / `RRF discussion-local` items): the exact $\mathbb C^*$ rewrite $m'=me^{-s(\nu)}$, $\nu'=\nu e^{i[m-1-s(\nu)]}$; radial equivariance under $(m,\nu)\mapsto(m^{-1},\nu^{-1})$; phase equivariance **iff** $m+m^{-1}-2\in2\pi\mathbb Z$; $T\circ S_o-S_o\circ T=(0,2(\cosh\rho-1))$; $\det DT=1+(e^\rho-1)\cos\eta$; $DT(P_2)=\begin{pmatrix}1&1\\1&2\end{pmatrix}$, eigenvalues $\phi^{\pm2}$; $\widehat f_{\rm form}(\lambda z)=\lambda\widehat f_{\rm form}(z)$ from $p-q\equiv1\ (6)$ (hence odd). **The registry editor may change the three pending tags to `Claude-checked`.**

## 2. Are the Dyadic imports accurate? Yes — all of them
Checked against the adopted v6.4.10 text: $Q_{\rm true}$ and $W_{\rm DSN}$ with $\eta_{\rm wrap}$ (§1); the anti-correlation frame $U=\tfrac{\sqrt3}2\rho$, $V=\eta_{\rm wrap}-\tfrac\rho2$, $U+iV=We^{-i\pi/6}$ (§6.5 — identity re-derived); lifted-phase $\mathcal L$ with no seam (§6.14); SG-19 operations (i)–(iii) and the non-transferable quantities; the $h$/$J$ table path; NF-INV/NF-REM domains; $E_{\rm odd}$, $F_4$ and the symmetrisation-order control (§6.12); DYAD-THM-C21; the standing obstruction. The registry's decision to put $W_{\rm DSN}$/$(U,V)$ on the **wrapped** side and $W_{\rm lift}$ in `RRF-DYAD-W`, equal only on the principal lift, is exactly the distinction the adopted text draws. SG-13/14/15/19 are respected; no Dyadic result is over-read; the registry explicitly does *not* claim $E_{\rm odd}$ has physical meaning (matches owner `[OPEN]`).

One stale line: Wrap-up v0.2 §29 item 7 says v6.4.10 "remains a draft and is not treated as an adopted owner source." Registry v0.3 already cites the adopted document; the wrap-up should be bumped to match (editorial).

## 3. What the Dyadic stream learned (genuinely new, in my view)
1. **A hidden involution of the raw one-step map.** The adopted normalizer has a structural payoff beyond remainders: the trivial NF sign symmetry transports to $S_6=h(-I)h^{-1}$, an involution commuting with $f$ through degree 6, **unique** under the adopted zero-resonant-coefficient convention (the homological solve has no free parameters at degree $\le6$). In raw coordinates it is invisible — the naive swap fails by $(0,2(\cosh\rho-1))$ — and it begins nonlinearly: $S_6(W)=-W+2h_2(W)+O(3)$. This is a Dyadic-owned mathematical fact, not yet in the owner ledger.
2. **The one-sided asymmetry has a global, one-line form.** In the wrapped $\mathbb C^*$ representation the radial equation is exactly inversion-equivariant while the phase equation is equivariant only where $m+m^{-1}-2\in2\pi\mathbb Z$ (locally: $m=1$). This is the same obstruction as RECOG's $T_b$ and as $F_4$ at six steps, now stated without truncation. Representation, not ontology — but a clean statement the owner should hold.
3. **R11 now has a precise target.** The raw comparator $\bar W_aW_b$ is not closed under the transported swap (both-sided defect $O(3)$, one-sided anti-symmetry only to $O(3)$), whereas the NF comparator $\bar z_az_b$ transforms exactly. So the covariant observable algebra is the NF-native one, and $\overline{h(z_a)}h(z_b)$ is what "raw comparator in the final chart" means. That converts R11 from a reconciliation chore into a typed statement.

## 4. Should the Dyadic stream do anything? Yes, three small things — none urgent, none reopening v6.4.10
- **Now:** send §1 to the registry editor (gate closure).
- **Queue for v6.4.11, batched with the R11 outcome (do not reopen v6.4.10):**
  - `DYAD-ALG-NF6-INV` — transported involution $S_6$: definition, the two degree-6 identities, $s_2=2h_2$, uniqueness under `[conv: DYAD-ALG-NF6]`; **scoped as a representation-level dynamical symmetry**, with OPEN-A (physical pole relabeling; agreement with $\zeta\mapsto\zeta^{-1}$ only at linear order) explicitly not claimed.
  - `DYAD-ALG-WRAP` — exact $\mathbb C^*$ rewrite of $T$ and the wrapped swap diagnostic, `[ALG]`, tagged representation-not-ontology (SG-14/15).
  - §6.12 cross-reference: comparator covariance defect as the R11 target (one line; the RECOG owner records the reconciliation).
- **Nothing else.** No constant, chart, or scientific status changes.

## 5. What the Dyadic stream cannot decide — and should not be cited for
The wrap-up's central ontological question (node-first vs dyad-first) is **undecidable from isolated-dyad mathematics** — the state is already $(\rho,\eta)$ with no per-pole variables, so Dyadic results are silent by construction. The discriminator is higher-arity ($H_2$, $H_\times$, winding) and lives in Genesis/network streams. Likewise the $\mathbb Z_6/U(1)/\lambda^6$ identification is unearned (registry §8.3 correctly says so). The Dyadic stream's role in this programme is exactly what the registry uses it for: certified local objects plus registered transport rules. It should not be quoted in support of any `[HYP]` in the wrap-up, and it currently is not.
