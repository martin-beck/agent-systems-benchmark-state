---
{
  "branch": "feature/ar-1278-primary-runtime-client",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1278",
  "next_action": "Promote after dependency verification; hand the runtime-issued replay client into primary argument dispatch and prove supervised lifecycle behavior.",
  "observed_branch": "feature/ar-1278-primary-runtime-client",
  "observed_dirty": 0,
  "observed_head": "69e8b064d3121a4bae1f672cdae9c0c8672000bc",
  "owner": "",
  "plan": "../plans/AR-1278.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Connect the primary replay command to the runtime-issued transport client.",
  "task_revision": 6,
  "title": "Primary replay runtime client handoff",
  "updated_at": "2026-09-17T00:09:31+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1278-primary-runtime-client"
}
---

## AR-1278

Connect the primary argument-level replay command to the runtime-issued transport client. Preserve
AR-1277's blocked evidence and require actual supervised execution and lifecycle proof.

- 2026-09-17T00:08:37+00:00: Dependencies AR-1237, AR-1238, and AR-1239 are done; AR-1277 proves the
  primary dispatcher still does not receive a runtime-issued client.

- 2026-09-17T00:08:53+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T00:09:10+00:00: Recorded command exit 0; command argv SHA-256
  9232d01513397d9430c82af844fc9d297aeb87686c350d1879473604dfae2c2e.

- 2026-09-17T00:09:31+00:00: Released blocked/ownerless after fresh main audit, no product mutation.
  Exact evidence: crates/asb-cli/src/lib.rs dispatch/replay accepts only argument
  paths/profile/agent/stdout; no runtime client/transport module exists on origin/main. asb-runtime
  exposes sidecar/process primitives but no CLI handoff entrypoint. Safely connecting runtime-issued
  client requires introducing and reviewing the dependency-neutral transport contract before primary
  command integration. Therefore supervised cassette response, provider/descendant egress denial,
  no-fallback, cancellation/restart, timeout/crash reaping, cleanup, and malformed/stale/duplicate
  proof cannot be established in this AR without fabricating authority.
