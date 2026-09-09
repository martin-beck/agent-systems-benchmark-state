---
{
  "branch": "feature/workbuddy-provenance",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0310",
    "AR-0315",
    "AR-0317",
    "AR-0503",
    "AR-0855"
  ],
  "id": "AR-0863",
  "next_action": "Pin official source, package, dependency closure, license, executable digest, protocol mode, and supported platform before any adapter claim.",
  "owner": "",
  "plan": "../plans/AR-0863.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Pin WorkBuddy source, package, and license provenance.",
  "task_revision": 2,
  "title": "Pin WorkBuddy source, package, and license provenance",
  "updated_at": "2026-09-09T03:14:56+00:00",
  "worktree_key": "agent-systems-benchmark-workbuddy-provenance"
}
---
## AR-0863

Pin official source, package, dependency closure, license, executable digest, protocol mode, and supported platform before any adapter claim.

This phase cannot claim support from mocks, parser fixtures, source inspection, compilation, or mutable artifacts. If its executable evidence is unavailable, leave this child blocked with exact provenance evidence while the sibling agent series proceeds.

- 2026-09-09T03:14:56+00:00: All eight dependencies are done; promote WorkBuddy provenance as the
  next highest-priority dependency-ready provider track.
