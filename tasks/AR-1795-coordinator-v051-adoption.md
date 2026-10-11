---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1756"
  ],
  "id": "AR-1795",
  "next_action": "Retry canonical publication-tier formal verification after the occupied shared admission lane clears; then independently review the exact state and release only with all required evidence.",
  "owner": "",
  "plan": "../plans/AR-1795-coordinator-v051-adoption.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "hosted",
    "evidence_digest": "sha256:493bb6ee0f393cbb887c29b6f95d4ba2677dc86e5687c75334584d45cd4cde54",
    "evidence_ref": "quality/AR-1795-v051-adoption",
    "spec_ref": "specs/AR-1795.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1795.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Adopt v0.5.1 with strict coverage repair.",
  "task_revision": 9,
  "title": "Coordinator v0.5.1 adoption",
  "updated_at": "2026-10-11T12:24:46+00:00",
  "worktree_key": ""
}
---

Adopt the exact unsigned lightweight upstream release `v0.5.1` at
`7b19c0ffc8b37d0071d480cd666baef3f3672e35`. The release makes an exact,
still-authorized worktree-binding retry an idempotent no-op while retaining
fail-closed rejection for conflicting, stale, expired, partial, or unauthorized
requests.

The snapshot must be installed only through the upstream vendor tool and its
manifest verified byte-for-byte. ASB-owned compatibility adapters and tests may
be repaired for the removed legacy `authorized` gate field, but vendored bytes,
coverage thresholds, privacy policy, and generated-state integrity must not be
weakened.

- 2026-10-11T08:47:53+00:00: Claimed by codex-ar1793-awc-v051.

- 2026-10-11T09:07:34+00:00: Heartbeat by codex-ar1793-awc-v051.

- 2026-10-11T09:07:37+00:00: Isolated exact-candidate run passed 1574 tests; coverage is 93.83
  percent against the unchanged 95 percent threshold.

- 2026-10-11T11:14:19+00:00: Expired stale claim released; preserve coordinator adoption task for
  explicit reassignment.

- 2026-10-11T11:53:54+00:00: Claimed by codex-ar1795-v051-coverage.

- 2026-10-11T12:00:19+00:00: Fresh full branch coverage at state 70d7f9b: 95.0098 percent
  (15007/15628 statements; 5270/5714 branches). Vendor v0.5.1, schema, generated-view, and
  whitespace checks passed. Canonical formal verifier did not run because another process owns its
  shared admission queue.

- 2026-10-11T12:24:21+00:00: Hosted pr-publication formal workflow 38137857759 passed; full ASB
  suite passed 1627 tests at 95.0098 percent branch coverage. Vendor, schema, generated views,
  doctor, and independent reviews passed.

- 2026-10-11T12:24:46+00:00: v0.5.1 vendor adoption accepted after trusted pr-publication formal
  workflow 38137857759, 95.0098 percent coverage, vendor/schema/doctor checks, independent review,
  and exact-main contract-repair verification.
