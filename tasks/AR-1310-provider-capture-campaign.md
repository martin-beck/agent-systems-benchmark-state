---
{
  "branch": "feature/ar-1310-provider-capture-campaign",
  "checkpoint_commit": "17a1530e620608a4d53b6d92ba48c642400778e2",
  "claim_expires": "2026-09-19T00:31:38+00:00",
  "depends_on": [
    "AR-1060",
    "AR-1151"
  ],
  "id": "AR-1310",
  "next_action": "Route DCO failure for pre-existing merge 909078c to a dedicated merge-integrity AR; separately rerun a supported exact-main post-merge Repository quality path that reports coverage. Local tree is 90.48%, but hosted run 35396621049 did not qualify. Keep AR-1312 blocked.",
  "observed_branch": "feature/ar-1310-provider-capture-campaign",
  "observed_dirty": 0,
  "observed_head": "9a2f313e86332e35eec40b97a692026b497d46cd",
  "owner": "ar1310_exactmain_rerun",
  "plan": "../plans/AR-1310.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Runtime-owned provider capture and recording campaign qualification.",
  "task_revision": 114,
  "title": "Runtime-owned provider capture and recording campaign qualification",
  "updated_at": "2026-09-18T23:02:04+00:00",
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

- 2026-09-18T20:14:13+00:00: Recorded command exit 0; command argv SHA-256
  681994a9b7b368ece8b133aae9b6f6ac982dd6a4869c3ca5fb59dcb9ad68604a.

- 2026-09-18T20:14:25+00:00: Recorded command exit 0; command argv SHA-256
  21a77d7af7a7773510d429c87f19419c70f74441be9b0231b553201f463fc995.

- 2026-09-18T20:14:37+00:00: Recorded command exit 0; command argv SHA-256
  749b4c6a2f62fa12777ddea8d29c6262b09e76d3d7b59068932ec40a61296d92.

- 2026-09-18T20:14:53+00:00: Recorded command exit 0; command argv SHA-256
  a21a7e60eee0efcd5f4353b04cf59f00fc7fb30606d66fa1af9ed484d7f5bd4a.

- 2026-09-18T20:15:16+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:15:38+00:00: PR #229 exact-head a6a3e43 was rejected by hosted Rust job 105745687544
  in run 35389941221 with E0369 at crates/asb-replay/src/service.rs:2015: assert_eq! compared
  Result<CassetteContents, ReplayError>, but ReplayError intentionally lacks PartialEq. Corrective
  action: changed the negative test to assert!(matches!(..., Err(ReplayError::InvalidHttp))),
  preserving the fail-closed API and avoiding an unnecessary public trait derivation. Focused
  negative test, cargo fmt check, workspace clippy -D warnings, and full cargo test --locked
  --workspace --offline pass. New commit is SSH-signed with DCO; push exact head and await required
  CI.

- 2026-09-18T20:16:28+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:18:21+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:19:51+00:00: PR #229 exact head a6a3e43 CI rerun is active. Green so far: platform,
  Kani, Loom, fault assurance subchecks, headers, AWQ shadow. Rust verification, repository quality,
  and emulated-aarch64 jobs remain queued in-progress without runners; no new failure is present.
  Continue monitoring exact-head CI; do not merge until all required checks are green and
  independent review is complete.

- 2026-09-18T20:21:37+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:22:32+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-18T20:22:49+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T20:23:03+00:00: Recorded command exit 0; command argv SHA-256
  e2886ebf03166eedddea518d6877d4aa2f8cd907aca062c27df9772900db7a25.

- 2026-09-18T20:23:20+00:00: Recorded command exit 0; command argv SHA-256
  3ef4cc9ad8371beabf92f1b879124cc1fa576afdc4bd18427e4094ca951d4d86.

- 2026-09-18T20:23:37+00:00: Recorded command exit 0; command argv SHA-256
  6120de36aaf3f41dd6cadb792c3fccfa2bc059e1af956c26b16aabbc0ee7bbd5.

- 2026-09-18T20:23:49+00:00: Recorded command exit 0; command argv SHA-256
  e413ffa35238f68131fa61b0df56ecf29197be112aaee02b8be8b9cfb7b89ce5.

- 2026-09-18T20:24:06+00:00: Recorded command exit 0; command argv SHA-256
  a21a7e60eee0efcd5f4353b04cf59f00fc7fb30606d66fa1af9ed484d7f5bd4a.

- 2026-09-18T20:24:24+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:24:33+00:00: Hosted policy gate on exact head a6a3e43 reported workspace line
  coverage 89.96% against the unchanged fail-under-lines=90 floor. This is a real coverage deficit,
  not a threshold/harness issue. Added runtime_capture_failures_remain_typed_and_fail_closed,
  exercising IdentityMismatch, Bounds, and Verification failure transitions and asserting
  failed/offline-ineligible durable records. Focused test and clippy pass; signed DCO commit 1625655
  pushed as new exact PR head. Re-run all required CI, including coverage, before merge.

- 2026-09-18T20:26:09+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:30:27+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-18T20:30:41+00:00: Recorded command exit 0; command argv SHA-256
  a95b132904994f14ac922782db993a78f70cec397d3e79836844c0bccd6ff7ed.

- 2026-09-18T20:30:54+00:00: Recorded command exit 0; command argv SHA-256
  3ef4cc9ad8371beabf92f1b879124cc1fa576afdc4bd18427e4094ca951d4d86.

- 2026-09-18T20:31:06+00:00: Recorded command exit 0; command argv SHA-256
  6120de36aaf3f41dd6cadb792c3fccfa2bc059e1af956c26b16aabbc0ee7bbd5.

- 2026-09-18T20:31:18+00:00: Recorded command exit 0; command argv SHA-256
  0283110e31b24c8b7ad0e1b8f6bc27068eaa4e8317264ab2fd9dd0eb75eba43d.

- 2026-09-18T20:31:35+00:00: Recorded command exit 0; command argv SHA-256
  a21a7e60eee0efcd5f4353b04cf59f00fc7fb30606d66fa1af9ed484d7f5bd4a.

- 2026-09-18T20:31:54+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:32:03+00:00: Policy rerun at exact head 1625655 improved workspace coverage from
  89.96% to 89.98% but remained below fail-under-lines=90. Added
  runtime_capture_rejects_unverified_or_malformed_results, exercising Ok(_) capture responses with
  redaction=false, replay=false, and malformed cassette digest; each durably fails the campaign
  closed with verification reason. Focused test, fmt, and workspace clippy pass. Signed DCO commit
  9a2f313 pushed as new PR head. Rerun all exact-head gates and inspect coverage result before
  merge.

- 2026-09-18T20:34:15+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:45:07+00:00: Recorded command exit 0; command argv SHA-256
  3dbe6c633e61546372355bc5a47e24dd9b880f8103ce2e983a8a29d57be4fdd3.

- 2026-09-18T20:46:18+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:49:22+00:00: Heartbeat by ar1310-provider-capture.

- 2026-09-18T20:49:30+00:00: Post-merge verification found a real required-gate failure; AR is not
  releasable yet. Main is exactly 17a1530e620608a4d53b6d92ba48c642400778e2 and PR #229 is merged,
  but post-merge Repository quality run 35393146183 failed Policy coverage: workspace line coverage
  89.99% (52,704 executed / 5,274 missed across 80,319 lines), below fail-under-lines=90. The
  post-merge Rust and emulated-aarch64 runs were still in progress at inspection; other completed
  post-merge workflows were green. Do not mark done or release until a follow-up coverage correction
  is merged and all exact-main required checks pass.

- 2026-09-18T20:51:27+00:00: Recorded command exit 0; command argv SHA-256
  d83d8458a410708d54dfb3a77946f2af231374c1ef035e70d60f21c1e02b7438.

- 2026-09-18T20:51:39+00:00: Recorded command exit 0; command argv SHA-256
  a2fe0ae1199ec0604768a96c2c2c8da495c28e42f3103500fd7015d6376f3625.

- 2026-09-18T20:51:52+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.

- 2026-09-18T20:52:05+00:00: AR-1310 implementation merged at
  17a1530e620608a4d53b6d92ba48c642400778e2, but required post-merge policy run 35393146183 failed
  the unchanged workspace coverage floor at 89.99% (52,704 executed, 5,274 missed of 80,319 lines).
  Exact blocker transferred to successor AR-1312 (durably recorded and dependency-linked); this AR
  is now blocked and ownerless pending successor correction and all-green exact-main post-merge
  checks.

- 2026-09-18T21:18:11+00:00: Coverage repair worker authorized to investigate and implement the
  post-merge 89.99% gate correction; preserve existing implementation evidence and do not weaken
  threshold.

- 2026-09-18T21:18:21+00:00: Claimed by ar1310-coverage-repair.

- 2026-09-18T21:19:13+00:00: Heartbeat by ar1310-coverage-repair.

- 2026-09-18T21:22:39+00:00: Recorded command exit 0; command argv SHA-256
  c94bd28b1048f8a1cca912fd8f67e3fd057de4b19098183e4422aa306e665090.

- 2026-09-18T21:23:38+00:00: Coverage rerun on exact merged tree passed locally: workspace 90.48%,
  critical packages 96.47%, all tests passed; no source diff needed. Keep blocked until hosted
  exact-main post-merge rerun proves 90% and all required workflows green; then promote AR-1312.

- 2026-09-18T21:24:27+00:00: Authorized bounded hosted exact-main rerun of Repository quality for
  merged commit 17a1530; no product changes or gate changes.

- 2026-09-18T21:24:30+00:00: Claimed by ar1310-coverage-repair.

- 2026-09-18T21:24:39+00:00: Recorded command exit 0; command argv SHA-256
  493276d5414104db09a78a144750702bd68d4b359a663ebfeb76e3a05bd61d5b.

- 2026-09-18T21:24:55+00:00: Recorded command exit 0; command argv SHA-256
  99c08617ba854e492585f3d50c6076b7808f84d08f1eb2603f6d7d5eea47f300.

- 2026-09-18T21:26:02+00:00: Heartbeat by ar1310-coverage-repair.

- 2026-09-18T21:26:05+00:00: Recorded command exit 0; command argv SHA-256
  c435e9db4536a232aea27856f0d7cf03c9720a9b2103947d5f91489628d5952c.

- 2026-09-18T21:26:45+00:00: Hosted exact-main dispatch 35396621049 targeted merge 17a1530 but
  failed two distinct gates: repository policy rejected pre-existing merge 909078c as lacking DCO,
  and therefore did not provide a passing hosted coverage result. Local exact-tree coverage is
  90.48% workspace/96.47% critical. No active DCO-repair AR owns this new merge-integrity finding;
  coordinator must route it separately. Keep AR-1310 and AR-1312 blocked; do not weaken policy or
  promote.

- 2026-09-18T21:27:15+00:00: Coordinator requested explicit next action after hosted rerun failure;
  no implementation retry.

- 2026-09-18T21:27:17+00:00: Claimed by ar1310-coverage-repair.

- 2026-09-18T21:27:20+00:00: Explicitly separated hosted policy/DCO failure from unresolved hosted
  coverage evidence; no gate weakening or product diff.

- 2026-09-18T21:27:23+00:00: Released ownerless after recording distinct DCO/policy and
  hosted-coverage blockers.

- 2026-09-18T22:05:29+00:00: Audit confirms no existing AR can own historical DCO defect
  909078ced21f36e5a72590c9decf41ac56452212: AR-1246/1247 are completed protected-main admission
  fixes and do not authorize history repair. Keep this follow-up blocked pending a separately
  authorized merge-integrity AR.

- 2026-09-18T22:05:39+00:00: Claimed by ar1310_followup_routing.

- 2026-09-18T22:06:05+00:00: Exact evidence: workflow 35396621049 on 17a1530 failed repository
  policy because 909078ced21f36e5a72590c9decf41ac56452212 lacks matching Signed-off-by; optional
  publication was skipped. Existing AR-1246/1247 are done and only fix protected-main
  admission/workflow behavior, so neither owns historical repair. No existing AR legitimately owns
  this repair; preserve blocker and keep AR-1312 dependency-blocked.

- 2026-09-18T23:01:35+00:00: Authorized bounded exact-main Repository quality rerun only; preserve
  historical 909078c DCO blocker and AR-1312 dependency.

- 2026-09-18T23:01:38+00:00: Claimed by ar1310_exactmain_rerun.

- 2026-09-18T23:01:47+00:00: Recorded command exit 0; command argv SHA-256
  493276d5414104db09a78a144750702bd68d4b359a663ebfeb76e3a05bd61d5b.

- 2026-09-18T23:02:04+00:00: Recorded command exit 0; command argv SHA-256
  22fb6eebf0a2e27fc56964e2f78bb25774bbb46ee2b30bde5322fbdf4aa98bf0.
