---
{
  "branch": "feature/ar-1812-cli2key-ordinary-bootstrap",
  "checkpoint_commit": "5b71c956ea88788c3b303425331e0682c8dbc241",
  "claim_expires": "2026-10-12T13:32:58+00:00",
  "depends_on": [
    "AR-1779",
    "AR-1799",
    "AR-1813"
  ],
  "id": "AR-1812",
  "next_action": "Repair workspace gate failure: crates/asb-cli/tests/diagnostic_contract.rs rejects new lib.rs producer line identities after cli2key wiring; update the reviewed call-site identity contract (without weakening diagnostics), remove generated handoffctl __pycache__, rerun the failing test and full workspace gates.",
  "observed_branch": "feature/ar-1812-cli2key-ordinary-bootstrap",
  "observed_dirty": 0,
  "observed_head": "5c75c1a9fe36bb5f08c3cb4ccc20f213d496b65e",
  "owner": "ar1812-repair-luna56",
  "plan": "../plans/AR-1812-cli2key-ordinary-bootstrap.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1812.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1812.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Wire the verified cli2key installation and runtime authority into ordinary ASB run and sweep dispatch without fallback.",
  "task_revision": 46,
  "title": "Implement cli2key ordinary CLI bootstrap",
  "updated_at": "2026-10-12T11:32:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1812-cli2key-ordinary-bootstrap"
}
---

The ordinary ASB CLI currently has the AR-1799 authority seam and the AR-1779
installation contract, but no production adapter that resolves the verified
receipt and composes them for `run` and `sweep`. Implement that adapter with
strict identity checks, opaque authority retention, bounded teardown, and
typed no-fallback failures. Development qualification must use local/mock
fixtures and must not require a live provider or TLC.

- 2026-10-12T10:11:57+00:00: Promoted P0 prerequisite for AR-1810: wire verified AR-1779 cli2key
  receipt and AR-1799 opaque authority into ordinary run/sweep dispatch. Development path remains
  local/mock and non-TLC.

- 2026-10-12T10:12:04+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T10:12:22+00:00: Bound worktree
  agent-systems-benchmark-ar-1812-cli2key-ordinary-bootstrap on branch
  feature/ar-1812-cli2key-ordinary-bootstrap.

- 2026-10-12T10:13:24+00:00: Implementation audit found the requested seam cannot be implemented in
  asb-cli alone: Cli2KeyRuntimeAuthority::bootstrap requires a LiveProviderAttemptFactory, but
  production construction is private to asb-runtime and only injected test factories exist. AR-1779
  generic receipt has no runtime identity fields or bridge command contract. A local resolver
  without an opaque factory would fabricate authority or fallback, violating scope. No product
  changes retained; cargo check of exploratory resolver correctly failed closed under dead-code
  warnings.

- 2026-10-12T10:13:29+00:00: Blocked on missing production runtime API: asb-runtime must expose an
  opaque sidecar-backed LiveProviderAttemptFactory/source and AR-1779 must publish a verified
  runtime receipt contract. No safe asb-cli-only implementation exists; no fallback or fabricated
  authority used.

- 2026-10-12T11:09:26+00:00: AR-1813 is released done with runtime factory/receipt API, signed merge
  5c843a12 and verified exact-main gates; prerequisite is now satisfied. Reopen for ordinary CLI
  run/sweep integration.

- 2026-10-12T11:09:41+00:00: Claimed by ar1810-cli2key-luna56.

- 2026-10-12T11:09:48+00:00: Recorded command exit 0; command argv SHA-256
  0217f97b451c01319f8c5092fe792519a33fd1e7c07b7b0177f5c3b1db13a37d.

- 2026-10-12T11:09:52+00:00: Recorded command exit 0; command argv SHA-256
  cec9ac3df8e960560d557772da347f4f99305b0d06d797c609ff7c789cdc49f9.

- 2026-10-12T11:10:15+00:00: Unblocked and claimed after AR-1813 release; existing branch rebased
  cleanly to 5c843a12. Runtime receipt/factory API is now available; no live provider or TLC
  required.

- 2026-10-12T11:11:32+00:00: Heartbeat by ar1810-cli2key-luna56.

- 2026-10-12T11:16:48+00:00: Worker interrupted after no durable progress since 11:11:32Z;
  implementation worktree remained clean. Reclaim for a replacement worker; preserve no product
  changes.

- 2026-10-12T11:19:25+00:00: Claimed by ar1812-replacement-luna56.

- 2026-10-12T11:19:26+00:00: Heartbeat by ar1812-replacement-luna56.

- 2026-10-12T11:21:06+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T11:21:13+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T11:21:59+00:00: Recorded command exit 101; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-12T11:22:11+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T11:22:18+00:00: Recorded command exit 0; command argv SHA-256
  e40d55db50172a64d4a11ba8067c7e1a929c77dc6abb7d46af26c9aff8332947.

- 2026-10-12T11:22:25+00:00: Recorded command exit 101; command argv SHA-256
  6f8c4f7436f1263f9bbde46baeb9f21300065e295d6e6cdf4810d53fb11471c9.

- 2026-10-12T11:22:40+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T11:22:47+00:00: Recorded command exit 101; command argv SHA-256
  6f8c4f7436f1263f9bbde46baeb9f21300065e295d6e6cdf4810d53fb11471c9.

- 2026-10-12T11:23:00+00:00: Recorded command exit 101; command argv SHA-256
  4cde946e8331e96448132747a367054a64d2ee277e7e66e4937bdaae4a45d869.

- 2026-10-12T11:23:12+00:00: Recorded command exit 101; command argv SHA-256
  4cde946e8331e96448132747a367054a64d2ee277e7e66e4937bdaae4a45d869.

- 2026-10-12T11:23:32+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T11:23:39+00:00: Recorded command exit 0; command argv SHA-256
  4cde946e8331e96448132747a367054a64d2ee277e7e66e4937bdaae4a45d869.

- 2026-10-12T11:23:58+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-12T11:24:05+00:00: Recorded command exit 0; command argv SHA-256
  6f8c4f7436f1263f9bbde46baeb9f21300065e295d6e6cdf4810d53fb11471c9.

- 2026-10-12T11:24:14+00:00: Recorded command exit 0; command argv SHA-256
  e274074a17e0682b5edf79b5caca577a41520ed9ca8daf9342f0433b678582a1.

- 2026-10-12T11:24:18+00:00: Recorded command exit 0; command argv SHA-256
  c4dbae810880d038214e7ddc1c51edd196e89dbb8672ccf73248cd400e351916.

- 2026-10-12T11:24:34+00:00: Checkpointed source commit f489fbf51c5cbafe9e7ddc07b09ab1a9997b096d.

- 2026-10-12T11:25:00+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-12T11:26:08+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-12T11:26:27+00:00: Checkpointed source commit 10f095df843fd0b927c8f72f372a6245a9eac954.

- 2026-10-12T11:26:59+00:00: Heartbeat by ar1812-replacement-luna56.

- 2026-10-12T11:27:01+00:00: Checkpointed source commit 5b71c956ea88788c3b303425331e0682c8dbc241.

- 2026-10-12T11:27:51+00:00: Recorded command exit 101; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-12T11:28:24+00:00: Full cargo test --locked --workspace reached crates/asb-cli
  diagnostic_contract and failed only ordinary_cli_producers_are_mechanically_closed: the existing
  reviewed producer line map no longer recognizes shifted lib.rs call sites after commit 5c75c1a.
  Exit 101 at 11:27:51Z. No product fix applied yet; repair must preserve the mechanical diagnostic
  contract.

- 2026-10-12T11:30:37+00:00: Heartbeat by ar1812-replacement-luna56.

- 2026-10-12T11:32:14+00:00: Worker interrupted after heartbeat-only interval with no repair
  progress; preserved deterministic diagnostic-contract failure and implementation commit for
  replacement.

- 2026-10-12T11:32:58+00:00: Claimed by ar1812-repair-luna56.
