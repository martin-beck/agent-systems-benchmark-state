---
{
  "branch": "feature/ar1855-ar1850-metadata-schema-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T15:49:32+00:00",
  "depends_on": [],
  "id": "AR-1855",
  "next_action": "Merge PR #149 at exact reviewed head 7fc186e48b after green required checks, then verify exact-main schema, focused tests, and live doctor.",
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
  "task_revision": 12,
  "title": "Repair AR-1850 coordination metadata schema",
  "updated_at": "2026-10-13T13:58:29+00:00",
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

- 2026-10-13T13:50:35+00:00: Recorded command exit 0; command argv SHA-256
  a3f1eec401f2f0825b7582956feabd8dad3c2ccd409fc971e4eb153e9482ddc9.

- 2026-10-13T13:50:46+00:00: Recorded command exit 0; command argv SHA-256
  f0d4dd75ebf247b55c04c2ded5b6a0668783b547718ad99a62c8e1ab4d30d069.

- 2026-10-13T13:50:56+00:00: Recorded command exit 0; command argv SHA-256
  2cd28d97e950956062d7bc35b437a285760d806ec6319a9bedfa8d4e88a0c7bd.

- 2026-10-13T13:51:06+00:00: Recorded command exit 0; command argv SHA-256
  4f4b2b53231bbc9bfeec52a1798ac3bc0df3c69da42db14963dcd42b4c07993e.

- 2026-10-13T13:57:40+00:00: Recorded command exit 0; command argv SHA-256
  5764b6e0a77eb76d1a332ced5f0b73c6fd0abb42fd073ef12e800fc84ff1df62.

- 2026-10-13T13:58:02+00:00: Recorded command exit 0; command argv SHA-256
  8b872581a42f60c2dba01e615ff19183488db00eb5327c618f2b8a9893a63bed.

- 2026-10-13T13:58:19+00:00: Independent reviewer approved PR #149 exact head 7fc186e48b: six-line
  test typing/format-only diff; positive and hostile cases remain intact; no gate or product
  changes.

- 2026-10-13T13:58:29+00:00: Recorded command exit 0; command argv SHA-256
  0a6a0c0535f7d8d79b6f2347c65a28491e44dc4fb50c0122a5afc32c6be86fe4.
