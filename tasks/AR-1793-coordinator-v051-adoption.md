---
{"id":"AR-1793","title":"Coordinator v0.5.1 adoption","priority":"P0","depends_on":["AR-1756"],"plan":"../plans/AR-1793-coordinator-v051-adoption.md","summary":"Adopt the released Coordinator v0.5.1 snapshot in ASB state and restore all downstream quality gates without modifying vendored bytes.","status":"open","next_action":"Verify the released snapshot, complete ASB-owned compatibility and coverage repairs, then submit the isolated vendor adoption for review.","owner":"","claim_expires":"","checkpoint_commit":"","task_revision":1,"schema_version":1,"updated_at":"2026-10-11T00:00:00+00:00","branch":"","worktree_key":""}
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
