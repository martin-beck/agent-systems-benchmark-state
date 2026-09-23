---
{
  "branch": "feature/ar-1329-live-provider-run-execution",
  "checkpoint_commit": "d24221731891fb39f56118be9c5ae51364824517",
  "claim_expires": "2026-09-23T17:19:14+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1340"
  ],
  "id": "AR-1329",
  "next_action": "AR-1342 LiveLaunchFactory focused tests pass, but CLI integration remains fail-closed: no runtime-owned live relay listener/request protocol, concrete egress target allowlist, credential transport, or pinned gate acquisition is exposed to asb run/sweep. Add a coordinator-owned runtime live-launch service API (per-attempt authority issuance and relay proxy) before AR-1329 product mutation; do not bypass NetworkPolicy::Deny.",
  "observed_branch": "feature/ar-1329-live-provider-run-execution",
  "observed_dirty": 0,
  "observed_head": "d24221731891fb39f56118be9c5ae51364824517",
  "owner": "codex-asb-ar1329-live-cli-luna56",
  "plan": "../plans/AR-1329.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Execute real agents against the selected provider through asb run and sweep with credential-free resolution.",
  "task_revision": 39,
  "title": "Live-provider run execution for real agents",
  "updated_at": "2026-09-23T15:19:54+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1329-live-provider-run-execution"
}
---

`asb run` and `asb sweep` currently execute a digest-pinned `batch-stdio-v1`
runtime stub instead of a real agent, so no benchmark can produce live evidence.
This AR wires the AR-1327 OpenRouter adapter projections into the execution path
so `run` and `sweep` launch a real agent process against the selected provider
and workload, resolves credentials only through the enrolled environment
channel, enforces the declared egress allowances, and requires an explicit
opt-in flag for any live provider contact. Offline CI, synthetic doubles, and
the digest-pinned mode remain default and never touch the network.

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
