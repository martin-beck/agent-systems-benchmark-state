---
{
  "branch": "codex/ar1849-formal-admission-env-repair",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T13:11:59+00:00",
  "depends_on": [],
  "id": "AR-1849",
  "next_action": "Claim the repair, add workflow-wide private TLC admission variables and contract tests, then publish exact-head CI evidence before requalifying AR-1841.",
  "owner": "ar1849-formal-admission-env-luna",
  "plan": "../plans/AR-1849-formal-admission-env-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "mechanical",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1849.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1849.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair workflow-wide private TLC admission environment for formal CI.",
  "task_revision": 4,
  "title": "Formal admission environment repair",
  "updated_at": "2026-10-13T11:12:20+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1849-formal-admission-env"
}
---

The hosted formal workflow scopes `TLC_ADMISSION_QUEUE` and
`TLC_ADMISSION_LOCK` only to the model invocation. The subsequent full
unittest step therefore falls back to the root-owned `/tmp` lock and fails
before the runner tests can execute. Make the approved private paths job-wide,
retain absolute-path and privacy boundaries, and add regression coverage.

- 2026-10-13T11:10:00+00:00: Created as a narrowly scoped successor repair after PR #142 formal CI rejected AR-1841 on the unscoped admission lock.

- 2026-10-13T11:11:41+00:00: Promoted focused successor repair for workflow-wide private TLC
  admission environment.

- 2026-10-13T11:11:59+00:00: Claimed by ar1849-formal-admission-env-luna.

- 2026-10-13T11:12:20+00:00: Recorded command exit 0; command argv SHA-256
  fa8b5b71edf3200d321ee3c09e348eccd55c38732142f7ba47f3a35c7d1b1356.
