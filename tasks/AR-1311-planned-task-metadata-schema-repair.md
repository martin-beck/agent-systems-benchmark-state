---
{
  "branch": "repair/ar-1311-planned-task-metadata-schema",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T20:24:55+00:00",
  "depends_on": [],
  "id": "AR-1311",
  "next_action": "Claim this metadata-only repair, remove unsupported empty live-observation fields from planned AR-1309, regenerate views, and rerun schema and state gates. Do not alter AR-1309 meaning or claim implementation.",
  "owner": "codex-state-metadata-schema-20260918",
  "plan": "../plans/AR-1311.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair planned-task metadata that violates the current live-observation schema.",
  "task_revision": 2,
  "title": "Repair planned-task metadata schema contradiction",
  "updated_at": "2026-09-18T19:54:55+00:00",
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
