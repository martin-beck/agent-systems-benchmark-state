---
{
  "branch": "feature/csb-execution-assurance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T09:08:42+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0104"
  ],
  "id": "AR-0603",
  "next_action": "Acquire and verify an exact public CSB source graph, then specify its bounded subprocess and containment contract.",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0603.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Pin and audit CSB provenance and prove a bounded sandboxed execution, cancellation, recovery, artifact, and privacy boundary.",
  "task_revision": 3,
  "title": "Establish pinned CSB execution and conformance boundary",
  "updated_at": "2026-09-07T06:08:42+00:00",
  "worktree_key": "agent-systems-benchmark-csb-execution-assurance"
}
---
## AR-0603

Pin and license-audit one exact public CSB revision and build graph, expose only a bounded
version-negotiated subprocess protocol, and prove containment, cancellation, recovery, artifact,
path, and privacy behavior before ASB may invoke CSB.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T06:07:58+00:00: Coordinator verified AR-0603 dependencies, ownership isolation, and
  user authorization; promote for contracts worker.

- 2026-09-07T06:08:42+00:00: Claimed by contracts-20260906.
