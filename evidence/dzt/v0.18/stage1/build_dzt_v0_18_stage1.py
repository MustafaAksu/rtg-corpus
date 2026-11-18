#!/usr/bin/env python3
"""DZT v0.18, stage 1: corrected intermediate, built from the tagged v0.8 bytes.

    python3 -I evidence/dzt/v0.18/stage1/build_dzt_v0_18_stage1.py [--out PATH] [--log PATH]

Reads the base with `git show dzt-v0.8:<DSN>` and asserts its SHA-256. Every edit is
located by an anchor (a line prefix that must occur exactly once in the current text);
a missing or repeated anchor, or an unexpected old line, stops the build.

Scope (PI decisions of 18 Nov 2026 on records/dzt/DZT_REACTIVATION_TRIAGE.md, list (i)):
stage 1 holds every change that needs a reader's judgment — triage rows 1, 8, 10, 11,
13 and 16, and the parts of the Methodology v1.4 migration that touch claim text
(local aliases, one home per statement in §1, unpacked grade tokens, superseded
observation moved to Appendix B). The header, the version labels removed as history,
Appendix A and the footer are left for stage 2 (Methodology §13.6). No new scientific
claim and no grade is raised.
"""
import argparse
import hashlib
import subprocess
import sys

DSN = "dsn/RTG_DYADIC_ARITHMETIC_RESONANCE_TRANSFORM_DSN.md"
BASE_TAG = "dzt-v0.8"
BASE_SHA = "cad20982d294775d52592c304d743695c6ec2d8cf4975c78de203db3d6a92ff2"
REC = "upload/dzt-recovery-20261116/received/originals/downloads/"
DY = "`RTG_DYADIC_OSCILLATOR_DSN` v6.4.24 (`dyad-v6.4.24`)"
DYS = "Dyadic v6.4.24"

LOG = []


def sha(s):
    return hashlib.sha256(s.encode("utf-8") if isinstance(s, str) else s).hexdigest()


def die(msg):
    sys.stderr.write("BUILD STOP: %s\n" % msg)
    sys.exit(1)


class Doc:
    def __init__(self, text):
        self.L = text.split("\n")

    def find(self, prefix):
        hits = [i for i, l in enumerate(self.L) if l.startswith(prefix)]
        if len(hits) != 1:
            die("anchor %r occurs %d times" % (prefix[:70], len(hits)))
        return hits[0]

    def set_line(self, key, prefix, new, note, old_sha16=None):
        i = self.find(prefix)
        h = sha(self.L[i])[:16]
        if old_sha16 and h != old_sha16:
            die("%s: old line hash %s != expected %s" % (key, h, old_sha16))
        self.L[i] = new
        LOG.append((key, "set-line", "line %d, sha256 %s" % (i + 1, h), "%d chars" % len(new), note))

    def sub(self, key, prefix, old, new, note):
        i = self.find(prefix)
        if self.L[i].count(old) != 1:
            die("%s: %r occurs %d times in its line" % (key, old[:60], self.L[i].count(old)))
        self.L[i] = self.L[i].replace(old, new)
        LOG.append((key, "substitute", repr(old)[:90], repr(new)[:90], note))

    def replace_range(self, key, start_prefix, end_prefix, new_text, note):
        """Replace lines [start, end) by new_text; the end line is kept."""
        a, b = self.find(start_prefix), self.find(end_prefix)
        if not a < b:
            die("%s: empty or reversed range" % key)
        old = "\n".join(self.L[a:b])
        new = new_text.split("\n")
        self.L[a:b] = new
        LOG.append((key, "replace-range", "lines %d-%d, sha256 %s" % (a + 1, b, sha(old)[:16]),
                    "%d lines" % len(new), note))

    def insert_before(self, key, prefix, new_text, note):
        a = self.find(prefix)
        new = new_text.split("\n")
        self.L[a:a] = new
        LOG.append((key, "insert", "before line %d" % (a + 1), "%d lines" % len(new), note))

    def text(self):
        return "\n".join(self.L)


# ---------------------------------------------------------------- replacement blocks

ALIASES = """## Local Tag Aliases

Status tags follow DSN Methodology v1.4 §8.1 and §8.3; qualifiers follow its §3.2. The entries below are local to this document.

| Local alias | Canonical expansion | Use |
|---|---|---|
| `[NUM diagnostic]` | `[NUM]` `[scope: named diagnostic campaign]` | Finite numerical evidence (Methodology §8.4) |

Labels that are not status tags:

- `[import-ref]` marks a reference to a result owned by another DSN (Methodology §4.3). A status tag printed next to it is the owner's tag at the pinned edition (§7); ownership is not transferred.

**Standard clause** (Methodology §1.1, rule 5):

- **[RECOVERED]** — the bytes were received unchanged with the DZT recovery (PR #289; plain files PR #308) and are in `""" + REC + """`; their SHA-256 equals the recovery manifest `upload/dzt-recovery-20261116/received/MANIFEST.json` (`EV-BYTES`, `EV-HASH`). The run recorded in this document is source-reported (`EV-SRC-REPORTED`) and was not repeated for this edition (`EV-NOT-RERUN`); the bytes are not shown to be those of the recorded run.

---
"""

SECTION1_TAIL = """`[ALG]` **$p=12$ reduced norm.** The certified cascade value $v=-13+\\tfrac{15\\sqrt3}{2}$ (Dyadic, channel $(4,(0,3))$, $p=12$) has $N_{\\mathbb{Q}(\\sqrt3)/\\mathbb{Q}}(v)=\\tfrac14$; it is the $\\varphi(12)/2=2$ case of the amplitude norm below. Statement: §6.3, DZT-ALG-P12-NORM.

`[ALG]` `[scope: validation table p=12–64, 14 points]` **Amplitude norm.** With $M_p=Q_p/(i\\zeta_p^3)\\in\\mathbb{Q}(\\zeta_p)^+$ (Dyadic all-$p$ factorization, DYAD-THM-Q403-PHASELAW), $\\lvert N_{\\mathbb{Q}(\\zeta_p)^+/\\mathbb{Q}}(M_p)\\rvert$ is rational at every audited point. The tabulated values are absolute values; their sign is not determined here. The canonical computation is the closed-form audit for $p\\le1000$. Statement and values: §6.3, DZT-ALG-CASCADE-NORM.

`[ALG]` `[scope: finite horizon p≤1000, 249 points]` **Odd-prime anomalies.** On the audited range the values with an odd prime in their numerator are exactly those at $p=8\\ell^a$ ($\\ell$ an odd prime, $\\ell^a\\equiv1\\!\\pmod4$; 20 points), with numerator $\\ell^2$; on the 14-point table the only such point is $p=40$. Statement: §6.3, DZT-ALG-CASCADE-ANOMALY-SET.

`[FAIL]` **Support-on-2 hypothesis.** The hypothesis that the amplitude norm is a pure power of 2 for all $4\\mid p$ is false ($p=40$ gives $\\tfrac{25}{16}$). Record: §6.3 and Appendix B, DZT-HYP-MAHLER-NEARMISS.

`[OPEN]` **Frontier.** DZT-OPEN-0A is closed at finite-horizon scope (all three rows: $b=5$ survival, $b\\le4$ structural absence, cascade $(4,(0,3))$). The active frontier is DZT-OPEN-0B-R: prove or reject the anomaly rule for all $p$ from a resultant identity (§2). Then the Track B objects.

---
"""

PRIORITY_2 = ("2. **DZT-OPEN-0B-R** — prove or reject the corrected resultant pattern: $\\lvert N_+(M_{8q})\\rvert$ has odd-prime "
              "support iff $q=\\ell^a$ is a prime power with $q\\equiv1\\!\\pmod4$, with numerator $\\ell^2$. Verified `[ALG]` "
              "`[scope: finite horizon p≤1000, 249 points]`; candidate mechanism `[HYP]` (below and §6.3).")

OB_VERIFIED_OLD = "Verified `[ALG finite horizon, p≤1000, 249 pts]`: computing $N_+(M_p)$ from"
OB_VERIFIED_NEW = "Verified `[ALG]` `[scope: finite horizon p≤1000, 249 points]`: computing $\\lvert N_+(M_p)\\rvert$ from"

OB_TARGET = ("Open target: prove or reject the corrected rule from a resultant identity for $\\mathrm{Res}(\\Phi_{8q},A_s)$. "
             "With the Dyadic phase law proved for all $p$ (DYAD-THM-Q403-PHASELAW), the factorization and hence the norm object "
             "$M_p\\in\\mathbb{Q}(\\zeta_p)^+$ are defined for all $p=4s\\ge12$, so this is a fully **DZT-native** problem (a "
             "cyclotomic resultant identity) with no remaining dependency on the Dyadic stream. The anomaly law itself stays "
             "`[ALG]` `[scope: finite horizon p≤1000]` until the identity is proved. Candidate mechanism (`[HYP]`): the "
             "$\\equiv1\\!\\pmod4$ gate is the reality of $\\mathbb{Q}(\\sqrt q)\\subset\\mathbb{Q}(\\zeta_q)^+$ — for $q\\equiv1$, "
             "$\\sqrt q$ is real and $\\ell$ enters $N_+$; for $q\\equiv3$, only $\\sqrt{-q}$ (imaginary) lies in "
             "$\\mathbb{Q}(\\zeta_q)$, excluded from the real-subfield norm.")

HR_NORM = ("| Amplitude norm | rational $\\lvert N_+(M_p)\\rvert$ per point, `[ALG]` `[scope: validation table p=12–64; audit "
           "p≤1000]`; on the audited range the odd-prime anomalies are exactly $p=8\\ell^a$, $\\ell^a\\equiv1\\!\\pmod4$ | the "
           "2-power/support-on-2 *law* — **falsified** at $p=40$; any $k_p$ formula; a sign of $N_+(M_p)$ read off the tables | §6.3 |")
HR_PHASE = ("| Phase-law import | $Q_p=i\\zeta_p^3M_p$, $M_p\\in\\mathbb{Q}(\\zeta_p)^+$ as Dyadic **all-$p$ `[THM]`** "
            "(DYAD-THM-Q403-PHASELAW) | zeta-continuation / RH / prime-distribution reading without a named DZT bridge "
            "(SG-DZT-4) | §6.3, §7 |")

B5_IMPORT = ("`[import-ref]` `[ALG]` `[import: RTG_DYADIC_OSCILLATOR_DSN v6.4.24 §6.11 | DYAD-ALG-B5-ALLP-NONVANISHING]` "
             "Channel polynomial $N(x)=2x^6+x^5-5x^4-3x^3-4x^2+2x+1$, with the certified statement $\\Phi_p\\nmid N$ for all "
             "$p$ (cyclotomic non-division; $\\deg N=6\\Rightarrow$ exception set $\\varphi(p)\\le6$, all checked). It closes the "
             "Dyadic OPEN module DYAD-OPEN-B5-ALLP.")

H63 = "### §6.3 Cascade amplitude norm `[ALG]` — mixed content {#sec-6-3-nearmiss-norm}"

PHASE_IMPORT = ("`[import-ref]` `[THM]` `[import: RTG_DYADIC_OSCILLATOR_DSN v6.4.24 §6.11 | DYAD-THM-Q403-PHASELAW]` Each "
                "$q=4,(0,3)$ cascade value (Dyadic extraction DYAD-ART-Q403-EXTRACT; closed form in §7) factors as "
                "$Q_p=i\\zeta_p^3 M_p$ with $M_p=Q_p/(i\\zeta_p^3)\\in\\mathbb{Q}(\\zeta_p)^+$ for all $p=4s\\ge12$ ($p=8$ the "
                "zero degeneracy); the direction $i\\zeta_p^3$ is universal ($\\lambda^{-s}=-i$). $M_p$ is a real algebraic "
                "number whose sign is not asserted here. DZT's pointwise re-verification at the audited $p$ (incl. $p=40$) "
                "corroborates the Dyadic theorem; the all-$p$ proof is Dyadic-owned. `[ALG]` `[scope: object-level, all p=4s≥12]` "
                "Hence the norm $N_{\\mathbb{Q}(\\zeta_p)^+/\\mathbb{Q}}(M_p)\\in\\mathbb{Q}$ is a well-defined invariant for all "
                "$p=4s\\ge12$; its *values and anomaly pattern* are finite-horizon (below).")

CASCADE_NORM = """`[ALG]` `[RID: DZT-ALG-CASCADE-NORM]` `[scope: validation table, p=12–64; canonical computation is the p≤1000 closed-form audit below]` The absolute value of the real-subfield norm, $\\lvert N_{\\mathbb{Q}(\\zeta_p)^+/\\mathbb{Q}}(M_p)\\rvert$, is rational at every point:
$$\\big(\\tfrac14,\\tfrac18,\\tfrac14,\\tfrac18,\\tfrac18,\\tfrac1{32},\\tfrac18,\\tfrac{25}{16},\\tfrac1{32},\\tfrac1{32},\\tfrac1{64},\\tfrac1{64},\\tfrac1{16},\\tfrac1{512}\\big),\\quad p=(12,16,20,24,28,32,36,40,44,48,52,56,60,64).$$
Pure 2-power at all 14 points except $p=40$: $\\lvert N_+(M_{40})\\rvert=\\tfrac{25}{16}=5^2\\cdot2^{-4}$ (numerator $5^2$; the only value above 1 on the table). The values are absolute values: the closed-form audit computes $\\sqrt{\\lvert N_{\\rm full}\\rvert}$ (§8, DZT-ART-CF-AUDIT), and the sign of $N_+(M_p)$ is not determined by DZT. Machine-verified `dzt_casev_norm_audit.py` (14-point, exit 1, falsifier flags $p=40$); $p=40$ and $p=60$ cross-checked against fresh Dyadic-engine extractions (runs source-reported; §8).
"""

P12_HOME = ("`[ALG]` `[RID: DZT-ALG-P12-NORM]` The certified cascade-boundary survivor $v=-13+\\tfrac{15\\sqrt3}{2}\\in\\mathbb{Q}(\\sqrt3)$ "
            "(Dyadic, channel $(q,D)=(4,(0,3))$, $p=12$; $|v|\\approx0.0096$) has $\\mathbb{Q}(\\sqrt3)/\\mathbb{Q}$ **reduced** field norm "
            "$N_{\\mathbb{Q}(\\sqrt3)/\\mathbb{Q}}(v)=v\\,\\bar v=(-13)^2-3\\big(\\tfrac{15}{2}\\big)^2=169-\\tfrac{675}{4}=\\tfrac14$. "
            "The smallness of $|v|$ coincides with a large conjugate ($\\bar v\\approx-25.99$) and a small rational norm $\\tfrac14$. "
            "The norm value is exact and machine-verified (`dzt_open_0a_verify.py`, §8; run source-reported). It is the "
            "$\\varphi/2=2$ point ($\\mathbb{Q}(\\zeta_{12})^+=\\mathbb{Q}(\\sqrt3)$); $p=8$ is the $Q_8=0$ degeneracy "
            "($\\mathbb{Q}(\\zeta_8)^+=\\mathbb{Q}(\\sqrt2)$). A fact about one value; survives the family falsification.")

SURVIVES = """`[OPEN]` What survives the falsification: the norm is rational; the Dyadic factorization holds; the certified boundaries are reproduced. The odd-prime support question is DZT-OPEN-0B-R (§2); the anomaly set found so far is DZT-ALG-CASCADE-ANOMALY-SET below — not support-on-2.
"""

ANOMALY_SET = ("`[ALG]` `[scope: finite horizon p≤1000, 249 points]` `[RID: DZT-ALG-CASCADE-ANOMALY-SET]` The odd-prime anomalies "
               "are exactly $p=8\\ell^a$ with $\\ell^a\\equiv1\\!\\pmod4$: the 20 points "
               "$\\{40,72,104,136,200,232,296,328,392,424,488,584,648,712,776,808,872,904,968,1000\\}$, each with "
               "$\\lvert N_+\\rvert$ numerator exactly $\\ell^2$ (e.g. $p=72=8\\cdot3^2\\!\\to9/64$; $p=200=8\\cdot5^2\\!\\to25/2^{20}$; "
               "$p=392=8\\cdot7^2\\!\\to49/2^{42}$). Machine-verified `dzt_anomaly_rule_check.py` (exit 0, 0 mismatches / 249; "
               "run source-reported, §8).")

NOTE_CORR = """`[ALG]` `[scope: finite horizon p≤1000]` **Correction of the imported note.** The note's pattern "anomaly for every odd prime power $q$" is **false**: prime powers $q\\equiv3\\!\\pmod4$ ($p=24,56,88,152,184,216,\\dots$) are pure 2-powers on the audited range. The required condition is $q\\equiv1\\!\\pmod4$. The note's $N_+=2^{-\\varphi(q)}$ denominator formula also fails in general (only the anomaly *locations* and the $\\ell^2$ *numerators* are clean); **no denominator law is asserted**.

`[HYP]` Candidate mechanism for the mod-4 gate: $q\\equiv1\\!\\pmod4\\Rightarrow\\mathbb{Q}(\\sqrt q)\\subset\\mathbb{Q}(\\zeta_q)^+$ real (so $\\ell$ enters the real-subfield norm); $q\\equiv3\\Rightarrow$ only $\\mathbb{Q}(\\sqrt{-q})$, imaginary, excluded. To be settled by the DZT-OPEN-0B-R resultant identity."""

IMPORTS = """All imports are from """ + DY + """, checked against that edition for v0.18; identifiers as classified by its Appendix F (`dyad-v6.4.24`), which creates no alias. Ownership remains Dyadic. No AZ, TDR-G, OPEN-M or Genesis import (SG-DZT-1/2/5).

- [RID: DYAD-ALG-B5-ALLP-NONVANISHING] :: $b=5$ channel: $F_{\\rm raw}^p(0,5)\\ne0$ for every $p\\ge6$; channel polynomial $N=2x^6+x^5-5x^4-3x^3-4x^2+2x+1$ with $\\Phi_p\\nmid N$ :: """ + DYS + """ §6.11 :: source for §6.2 :: dyadic map, $b=5$, all $p\\ge6$
  Source status: `[ALG]` (all $p$, complete); it closes the lifecycle identifier DYAD-OPEN-B5-ALLP.
  Verification: owner entry inspected (`EV-SRC-READ`); owner artifacts not rerun by DZT.
- [RID: DYAD-ALG-VANISH-B2] :: $F_{\\rm raw}^p(0,2)=0$ for $p\\ge4$; no secular mode :: """ + DYS + """ §6.11 :: $b\\le4$ row of DZT-OPEN-0A (DZT-ALG-B234-STRUCTURAL) :: dyadic map, $p\\ge b+2$ only
  Source status: `[ALG]`.
- [RID: DYAD-ALG-VANISH-B3] :: $F_{\\rm raw}^p(0,3)=0$ for $p\\ge5$; no secular mode :: """ + DYS + """ §6.11 :: as above :: dyadic map, $p\\ge b+2$ only
  Source status: `[ALG]`.
- [RID: DYAD-ALG-VANISH-B4] :: $F_{\\rm raw}^p(0,4)=0$ for $p\\ge6$; no secular mode :: """ + DYS + """ §6.11 :: as above :: dyadic map, $p\\ge b+2$ only
  Source status: `[ALG]`.
- Cascade values at $p=8$ and $p=12$ (no owner RID) :: channel $(4,(0,3))$: $p=8$ cancels; $p=12$ value $-13+\\tfrac{15\\sqrt3}{2}$ :: """ + DYS + """ §6.11 and §2 OPEN 9 :: §6.3, DZT-ALG-P12-NORM :: dyadic map
  Source status: owner statement without a RID (owner Appendix F, `dyad-v6.4.24`, lists the string DZT used as unmatched); cited as text. Sign as stated by the owner.
- [RID: DYAD-ALG-P6-FACEFLUX] :: $\\lambda_6=e^{iF_f/2}=e^{i\\pi/3}$ resonance eigenvalue :: """ + DYS + """ §6.2 :: SG-DZT-7 two-root discipline :: $p=6$ only
  Source status: `[ALG]`.
- [RID: DYAD-THM-Q403-PHASELAW] :: for $p=4s$, $s\\ge2$: $\\sigma_{-1}(Q)=-L^{-6}Q$ for the closed form $Q=L^5(IL^2+I-L^2+1)/[2(L+1)^4(L^2+L+1)]$, $L=\\zeta_p$, $I=L^{p/4}=i$; hence $Q_p=i\\zeta_p^3M_p$ with $M_p=Q_p/(i\\zeta_p^3)\\in\\mathbb{Q}(\\zeta_p)^+$ ($p=8$ the zero degeneracy; nonzero phase law from $p=12$) :: """ + DYS + """ §6.11 :: §6.3 norm object; closed-form audit of DZT-OPEN-0B-R :: dyadic map, $4\\mid p$
  Source status: `[THM]` `[proof: exact algebraic identity]`. Its parts at the owner carry no separate RIDs (owner Appendix F, `dyad-v6.4.24`): the universal direction $\\lambda^{-s}=\\zeta_p^{-p/4}=-i$ for all $4\\mid p$; the reality relation $f^{\\bar W}_{(b,a)}=\\overline{f^W_{(a,b)}}$, lifting through composition ($J(f^s)=(Jf)^s$), with $J$ realized by the Galois automorphism $\\sigma_{-1}$; the leading $(0,3)$ accumulation $\\sum_{k=0}^{s-1}\\zeta_p^{-4k}=0$ for $s\\ge2$, so that $Q_p$ is the subleading remainder (total cancellation at $s=2$, i.e. $Q_8=0$); the remainder relation in its $A_p$-form, $\\sigma_{-1}(A_p)=\\zeta_p^{-6}A_p$; and the closed form above.
  Verification: owner entry inspected (`EV-SRC-READ`). DZT checked the closed form against the Dyadic extractor at $p=12,16,20,24,40,44,60$ (source-reported). The owner certificate is DYAD-ART-Q403-CERT; not rerun by DZT.
- [RID: DYAD-ART-Q403-EXTRACT] :: exact in-field extractor `q4_03_cascade_extract.py` for the Case-V values $Q_p\\in\\mathbb{Q}(\\zeta_p)$ ($p=8$–$64$, $4\\mid p$): raw $R^{\\rm raw}_{p,4}=\\lambda^{-s}f_p^s-\\mathrm{Id}$, $s=p/4$, charge-projected on $K^{\\rm extra}_{p,4}$, $\\chi(a,b)=(a-b-1)\\bmod p$; calibration gates $p=8\\to0$, $p=12\\to-13+\\tfrac{15\\sqrt3}{2}$ :: """ + DYS + """ §8 :: source of the Case-V values used for §6.3 and DZT-ALG-CASCADE-ROW :: dyadic map, $4\\mid p$, $p=8$–$64$
  Source status: owner artifact `[ALG]`. Correspondence by content only: DZT cited the extractor with SHA-256 `ecdb805f…05eac2` and its horizon file with `14526cf1…7bec16`; the owner records no hash and neither file is in this repository, so no byte identity is claimed.
- [RID: DYAD-ART-Q403-CERT] :: certificate `q4_03_R_identity_certificate.py`, exits `CERTIFICATE PASS` :: """ + DYS + """ §8 :: proof artifact of DYAD-THM-Q403-PHASELAW :: —
  Availability: not in this repository; not rerun by DZT.

---
"""

ARTIFACTS = """Paths in this section are relative to `""" + REC + """`.

- [RID: DZT-ART-VERIFY-0A] :: `dzt_open_0a_verify.py` :: computes $R_{(0,5)}(p)$ over the horizon sweep and the $p=12$ reduced field norm; reproduces imported $b=5$ survival on the tested horizon (ownership-safe wording) and norm $=\\tfrac14$ :: `[ENG]` exit 0
  Files: [RECOVERED] two contents — `dzt_open_0a_verify (1).py` (= `dzt_open_0a_verify (2).py`), SHA-256 `3791b110b94fb7e6988c05109d963522f1fbc9e2907034945152d74ff7ba5c7e`, whose output wording matches this entry; and `dzt_open_0a_verify.py`, SHA-256 `989f6c2d858747bac66a97a7fe6eb6a7e135ddde040c57a936f881a7a9e62b52`, without the ownership-safe wording.
- [RID: DZT-ART-CHANNEL-AUDIT] :: `dzt_channel_audit.py` :: two-layer channel-state audit; certifies $b\\le4$ $E_C=0$ structural-absence encoding (no resultant), distinct from $b=5$ $E_C=1$ cyclotomic survival; cascade row intentionally not computed :: `[ENG]` exit 0
  Files: [RECOVERED] `dzt_channel_audit.py`, SHA-256 `afcbed4f6ba7d6d00aef40d181789626fa44a6a9dd3b283ca5e171fa384c563c`.
- [RID: DZT-ART-CASCADE-AUDIT] :: `dzt_0b_audit.py` :: re-extracts $Q_p$ from the Dyadic engine, verifies the phase law and $M_p\\in\\mathbb{Q}(\\zeta_p)^+$, computes field norms $p=12$–$28$ :: `[ENG]` exit 0
  Files: [RECOVERED] `dzt_0b_audit.py`, SHA-256 `b586c7c273469dd075164b245b485486ca08a33f514f11585c00ac940f8586f9`. It calls the Dyadic engine, which is not in this repository.
- [RID: DZT-ART-NORMLAW] :: `dzt_0b_normlaw.py` :: 7-point amplitude-norm computation ($p=12$–$36$); superseded as evidence by the 14-point transcription harness and, canonically, by the closed-form audit DZT-ART-CF-AUDIT :: `[ENG]` exit 0
  Files: [RECOVERED] `dzt_0b_normlaw.py`, SHA-256 `1b03da50a3bc02c7efd368d644970ec84f1c8255990ea6e31814a888c57f0fb4`.
- [RID: DZT-ART-CASEV-AUDIT] :: `dzt_casev_norm_audit.py` :: reusable 14-point transcription-based Case-V audit ($p=12$–$64$); **falsifies** support-on-2 at $p=40$ :: `[ENG]` exit 1 (falsifier fired, as designed)
  Files: [RECOVERED] two contents — `dzt_casev_norm_audit (1).py`, SHA-256 `22783fcd701dce5f4a8cf073f84db058e13604b55b1f5867e5653a32f54f0f16`, the 14-point audit this entry describes; and `dzt_casev_norm_audit.py`, SHA-256 `d48716c892d9c04804cdebd1bde79fb4cc6efff95d24f213634c932fc8279d9b`, an earlier, shorter horizon.
- [RID: DZT-ART-CF-AUDIT] :: `dzt_casev_norm_from_closed_form.py` :: transcription-free closed-form norm audit to $p=1000$ (249 points) from the Dyadic closed form (DYAD-THM-Q403-PHASELAW, §7); it reports $\\sqrt{\\lvert N_{\\rm full}\\rvert}$, so the sign of $N_+(M_p)$ is not part of its output; CSV `dzt_casev_norm_closed_form_p8_1000.csv` :: `[ENG]` (Dyadic-imported script, DZT-rerun)
  Files: [RECOVERED] two contents — `dzt_casev_norm_from_closed_form (2).py` (= `(3)`), SHA-256 `e38b5f7e0d809bc9333df91968ee741c89fecad5ea8fcd10fbfd3eecd65aa6ed`, which prints the required $q\\equiv1\\!\\pmod4$ condition; and `dzt_casev_norm_from_closed_form.py` (= `(1)`), SHA-256 `4d3d3ca374d884377cf1ad5faa83fa218897c10dd69d9e119e076a73f7edb10e`, the uncorrected printed heuristic. CSV `dzt_casev_norm_closed_form_p8_1000.csv`, SHA-256 `d9dd7bd90bb9fd2340f6e5259129437db4850d5c057be0d5f527bbc78183555a`.
- [RID: DZT-ART-ANOMALY-RULE] :: `dzt_anomaly_rule_check.py` :: verifies the **corrected** anomaly rule ($p=8\\ell^a$, $\\ell^a\\equiv1\\!\\pmod4$, numerator $\\ell^2$) against the 249-row CSV :: `[ENG]` exit 0 (0 mismatches)
  Files: [RECOVERED] `dzt_anomaly_rule_check.py`, SHA-256 `cec06de0650a43f91f4c242403c6eb18af5a40915add5cdc2ff51611a4145b44`.

Every exit code in this section is source-reported; none was rerun for v0.18.

---
"""

APPENDIX_B_ADD = """
---

`[SUPERSEDED]` Original (DZT-ALG-CASCADE-NORM and the §1 readout, `dzt-v0.8` §1 and §6.3): the tabulated values were headed $N_+(M_p)$, and $M_p$ was written as $\\lvert Q_p\\rvert$. Reason: the values are absolute values — the closed-form audit computes $\\sqrt{\\lvert N_{\\rm full}\\rvert}$ and the sign of $N_+(M_p)$ is not determined by DZT — and $M_p$ is defined as $Q_p/(i\\zeta_p^3)$, a real number whose sign is not asserted. Replacement: §6.3, DZT-ALG-CASCADE-NORM, stated for $\\lvert N_+(M_p)\\rvert$; the values are unchanged. Recorded in: v0.18.

---

`[SUPERSEDED]` Original (`dzt-v0.8` §6.3, an `[OBS]` of v0.6): "$p=40$ is the sole anomaly across 14 points", an isolated exception. Reason: true only for $p\\le64$; the closed-form audit to $p\\le1000$ finds 20 anomaly points (the next after $p=40$ is $p=72$), as the v0.7 `[COR]` recorded. Replacement: §6.3, DZT-ALG-CASCADE-ANOMALY-SET. Recorded in: v0.7 (as a `[COR]` in §6.3); moved here in v0.18.
"""


def build(base_text):
    d = Doc(base_text)
    # E00 header companion pins, except the Methodology pin (row 9, S1; the Methodology pin is stage 2)
    d.set_line("E00a programme-pin", "**Programme document:**",
               "**Programme document:** Programme Overview v1.4 (`programme-v1.4`)",
               "Programme pin at the governing tag (row 9)")
    d.sub("E00b companion-pins", "**Companion documents:**",
          "`RTG_DYADIC_OSCILLATOR_DSN_v6.4.8.1` (source of truth for all OPEN 9 arithmetic) · `RTG_ARITHMETIC_RESONANCE_AND_ZETA_DSN_v0.6` (discrete-branch AZ; quarantined, see SG-DZT-1) · `RTG_ONTOLOGICAL_FOUNDATIONS_v0.7`",
          "Dyadic Oscillator v6.4.24 (`dyad-v6.4.24`; source of truth for all OPEN 9 arithmetic) · Arithmetic Resonance and Zeta v0.10 (`az-v0.10`; discrete branch, quarantined, see SG-DZT-1) · Ontological Foundations v0.12 (`ofn-v0.12`)",
          "Dyadic, AZ and OFN pins at the governing tags (row 9); Methodology pin unchanged here")
    # E01 local aliases (triage row 13; Methodology v1.4 §8.4)
    d.replace_range("E01 aliases", "## Local Tag Aliases", "## §1. Current Canonical State", ALIASES + "",
                    "aliases under Methodology v1.4 §8.4; [import-ref] a label, not a status alias; standard clause [RECOVERED] (row 16)")
    # E02 Dyadic identifiers in the channel-state definition (row 10)
    d.sub("E02 vanish-ids", "- $E_C(p)=0$ — **structural/secular absence**", "Dyadic DYAD-ALG-VANISH-B2/B3/B4",
          "Dyadic DYAD-ALG-VANISH-B2, DYAD-ALG-VANISH-B3, DYAD-ALG-VANISH-B4",
          "three owner RIDs (Dyadic Appendix F)")
    # E02b cascade row of DZT-OPEN-0A: Dyadic artifact RID and |N_+| (rows 1, 10)
    d.sub("E02b 0A-cascade-art", "- Cascade $(q,D)=(4,(0,3))$", "(DYAD-ART-CASCADE-Q4-03, hash-pinned)",
          "(Dyadic extractor DYAD-ART-Q403-EXTRACT; §7)", "owner artifact RID per Appendix F; byte identity not claimed (§7)")
    d.sub("E02c 0A-cascade-abs", "- Cascade $(q,D)=(4,(0,3))$", "is rational at all points; 2-power on",
          "is rational at all points; its absolute value is a 2-power on", "the 2-power statement is about |N_+| (row 1)")
    # E03 §1: one home per statement; |N_+| labels; scope of the tables; frontier (rows 1, 8, 13)
    d.replace_range("E03 section1", "`[ALG]` **First native arithmetic fact", "## §2. Active Frontier / OPEN Registry",
                    SECTION1_TAIL,
                    "§1 keeps readouts with RIDs and pointers (Methodology §1.1 rule 3); |N_+| labels (row 1); table and anomaly scopes stated together (row 8); [HEUR diagnostic] unpacked (row 13)")
    # E04 §2 priority item (row 13)
    d.set_line("E04 priority-2", "2. **DZT-OPEN-0B-R**", PRIORITY_2,
               "[HEUR/ALG finite horizon] unpacked; mechanism by pointer (one home)")
    # E05 OPEN-0B-R block (rows 1, 10, 13)
    d.sub("E05 0B-R verified", "Verified `[ALG finite horizon, p≤1000, 249 pts]`", OB_VERIFIED_OLD, OB_VERIFIED_NEW,
          "grade token unpacked; |N_+|")
    d.set_line("E06 0B-R target", "Open target: prove or reject the corrected rule", OB_TARGET,
               "version label removed; Dyadic RID; grade token unpacked; mechanism kept `[HYP]`")
    # E07 §5 rows (rows 1, 8, 10, 13)
    d.set_line("E07 HR norm", "| Amplitude norm |", HR_NORM, "|N_+|; table and audit scopes; [ALG fin-hor] unpacked")
    d.set_line("E08 HR phase", "| Phase-law import |", HR_PHASE, "Dyadic RID per Appendix F")
    # E09 §6.2 import (row 10)
    d.set_line("E09 b5-import", "`[import-ref]` Channel polynomial (Dyadic DYAD-OPEN-B5-ALLP)", B5_IMPORT,
               "Methodology §3.3 import form; owner result RID; lifecycle RID kept")
    # E10 §6.3 heading and phase-law import (rows 1, 10, 13)
    d.set_line("E10 6.3-heading", "### §6.3 Cascade amplitude norm", H63, "mixed-content heading (Methodology §3.5); anchor kept")
    d.set_line("E11 phase-import", "`[import-ref]` `[from: DYAD-ART-CASCADE-Q4-03", PHASE_IMPORT,
               "M_p defined, not |Q_p| (row 1); Dyadic RIDs (row 10); [THM/ALG] and [ALG all-p] unpacked (row 13); version label removed")
    # E12 cascade norm (rows 1, 8)
    d.replace_range("E12 cascade-norm", "`[ALG]` `[RID: DZT-ALG-CASCADE-NORM]`",
                    "`[FAIL]` `[RID: DZT-HYP-MAHLER-NEARMISS]` The v0.4 hypothesis", CASCADE_NORM,
                    "|N_+| labels and sign statement (row 1); runs marked source-reported (row 16)")
    # E12b one home for the p=12 norm statement (the §1 detail moves here; Methodology §1.1 rule 3)
    d.set_line("E12b p12-home", "`[ALG]` `[RID: DZT-ALG-P12-NORM]`", P12_HOME,
               "full statement at its §6.3 home, including the computation and evidence pointer formerly only in §1")
    # E13 survives / superseded v0.6 OBS and its v0.7 COR (row 8; live-file rule)
    d.replace_range("E13 survives", "`[OPEN]` Survives:", "`[ALG finite horizon]` `[scope: p≤1000, 249 points]`", SURVIVES,
                    "superseded [OBS] 'p=40 isolated' and its [COR] leave the live text; recorded in Appendix B (row 8)")
    d.set_line("E14 anomaly-set", "`[ALG finite horizon]` `[scope: p≤1000, 249 points]`", ANOMALY_SET,
               "[ALG finite horizon] unpacked (row 13); |N_+| (row 1); run source-reported (row 16)")
    d.set_line("E15 note-correction", "`[HEUR diagnostic]` **Correction of the imported note.**", NOTE_CORR,
               "undeclared alias [HEUR diagnostic] unpacked: verified finite statement [ALG], mechanism [HYP] (row 13)")
    # E16 §7 import ledger (rows 9, 10, 11)
    d.replace_range("E16 imports", "- [RID: DYAD-OPEN-B5-ALLP] ::", "## §8. Artifact and Script Registry", IMPORTS,
                    "Import Ledger in Methodology §4.3 form at dyad-v6.4.24, per Dyadic Appendix F; no alias")
    # E17 §8 artifacts (row 16)
    d.replace_range("E17 artifacts", "- [RID: DZT-ART-VERIFY-0A] ::", "## §9. Collaboration and Provenance", ARTIFACTS,
                    "recovered files by path and SHA-256; evidence states; exit codes source-reported")
    # E18 §9 provenance tag cells (row 13)
    d.sub("E18 prov-283", "| Amplitude norm 2-power on $p=12$–$36$", "| `[ALG fin-hor]` |",
          "| `[ALG]` `[scope: finite horizon]` |", "grade token unpacked")
    d.sub("E19 prov-286", "| $p=40$ is the sole 2-power anomaly across 14 points", "(isolated outlier) | Claude (v0.6) | `[OBS]` |",
          "(isolated outlier; superseded, Appendix B) | Claude (v0.6) | `[OBS]` |", "superseded observation marked")
    d.sub("E20 prov-289", "| Corrected anomaly rule:", "| `[ALG fin-hor]`/`[HEUR]` |",
          "| `[ALG]` `[scope: finite horizon p≤1000]`; mechanism `[HYP]` |", "compound token unpacked")
    d.sub("E21 prov-291", "| (R)-link closed upstream", "| `[THM/ALG]` |", "| `[THM]` (Dyadic) |", "owner grade")
    d.sub("E22 prov-292", "| Object-vs-pattern discipline", "| `[scope]` |", "| `[DEF]` (scope rule) |", "non-tag replaced")
    d.sub("E23 prov-294", "| Imported Dyadic all-$p$ THMs", "| `[THM]`/`[ALG fin-hor]` |",
          "| `[THM]` (Dyadic, at `dyad-v6.4.24`) |", "owner grade at the pinned edition")
    # E24 Appendix B (rows 1, 8)
    d.insert_before("E24 appendix-b", "*END OF DOCUMENT", APPENDIX_B_ADD.lstrip("\n"),
                    "two [SUPERSEDED] records: |N_+| labels and M_p wording; v0.6 'p=40 isolated' observation")
    return d.text()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=DSN)
    ap.add_argument("--log", default="evidence/dzt/v0.18/stage1/edit_log.txt")
    a = ap.parse_args()
    base = subprocess.run(["git", "show", "%s:%s" % (BASE_TAG, DSN)], capture_output=True, check=True).stdout
    if sha(base) != BASE_SHA:
        die("base hash %s != %s" % (sha(base), BASE_SHA))
    out = build(base.decode("utf-8"))
    # assertions on the result
    for s in ["DYAD-THM-Q403-PHASE-ALLP", "DYAD-ART-CASCADE-Q4-03", "DYAD-ALG-PHASELAW", "DYAD-THM-P1", "DYAD-THM-REALITY",
              "DYAD-THM-LEAD", "DYAD-CF-Q403", "DYAD-ALG-CASCADE-P12", "DYAD-ALG-VANISH-B2/B3/B4", "M_p=|Q_p|",
              "[THM/ALG]", "[ALG fin-hor]", "[HEUR diagnostic]", "[ALG finite horizon"]:
        live = out.split("## Appendix A")[0].split("**Status summary:**")[1].split("\n", 1)[1]
        if s in live:
            die("forbidden string survives in the live body: %r" % s)
    for rid in ["DZT-DEF-CHANNEL-TRANSFORM", "DZT-DEF-CHANNEL-STATE", "DZT-DEF-AMBIENT-FIELD", "DZT-ALG-P12-NORM",
                "DZT-ALG-CASCADE-NORM", "DZT-HYP-MAHLER-NEARMISS", "DZT-OPEN-REPRODUCTION-AUDIT", "DZT-ALG-B5-RESULTANT",
                "DZT-ALG-B234-STRUCTURAL", "DZT-ALG-CASCADE-ROW", "DZT-OPEN-NORM-LAW", "DZT-OPEN-LOCAL-FORMAL-ZETA",
                "DZT-OPEN-ANALYTIC-ZETA", "DZT-ALG-CASCADE-ANOMALY-SET", "DZT-RETRACT-MAHLER-RESULT"] + \
               ["DZT-ART-" + x for x in ["VERIFY-0A", "CHANNEL-AUDIT", "CASCADE-AUDIT", "NORMLAW", "CASEV-AUDIT", "CF-AUDIT", "ANOMALY-RULE"]]:
        if "[RID: %s]" % rid not in out and "RID: %s]" % rid not in out:
            die("registered RID lost: %s" % rid)
    for i in range(1, 9):
        if "[SG-DZT-%d]" % i not in out:
            die("guard lost: SG-DZT-%d" % i)
    data = out.encode("utf-8")
    with open(a.out, "wb") as f:
        f.write(data)
    with open(a.log, "w", encoding="utf-8", newline="\n") as f:
        f.write("DZT v0.18 stage 1 edit log\nbase %s %s\nresult sha256 %s, %d bytes\n\n" % (BASE_TAG, BASE_SHA, sha(data), len(data)))
        for k, op, old, new, why in LOG:
            f.write("%-22s %-14s\n    old: %s\n    new: %s\n    why: %s\n" % (k, op, old, new, why))
    print("stage 1 written: %s, %d bytes, sha256 %s, %d edits" % (a.out, len(data), sha(data), len(LOG)))


if __name__ == "__main__":
    main()
