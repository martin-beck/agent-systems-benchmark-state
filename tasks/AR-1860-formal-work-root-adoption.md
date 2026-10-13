---
{
  "branch": "codex/ar1860-formal-work-root",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1860",
  "next_action": "Merge PR #151 signed state-only coordination repair, run exact-main doctor/schema/post-merge assurance, then release AR-1860 with merged evidence.",
  "owner": "",
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
  "status": "done",
  "summary": "Adopt and qualify the dependency-safe v0.7.0 formal work-root repair.",
  "task_revision": 21,
  "title": "Dependency-safe formal work-root repair adoption",
  "updated_at": "2026-10-13T17:19:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar1860-formal-work-root"
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

- 2026-10-13T17:04:43+00:00: Recorded command exit 0; command argv SHA-256
  5101bcf96d946f412ead54be400cc738e6fe3381146adc613efebe8f9fe375bc.

- 2026-10-13T17:04:57+00:00: Formal pr-publication gate passed terminally at exact product head
  1f3c7f65ca; every checked TLC model reported no error, including Handoffctl and recovery models.

- 2026-10-13T17:05:39+00:00: Exact-head review: 89/89 commits from origin/main are SSH-signed and
  carry DCO trailers; product worktree clean. Candidate branch pushed to origin for PR publication.

- 2026-10-13T17:10:39+00:00: Recorded command exit 0; command argv SHA-256
  6ec39729fa000aadc6afbd94bbf0c1639087072caf2c16bc994e4a29e7da65d2.

- 2026-10-13T17:17:17+00:00: Independent review completed at PR #151 head b08db6f917: effective diff
  is one line, normalizing AR-1858 worktree_key to accepted unique
  agent-systems-benchmark-ar1858-coverage-v070; AR-1860 key was already present in base. No product
  changes. AWQ and strict CI green; PR mergeable.

- 2026-10-13T17:18:52+00:00: Recorded command exit 0; command argv SHA-256
  19ac5910013c638c6eee371b5fdc3ca9222859fb20824ba4b6e1adb94fa2b33b.

- 2026-10-13T17:19:12+00:00: Released after signed local merge
  462e40d4311534438cb7689334eb9dfcaa0f5d43 of PR #151; origin/main exact at 1473bb90bd. Doctor
  --live, render-status --check, validate_schema.py, and check_generated_views.py all passed.
  Post-merge exact product worktree c8cce18b81737872fd2f0ce47a6da8ab9dbc9fcb focused workflow
  triggers passed 6/6. Full 1638/1638 and formal qualification remain durably recorded; signed
  DCO/independent review/hosted CI evidence retained.
