---
{
  "branch": "repair/ar-1744-make-test-scratch-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T14:41:03+00:00",
  "depends_on": [],
  "id": "AR-1744",
  "next_action": "Reproduce the current-main make test failure and repair test scratch-root isolation.",
  "observed_branch": "repair/ar-1744-make-test-scratch-isolation",
  "observed_dirty": 0,
  "observed_head": "2014f665be1ce30f63f171c93f996ae7606e74a1",
  "owner": "codex-ar1744-make-test",
  "plan": "../plans/AR-1744-make-test-scratch-isolation.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1744.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1744.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair make test failure caused by runtime scratch fixtures inheriting the Cargo target directory.",
  "task_revision": 23,
  "title": "Repair make test scratch-root isolation",
  "updated_at": "2026-10-08T12:52:11+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1744-make-test-scratch-isolation"
}
---

The current protected ASB main fails under `make test` because the Makefile
exports `CARGO_TARGET_DIR` into the test process while runtime scratch fixtures
derive their temporary roots from that variable. The resulting fixtures can be
created inside the repository Cargo target tree, violating the test contract
that scratch roots are external and private. The failure must be reproduced on
the exact main head, repaired without weakening path validation, and covered by
focused and full gates.

The repair must preserve the pinned toolchain, locked dependency/test path,
private bounded fixtures, cleanup guarantees, and all existing positive and
negative path checks. Add regression coverage for the Make invocation and the
named validated-linker environment test, update documentation only if needed,
and record exact PR, signature/DCO, CI, merge, and post-merge evidence.

- 2026-10-08T12:40:57+00:00: Dependencies verified; reproduce and repair current-main make test
  scratch isolation.

- 2026-10-08T12:41:03+00:00: Claimed by codex-ar1744-make-test.

- 2026-10-08T12:41:35+00:00: Recorded command exit 0; command argv SHA-256
  a014a10eb5dd4fa65cb2e51a89d085d13ae41eb5538833a58867e76d5d4ba18a.

- 2026-10-08T12:42:22+00:00: Recorded command exit 0; command argv SHA-256
  03006edd7c26ab149381fd8e64ec9685ed4567ae0f5d554c6aff520c8a67c503.

- 2026-10-08T12:43:09+00:00: Recorded command exit 0; command argv SHA-256
  ba6497e0660a2089fe8bb13f171c609310126866b1c97fc4fc731b7f2f5ffad4.

- 2026-10-08T12:43:41+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-10-08T12:44:52+00:00: Recorded command exit 0; command argv SHA-256
  f71975b0e0b00a780fed3410ff70f306b8004ce22f8d1aecc438b8adc79fe8e9.

- 2026-10-08T12:45:22+00:00: Recorded command exit 0; command argv SHA-256
  d0f198b9a45d38114b538f0cff6b253a9963ac66566cf5946a99d7c709f8a3b3.

- 2026-10-08T12:46:47+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T12:47:44+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-10-08T12:48:19+00:00: Recorded command exit 0; command argv SHA-256
  9a5585c26ae7ddbd2a1aa9e21b2c4b1a5d8a599f6e1b256c90d74782e7485a56.

- 2026-10-08T12:49:25+00:00: Recorded command exit 2; command argv SHA-256
  3fc122cf075789d0bc02db7fd32de1be63709d388a5a8cb44f03ddbc0ae0dfb6.

- 2026-10-08T12:50:23+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T12:51:25+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-10-08T12:51:49+00:00: Recorded command exit 0; command argv SHA-256
  bc586414bde2565f55afc62585428f4cf76392ef9881a202e1b65e0f44409086.
