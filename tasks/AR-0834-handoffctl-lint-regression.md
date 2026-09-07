---
{
  "branch": "fix/handoffctl-apply-resume-lint",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T09:09:10+00:00",
  "depends_on": [
    "AR-0002",
    "AR-0830"
  ],
  "id": "AR-0834",
  "next_action": "Repair the unused apply_resume tasks parameter and prove handoffctl focused/full quality checks remain green.",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0834.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair the coordination-tool Ruff regression discovered during AR-0830 reconciliation.",
  "task_revision": 7,
  "title": "Repair handoffctl lint regression",
  "updated_at": "2026-09-07T07:11:51+00:00",
  "worktree_key": "agent-systems-benchmark-coordination-lint-regression"
}
---
## AR-0834

Repair the pre-existing Ruff unused-argument regression in `apply_resume` without changing
handoffctl behavior or weakening lint policy.

Acceptance criteria:

- Make the smallest behavior-preserving source change.
- Add or retain a regression test proving resume semantics and argument handling.
- Run focused tests, Ruff, mypy, full state validation, and live doctor.
- Commit with SSH signature and DCO; independently review the exact immutable head.

- 2026-09-07T07:09:08+00:00: AR-0002 and AR-0830 are done; the lint defect is reproduced at
  handoffctl.py:693, paths are isolated to coordination tooling/tests, and no active worker owns
  them.

- 2026-09-07T07:09:10+00:00: Claimed by contracts-20260906.

- 2026-09-07T07:09:53+00:00: Recorded command exit 0; command argv SHA-256
  38aa8a359afcc810ed2439f948965789057025369b5db49c6004df4cb1498745.

- 2026-09-07T07:11:26+00:00: Recorded command exit 0; command argv SHA-256
  875997ae4b3248d2c736284814636a82bbf3a04ea95c2d1675cff718c05b4fa8.

- 2026-09-07T07:11:38+00:00: Recorded command exit 2; command argv SHA-256
  b74c1485e8f8218ecfa5c72a8def2f786f2a7bdafc8d567f2a9e93a0043e9773.

- 2026-09-07T07:11:51+00:00: Recorded command exit 0; command argv SHA-256
  45e1698bec07062cb73fba1feff59930bd05e7f13f5d25d9d15c5b0c36fa7e30.
