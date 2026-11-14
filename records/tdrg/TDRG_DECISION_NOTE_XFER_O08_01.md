# TDR-G decision note — custody transfer XFER-O08-01 (OFN Finding A)

**[SESSION] NONCANONICAL. Decision support only: it changes no DSN text, RID or custody, and it is not a pipe item.**

**Prepared by** the TDR-G co-owner (Claude, session `claude01SKePJ`), 13 November 2026. This is the separate note on XFER-O08-01 asked for with the v2.13 cycle (PI, 13 Nov 2026, 12:07 +03:00).

**The co-owner's condition** comes from the ChatGPT co-owner's plan evaluation (12:06):
- the mathematical acceptance of Finding A and the transfer of its custody are separate questions;
- a transfer happens only with the explicit agreement of both owners and with proper records.

**Sources:**
- OFN `ofn-v0.12`: §4.1, `RTG-OFN-ALG-STAR-TOKEN-SHIFT`; §12; the import rows IMP-O08-*; the NUMGEN consumer row.
- TDR-G `tdrg-v2.12.15`: §7 import entry; SG-14; TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED.
- Methodology v1.4 §4.4 (RID lifecycle) and §13.3 (ownership transfer).

## 1. State

- **Statement.** Finding A (`RTG-OFN-ALG-STAR-TOKEN-SHIFT`, OFN `[RESULT]` `[from: ALG]`) concerns the common token shift $B_c:\delta_i\mapsto\delta_i+c$:
  - a fixed swap or path permutation commutes with $B_c$;
  - the star update commutes with it iff $2c\equiv0 \pmod N$.
- **Mathematical acceptance — done.** TDR-G accepted the statement on 27 Oct 2026, by one-line algebra on TDRG-DEF-STAR and `EV-CODE` against `blow_up_star_with_snapshot`. TDR-G imports it at `ofn-v0.12` and uses it in SG-14. TDRG-ALG-BIRTH-SPECTRUM-NOT-CLOSED also cites it.
- **Custody — open.** OFN offered the transfer XFER-O08-01. Both OFN v0.11/v0.12 and TDR-G v2.12.14/v2.12.15 record it as "deferred to TDR-G v2.13". The RID stays OFN's.
  - v2.13 is now a maintenance edition, and the PI placed custody outside it.
  - The v2.13 candidate therefore states custody as open, a separate decision of both owners (PR #265, edit E24).
  - OFN's text still reads "deferred to TDR-G v2.13". That becomes stale once v2.13 is adopted without a transfer, so OFN should be told (§4).
- **Other consumers.** NUMGEN v1.21 imports the same RID (OFN §12 consumer table). A transfer would change the owner its import points to.

## 2. What a transfer would involve (Methodology §§4.4, 13.3)

**The record.** It names:
- the old owner (OFN) and the new owner (TDR-G);
- the old location (OFN §4.1) and the new location (for example TDR-G §6.3, beside TDRG-DEF-STAR, or §6.13 with the token laws);
- the statement, stated as unchanged;
- the approval of both owners and the editions.

**The RID.** Methodology §4.4: "The original prefix may remain even after custody changes." So the RID can stay `RTG-OFN-ALG-STAR-TOKEN-SHIFT` under TDR-G custody. Alternatively TDR-G registers a `TDRG-…` RID with an exact alias mapping recorded by both owners. The retired ID is never recycled.

**The grade and wording.**
- OFN states the result as `[RESULT]` `[from: ALG]`. In TDR-G it would be an owner `[ALG]` block.
- Since v2.12.15, TDRG-DEF-STAR states a wider event domain (any single-star component). Finding A's algebra uses only the centre and newborn map, which is unchanged, so the statement carries over. A transfer review should still confirm that in writing.

**Edits on both sides.**
- **TDR-G:** a scientific edition, since it adds a claim block. The §7 import becomes owned text, and SG-14 points to the local block.
- **OFN:** a release that turns §4.1 into an import or pointer and updates §12.
- **NUMGEN:** a repin at its next edition (notice only).

## 3. Options

| # | Option | For | Against |
|---|---|---|---|
| X1 | **Transfer** to TDR-G (RID kept or aliased) | The statement is about TDR-G's own update rules. OFN's own scope says it "owns commitments and selection questions, not technical-owner results" (`ofn-v0.12` §0). TDR-G already checks and uses it; one owner per claim (Methodology §0.3). | Two coordinated releases plus a consumer repin; OFN loses a registered result that it also uses as an OPEN cross-reference (§9). |
| X2 | **Decline** the transfer by joint record; OFN keeps custody; TDR-G keeps importing | No edits beyond closing the offer; the import works today. | A technical result about TDR-G's rules stays owned outside TDR-G. |
| X3 | **Defer again** to a named later TDR-G edition | Keeps both options open. | "Deferred" has already outlived its target edition once. |

## 4. Recommendation (for the PI and both owners; nothing here is adopted)

**X1, done as a coordinated pair of later editions, not in v2.13.** The first step is a `request` item from TDR-G to `pipes/OFN/` that proposes:
- the terms: the RID kept with its OFN prefix, the location, the unchanged statement, and the domain check against the current TDRG-DEF-STAR;
- the order: OFN decides first, then the TDR-G scientific edition registers the block, then OFN's next edition points to it, then NUMGEN is notified.

OFN decides on the request, as for any pipe item. Whether X1, X2 or X3 is chosen, the post-v2.13 notice to OFN should say that the custody question is open and not tied to v2.13, so that OFN's "deferred to TDR-G v2.13" text can be corrected at its next edition.
