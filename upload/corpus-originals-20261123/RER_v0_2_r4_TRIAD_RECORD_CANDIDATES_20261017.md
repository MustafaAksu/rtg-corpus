# RER v0.2 r4 — Triadic-side source delta and record candidates

**Date:** 17 Oct 2026.
**Author:** Claude (Triadic contributor / auditor).
**Status:** NONCANONICAL review draft for the RER editor.

**What this file is not:**
- It is not an RER revision.
- It is not an owner edit.
- It is not an adoption.

**Base:**
- RER v0.2 DRAFT r3.1, received copy SHA-256 `a57aef068ec9eb31f1d7981c239faf855b758652a4e6a37c4295e712d3e42bf9`.
- REGISTRY r3.1 JSON, SHA-256 `b996ba8e0d3d472ba31d3b1613b4376a3739f1543b072d6c3abe9a8626e8a213`.
- r3.1 stays unfrozen. Nothing below changes an existing r3.1 record's grade, formula or exactness.

The four parts follow the editor's 17 Oct request:
- (A) source inventory delta;
- (B) full record candidates;
- (C) r3.1 → r4 change matrix and open gaps;
- (D) Triadic consumer-sync queue.

**Evidence vocabulary** (r3.1 §2, unchanged):
- `OWNER-REPORTED HASH`: the owner's text prints the hash; this preparation did not byte-hash a delivered file.
- `BYTE-HASHED HERE`: the file was hashed in this preparation.
- `EXECUTED HERE`: the script ran in this preparation, exit 0.
- `SOURCE-READ`: the passage was read in the project copy.

**Receiving review:** for files that exist only in this contributor workspace, the receiving reviewer should treat the hashes as source-reported until the files themselves are delivered.

---

## A. Source inventory delta (new or changed rows for r3.1 §7)

| Source ID (proposed) | Version / status | Identity | Evidence in this preparation |
|---|---|---|---|
| `DYAD6412_1` | Dyadic v6.4.12.1. Metadata-only release (17 Oct) of adopted v6.4.12 (16 Oct); scientific text byte-identical to v6.4.12 | release `36e7ef58c952f19cd48683c601957f6a01d90c2e2c6f548b28c1707764c5f107`; v6.4.12 `c2f00eb0832e6aabcbcfd1a3c583d6f1e7b0950a2f8db97d89045ed0bcb438e8` | OWNER-REPORTED HASH (metadata change record); §§1, 2, 6.15, 6.16, 7 SOURCE-READ |
| `GEN286` | Genesis v2.8.6, ADOPTED 16 Oct | `294c6fc26482d7deae42900cb50b3029ac81e96d66e239bfe8b797e95fdaa269` | OWNER-REPORTED HASH (release record); §§1, 3 (SG-15), 6.3, 6.3a, 7 SOURCE-READ |
| `RRF082` | RRF v0.8.2, ADOPTED working standard 17 Oct | own SHA-256 not printed in the file; predecessor v0.8.1 `1ba4713855a59b51cad8d79f88007380dfe2364f1b638478a927eea68f642c4c` | header and §§0.2, 2.4b, 4.2, 6.2, 8.1, 10.2 SOURCE-READ; the separate v0.8.2 adoption record was not inspected. **Gap G1** |
| `K3REC` | K3 cubic-factor obstruction SESSION record v0.1.2 (Genesis Stage A) | `9f95d48d23a340738146271d4bcf1a483b04252e9210c9f403a7f23172dd083a` | OWNER-REPORTED HASH (Genesis manifest); SOURCE-READ |
| `K3CERT` | `k3_obstruction_exact_check.py` | `384aaa5f17ecd0786960b3a97fc08a5d332c9e12809a2c92796616f2615a01ee` | OWNER-REPORTED HASH; not rerun here |
| `OPEN19REC` | DYAD OPEN 19 proof SESSION v1.2 | `6749df1126b36453f1f860dd797a872f291fcc7926412225f839acfb2e60e1c6` | OWNER-REPORTED HASH (DYAD §8); SOURCE-READ |
| `OPEN19CERTS` | `dyad_open19_kernel_check.py` v1.1 / `dyad_open19_R0_identity_cert.py` | `1cb40446c0289424fcb8539c77aec6d43f4e6a0873434645b8cc3dc4397a291e` / `c8c144426b2c9e795df19a997b181209fce6ab7edeaa1b9c04e731ad0d059cf8` | OWNER-REPORTED HASH; not rerun here |
| `G2NOTE04` | DYAD–RRF–OFN G2 consolidated note v0.4 (noncanonical) | no hash printed | SOURCE-READ. **Gap G2** |
| `TRIAD16` | Triadic v1.6 (unchanged owner) | `c768687cec6d52ffd358dc362cee4348f076160943564adaa461e6c7c4595b36` | BYTE-HASHED HERE; matches r3.1 |
| `GIIL019` | Genesis Identification & Inheritance Ledger v0.19 DRAFT, as pinned by Genesis queue v0.4 §0 | `f6320914190b434332058b69fe0974ce584d1a8167ae40e2650091be5bdbe2f8` | OWNER-REPORTED HASH (queue); bytes not available. An accessible v0.16 is an older noncanonical draft. **Gap G3** |
| `TRIAD_BGJ` | Triadic note: formal involution vs birth graph, 15 Oct | `494b34f2915e6922e4b36c2bcee242b454c2e7ac5f60670b49d6a82648a89413` | contributor workspace; BYTE-HASHED HERE |
| `TRIAD_BGJ_PY` / `_LOG` | `triad_formal_involution_birth_jet.py` / log | `5c020986bc0ee54b4c9f0795e954e625088802253b78546a479d17fb193a9feb` / `34d48bd29d68f1a1e86adf38966047bc2ab96c4900b6b9b790fff628f4974012` | EXECUTED HERE, exit 0 (15 Oct; standard library, ~1 s) |
| `TRIAD_GC_PY` / `_LOG` | `triad_involution_graph_completion.py` / log | `024c9ad1ee5d36ecc088de1e8301109c75fd236d524987ce4a2e681cf89a0574` / `206ec8d3d1d1907ec459a6a989980c1259b93d35cebfe3b15f4f7a53d9e0ec84` | EXECUTED HERE, exit 0 |
| `TRIAD_CK_PY` / `_LOG` | `triad_cubic_centralizer_kernel_check.py` / log | `fac5ffe7ccfefc9ded108b413e04d2bddb1e6d3fbb1b835edea5ba88af082e91` / `275ce62bdd6d86887020f10ea16304538fae11a3404911fd9f9670d1861fc62e` | EXECUTED HERE, exit 0 (17 Oct; standard library, ~90 s) |
| `TRIAD_EC_PY` / `_LOG` | `triad_k3_econjugacy_check.py` / log | `c3168ca31144d5ac9a4f08067b1346be4f61a67f91f79b545940c1f67ce5cb62` / `607eca6cf2ed07ae3eb7976fdbb80aee078509115d6ccff64eac443d7d9e8e66` | EXECUTED HERE, exit 0 (17 Oct; exact Fractions + mpmath at 50 digits) |
| `TRIAD_RCPT` | Triadic receipt of the 16–17 Oct updates | `90a171d78bdf7c154e340aece80e634ede78a96dad1207d8e7a2688c4e182242` | contributor workspace; BYTE-HASHED HERE |

Retained unchanged from r3.1:
- `RECOG` v0.3.20, freeze candidate. No later RECOG release is assumed; Dyadic v6.4.12.1 itself cites v0.3.20.
- `POLY` (`03042f84…d83c`, re-hashed here and unchanged).
- `SERIES2`, `FORMALSCRIPT`, all Stage-2 sources.

**Superseded as governing pins, kept as history:**
- `GEN` v2.8.5 is superseded by `GEN286`.
- `RRF08_ADOPTED` v0.8 is superseded by `RRF082`; v0.8.1 sits between them.
- `DYAD` v6.4.10 is superseded by `DYAD6412_1`; the v6.4.10 archived pin stays as the v0.1 source pin.
- `OFN` v0.8 is superseded by `OFN9`, already present.

**Custody note** (Genesis v2.8.6 §1 / Dyadic §1):
- The primitive map has **one** definition. `DYAD-DEF-PRIMITIVE-MAP` is the owner; `GEN-DEF-PRIMITIVE-MAP` is a recognized alias.
- RER must cite it as one object, not as two independent sources.

---

## B. Record candidates (r3.1 §2 schema: six scientific fields plus contract fields)

Each record carries the r3.1 field structure. The local keys are navigation keys, not owner RIDs.

<a id="rer-gen-k3-modal"></a>
### RER-GEN-K3-MODAL — Genesis planar-factor no-go applied to the RER modal map at the primitive clock

**Primary grade:** [THM], imported at owner grade; the application step is [ALG].
**Exactness:** `EXACT_LOCAL`.
**Task:** `SOURCE_SCOPED_RESULT_RECORDED`.
**Registry/owner adoption:** pending / Genesis owner theorem adopted in v2.8.6.

| Field | Contract |
|---|---|
| Carrier | Ambient modal state X=(s,c) ∈ R⁴ of r3.1 §3; GEN-CONDITIONAL-MODAL-REPROJECT-EACH-STEP; identified with the Genesis sum-zero carrier 𝒞 by E; profile UNREGISTERED_CONDITIONAL_OR_ABSTRACT_NO_PROFILE_CREATED. |
| Observables | Any local C³ submersion E′:(R⁴,0)→M² (planar target), or C¹ submersion onto M¹ or M³; no observable is privileged. |
| Constraints | Primitive clock only: E′∘𝒩 = T′∘E′ near 0. T′ is arbitrary (fixed point, linear part and cubic coefficient all free). Regularity C³ for d=2 and C¹ for d=1,3. |
| Transformation law | Linear conjugacy E∘𝒩 = F₁∘E with F₁ = P_𝒞∘T^{×3} (Genesis §6.3a). The per-edge eigenframe 𝓛^{×3} is linear and commutes with mean subtraction, so the no-go transports exactly. |
| Closure status | NO_LOWER_DIMENSIONAL_PRIMITIVE_CLOCK_FACTOR: 𝒩 has no local C³ planar factor and no C¹ factor of dimension 1 or 3. |
| Memory | A factor obstruction is not a proof of new information, physical dimension or compulsory memory. No memory or age carrier is added. |

[THM] **EXACT_LOCAL** `[import: RTG_GENESIS_GEOMETRY_DSN_v2.8.6 §6.3a | RID: GEN-THM-K3-PLANAR-FACTOR-NOGO]`. The projected-K₃ primitive map has no local submersive factor of strictly lower real dimension:
- d=1 and d=3 are excluded at C¹;
- d=2 is excluded at C³.

[ALG] **Application.**
- P·E = I₂ and E·P = I₃ − J/3, so E is a linear isomorphism R⁴ → 𝒞.
- (E⊗I₂)∘𝒩 = ((EP)⊗I₂)∘T^{×3}∘(E⊗I₂) = F₁∘(E⊗I₂).
- Hence every factor E′ of 𝒩 gives the factor E′∘E⁻¹ of F₁ with the same target, regularity and T′, and conversely.

Formula/witness: `E o N = F1 o E`; exact identities `PE=I`, `EP=I-J/3`. Numerical check: max |E𝒩(x) − F₁(Ex)| = 1.3·10⁻⁵¹ at 50 random points (50 digits).

**Domain / admissibility:** Local germs at 0, as in Genesis §6.3a. No sector or punctured domain.

**Map / clock:** `N` — the **primitive** step, reprojected each step. **Not** the six-step map F = 𝒩⁶.
- A factor of 𝒩 gives one of 𝒩⁶, but not conversely.
- Step (a) of the Genesis proof uses the linear part λ of the primitive map.
- **Factors of 𝒩⁶ alone (six-step contract) are not covered: OPEN (gap G5).**

**Factor or parametrization tested:** Arbitrary local submersive semiconjugacy onto lower-dimensional dynamics.

**Order / error:** Exact local; cubic comparison (Genesis §6.3a (b)–(e)); no radius.

**Contract type:** `PRIMITIVE_CLOCK_SEMICONJUGACY_NO_GO`. This is distinct from:
- RER-GEN-C05/C06, which are six-step, Qs-preserving minimal-rank tests;
- RER-GEN-C08/C10, which are reachable and regular-reachable factor tests.

The results do not imply one another.

**Evidence:**
- Genesis owner theorem: OWNER-REPORTED HASH `GEN286`, proof SOURCE-READ.
- Source data certificate `K3CERT`: OWNER-REPORTED, not rerun here.
- E-conjugacy: `TRIAD_EC_PY`, EXECUTED HERE.
- The chiral identities of the K3 source were independently re-checked by Claude in G2 note v0.4 §3a: SOURCE-READ, not rerun here.

**Review receipt:** none yet.

Import/reference:
- `GEN286` §6.3a and SG-15;
- `K3REC` §§2, 4;
- `TRIAD_EC_PY`;
- `TRIAD_RCPT` §2.

[OPEN] C¹ or C² planar factors.
[OPEN] Six-step-clock factors (gap G5).
[OPEN] Non-submersive or non-local factor maps.
[OPEN] Other carriers, including the h-transported carrier.
[OPEN] Physical node exchange / G2.

**Next test:** If the six-step contract is wanted, test planar factors of ℱ = 𝒩⁶ directly. Genesis step (a) does not apply there, because Dℱ(0) = I.

**Non-transfer:**
- No physical node-exchange, carrier or network–dyad selection (Genesis SG-15).
- No identification of EF=TE with EF=T⁶E.
- No new independent state datum or physical emergence.
- No automatic RRF registration.

<a id="rer-dyad-formal-involution"></a>
### RER-DYAD-FORMAL-INVOLUTION — Unique formal −I involution of the isolated dyad (owner import)

**Primary grade:** [THM], owner grade.
**Exactness:** `FORMAL_ONLY`.
**Task:** `SOURCE_SCOPED_RESULT_RECORDED`.
**Registry/owner adoption:** pending / Dyadic owner theorem adopted in v6.4.12.

| Field | Contract |
|---|---|
| Carrier | Formal germs of the isolated dyad at P₁ in the raw linear frame W=𝓛(ρ,η); profile RRF-DYAD-W (RRF v0.8.2 §2.3, §2.4b). Not the triad carrier. |
| Observables | Formal state; no comparator is privileged. |
| Constraints | F=T⁶=id+μ\|W\|²W+O(4) with Re μ ≠ 0 and Im μ ≠ 0. Real formal category. |
| Transformation law | R₀=T³∘F^{−1/2}=ĥ(−I)ĥ⁻¹ for any formal Poincaré–Dulac normalizer ĥ. The finite chart S_h=h₆(−I)h₆⁻¹ equals R₀ only through jet degree 6. |
| Closure status | FORMAL_UNIQUE: R₀ is the unique formal involution with DR(0)=−I that commutes with F. It also commutes with T. The tangent-to-identity formal centralizer of F is {exp(s log F)}. |
| Memory | Formal symmetry; no physical pole exchange and no memory carrier. |

[THM] **FORMAL_ONLY**. Imports:
- `[import: DYAD v6.4.12.1 §6.16 | RID: DYAD-THM-FORMAL-INVOLUTION-UNIQUE]`;
- `[RID: DYAD-THM-FORMAL-CENTRALIZER]`;
- `[RID: DYAD-ALG-CENT-KERNEL]`.

Conditional analytic consequence `[RID: DYAD-THM-ANALYTIC-CLOCK-BRIDGE]`: an analytic involution with RT⁶=T⁶R and DR(0)=−I commutes exactly with T.

**Domain / admissibility:** Formal; the analytic bridge is local, under the §6.15(b) hypotheses.

**Map / clock:** Both T and T⁶. The same formal involution is selected for both. The factor contracts EF=TE and EF=T⁶E remain distinct.

**Factor or parametrization tested:** Not a factor; a symmetry classification.

**Order / error:** All formal orders. No convergence: OPEN 20 (B-an, B-∞), `DYAD-OPEN-INVOLUTION-REALIZATION`.

**Contract type:** `FORMAL_SYMMETRY_CLASSIFICATION`.

**Evidence:**
- Owner theorem: OWNER-REPORTED HASH `DYAD6412_1`, SOURCE-READ.
- Kernel and R₀ certificates: `OPEN19CERTS`, OWNER-REPORTED, not rerun here.
- Independent polar-coordinate proof of Lemma K: G2 note v0.4 §2a (ChatGPT), SOURCE-READ.

**Review receipt:** none yet.

Import/reference:
- `DYAD6412_1` §§6.15, 6.16 and §2 OPEN 19/20;
- `OPEN19REC`;
- `RRF082` §2.4b.

[OPEN] OPEN 20 B-an: convergence of R₀, equivalently of F^{1/2}.
[OPEN] OPEN 20 B-∞: C^∞ flat uniqueness.
[OPEN] Physical exchange (RRF OPEN-A).

**Next test:** None in RER. This is an owner import.

**Non-transfer:**
- No triad statement follows from this record (see RER-TRIAD-FORMAL-INVOLUTION).
- No physical pole exchange.
- S_h is not upgraded beyond degree 6.

<a id="rer-triad-formal-involution"></a>
### RER-TRIAD-FORMAL-INVOLUTION — Formal involution of the conditional modal map; uniqueness only at the primitive clock with linear part −I₄

**Primary grade:** [THM] for (i).
**Exactness:** `FORMAL_ONLY` for (i); `FINITE_ORDER` for the (ii) subclaim.
**Task:** `SOURCE_SCOPED_RESULT_RECORDED`.
**Registry/owner adoption:** pending / none. The Triadic contributor result is not owner-adopted.

| Field | Contract |
|---|---|
| Carrier | Formal germ R[[s₁,s₂,c₁,c₂]]; GEN-CONDITIONAL-MODAL-REPROJECT-EACH-STEP; profile UNREGISTERED_CONDITIONAL_OR_ABSTRACT_NO_PROFILE_CREATED. |
| Observables | Formal state; slot actions ρ_Π = PΠE ⊗ I₂. |
| Constraints | D𝒩(0)=A⊕A, A³=−I; ℱ=𝒩⁶=id+G₃+O(4). Fixed conditional model; no physical selection. |
| Transformation law | Ŝ_triad := 𝒩³∘ℱ^{−1/2}. Every slot permutation ρ_Π commutes exactly with 𝒩, and hence with Ŝ_triad. |
| Closure status | (i) FORMAL_UNIQUE_PRIMITIVE_CLOCK. (ii) LEMMA_K_DOES_NOT_TRANSFER: the cubic kernel is two-dimensional. |
| Memory | Formal symmetry only; no physical node exchange and no memory carrier. |

[THM] **(i) FORMAL_ONLY.** Ŝ_triad is a formal involution with DŜ(0)=−I₄ that commutes with 𝒩 and with every ρ_Π. It is the **unique** formal involution that both commutes with 𝒩 and has linear part −I₄.

*Proof (dimension-free, as in G2 note v0.4 §2):*
1. R commutes with ℱ, hence with ℱ^{−1/2}. Tangent-to-identity roots are unique, since log is bijective.
2. So R commutes with Ŝ.
3. RŜ is a tangent-to-identity involution.
4. A tangent-to-identity involution is the identity, so R = Ŝ.

The jet check `TRIAD_BGJ_PY` (exact, degree ≤ 5) confirms ŜŜ=id, Ŝ𝒩=𝒩Ŝ, DŜ=−I₄, slot commutation for all four actions, and Ŝ≠−I.

[ALG] **(ii) FINITE_ORDER.** Two dyad facts do not transfer to the triad.

*Linear-part dichotomy.* The real commutant of A⊕A is all complex-linear maps of C². So involutions commuting with 𝒩 need not have DR(0)=±I. The exact slot reflections (e.g. c↦−c) are examples.

*Lemma K.* On homogeneous real vector fields of degree k on R⁴, dim ker(ad_{X₃}) = 0, **2**, 0, 0, 0, 0 for k = 2, …, 7. The dyad has dimension 1 at k=3.
- [NUM] identification in chiral modes u=w₁+λw₂, v=w₁+λ̄w₂: the kernel is spanned by
  - A = (a u|u|², −iβ*|u|² v),
  - B = (−iβ*|v|² u, a v|v|²),
  - where a = 1/6 − i√3/9 and β* = 2√3/9;
  - X₃ = A + B;
  - least-squares fit residual 1e-14.
- Hence:
  - the formal tangent-to-identity centralizer of the triad's ℱ is **not known** to be {exp(sX)};
  - uniqueness for involutions that commute with ℱ only is **OPEN**;
  - there is no triadic analogue of DYAD-THM-ANALYTIC-CLOCK-BRIDGE.

Formula/witness: `S = N^3 o F^(-1/2)`; `F^(-1/2) = x - g/2 + (3/8)(g o F - g) + O(7)` with g = F − id; `dim ker ad_X3 |_k = (0,2,0,0,0,0)`.

**Domain / admissibility:** Formal germ at 0. Kernel dimensions are exact for k ≤ 7 only.

**Map / clock:** Uniqueness at the **primitive** clock 𝒩. The six-step-only class is open.

**Factor or parametrization tested:** Not a factor; a symmetry classification.

**Order / error:**
- (i) holds at all formal orders by proof; the jet check is through degree 5.
- (ii) is exact for k = 2, …, 7.
- No convergence.

**Contract type:** `FORMAL_SYMMETRY_CLASSIFICATION`.

**Evidence:**
- `TRIAD_BGJ_PY` and `TRIAD_CK_PY`: EXECUTED HERE.
- The proof of (i) was reviewed by the Triadic reviewer (15 Oct; scope narrowed 17 Oct by the RER editor).

**Review receipt:** Triadic reviewer ACCEPT (formal, 15 Oct). Scope narrowing accepted by the RER editor on 17 Oct.

Import/reference:
- `TRIAD_BGJ` §1;
- `TRIAD_RCPT` §3;
- `TRIAD_CK_PY`;
- G2 note v0.4 §2 (dimension-free uniqueness argument).

[OPEN] Six-step-only uniqueness. This needs the 4D formal centralizer of ℱ: whether A and B separately extend to all orders.
[OPEN] Convergence of Ŝ_triad.
[OPEN] Physical node exchange (OFN OPEN-OPA, RRF OPEN-A).

**Next test:** Decide whether span{A, B} extends to a two-parameter formal centralizer. Solve [X, Y] = 0 order by order with Y₃ = B. Uniqueness of the completion follows from the zero kernels at k ≥ 4, so only the obstruction (cokernel) has to be computed.

**Non-transfer:**
- No physical node exchange.
- The slot symmetry is not node-coincidence invariance (RRF §6.2).
- No identification with the dyad's R₀ or with the h-transported carrier of G2 note v0.4 §5b.

<a id="rer-triad-birth-graph-involution"></a>
### RER-TRIAD-BIRTH-GRAPH-INVOLUTION — Birth graph under Ŝ_triad: degree-4 graph defect, unique even completion, no permutation of age sheets

**Primary grade:** [ALG].
**Exactness:** `FORMAL_ONLY`, with explicit exact jets through degree 5.
**Task:** `SOURCE_SCOPED_RESULT_RECORDED`.
**Registry/owner adoption:** pending / none.

| Field | Contract |
|---|---|
| Carrier | Trial birth graph B_κ(s)=(s, κ̃Q(s)Ms), M=[[1,−2],[2,−1]], κ=√3κ̃ (= c₀ = κQ_sJ_Qs of Genesis §6.3); formal age family 𝒞(s,τ) (RER-TRIAD-FORMAL-AGE). |
| Observables | Covariance defect D(s)=Ŝ(B(s))−B(−s); graph defect G(s)=Ŝ_c(B)−C(Ŝ_s(B)). |
| Constraints | Fixed real κ̃; formal; age-sheet statement on the pinned κ̃=1 table. |
| Transformation law | Covariance (D) and graph invariance (G) are separate contracts. D's degree-2/3 parent terms are effects of Ŝ's nonlinear chart, not graph data. |
| Closure status | (a) The cubic graph is not Ŝ-invariant. G vanishes at degrees 2–3, is first nonzero at degree 4, and is exactly κ̃-linear. (b) Unique even completion C₄=G₄/2; with it, the defect vanishes through degree 5. (c) Ŝ maps no age sheet onto any age sheet (κ̃=1). |
| Memory | Formal graph geometry; does not select a birth initialization, a post-birth law or a memory carrier. |

[ALG] **(a)**
- G₄ = κ̃·[¾r⁴ − 4r³e + 6r²e² − 6re³ + 11/4 e⁴, 11/4 r⁴ − 7r³e + 9r²e² − 7re³ + 2e⁴] ≠ 0.
- D_parent is nonzero from degree 2 and κ-free through degree 5.
- D_child is zero at degrees 2–3 and first nonzero at degree 4, proportional to κ̃.

[COR] (contributor, 15 Oct): the earlier claim Ŝ(B_κ(s)) = B_κ(−s) + O(|s|⁵) is withdrawn.

[ALG] **(b)**
- For c = C₃ + C₄ + O(5), the degree-4 graph defect is G₄[C₃] − 2C₄. This was checked for a generic quartic C₄.
- So C₄ = G₄/2 is the unique degree-4 completion. With it, the defect vanishes through degree 5 (κ̃ = 1, 2).
- Odd-degree terms C₅ drop out of G₅.
- Statement scope: a formal completion through degree 5; existence at all orders is not claimed.

[ALG] **(c)**
- The pinned table has 𝒞₄ ≡ 0 for every τ, because deg_τ𝒞₄ ≤ 0.
- The Ŝ-image of every sheet therefore has quartic Φ₄ = G₄ ≠ 0.
- So Ŝ_triad(sheet τ) is not a sheet τ′ for any real τ′.

[ALG] **(d) Relation to the Genesis remainder guard** (Genesis v2.8.6 OPEN 5/2B; GCL-06). For a child law c = κQ_sJ_Qs + O(|s|^p), the phase correction is bounded by O(Q_s^{(p−3)/2}).
- An Ŝ-compatible graph has p = 4 for κ̃ ≠ 0.
- The age-family sheets have p ≥ 5.
- Hence, formally, **Ŝ-compatibility of the birth graph and a fifth-order child remainder are mutually exclusive** for κ̃ ≠ 0.
- [OPEN] Neither branch is a physical birth initialization or post-birth law; the physical branch selection remains open.

Formula/witness:
- `G = S_c(B) - C(S_s(B))`, first nonzero at degree 4;
- `G4[C3+C4] = G4[C3] - 2 C4`;
- `Phi4 = G4 - C4`.

**Domain / admissibility:** Formal; jets through degree 5. Statement (c) uses the κ̃ = 1 table; the κ̃-linearity of G₄ extends (a) and (b) to every κ̃.

**Map / clock:** Ŝ_triad of the primitive-clock record. Contrast: RER-GEN-C07 measures the ℱ-invariance defect of the same graph at degree 5. The two defects are different objects.

**Factor or parametrization tested:** Graph invariance and covariance under the formal involution; not a factor.

**Order / error:** Exact jets through degree 5; no convergence and no remainder constant.

**Contract type:** `GRAPH_INVARIANCE_TEST_UNDER_FORMAL_SYMMETRY_NOT_FACTOR`.

**Evidence:**
- `TRIAD_BGJ_PY` and `TRIAD_GC_PY`: EXECUTED HERE.
- `POLY` re-hashed.
- Triadic reviewer request of 15 Oct satisfied: the jet from degree 2, parent and child.

**Review receipt:** RER editor ACCEPT of the scoping (17 Oct). Mathematics review pending.

Import/reference:
- `TRIAD_BGJ` §§2–4;
- `TRIAD_RCPT` §4;
- `GEN286` §2 OPEN 5/2B and §6.3;
- `POLY`.

[OPEN] All-order existence of the even completion.
[OPEN] Analytic realization.
[OPEN] Which (if any) graph is the physical birth initialization.
[OPEN] Physical p-branch selection.

**Next test:** Extend (b) to degree 7. Check whether the degree-6 even completion is forced and the degree-7 defect vanishes automatically.

**Non-transfer:**
- No physical birth law.
- No reset or healing inference.
- No compulsory memory.
- No selection of the p = 4 branch.
- No automatic RRF registration.

---

## C. r3.1 → r4 change matrix

| r3.1 location | r4 change | Kind |
|---|---|---|
| Header: companions | Genesis v2.8.5 → v2.8.6; RRF v0.8 → v0.8.2 (v0.8 and v0.8.1 kept historical); add Dyadic v6.4.12.1 | pointer |
| Header: status summary | Add the four new records; "sixteen + sixteen" becomes "sixteen + twenty" supplementary contracts; RRF v0.8.2 governs | metadata |
| §1 | One [THM] line: K3 applied to 𝒩 at the primitive clock. One [THM] line: the triad formal involution, primitive clock, −I₄ only. One [ALG] line: birth-graph completion and age-sheet non-permutation. [OPEN] six-step clauses | summary |
| §3 | After the 𝒩 definition, add [ALG] E∘𝒩 = F₁∘E: "the RER modal map is the Genesis projected-K₃ map up to the linear isomorphism E" | model contract |
| §5 G7–G10 | Repin RRF v0.8 → v0.8.2 (§§2.4b, 4.2, 6.2, 8.1). Note that RRF v0.8.2 §8.1 does not import RER F3, formal age, w₁₃ or factors as RRF theorems; no RER change follows | pointer + receipt |
| §6 C05/C06 | Non-transfer line: "distinct from RER-GEN-K3-MODAL (primitive-clock semiconjugacy)" | cross-reference |
| §6 C07 | Cross-reference: "the Ŝ_triad graph defect (degree 4) is a different object; see RER-TRIAD-BIRTH-GRAPH-INVOLUTION" | cross-reference |
| §6 RER-RRF-CND01 | Primitive map cited as DYAD-DEF-PRIMITIVE-MAP (Genesis alias). RRF §6.2 now pins DYAD-THM-LOCAL-INVOLUTION-GERM, DYAD-THM-FORMAL-INVOLUTION-UNIQUE and DYAD-THM-ANALYTIC-CLOCK-BRIDGE | pointer |
| §6 new | The four records of part B | new records |
| §7 | Part A rows; RECOG v0.3.20 retained; GIIL v0.19 noted as the governing Genesis reference, with accessible v0.16 marked as older | source table |
| §8 | Add P1 Triadic consumer sync (part D). Add P2 tasks: G5 six-step factor test; 4D centralizer; degree-7 completion. Stage-2 rows unchanged | queue |
| §9 | r4 entry: source synchronization plus four Triadic-side records. No existing record's grade, formula or exactness changed. The 15 Oct [COR] noted | history |
| Unchanged | C01–C10, FORMAL-AGE, AGE-CURVATURE, REGULAR-3FOLD, ER2B-T6D, ER2B-CARRIER, F3-N7N8; Stage-2 status (global certificate PENDING, TM lemma review OPEN, K=8 stopped at 1/8) | — |

**Open source and evidence gaps**

| Gap | Content | Effect |
|---|---|---|
| G1 | RRF v0.8.2 own file hash and adoption record not inspected | pin by header until supplied |
| G2 | G2 consolidated note v0.4 has no hash | cite as SOURCE-READ noncanonical |
| G3 | GIIL v0.19 bytes not available; v0.16 is older | no GIIL import in r4 |
| G4 | Contributor-workspace files (part A rows marked BYTE-HASHED / EXECUTED HERE) not yet delivered to the RER package | treat as source-reported until delivered; deliver with this file |
| G5 | Planar factors of ℱ = 𝒩⁶ at the six-step clock are not covered by K3 | OPEN |
| G6 | 4D formal centralizer of ℱ (two-dimensional cubic kernel) | OPEN; six-step-only triad uniqueness stays OPEN |
| G7 | ER-2B v0.2 C19–C20 primary source; coincidence certificate | unchanged from r3.1 |
| G8 | Stage-2 global certificate; TM lemma review | unchanged from r3.1 |
| G9 | R_n ≈ √(19/3)(Q₀/Q_n)^{3/2} is a DYAD-side asymptotic [ALG/NUM]; L-SHADOW-POLY is OPEN | not an RER record; reference only |

---

## D. Triadic v1.6 consumer-sync queue (proposals; not applied to the owner file)

Line numbers refer to Triadic v1.6, SHA-256 `c768687c…5b36`.

| # | Triadic location | Current | Proposed | Kind |
|---|---|---|---|---|
| D1 | §7.1, line ~781: `DYAD-ALG-LIEGAUGE-NORM` :: Birkhoff frame and protection matrix | Lie-gauge RID, pin v6.4.8.1 via bridge note | `DYAD-DEF-BRIDGE-EXPORT-CONTRACT` (frame, v⊥) + `DYAD-ALG-PROTECTION-MATRIX`, pin Dyadic v6.4.12.1. The `[conv: Lie strict-kernel gauge]` qualifier is dropped for these items only (Dyadic N2) | RID repin |
| D2 | §7.1: DYAD-THM-C21, DYAD-ALG-BRIDGE-LEMMA | pin v6.4.8.1 | Same RIDs, repinned to v6.4.12.1. Values unchanged; v6.4.11 cross-references RECOG's general bridge-lemma proof | pointer |
| D3 | §7.4 line 806 (and §6 lines 313, 649): Genesis birth theorem "c₀ = κQ_sJ_Qs* + O(\|s*\|⁵)" as unconditional [THM], from v2.8.4 | unconditional fifth-order remainder | **Scientific repin.** Genesis v2.8.5/2.8.6 (GCL-06) makes the O(\|s\|⁵) child remainder conditional on the selected child functional; a raw-residual quartic permits O(\|s\|⁴). Import the leading c₀^{[3]} as [THM] and the remainder as conditional. RER-TRIAD-BIRTH-GRAPH-INVOLUTION (d) is a concrete instance | **scope narrowing** |
| D4 | §7.4 line 804: metric B, "RID unavailable / REQ-T16-METRIC" | owner assignment pending | `GEN-DEF-PRIMITIVE-METRIC`, with `GEN-THM-PRIMITIVE-METRIC-INVARIANCE` for AᵀBA = B (Genesis v2.8.5 §6.1) | RID fill |
| D5 | §7.4 and others: the primitive map T | via Genesis §6.1, RID unavailable | `DYAD-DEF-PRIMITIVE-MAP` (owner), alias `GEN-DEF-PRIMITIVE-MAP` | RID fill |
| D6 | §7.4 other Genesis v2.8.4 imports (Q(V_s), P₄, ΔQ_c, birth symmetry, HINDEX norm) | v2.8.4 sections | Repin to v2.8.6 after value-by-value check. Available RIDs: `GEN-THM-DELTA-QC`, `GEN-ART-G3D-SEED`, `GEN-ART-JQ-PHASEDRIFT`, `GEN-OPEN-HINDEX`; the 9B lowering-bridge caveat (GCL-03) applies to HINDEX uses | pointer + check |
| D7 | §7.1 reference line 797: Genesis v2.8.4 `GEN-OPEN-APEX-SLOT` | reference-only | Mark as `[RETRACTED]` as a [RESULT] in Genesis v2.8.5 (GCL-05/CN-01), RID preserved; keep as history | history |
| D8 | Header companions | OFN v0.8, Dyadic v6.4.10, Genesis v2.8.4, OPEN-M v0.6, RRF v0.6 | OFN v0.9, Dyadic v6.4.12.1, Genesis v2.8.6, OPEN-M v0.7.1, RRF v0.8.2 (convention reference only) | pointer |
| D9 | §7 / CN-01–CN-05 status | "consumer acceptance pending" | Record Genesis v2.8.5's consumption of CN-01/02/03/05 and the CN-04 → OPEN-M routing | receipt |
| D10 | Optional cross-reference | — | `GEN-THM-K3-PLANAR-FACTOR-NOGO` at §6.3a scope; the RRF §3.1 CN-05 convention record (B_T = 2B_G, Q_c^T = (κ²/4)(Q_s^T)³, convention only) | cross-reference |

D3 is the only item that narrows a live Triadic claim's scope. All other items are pointer, RID or receipt hygiene.

---

**Release boundary:**
- No owner DSN, RER, RRF or registry file was edited.
- No pilot or sweep was run.
- The two new scripts (kernel check, E-conjugacy check) are light checks, 90 s and 1 s.
- r3.1 stays unfrozen.
- r4 is a review draft; nothing in it is an adopted RER record by default.
