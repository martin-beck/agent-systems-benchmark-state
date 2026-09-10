---
{
  "branch": "test/capability-coverage-sink",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1023"],
  "id": "AR-1038",
  "next_action": "Preserve the validated external LLVM coverage sink across capability test env_clear without inheriting other ambient state.",
  "owner": "",
  "plan": "../plans/AR-1038.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Prevent sanitized capability child tests from writing default profraw files into the source checkout.",
  "task_revision": 1,
  "title": "Preserve coverage sinks in sanitized CLI child tests",
  "updated_at": "2026-09-10T22:58:00+00:00",
  "worktree_key": "agent-systems-benchmark-capability-coverage-sink"
}
---
## AR-1038

Fix the six `default_*.profraw` files discovered during AR-1013 full coverage without weakening
`env_clear()`. This is an ASB test-harness repair only and owns no standalone TUI or production UI.
