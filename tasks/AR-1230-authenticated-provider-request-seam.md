---
{
  "branch": "feature/ar-1230-authenticated-provider-request-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T21:17:30+00:00",
  "depends_on": [
    "AR-0319",
    "AR-0320",
    "AR-1100"
  ],
  "id": "AR-1230",
  "next_action": "PR #178 exact head 1f49831 requires independent re-review and CI. Seam schema/docs and unknown-field negative test now present; verify exact-head gates, then hand off to AR-1228 transport and AR-1229 application integration.",
  "observed_branch": "feature/ar-1230-authenticated-provider-request-seam",
  "observed_dirty": 2,
  "observed_head": "1f49831b291368bc01d6fba574bc0c0115a8224e",
  "owner": "asb_ar1230_auth_request_seam",
  "plan": "../plans/AR-1230.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Define the approved bounded provider authentication request and secret-injection seam.",
  "task_revision": 68,
  "title": "Authenticated provider-request seam and secret injection contract",
  "updated_at": "2026-09-15T19:18:14+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1230-authenticated-provider-request-seam"
}
---

Create the architecture contract required to turn qualified credential sources into authenticated
provider probes without exposing secret values to argv, ordinary environment, config, control
frames, logs, evidence or public state. This prerequisite owns the narrow seam and its security
proofs; AR-1228 owns concrete bounded provider transport and AR-1229 owns durable application
integration.

- 2026-09-15T18:40:00+00:00: Created after independent review found that the opaque credential
  resolver cannot safely support HTTP authentication without an approved provider-request seam.

- 2026-09-15T18:43:01+00:00: Dependencies AR-0319, AR-0320 and AR-1100 verified complete; promote
  authenticated provider-request seam prerequisite.

- 2026-09-15T18:43:15+00:00: Claimed by asb_ar1230_auth_request_seam.

- 2026-09-15T18:43:29+00:00: Recorded command exit 0; command argv SHA-256
  e95aa81c9bca865107c5e1bb46effcb4a6f91d4a8e4c8c04b85dccbe373d0147.

- 2026-09-15T18:43:39+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T18:47:16+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T18:47:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:47:39+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:47:53+00:00: Recorded command exit 101; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T18:48:10+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:48:21+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:48:31+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T18:49:15+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T18:49:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:49:29+00:00: Recorded command exit 101; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:50:05+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:50:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:50:23+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:50:33+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T18:50:52+00:00: Recorded command exit 0; command argv SHA-256
  d5d8ec2d971ee120c52a4cd53646d5f8f717cbf63ff5d3ee936f9b836bfef296.

- 2026-09-15T18:51:02+00:00: Recorded command exit 0; command argv SHA-256
  7115fedb28a347b6a358854c30345e8783e45160d8111ec428f8e5fd6a051424.

- 2026-09-15T18:51:14+00:00: Recorded command exit 0; command argv SHA-256
  987e0d9ac4e88d83cd62975832c181c3c798255f62859a22c4f44552b8cfc960.

- 2026-09-15T18:51:45+00:00: Implemented signed+DCO commit 5869e73. Added authenticated_request
  module with bounded typed metadata, endpoint identity validation, generation/timeout/response
  bounds, provider policy validation, opaque final-boundary header injection, credential wiping and
  sink-failure handling. Added negative endpoint/policy/timeout/empty-credential/sink tests. Focused
  authenticated_request tests: 2 passed; fmt and clippy -D warnings passed. Prior exit 101 was a
  moved-value test assertion, fixed by cloning request metadata; rerun passed.

- 2026-09-15T18:53:34+00:00: Recorded command exit 1; command argv SHA-256
  71dfaac7543cef9fb3f7b0cd58d8b68698acf268eeae2437c31b9dcab5de1a77.

- 2026-09-15T18:54:06+00:00: PR #178 exists at
  https://github.com/martin-beck/agent-systems-benchmark/pull/178 for exact head 5869e73. Draft
  creation command reported the existing PR, so no duplicate was created. Review/CI are now the next
  gates; branch remains clean and signed+DCO.

- 2026-09-15T18:57:38+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T18:57:42+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T18:57:54+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T18:58:04+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T18:58:15+00:00: Recorded command exit 0; command argv SHA-256
  f48cefb7cabe3c07fff244c663444bb3880fa4822367bcf3d9227ffb2d2e69e5.

- 2026-09-15T18:58:26+00:00: Recorded command exit 0; command argv SHA-256
  230ed3a15f3902ddd53faa483917276839f10dca41216f1d843412391b55b0f7.

- 2026-09-15T18:58:38+00:00: Recorded command exit 0; command argv SHA-256
  987e0d9ac4e88d83cd62975832c181c3c798255f62859a22c4f44552b8cfc960.

- 2026-09-15T18:59:03+00:00: Review findings addressed in signed+DCO d4a102f: injection now
  validates concrete endpoint identity and current generation, checks cancellation before/after
  sink, supports explicit Ollama no-auth policy, and rejects unsupported provider/policy
  combinations. Added endpoint mismatch, stale/cancelled, empty credential and sink failure tests.
  Focused tests 2 passed; fmt and clippy -D warnings passed. Pushed PR #178 update.

- 2026-09-15T19:02:44+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T19:02:47+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T19:03:01+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T19:03:10+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T19:03:31+00:00: Recorded command exit 0; command argv SHA-256
  f48cefb7cabe3c07fff244c663444bb3880fa4822367bcf3d9227ffb2d2e69e5.

- 2026-09-15T19:03:45+00:00: Recorded command exit 0; command argv SHA-256
  c895e6f749fd841a1f89f7c39f3e33936721eb3a74a8fe1f4d52db7f1adbcf28.

- 2026-09-15T19:03:57+00:00: Recorded command exit 0; command argv SHA-256
  987e0d9ac4e88d83cd62975832c181c3c798255f62859a22c4f44552b8cfc960.

- 2026-09-15T19:04:28+00:00: Review follow-up signed+DCO commit 2a74205 adds typed Cancellation
  trait (with closure compatibility), explicit Ollama no-auth policy, internal endpoint/generation
  checks during inject, cancellation checks before/after sink, and fail-closed tests. Focused tests
  2 passed; fmt and clippy -D warnings passed. Remaining transport deadline/response parsing and
  schema/application integration are explicitly delegated to AR-1228/AR-1229, not duplicated here.

- 2026-09-15T19:07:32+00:00: Recorded command exit 0; command argv SHA-256
  76de03f637b705a83f0ca0e766836de886f4155c7bbbde8aa8df5661f827d1c9.

- 2026-09-15T19:09:15+00:00: Recorded command exit 0; command argv SHA-256
  76de03f637b705a83f0ca0e766836de886f4155c7bbbde8aa8df5661f827d1c9.

- 2026-09-15T19:09:26+00:00: Recorded command exit 0; command argv SHA-256
  08607eeae74953e4c733ce953de6e047554b2f4d866144d6379d9b87afbce809.

- 2026-09-15T19:09:36+00:00: Recorded command exit 0; command argv SHA-256
  eaf2472e4b0ec29bac3303a6d46474c99be3c0ab077feca87b1c3650d4745e53.

- 2026-09-15T19:10:54+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T19:10:57+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T19:11:09+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T19:11:18+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T19:11:40+00:00: Recorded command exit 0; command argv SHA-256
  7a3d88c01c0f32ffd29dd350d05bcc908850b8ee901c1c720637f36195a38076.

- 2026-09-15T19:11:51+00:00: Recorded command exit 0; command argv SHA-256
  f0bf50ddfd1aabfbcdf33671055efeda1ff318ffe0e0923f45016d541767363c.

- 2026-09-15T19:12:03+00:00: Recorded command exit 0; command argv SHA-256
  987e0d9ac4e88d83cd62975832c181c3c798255f62859a22c4f44552b8cfc960.

- 2026-09-15T19:12:35+00:00: Added versioned authenticated-request JSON schema with
  additionalProperties false and public AUTHENTICATED_REQUEST.md documentation in signed+DCO commit
  1f49831. Added unknown-field negative test; focused authenticated_request tests: 3 passed; fmt and
  clippy -D warnings passed. Ownership plans corrected: AR-1228 transport only, AR-1229
  config/control/CLI only, AR-1230 seam only. PR #178 pushed to 1f49831.

- 2026-09-15T19:17:30+00:00: Heartbeat by asb_ar1230_auth_request_seam.

- 2026-09-15T19:17:33+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T19:17:45+00:00: Recorded command exit 0; command argv SHA-256
  c1e7039f75f0d249f1099a8ed9798935c71634c00dc669755dba2f34373ab2dd.

- 2026-09-15T19:17:57+00:00: Recorded command exit 0; command argv SHA-256
  4340dcbf253e5e20fd7f5355131da4428901f1f912a4e0ac816826265343c6b5.

- 2026-09-15T19:18:14+00:00: Recorded command exit 0; command argv SHA-256
  95a4ac9017df59d3b356a7333affeb775c5f5ee2d5e1c865450410bf1b8d23c8.
