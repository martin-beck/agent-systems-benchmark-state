---
{
  "schema_version": 1,
  "id": "AR-1474",
  "title": "Runtime-owned authority-input resolver",
  "status": "planned",
  "priority": "P0",
  "summary": "Persist and resolve authenticated runtime authority inputs without caller-supplied or synthetic authority.",
  "next_action": "Promote after validating completed dependencies, then claim the isolated worktree and implement the bounded runtime-owned resolver.",
  "task_revision": 1,
  "updated_at": "2026-09-27T03:27:00+00:00",
  "owner": "",
  "claim_expires": "",
  "worktree_key": "agent-systems-benchmark-ar-1474-runtime-authority-input-resolver",
  "branch": "feature/ar-1474-runtime-authority-input-resolver",
  "checkpoint_commit": "",
  "plan": "../plans/AR-1474-runtime-authority-input-resolver.md",
  "depends_on": ["AR-1362", "AR-1471", "AR-1472", "AR-1379"]
}
---

Successor created from the AR-1473 protected-main audit. It owns the concrete
runtime/control persistence and resolution seam; it must not bypass existing
authority, privacy, lifecycle, formal, or egress contracts.

- 2026-09-27T03:27:00+00:00: Created after AR-1473 confirmed that no
  runtime-owned resolver exists for policy, target/tool, lease/relay,
  credential capability, namespace, cancellation, or teardown inputs.
