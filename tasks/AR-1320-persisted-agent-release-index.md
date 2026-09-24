---
{
  "branch": "feature/ar-1320-persisted-agent-release-index",
  "checkpoint_commit": "77571ff978b886e24d35e29c0febb553a90a2d65",
  "claim_expires": "2026-09-24T22:04:29+00:00",
  "depends_on": [
    "AR-1316"
  ],
  "id": "AR-1320",
  "next_action": "Continue with AR-1322 for the bounded signed local release-index source and verified closure promotion; persistence/restart/refresh fencing is merged.",
  "owner": "codex-ar1320-luna56",
  "plan": "../plans/AR-1320.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Persist and verify the ASB agent release index used by the setup wizard.",
  "task_revision": 10,
  "title": "Persisted authenticated agent release index",
  "updated_at": "2026-09-24T20:06:07+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1320-persisted-agent-release-index"
}
---

AR-1316 now publishes a truthful unavailable roster, but it is rebuilt in the
backend and does not yet persist a verified source snapshot across restart.
This AR owns the durable signed release-index and generation lifecycle needed
before any agent can become selectable.

- 2026-09-24T20:02:12+00:00: AR-1316 is durably done; promote the next setup/catalog AR for
  implementation.

- 2026-09-24T20:04:29+00:00: Claimed by codex-ar1320-luna56.

- 2026-09-24T20:04:48+00:00: Recorded command exit 0; command argv SHA-256
  498ccf248bc166cd8940e579a67ad12e0a07199783062cc3019459f7d310c063.

- 2026-09-24T20:05:21+00:00: Recorded command exit 0; command argv SHA-256
  f4abd2f9e2e254f6744cfc1db142170dec6bb1d20a66ac186cc4a74024b38d62.

- 2026-09-24T20:05:37+00:00: Recorded command exit 0; command argv SHA-256
  00470261f504532f2ea6775b2d6738887b5f75732f3a984770807beb880c321b.

- 2026-09-24T20:05:52+00:00: Recorded command exit 2; command argv SHA-256
  abae542d76af0b1098b080baf7adb60773eeb1ca61f6fcd047144c1bbf300c15.

- 2026-09-24T20:06:07+00:00: Recorded command exit 0; command argv SHA-256
  c74a5b2e0a8bdf6896b87e7bfb78dd6cf3363890501bd6ffc2839025615c055d.
