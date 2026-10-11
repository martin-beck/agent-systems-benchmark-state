---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-11T11:07:34+00:00",
  "depends_on": [
    "AR-1756"
  ],
  "id": "AR-1793",
  "next_action": "Add ASB-owned targeted tests until the strict 95 percent coverage gate passes, then independently review the exact candidate.",
  "owner": "codex-ar1793-awc-v051",
  "plan": "../plans/AR-1793-coordinator-v051-adoption.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt v0.5.1 with strict coverage repair.",
  "task_revision": 4,
  "title": "Coordinator v0.5.1 adoption",
  "updated_at": "2026-10-11T09:07:37+00:00",
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
