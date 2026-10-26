# C7C-M2 Analysis Log

**Governing:** `NG_C7C_M2_ANALYSIS_OPENING_MANIFEST_v1.json` (`d170efb5…5d73`), which pins the preregistration (`248f128c…8987`), its freeze manifest, Census Protocol v1 and both census results. Entries are appended in order and never edited; corrections are new entries.

---

## E0 — 2026-09-30 — Inspection order and column discipline (fixed before any outcome inspection)

**Inspection order (co-owner ruling, literal):**
1. Level a: construct only the candidate witnessed chains `D̃_mid^a` and the relation `≈_a`; **no Π is inspected**. N1(a) may be assessed here.
2. Evaluate **source Π** on the candidate middle chains; those with Π true form `D̃_M2^a`.
3. Only then assess **N2(a)**: at least one admitted source chain together with a physically distinct equivalent replacement.
4. If N1/N2 are non-vacuous, run WD-DOM: for every admitted source chain and every frozen witness choice, form the canonical `[φ′]` and evaluate **replacement Π**. One certified `¬Π` counterexample ⇒ FAIL(a); a universal proof plus N1/N2 ⇒ PASS(a); otherwise INCONCLUSIVE under the preregistration.
5. The same order for level b; then place the result in one of the six admissible reading-matrix combinations.

**Source Π vs replacement Π.** Source Π decides membership in `D̃_M2` and thus whether N2 can apply. Replacement Π is WD-DOM's outer-leg test.

**Column discipline.** The vacuity verdict (N1, N2) and the WD-DOM truth evidence (source-Π set, replacement-Π results, counterexamples) are kept in **separate columns**. N1/N2 are **not** used as gates that stop Π inspection: a certified FAIL counterexample is informative even where PASS is excluded. The final level verdict combines the two columns only at the end.

---

## E1 — 2026-09-30 — Step 1, level a: `D̃_mid^a`, `≈_a`, N1(a). **No Π inspected.**

### E1.1 Records and orientation (from the opening manifest, 120 records)
- **Continuous dyad.** `U-DYAD-1 = (B_+, B_-)` and `U-DYAD-2 = (B_-, B_+)`. The same certified domain, per C7C-0: the swap preserves domain and co-realization. Instances are the orbits `ω` of the certified tube; both records live on every instance.
- **TDR-G (118 records).** Each record is `x_s = (SWAP_s, P3_s)` on the trajectory of its frozen seed `s`. **Orientation note:** the owner's live text does not state the orientation literally. It follows from the sealed artifacts: the harness forms the class as `reduced(n_swap, n_p3)`, and C7B-ALG-T3 counts A-events against B-events, so A = SWAP and B = P3. The Census-1 TDR-G universe holds only the witness records as certified (C-2 option (i)); C7C-0 swap images `(P3_s, SWAP_s)` were not enumerated for TDR-G and are not in the admissible set.
- **Instance identity.** As recorded in census F5: one frozen seed → one deterministic trajectory; one dyad orbit → one instance.

### E1.2 Candidate middle chains `D̃_mid^a`
Definition (prereg v4 §4.2, §5): `(x, [φ], y)` with `𝔍^R(x) ~_a 𝔍^L(y)`, i.e. the **same certified stream on the same instance**, with the identity germ on a common tail.

| family | right end of `x` | left end of `y` | `~_a` possible? | candidate chains |
|---|---|---|---|---|
| dyad | `U-DYAD-1`: `B_-` on `ω` | `U-DYAD-2`: `B_-` on `ω` | yes — identical interface `(B_-, 𝒫_ω, N_{B_-})` | `(U-DYAD-1, [id], U-DYAD-2)` per instance `ω` |
| dyad | `U-DYAD-2`: `B_+` on `ω` | `U-DYAD-1`: `B_+` on `ω` | yes | `(U-DYAD-2, [id], U-DYAD-1)` per instance `ω` |
| dyad | `U-DYAD-1`: `B_-` | `U-DYAD-1`: `B_+` | no — different streams | — |
| TDR-G | `P3_s` | every TDR-G left end is `SWAP_{s′}` | **no** — schema keys differ (P3 ≠ SWAP) | **none** |
| cross-family | — | — | no — `κ_b` keys differ, so no same stream either | none |

**`D̃_mid^a` = { `(U-DYAD-1, [id], U-DYAD-2)_ω`, `(U-DYAD-2, [id], U-DYAD-1)_ω` : `ω` an instance of the certified tube }.** It is empty on the admissible TDR-G set and across families.

### E1.3 The relation `≈_a`
`x ≈_a x′` iff `x ≡_Q x′`, `𝔍^L(x) ~_a 𝔍^L(x′)` and `𝔍^R(x) ~_a 𝔍^R(x′)`. Since `~_a` requires the same stream on the same instance at **both** ends:
- `U-DYAD-1` vs `U-DYAD-2`: left ends `B_+` vs `B_-` — not related.
- a dyad record on instance `ω` vs the same record on `ω′ ≠ ω`: different instances — not related.
- `x_s` vs `x_{s′}`, `s ≠ s′`: different instances — not related.

Hence **`≈_a` is the identity relation** on record-instances of the admissible set.

### E1.4 N1(a)
N1 requires `≈_L` to identify at least one pair of **physically distinct** realizations. `≈_a` identifies none.

| level | N1 | N2 | WD-DOM evidence |
|---|---|---|---|
| a | **FAIL** — `≈_a` is the identity on the admissible set | not yet assessable (needs source Π, step 2) | not yet inspected |

By prereg §8 a failed N1 already **excludes PASS(a)**. Per E0, Π inspection still proceeds: steps 2–4 are carried out at level a, in order, to record the WD-DOM evidence column.

**Next:** step 2, level a — source Π on the two candidate chain families of E1.2.

---

## E1-COR-1 — 2026-09-30 — Orientation provenance (correction to E1.1)

The `(SWAP, P3)` orientation is **not** inferred from the numerical ordering of sealed counters. It is inherited from the frozen C7B-DISC-1 protocol (Number Genesis v1.15, `d56440c6…`, L1512–L1520): `A_d := canonical isolated-dyad swap event`, `B_d := canonical active-P3 successor-shift event`, `p(C) := N_{A_d}(C)`, `q(C) := N_{B_d}(C)`. v1.20.6 carries that protocol in its registry (L2743, "frozen pre-data TDR-G SWAP/P3 discrimination architecture"). The harness ordering `reduced(n_swap, n_p3)` is corroborating evidence only. No science changes.

## E1-COR-2 — 2026-09-30 — N2 consequence of E1 (correction to E1.4)

Within the frozen Census-1 admissible evidence set, `≈_a` is the identity, so no physically distinct equivalent replacement exists. Therefore **N2(a) is already UNSATISFIED on Census-1 evidence**, independently of source-Π occupancy: if source Π is false there is no admitted chain; if it is true there is still no distinct `≈_a` replacement. This is **not** an exhaustiveness theorem over all `R_bd`; Census-1 TDR-G is witness-only. The E0 order is unchanged: source Π is still evaluated (E2), because it carries separate information — the occupancy of `D̃_M2^a`.

---

## E2 — 2026-09-30 — Step 2, level a: source Π on the two dyad chain families. TDR-G and level b not opened.

**Candidates (E1.2):** `(U-DYAD-1, [id], U-DYAD-2)_ω` and `(U-DYAD-2, [id], U-DYAD-1)_ω`.

**Transported outer pairs.** At level a the witness is the identity germ, so the transported outer pair `(A, C)_φ` is the literal pair on the instance `ω`:
- `(U-DYAD-1, [id], U-DYAD-2)`: `x = (B_+, B_-)`, `y = (B_-, B_+)` → outer pair `(B_+, B_+)`.
- `(U-DYAD-2, [id], U-DYAD-1)`: `x = (B_-, B_+)`, `y = (B_+, B_-)` → outer pair `(B_-, B_-)`.

**Adjudication.** `U-DYAD-2 = S(U-DYAD-1)` (C7C-0), so the two candidates are exactly `x ∘ Sx` for `x = U-DYAD-1` and for `x = U-DYAD-2`. Owner v1.20.6 L1994 `[RESULT] [from: ALG]` (**Unrestricted WD-CLOSE: FAIL on the current carrier**): for any `x = (A,B) ∈ R_bd`, `x ∘ Sx = (A,A)` is not two independent event types (SG-NG-20, L250) and **is not in `R_pair`**. By G-bridge the witness germ does not affect the outer pair's `R_pair` status, and at level a it is the identity anyway.

| candidate chain family | outer pair | source Π | basis |
|---|---|---|---|
| `(U-DYAD-1, [id], U-DYAD-2)_ω` | `(B_+, B_+)` | **false** | owner L1994 `[ALG]`; SG-NG-20 |
| `(U-DYAD-2, [id], U-DYAD-1)_ω` | `(B_-, B_-)` | **false** | owner L1994 `[ALG]`; SG-NG-20 |

**Consequence: `D̃_M2^a = ∅` on Census-1 evidence.** No candidate chain is admitted.

| level | N1 | N2 | WD-DOM evidence |
|---|---|---|---|
| a | FAIL (E1.4) | FAIL — forced by `≈_a = id` (E1-COR-2); also `D̃_M2^a = ∅` | source Π false on every candidate; `D̃_M2^a` empty |

**Not yet recorded (E3):** steps 3–4 at level a — the formal N2(a) entry, the WD-DOM evidence entry, and the level-a verdict.

---

## E2-COR-1 — 2026-09-30 — G-bridge wording (correction to E2)

G-bridge does **not** state that `R_pair` membership is independent of the witness germ. It states only that a germ does not itself establish physical co-realization. In E2 the level-a germ is `[id]`, so the transported outer pair is literally `(A, A)`; its failure of `R_pair` membership follows independently from the owner's unrestricted WD-CLOSE theorem (L1994). **No Π-independence across germs is claimed.**

---

## E3 — 2026-09-30 — Steps 3–4, level a, and level-a closure

**Step 3 — N2(a).** UNSATISFIED: no admitted source chain exists (`D̃_M2^a = ∅`, E2), and `≈_a` is the identity on the admissible set (E1-COR-2).

**Step 4 — WD-DOM(a).** With `D̃_M2^a = ∅`, the WD-DOM proposition quantifies over an empty domain. It is **logically vacuous**, and by prereg §8 that is **not a PASS**. No replacement Π can be evaluated, because no admitted source chain exists to replace, so there is **no certified replacement counterexample** and therefore **no FAIL**. The source-Π = false results of E2 concern membership in `D̃_M2^a` (whether a chain is admitted); they are **not** WD-DOM failures and must not be read as such.

| level | N1 | N2 | `D̃_M2` | WD-DOM evidence | verdict |
|---|---|---|---|---|---|
| **a** | UNSATISFIED | UNSATISFIED | `∅` | vacuous on an empty domain; no replacement Π evaluable; no counterexample | **INCONCLUSIVE (vacuous)** |

**Level a = INCONCLUSIVE (vacuous)** on Census-1 evidence. By the frozen reading matrix (prereg v4 §10), the final combination must be one of `INCONCLUSIVE/PASS`, `INCONCLUSIVE/FAIL` or `INCONCLUSIVE/INCONCLUSIVE`, according to level b.

**Next:** level b, step 1 — `D̃_mid^b`, `≈_b`, N1(b). No Π inspected.

---

## E4 — 2026-09-30 — Step 1, level b: `D̃_mid^b`, `≈_b`, N1(b). **No Π inspected.**

### E4-L1 — tail isomorphisms of a chain are translations `[ALG]`
Every record's prefix poset is the chain of initial segments of one trajectory, order-isomorphic to `ℕ`. An order isomorphism `φ : ℕ_{≥m} → ℕ_{≥n}` maps the minimum to the minimum and preserves the successor relation; hence `φ(k) = k − m + n`. So **every level-b witness germ is a translation germ `[c]`**, and `~_b` holds iff the two streams have equal `κ_b` and `sup_n |N(n) − N′(n + c)| < ∞` for some `c`.

### E4-L2 — continuous dyad: cross-orbit `~_b` for each sign `[ALG]`, derived from owner results
Owner inputs (v1.20.6):
- **Canonical section identity** L2082–L2086 `[RESULT] [from: ALG]`: `Θ = 0 ⟺ η_wrap = 0 and ρ > 0`. This is exactly N5-PHYS-1's `B_+` (L1795: `η_wrap = 0` crossing with `ρ > 0`). L-MONO identifies the canonical B count with the lap count (L2171).
- **INF-2** L2171–L2176 `[RESULT] [from: ALG]`: `N_B(M) = M − (τ/2π) log M + O(1)` over `M` blocks (`6M` primitive steps), with a universal `log` coefficient.
- **N5-PHYS-1 strict alternation** (L1805–L1807): `|N_{B_+} − N_{B_-}| ≤ 1` on every prefix.
- A B-event is a primitive transition token, so there is at most one per primitive step.

*Proof.* For orbits `ω, ω′` in the common certified domain of N-5A-S1-INF and N5-PHYS-1, both of which are certified on sufficiently small tubes, so the domain is their intersection: `N^ω_{B_+}(6M) − N^{ω′}_{B_+}(6M)` is a difference of two `O(1)` remainders with the same leading terms, hence bounded. A primitive prefix `6M + r`, `r ≤ 5`, adds at most 5 events, so the difference stays bounded on all primitive prefixes, i.e. witness `[0]`. A translation by `c` changes a count by at most `|c|`, so **every** translation germ `[c]` is a bounded witness. For `B_-`, strict alternation transfers the bound. Hence `B_+^ω ~_b B_+^{ω′}` and `B_-^ω ~_b B_-^{ω′}` for all such `ω, ω′`, with every `[c]` admissible. `κ_b` agrees: same family, schema, sector key, gauge and semantics. No orbit data was generated (census note N-2). ∎

### E4.3 — TDR-G: ordered event densities
Eventual periodicity gives `N_E(n) = α_E n + O(1)` with `α_E = n_E / L_cycle`. By E4-L1, two same-schema TDR-G streams are `~_b` **iff their densities are equal**; then every translation is a bounded witness. Pair-level `≈_b` needs **both** `α_swap` and `α_P3` equal. Equal rational labels alone are **not** sufficient: the same label can come with different absolute densities. Equal ordered densities imply equal labels.

Exact computation from the frozen replay records (evidence `NG_C7C_M2_E4_TDRG_DENSITY_v1.json`, `c67342a9…6fa8`):
- the 118 admissible records fall into **15** classes of equal `(α_swap, α_P3)`, each with **≥ 2** records;
- **567** pairs of physically distinct realizations share a class;
- **80** further equal-density pairs are **not** counted as distinct, because one seed's initial reduced state lies on the other's trajectory, making them two starting points of one orbit.

Frozen sector key `M2-SECTOR-TDRG-N24K1` excludes panel identity, so DISC-1 and DISC-2 records share `κ_b`.

### E4.4 — Candidate middle chains `D̃_mid^b`

| family | candidate chains | basis |
|---|---|---|
| dyad | `(U-DYAD-1_ω, [c], U-DYAD-2_{ω′})` — right end `B_-^ω`, left end `B_-^{ω′}` | E4-L2 |
| dyad | `(U-DYAD-2_ω, [c], U-DYAD-1_{ω′})` — right end `B_+^ω`, left end `B_+^{ω′}` | E4-L2 |
| TDR-G | **none** — right schema P3, every left schema SWAP; `κ_b` schema keys differ | prereg §4.3 |
| cross-family | none — `κ_b` differs | prereg §4.3 |

Here `ω, ω′` range over the common certified domain (`ω = ω′` included, recovering level a) and `[c]` over all translation germs.

### E4.5 — `≈_b`
- **dyad:** `U-DYAD-1_ω ≈_b U-DYAD-1_{ω′}` for all `ω, ω′`: equal labels; left ends `B_+` and right ends `B_-` are `~_b` by E4-L2, with independent end witnesses. The same holds for `U-DYAD-2`. `U-DYAD-1` and `U-DYAD-2` are not related: their left schemas differ.
- **TDR-G:** `x_s ≈_b x_{s′}` iff `(α_swap, α_P3)` are equal, giving 15 classes.

### E4.6 — N1(b)
**SATISFIED.** `≈_b` identifies physically distinct realizations:
- **dyad, analytically:** `U-DYAD-1_ω ≈_b U-DYAD-1_{ω′}` for distinct orbits `ω ≠ ω′` of the certified domain;
- **TDR-G, independently:** 567 physically distinct equal-density pairs.

| level | N1 | N2 | `D̃_M2` | WD-DOM evidence | verdict |
|---|---|---|---|---|---|
| a | UNSATISFIED | UNSATISFIED | `∅` | vacuous | INCONCLUSIVE (vacuous) |
| **b** | **SATISFIED** | not yet assessable (needs source Π) | not yet determined | not yet inspected | open |

**Observation for later steps, not used here:** every translation `[c]` is an admissible witness. WD-DOM(b) quantifies over every witness choice, so steps 2–4 must cover all `[c]`, not just `[0]`.

**Next:** step 2, level b — source Π on the dyad candidate chains of E4.4.

---

## E4-COR-1 — 2026-10-01 — TDR-G distinctness wording (correction to E4.3 and E4.6)

The distinctness criterion of `NG_C7C_M2_E4_TDRG_DENSITY_v1` — two seeds are the same orbit if one's initial reduced state lies on the other's forward reduced trajectory — **proves same-orbit** when it fires, but it is not a complete test of distinctness. Without a global injectivity or merge certificate for the no-birth TDR-G map, two different prehistories could merge into one tail with neither start on the other's forward trajectory. Corrected statement:

> **567 equal-density pairs are not identified as same-orbit pairs by the frozen forward-orbit criterion; 80 pairs are positively identified as two starting points on one orbit (567 + 80 = 647 = all unordered equal-density pairs in the 15 classes). The 567 are supporting level-b equivalence candidates, not a load-bearing proof of physical distinctness, unless a no-birth injectivity/merge certificate is supplied.**

**N1(b) is unchanged:** SATISFIED, with the **continuous-dyad analytic witness** as the load-bearing witness (E4-L2: distinct orbits `ω ≠ ω′` of the certified tube, both ends `~_b`). The TDR-G result is supporting evidence only.

## E4-COR-DATE — 2026-10-01 — Entry dates (correction to E0–E4 headers)

The entry dates were assigned without consulting the clock. The container clock dates the E4 density artifact and the E4 append to **2026-10-01 12:59 UTC**, so **E4's date is 2026-10-01**, not 2026-09-30. E0–E3 carry no per-entry timestamps; file metadata bounds them only to the interval between the opening manifest (2026-09-30 14:49 UTC) and E4 (2026-10-01 12:59 UTC). Their order — the property the log certifies — is intact by append-only construction. From this entry on, dates are taken from the clock.

---

## E5 — 2026-10-01 — Step 2, level b: source Π on the dyad candidate chains. TDR-G not opened (no TDR-G chain in `D̃_mid^b`).

**Candidates (E4.4).** `(U-DYAD-1_ω, [c], U-DYAD-2_{ω′})` and `(U-DYAD-2_ω, [c], U-DYAD-1_{ω′})`, for all `ω, ω′` in the common certified domain and every translation germ `[c]`, `c ∈ ℤ`.

**Transported outer pairs.** For `(U-DYAD-1_ω, [c], U-DYAD-2_{ω′})`, `x = (B_+^ω, B_-^ω)` and `y = (B_-^{ω′}, B_+^{ω′})`, so `(A, C)_φ = (B_+^ω, B_+^{ω′})`, with `N_A` on `𝒫_ω` and `N_C` read through the translation `c`. Symmetrically the other family gives `(B_-^ω, B_-^{ω′})`.

**Owner criterion.** `R_pair` (L1973–L1974): *certified co-realized ordered physical pairs (A,B; domain, order, provenance) satisfying the event-stream, common-order and prefix-cofinal repeatability requirements*. SG-NG-20 (L250): *two independently certified event/recurrence types co-realized in one admissible physical sector*, with a declared RTG-native order relation; ratios of powers or blockings of one generator are re-indexing.

**Adjudication, case by case. Every case is decided on the outer pair's own certified status, never on the germ (E2-COR-1).**

| case | outer pair | source Π | basis |
|---|---|---|---|
| **S** — `ω = ω′`, `c = 0` | `(B_±^ω, B_±^ω)`, literally `(A, A)` | **false** | owner L1994 `[ALG]` (`x ∘ Sx`), SG-NG-20 |
| **S′** — `ω = ω′`, `c ≠ 0` | one stream compared with a translate of itself | **false** | not two independently certified event types; a translation is re-indexing of the same stream (SG-NG-20) |
| **X** — `ω ≠ ω′`, any `c` | `(B_±^ω, B_±^{ω′})` | **false** | (i) **not co-realized**: `ω` and `ω′` are distinct realizations (census F5 instance identity: one orbit, one instance); no certified provenance places both streams in one realization with a common order, and the translation germ only aligns comparison contexts and cannot create co-realization (G-bridge); (ii) additionally, both streams are instances of the **same** event type (`B_+` resp. `B_-`), not two independently certified types (SG-NG-20) |

Ground (i) alone suffices for case X; ground (ii) is recorded as independent support.

**Consequence: `D̃_M2^b = ∅` on Census-1 evidence.** No dyad candidate chain at level b is admitted, for any orbits or any translation germ. There is no TDR-G candidate (E4.4).

| level | N1 | N2 | `D̃_M2` | WD-DOM evidence |
|---|---|---|---|---|
| a | UNSATISFIED | UNSATISFIED | `∅` | vacuous — INCONCLUSIVE (vacuous) |
| **b** | **SATISFIED** (dyad, E4-COR-1) | not yet recorded (E6) | **`∅`** | source Π false on every candidate |

**Not yet recorded (E6):** steps 3–4 at level b — the formal N2(b) entry, the WD-DOM(b) evidence entry, the level-b verdict, and the reading-matrix placement.

---

## E5-COR-1 — 2026-10-01 — Uniformity wording (correction to E5)

E5's sentence "every case is decided on the outer pair's own certified status, never on the germ" reads too generally. Corrected: **for these dyad candidate families, the obstruction is uniform in `[c]`; no general Π-independence from the witness germ is inferred.** `[c]` remains part of the quantification; the same independent obstruction simply holds for every `c`. No scientific change.

---

## E6 — 2026-10-01 — Steps 3–4, level b; level-b closure; final reading-matrix placement

**Step 3 — N2(b).** UNSATISFIED: N2 requires at least one admitted source chain, and `D̃_M2^b = ∅` (E5).

**Step 4 — WD-DOM(b).** The source domain is empty, so WD-DOM(b) is **logically vacuous**. N1(b) being satisfied does **not** turn this into a PASS, because N2 is missing. There is no certified replacement counterexample, hence **no FAIL**.

| level | N1 | N2 | `D̃_M2` | WD-DOM evidence | verdict |
|---|---|---|---|---|---|
| a | UNSATISFIED | UNSATISFIED | `∅` | vacuous; no counterexample | **INCONCLUSIVE (vacuous)** |
| b | SATISFIED (dyad analytic witness) | UNSATISFIED | `∅` | vacuous; no counterexample | **INCONCLUSIVE (vacuous at N2)** |

**Reading-matrix placement (prereg v4 §10):** `(a, b) = (INCONCLUSIVE, INCONCLUSIVE)`, an admissible combination. Reading: *neither level supplies an instance; report, do not upgrade.*

**C7C-M2 outcome on Census-1 evidence: INCONCLUSIVE / INCONCLUSIVE.** Census-1 decides WD-DOM **neither positively nor negatively**. No M2 theorem verdict is drawn.

### E6-D — Diagnostic / evidence-architecture finding (not an M2 verdict)

**Scope correction to the pre-E6 discussion.** It is **not** true that every admissible realization carries exactly two independent event types; the continuous-dyad realization also carries, for example, the primitive `T` stream and the canonical-section stream, and the owner closed N-5A on two independently certified co-realized recurrence types. That earlier phrasing is withdrawn.

**Finding.** The admissible Census-1 `R_bd` evidence **does not contain a certified nondegenerate composable three-stream configuration**, i.e. a witness of the shape
```text
(A,B) ∈ R_bd ,   (B,C) ∈ R_bd ,   (A,C) ∈ R_pair ,
```
within one certified comparison architecture, with a suitable middle-interface witness. Its dyad contribution is only the reciprocal bounded pair `(B_+,B_-)` / `(B_-,B_+)`, and every chain built from it has an outer pair that is the same stream, a re-indexing of it, or not co-realized (E2, E5). Its TDR-G contribution is only the oriented `(SWAP, P3)` witness records, with no reversed or adjacent bounded leg in the admissible set (E1, E4).

Having three event types is a **necessary** intuition, not a sufficient condition: even with three types, a bounded leg or the outer `R_pair` certificate may be missing.

**Diagnosis.** The frozen WD-DOM instrument is well-defined but receives **no admitted source chain** on the present evidence set. **Missing object: a certified nondegenerate composable 3-stream carrier witness.**

**Constraints unchanged.** This finding authorizes no new realization search: G-search and M-4 HOLD stand. It specifies only the **evidence shape** a future, separately preregistered campaign would need. M2-0, M2-1 and M2-2 remain internal design lemmas of the frozen instrument; entering M2-1 into the owner ledger is a separate owner decision.

**Analysis phase closed.** All steps of the E0 order have been executed at both levels, in order.
