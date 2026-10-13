---
{
  "branch": "policy/concurrent-integration-liveness",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1796",
  "next_action": "Reconcile the stale AR-1796 merge identity against current protected main, then obtain a fresh exact-head full-exhaustive formal attestation before any v0.5.2 release attempt.",
  "observed_branch": "policy/concurrent-integration-liveness",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1796-concurrent-integration-liveness.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Keep autonomous development live during concurrent protected-main integration.",
  "task_revision": 17,
  "title": "Concurrent integration liveness",
  "updated_at": "2026-10-13T20:32:07+00:00",
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

- 2026-10-13T19:35:05+00:00: Heartbeat by codex-ar1796-liveness2-luna.

- 2026-10-13T19:35:12+00:00: Exact live audit 2026-10-13: historical AR-1796 repair commit
  78b4cf216d is present but is not an ancestor of current origin/main 870331be533; recorded 31a7e14
  is absent; latest public release is asb-0.1.0-plan-output-ce190 and no v0.5.2/full-exhaustive
  attestation is present. Implementation/release cannot be marked complete until current-head
  identity and fresh attestation are reconciled.

- 2026-10-13T19:35:42+00:00: Bounded exact-state audit complete. Return ownerless/open with
  preserved next_action: reconcile stale AR-1796 merge identity against current protected main,
  obtain fresh exact-head full-exhaustive formal attestation, then reassess v0.5.2 release. No
  product or release gate changes made.

- 2026-10-13T20:31:25+00:00: Claimed by codex-ar1796-liveness2-luna.

- 2026-10-13T20:31:56+00:00: Live audit 2026-10-13: current protected remote main is
  870331be533ea1a0ba9645ddbb690df56af84935; historical AR-1796 repair merge
  78b4cf216d8159171c85c2229e59a163aa432833 is not an ancestor, and recorded 31a7e14 is absent.
  Public PR lookup reports historical PR #115 as merge 004d87252b065679d80ca9674356b47146754528, not
  78b4cf216d. No asb-0.5.2 tag or fresh full-exhaustive formal attestation is present. No
  product/release mutation is safe; next action remains reconcile current-head identity then obtain
  fresh exact-head full-exhaustive attestation.

- 2026-10-13T20:32:07+00:00: Blocked by verified stale merge identity and missing current-head exact
  formal evidence: 78b4cf216d is not ancestor of protected origin/main 870331be533; recorded 31a7e14
  absent; no asb-0.5.2 tag; no fresh full-exhaustive attestation. Next action: reconcile identity on
  current protected main, then obtain fresh exact-head full-exhaustive formal attestation before any
  v0.5.2 release attempt.
