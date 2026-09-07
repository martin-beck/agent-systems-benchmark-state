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
  "owner": "quality-20260906",
  "plan": "../plans/AR-0845.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent exhausted GitHub artifact quota from obscuring authoritative ASB results.",
  "task_revision": 3,
  "title": "Harden CI artifact quota behavior",
  "updated_at": "2026-09-07T11:34:47+00:00",
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
