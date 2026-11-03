#!/usr/bin/env python3
"""Genesis v2.10, content stage: the inbox round after v2.9 (one stage; no compaction). Output is a candidate, not an edition.

Scope: the fixed co-owner list `records/gen/GEN_OWNER_RECONCILIATION_INBOX_20261103.md` (ChatGPT co-owner acceptance,
PR #161 comment 6602196670). PI decision, 3 Nov 2026, verbatim: "Sürüm 2.10 uygun, kapsam böyle uygun, RID'lein adları
uygun" (edition v2.10; that list as scope; RIDs GEN-ALG-P4-DRIFT-IDENTITY and GEN-ALG-BIRTH-SYMMETRY-SEED).

Rules:
- input must be the adopted v2.9 bytes (tag gen-v2.9, SHA-256 9178ca2c…00ac);
- every edit is assertion-gated: mode "str" = exact substring occurring exactly once; mode "line" = one whole line occurring
  exactly once; each edit is logged with old/new text and hashes;
- §6.3a–§6.3c are not touched; Appendix A gets one new entry above v2.9; Appendix B gets one new corrected-claim entry
  (the G8 grade correction); the header carries the candidate status (the publication transform sets the adopted lines).

usage: build_gen_v2_10.py BASE OUT EDITLOG_JSON      BASE = `git show gen-v2.9:dsn/RTG_GENESIS_GEOMETRY_DSN.md`
"""
import hashlib, json, sys

BASE_SHA = "9178ca2cd38bea8d55deada78b6adbd8022533c4baad7af101583b1179d300ac"
REL = "`records/gen/GEN_v2_10_RELEASE_RECORD.md`"
NEW_RIDS = ["GEN-ALG-P4-DRIFT-IDENTITY", "GEN-ALG-BIRTH-SYMMETRY-SEED"]
INB = "`[indep-INB]`"

E = []
def ed(key, item, mode, old, new): E.append((key, item, mode, old, new))

# ---------------- header (candidate status) ----------------
ed("H1", "header", "line", "# RTG_GENESIS_GEOMETRY_DSN_v2.9", "# RTG_GENESIS_GEOMETRY_DSN_v2.10")
ed("H2", "header", "line", "**Date:** 25 October 2026  ", "**Date:** 3 November 2026  ")
ed("H3", "header", "line",
   "**Document status:** ADOPTED — PI, 25 October 2026 (corrections of the reconciled v2.8.9 advisory and Methodology v1.4 compaction; stage 1 and stage 2 reviewed). Adoption record: `records/gen/GEN_v2_9_RELEASE_RECORD.md`.  ",
   f"**Document status:** CANDIDATE — not adopted (inbox round after v2.9: G1–G8 and producer/consumer pins; one content stage). Release record: {REL}.  ")
ed("H4", "header", "line",
   "**Supersedes:** `RTG_GENESIS_GEOMETRY_DSN_v2.8.9` (SHA-256 `d143673e9596abc900f54f269582299c87c9146504d6c9e1fd08ac294ba8c6fc`; tag `gen-v2.8.9`).  ",
   f"**Supersedes:** `RTG_GENESIS_GEOMETRY_DSN_v2.9` (SHA-256 `{BASE_SHA}`; tag `gen-v2.9`).  ")
ed("H5", "header", "str", "**Release record:** `records/gen/GEN_v2_9_RELEASE_RECORD.md`. Version history: Appendix A.",
   f"**Release record:** {REL}. Version history: Appendix A.")

# ---------------- G1: independent route to G2 = 0 ----------------
ed("G1a", "G1", "str",
   "All one-step quadratic forcing cancels over one 6-step block.\n",
   "All one-step quadratic forcing cancels over one 6-step block.\n\n"
   r"`[ALG]` **Independent route (application of `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE`, §7).** For $L=\operatorname{diag}(A,A,A)$ with $A=DT(0)$, "
   r"$A^6=I$, the first nonlinear degree is quadratic and the degree-2 vector charges $a-b-1\in\{1,-1,-3\}$ are nonzero mod 6, so the resonant projection "
   r"of $F_2$ vanishes and $G_2=0$; this holds for every quadratic $F_2:\mathbb R^6\to\mathbb R^6$, cross-component terms included. Exact check: "
   + INB + " gate G1. This is a new proof of the §6.4 statement, not a recovery of its original source (`GEN-ART-G2-CHRONO`, `[custody-A]`).\n")
ed("G1b", "G1", "str",
   "a possible independent route via `RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` is noted in the owner disposition record and is not used here",
   "independent route: `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` (§7) with the §6.4 `[ALG]` application, " + INB + " gate G1 (a new proof, not a recovery); "
   "`RECOG-ALG-LEADING-RETURN-EQUIVARIANCE` is a second route, noted only")
ed("G1c", "G1", "str",
   "### From `RTG_DISCRETE_GENESIS_DSN_v2.12.13`",
   "### From `RTG_NUMBER_GENESIS_DSN_v1.21`\n\n"
   "Claim-level import for the §6.4 independent route only (`numgen-v1.21`).\n\n"
   r"- [RID: NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE] :: `[RESULT][from: ALG]` first-nonlinear cyclic-average theorem: if $f=R+h_d+O(d+1)$, then "
   r"$[f^p-\mathrm{id}]_d=pR^{-1}\Pi_0h_d$ (NUMGEN §6.4) :: §6.4 independent route to $G_2=0$; the diag(A,A,A) application is the Genesis `[ALG]` line there" "\n\n"
   "### From `RTG_DISCRETE_GENESIS_DSN_v2.12.14`")

# ---------------- G3/G4: OFN companion; TDR-G navigation pointer; pins ----------------
ed("G3a", "G3/G4", "str",
   "- `RTG_ONTOLOGICAL_FOUNDATIONS` v0.10 (`ofn-v0.10`) — foundational context;",
   "- `RTG_ONTOLOGICAL_FOUNDATIONS` v0.12 (`ofn-v0.12`) — foundational context;")
ed("G3b", "G3/G4", "str", "OFN §5.5 and IMP-O10-01 import §6.3a–§6.3c (Programme IF32);",
   "OFN §5.5 and its §11 import rows take §6.3a–§6.3c (Programme IF32); OFN v0.11 amended two OFN contract fields (OFN11-C01, OFN11-C02) that Genesis does not use;")
ed("G3c", "G3/G4", "line", "- OFN (IF32) :: OFN §11 rows IMP-O10-*, §5.5 :: §6.3a–§6.3c",
   "- OFN (IF32) :: OFN §11 import rows and §5.5, at OFN v0.12 :: §6.3a–§6.3c")
ed("P1", "pins", "line", "- Programme v1.3 and OFN v0.10: companion references above, not scientific imports.",
   "- NUMGEN: v1.21 (`numgen-v1.21`) for the §6.4 route row only.\n- Programme v1.3 and OFN v0.12: companion references above, not scientific imports.")
ed("P2", "pins", "line", "- Discrete Genesis: v2.12.13, blocked interface (Programme IF25); no import.",
   "- Discrete Genesis: v2.12.14 (`tdrg-v2.12.14`), blocked interface (Programme IF25); no import.")

# ---------------- G5: DYAD-ALG-NU5-P5 label and claim-level pin ----------------
ed("G5a", "G5", "str",
   r"- [RID: DYAD-ALG-NU5-P5] :: $\nu_5^{(5)}$ closed form, exact over $\mathbb{Q}(\sqrt5,\sqrt{10+2\sqrt5})$ `[conv: one-step NF, declared K_5 family, frame W_p, resonant h=0]` (exact certificate `dyad_m2c_nu5_p5_exact.py`, Dyadic owner; v2.8.8) :: §6.2 OPEN 9 imports",
   r"- [RID: DYAD-ALG-NU5-P5] :: $\nu_5^{(5)}$ closed form, exact in $\mathbb{Q}(\zeta_5)$, $\zeta_5=e^{2\pi i/5}$, with real and imaginary parts in $\mathbb{Q}(\sqrt5,\sqrt{10+2\sqrt5})$ `[conv: one-step NF, declared K_5 family, frame W_p, resonant h=0]` (exact certificate `dyad_m2c_nu5_p5_exact.py`, Dyadic owner; claim-level pin `dyad-v6.4.23` §6.11, where the field label is corrected; value unchanged) :: §6.2 OPEN 9 imports")
ed("P3", "pins", "line",
   "- Dyadic: v6.4.13 for the historical rows above (proof pins); v6.4.22 (`dyad-v6.4.22`) for the two §6.3c (C2) rows only.",
   "- Dyadic: v6.4.13 for the historical rows above (proof pins), except `DYAD-ALG-NU5-P5` at v6.4.23 (`dyad-v6.4.23`, field label); v6.4.22 (`dyad-v6.4.22`) for the two §6.3c (C2) rows only.")

# ---------------- G6: Triadic v1.7, import grade (a) T-6s/T-6t, (b) T-6u ----------------
ed("G6a", "G6", "str",
   "`[CAND]` `[import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6 §6.15 | TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY]` **In-plane coherent-source identity (Triadic v1.6 scope).**",
   "`[ALG]` `[import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 §6.15 | TRIAD-ALG-T6S-COHERENT-CONJUGATE-FAMILY]` **In-plane coherent-source identity (Triadic v1.7 scope).**")
ed("G6b", "G6", "str",
   "`[CAND]` `[import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6 §6.16 | TRIAD-ALG-T6T-JACOBI-MODE-SIGNS]` **Mode-sign count, not physical source-direction independence.** Adopted Triadic v1.6 retains",
   "`[ALG]` `[import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 §6.16 | TRIAD-ALG-T6T-JACOBI-MODE-SIGNS]` **Mode-sign count, not physical source-direction independence.** Adopted Triadic v1.7 retains")
ed("G6c", "G6", "line",
   "**[CAND]** `[scope: primitive seed diagnostic]` [RID: GEN-CAND-APEX-T6U] [import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6 §6.17 | TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC]",
   "`[ALG]` `[import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 §6.17 | TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC]` Triadic's primitive apex seed diagnostics, restricted to the "
   "parent-seed and increment-channel values used below. Depends on: Triadic §6.17 at v1.7; see §7.\n\n"
   "**[CAND]** `[scope: primitive seed diagnostic]` [RID: GEN-CAND-APEX-T6U] Genesis interface reading of the import above:")
ed("G6d", "G6", "str", "and not a bound on an independent UV source. Triadic v1.6 separately types",
   "and not a bound on an independent UV source. Triadic v1.7 separately types")
ed("G6e", "G6", "line", "### From `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6`", "### From `RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7`")
ed("G6f", "G6", "str", "Consumer reconciliation against adopted v1.6 is applied in this release.",
   "The three imports are pinned claim by claim at v1.7 (`triad-v1.7`; statements, values and grades unchanged since v1.6, Triadic §7). The CN-01–CN-05 rows below are the v1.6 consumer notices as received.")
ed("G6g", "G6", "line",
   "- Triadic: v1.6 for the imports above; the §6.17 table is read at `triad-v1.6.1` for the T-6u case label (§8), a companion reading.",
   "- Triadic: v1.7 (`triad-v1.7`) for the three imports above, claim by claim; CN-01–CN-05 as received at v1.6; the §6.17 table is read at `triad-v1.6.1` for the T-6u case label (§8), a companion reading.")
ed("G6h", "G6", "str", "- **OPEN 1T — Triadic v1.6 phase/interface import protocol.** CLOSED (v2.8.5):",
   "- **OPEN 1T — Triadic phase/interface import protocol.** CLOSED (v2.8.5):")
ed("G6i", "G6", "str", "retained imports are limited to adopted, explicitly scoped Triadic v1.6 statements;",
   "retained imports are limited to adopted, explicitly scoped Triadic statements at the pinned edition (§7);")
ed("G6j", "G6", "line", "**OPEN 1T — Triadic v1.6 phase/interface import protocol** [RID: GEN-OPEN-TRIAD-PHASE-IMPORT]",
   "**OPEN 1T — Triadic phase/interface import protocol** [RID: GEN-OPEN-TRIAD-PHASE-IMPORT]")
ed("G6k", "G6", "line", "- TRIAD (IF06) :: Triadic §7, pin v2.8.7 :: primitive tetrahedral seed and metric conventions",
   "- TRIAD (IF06) :: Triadic §7.2: `gen-v2.9` claim by claim; the radial-polynomial import held at v2.8.7 pending the d-mode identity (`GEN-ALG-P4-DRIFT-IDENTITY`, §6.5) :: primitive tetrahedral seed and metric conventions")

ed("G6l", "G6", "str",
   "`[CAND]` `[scope: primitive seed comparison]` — [import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.6 §6.17 | TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC]",
   "`[CAND]` `[scope: primitive seed comparison]` (Genesis reading; the import line beneath it in §2 carries `[ALG]`) — [import: RTG_TRIADIC_BIRTH_LIFT_DSN_v1.7 §6.17 | TRIAD-ALG-T6U-APEX-SEED-DIAGNOSTIC]")

# ---------------- G7: the d-mode quartic identity ----------------
ed("G7a", "G7", "str",
   "`[THM]` Vanishing channels: $d^2s$, $d^2c$, $scd$ — by direct incidence cancellation and quadratic route sparsity.\n",
   "`[THM]` Vanishing channels: $d^2s$, $d^2c$, $scd$ — by direct incidence cancellation and quadratic route sparsity.\n\n"
   r"`[ALG]` [RID: GEN-ALG-P4-DRIFT-IDENTITY] **Quartic drift identity (d-mode).** For the six-step block map $Z\mapsto L^6Z+G_2(Z)+G_3(Z)+O(\|Z\|^4)$ of §6.4 "
   r"and $Q_d=d^\top Bd$, with $d'$ the $d$-component of the image, "
   r"$Q_d(d')-Q_d(d)=2d^\top B\,G_{2,d}(Z)+\bigl[2d^\top B\,G_{3,d}(Z)+Q_d(G_{2,d}(Z))\bigr]+O(\|Z\|^5)$, the cubic term first and the quartic bracket second. "
   r"With $L^6=I$ (`GEN-THM-LIN-ORDER6`) and $G_2=0$ (§6.4) the cubic term and $Q_d(G_{2,d})$ vanish, so" "\n"
   r"$$\mathcal P_4(s,c,d)=\Delta Q_d^{(4)}=2d^\top B\,G_{3,d}(s,c,d),\qquad G_{3,d}(s,c,0)=\tfrac12B^{-1}\nabla_d\mathcal P_4\big|_{d=0}.$$" "\n"
   r"Through this identity the printed $\Delta Q_d^{(4)}$ above reproduces the printed seed values $Q_{d,1}^{[s^3]}=\tfrac{7}{1024}Q_s^3$ and "
   r"$Q_{d,1}^{[c^3]}=\tfrac{61}{34992}Q_c^3$ below (exact: " + INB + r" gates G7a, G7b). Depends on: `GEN-THM-LIN-ORDER6`; §6.4 $G_2=0$ "
   r"(original source `GEN-ART-G2-CHRONO`, `[custody-A]`; independent route in §6.4); $Q_u=u^\top Bu$. It is the $d$-mode analogue of `GEN-THM-DELTA-QC` "
   r"and distinct from it. Not supplied: an independent certificate of the $\Delta Q_d^{(4)}$ coefficients (`GEN-ART-P4-PRIMITIVE`, `[custody-A]`)." "\n")

# ---------------- G8: birth symmetry [ALG] with RID ----------------
ed("G8a", "G8", "str",
   "`[THM]` **Birth-symmetry (corrected v2.2).** For the certified $s^3$-seeded apex at $d_0=0$:",
   "`[ALG]` [RID: GEN-ALG-BIRTH-SYMMETRY-SEED] **Birth-symmetry (corrected v2.2).** Exact evaluation, for the certified $s^3$-seeded apex at $d_0=0$:")
ed("G8b", "G8", "str", "corrected $J_Q$, birth-symmetry sign, and phase-drift law promoted to `[ALG]`;",
   "corrected $J_Q$, birth-symmetry sign (`GEN-ALG-BIRTH-SYMMETRY-SEED`, §6.6), and phase-drift law promoted to `[ALG]`;")
ed("G8c", "G8", "line", "- Corrected $J_Q$, birth-symmetry sign, phase-drift law: `[ALG]` (§6.6).",
   "- Corrected $J_Q$, birth-symmetry sign (`GEN-ALG-BIRTH-SYMMETRY-SEED`), phase-drift law: `[ALG]` (§6.6).")
ed("G8d", "G8", "str",
   r"- [RID: GEN-ART-JQ-PHASEDRIFT] :: corrected $J_Q$, birth-symmetry, and phase-drift law $\Delta\phi_{ds}$ :: `[ALG]` — symbolic; sign flip at $Q_s^*\approx0.603$",
   r"- [RID: GEN-ART-JQ-PHASEDRIFT] :: corrected $J_Q$, birth-symmetry, and phase-drift law $\Delta\phi_{ds}$ :: `[ALG]` (artifact typing; supports `GEN-ALG-BIRTH-SYMMETRY-SEED`, §6.6) — symbolic; sign flip at $Q_s^*\approx0.603$")

# ---------------- §8: standard clause and rows for the new RIDs ----------------
ed("S8a", "evidence", "str",
   "exact sympy gates K1–K4 and S1–S3 (S4 is numerical and supports no live text) — `EV-CODE`, `EV-RUN`, `EV-INDEP`.\n",
   "exact sympy gates K1–K4 and S1–S3 (S4 is numerical and supports no live text) — `EV-CODE`, `EV-RUN`, `EV-INDEP`.\n"
   "- " + INB + " :: independent contribution, not a rerun of missing original code and not a recovery of the original source (Methodology §12.3): "
   "`evidence/gen/scripts/gen_inbox_checks.py` (`4b9f0a3c…5415`), exact sympy gates T0, CONV, G1, G7a, G7b, G8 on the printed Genesis data — `EV-CODE`, `EV-RUN`, `EV-INDEP`.\n")
ed("S8b", "G7/G8", "str",
   "\n\n---\n\n## §9. Collaboration and Provenance",
   "\n- [RID: GEN-ALG-P4-DRIFT-IDENTITY] :: d-mode quartic drift identity $\\mathcal P_4=2d^\\top BG_{3,d}$ :: `[ALG]` `[scope: §6.5; §6.4 premises]` — proof: §6.5 (expansion), "
   + INB + " gates G7a, G7b"
   "\n- [RID: GEN-ALG-BIRTH-SYMMETRY-SEED] :: birth-symmetry values at the certified $s^3$ seed :: `[ALG]` `[scope: §6.6]` — exact evaluation; seed `GEN-ART-G3D-SEED`; "
   "also from the printed $\\mathcal P_4$ through `GEN-ALG-P4-DRIFT-IDENTITY`, " + INB + " gate G8"
   "\n\n---\n\n## §9. Collaboration and Provenance")

APPA_START = "## Appendix A — Version History {#appendix-a}\n\n"
APPA_ANCHOR = "### v2.9 — 25 October 2026 — Adopted\n"
APPA_ENTRY = (
 "### v2.10 — 3 November 2026 — candidate (not adopted)\n\n"
 "- **Basis:** the Genesis inbox after v2.9 (eight `pipes/GEN/` items), the Atlas advisory `records/gen/ATLAS_ADVISORY_GEN_INBOX_20261103.md`, the two owner "
 "disposition records and the fixed co-owner list `records/gen/GEN_OWNER_RECONCILIATION_INBOX_20261103.md`; PI decision of 3 November 2026.\n"
 "- **New RIDs:** `GEN-ALG-P4-DRIFT-IDENTITY` (§6.5, the d-mode identity $\\mathcal P_4=2d^\\top BG_{3,d}$ under the §6.4 premises; G7); "
 "`GEN-ALG-BIRTH-SYMMETRY-SEED` (§6.6; G8).\n"
 "- **Grade correction:** §6.6 birth symmetry `[THM]` → `[ALG]`, values unchanged (Appendix B; G8).\n"
 "- **Independent route:** §6.4 $G_2=0$ via `NUMGEN-RESULT-N3CP-CYCLIC-AVERAGE` and a Genesis `[ALG]` application line; `GEN-ART-G2-CHRONO` stays `[custody-A]` (G1).\n"
 "- **Imports and pins:** NUMGEN v1.21 route row (G1, G2); Triadic imports repinned claim by claim to v1.7, T-6s/T-6t as `[ALG]` imports, T-6u as an `[ALG]` import "
 "with the separate Genesis `[CAND]` reading `GEN-CAND-APEX-T6U` (G6); `DYAD-ALG-NU5-P5` field label corrected and that row repinned to v6.4.23 (G5); "
 "OFN companion and IF32 row at v0.12 (G3, G4); Discrete Genesis blocked-interface pointer at v2.12.14; TRIAD consumer row at its declared state.\n"
 "- **Unchanged:** §6.3a–§6.3c; every other RID's statement and grade; every OPEN status.\n"
 f"- **Records:** release record {REL}; predecessor tag `gen-v2.9` (SHA-256 `9178ca2c…00ac`).\n\n")
APPB_START = "## Appendix B — Retired and Rejected Claims {#appendix-b}\n\n"
APPB_ENTRY = (
 "### Corrected claims (inbox round after v2.9)\n\n"
 "**[RETRACTED | RID: GEN-ALG-BIRTH-SYMMETRY-SEED]** Grade `[THM]` of the §6.6 birth-symmetry statement (v2.2–v2.9). Reason: the values "
 "$I_{ds}^{(1)}=\\omega_{ds}^{(1)}=-Q_s^2/16$, $\\phi_{ds}^{(1)}$ and $D_{\\rm birth}^{[s^3]}=\\tfrac{7}{512}Q_s^3$ are an exact evaluation at the certified $s^3$ seed, whose "
 "artifact `GEN-ART-G3D-SEED` is `[ALG verified]`; §1, §2 and §8 already graded it `[ALG]`. Corrected grade `[ALG]`, values unchanged. Record: Appendix A, v2.10 entry; "
 "co-owner list item G8.\n\n")

def sha(s): return hashlib.sha256(s.encode()).hexdigest()

def apply(text, key, mode, old, new):
    if mode == "str":
        n = text.count(old); assert n == 1, f"{key}: expected 1 match, found {n}"
        return text.replace(old, new)
    ls = text.split("\n"); idx = [i for i, l in enumerate(ls) if l == old]
    assert len(idx) == 1, f"{key}: expected 1 whole-line match, found {len(idx)}"
    ls[idx[0]] = new; return "\n".join(ls)

def build(base):
    assert sha(base) == BASE_SHA, "base is not adopted v2.9 (tag gen-v2.9)"
    keys = [e[0] for e in E]; assert len(keys) == len(set(keys))
    t, log = base, []
    for k, item, mode, old, new in E:
        assert old != new, k
        t = apply(t, k, mode, old, new)
        log.append({"key": k, "item": item, "mode": mode, "old": old, "new": new, "old_sha256": sha(old), "new_sha256": sha(new)})
    for k, a, ins in (("APPA", APPA_ANCHOR, APPA_ENTRY + APPA_ANCHOR), ("APPB", APPB_START, APPB_START + APPB_ENTRY)):
        assert t.count(a) == 1, k
        t = t.replace(a, ins)
        log.append({"key": k, "item": "appendix", "mode": "insert", "old": a, "new": ins, "old_sha256": sha(a), "new_sha256": sha(ins)})
    ft = "*END OF DOCUMENT — RTG_GENESIS_GEOMETRY_DSN_v2.9 (ADOPTED, 25 October 2026).*"
    fn = "*END OF DOCUMENT — RTG_GENESIS_GEOMETRY_DSN_v2.10 (candidate; not adopted).*"
    t = apply(t, "F1", "line", ft, fn)
    log.append({"key": "F1", "item": "footer", "mode": "line", "old": ft, "new": fn, "old_sha256": sha(ft), "new_sha256": sha(fn)})
    return t, log

def main(argv):
    base_p, out_p, log_p = argv[1:4]
    raw = open(base_p, "rb").read(); t, log = build(raw.decode("utf-8"))
    data = t.encode("utf-8"); open(out_p, "wb").write(data)
    json.dump({"base_sha256": BASE_SHA, "base_tag": "gen-v2.9", "candidate_sha256": hashlib.sha256(data).hexdigest(),
               "declared_new_gen_rids": NEW_RIDS, "edit_count": len(log), "edits": log},
              open(log_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(log), "edits")

if __name__ == "__main__":
    main(sys.argv)
