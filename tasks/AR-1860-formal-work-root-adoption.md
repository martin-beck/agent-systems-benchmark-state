---
{
  "branch": "codex/ar1860-formal-work-root",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T18:56:43+00:00",
  "depends_on": [],
  "id": "AR-1860",
  "next_action": "Obtain independent review and exact-head CI for signed product repair; then merge and watch post-merge assurance before release.",
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
  "task_revision": 14,
  "title": "Dependency-safe formal work-root repair adoption",
  "updated_at": "2026-10-13T17:03:22+00:00",
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

- 2026-10-13T16:57:46+00:00: Portable-smoke formal gate passed at exact signed product head
  1f3c7f65ca; TLC completed with no error and handoffctl recorded terminal success.

- 2026-10-13T17:00:22+00:00: Recorded command exit 1; command argv SHA-256
  3a25f96e51b065e3f52ee81355fe3e625eb6cd2e735a0d508eea0bd4a4e0584b.

- 2026-10-13T17:03:09+00:00: Recorded command exit 0; command argv SHA-256
  022ea8a842fe1c1186950e1af2ff14e380232faa8796092449d4926946f69644.

- 2026-10-13T17:03:22+00:00: Full uv offline suite passed 1638/1638 in 159.067s at exact product
  HEAD 1f3c7f65ca. Initial system interpreter run failed only from missing jsonschema; no product
  failure. Portable-smoke formal passed; full hosted formal remains environment-gated by systemd-run
  admission.
