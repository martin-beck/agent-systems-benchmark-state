---
{
  "branch": "feature/ar-1314-optional-bundle-signing",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-19T10:12:40+00:00",
  "depends_on": [],
  "id": "AR-1314",
  "next_action": "Wait for PR #232 exact-head CI after schema-v3 repair; if all required checks pass, independently review and merge through the established workflow, then reconcile AR-1314. Preserve signature-required defaults.",
  "observed_branch": "feature/ar-1314-optional-bundle-signing",
  "observed_dirty": 0,
  "observed_head": "dbfecb983e7d0592b958778419b58973e5397d5d",
  "owner": "ar1314_bundle_profile",
  "plan": "../plans/AR-1314.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Make runtime-bundle signatures optional only through an explicit, truthfully labelled development/release profile.",
  "task_revision": 68,
  "title": "Optional runtime-bundle signing for development and tagged releases",
  "updated_at": "2026-09-19T08:14:30+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1314-optional-bundle-signing"
}
---

# AR-1314

ASB development and tagged-release workflows must be able to publish a runtime bundle without a
detached bundle signature when explicitly selected. This does not remove commit/DCO integrity,
exact content digests, SBOMs, provenance, target checks, or release/tag verification. The default
installer/verifier remains signature-required; unsigned output must be opt-in, clearly labelled,
and rejected as formal qualification evidence.

The implementation must add versioned policy/profile metadata, positive and negative tests,
updated schemas/generated documentation, helpful failure messages, and an offline path. It must
not weaken AR-1307/AR-1308 full-exhaustive formal gates: those continue to require the exact
reviewed signed input bundle and terminal attestation.

- 2026-09-19T07:45:37+00:00: Dependencies are empty; promote explicit unsigned development/release
  profile implementation while preserving formal gates.

- 2026-09-19T07:46:29+00:00: Claimed by ar1314_bundle_profile.

- 2026-09-19T07:47:01+00:00: Recorded command exit 0; command argv SHA-256
  9ce28bbb59af15b4a34d9cab9cde7b29c5b76683dd446d280ae4b21f09407d2e.

- 2026-09-19T07:47:30+00:00: Recorded command exit 0; command argv SHA-256
  416936102312518bc032ec45a68736d742b34b9271d7a68688aaf99b9c8c3bf0.

- 2026-09-19T07:48:13+00:00: Recorded command exit 0; command argv SHA-256
  c4826fc3c54b3fad6bc5209245ff2566a6f53630576266e097eef91f8a96beef.

- 2026-09-19T07:50:32+00:00: Recorded command exit 101; command argv SHA-256
  7d8f9b35dbe47dc283e140e0f2c100bfc96671e55e1e272123a46160b04a26cd.

- 2026-09-19T07:50:51+00:00: Recorded command exit 101; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T07:51:14+00:00: Recorded command exit 0; command argv SHA-256
  5c2c153e2f434c40c78a037ecd2a0e260614332d83a927394666575b66c616a9.

- 2026-09-19T07:51:34+00:00: Recorded command exit 0; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T07:51:51+00:00: Focused cargo test first exited 101 because generated schema/v2 lagged
  the new profile/status fields; regenerated the checked schema and reran cargo test -p asb-bundle
  successfully (21 verifier, 2 schema, 4 unit tests). No product failure or gate weakening.

- 2026-09-19T07:53:30+00:00: Recorded command exit 0; command argv SHA-256
  d43baaf07b37e5983d58e89055f9e3b8e7d46904dbf7bcb4724239874b87409e.

- 2026-09-19T07:53:49+00:00: Recorded command exit 0; command argv SHA-256
  3ead084eabc4aa358936eebefbc35e828aadd8d496ece3d76bd51125cd9da724.

- 2026-09-19T07:55:41+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T07:55:51+00:00: The full focused cargo test reached terminal success: 4 unit, 21
  offline verifier, 2 schema-conformance, and 0 doctests passed. The handoffctl post-record then
  exited 101 with LOCK_TIMEOUT after 10s while acquiring the coordinator lock; this is coordination
  bookkeeping only, not a product test failure. Heartbeat renewed and retrying state update.

- 2026-09-19T07:56:27+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T07:56:30+00:00: Recorded command exit 0; command argv SHA-256
  d43baaf07b37e5983d58e89055f9e3b8e7d46904dbf7bcb4724239874b87409e.

- 2026-09-19T07:56:45+00:00: Recorded command exit 101; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T07:56:58+00:00: Recorded command exit 0; command argv SHA-256
  d43baaf07b37e5983d58e89055f9e3b8e7d46904dbf7bcb4724239874b87409e.

- 2026-09-19T07:57:16+00:00: Recorded command exit 0; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T07:57:42+00:00: Recorded command exit 0; command argv SHA-256
  2d322e3f6936159dcff6cb659168fcdf40d0225f6c4e837ce3423d8bab95826f.

- 2026-09-19T07:58:41+00:00: Recorded command exit 0; command argv SHA-256
  f09a28f66e1fc227b80abbbc9e6e5e4b1484e1d40abc5d88794ac34795421ba6.

- 2026-09-19T07:58:55+00:00: Recorded command exit 0; command argv SHA-256
  56fb97d1b57b6d2ecaf6cf411d05a2c24f7d68fbbd59787dbeaee309deb4b05a.

- 2026-09-19T07:59:08+00:00: Recorded command exit 0; command argv SHA-256
  c36844b605fe5b5fd40b0587c693d892f63c7362c39fa862241798db3f38845e.

- 2026-09-19T07:59:20+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T07:59:25+00:00: Recorded command exit 0; command argv SHA-256
  8438a032a6c6bac24f17c3e433686cd74544a799d5d2ba763711ef623191ebb5.

- 2026-09-19T07:59:39+00:00: Recorded command exit 0; command argv SHA-256
  ec24a9ce563aba80e4d135bc5e0fc2a3f69c94cd8fe02e952f066c1ce6d7f74a.

- 2026-09-19T07:59:53+00:00: Recorded command exit 8; command argv SHA-256
  67b214146cdfd6c1c5f6170b9a3386b06f161e916f48a3df7591b761eee501dd.

- 2026-09-19T08:00:29+00:00: Recorded command exit 1; command argv SHA-256
  67b214146cdfd6c1c5f6170b9a3386b06f161e916f48a3df7591b761eee501dd.

- 2026-09-19T08:00:46+00:00: Recorded command exit 0; command argv SHA-256
  e449d0960eaf4844f9248ffbe8e9d5048a5e181fe2660b470eaaeeac8b4e9b2d.

- 2026-09-19T08:01:01+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T08:01:13+00:00: PR #232 is published at exact signed+DCO head
  6fc467c12566e2738b1e0a5bb20fc9671944398d. Required policy run 35430794115 failed only because
  canonical contract consistency rejects the checked-in runtime-bundle schema/v2 change as an
  in-place v1 schema change (909078c boundary, pending AR-1313/PR-231 recovery). Preserve PR and
  wait; no merge or gate weakening authorized.

- 2026-09-19T08:05:26+00:00: Recorded command exit 0; command argv SHA-256
  b07c29c89007f687cab8bf5202948b9caa89cf36afaab3e41ab3f0c660d9f948.

- 2026-09-19T08:05:39+00:00: Recorded command exit 0; command argv SHA-256
  00fec45df73a1c1108d5cc91c5fc7ff8b4cb9cb0e6d7ae4be78ff5f40a5c1bb2.

- 2026-09-19T08:07:17+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T08:07:20+00:00: Recorded command exit 2; command argv SHA-256
  8d7a0da226d5f390ed23f1c8dd85c816f9f3b74f52339b05cd12265547734451.

- 2026-09-19T08:07:35+00:00: Recorded command exit 1; command argv SHA-256
  62f9e03c117c4e82ab80f6025adc1b390d3e258cda91c264758b5b2770379fec.

- 2026-09-19T08:07:48+00:00: Recorded command exit 0; command argv SHA-256
  6a3893d49b36580694ab784cf24c3ed65136cfc0f671d98e0dd9b6b71d579361.

- 2026-09-19T08:08:01+00:00: Recorded command exit 1; command argv SHA-256
  a496cffa5ec5beeabb7a500436291e149a222a1ed6ed47180b9c0f944949e839.

- 2026-09-19T08:08:47+00:00: Recorded command exit 0; command argv SHA-256
  6a3893d49b36580694ab784cf24c3ed65136cfc0f671d98e0dd9b6b71d579361.

- 2026-09-19T08:09:00+00:00: Recorded command exit 0; command argv SHA-256
  a496cffa5ec5beeabb7a500436291e149a222a1ed6ed47180b9c0f944949e839.

- 2026-09-19T08:09:38+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T08:09:47+00:00: Repair in progress: checked-in schema/v2 and fixture v1 are restored
  byte-for-byte to baseline 78a8e9f; new manifest schema version 2 is generated at schema/v3 with
  fixture v2, and contract catalog/registry now enrolls v3. The earlier contract gate exit 2 is
  explained: it correctly rejected the in-place v2 schema mutation. No gate was weakened.

- 2026-09-19T08:09:59+00:00: Recorded command exit 0; command argv SHA-256
  98b14edf2a525dfaacad74b297750831f9e57ed7549e2624c0a5420cc564f3e2.

- 2026-09-19T08:10:14+00:00: Recorded command exit 0; command argv SHA-256
  3ead084eabc4aa358936eebefbc35e828aadd8d496ece3d76bd51125cd9da724.

- 2026-09-19T08:10:28+00:00: Recorded command exit 0; command argv SHA-256
  2d322e3f6936159dcff6cb659168fcdf40d0225f6c4e837ce3423d8bab95826f.

- 2026-09-19T08:11:08+00:00: Recorded command exit 0; command argv SHA-256
  b794688388d11e29edc9eafc9af60bddce0eb903f7bff34a68fb6f092a8ba9e7.

- 2026-09-19T08:11:20+00:00: Recorded command exit 0; command argv SHA-256
  cee94ee818aec106fb1b52a9f303bb01405b73d5ebca20881fff78366b6dfde7.

- 2026-09-19T08:11:33+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T08:11:38+00:00: Recorded command exit 0; command argv SHA-256
  098910e1578d36efb36c35bd66079047ad4caa66775cbbd6f0d734be732afa5e.

- 2026-09-19T08:11:56+00:00: Schema-v3 repair committed and pushed as signed+DCO
  dbfecb983e7d0592b958778419b58973e5397d5d. Schema/v2 and fixture v1 match baseline 78a8e9f
  byte-for-byte; manifest schema version 2 is represented by schema/v3 and fixture v2. Contract
  consistency with baseline and all registered conformance commands passed; focused bundle tests
  (22), Python bundle tests (3), and clippy passed. PR #232 updated; awaiting exact-head CI.

- 2026-09-19T08:12:40+00:00: Heartbeat by ar1314_bundle_profile.

- 2026-09-19T08:12:51+00:00: Post-push monitoring query hit a transient handoffctl shared-lock
  timeout; heartbeat subsequently succeeded. No product or Git mutation occurred. Continue
  exact-head PR checks.

- 2026-09-19T08:12:58+00:00: Recorded command exit 8; command argv SHA-256
  67b214146cdfd6c1c5f6170b9a3386b06f161e916f48a3df7591b761eee501dd.

- 2026-09-19T08:13:41+00:00: Recorded command exit 8; command argv SHA-256
  67b214146cdfd6c1c5f6170b9a3386b06f161e916f48a3df7591b761eee501dd.

- 2026-09-19T08:14:30+00:00: Recorded command exit 8; command argv SHA-256
  67b214146cdfd6c1c5f6170b9a3386b06f161e916f48a3df7591b761eee501dd.
