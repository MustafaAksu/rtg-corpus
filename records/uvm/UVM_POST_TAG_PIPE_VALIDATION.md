# UVM post-tag native pipe checks — 25 November 2026

Payload: f7bd089f19e4d3c98dc2da8ff6b2e6ef0e56eb09
Base: c7b7a3c149832bf06f66f2b7b2d68da7faab9e7d
Isolated Actions runner: 63df7c63797c01de53ea6026017abd5ddb7aec3c
Run: https://github.com/MustafaAksu/rtg-corpus/actions/runs/45584058742
Job: 139101027850

Native commands: python3 -I tools/pipes_index.py --selftest; python3 -I tools/pipes_index.py; python3 -I tools/pipes_index.py --check. DSN SHA-256 and tagged blob equality checked. git diff --quiet against base for dsn/, BASELINE.md, upload/, evidence/, tools/, and frozen UVM release record succeeded. The generated INDEX.md bytes were emitted in the run log and inserted via base64 blobs, not hand-edited.

2026-11-25T09:18:07.7016913Z dsn/RTG_OPEN_M_DSN.md: OK
2026-11-25T09:18:07.7475180Z ok   positive: valid open item — accepted
2026-11-25T09:18:07.7475938Z ok   positive: valid closed item with verdict and pointer — accepted
2026-11-25T09:18:07.7476730Z ok   positive: valid LIT finding to a stream — accepted
2026-11-25T09:18:07.7477509Z ok   positive: valid stream request to LIT — accepted
2026-11-25T09:18:07.7478028Z ok   positive: valid SAT request to LIT — accepted
2026-11-25T09:18:07.7478616Z ok   negative: unknown stream key — 20261026-NUMGEN-x.md: to='FOO' not a stream key
2026-11-25T09:18:07.7479687Z ok   negative: invalid state (notice vocabulary) — 20261026-NUMGEN-x.md: state='sent'
2026-11-25T09:18:07.7480570Z ok   negative: dispositioned without disposition — 20261026-NUMGEN-x.md: state dispositioned needs a disposition
2026-11-25T09:18:07.7481866Z ok   negative: disposition without verdict/pointer — 20261026-NUMGEN-x.md: disposition must read "YYYY-MM-DD · <verdict> · <pointer>" with verdict in ['accept', 'accept with change', 'reject', 'defer', 'no action']
2026-11-25T09:18:07.7483040Z ok   negative: disposition pointer missing — 20261026-NUMGEN-x.md: disposition pointer must name a records/dsn path or a RID
2026-11-25T09:18:07.7483902Z ok   negative: disposition present while open — 20261026-NUMGEN-x.md: a disposition is present but state is open
2026-11-25T09:18:07.7484722Z ok   negative: tag not in repository — 20261026-NUMGEN-x.md: tag tdrg-v9.9 does not exist in the repository
2026-11-25T09:18:07.7485546Z ok   negative: empty tag list — 20261026-NUMGEN-x.md: tags must name at least one repository tag
2026-11-25T09:18:07.7486562Z ok   negative: filed under wrong inbox — 20261026-NUMGEN-x.md: filed under DYAD/ but to=TDRG
2026-11-25T09:18:07.7487309Z ok   negative: filename FROM mismatch — 20261026-RECOG-x.md: filename FROM differs from front matter
2026-11-25T09:18:07.7488056Z ok   negative: filename date mismatch — 20261027-NUMGEN-x.md: filename date differs from date field
2026-11-25T09:18:07.7488963Z ok   negative: unknown field (second status axis) — 20261026-NUMGEN-x.md: unknown field notice_status
2026-11-25T09:18:07.7489868Z ok   negative: filed_by not a stream key — 20261026-NUMGEN-x.md: filed_by='Claude' not a stream key
2026-11-25T09:18:07.7490506Z ok   negative: empty body — 20261026-NUMGEN-x.md: empty body
2026-11-25T09:18:07.7491129Z ok   negative: empty repository tag list refused
2026-11-25T09:18:07.7491530Z RESULT: PASS (5 positive, 15 negative)
2026-11-25T09:18:07.8094063Z pipes OK: 177 items in 20 inboxes
2026-11-25T09:18:07.8696369Z pipes OK: 177 items in 20 inboxes
2026-11-25T09:18:09.1892644Z PASS native generation exactly ten derived INDEX.md files

Generated index SHA-256 values:
5f41e0d3c8507f9558c5d077fba72afc540b024499d7608a0000916975d1d80e  pipes/ATLAS/INDEX.md
cb693d06ede25961d5805e2108db1434ab8d9f83e40cf1f6019fcb7c7e76a359  pipes/AZ/INDEX.md
5a607d484635a206479b3dbefe32c26fd04aa213d2ee13ba3e3d70047d695ba4  pipes/DYAD/INDEX.md
6ebb609c6f240234b0defde4b6c30a6885cc5f44d85e80fab2ef5a20eb10a0dc  pipes/GEN/INDEX.md
3f722c11a96f6512e57d56f045ac79db9bddc059bb851ea6da7c7c0bfae9978d  pipes/OFN/INDEX.md
fa18e4efe5f35f2267156e46cd2a506b89da789d752437aac1b205c76706b03d  pipes/PREL/INDEX.md
6f58aaea1d3a461129bcd15a6adc19c5c6c9956e41004e1c3e8b4db1c692a7a3  pipes/PROG/INDEX.md
e827fa9d1e2b0f0831e3593e3bb8db0d2a092c6b623b65eeae9a062f3c35350e  pipes/RRF/INDEX.md
be37c0278248d2923208c1fe5d6829806d89355d5511c3b21de9d804070cd8fd  pipes/TRIAD/INDEX.md
da55f5eee34fa4e0840feb2d08c478c869e261ade82466196de54fa3ef94b1af  pipes/UVM/INDEX.md
