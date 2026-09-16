---
{
  "branch": "docs/ar-1210-tutorial-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T05:38:15+00:00",
  "depends_on": [],
  "id": "AR-1210",
  "next_action": "Promote after review; define the versioned offline tutorial-step schema and ASB syntax validator.",
  "owner": "asb_ar1210_tutorial_contract",
  "plan": "../plans/AR-1210.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define offline tutorial steps and validate them against the ASB CLI grammar.",
  "task_revision": 3,
  "title": "Tutorial contract and syntax validator",
  "updated_at": "2026-09-16T03:38:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1210"
}
---

Implement the linked plan. This AR is syntax/contract infrastructure only: tutorial commands must
never execute in its CI job and no provider, credential, network, benchmark, or LLM connection may
be required.

- 2026-09-16T03:37:51+00:00: Dependencies are empty; complete AR and plan reviewed; promote offline
  tutorial contract validator.

- 2026-09-16T03:38:15+00:00: Claimed by asb_ar1210_tutorial_contract.
