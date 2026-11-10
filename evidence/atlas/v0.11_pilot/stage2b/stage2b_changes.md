# Stage 2b — the three corrected spans, verbatim

Base: stage-2a output `ace0b408def88c78291e7f26eaa8e358ade87205b738a9dcf8f7952a9818a5d6`. Candidate: `66f0b2ebdad84a578a7159d727c2d51d3831ebea15f18c07d9b17744173c20da`. 519,983 → 520,271 bytes.

## 1. L736 `RECOG-THM-A1B-SLIP-SCHEDULE-U`

**Base:**

```text
[assuming: Dyadic (D5) row-A bridge proof constants]
```

**Stage 2b:**

```text
[import: DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM (dyad-v6.4.23) and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS]
```

**Owner evidence (`recog-v0.3.27`):** RECOG-THM-A1C-SHARPENED-SCHEDULE: owner DSN line 764 carries [import: … DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM] and "the former (D5) qualifier is discharged, v0.3.27"

## 2. L740 `RECOG-RESULT-A1C-RECORD-PHASE-READOUT`

**Base:**

```text
; [assuming: (D5)];
```

**Stage 2b:**

```text
; [import: DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM (dyad-v6.4.23) and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS];
```

**Owner evidence (`recog-v0.3.27`):** RECOG-ALG-A1C-JOINT-CONTRACTOR: owner DSN line 1056 carries the same [import:] and "the former (D5) qualifier is discharged, v0.3.27"

## 3. L823 `RECOG-OPEN-EVENT-RULE`

**Base:**

```text
under the (D5) [assuming:] (RECOG-ALG-A1C-JOINT-CONTRACTOR)
```

**Stage 2b:**

```text
with the row-A remainder constants of DYAD-THM-LPHASE-ROWA-BRIDGE, DYAD-THM-OPEN3-SPIRAL-REM (dyad-v6.4.23) and RECOG-ALG-A1C-JET-REMAINDER-BOUNDS (RECOG-ALG-A1C-JOINT-CONTRACTOR)
```

**Owner evidence (`recog-v0.3.27`):** A1c-decoder sub-item: owner DSN line 180 "with the row-A remainder constants of the envelope (…; the former (D5) qualifier discharged at v0.3.27)"
