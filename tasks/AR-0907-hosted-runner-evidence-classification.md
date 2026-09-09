---
{
  "branch": "fix/hosted-runner-evidence-classification",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0702",
    "AR-0848"
  ],
  "id": "AR-0907",
  "next_action": "Add a closed hosted-portability schema and conditional workflow boundary while preserving exact native qualification and its 24.04.4 evidence.",
  "owner": "",
  "plan": "../plans/AR-0907.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Separate rolling hosted portability checks from immutable native qualification evidence.",
  "task_revision": 1,
  "title": "Classify hosted runner evidence without weakening native qualification",
  "updated_at": "2026-09-09T16:23:00+00:00",
  "worktree_key": "agent-systems-benchmark-hosted-runner-evidence"
}
---
## AR-0907

Repair the native-platform workflow boundary exposed by the rolling `ubuntu-24.04` hosted image.
Keep AR-0848's exact Ubuntu 24.04.4 native qualification immutable and fail closed while allowing
the hosted runner to report a separately named, non-qualification portability result when its
patch release has advanced.
