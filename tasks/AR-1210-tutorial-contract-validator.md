---
{
  "branch": "docs/ar-1210-tutorial-contract",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1210",
  "next_action": "Promote after review; define the versioned offline tutorial-step schema and ASB syntax validator.",
  "owner": "",
  "plan": "../plans/AR-1210.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Define offline tutorial steps and validate them against the ASB CLI grammar.",
  "task_revision": 1,
  "title": "Tutorial contract and syntax validator",
  "updated_at": "2026-09-15T00:00:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1210"
}
---

Implement the linked plan. This AR is syntax/contract infrastructure only: tutorial commands must
never execute in its CI job and no provider, credential, network, benchmark, or LLM connection may
be required.
