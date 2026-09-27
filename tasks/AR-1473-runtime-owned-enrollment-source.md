---
{
  "branch": "feature/ar-1473-runtime-owned-enrollment-source",
  "checkpoint_commit": "59323f41ed2d10a952a1276107459260ebdf409a",
  "claim_expires": "2026-09-27T12:56:22+00:00",
  "depends_on": [
    "AR-1471",
    "AR-1472",
    "AR-1379"
  ],
  "id": "AR-1473",
  "next_action": "Await AArch64 36314444926, Rust 36314444940, Repository quality 36314444954; all other five post-merge workflows SUCCESS. Release done after these three SUCCESS.",
  "observed_branch": "feature/ar-1473-runtime-owned-enrollment-source",
  "observed_dirty": 0,
  "observed_head": "4a29c3431d236cc9766c47408dab8de998a31a3b",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1473-runtime-owned-enrollment-source.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Resolve authenticated control enrollment into an opaque runtime-owned source for normal ASB run and sweep.",
  "task_revision": 46,
  "title": "Runtime-owned authenticated enrollment source",
  "updated_at": "2026-09-27T11:06:59+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1473-runtime-owned-enrollment-source"
}
---

Successor created from the AR-1470 and AR-1391 protected-main audits. It owns
only the missing runtime/control enrollment-to-source seam and must preserve
the existing fail-closed authority boundaries.

- 2026-09-27T03:23:00+00:00: Created after AR-1470 re-audit at protected main
  `1e2c5911` confirmed that certificate-chain storage and adapter integration
  exist but no runtime-owned enrollment operation populates the source used by
  normal `run`/`sweep`.

- 2026-09-27T03:23:34+00:00: Dependencies AR-1471, AR-1472, and AR-1379 are done at protected main;
  promote runtime-owned enrollment source successor.

- 2026-09-27T03:23:50+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T03:24:17+00:00: Recorded command exit 0; command argv SHA-256
  5c670d69ab763357b1a5368abe8f9729e0d00e33fbedd2be82f26a36c0aad7f5.

- 2026-09-27T03:25:25+00:00: Recorded command exit 0; command argv SHA-256
  5c65734e6538cf9e4793a7b2544e7ef4effba6047efc156c8474d0017efc7be6.

- 2026-09-27T03:25:56+00:00: Protected-main audit at 1e2c59119820bc073ea4c6736782f5041a395a28:
  existing AR-1471 receipt/chain validation and AR-1472 opaque adapter are present, but no
  runtime-owned enrollment source can resolve concrete policy/allowlist, lease/relay roots, pinned
  tools, credential capability, namespace, cancellation or teardown inputs.
  RuntimeCertificateChainStore::install and LiveProviderRuntimeBridge::request_control_receipt still
  require caller/runtime-provided stores; RuntimeAuthorityRecord persists only digest metadata.
  Normal CLI run/sweep remains fail-closed without an injected source. Focused cargo test --locked
  -p asb-runtime -p asb-cli passes all tests; no product/asb-tui/live-provider changes. Next action:
  coordinator must create a narrowly scoped private authority-source successor defining the owner
  and persistence of those bootstrap inputs before wiring normal dispatch; do not synthesize or
  expose authority.

- 2026-09-27T10:41:34+00:00: Dependencies AR-1471, AR-1472, and AR-1379 are now durably done; resume
  stale blocked AR-1473 for its existing narrow runtime-owned enrollment-source scope.

- 2026-09-27T10:41:40+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-27T10:41:52+00:00: Recorded command exit 0; command argv SHA-256
  0eea711e830e8f19bc1098a9cde6ce4c90ce0f0585016f0897c2fcc8baf356b8.

- 2026-09-27T10:42:14+00:00: Recorded command exit 0; command argv SHA-256
  b24e1452d90408fbeca79860cd9c189a296605391fbad89fe6d6492354892a4f.

- 2026-09-27T10:43:36+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:43:38+00:00: Re-audit after resume and refresh to protected main 5e577e6:
  AR-1471/1472/1379 are done; existing RuntimeAuthorityInputResolver persists digest-only metadata
  and fences owner/generation/cancel/teardown, but its profile-to-LiveProviderEnrollment source is
  not wired (materialize_handle_from_resolver remains dead-code and no source implementation
  exists). Scope remains implement the smallest private runtime-owned enrollment source; no caller
  authority or live provider.

- 2026-09-27T10:44:31+00:00: Recorded command exit 0; command argv SHA-256
  80f686c9e284663d0b87b5005cd228e41b5a79e718cd27a9a4001e8a688e0170.

- 2026-09-27T10:44:53+00:00: Recorded command exit 0; command argv SHA-256
  4b2493c1c487937f8a5629889017f5a1a88763d1c7a8f9253c68d146a69c8d59.

- 2026-09-27T10:45:16+00:00: Recorded command exit 0; command argv SHA-256
  8fb90a30a28d1aa7ceb89b0dadf0c82d82ec4515d3a70ed62ea775e9a620cdbc.

- 2026-09-27T10:46:00+00:00: Recorded command exit 101; command argv SHA-256
  134f5031c902fed628660ebc0b777565ef06679d617f64673d7f138365a103d9.

- 2026-09-27T10:46:45+00:00: Recorded command exit 0; command argv SHA-256
  593f2e290e2f46e223dd42eea080eaac227ba1ea00eb95442da9022770b01ed1.

- 2026-09-27T10:47:12+00:00: Recorded command exit 0; command argv SHA-256
  b91d1465ef337c801835bcff5ebce9d57e4bd823efb2d732bf0528eefeb788ea.

- 2026-09-27T10:47:39+00:00: Implemented smallest AR-1473 seam in
  crates/asb-runtime/src/live_service.rs: private RuntimeOwnedEnrollmentSource implements
  LiveProviderEnrollment over authenticated LiveProviderRuntimeAuthorityProfile +
  RuntimeAuthorityInputResolver, revalidating owner/generation/cancel/teardown before minting opaque
  handles. Added positive mint/revocation-negative and wrong-owner-negative tests. Focused tests and
  full 139-test asb-runtime suite pass (138 passed, 1 ignored); fmt and runtime clippy pass. Initial
  full runtime clippy exit 101 was new-source dead-code lint; fixed with scoped allowance matching
  existing private resolver. Signed SSH+DCO commit 4a29c3431d236cc9766c47408dab8de998a31a3b. No
  asb-tui/live-provider authority changes.

- 2026-09-27T10:50:48+00:00: Recorded command exit 0; command argv SHA-256
  93d9b153ca69f1ef9e0239282911bf620a82c296540d11205da622ee95b808ac.

- 2026-09-27T10:51:33+00:00: Recorded command exit 0; command argv SHA-256
  f2d44d52f550fa2792f69934b78ed1adeb45f7364e2ce0640b2220d66732940a.

- 2026-09-27T10:52:06+00:00: Independent diff review: one scoped file
  crates/asb-runtime/src/live_service.rs, 90 added lines; private RuntimeOwnedEnrollmentSource
  consumes only authenticated profile/resolver and emits opaque handle, revalidates
  owner/generation/cancel/teardown, has positive and two hostile tests. No asb-tui, CLI authority
  inputs, credentials, provider/network, or handoffctl changes. Full workspace tests, clippy,
  rustdoc, release build, fmt and diff checks exit 0. Clean SSH-signed+DCO head
  4a29c3431d236cc9766c47408dab8de998a31a3b.

- 2026-09-27T10:52:21+00:00: Recorded command exit 0; command argv SHA-256
  3e0210acaeb7e5620d1abd6cf023f880602991da7568cb915133c985a4d02d43.

- 2026-09-27T10:52:44+00:00: Recorded command exit 0; command argv SHA-256
  5fda3c1e9f6e4571e2a85aae86fb0eae97e5a9dc6bc91bf0eb3e96c4f872ffff.

- 2026-09-27T10:53:43+00:00: Recorded command exit 0; command argv SHA-256
  5fda3c1e9f6e4571e2a85aae86fb0eae97e5a9dc6bc91bf0eb3e96c4f872ffff.

- 2026-09-27T10:54:55+00:00: Recorded command exit 0; command argv SHA-256
  5fda3c1e9f6e4571e2a85aae86fb0eae97e5a9dc6bc91bf0eb3e96c4f872ffff.

- 2026-09-27T10:56:03+00:00: Recorded command exit 0; command argv SHA-256
  5fda3c1e9f6e4571e2a85aae86fb0eae97e5a9dc6bc91bf0eb3e96c4f872ffff.

- 2026-09-27T10:56:22+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-27T10:57:17+00:00: Recorded command exit 0; command argv SHA-256
  5fda3c1e9f6e4571e2a85aae86fb0eae97e5a9dc6bc91bf0eb3e96c4f872ffff.

- 2026-09-27T10:58:29+00:00: Recorded command exit 0; command argv SHA-256
  5fda3c1e9f6e4571e2a85aae86fb0eae97e5a9dc6bc91bf0eb3e96c4f872ffff.

- 2026-09-27T10:59:34+00:00: Recorded command exit 0; command argv SHA-256
  5fda3c1e9f6e4571e2a85aae86fb0eae97e5a9dc6bc91bf0eb3e96c4f872ffff.

- 2026-09-27T10:59:56+00:00: Recorded command exit 0; command argv SHA-256
  c2b6d9c031ca432ea77c701b280b564ce408727ade122cf5a4a551e20f649c96.

- 2026-09-27T11:01:20+00:00: Recorded command exit 0; command argv SHA-256
  ba5b564d3e42e1948fcd6ddcb67069284a40a822ba2bdff9e4dc39d953c4a76e.

- 2026-09-27T11:01:36+00:00: Recorded command exit 0; command argv SHA-256
  5fda3c1e9f6e4571e2a85aae86fb0eae97e5a9dc6bc91bf0eb3e96c4f872ffff.

- 2026-09-27T11:02:08+00:00: PR #356 exact head 4a29c3431d236cc9766c47408dab8de998a31a3b has all 13
  required checks terminal SUCCESS: AWQ, bounded fuzz, credential-free, Emulated AArch64, Huawei
  headers, Kani, Loom, mutation, platform, policy/coverage/supply-chain, retained faults, Rust, and
  TLC/Alloy. Independent review remains clean and scoped.

- 2026-09-27T11:02:21+00:00: Recorded command exit 0; command argv SHA-256
  85ab67987a6860787d942d9ff69022f91f8fbacb3f5e41924a58df59f29cc3ee.

- 2026-09-27T11:02:46+00:00: Recorded command exit 0; command argv SHA-256
  70c68eaec76c0a74d99fa54a5ae92a8d0e946cfec384add83146166562127260.

- 2026-09-27T11:03:53+00:00: Recorded command exit 0; command argv SHA-256
  70c68eaec76c0a74d99fa54a5ae92a8d0e946cfec384add83146166562127260.

- 2026-09-27T11:05:01+00:00: Recorded command exit 0; command argv SHA-256
  70c68eaec76c0a74d99fa54a5ae92a8d0e946cfec384add83146166562127260.

- 2026-09-27T11:06:12+00:00: Recorded command exit 0; command argv SHA-256
  70c68eaec76c0a74d99fa54a5ae92a8d0e946cfec384add83146166562127260.

- 2026-09-27T11:06:32+00:00: Recorded command exit 0; command argv SHA-256
  25c82a763f06acbe3882cc80e2d73d2ad0c6623cfb23ad84b87ef18a7c4bcad7.

- 2026-09-27T11:06:59+00:00: Post-merge exact-main job-level matrix at
  59323f41ed2d10a952a1276107459260ebdf409a: Credential-free 36314444913 SUCCESS; Huawei headers
  36314444973 SUCCESS; Formal 36314444936 SUCCESS; Hosted 36314444948 SUCCESS; Fault 36314444956
  SUCCESS. Pending: Emulated AArch64 36314444926 job in_progress; Rust 36314444940 job in_progress;
  Repository quality 36314444954 job in_progress. No failures.
