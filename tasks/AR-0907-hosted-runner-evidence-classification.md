---
{
  "branch": "fix/hosted-runner-evidence-classification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T19:25:36+00:00",
  "depends_on": [
    "AR-0702",
    "AR-0848"
  ],
  "id": "AR-0907",
  "next_action": "Add a closed hosted-portability schema and conditional workflow boundary while preserving exact native qualification and its 24.04.4 evidence.",
  "owner": "quality_20260906",
  "plan": "../plans/AR-0907.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Separate rolling hosted portability checks from immutable native qualification evidence.",
  "task_revision": 4,
  "title": "Classify hosted runner evidence without weakening native qualification",
  "updated_at": "2026-09-09T17:01:56+00:00",
  "worktree_key": "agent-systems-benchmark-hosted-runner-evidence"
}
---
## AR-0907

Repair the native-platform workflow boundary exposed by the rolling `ubuntu-24.04` hosted image.
Keep AR-0848's exact Ubuntu 24.04.4 native qualification immutable and fail closed while allowing
the hosted runner to report a separately named, non-qualification portability result when its
patch release has advanced.

- 2026-09-09T16:25:32+00:00: Dependencies AR-0702 and AR-0848 are done. The focused
  hosted-portability schema/workflow fence is disjoint from preserved AR-0877/AR-0906 candidates and
  keeps exact native qualification immutable.

- 2026-09-09T16:25:36+00:00: Claimed by quality_20260906.

- 2026-09-09T17:01:56+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.
