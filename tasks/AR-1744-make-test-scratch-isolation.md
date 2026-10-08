---
{
  "branch": "repair/ar-1744-make-test-scratch-isolation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T14:41:03+00:00",
  "depends_on": [],
  "id": "AR-1744",
  "next_action": "Reproduce the current-main make test failure and repair test scratch-root isolation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
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
  "task_revision": 3,
  "title": "Repair make test scratch-root isolation",
  "updated_at": "2026-10-08T12:41:03+00:00",
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
