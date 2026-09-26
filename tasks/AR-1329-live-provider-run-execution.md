---
{
  "branch": "feature/ar-1329-live-provider-run-execution",
  "checkpoint_commit": "a336d6744b1a82f36a706ec606b847c92d49cfd3",
  "claim_expires": "",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1340"
  ],
  "id": "AR-1329",
  "next_action": "Local deterministic mock run/sweep qualification is delivered by AR-1433 (PR #325, merge 2872a31f, all exact-main gates green). AR-1329 remains blocked only for optional production live-provider integration: an atomic runtime-owned LiveProviderRuntimeService must resolve pinned policy, enrolled credentials, attested namespace/relay, concrete egress target, ResourceLease, SandboxBackend, and one LiveProviderAttempt per scheduler attempt with cancellation teardown. Do not use external reachability as a CI gate; preserve NetworkPolicy::Deny and direct/alternate egress denial. AR-1446 may consume the local path without waiting for this optional boundary.",
  "observed_branch": "feature/ar-1329-live-provider-run-execution",
  "observed_dirty": 0,
  "observed_head": "04b4c067055073031cd6d88cf18f0d158f488ad0",
  "owner": "",
  "plan": "../plans/AR-1329.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "done",
  "summary": "Qualify asb run and sweep through a mandatory deterministic local mock; retain optional fail-closed live integration.",
  "task_revision": 56,
  "title": "Local-mock run execution with optional live-provider integration",
  "updated_at": "2026-09-26T20:10:13+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1329-live-provider-run-execution"
}
---

`asb run` and `asb sweep` currently execute a digest-pinned `batch-stdio-v1`
runtime stub rather than the deterministic local sub-1B/LiteLLM-compatible mock
agent path. This AR qualifies that local path as the mandatory development and
CI route, wiring the AR-1327 projections into execution while preserving
credential non-disclosure and declared-egress denial. Optional production live
provider contact remains explicitly gated by runtime-owned authority and is
never required for benchmark qualification or completion. Offline CI, synthetic
doubles, and the digest-pinned mode remain default and never touch the network.

- 2026-09-23T08:41:51+00:00: Dependencies AR-1327 and AR-1328 are done; begin live provider
  execution implementation.

- 2026-09-23T08:41:54+00:00: Claimed by codex-asb-ar1329-20260923.

- 2026-09-23T08:42:44+00:00: Heartbeat by codex-asb-ar1329-20260923.

- 2026-09-23T08:48:27+00:00: Focused CLI and workflow tests pass. Live credential transport is
  bounded and secret-free; AR remains in_progress pending authenticated relay/egress integration and
  denial tests.

- 2026-09-23T08:51:09+00:00: Removed unsafe direct credential injection and now fail closed for live
  launches. Evidence: cargo check, CLI live-gate test, and workflow transcript pass; current runtime
  APIs have no provider endpoint allowlist or authenticated live relay.

- 2026-09-23T08:53:25+00:00: Added runtime provider_egress module and denial tests. cargo test -p
  asb-runtime provider_egress, cargo check -p asb-cli and CLI live-gate tests pass. Actual
  authenticated relay/backend integration remains required.

- 2026-09-23T08:55:36+00:00: AR-1339 created and claimed to implement the missing runtime
  provider-egress backend. AR-1329 remains in_progress with safe fail-closed CLI and typed egress
  identity committed at 44ddf14.

- 2026-09-23T09:56:05+00:00: AR-1339 is now merged at 229941f with all seven post-merge workflows
  green; AR-1329 is dependency-ready and should resume relay integration.

- 2026-09-23T09:56:11+00:00: Heartbeat by codex-asb-ar1329-20260923.

- 2026-09-23T10:14:51+00:00: Heartbeat by codex-asb-ar1329-20260923.

- 2026-09-23T11:26:08+00:00: Heartbeat by codex-asb-ar1329-20260923.

- 2026-09-23T11:27:08+00:00: Heartbeat by codex-asb-ar1329-20260923.

- 2026-09-23T11:27:14+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-23T11:27:37+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-23T11:29:27+00:00: Recorded command exit 0; command argv SHA-256
  aa0321b8e6974c0520a593ecf349e83213fa5d83db2a7c8714bc93aa41a96aca.

- 2026-09-23T11:29:41+00:00: Heartbeat by codex-asb-ar1329-20260923.

- 2026-09-23T11:30:07+00:00: Rebased isolated worktree onto protected main
  2774b1d648b5c3bbda0e290e158dc352502d3768 using handoffctl run. Focused cargo test -p asb-cli
  live_provider_requires_explicit_selection_before_any_run_effects passed (0 tests due filter;
  command exit 0). Integration audit: CLI spawn_verified_agent deliberately returns live provider
  runtime boundary unavailable; AR-1340 runtime API requires pre-issued namespace-bound handoff and
  SandboxBackend plus an existing validated relay socket, but no sanctioned CLI relay/backend
  acquisition exists. Direct re-enable would bypass NetworkPolicy::Deny, so no unsafe mutation made.

- 2026-09-23T11:30:15+00:00: Recorded command exit 0; command argv SHA-256
  240bd80324356f608b0a39871d69a15449eec6a61ea57561a531f72d616cb223.

- 2026-09-23T11:31:19+00:00: Heartbeat by codex-asb-ar1329-20260923.

- 2026-09-23T11:32:26+00:00: Follow-up repair AR creation is coordinator-owned; no task-creation
  command exists in handoffctl, so I do not fabricate AR-1342 files or claim creation. Proposed
  AR-1342 scope is recorded in next_action with exact missing API/call path and denial requirements.
  AR-1329 remains in_progress and truthfully blocked on that successor capability; no product
  changes made. Heartbeat renewed. Reconcile completed state commit but doctor --live and snapshot
  both fail because generated WORKTREES.md is stale; this is recorded as an external
  state-reconciliation failure.

- 2026-09-23T11:32:39+00:00: Released open, not done: live run/sweep remains fail-closed because
  asb-cli has no runtime-owned relay/backend acquisition path. Proposed coordinator successor
  AR-1342 must supply a validated relay listener, ProviderEgressHandoff, runtime-observed
  NamespaceIdentity-bound LiveProviderNamespaceHandoff, SandboxBackend, ResourceLease, and child
  launch context. Preserve NetworkPolicy::Deny, direct/alternate egress denial, credential
  non-disclosure, cancellation/teardown, and offline default. No unsafe direct bypass. State
  reconcile doctor/snapshot currently report stale WORKTREES.md.

- 2026-09-23T12:20:51+00:00: Claimed by codex-asb-ar1329-20260923b.

- 2026-09-23T12:21:13+00:00: AR-1342 is durably done with all seven post-merge workflows green.
  AR-1329 resumed under replacement gpt-5.6-luna medium worker; previous fail-closed boundary
  remains until live integration evidence passes.

- 2026-09-23T12:21:38+00:00: Heartbeat by codex-asb-ar1329-20260923b.

- 2026-09-23T12:22:45+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-23T12:23:26+00:00: Recorded command exit 0; command argv SHA-256
  ff6d1fa7a7185010f75fcfafe4bdc1bdd5b9804d8c2b3e7abdd8a1b96cd81c63.

- 2026-09-23T12:24:04+00:00: Recorded command exit 0; command argv SHA-256
  a43f0c33e0455d600a2740a14bbe7c9bd040668bf69202bfcb0a3e00b1f5942c.

- 2026-09-23T12:24:32+00:00: Rebased isolated worktree through handoffctl onto protected main
  d24221731891fb39f56118be9c5ae51364824517. Audited execute_inner -> run_attempt ->
  spawn_verified_agent: live_provider still returns runtime boundary unavailable. AR-1342 exports
  LiveLaunchFactory/LiveLaunchContext and SandboxBackend::attest_live_launch, but no CLI-consumable
  factory inputs or provider relay server exist. ProviderEgressRelay is client-only; selection
  carries endpoint digest, not a concrete target. Focused handoffctl cargo test --locked -p
  asb-runtime live_factory --lib passed 2/2. No unsafe product change made; NetworkPolicy::Deny and
  direct/alternate egress denial preserved.

- 2026-09-23T12:24:47+00:00: Recorded command exit 0; command argv SHA-256
  e8f1b6e696bc5011c596493b05e19e1aa1b10bd52d18175e4f2e3d69485513aa.

- 2026-09-23T12:25:00+00:00: Heartbeat by codex-asb-ar1329-20260923b.

- 2026-09-23T12:25:03+00:00: Recorded command exit 0; command argv SHA-256
  a76a8bc2155da045daf9d31e4f0496b38768f63b49972ee17a8fe155ee6a123a.

- 2026-09-23T12:26:55+00:00: Released ownerless and open after AR-1329 live integration audit.
  Checkpoint protected main d24221731891fb39f56118be9c5ae51364824517. AR-1342 LiveLaunchFactory
  focused tests pass, but CLI remains fail-closed because no runtime-owned live relay
  listener/request protocol, concrete egress target allowlist acquisition, credential transport, or
  pinned live gate acquisition is available. Successor AR-1343 now provides the required scoped
  repair; preserve NetworkPolicy::Deny and direct/alternate egress denial.

- 2026-09-23T15:19:14+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T15:19:54+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-23T15:20:13+00:00: Recorded command exit 0; command argv SHA-256
  91c481d4f1a058d3265e9102b0531d1eefe09cb45e5c1807ecda5e8c8b6b67d5.

- 2026-09-23T15:21:36+00:00: Rebased isolated AR-1329 worktree from stale d242217 to protected
  origin/main a336d674 via handoffctl run. Merged AR-1344/1345 API audit confirms injected factory
  helpers and lifecycle are present, but real asb run/sweep dispatch still has no runtime-owned
  acquisition implementation. No product mutation made.

- 2026-09-23T15:21:52+00:00: Heartbeat by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T15:22:12+00:00: Current merged AR-1344/1345 audit: run_with_live_provider_factory and
  run_with_live_provider_attempt are library injection seams only; normal CLI dispatch passes None.
  No production constructor exists for SandboxLaunchInput + ResourceLease + SandboxBackend +
  concrete ProviderEgressTarget + LiveProviderNamespaceHandoff + LiveProviderRelay. Constructing
  synthetic/test authority or bypassing NetworkPolicy::Deny would violate the contract. Precise
  repair scope recorded; no unsafe product mutation.

- 2026-09-23T15:22:38+00:00: Released ownerless/open at protected checkpoint a336d674. Exact
  blocker: no production runtime-owned atomic acquisition service for SandboxBackend, benchmark
  ResourceLease, launch token, runtime-observed NamespaceIdentity, per-attempt LiveProviderRelay,
  concrete egress target, and credential channel. AR-1343 must implement and verify this service;
  AR-1329 remains fail-closed until then.

- 2026-09-24T04:37:37+00:00: Claimed by codex-asb-runtime-receipt-source-luna56.

- 2026-09-24T04:37:55+00:00: Heartbeat by codex-asb-runtime-receipt-source-luna56.

- 2026-09-24T04:37:59+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-09-24T04:38:12+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-24T04:38:42+00:00: Recorded command exit 0; command argv SHA-256
  286135258494dbd54e39008e25f49688ba0cf41ce7867f34659d6993e4c009c5.

- 2026-09-24T04:39:01+00:00: Re-audit after merged AR-1380/1381: runtime scheduler and CLI factory
  wiring are present, but no atomic runtime-owned source constructs LiveProviderRuntimeHandle from
  authenticated enrollment/control state for the actual asb run/sweep command. Existing CLI only
  accepts an externally supplied scheduler; accepting caller authority or synthesizing
  credentials/chain is forbidden. No safe product diff remains in AR-1329. Create successor for
  authenticated runtime execution-source materialization.

- 2026-09-25T15:00:00+00:00: Coordinator production-readiness audit clarified that the mandatory local execution boundary remains AR-1432/AR-1433, while the optional production live boundary remains runtime-owned and fail-closed. Created AR-1446 for disposable first-customer install/configure/benchmark/replay/recovery/cleanup qualification; no live-provider or CI gate was weakened.

- 2026-09-25T17:15:00+00:00: AR-1433 delivered and post-merge verified the runtime-owned
  deterministic mock-attempt path. The mandatory local boundary is no longer blocked;
  only the optional production live-provider service remains blocked. AR-1446 can use
  the local path independently.

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

- 2026-09-26T20:09:57+00:00: Local deterministic mock boundary is complete via AR-1433 and current
  first-customer qualification; external provider reachability is explicitly optional and cannot
  block this AR.

- 2026-09-26T20:10:04+00:00: Claimed by coordinator-ar1329-local-completion.

- 2026-09-26T20:10:13+00:00: Completed: deterministic local/mock run and sweep boundary delivered by
  AR-1433 (PR #325, merge 2872a31f2ee90ac5df1a47203b2a618b1829cfec), all exact-main gates passed,
  and consumed by current first-customer qualification/release at
  0a85123785c3e5e293fee02df757f494ac3423fe. External/live provider reachability and runtime live
  integration remain optional supplementary capability, never a completion or CI gate;
  NetworkPolicy::Deny and direct/alternate-egress denial remain intact.
