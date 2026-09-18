---
{
  "branch": "feature/ar-1310-provider-capture-campaign",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T22:10:22+00:00",
  "depends_on": [
    "AR-1060",
    "AR-1151"
  ],
  "id": "AR-1310",
  "next_action": "Promote only after review confirms AR-1160 blocked evidence is preserved and the runtime capture design is dependency-ready; implement the provider-bound capture seam, durable tuple cassette coverage, restart reconciliation, and fail-closed offline activation.",
  "observed_branch": "feature/ar-1310-provider-capture-campaign",
  "observed_dirty": 1,
  "observed_head": "75fe4b803d73cea3f7e3619dfdbc92f9e3dc3096",
  "owner": "ar1310-provider-capture",
  "plan": "../plans/AR-1310.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Runtime-owned provider capture and recording campaign qualification.",
  "task_revision": 47,
  "title": "Runtime-owned provider capture and recording campaign qualification",
  "updated_at": "2026-09-18T20:13:30+00:00",
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

- 2026-09-18T20:02:29+00:00: Recorded command exit 0; command argv SHA-256
  709b04646320a29049c036d1afb38f9ac62448a930148b63d961487a82b63b2c.

- 2026-09-18T20:02:45+00:00: Recorded command exit 0; command argv SHA-256
  63edc61d67f5d00dd45283ff8f7aebe6ddccd135ddeab266222713444254ab7e.

- 2026-09-18T20:03:04+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-18T20:03:28+00:00: Recorded command exit 0; command argv SHA-256
  3ef4cc9ad8371beabf92f1b879124cc1fa576afdc4bd18427e4094ca951d4d86.

- 2026-09-18T20:04:46+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T20:04:58+00:00: Recorded command exit 101; command argv SHA-256
  03e3afb3d0d86dfbcda0c8581df5c6db6e16afc6f3f1462066deb18e6c8270a9.

- 2026-09-18T20:05:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T20:05:32+00:00: Recorded command exit 0; command argv SHA-256
  03e3afb3d0d86dfbcda0c8581df5c6db6e16afc6f3f1462066deb18e6c8270a9.

- 2026-09-18T20:06:03+00:00: Recorded exit-101 diagnosis: new cassette conversion test passed
  Redactor::redact_contents() tuple directly to seal_cassette; compiler E0308 expected
  RedactedCassetteContents but received (RedactedCassetteContents, RedactionReport). Corrected by
  destructuring the redaction result; focused conversion test now passes, along with prior
  lifecycle/callback/restart tests and full asb-replay suite. No retry loop; next action is full
  locked workspace gates.

- 2026-09-18T20:06:47+00:00: Recorded command exit 0; command argv SHA-256
  681994a9b7b368ece8b133aae9b6f6ac982dd6a4869c3ca5fb59dcb9ad68604a.

- 2026-09-18T20:07:34+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-18T20:07:55+00:00: Recorded command exit 0; command argv SHA-256
  6309e5e05b44cd2f6204d35148f199077dfea79b6ef6f8e9c8c315edbd8c6ba9.

- 2026-09-18T20:08:36+00:00: Recorded command exit 0; command argv SHA-256
  75c4463fda736f04d1c1dd98b2fda9f27aa1920aa8b83710e8e18641e5d6f801.

- 2026-09-18T20:08:57+00:00: Recorded command exit 0; command argv SHA-256
  bdae844a239c001d402a9d4a0a44284802cf631f36f22f65f2c5780eceab07d2.

- 2026-09-18T20:09:09+00:00: Recorded command exit 0; command argv SHA-256
  11175cf7375ccd3bfbece73182a47faa43761567b2b57176130eb3ff39885b18.

- 2026-09-18T20:09:30+00:00: Recorded command exit 0; command argv SHA-256
  864336bc98df1adb7bace3da76535bbcb230b0a2cbcd1856119d0092c3eeb8d9.

- 2026-09-18T20:09:50+00:00: Recorded command exit 0; command argv SHA-256
  9c18c517ce76c987d419c979203097df99f24e6351405e00db318886079eeab7.

- 2026-09-18T20:10:22+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:12:55+00:00: Recorded command exit 0; command argv SHA-256
  e7aa0d9169621aa27b672bd55952da4005df3a0d6ff1ff60a949cb4a327269a6.

- 2026-09-18T20:13:12+00:00: Recorded command exit 0; command argv SHA-256
  3ef4cc9ad8371beabf92f1b879124cc1fa576afdc4bd18427e4094ca951d4d86.

- 2026-09-18T20:13:30+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.
