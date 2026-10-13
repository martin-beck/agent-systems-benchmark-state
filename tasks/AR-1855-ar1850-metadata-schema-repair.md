---
{
  "branch": "feature/ar1855-ar1850-metadata-schema-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T15:49:32+00:00",
  "depends_on": [],
  "id": "AR-1855",
  "next_action": "Validate the corrected AR-1850 coordination metadata against the published task schema, review the positive and hostile cases, and publish the state-only repair.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1855-metadata-schema-luna",
  "plan": "../plans/AR-1855-ar1850-metadata-schema-repair.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1855.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair the malformed observed_dirty coordination field on AR-1850 without changing its product scope.",
  "task_revision": 4,
  "title": "Repair AR-1850 coordination metadata schema",
  "updated_at": "2026-10-13T13:50:18+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1855-ar1850-metadata-schema-repair"
}
---

AR-1850 carries `observed_dirty: false`, but the current ASB task schema defines
that field as a non-negative integer dirty-entry count. Replace only that
malformed metadata with the semantically equivalent zero count. Preserve every
AR-1850 product requirement, owner, dependency, and launcher scope.

- 2026-10-13T00:00:00+00:00: Successor created to repair the AR-1850 task
  metadata without claiming or modifying the AR-1850 product implementation.

- 2026-10-13T13:49:32+00:00: Claimed by ar1855-metadata-schema-luna.

- 2026-10-13T13:49:51+00:00: Recorded command exit 0; command argv SHA-256
  2cd28d97e950956062d7bc35b437a285760d806ec6319a9bedfa8d4e88a0c7bd.

- 2026-10-13T13:50:18+00:00: Recorded command exit 0; command argv SHA-256
  8b872581a42f60c2dba01e615ff19183488db00eb5327c618f2b8a9893a63bed.
