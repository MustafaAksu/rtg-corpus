# RER r2 review receipt and Stage-2 follow-up

**Date:** 14 October 2026.  
**Status:** Noncanonical receiving review. No RER revision, scientific-owner adoption, RRF registration, new mathematics, Taylor-model box evaluation, or region certificate.

## 1. Requested original note is available

The exact original `STAGE2_RECEIVING_REVIEW.md` is included unchanged under `sources/`.

SHA-256: `c935a4aca063b59099fbc9bf4052b5d50c6a1782ec755b80f5b8594d4876d4e2`.

It has six findings, G1–G6. In particular, G2 is parallel-output/config hashing and G3 is the mismatch between the configured coefficient file/KT and the engine's hardcoded table. Those two findings were not addressed by the newly delivered changes.

Some older attachments have expired in the wider conversation. This original note, the four new files, the current r2 Markdown/JSON and the coefficient table were accessible. No reupload is needed for this follow-up. The updated governing config and completed K8 pilot file were not part of this delivery; the only mounted `stage2_config.json` still selects the old v3 engine.

## 2. RER review acceptance and three bounded amendments

The contribution note, r2 Markdown and machine-registry hashes all match the reported values. Seven Triadic-facing records have `ACCEPT SCOPED`; RER-F3-N7N8 is additionally accepted at its existing source/certificate-limited scope. That is contributor review of the indicated records, not approval of all 32 records or owner adoption. The separate receipt records only what the contributor explicitly supplied.

The following amendments are supported for the next registry revision; they have **not** been applied to the accepted-for-review r2 bytes:

1. **RER-GEN-C09:** write “equal current parent vectors on sheets of unequal fixed finite ages can have different future Qs.” The same-age versus different-age distinction should also appear in the repeated claim summary.
2. **RER-TRIAD-REGULAR-3FOLD:** the age-0/1 proof uses the C07 degree-five drift and continuity of the derivative of a C1 defining function. The same argument extends to **each fixed finite pair n != m using C09's difference expansion**. This is not a uniform-in-age neighborhood and not an abstract-factor impossibility theorem. The original 0/1 statement need not be silently broadened; record the general-pair consequence with its C09 dependency.
3. **RER-ER2B-T6D:** name the exact edge-slot interchange 2↔3 as the source of `F(s,-c)=(F_s(s,c),-F_c(s,c))`. Do not identify it with an already selected physical pole/node exchange.

The withdrawn interpretation of a ratio of upper bounds was already excluded by RER-F3-N7N8. The contributor's withdrawal closes that wording issue, not the analytic or whole-region certificate gate.

## 3. Source identities checked

| Received item | SHA-256 |
|---|---|
| Contributor record review | `d388d7eb0e0855051d0a783383b69254be17f64102e6568fdc37c5d3e907e1ab` |
| Engine v3.1 | `674961ccd19b48653c40f5698668f21d832f1d948a91259eb36d1a639694e17e` |
| Driver v2 | `cb26b2e427e323bbc128f01032c232cfb9c00f3c951379dc01ebc43905a41276` |
| Hardened coverage verifier | `ed19d7139c5a2e96c7a6d526db7692f448398ca1ecfb81fc8f416e3b4b5e1ac5` |

The local upload suffix `(1)` was removed only from the copied filenames in this package; their bytes are unchanged. The source manifest records both paths.

The engine v3→v3.1 source diff changes serialization helpers, the serialization calls and exact tau-plus recording; it does not replace the existing Taylor-model recurrence. No complete revalidation of that recurrence is claimed here.

## 4. New regression findings

The hardened `validate()` now rejects incorrect endpoints, K, source hash, a five-step list, a down-rounded K and a wrong tau-plus interval in the receiving tests. Those are real improvements.

However, **“full contract closed” is not supported by the delivered code yet**.

### G1a — finite/nonnegative and geometric fields remain insufficiently checked

The following mutated fields were accepted by the actual delivered `validate()` definition:

- `K_raw = K_up = -1`;
- `K_raw = K_up = Infinity`;
- `R_eff = 1` while that same record reports `Rmax = 0.142`;
- `rho_s = NaN`;
- one step's `fresh_s = -1`;
- nonnumeric strings inside a length-four `comp_bounds` list.

These are synthetic record-contract tests, not engine output. No claim about false published pilot coefficients follows from them.

The **unchanged full coverage CLI** was also run with an explicitly synthetic, complete small tiling of the stated annulus. All 16 `(box,N)` records had matching hashes/endpoints and six step entries but negative K. It returned exit 0 and printed:

```
CERTIFIED over the whole region: K_7 = -1
CERTIFIED over the whole region: K_8 = -1
```

This is a concrete unsafe-acceptance regression. It is not a mathematical certificate and no such synthetic rows are offered as real results.

Minimum repair: all numeric enclosure fields must be parsed, finite, and nonnegative where they represent norms/radii/bounds. Radius bounds must be checked against the planned geometry, not just `R_eff >= R_floor` and `Rmax > Rmin`. In particular R_eff cannot exceed the verified maximum radius and must be an admissible conservative lower bound of the box/annulus radius. Record rounding checks are separate from proving the underlying computed bounds.

### G1b — duplicates are not fully rejected

The collector compares duplicate rows only through `K_raw`. A duplicate with a different `K_perp_up` but identical K_raw silently overwrites the earlier one. Also, when a different K_raw removes a key, a third repeat can reinstate that key: the complete collector then exits 0 despite having recorded the unresolved conflict.

The receiving harness executes the original collector/report AST unchanged for these tests; it does not substitute new duplicate logic.

Minimum repair: compare a canonical scientific payload, not K_raw alone, and permanently quarantine a conflicting key until an explicit resolution. Identical deterministic duplicates can be deduplicated. Failed attempts and successful retries need a stated separate policy; not every historical failed attempt must poison a later genuine valid result.

### G1c — driver resume still checks only PASS plus three hashes

The driver lines 98–105 have no call to the new coverage validator. Preseeded rows containing only IDs, PASS and matching hashes caused the unchanged driver to skip every job and finish with `done 0 runs this session`. The same rows lack endpoints and step fields and would not pass the coverage contract.

Minimum repair: use one shared contract validator for both resume and aggregation; invalid or conflicting rows must not count as completed jobs.

### G2 — parallel output path still changes or ignores the intended contract

Both scripts still use `HERE / CFG['results']`. The driver does not implement `--results`; supplying it in the receiving test created no requested worker file. Changing the `results` field in config still changes the raw config hash.

Minimum repair: add an operational `--results` override to both scripts without changing the hashed mathematical config, or use a documented canonical semantic-config hash. Use separate per-worker files; do not concurrently append to one file without a defined safe writer.

### G3 — coefficient and KT selection are still not bound to the engine

The driver hashes `CFG['poly']` and reports `CFG['KT']`. Engine v3.1 line 39 still loads its local `age_family_polynomials_kt1.json` unconditionally. Neither layer rejects KT=2. In a receiving test the driver accepted KT=2 and a changed alternative polynomial file; direct module inspection confirmed that the engine still loaded the fixed original table. No box calculation was performed under this deliberately invalid configuration.

Minimum repair for the current study: require KT=1 and the exact intended coefficient file/pin before any resume or evaluation. Alternatively pass the selected table explicitly into the engine and retain the mathematical KT scope check. Merely checking a record against the same incorrect config does not bind the executed source.

### G4 — interpretation corrected

The contributor's withdrawal is accepted: a quotient of two independently calculated upper bounds is not an actual transverse fraction. A one-sided certificate may supply total/transverse upper enclosures without deciding the direction of the true defect.

### G5 — finite endpoint serialization improved; nonfinite values collapse to zero

For 30 tested finite endpoints at matched MP/IV precision 15, 30 and 60 decimal digits, conversion recovered the exact endpoint and the emitted upper/lower strings had the required direction. This is a focused replay, not a proof of every interval lemma or arbitrary mixed-precision context.

A new defect appears for nonfinite inputs. The actual `mpf_to_fraction` uses the mantissa/exponent without rejecting special encodings. Consequently:

```
dec_up(+inf) = dec_up(-inf) = dec_up(nan) = "0"
dec_down(+inf) = dec_down(-inf) = dec_down(nan) = "0"
```

Infinity and NaN have zero mantissas in those internal encodings and are silently converted to Fraction(0). This must be a hard failure before converting any proof endpoint. Otherwise even a later finite-value check in the coverage verifier cannot detect the lost nonfinite state.

### G6 — pilot status remains as stated

The replacement K8 pilot was not supplied and the previous run was reported lost. A later file with the old engine/config hashes can be informational, but cannot be relabelled as a governing-config run. No full-region K, global degree optimum or Taylor-model lemma acceptance follows from its arrival.

## 5. Recommended patch order

1. Reject nonfinite endpoints in the serializer and nonfinite/negative norm values in records.
2. Share plan/config/record validation between resume and aggregation; harden radius and duplicate checks.
3. Implement operational output-path overrides or a semantic config identity; reject unsupported KT/coefficient sources.
4. Deliver the updated governing config and a short resume/merge/tamper regression bundle. No long sweep is needed to test these repairs.
5. Keep Taylor-model lemma review and complete coverage of actual box computations as separate gates.

Even after all record tests pass, `record coverage complete` must not silently mean `independently mathematically certified`. A source hash identifies code; it does not prove its remainder lemmas or authenticate the numerical payload merely because a JSON row repeats the hash.

## 6. Test and update boundary

The receiving harness has **28 expected-behavior regression assertions**. Some pass precisely because they reproduce an unsafe acceptance in the delivered program. They are NOT 28 certificate assertions, a mathematical validator, or a successful whole-region computation.

The tests used synthetic records and a deliberately small valid tiling to exercise the unchanged full coverage CLI. Focused tests used the unmodified function/collector ASTs. Driver tests ran the supplied program with preseeded records, never calling `certify_box`. Logs identify all these scopes.

The RER r2 scientific review can be recorded as supplied `ACCEPT SCOPED` for the eight named records, with wording amendments pending. The Stage-2 current-use entry should record the new implementation and this remaining-gate review; it should not close its global-certification task. No reviewed r2, original source, historical note, owner document or physical selection is changed here.
