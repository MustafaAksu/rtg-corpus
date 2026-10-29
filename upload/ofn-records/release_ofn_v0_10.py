# release_ofn_v0_10.py — OFN v0.10 final owner file from the approved Draft 2 (19 Oct 2026)
# PI approval ("Onay veriyorum", 19 Oct 2026, 18:26 TRT) is bound to Draft 2 SHA-256 58e2dec5…3610.
# Publication edits only: header/adoption metadata, proposed->registered wording, history entry, footer.
import hashlib, sys, re
D2 = sys.argv[1] if len(sys.argv) > 1 else 'RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_DRAFT2.md'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'RTG_ONTOLOGICAL_FOUNDATIONS_v0_10.md'
D2_SHA = '58e2dec54ad600dec189119adc16c8ca89872e74419f78ae317f33558a913610'
raw = open(D2, 'rb').read()
assert hashlib.sha256(raw).hexdigest() == D2_SHA, 'input is not the approved Draft 2'
s = raw.decode('utf-8'); d2 = s; log = []
def rep(old, new, tag, count=1):
    global s
    n = s.count(old); assert n == count, (tag, n); s = s.replace(old, new); log.append(tag)
BR = '  '
# R01 header block
h0 = s.index('# RTG_ONTOLOGICAL_FOUNDATIONS_v0.10'); h1 = s.index('## Local Tag Aliases')
H = [
'# RTG_ONTOLOGICAL_FOUNDATIONS_v0.10', '',
'**Title:** Relational Time Geometry — Ontological Foundations and Model-Selection Layer',
'**Date:** 19 October 2026',
'**Scope:** Integration of the co-owner-accepted FMS model-selection handoff (genuine relational-triad contract, class-C model contract and its scoped imports) into the adopted v0.9 text. No v0.9 definition body, hypothesis, local result, guard or OPEN status is revised.',
'**Document class:** Foundational ontology / model-selection ledger under Methodology v1.3 §0.5.',
'**Document status:** ADOPTED — active canonical Ontological Foundations v0.10, effective 19 October 2026.',
'**Supersedes:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0.9` as the active OFN reference, effective 19 October 2026. Adopted v0.9 (SHA-256 `5ae8fdab…9795`), Draft 1 and Draft 2 are preserved unchanged as historical records.',
'**Companion documents:** unchanged from v0.9 for every inherited import. The v0.10 additions cite only: `RTG_GENESIS_GEOMETRY_DSN_v2.8.9`; `RTG_DYADIC_OSCILLATOR_DSN_v6.4.16` (lifecycle-only release) with v6.4.13–v6.4.15 as the RID sources; `RTG_RRF_REPRESENTATION_REGISTRY_v0.8.3` (adopted working standard). Inherited v0.9 pins are not re-pinned (§11.4).',
'**DSN Methodology:** DSN_METHODOLOGY_v1.3',
'**Status summary:** v0.10 adds §5.5, the genuine relational-triad model-selection contract for the FMS interface: verdicts Q1–Q6 with Standard C at cubic order and the local C³ regularity of Q6; the class-C transported family declared as a different conditional model (RRF v0.8.3 §0.3); two OFN local results; the scoped FMS disposition; and the ψ-modulus with its readout limit. Five claim-level imports (IMP-O10-01–05) and five reference-only records (RF-O10-01–05) are added. Registered OFN records are now eleven definitions, FSP-U as hypothesis, four local results and twenty-one foundational OPENs (twenty inherited statuses unchanged — nineteen ACTIVE, one PARTIAL — plus OPEN-OFN-TRIAD-CLASS, ACTIVE). No physical carrier, chirality, isolation regime, exchange operation, ontology or primacy is selected.',
'**Authors:** Mustafa (PI) · Claude · ChatGPT · Gemini · Grok — inherited attribution; separate approval by every listed contributor is not inferred.',
'**Revision editor:** Claude (OFN co-owner); second OFN co-owner review by ChatGPT.',
'**Programme document / placement:** Adopted Programme v1.2; Tier 2, namespace `RTG-OFN`; no maturity change.',
'**Revision base:** Adopted `RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md`, SHA-256 `5ae8fdabad35a370f5709afa4d5dca6491e154c75f8a6f15fbb32d251fe59795`, equal to its release record.',
'**Governing input:** `OFN_REPLY_TO_FMS_MODEL_SELECTION_v0_8_2.md`, SHA-256 `6e4fc3c3a999617a63482d0c19d3aa388031e8dbc55c5d7742fb6eadaf564b1d`, accepted by both OFN co-owners on 19 October 2026.',
'**Adoption:** Adopted on 19 October 2026 by Mustafa (PI) ("Onay veriyorum", 18:26 TRT), approving O10-P1–P7 in full at their stated scopes, after the second co-owner\'s final disposition ACCEPT — OWNER ADOPTION READY. O10-P7 interface notices take effect from this adoption.',
'**Approved draft:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_DRAFT2.md`, SHA-256 `58e2dec54ad600dec189119adc16c8ca89872e74419f78ae317f33558a913610`, preserved unchanged. Chain: v0.9 → `build_ofn_v0_10_draft1.py` (`6a4fe7af…58ff`) → Draft 1 (`d94e1e39…8c36`) → `build_ofn_v0_10_draft2.py` (`930b0aef…5c82`) → Draft 2 → `release_ofn_v0_10.py` → this file. Both drafts were rebuilt independently by the second co-owner.',
'**Release record:** `RTG_ONTOLOGICAL_FOUNDATIONS_v0_10_RELEASE_RECORD.md` (identities, publication-edit list, outbound notices N-O10-1–4).',
'**Not integrated:** the 13 October 2026 OPEN-narrowing package; it needs its own authorization.',
'**Evidence boundary:** Owner statements were read at the cited sections; co-owner SESSION computations are listed in §12.1. No owner certificate is rerun. FMS SESSION results are reference-only (RF-O10-02); the universal finite-$a$ statement keeps its FMS P4 qualification.',
'',
]
s = s[:h0] + '\n'.join(l + BR if l.startswith('**') else l for l in H) + '\n' + s[h1:]; log.append('R01 header')
# R02 proposed -> registered wording in new text only
pairs = [
('*v0.10 Draft 1 / Draft 2:* no adoption is recorded. The second co-owner accepted Draft 1 with two editorial corrections, applied in Draft 2; proposals O10-P1–P7 (§12.5) await a separate PI decision on Draft 2.',
 '*v0.10:* adopted on 19 October 2026 by the PI, approving O10-P1–P7 on Draft 2 (SHA-256 `58e2dec5…3610`). The v0.9 registrations, statements and custody are retained; v0.10 adds two definitions, two local results and one OPEN record, and closes no scientific OPEN.'),
('| Genuine relational-triad model-selection contract (proposed v0.10) |', '| Genuine relational-triad model-selection contract (v0.10) |'),
('### 5.5 Genuine Relational-Triad Model-Selection Contract (FMS Receiving Interface) — proposed v0.10', '### 5.5 Genuine Relational-Triad Model-Selection Contract (FMS Receiving Interface) — v0.10'),
('Every `[DEF]` and `[RESULT]` in this section is **proposed** (O10-P2–P5) and carries no owner status until PI adoption.',
 'The `[DEF]` and `[RESULT]` records in this section are registered by the v0.10 adoption (O10-P2–P5, 19 October 2026).'),
('`[DEF]` [proposed; part of RTG-OFN-DEF-TRIAD-MODEL-CONTRACT]', '`[DEF]` [part of RID: RTG-OFN-DEF-TRIAD-MODEL-CONTRACT]', 2),
('[proposed RID: ', '[RID: ', 5),
('its OFN registration is proposed here.', 'its OFN registration is made by the v0.10 adoption.'),
('(proposed OPEN-OFN-TRIAD-CLASS)', '(OPEN-OFN-TRIAD-CLASS)'),
('#### 5.5.3 Proposed OFN local results', '#### 5.5.3 OFN local results'),
('OFN custody proposed]', 'OFN custody]', 2),
('until adoption it remains OFN SESSION.', 'it is registered under OFN custody by the v0.10 adoption.'),
('*v0.10 Draft 1:* the twenty identities and statuses above are unchanged. One new record, OPEN-OFN-TRIAD-CLASS, is proposed (O10-P6) at the end of this registry; it becomes a registered identity only on adoption.',
 '*v0.10:* the twenty identities and statuses above are unchanged. One new record, OPEN-OFN-TRIAD-CLASS, is registered (O10-P6) at the end of this registry; the registry now holds twenty-one records.'),
('Reconciliation input (v0.10 Draft 1)', 'Reconciliation input (v0.10)', 3),
('RTG-OFN-ALG-RAW-STANDARD-C-NOGO (proposed) excludes', 'RTG-OFN-ALG-RAW-STANDARD-C-NOGO excludes'),
('the proposed Q5 (§5.5.2)', 'Q5 (§5.5.2)'),
('*(proposed v0.10; not registered before adoption)*', '*(registered by the v0.10 adoption, 19 October 2026)*'),
('Status: ACTIVE (proposed) |', 'Status: ACTIVE |'),
('Next required artifact or decision: PI decision on this record; then an RRF readout contract.', 'Next required artifact or decision: an RRF readout contract.'),
('### 11.4 v0.10 Draft 1 Claim-Level Imports (proposed)', '### 11.4 v0.10 Claim-Level Imports'),
('### 11.5 v0.10 Draft 1 Reference-Only Records (proposed)', '### 11.5 v0.10 Reference-Only Records'),
('The corollary stays OFN-derived and OFN-registered on adoption.', 'The corollary is OFN-derived and registered under OFN custody by the v0.10 adoption.'),
('| *v0.10 Draft 1:* ', '| *v0.10:* ', 4),
('| *Proposed v0.10*, OFN definition | Registers on adoption (O10-P2) |', '| Registered v0.10, OFN definition | Registered 19 Oct 2026 (O10-P2) |'),
('| *Proposed v0.10*, OFN definition; order fixed by PI decision 18 Oct 2026 at session level | Registers on adoption (O10-P2) |', '| Registered v0.10, OFN definition; order fixed by PI decision 18 Oct 2026 | Registered 19 Oct 2026 (O10-P2) |'),
('| *Proposed v0.10*, OFN RESULT from ALG | Registers on adoption (O10-P4); OPEN-C19-L gap recorded |', '| Registered v0.10, OFN RESULT from ALG | Registered 19 Oct 2026 (O10-P4); OPEN-C19-L gap recorded |'),
('| *Proposed v0.10*, OFN RESULT from THM + ALG | Registers on adoption (O10-P4); Genesis erratum concurs |', '| Registered v0.10, OFN RESULT from THM + ALG | Registered 19 Oct 2026 (O10-P4); Genesis erratum concurs |'),
('| *Proposed v0.10*, OFN OPEN | Registers on adoption (O10-P6) |', '| Registered v0.10, OFN OPEN | Registered 19 Oct 2026 (O10-P6) |'),
('### 12.5 v0.10 Draft 1 Proposals and Assembly Record', '### 12.5 v0.10 Decisions and Assembly Record'),
('| Key | Proposal | Effect if adopted |', '| Key | Decision (adopted 19 Oct 2026) | Effect |'),
('### Proposed v0.10 records — Draft 1, 19 October 2026', '### Adopted v0.10 records — 19 October 2026'),
('**OFN10-C01 — FMS model-selection interface (proposed).**', '**OFN10-C01 — FMS model-selection interface (adopted 19 October 2026).**'),
]
for p in pairs:
    old, new = p[0], p[1]; c = p[2] if len(p) > 2 else 1
    rep(old, new, 'R02 ' + old[:28], c)
# R03 §12.5 adoption line
rep('Remaining: PI decisions on O10-P1–P7, individually or together, on the Draft 2 hash.',
    'Second co-owner final disposition on Draft 2: ACCEPT — OWNER ADOPTION READY. **PI adoption, 19 October 2026: O10-P1–P7 approved in full on Draft 2 (SHA-256 `58e2dec5…3610`).** The final file differs from Draft 2 only by the publication edits listed in the release record.', 'R03 §12.5 adoption')
# R04 Appendix C entry
rep('## Appendix C — Version History\n', '''## Appendix C — Version History

### v0.10 — 19 October 2026 — ADOPTED / FMS model-selection interface release

- **Authority and approved object:** adopted by Mustafa (PI) on 19 October 2026, approving O10-P1–P7 in full, on Draft 2 (SHA-256 `58e2dec54ad600dec189119adc16c8ca89872e74419f78ae317f33558a913610`) after both OFN co-owners accepted it; v0.10 supersedes v0.9 as the active OFN reference.
- **Finalization boundary:** header/adoption metadata, proposed→registered wording, this entry and the footer only (`release_ofn_v0_10.py`; list in the release record). No scientific statement, grade, scope or OPEN status differs from Draft 2.
- **Registered:** `RTG-OFN-DEF-TRIAD-MODEL-CONTRACT`, `RTG-OFN-DEF-STANDARD-C`, `RTG-OFN-ALG-RAW-STANDARD-C-NOGO`, `RTG-OFN-ALG-NARROW-Q6-PLANAR-PRODUCT`, `RTG-OFN-OPEN-TRIAD-CLASS`.
- **Unchanged open items:** OPEN-OFN-3B ACTIVE; DYAD OPEN 20 (existence of $J$); independent all-κ audit of FMS P4; physical carrier and ψ selection (OPEN-OFN-TRIAD-CLASS). O10-P7 notices N-O10-1–4 are issued with the release record.
''', 'R04 Appendix C')
# R05 footer
fi = s.index('*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.10 — DRAFT 2')
s = s[:fi] + '*END OF DOCUMENT — RTG_ONTOLOGICAL_FOUNDATIONS_v0.10*' + BR + '\n*ADOPTED 19 October 2026; active canonical OFN, superseding v0.9. Adds the FMS model-selection interface (§5.5); inherited definitions, OPEN statuses and technical custody are unchanged. Approved object: Draft 2, SHA-256 58e2dec5…3610.*\n'; log.append('R05 footer')
open(OUT, 'w', encoding='utf-8', newline='\n').write(s)
# checks
rid = lambda t: set(re.findall(r'RTG-OFN-[A-Z0-9-]+', t))
anc = lambda t: set(re.findall(r'<a id="([^"]+)"', t))
st = lambda t: [l for l in re.findall(r'^Status: .*$', t, re.M)]
v09 = open('RTG_ONTOLOGICAL_FOUNDATIONS_v0_9.md').read()
c1 = rid(d2) == rid(s); c2 = anc(d2) == anc(s)
sv, sf = st(v09), st(s)
c3 = all(l in sf for l in sv) and len(sf) == len(sv) + 1
leftover = [m.group(0) for m in re.finditer(r'.{0,40}(\[proposed|\(proposed\)|Proposed v0\.10|adoption pending).{0,20}', s)]
print('edits:', len(log)); print('RIDs same as Draft 2:', c1, '| anchors same:', c2, '| 20 v0.9 Status lines kept + 1 new:', c3, len(sf))
print('leftover proposal markers outside history:', leftover)
print('final sha256:', hashlib.sha256(s.encode()).hexdigest(), 'lines', s.count('\n'))
sys.exit(0 if (c1 and c2 and c3) else 1)
