---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T18:54:25+00:00",
  "depends_on": [],
  "id": "AR-1860",
  "next_action": "Promote and claim the dependency-safe repair adoption; bind the exact v0.7.0 formal worktree and qualify signed HEAD 1f3c7f65ca.",
  "owner": "ar1857-coverage-repair-luna",
  "plan": "../plans/AR-1860-formal-work-root-adoption.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "mechanical",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1860.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1860.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt and qualify the dependency-safe v0.7.0 formal work-root repair.",
  "task_revision": 3,
  "title": "Dependency-safe formal work-root repair adoption",
  "updated_at": "2026-10-13T16:54:25+00:00",
  "worktree_key": ""
}
---

Narrow successor for the formal work-root seam exposed by AR-1858. AR-1859
remains historical and intentionally unpromoted because it depends on unfinished
AR-1858. This task records that cycle, adopts the existing signed repair at
product HEAD 1f3c7f65ca61e1e77fe4d357e37940ad8eddbe12, and preserves the 95%
coverage floor and all formal gates.

- 2026-10-13T16:54:11+00:00: Dependencies verified: standalone successor records the AR-1858/1859
  cycle and adopts exact signed v0.7.0 repair head.

- 2026-10-13T16:54:25+00:00: Claimed by ar1857-coverage-repair-luna.
