---
{
  "branch": "feature/ar-1468-control-authority-materialization-successor",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1288",
    "AR-1362",
    "AR-1364",
    "AR-1366"
  ],
  "id": "AR-1468",
  "next_action": "Promote and claim the corrected-dependency successor, then implement the owner-checked control authority materializer through the reviewed workflow.",
  "owner": "",
  "plan": "../plans/AR-1468-control-authority-materialization-successor.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Implement the control-owned authority materializer without the superseded AR-1369 dependency deadlock.",
  "task_revision": 2,
  "title": "Control authority materialization successor",
  "updated_at": "2026-09-26T22:44:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1468-control-authority-materialization-successor"
}
---

AR-1468 supersedes only the dependency wiring of AR-1370. It preserves the
historical AR-1369/1370 evidence and owns the implementation needed by the
runtime live-acquisition chain. Local/mock qualification is mandatory;
external provider access is optional and never a CI or completion requirement.

- 2026-09-26T22:44:37+00:00: Corrected successor depends only on completed authority foundations;
  begin implementation.
