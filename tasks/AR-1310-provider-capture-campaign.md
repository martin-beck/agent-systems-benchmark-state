---
{
  "branch": "feature/ar-1310-provider-capture-campaign",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T21:50:44+00:00",
  "depends_on": [
    "AR-1060",
    "AR-1151"
  ],
  "id": "AR-1310",
  "next_action": "Promote only after review confirms AR-1160 blocked evidence is preserved and the runtime capture design is dependency-ready; implement the provider-bound capture seam, durable tuple cassette coverage, restart reconciliation, and fail-closed offline activation.",
  "observed_branch": "feature/ar-1310-provider-capture-campaign",
  "observed_dirty": 4,
  "observed_head": "21b675e8119104ebbfec967454fabc2dfa0d632d",
  "owner": "ar1310-provider-capture",
  "plan": "../plans/AR-1310.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Runtime-owned provider capture and recording campaign qualification.",
  "task_revision": 23,
  "title": "Runtime-owned provider capture and recording campaign qualification",
  "updated_at": "2026-09-18T20:02:10+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1310-provider-capture-campaign"
}
---

# AR-1310: Runtime-owned provider capture and recording campaign qualification

AR-1160 delivered the renderer-neutral lifecycle protocol but is blocked because its
backend only changes aggregate recording state: it does not invoke the runtime-owned
authenticated capture seam, persist per-tuple cassette evidence, reconcile uncertain
provider effects, or establish an offline default from verified artifacts. This fresh
successor owns that missing ASB product work. It must not modify asb-tui, weaken any
native/formal/privacy gate, or treat path-supplied capture manifests as live provider
recording.

## Scope

- Add an authenticated runtime/provider launch callback that receives only the
  runtime-issued route and bounded request/response exchange, invokes the existing
  `StrictReplayService::capture_authenticated_connection` boundary, and prevents
  frontend-supplied endpoints, credentials, prompts, responses, or raw capture data
  from entering public control responses or durable state.
- Extend the durable campaign record with a bounded canonical tuple identity,
  attempt/generation fence, cassette digest and redaction/verification result for
  every selected agent/workload tuple. Persist intent before provider effects and
  reconcile interrupted `in_progress` tuples to `stale` without replaying uncertain
  paid work.
- Make execute/progress/reconcile/cancel idempotent and restart-safe, requiring
  exact provider profile, model, workload/scorer and runtime identity matches.
- Make offline-default activation possible only after every expected tuple has one
  current, authenticated, privacy-reviewed cassette and strict replay validation;
  reject duplicates, stale identities, missing digests, partial coverage and
  fabricated aggregate counters.
- Add renderer-neutral control schemas, generated-schema checks, positive and
  negative tests, bounded fixture cassettes, privacy scans and documentation.
  Keep the CLI path-based `record-campaign` importer separate and explicitly unable
  to authorize live campaign completion.

## Explicit non-scope

No asb-tui checkout or source changes; no new provider credentials or network
fallback; no weakening of exact-head CI, DCO/SSH signatures, coverage, formal,
platform, provenance or privacy gates; no edits to `handoffctl`.

## Dependencies

AR-1060 and AR-1151 remain complete prerequisites for the control and strict-replay
contracts. AR-1160 is a blocked implementation predecessor whose evidence and
protected-main baseline must be reviewed before promotion; this successor is scoped
independently so its promotion is not falsely implied by AR-1160 completion.

## Acceptance criteria

1. A real runtime-owned provider launch reaches the authenticated capture callback
   through the same call graph used by a campaign execute request; tests fail if the
   callback is bypassed or a frontend can supply a route/credential.
2. Every tuple has durable intent, in-progress, complete/failed/stale state and a
   content-addressed cassette metadata record; restart and duplicate/idempotency tests
   prove no uncertain provider request is repeated.
3. Complete coverage requires exact unique tuple identity, current generation,
   verified redaction and strict-replay cassette validation. Aggregate counts alone
   cannot satisfy the gate.
4. Offline-default activation succeeds only on complete current coverage and remains
   rejected for missing, duplicate, stale, malformed, privacy-failing or mismatched
   cassettes. Offline replay has no provider fallback.
5. Focused tests, full locked workspace gates, generated schemas, privacy scans,
   SSH-signed matching-DCO commits, independent immutable-head review, exact-head
   required CI and post-merge main workflows all pass. Durable evidence records
   exact commit, PR, CI run IDs, review, merge and post-merge results.

- 2026-09-18T19:50:38+00:00: Dependencies AR-1060 and AR-1151 are done; reviewed AR-1160 blocked
  evidence and protected-main baseline, promoting scoped runtime-owned capture successor without
  treating AR-1160 as complete.

- 2026-09-18T19:50:44+00:00: Claimed by ar1310-provider-capture.

- 2026-09-18T19:51:19+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-18T19:51:31+00:00: Recorded command exit 0; command argv SHA-256
  bf43ec402b013c87fb57a0b4068159ccc34f413e85b223c6730d0284340156ba.

- 2026-09-18T19:56:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T19:56:53+00:00: Recorded command exit 101; command argv SHA-256
  3245a656999a89261584f9836b9f14a677949b83542660656338485f93deb290.

- 2026-09-18T19:57:14+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T19:57:36+00:00: Recorded command exit 101; command argv SHA-256
  3245a656999a89261584f9836b9f14a677949b83542660656338485f93deb290.

- 2026-09-18T19:57:54+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T19:58:10+00:00: Recorded command exit 101; command argv SHA-256
  3245a656999a89261584f9836b9f14a677949b83542660656338485f93deb290.

- 2026-09-18T19:58:53+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T19:59:07+00:00: Recorded command exit 0; command argv SHA-256
  3245a656999a89261584f9836b9f14a677949b83542660656338485f93deb290.

- 2026-09-18T20:00:07+00:00: Implementation checkpoint: added runtime-owned ProviderCapture
  trait/request/result with fail-closed UnavailableProviderCapture; durable per-tuple coverage
  metadata and exact-matrix validation; execute now persists in_progress intent, invokes injected
  runtime callback, and durably records complete/failed outcomes. Corrected recorded exit-101
  compile errors (coverage previous Option type and moved campaign_id closure captures); focused
  lifecycle test now passes. Earlier exit-101 was compile failure, not silent retry; next run
  validates positive callback test and full gates.

- 2026-09-18T20:00:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T20:00:36+00:00: Recorded command exit 0; command argv SHA-256
  5756b7eeda2418e8e776d8aeb7945c70ec3dbeadda3f377c14f1c2c9f3482e7d.

- 2026-09-18T20:00:57+00:00: Recorded command exit 0; command argv SHA-256
  a2b5ac760ec7e9a9ed5550c92278b438b2e3f3350422ea5bbe0012152d013453.

- 2026-09-18T20:01:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T20:02:10+00:00: Recorded command exit 1; command argv SHA-256
  a17906f67ce357b0a31d56a1789a18edc8bd112f75438fa987842522f6a412a9.
