# TDR-G decision note — the `largest_center` tie rule and TDR-19

**[SESSION] NONCANONICAL. Decision support only; it changes no DSN text, grade, policy or engine.**

- **Prepared by:** the TDR-G co-owner (Claude, session `claude01SKePJ`), 13 November 2026.
- **Mandate:** this note is the separate `largest_center` / TDR-19 note asked for with the v2.13 cycle (PI, 13 Nov 2026, 12:07 +03:00).
- **ChatGPT co-owner's condition** (plan evaluation, 12:06): removing the label-dependent centre choice may be a change of the policy law, not an engine fix. It must not be adopted before the alternatives and their dynamical consequences are compared.

**Sources:**
- TDR-G `tdrg-v2.12.15`: §6.3 policy table and TDRG-DEF-MULTISTAR; §6.6 TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK; SG-7, SG-14; §2 TDR-19.
- Pinned engine `upload/tdrg-records/genesis_mode_b_mc_v18.py`, SHA-256 `9d787b435c42fd2024c81e614e3c6e3e076dc2bd30ad1e7e286ada8e6dfe675e`, function `choose_largest_center`.

## 1. What is established

- **The rule as implemented** (`EV-CODE`). `choose_largest_center` returns the first centre under the key (−degree inside the component, node id). When two or more valid centres share the largest degree, the node label decides which centre fires.
- **The DSN's account.** The DSN records this as TDRG-ALG-LARGEST-CENTER-ID-TIEBREAK (owner finding N1, v2.12.14): `[ALG]`, scoped to the engine function. The $K_{2,3}$ fixture shows that exchanging two centre labels changes the firing centre. SG-14 records the branch as not relabelling-covariant, "to be resolved with TDR-19". The `largest_center` results of §§6.6–6.7 and §1 are kept, not rerun. The canonical branch `bound_symmetric` is unaffected: it binds multistars.
- **What the policy definition leaves open.** The policy table says only "one center fires". Neither the DSN definition (§6.3) nor TDR-19 states which centre fires when several qualify equally. **The tie rule is therefore part of the policy's definition, not of its implementation.** Changing it changes the declared law of the branch (SG-7: policies are distinct physical universes), and is a TDR-19 decision, not an engine correction. This agrees with the co-owner's condition.

## 2. New measurement: ties are the common case

Ties are not a corner case. In most `largest_center` multistar events, two or more centres share the largest degree, so the node ID decides.

| $N$ | $k$ | $T$ | seeds | multistar events | ties | tie fraction |
|---:|---:|---:|---:|---:|---:|---:|
| 90 | 6 | 500 | 3 | 1,235 | 1,023 | 0.83 |
| 120 | 8 | 500 | 3 | 1,281 | 1,117 | 0.87 |
| 240 | 16 | 500 | 2 | 935 | 718 | 0.77 |

Tie sizes range from 2 to 46 equally maximal centres.

**Evidence:** `EV-CODE` and `EV-RUN`, session container, Python 3.13.18.
- Probe: `evidence/tdrg/decision_notes/largest_center_tie_probe.py` (SHA-256 `12c203f8394ade76a153baa0697e81dda2c96225da9169417ee163566c5bea5a`).
- Output: `largest_center_tie_probe_output.jsonl` (`2e60fbc223eed7b36da4cf330a5d40f8c983bbcd1ede8b16b503de4b769f1177`).
- Method: the probe wraps `choose_largest_center` without changing its return value and counts, for every event, whether the maximal in-component degree is shared. A rerun of the first cell reproduced the same counts.

**Limits:**
- These are short runs ($T=500$, cap 600) at $k/N$ between $1/15$ and $1/16$. They are not the §6.6 campaign protocol, and they say nothing about how strongly the outcome depends on which tied centre fires.
- **Not run:** any comparison of tie rules.

**Consequence:** the §6.6 `largest_center` numbers — $rN_T\approx0.76$–$0.80$, $rN_{\rm late\_birth}=0.9995$, $b/\text{step}\approx1.01$–$1.02$, and the policy ordering — are statistics of a branch whose firing centre is label-chosen in most events. They stay valid as statements about that implementation, which is how §6.6 scopes them. They cannot be read as statements about a covariant "one centre fires" law until a covariant rule has been compared.

## 3. Options

Each option is a law choice for the branch. None changes `bound_symmetric`.

| # | Rule for equal-degree centres | Covariance (SG-14) | Effect on the branch | Cost |
|---|---|---|---|---|
| L0 | Keep the node-ID tie-break (status quo); `largest_center` stays declared non-covariant and non-canonical | no | none | none; but its results remain label-dependent in about 80 % of events |
| L1 | Tie → inert (no birth for that component this tick, like `bound_symmetric`) | yes | strong: removes most of the branch's births (most events tie); likely moves the branch toward crystallization | a rerun of the §6.6 cells |
| L2 | Tie → all tied centres fire (partial `all_centers`) | yes (modulo newborn relabelling, as `all_centers`) | `ms_bpe` > 1 on ties; moves toward the avalanche branch | rerun |
| L3 | Tie broken by $G_{\rm cov}$-invariant data (e.g. centre token, neighbourhood structure), with L1 or L2 as fallback on residual symmetric ties | yes, if the data are invariant (SG-14 forbids ID, listing or creation order) | unknown; depends on how often the invariant data still tie | design, plus a check that the data are invariant (as for TDRG-DEF-ORIENT), plus a rerun |
| L4 | Uniformly random choice among tied centres | in distribution only, not per realization; it makes the step stochastic | the branch becomes a stochastic law, unlike every other branch | rerun; a change of model class |

## 4. Recommendation (for the PI; nothing here is adopted)

1. **Now, at no cost:** keep L0 and the existing scope. Have the §6.6 entry state that ties decide the firing centre in most events — the new measurement — when the owners next edit §6.6. That is a scientific scope statement, to be reviewed in a scientific edition, not in v2.13.
2. **Comparison campaign before any law choice** (the co-owner's condition):
   - run L0, L1, L2 and one L3 variant on the same seeds at two §6.6 cells, for example $N=90$, $k=8$ and $N=120$, $k=8$;
   - compare $rN_T$, $rN_{\rm late}$, $b/\text{step}$, `ms_bpe` and the policy ordering;
   - the runs belong on the PI's Windows machine; the script would be a small wrapper of the pinned engine like the probe, and an engine patch is not required.
3. **Decision under TDR-19:** which rule, if any, defines `largest_center` as a covariant law; or whether the branch stays a recorded non-covariant comparison branch. The question "which multistar policy is physical" (TDR-19's own question) is separate and stays OPEN.

## 5. Not in this note

- Any change to the engine, to §6.6 or to SG-14.
- The OPEN-POLICY-GEOMETRY runs, which use `largest_center` as one policy slice. They would inherit whichever rule is chosen.
