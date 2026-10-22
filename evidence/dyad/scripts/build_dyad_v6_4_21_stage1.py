#!/usr/bin/env python3
"""DYAD v6.4.21, stage 1: corrected intermediate.

Applies the accepted closeout corrections (records/dyad/ATLAS_CLOSEOUT_DYAD_v6_4_20.md
§2: S-1..S-5, FC-34) to the adopted v6.4.20 file. Every edit is assertion-gated:
the old text must occur exactly once. No layout compaction happens here (stage 2).

usage: build_dyad_v6_4_21_stage1.py BASE OUT EDITLOG_JSON
"""
import hashlib, json, sys

BASE_SHA = "0b2d5a44eb818598bb330464dfa4f2e9d75521715f577a7c2e589e165f1a4852"

EDITS = [
# ---- S-1 current status at every point of use ----
("S-1a", "§1 OPEN 13 entry (R11 wording)",
 r"$c_\theta^{(6)}$ is retained under its own convention and is not transferred to the conjugacy chart pending RECOG R11 (SG-19).",
 r"$c_\theta^{(6)}$ is retained under its own convention and is not transferred to the conjugacy chart (SG-19; permanent non-transfer guard). The chart quintic phase coefficient is $+\tfrac{89\sqrt3}{324}$ (RECOG-ALG-CHART-LAWS); RECOG R11 is CLOSED (RECOG v0.3.2)."),
("S-1b", "§1 Lemma F entry (existence pointer)",
 r"Consequences for *existing* $C^\infty$ objects: $C^\infty$ clock bridge, $C^\infty$ uniqueness, smooth roots commute with $T$ (F1–F3). No existence is asserted.",
 r"Consequences for *existing* $C^\infty$ objects: $C^\infty$ clock bridge, $C^\infty$ uniqueness, smooth roots commute with $T$ (F1–F3). F1–F3 assert no existence; existence is DYAD-THM-SMOOTH-EMBEDDING (§6.17)."),
("S-1c", "§1 OPEN 3 per-block entry (status)",
 r"(`DYAD-THM-OPEN3-SPIRAL-REM`, §6.14). OPEN 3 is PARTIAL: asymptotic-phase transfer (P4) OPEN.",
 r"(`DYAD-THM-OPEN3-SPIRAL-REM`, §6.14). OPEN 3 is CLOSED within its defined scope (v6.4.16); P4 is `DYAD-THM-OPEN3-ASYMPTOTIC-PHASE` (`[assuming: RECOG-THM-R9-MEMORY]`); the primitive-variable remainder is OPEN 21 (CLOSED, v6.4.17)."),
("S-1d", "§2 OPEN 3b sub-item (remainder pointer)",
 r"proved as separate results (`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`, §6.14). Primitive-variable remainder beyond formal second order not certified.",
 r"proved as separate results (`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`, §6.14). The primitive-variable remainder beyond formal second order is certified by `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (OPEN 21; R9 premise; rows A/B unchanged)."),
("S-1e1", "§2 OPEN 9 active list: remove closed Q403 item",
 "- Exact cubic cascade formula for $q=4,(0,3)$: **CLOSED (v6.4.9)** `[THM]` `[proof: exact algebraic identity]` — all-$p$ closed form, $Q_p=i\\zeta_p^3 M_p$, $M_p\\in\\mathbb{Q}(\\zeta_p)^+$ (DYAD-THM-Q403-PHASELAW)\n",
 ""),
("S-1e2", "§2 OPEN 9 active list: remove closed b=5 item",
 None, ""),  # filled below (long text)
("S-1e3", "§2 OPEN 9 closed list: add Q403 and b=5 items",
 "imported, owner RECOG [RID: RECOG-ALG-NU3-CLOSED-FORM, RECOG-ALG-NU3-NONVANISHING] (v6.4.11)\n",
 None),  # filled below
("S-1e4", "§2 OPEN 9: drop struck 'Next required artifacts' line",
 "- ~~Exact cubic cascade computation for $q=4,(0,3)$ via `rtg_p_certs.py`~~ **DONE v6.4.9** (DYAD-THM-Q403-PHASELAW; certificate `q4_03_R_identity_certificate.py`)\n",
 ""),
("S-1f", "§2 closed list, OPEN 19 line (tangent to identity)",
 r"formal centralizer of $T^6$ is $\{\exp(sX)\}$; unique formal involution",
 r"formal tangent-to-identity centralizer ($DG(0)=I$) of $T^6$ is $\{\exp(sX)\}$; unique formal involution"),
("S-1g", "§5 spiral-residual row (P4)",
 r"identifying $S_Q$ with $P_5$ (cross term $-2qD_3$); primitive asymptotic-phase transfer (P4); equivalence",
 r"identifying $S_Q$ with $P_5$ (cross term $-2qD_3$); the primitive asymptotic-phase transfer (P4) as implied by the per-block result alone (P4 is DYAD-THM-OPEN3-ASYMPTOTIC-PHASE); equivalence"),
("S-1h", "§6.14 recorded distinctions (iii): P2B v2 provenance",
 r"This does **not** replace the byte-level comparison with the adopted P2B v2 `certificate.json` (`jets.h_degree6`, `jets.J_through6`), which remains an open provenance item.",
 r"Coefficient verification against the adopted P2B v2 `certificate.json` (`jets.h_degree6`, `jets.J_through6`) is complete: the v6.4.16 record shows the reproduced $h$, $J$ coefficients equal the certificate coefficients in exact arithmetic. This is coefficient equality, not byte identity of files; no byte-identity check is claimed."),
("S-1i", "§6.14 OPEN 3 primitive-variable form (remainder pointer)",
 r"The $O(Q_0^{3/2})$ remainder in primitive variables is **not** certified (it needs a second-order bound on $h^{-1}-(\mathrm{id}-h_2)$); this part is not a `[THM]`.",
 r"This expansion is formal at second order and is not itself a `[THM]`; its $O(Q_0^{3/2})$ remainder in primitive variables is certified separately by `DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER` (OPEN 21, `[assuming: RECOG-THM-R9-MEMORY]`)."),
("S-1l", "§6.14 OPEN 3 primitive-variable form (scope tag)",
 r"`[ALG]` `[scope: formal second order; remainder not certified]` **Primitive-variable form.**",
 r"`[ALG]` `[scope: formal second order; remainder certified separately, OPEN 21]` **Primitive-variable form.**"),
("S-1j", "§6.14 OPEN 3b recorded distinctions (ii)",
 r"(ii) The primitive-variable expansion is formal at second order; only the chart-variable law is certified.",
 r"(ii) The primitive-variable expansion of DYAD-ALG-OPEN3-PHASE-OFFSET is formal at second order; its remainder is certified by DYAD-THM-OPEN21-PRIMITIVE-PHASE-REMAINDER (OPEN 21), and the chart-variable law by DYAD-THM-OPEN3-ASYMPTOTIC-PHASE."),
("S-1k", "§8 DYAD-ART-ATLAS-P2 (evidence attribution)",
 r"r1 package replayed by the external reviewer (21 Oct 2026), r2 OWNER-RUN",
 r"r1 and r2 packages replayed by the external reviewer (21 Oct 2026; r2: G0–G21, the r2 negative controls, M1–M11, S1–S4 with C1–C2, R1–R4 with D1–D2), as recorded at adoption"),
# ---- S-6a field label (owner script recovered 22 Oct 2026; exact recomputation) ----
("S-6a", "§1 OPEN 13 entry (h4 coefficient field)",
 r"Archival Lie-gauge 6-step object: $h_4$ exact over $\mathbb{Q}(\sqrt{3})$,",
 r"Archival Lie-gauge 6-step object: $h_4$ exact with coefficients in $\mathbb{Q}(i\sqrt3)$ (real parts in $\mathbb Q$, imaginary parts in $\mathbb Q\sqrt3$; exact recomputation `dyad_h4_archival_exact_check.py`, v6.4.21),"),
("S-6a-reg", "§8 DYAD-ART-NORM-P6 (source pin)",
 r"- [RID: DYAD-ART-NORM-P6] :: `normalize_p6_liegauge_exact.py` :: Archival",
 r"- [RID: DYAD-ART-NORM-P6] :: `normalize_p6_liegauge_exact.py` (SHA-256 `cec918f808cbc02c53beba5f88faf1edbed830a87dac7283e6ac2511d2ec5835`, `evidence/dyad/scripts/`; its $h_4$ closed forms are confirmed exactly by `dyad_h4_archival_exact_check.py`) :: Archival"),
# ---- review R21-01: R11 wording ----
("R11-a", "§1 backbone entry (R11 label)",
 r"and its identification with $\mathcal A_{\rm raw}$ or with any final-chart quantity is `[OPEN]` (R11).",
 r"and its identification with $\mathcal A_{\rm raw}$ or with any final-chart quantity remains `[OPEN]` as a fitted-backbone identification problem. RECOG R11 is CLOSED at its final-chart ledger scope; the SG-19 non-transfer guard remains."),
("R11-b", "§6.5 OPEN entry (R11 sentence)",
 r"This revision does not transfer those claims through $h$ or close RECOG R11.",
 r"This ledger does not transfer those claims through $h$. RECOG R11 is CLOSED at its final-chart ledger scope; that closure does not identify the historical fitted backbone with the exact dynamics or transfer it through $h$."),
("R11-c", "§6.5 historical fit (qualification label)",
 r"remains `[OPEN]` under the §6.5/R11 qualification.",
 r"remains `[OPEN]` under the §6.5 and SG-19 non-transfer qualifications."),
# ---- S-2 N11 adopted use ----
("S-2", "§7 notices: N11→RECOG row",
 "| N11 | v6.4.15 | RECOG | OPEN 3b offset and memory | RECEIVED — reference import (SG-R14) | RECOG v0.3.22 §7.2 |",
 "| N11 | v6.4.15 | RECOG | OPEN 3b offset and memory | ADOPTED USE — `RECOG-THM-A1A-CD-IDENTIFICATION` depends on T1/T2 (`DYAD-THM-OPEN3-ASYMPTOTIC-PHASE`) at RECOG's pin; the earlier v0.3.21 reference import (SG-R14) is in the v6.4.20 notice table | RECOG v0.3.22 §6.13b; §7.2 mirror to be reconciled by RECOG |"),
# ---- S-3 subclaim dependencies in §7 ----
("S-3", "§7 dependency structure (self-contained part of PHASE-OFFSET)",
 r"the OPEN 3 per-block and offset results (DYAD-ALG-OPEN3-LEADING, DYAD-THM-OPEN3-SPIRAL-REM, DYAD-ALG-OPEN3-PHASE-OFFSET, DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS), DYAD-THM-LPHASE-ROWA-REMAINDER, the six-step module and the OPEN 9 arithmetic ledger.",
 r"the OPEN 3 per-block and offset results (DYAD-ALG-OPEN3-LEADING, DYAD-THM-OPEN3-SPIRAL-REM, DYAD-THM-OPEN3-PHASE-OFFSET-BOUNDS, and of DYAD-ALG-OPEN3-PHASE-OFFSET the static-offset identity and $\Delta_1,\Delta_2$; its primitive-memory expansion uses the R9 memory law, $c_{\rm iso}$ and $\Lambda_1$), DYAD-THM-LPHASE-ROWA-REMAINDER, the six-step module and the native OPEN 9 derivations, excluding the named RECOG imports."),
# ---- S-4 notation table ----
("S-4a", "Appendix C: J row (J_Q correction)",
 r"| see column | read by section; $J_Q$ is Genesis/Triadic notation, not used here |",
 r"| see column | read by section; $J_Q=\mathcal L^{-1}i\mathcal L$ is the rotation defined and used in §6.12 (birth kinematics; Genesis/Triadic notation) |"),
("S-4b", "Appendix C: overload rows",
 r"| $K_p$, $u$ | $2-2\cos(2\pi/p)$; $1/(1-\lambda)$ in the $K_p$ eigenframe | §2 OPEN 9, §6.11, Appendix D | — |",
 r"| $K_p$, $u$ | $2-2\cos(2\pi/p)$; $1/(1-\lambda)$ in the $K_p$ eigenframe | §2 OPEN 9, §6.11, Appendix D | — |"
 "\n" r"| $U$ (other uses) | (i) ISP anti-correlation coordinate $U=\tfrac{\sqrt3}2\rho$ (§6.4); (ii) the start/base-point set $U=\{0<Q\le\tfrac1{625}\}$ (§6.14), whose invariant six-phase tube is $U_T$ (see the $U$, $U_T$ row); (iii) the projection window $U$ of OPEN 16, $\Pi(Q_0,U,\mathcal O)$ | §6.4, §6.14, §2 OPEN 16 | read by section |"
 "\n" r"| $\widehat h$, $h_6$, $h$ (OPEN-M) | formal Poincaré–Dulac normalizer; finite adopted degree-6 normalizer; OPEN-M source amplitude $h$ | §6.16, §6.14, SG-15 | the OPEN-M $h$ is not a normalizer (SG-15) |"
 "\n" r"| $M(s)$ | majorant of $h-\mathrm{id}$ in DYAD-THM-NF-INV; distinct from the $M$ entries above | §6.14 | — |"
 "\n" r"| $\kappa$ | $\kappa=M'(R)$, contraction constant of DYAD-THM-NF-INV; not the historical fit parameter $\kappa_{\rm bb}$ | §6.14, §6.5 | — |"
 "\n" r"| $r$, $r_m$ | polar radius $z=re^{i\Theta}$; L-PHASE remainder $r_m$ | §6.14 | — |"),
# ---- S-5 provenance caveats at point of use ----
("S-5a", "§2 OPEN 9 raw cubic theorem (status, p-range)",
 r"[RID: DYAD-THM-RAW-CUBIC] `[v6.4.20: statement recovered]` For the declared $K_p$ family",
 r"[RID: DYAD-THM-RAW-CUBIC] `[v6.4.21: formula recovered and algebraically verified; identity with the historical proposition not yet established (Appendix E)]` For the declared $K_p$ family"),
("S-5b", "§2 OPEN 9 raw cubic theorem (admissible p-range)",
 r"Scope: one-step, raw frame. It is not the normalized $\nu_3$",
 r"Scope: one-step, raw frame; $p\ge3$ (the raw $Z_p$ eigenframe needs $\lambda\ne\bar\lambda$; the denominator $4\sin(2\pi/p)$ vanishes at $p=2$). It is not the normalized $\nu_3$"),
("S-5c", "Appendix F: RAW-CUBIC row",
 r"| `DYAD-THM-RAW-CUBIC` | statement recovered in P1 (FA-08) |",
 r"| `DYAD-THM-RAW-CUBIC` | formula recovered and algebraically verified (P1, FA-08); identity with the historical proposition not yet established (Appendix E) |"),
("S-5d", "§6.11 projector inventory (unrecovered definitions)",
 r"$C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, $\Delta_{\rm overlap}$." "\n",
 r"$C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, $\Delta_{\rm overlap}$. Eight of these objects ($\mathcal Q(p)$, $\Pi^{\rm extra}_{p,q}$, $J^{extra,raw}_{p,q,D}$, $\mathcal B^{extra}_{p,q,D}$, $Z^{\rm miss}_{p,q,D}$, $C^{\rm mult}_{\rm sub}$, $C^{\rm uniq}_{\rm sub}$, $\Delta_{\rm overlap}$) have no recovered definition (Appendix D). Named source: the OPEN 9 owner working files of the v5.4.x series beyond `OPEN9_arithmetic_horizon_definitions.md`; next step: the owner locates them and records the definitions, or records them as unrecoverable." "\n"),
("S-5e", "§6.11 eigenframe linear-part lemma (statement not recovered)",
 r"`[ALG]` **Eigenframe linear-part lemma.** Anchors the degree-2 no-cascade bypass.",
 r"`[ALG]` **Eigenframe linear-part lemma.** Anchors the degree-2 no-cascade bypass. Its statement is not recovered (Appendix D); named source: the OPEN 9 owner working files of the v5.4.x series; next step: the owner recovers and records the statement."),
# ---- FC-34 cross-reference ----
("FC-34", "§6.12 bridge export table: shear/healing ratio row",
 r"| shear/healing ratio $4\sqrt3/3=\vert \Im\mu\vert /\vert \Re\mu\vert $ | derived from DYAD-THM-C21 | `[ALG]` | ratio of cubic coefficients |",
 r"| shear/healing ratio $4\sqrt3/3=\vert \Im\mu\vert /\vert \Re\mu\vert $ | derived from DYAD-THM-C21 | `[ALG]` | ratio of cubic coefficients; bookkeeping cross-reference (FC-DYAD-34): $(4\sqrt3/3)^2=16/3$ equals Genesis v2.8.9 §6.3's leading homogeneous-graph ratio $Q(c_{0,\rm shear}^{[3]})/Q(c_{0,\rm recoil}^{[3]})$ ($\kappa_{\rm shear}=-2\sqrt3/3$, $\kappa_{\rm recoil}=-\tfrac12$); arithmetic identity only, selects no birth policy |"),
]

B5_ACTIVE = None  # located at run time: the active-list line starting with this prefix
B5_PREFIX = "- Channel boundary all-$p$ (DYAD-OPEN-B5-ALLP): **CLOSED `[ALG]`**."

def main(base, out, log):
    raw = open(base, "rb").read()
    assert hashlib.sha256(raw).hexdigest() == BASE_SHA, "base is not adopted v6.4.20"
    s = raw.decode("utf-8")
    # locate the b=5 active line (long) and the Q403 line to move into the closed list
    lines = s.split("\n")
    b5 = [l for l in lines if l.startswith(B5_PREFIX)]
    assert len(b5) == 1
    q403 = "- Exact cubic cascade formula for $q=4,(0,3)$: **CLOSED (v6.4.9)** `[THM]` `[proof: exact algebraic identity]` — all-$p$ closed form, $Q_p=i\\zeta_p^3 M_p$, $M_p\\in\\mathbb{Q}(\\zeta_p)^+$ (DYAD-THM-Q403-PHASELAW)"
    edits = []
    for k, loc, old, new in EDITS:
        if k == "S-1e2":
            old = b5[0] + "\n"
        if k == "S-1e3":
            new = old + q403 + "\n" + b5[0] + "\n"
        edits.append((k, loc, old, new))
    # Appendix A (the version history) is a historical record: edits apply to live text only.
    i = s.index("## Appendix A — Version History"); j = s.index("## Appendix B —")
    appA = s[i:j]; MARK = "\x00APPENDIX-A\x00"; s = s[:i] + MARK + s[j:]
    record = []
    for k, loc, old, new in edits:
        n = s.count(old)
        assert n == 1, f"{k}: expected 1 match, found {n}"
        s = s.replace(old, new)
        record.append({"key": k, "location": loc,
                       "old_sha256": hashlib.sha256(old.encode()).hexdigest(),
                       "new_sha256": hashlib.sha256(new.encode()).hexdigest(),
                       "old": old, "new": new})
    s = s.replace(MARK, appA)
    data = s.encode("utf-8")
    open(out, "wb").write(data)
    json.dump({"base_sha256": BASE_SHA,
               "intermediate_sha256": hashlib.sha256(data).hexdigest(),
               "edits": record}, open(log, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(hashlib.sha256(data).hexdigest(), len(record), "edits")

if __name__ == "__main__":
    main(*sys.argv[1:4])
