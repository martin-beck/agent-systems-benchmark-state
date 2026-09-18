---
{
  "branch": "repair/ar-1311-planned-task-metadata-schema",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1311",
  "next_action": "Claim this metadata-only repair, remove unsupported empty live-observation fields from planned AR-1309, regenerate views, and rerun schema and state gates. Do not alter AR-1309 meaning or claim implementation.",
  "owner": "",
  "plan": "../plans/AR-1311.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Repair planned-task metadata that violates the current live-observation schema.",
  "task_revision": 4,
  "title": "Repair planned-task metadata schema contradiction",
  "updated_at": "2026-09-18T19:55:35+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1311-planned-task-metadata-schema"
}
---
## AR-1311

The current task schema permits a planned task to have no checkout observation, but
AR-1309 carries `observed_head` as an empty string. The live schema rejects that
present-but-empty field. Remove only unsupported empty observation metadata, retain
AR-1309's empty checkpoint convention for planned work, regenerate views, and prove
the state gates without changing implementation claims or the schema contract.

- 2026-09-18T19:54:55+00:00: Claimed by codex-state-metadata-schema-20260918.

- 2026-09-18T19:55:19+00:00: Recorded command exit 0; command argv SHA-256
  9628f1ff118a9d6f79a735b5385258a1bdf4f79308b09e086e1a2f1b96c45ea6.

- 2026-09-18T19:55:35+00:00: Removed only unsupported empty live-observation fields from planned
  AR-1309 through handoffctl run; retained empty checkpoint convention and original meaning. Schema
  and generated-view checks pass.
