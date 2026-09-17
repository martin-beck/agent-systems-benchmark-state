---
{
  "branch": "repair/ar-1298-narrow-metadata-repair",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1298",
  "next_action": "Restore unrelated task files to pre-AR-1297 bytes, retain only evidence-backed schema-failure repairs, regenerate views, and rerun all gates.",
  "observed_branch": "repair/ar-1298-narrow-metadata-repair",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1298.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Narrow AR-1297 metadata changes to the exact evidence-backed schema repairs.",
  "task_revision": 2,
  "title": "Narrow task metadata repair scope",
  "updated_at": "2026-09-17T05:35:13+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1298-metadata-cleanup"
}
---

## AR-1298

AR-1297 passed all validators but its commit normalized unrelated task files.
This cleanup owns only restoration of incidental changes and preservation of
the exact reported schema repairs. It must not rewrite history, weaken schema,
or touch product, asb-tui, handoffctl, or formal implementation.

- 2026-09-17T05:35:13+00:00: Independent review found incidental task rewrites in AR-1297; narrow
  scope before finalizing metadata publication.
