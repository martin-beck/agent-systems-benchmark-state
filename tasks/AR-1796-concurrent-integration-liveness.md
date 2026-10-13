---
{
  "branch": "policy/concurrent-integration-liveness",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-13T20:34:57+00:00",
  "claim_process": {
    "boot_digest": "sha256:7c78a2fd8557e03d4043618cb2c5f862fad89bf0143b18d8e2ebad9dc949c1b4",
    "pid": 1060249,
    "pid_namespace": "5:4026531836",
    "start_time": 4039008
  },
  "depends_on": [],
  "id": "AR-1796",
  "next_action": "Obtain fresh exact-head full-exhaustive formal attestation, then execute and verify the v0.5.2 release.",
  "observed_branch": "policy/concurrent-integration-liveness",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1796-liveness2-luna",
  "plan": "../plans/AR-1796-concurrent-integration-liveness.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Keep autonomous development live during concurrent protected-main integration.",
  "task_revision": 11,
  "title": "Concurrent integration liveness",
  "updated_at": "2026-10-13T19:34:57+00:00",
  "worktree_key": ""
}
---

Repair the policy that turns ordinary concurrent protected-main progress into
terminal worker blocking. Preserve exact merge-result assurance while ensuring
workers checkpoint, retry, and continue useful work during integration churn.

- 2026-10-11T12:25:29+00:00: Claimed by codex-ar1796-integration-liveness.

- 2026-10-11T12:30:01+00:00: Heartbeat by codex-ar1796-integration-liveness.

- 2026-10-11T12:32:25+00:00: Independent source audit rejected a naive post-unlock push: it can
  publish a concurrent head. The repair now requires durable candidate identity, serialized
  admission, remote-base fencing, post-push ancestry observation, and explicit ambiguous recovery.

- 2026-10-11T12:40:17+00:00: Implementation foundation now has candidate/key idempotency, publisher
  lease fencing, exact candidate observation, v3 migration, and a new publication model. Focused
  receipt tests pass. Canonical TLC queue is foreign-owned; isolated one-worker TLC cannot
  initialize a JVM because the host returns pthread_create EAGAIN before parsing.

- 2026-10-11T13:47:17+00:00: Heartbeat by codex-ar1796-integration-liveness.

- 2026-10-11T13:47:19+00:00: PR #1226 merged as 31a7e14; required CI, independent review, and
  canonical exact-head pr-fast attestation 38144510163 passed. Release remains pending the
  documented full-exhaustive gate.

- 2026-10-11T13:47:22+00:00: Implementation is merged and independently verified; hand off the
  release-only exact-head full-attestation step without treating it as a worker failure.

- 2026-10-11T13:48:19+00:00: Claimed by codex-ar1796-release-path.

- 2026-10-12T13:22:13+00:00: Expired release handoff has no live worker; return task to open for
  coordinator consistency.

- 2026-10-13T19:34:57+00:00: Claimed by codex-ar1796-liveness2-luna.
