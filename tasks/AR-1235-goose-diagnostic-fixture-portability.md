---
{
  "branch": "feature/ar-1235-goose-fixture-portability",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0003"],
  "id": "AR-1235",
  "next_action": "Planned from post-merge AArch64 run 35060286408. Reproduce exit 127 in diagnostic_and_symlink_fail_closed, classify fixture/runtime cause, then add a deterministic portable fixture without weakening fail-closed assertions.",
  "owner": "",
  "plan": "../plans/AR-1235.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair Goose diagnostic fixture portability under emulated AArch64.",
  "task_revision": 1,
  "title": "Portable Goose diagnostic fixture",
  "updated_at": "2026-09-16T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1235"
}
---

## AR-1235

Created from post-merge exact-main AArch64 failure run 35060286408. The existing Goose negative
fixture unexpectedly returned a normal failed outcome with exit code 127, so the test did not reach
its intended diagnostic error assertion. Preserve the failure and repair the fixture portably.
