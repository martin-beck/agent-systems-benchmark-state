---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1388",
    "AR-1385",
    "AR-1373",
    "AR-1366",
    "AR-1341",
    "AR-1342",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1391",
  "next_action": "Promote after dependencies are verified, then bind an isolated worktree and implement the runtime/control-owned authenticated bootstrap constructor.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "0000000000000000000000000000000000000000",
  "owner": "",
  "plan": "../plans/AR-1391-runtime-control-bootstrap-constructor.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Materialize authenticated runtime live authority into an opaque source without caller injection.",
  "task_revision": 1,
  "title": "Runtime control bootstrap constructor",
  "updated_at": "2026-09-24T07:43:00+00:00",
  "worktree_key": ""
}
---

This narrow successor owns the missing authority source identified by the
AR-1390 audit. It must not touch asb-tui, synthesize authority, or require an
external provider connection for development or CI.
