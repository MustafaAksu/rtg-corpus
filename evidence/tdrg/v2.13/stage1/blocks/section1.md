## §1. Current Canonical State {#sec-1-canonical-state}

`[DEF]` TDR-G is a finite relational system on $\mathbb{Z}_N$ ($N$ even): nodes carry phases $\theta_i$ and velocity tokens $\delta_i$, the node count grows at each star blow-up, and only the relational phases $\Delta_{ij}$ are physical (TDRG-DEF-ZN-STATE, TDRG-DEF-PHYSICAL-STATE). Nodes interact when $\Delta_{ij}$ lies in the defect band $\mathcal{D}_k$ around $N/2$ (TDRG-DEF-BAND), under the step order CONV-TICK and a declared multistar policy (§6.3).

`[THM]` Holonomy, $\Delta_{AB}+\Delta_{BC}+\Delta_{CA}\equiv0$, and narrow-band exclusion: under $k<N/6$ no triangle is fully defective (TDRG-THM-HOLONOMY, TDRG-THM-NARROW-BAND-EXCLUSION, §6.2). `[THM]` Two-node reachability at $k=0$ (TDRG-THM-REACHABILITY-K0); `[ALG]` its band form, under which superselection persists at $k>0$ in the two-node universe (TDRG-ALG-LEM-REACH, §6.5).

`[ALG]` Genesis-layer kinematics: no free annihilation; the two-node retrigger threshold $|d|_c\le2k$; advance-spectrum conservation for three nodes without births (TDRG-ALG-LEM-SPECCONS) and for $n$ nodes on ticks without births (TDRG-ALG-SPECCONS-N) (§6.5, §6.12, §6.13). `[ALG]` Token laws: each birth at centre token $x$ adds one token $-x$, the signed-class set is invariant, and the birth update of the spectrum is exact but not closed on the spectrum (§6.13; TDR-6 is PARTIAL).

`[ALG]` `[conv: v18 path orientation]` In the three-node universe ($N=24$, $k=1$, exact enumeration) the isolated period-2 dyad is not a persistent primitive (TDRG-ALG-BIND3-CYCLE-N24K1); `[NUM strong]` `[conv: v18 path orientation]` pure-bound survival is confined to even-advance parity sectors, and the conserved spectrum gates autonomous retrigger (TDRG-NUM-BIND3-PARITY, TDRG-NUM-BIND3-SPECTRAL-GATE, §6.12).

`[ALG]` Birth accounting: $rN_{\rm err}=0$ in all valid v16 motif logs, and $C_{\rm birth}=C_{\rm component}/\chi$ [assuming: the microscopic birth law] (§6.4). `[NUM]` Microscopic birth law: under `bound_symmetric`, `births_step` $=$ `clean_star_components` on all steps with nonzero births (§6.4).

`[NUM]` `[scope: full-range fit, N=120–1440]` `[conv: v18 path orientation]` On the canonical branch `bound_symmetric` at $k/N=1/15$, $T=5000$, $B_{\rm bulk}/\text{step}\sim N^{-0.869}$; the exponent is window-dependent ($N^{-0.730}$ on $480$–$1440$) and not a structural constant (§6.8, TDR-23). `[HEUR]` Thermodynamic crystallization, $B_{\rm bulk}/\text{step}\to0$ as $N\to\infty$, is an extrapolation (TDR-22b).

Policies (§6.6): `bound_symmetric` crystallizes `[NUM]`; `largest_center` inflates continuously `[NUM]`; `all_centers` inflates in avalanches, often cap-limited `[HEUR strong]`. Policy choice is physically real, not an implementation detail. `[ALG]` `trap`, `bound_multistar` and `bound_path_tie` are dynamically equivalent whenever multistars and path ties generate no births and no momentum transfer (§6.3). `[HEUR strong]` Large multistar bound states suppress clean single-centre births (§6.10).

`[ALG]` identity, `[NUM strong]` intensiveness: $O_t=(2k+1)M_t\psi_t$ with $\psi_{\rm slot}^{\rm bulk}$ effectively N-independent, explained by a bounded structural reservoir and $q_{\rm proj}\sim(2k+1)$ (TDR-24D and TDR-24F, closed at the mechanism level; their analytic constants are OPEN; §6.8, §2).

`[DEF]` **Frontier gate:** before discrete triadic dynamics (TDR-T), TDR-24A → TDR-24B → TDR-24C (§2).

---
