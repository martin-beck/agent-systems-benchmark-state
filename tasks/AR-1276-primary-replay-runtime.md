---
{
  "branch": "feature/ar-1276-primary-replay-runtime",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1276",
  "next_action": "Promote after dependency verification; wire the primary replay command to runtime-issued operation execution and prove supervised lifecycle behavior.",
  "observed_branch": "feature/ar-1276-primary-replay-runtime",
  "observed_dirty": 0,
  "observed_head": "69e8b064d3121a4bae1f672cdae9c0c8672000bc",
  "owner": "",
  "plan": "../plans/AR-1276.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Integrate runtime-owned operation execution into the primary strict-replay command.",
  "task_revision": 6,
  "title": "Primary replay runtime integration",
  "updated_at": "2026-09-16T23:58:53+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1276-primary-replay-runtime"
}
---

## AR-1276

Integrate the runtime-issued operation into the actual primary replay command. Preserve AR-1275's
blocked evidence and require real supervised cassette traffic and lifecycle tests.

- 2026-09-16T23:57:31+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done. AR-1275 is blocked
  evidence only; implement the primary command integration without consuming its branch.

- 2026-09-16T23:57:46+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-16T23:58:43+00:00: Heartbeat by asb_ar1024_lifecycle_router.

- 2026-09-16T23:58:46+00:00: Released blocked/ownerless without product mutation after exact
  architecture audit. Primary replay dispatch in crates/asb-cli/src/lib.rs accepts only cassette
  path, provider profile digest, agent ID, and stdout; no runtime context/service channel exists.
  Existing runtime/sidecar APIs are not callable from this argument-only process entrypoint without
  fabricating authority or adding a new runtime-to-CLI transport boundary. Exact blocker: cannot
  safely implement runtime-issued operation injection or prove supervised cassette response,
  provider/descendant egress denial, cancellation/restart/timeout/crash reaping, cleanup, and
  no-fallback in AR-1276 scope without that missing boundary. Preserve AR-1275 and request a
  follow-on transport-entrypoint AR.
