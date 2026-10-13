---
{
  "branch": "codex/ar1860-formal-work-root",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T18:56:43+00:00",
  "depends_on": [],
  "id": "AR-1860",
  "next_action": "Promote and claim the dependency-safe repair adoption; bind the exact v0.7.0 formal worktree and qualify signed HEAD 1f3c7f65ca.",
  "owner": "ar1857-coverage-repair-luna",
  "plan": "../plans/AR-1860-formal-work-root-adoption.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "sha256:8ca60bdf6f6e4a4517b0867d74963d75cbffdf16e330c717dac8a8a13e53e1ab",
    "evidence_ref": "tests/test_workflow_triggers.py:1f3c7f65ca61e1e77fe4d357e37940ad8eddbe12",
    "spec_ref": "specs/AR-1860.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1860.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt and qualify the dependency-safe v0.7.0 formal work-root repair.",
  "task_revision": 10,
  "title": "Dependency-safe formal work-root repair adoption",
  "updated_at": "2026-10-13T16:57:32+00:00",
  "worktree_key": "asb-state-coordinator-v070-ar1860-formal-work-root"
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

- 2026-10-13T16:54:44+00:00: Bound worktree asb-state-coordinator-v070-ar1860-formal-work-root on
  branch codex/ar1860-formal-work-root.

- 2026-10-13T16:54:49+00:00: Recorded command exit 0; command argv SHA-256
  90ecad10f27de2ad22f04045e661d6d624c4b20f02482a0a797c15abc441b5da.

- 2026-10-13T16:55:16+00:00: Heartbeat by ar1857-coverage-repair-luna.

- 2026-10-13T16:56:43+00:00: Heartbeat by ar1857-coverage-repair-luna.

- 2026-10-13T16:56:48+00:00: Recorded command exit 0; command argv SHA-256
  90ecad10f27de2ad22f04045e661d6d624c4b20f02482a0a797c15abc441b5da.

- 2026-10-13T16:57:24+00:00: Exact signed product head passes six focused workflow tests, including
  all three hostile TLC_WORK_ROOT variants; rc64 guard remains before TLC/Java execution.

- 2026-10-13T16:57:32+00:00: Recorded command exit 0; command argv SHA-256
  404b2e7badf14e1b35bcf8ef2d52e0f0aec5407f78caeaa459702baa76d9bf8d.
