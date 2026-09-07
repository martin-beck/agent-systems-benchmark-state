---
{
  "branch": "feature/ci-artifact-quota-resilience",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T13:04:47+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0831"
  ],
  "id": "AR-0845",
  "next_action": "Make optional CI evidence quota-aware while preserving required-check semantics and provenance.",
  "observed_branch": "feature/ci-artifact-quota-resilience",
  "observed_dirty": 5,
  "observed_head": "b1669203308db5a75fee1e78a45c6fc8e71f17ce",
  "owner": "quality-20260906",
  "plan": "../plans/AR-0845.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent exhausted GitHub artifact quota from obscuring authoritative ASB results.",
  "task_revision": 9,
  "title": "Harden CI artifact quota behavior",
  "updated_at": "2026-09-07T11:41:55+00:00",
  "worktree_key": "agent-systems-benchmark-ci-artifact-quota-resilience"
}
---
## AR-0845

Make ASB CI distinguish required checks from optional artifact publication when GitHub artifact quota
is exhausted. Preserve test truth, provenance, privacy, and failure visibility; never turn a required
artifact or required check silently optional. Add quota detection, bounded diagnostics, fixtures, and
operator guidance.

- 2026-09-07T11:34:45+00:00: Dependencies AR-0003 and AR-0831 are durably done; declared
  branch/ref/worktree are absent. Promote only optional-artifact quota resilience; keep AR-0846
  planned behind AR-0845 and AR-0903.

- 2026-09-07T11:34:47+00:00: Claimed by quality-20260906.

- 2026-09-07T11:34:54+00:00: Recorded command exit 0; command argv SHA-256
  b99c4627ac0ef4cea44bffc0a740f529746ed2e6296605c5f4663fdbed9116b4.

- 2026-09-07T11:39:06+00:00: Recorded command exit 1; command argv SHA-256
  2e086b8b83af13e1d3333985e8b55b5d4bfbb90b0d89cbe5701ad393a564251a.

- 2026-09-07T11:40:03+00:00: Recorded command exit 0; command argv SHA-256
  3dd7f7357a238d20596efa9d08905c55d8f536d5f27602fd768b58d69baa9212.
