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
  "task_revision": 4,
  "title": "Bootstrap canonical Coordinator unblock vendor adoption",
  "updated_at": "2026-10-08T18:36:23+00:00",
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
