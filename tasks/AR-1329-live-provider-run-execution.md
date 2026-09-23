---
{
  "branch": "feature/ar-1329-live-provider-run-execution",
  "checkpoint_commit": "44ddf14334ac971e8e89bda195635595cfc651ab",
  "claim_expires": "2026-09-23T13:29:41+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1340"
  ],
  "id": "AR-1329",
  "next_action": "Consume the AR-1340 attested namespace-bound relay handoff; then integrate live run/sweep and complete denial/live evidence without weakening NetworkPolicy::Deny.",
  "observed_branch": "feature/ar-1329-live-provider-run-execution",
  "observed_dirty": 0,
  "observed_head": "2774b1d648b5c3bbda0e290e158dc352502d3768",
  "owner": "codex-asb-ar1329-20260923",
  "plan": "../plans/AR-1329.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Execute real agents against the selected provider through asb run and sweep with credential-free resolution.",
  "task_revision": 20,
  "title": "Live-provider run execution for real agents",
  "updated_at": "2026-09-23T11:29:41+00:00",
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
