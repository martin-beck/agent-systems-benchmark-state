---
{
  "branch": "repair/ar-1749-coordinator-unblock-bootstrap",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T21:36:14+00:00",
  "depends_on": [],
  "id": "AR-1749",
  "next_action": "Adopt the exact reviewed Coordinator development vendor handoff on a claimable bootstrap AR, merge and verify it, then hand canonical unblock capability to blocked AR-1747.",
  "owner": "codex-asb-ar1749-vendor-bootstrap-20261008",
  "plan": "../plans/AR-1749-coordinator-unblock-bootstrap.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1749.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Bootstrap the reviewed Coordinator unblock and project evidence-policy vendor into ASB state without using an unreviewed topic-local lifecycle tool.",
  "task_revision": 16,
  "title": "Bootstrap canonical Coordinator unblock vendor adoption",
  "updated_at": "2026-10-08T18:45:21+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1749-coordinator-unblock-bootstrap"
}
---

AR-1747 is correctly blocked at revision 27 on canonical ASB-state main. The
installed v0.3.57 vendor does not expose `handoffctl unblock`, while the exact
reviewed upstream development handoff now does. Running a replacement tool from
an unmerged topic branch to mutate canonical lifecycle state would bypass the
reviewed vendor boundary; keeping AR-1747 blocked until its own tool merges is a
bootstrap cycle.

This dependency AR breaks that cycle through the normal claimable development
path. It adopts exact upstream Coordinator merge
`113dc61029f0e0c57bc7832e1e41430eafa17e73`, tree
`45ae6988ccd1c88230f262d735ff24d9d9b3bc4b`, and official development vendor
manifest SHA-256
`02149740b14a554d784e2f0fd8572a67dbf3faabe379fc39b4e9703de74e9936`.
It must preserve all vendored bytes exactly and add only bounded downstream-owned
compatibility repairs. After independent review, merge, and post-merge state CI,
canonical main may use its newly installed `unblock` command to reopen AR-1747.

This is development vendor adoption, not a release. Production authentication,
release signing, or a verified publication is not required. Exact identities,
privacy, schemas, formal closure, signatures, DCO, independent technical
review, hosted CI, and signed local integration remain mandatory.

- 2026-10-08T18:35:26+00:00: Promoted as the claimable reviewed bootstrap required to install
  canonical unblock and project evidence-policy support before blocked AR-1747 can resume.

- 2026-10-08T18:36:14+00:00: Claimed by codex-asb-ar1749-vendor-bootstrap-20261008.

- 2026-10-08T18:36:23+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-10-08T18:36:55+00:00: Recorded command exit 0; command argv SHA-256
  8224b337d3c97ceadaa502ba88ee88e87a102ec584a07a9f274d90c721bc3734.

- 2026-10-08T18:37:25+00:00: Recorded command exit 0; command argv SHA-256
  0ed28ab2d231d0b2bd8ef8fcc7c11bb59995fd48770e67cf2eb8a98065389117.

- 2026-10-08T18:38:00+00:00: Recorded command exit 0; command argv SHA-256
  b469340b3d2c95d64e1dcd4239499493e30817b9070e5b369d77803eea3f4e84.

- 2026-10-08T18:38:47+00:00: Recorded command exit 0; command argv SHA-256
  e58d8d6ab208993f137a551808e491b847fe6ecb17e34717b7cb33ef00fd88a6.

- 2026-10-08T18:40:05+00:00: Recorded command exit 0; command argv SHA-256
  445784d1998f3baea3c7d2c665983e93dc6495cd9ea819891c1ef45b467aa141.

- 2026-10-08T18:40:47+00:00: Recorded command exit 1; command argv SHA-256
  f76cbd34b54c6c91907a1f7951ff95d8587677b5750602eca1c0e923dd745f1c.

- 2026-10-08T18:41:43+00:00: Recorded command exit 0; command argv SHA-256
  54302719ae67021a7359012210c0a5bdea0c7ef0d67fbba86483bd5f0b75cc74.

- 2026-10-08T18:42:35+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-08T18:43:11+00:00: Recorded command exit 0; command argv SHA-256
  32a639b209a0b70bca326e8d672048305ea770f61751a054fad4148e4d4a21e9.

- 2026-10-08T18:43:53+00:00: Recorded command exit 0; command argv SHA-256
  569092f8be25fc784fe7f4a1099b3a3156d112e92e8908df14bcc7cdd7ced1f7.

- 2026-10-08T18:44:41+00:00: Recorded command exit 0; command argv SHA-256
  ba34fc07a45455f9f7b66d7d228395fd5fc0843ba5be4dfec6a6e2411be39f67.

- 2026-10-08T18:45:21+00:00: Recorded command exit 1; command argv SHA-256
  7d2c78bc54a2c5a71eb9d149dc10bcced35e74dfcc5074ace1b031b57952c571.
