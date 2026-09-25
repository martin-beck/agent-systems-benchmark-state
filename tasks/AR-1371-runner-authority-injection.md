---
{
  "branch": "feature/ar-1371-runner-authority-injection",
  "checkpoint_commit": "7c25e6ee94ff8d2efea5a3213e7f0285dc9a8ffb",
  "claim_expires": "",
  "depends_on": [
    "AR-1288"
  ],
  "id": "AR-1371",
  "next_action": "PR #271 merged as 3f0b67638647dc016f7d5abd3e246baf3ae4ec29 after all 12 exact-head checks passed. Seven post-merge workflows are running; monitor all to terminal success before releasing AR.",
  "observed_branch": "feature/ar-1371-runner-authority-injection",
  "observed_dirty": 0,
  "observed_head": "7c25e6ee94ff8d2efea5a3213e7f0285dc9a8ffb",
  "owner": "",
  "plan": "../plans/AR-1371-runner-authority-injection.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Inject existing authenticated certificate authority and runtime enrollment material into RunnerBackend/Catalog without synthetic authority.",
  "task_revision": 54,
  "title": "Runner authority injection",
  "updated_at": "2026-09-24T01:47:52+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1371-runner-authority-injection"
}
---

Replacement for blocked AR-1369 and planned AR-1370. Those audits found that
the current RunnerBackend/Catalog has no authenticated authority injection;
this task depends only on the completed AR-1288 issuer and must not synthesize
trust or launch authority from CLI/config input.

- 2026-09-24T00:58:24+00:00: Promote dependency-valid replacement for blocked AR-1369/1370;
  integrate completed AR-1288 issuer into RunnerBackend/Catalog.

- 2026-09-24T00:58:27+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:58:36+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:59:48+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T00:59:51+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-24T01:00:06+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T01:00:32+00:00: Recorded command exit 101; command argv SHA-256
  462f99fb6c13a94edf35bcd2beffd9d7ab45129bbf1e6a663c89769c174d0be5.

- 2026-09-24T01:00:49+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-24T01:01:04+00:00: Recorded command exit 0; command argv SHA-256
  462f99fb6c13a94edf35bcd2beffd9d7ab45129bbf1e6a663c89769c174d0be5.

- 2026-09-24T01:01:44+00:00: Recorded repair: first cargo check exited 101 on dead-code lint for the
  intentionally private issue_receipt seam. No gate weakening; added a narrow documented allow for
  the successor receipt operation, then reran fmt and cargo check successfully.

- 2026-09-24T01:02:11+00:00: Recorded command exit 0; command argv SHA-256
  d9fa5fa9d6b1edd0744be1b0aa7351347516f8475fbf10364d8f42e7873456ab.

- 2026-09-24T01:02:37+00:00: Recorded command exit 0; command argv SHA-256
  43d97a93f81a586e2fedc0be173d3aac708d94d483dc2a68a2260081af6a5c70.

- 2026-09-24T01:03:29+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T01:03:46+00:00: Recorded command exit 0; command argv SHA-256
  2ade5c66b9824bc07ed15f960bd197d95d86810e01ea897ea4782da4d022a751.

- 2026-09-24T01:04:31+00:00: Implementation checkpoint fb581f916970a1df99c20ae2a0f58f91d33420ff is
  SSH-signed+DCO. Added RuntimeAuthorityRecord persistence/validation and a digest-only
  CertificateAuthorityV1 recovery constructor; added a negative provider-mismatch/privacy test.
  Initial dead-code lint failure was repaired with a documented private seam annotation; focused
  gates now pass.

- 2026-09-24T01:05:17+00:00: Recorded command exit 0; command argv SHA-256
  12938f82fbaa9857db28f5434d0af3e082e02e4471a57c1807c2e82d77a69772.

- 2026-09-24T01:05:40+00:00: Recorded command exit 0; command argv SHA-256
  341e312c0532aa0e4f137a3f94aeabe37c46a8bbe85b57fa8e25dbf3ab2888c8.

- 2026-09-24T01:07:51+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T01:07:54+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-24T01:08:19+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T01:08:33+00:00: Recorded command exit 0; command argv SHA-256
  462f99fb6c13a94edf35bcd2beffd9d7ab45129bbf1e6a663c89769c174d0be5.

- 2026-09-24T01:08:51+00:00: Recorded command exit 0; command argv SHA-256
  43d97a93f81a586e2fedc0be173d3aac708d94d483dc2a68a2260081af6a5c70.

- 2026-09-24T01:09:06+00:00: Recorded command exit 0; command argv SHA-256
  d9fa5fa9d6b1edd0744be1b0aa7351347516f8475fbf10364d8f42e7873456ab.

- 2026-09-24T01:10:24+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T01:10:28+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T01:10:43+00:00: Recorded command exit 101; command argv SHA-256
  e07f3eaf900c636bb2287c116344ecffe6d7bcc46541b58551b1a488b7a8b0b7.

- 2026-09-24T01:11:11+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T01:11:26+00:00: Recorded command exit 0; command argv SHA-256
  e07f3eaf900c636bb2287c116344ecffe6d7bcc46541b58551b1a488b7a8b0b7.

- 2026-09-24T01:11:39+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T01:11:43+00:00: Recorded command exit 101; command argv SHA-256
  12938f82fbaa9857db28f5434d0af3e082e02e4471a57c1807c2e82d77a69772.

- 2026-09-24T01:12:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-24T01:12:56+00:00: Recorded command exit 0; command argv SHA-256
  12938f82fbaa9857db28f5434d0af3e082e02e4471a57c1807c2e82d77a69772.

- 2026-09-24T01:13:11+00:00: Recorded command exit 0; command argv SHA-256
  341e312c0532aa0e4f137a3f94aeabe37c46a8bbe85b57fa8e25dbf3ab2888c8.

- 2026-09-24T01:13:34+00:00: Recorded command exit 0; command argv SHA-256
  6120de36aaf3f41dd6cadb792c3fccfa2bc059e1af956c26b16aabbc0ee7bbd5.

- 2026-09-24T01:13:48+00:00: Recorded command exit 0; command argv SHA-256
  a6ccb937ebd0ce95c8f3f3e5db19cee75c645f587c125e35dcdbd6a993ea8404.

- 2026-09-24T01:14:29+00:00: Repaired full-gate exit 101 caused by test-only CertificateIdentityV1
  import at library scope; moved import into test module and reran full workspace tests and clippy
  successfully. Added restart recovery rejection for stale/revoked or mismatched persisted authority
  records; no credentials, paths, or synthetic authority cross boundary.

- 2026-09-24T01:14:44+00:00: Recorded command exit 0; command argv SHA-256
  19d1a051ae024c4c00fcfef6fc7a2f5fa5c3bfd0c1bf198586d67ce6c47ffc30.

- 2026-09-24T01:14:59+00:00: Recorded command exit 0; command argv SHA-256
  dccf804c123f55934178e5e5aadeff2532db3c2c666ebc242d3219bddfbc2091.

- 2026-09-24T01:15:13+00:00: Recorded command exit 8; command argv SHA-256
  7badf387284201e3fc92d2ab523310dc2541100eb9b953bb0c485767d1f314b5.

- 2026-09-24T01:15:56+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T01:16:00+00:00: Recorded command exit 8; command argv SHA-256
  7badf387284201e3fc92d2ab523310dc2541100eb9b953bb0c485767d1f314b5.

- 2026-09-24T01:16:13+00:00: Recorded hosted monitoring at 01:15:13Z: no failed checks; 2 passed and
  10 pending. The private install boundary is reachable only from RunnerBackend restart recovery,
  and it rejects absent/inactive enrollment, endpoint/credential/generation mismatch, invalid chain
  metadata, and revoked records.

- 2026-09-24T01:17:06+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T01:17:10+00:00: Recorded command exit 8; command argv SHA-256
  7badf387284201e3fc92d2ab523310dc2541100eb9b953bb0c485767d1f314b5.

- 2026-09-24T01:19:51+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T01:22:11+00:00: Heartbeat by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-24T01:23:30+00:00: Recorded command exit 0; command argv SHA-256
  cc92bd1752fb642b6572ec989bfb37a4f4d69ca558523c2a868ac6e487c24ecf.

- 2026-09-24T01:24:03+00:00: Protected merge completed through handoffctl. Post-merge workflows for
  exact merge 3f0b6763: Formal assurance, Repository quality, Hosted portability/native
  qualification, Fault assurance, Emulated aarch64, Rust verification in progress; Huawei MIT
  headers already green.

- 2026-09-24T01:47:52+00:00: PR #271 product merge 3f0b676 had all exact-head checks green but
  failed post-merge Repository quality for one-parent squash topology. AR-1372 corrected this with
  two-parent merge 265b936d and all seven post-merge workflows green; product behavior unchanged.

## Current development and CI qualification boundary

The mandatory development and CI qualification path for this AR is a deterministic
local provider/LLM mock (LiteLLM-compatible where practical), including hostile
negative tests and offline replay where applicable. External/live OpenRouter or
other provider reachability is optional supplementary evidence only; it is never a
completion, dependency-readiness, or CI gate. Production egress policy, credential
non-disclosure, runtime-owned authority, namespace/relay attestation, cancellation
and teardown, and fail-closed denial of unapproved external traffic remain required
contracts. Existing live-provider dependency edges describe production integration
ordering only and must not be used to block local qualification or to claim external
reachability.
