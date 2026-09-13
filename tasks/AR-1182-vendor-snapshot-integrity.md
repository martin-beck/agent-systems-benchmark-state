---
{
  "branch": "fix/coordinator-vendor-snapshot-integrity",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0851"
  ],
  "id": "AR-1182",
  "next_action": "Obtain a signed upstream release containing the lease-recovery fix, then sync and verify the complete immutable vendor snapshot without hand-editing files or weakening CI.",
  "owner": "",
  "plan": "../plans/AR-1182.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Restore exact coordinator vendor-lock integrity.",
  "task_revision": 1,
  "title": "Repair coordinator vendor integrity",
  "updated_at": "2026-09-13T20:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-coordinator-vendor-integrity"
}
---

## AR-1182

Restore a byte-exact, release-pinned coordinator snapshot after a downstream hotfix diverged from
the v0.3.5 lock. This is the infrastructure prerequisite for state PR #20 and later coordination
content; it does not authorize changing product or TUI code.

Current verification stops at `tools/handoffctl.py`: lock digest
`ccc2145c2d6345d93648566c66c79d9d1e7fe32a1ee2c52fd79e455220325f10` differs from checked-in
digest `8d9a4304de2f7d7a074508c2232a8853864f94c2a9c1ee0a1df06c4632dfca2f`.
