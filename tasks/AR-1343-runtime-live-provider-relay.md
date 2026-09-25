---
{
  "branch": "feature/ar-1343-runtime-live-provider-relay",
  "checkpoint_commit": "f22afd0378c2039f95fe044e7b9047bacb3dccb1",
  "claim_expires": "",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340"
  ],
  "id": "AR-1343",
  "next_action": "BLOCKED on concrete missing primitives: asb-runtime has no production supervisor constructor for pinned SandboxBackend/live gate and no runtime-owned target/namespace provisioning; asb-agents ResolvedCredential transport is crate-private and cannot safely cross into runtime; no CLI service can acquire lease, credential, target, namespace, token, and relay atomically. Keep AR-1329 fail-closed. Coordinator must promote a narrowly scoped cross-crate runtime provisioning repair before AR-1343 can proceed.",
  "observed_branch": "feature/ar-1343-runtime-live-provider-relay",
  "observed_dirty": 0,
  "observed_head": "f22afd0378c2039f95fe044e7b9047bacb3dccb1",
  "owner": "",
  "plan": "../plans/AR-1343-runtime-live-provider-relay.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "superseded",
  "summary": "Add the runtime live-provider relay service and per-attempt opaque factory acquisition required by asb run and sweep.",
  "task_revision": 56,
  "title": "Runtime live-provider relay service and CLI acquisition",
  "updated_at": "2026-09-23T15:32:35+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1343-runtime-live-provider-relay"
}
---

AR-1329 integration audit after AR-1342 found that the opaque
`LiveLaunchFactory` is present but not CLI-consumable: there is no runtime live
relay listener/request protocol, concrete egress target acquisition, or
credential transport. This successor supplies those missing runtime-owned
capabilities without bypassing the denied-network sandbox.

- 2026-09-23: Created from the AR-1329 integration audit. Do not enable direct
  provider sockets or construct live handoffs in asb-cli.

- 2026-09-23T12:27:09+00:00: Claimed by codex-asb-ar1343-20260923.

- 2026-09-23T12:27:56+00:00: Heartbeat by codex-asb-ar1343-20260923.

- 2026-09-23T12:28:24+00:00: Recorded command exit 0; command argv SHA-256
  4ceb2c778de2adc750cc517d528e384d733c51082e7610e12c936ac8ef87bebe.

- 2026-09-23T12:31:39+00:00: Worker session interrupted after clean worktree setup with no
  implementation progress; preserve AR-1343 scope/checkpoint and hand off to replacement
  gpt-5.6-luna worker.

- 2026-09-23T12:31:46+00:00: Claimed by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:32:11+00:00: Heartbeat by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:35:08+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T12:35:25+00:00: Recorded command exit 0; command argv SHA-256
  7efe3114a2de0fa03cfcf4662abf7101ec4435d3e4aa92802e6182588b498e68.

- 2026-09-23T12:35:43+00:00: Heartbeat by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:36:50+00:00: Heartbeat by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:38:36+00:00: Heartbeat by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:38:59+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T12:39:18+00:00: Recorded command exit 0; command argv SHA-256
  7efe3114a2de0fa03cfcf4662abf7101ec4435d3e4aa92802e6182588b498e68.

- 2026-09-23T12:39:33+00:00: Heartbeat by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:39:39+00:00: Recorded command exit 0; command argv SHA-256
  165b66592d52ddd4e707177d6fbd75dd46166e641fe1d35c2e6222ed3e115a0b.

- 2026-09-23T12:40:57+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-23T12:41:15+00:00: Recorded command exit 0; command argv SHA-256
  7efe3114a2de0fa03cfcf4662abf7101ec4435d3e4aa92802e6182588b498e68.

- 2026-09-23T12:41:36+00:00: Recorded command exit 0; command argv SHA-256
  586e375516d3a41ae175d1db864f6e628fa402cb6999dc968023a2577d33a4bb.

- 2026-09-23T12:42:12+00:00: Relay implementation now has bounded nonblocking accept/read,
  authenticated exact-target forwarding, namespace and egress authorization, teardown/revoke, and 7
  focused tests including positive synthetic TCP, malformed/oversized, expiry, revoke, timeout, and
  duplicate cases. Full asb-runtime all-targets passed: 79 passed, 1 ignored. CLI currently has
  live_provider flag but no LiveLaunchFactory/LiveProviderRelay call path; AR remains in progress
  and AR-1329 fail-closed.

- 2026-09-23T12:42:48+00:00: Confirmed exact integration gap by source audit: spawn_verified_agent
  returns live provider runtime boundary is unavailable before process creation. Do not weaken this
  guard or construct direct sockets/authority in CLI. Relay runtime implementation and tests remain
  green: focused 7/7; full asb-runtime all-targets 79 passed, 1 ignored; clippy passed.

- 2026-09-23T12:43:26+00:00: Heartbeat by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:43:36+00:00: Recorded command exit 0; command argv SHA-256
  d4c43938f4e8e026f52d75141ccd4bd42bd9b0f05e2d2eaeb557ea9a634d0733.

- 2026-09-23T12:43:56+00:00: Recorded command exit 0; command argv SHA-256
  f39ba171faca5eb0cd73a9c92322bf04853aa0d8337161d47841b645006e5230.

- 2026-09-23T12:44:30+00:00: Committed relay portion as ce2c2db068b05092f0f63291e0d94d4dbc9cda9c
  with SSH signature and DCO. Worktree clean. Runtime relay focused 7/7, full all-targets 79
  passed/1 ignored, clippy passed. Source audit confirms CLI lacks the supported runtime acquisition
  seam; AR-1329 remains fail-closed pending that bounded API.

- 2026-09-23T12:45:01+00:00: Relay service delivered and verified at
  ce2c2db068b05092f0f63291e0d94d4dbc9cda9c (focused 7/7, runtime all-targets 79 passed/1 ignored,
  clippy passed). Release ownerless/open for the bounded CLI acquisition follow-up; preserve
  spawn_verified_agent fail-closed until runtime backend, benchmark lease, observed namespace, and
  relay lifecycle API are implemented and verified.

- 2026-09-23T12:46:22+00:00: Claimed by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:46:45+00:00: Heartbeat by codex-asb-ar1343-replacement-20260923.

- 2026-09-23T12:47:00+00:00: Reclaimed under replacement owner. Relay commit ce2c2db is
  SSH-signed+DCO and checkpointed. Existing SandboxBackend lacks a public discovery/acquisition API;
  CLI lacks benchmark lease, runtime token, observed child namespace, and relay lifecycle ownership.
  Inventing direct sockets or caller-built authority would violate AR scope and security boundaries.

- 2026-09-23T12:48:55+00:00: Relay implementation is committed and verified at ce2c2db; CLI
  acquisition is now isolated in promoted AR-1344. Keep AR-1329 fail-closed.

- 2026-09-23T15:22:52+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T15:23:03+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-23T15:23:20+00:00: Recorded command exit 0; command argv SHA-256
  8da9301c3b436d1d2430be4cf7a9ec902b7262bb7e8f28de6f839d0fd0e2560c.

- 2026-09-23T15:23:51+00:00: Recorded command exit 0; command argv SHA-256
  08d57388abeac3a1c095ff93186ee24351040d12d34ebf7d4f49c95980a5621f.

- 2026-09-23T15:24:10+00:00: Claimed dependency-safe after AR-1329 release. Fast-forwarded AR-1343
  worktree ce2c2db onto protected main a336d674 via handoffctl run. Baseline cargo test --locked -p
  asb-runtime --all-targets passed 83, 1 capability-gated ignored. Existing APIs still require
  caller-built input/backend/lease/handoff/relay and therefore do not satisfy production CLI
  acquisition; no synthetic authority mutation made.

- 2026-09-23T15:25:26+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T15:25:45+00:00: Recorded command exit 0; command argv SHA-256
  7b75844f7457924af2cfa7451c02a303cb2141407ce12ce2929e1bc4a6e8ff99.

- 2026-09-23T15:26:03+00:00: Recorded command exit 0; command argv SHA-256
  65bd39b6e995daa8de012e38f77d7d34e17aaa7f48f7d1538e37af30d16d3784.

- 2026-09-23T15:26:46+00:00: Added signed+DCO runtime LiveProviderRuntimeService projection around
  the opaque per-attempt factory, with opaque Debug and fail-closed acquisition test. Focused test
  and fmt pass. This is only an API projection; it does not synthesize authorities or bypass
  NetworkPolicy::Deny. Further concrete provisioning remains required before CLI integration.

- 2026-09-23T15:26:56+00:00: Recorded command exit 1; command argv SHA-256
  430d9ad39ba87548abd9ed6c12cec9e1dda25e13db540f44842cc1563d74d07d.

- 2026-09-23T15:27:17+00:00: Recorded command exit 0; command argv SHA-256
  7b75844f7457924af2cfa7451c02a303cb2141407ce12ce2929e1bc4a6e8ff99.

- 2026-09-23T15:27:39+00:00: Recorded command exit 0; command argv SHA-256
  e8beebac0638d83321c84d952814966bbba80dc16ee7dd3d3ead10f3c2b72292.

- 2026-09-23T15:28:04+00:00: Recorded command exit 0; command argv SHA-256
  5d13fb85560ae1a4c76b1821443d621ebd0d87607e79dbaa60399582941c14ee.

- 2026-09-23T15:28:30+00:00: Full diff review found d20e2eb was only an injected callback wrapper
  and would falsely claim runtime ownership; reverted safely in signed+DCO f22afd0. Baseline focused
  service test passed before revert; clippy passed. Initial multi-filter cargo command failed
  because cargo test accepts one TESTNAME: exact error was `error: unexpected argument ... found`
  and usage `cargo test [OPTIONS] [TESTNAME] [-- [ARGS...]]`; repaired by running the single focused
  test, which passed. No PR/publication.

- 2026-09-23T15:28:37+00:00: Heartbeat by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T15:29:10+00:00: Searched all production constructors/usages. ResourceLease::acquire,
  SandboxBackend::new, LiveProviderNamespaceHandoff::issue, ProviderEgressTarget::new and credential
  resolution occur only in tests or unrelated CSB paths; credential transport bytes are
  crate-private in asb-agents. Reverted misleading callback-only d20e2eb as signed f22afd0. Focused
  service test passed before revert; repaired cargo invocation and clippy passed. No PR/publication.

- 2026-09-23T15:31:10+00:00: Recorded command exit 0; command argv SHA-256
  54b952fd95f4d20665acf3dcb0031607a58af7527eadb009443c3cb5687eec87.

- 2026-09-23T15:31:25+00:00: Recorded command exit 0; command argv SHA-256
  480f90c0e5a6057d0348cd82be98e01e51adae9126387ee9d10b727d1093e05d.

- 2026-09-23T15:31:39+00:00: Recorded command exit 0; command argv SHA-256
  23b2cad55d063096f1db1ccc3f3d836e4b2a7b710b948912fa96bcb9825162c3.

- 2026-09-23T15:32:35+00:00: AR-1343 audit completed without unsafe product mutation. Reverted
  misleading callback-only projection at signed+DCO f22afd0. Cross-crate production provisioning is
  absent: no supervisor-owned SandboxBackend/live gate, concrete target/namespace, credential
  transport, or atomic lease/token/relay lifecycle. Superseded by coordinator repair AR-1346; keep
  AR-1329 fail-closed.

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
