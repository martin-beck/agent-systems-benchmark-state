---
{
  "branch": "docs/ar-1214-record-replay",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1213"
  ],
  "id": "AR-1214",
  "next_action": "Implement the syntax-checked record/replay tutorial with synthetic cassette fixtures and no-network CI.",
  "owner": "",
  "plan": "../plans/AR-1214.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Teach privacy-safe LLM response recording and strict offline replay.",
  "task_revision": 2,
  "title": "LLM response record/replay tutorial",
  "updated_at": "2026-09-24T20:46:49+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1214"
}
---

Implement the linked tutorial and syntax/schema fixtures only; no provider or LLM connection is
permitted in its CI job.

- 2026-09-24T20:46:49+00:00: AR-1213 is durably released; promote the dependent record/replay
  tutorial.
