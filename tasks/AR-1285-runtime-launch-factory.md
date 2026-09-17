---
{
  "branch": "feature/ar-1285-runtime-launch-factory",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T03:28:19+00:00",
  "depends_on": [
    "AR-1282",
    "AR-1237",
    "AR-1238",
    "AR-1239"
  ],
  "id": "AR-1285",
  "next_action": "Promote after dependency verification; implement an opaque runtime-owned launch factory and CLI entrypoint boundary.",
  "observed_branch": "feature/ar-1285-runtime-launch-factory",
  "observed_dirty": 0,
  "observed_head": "f9ddf7ef6b3b2a96dd7faee04906f4e5cb3aa8e1",
  "owner": "asb_ar1024_lifecycle_router",
  "plan": "../plans/AR-1285.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a runtime-owned launch factory for authenticated strict-replay CLI execution.",
  "task_revision": 5,
  "title": "Runtime-owned strict-replay launch factory",
  "updated_at": "2026-09-17T01:30:21+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1285-runtime-launch-factory"
}
---

## AR-1285

Define the narrow authority boundary missing from AR-1284: the runtime, not the primary CLI,
must issue the authenticated launch context used for strict replay. This AR does not claim the
complete supervised cassette lifecycle; it supplies a real runtime-owned factory and entrypoint
that a later lifecycle AR can consume.

### Scope

ASB repository only. Owned paths are runtime launch/context construction, the primary CLI handoff
boundary, and focused integration fixtures/tests. No asb-tui or renderer paths. Do not reuse blocked
AR-1260--AR-1284 branches.

### Acceptance

- A runtime-owned factory issues opaque, generation-bound launch authority containing validated
  `SandboxLaunchInput`, `ResourceLease`, and pinned supervisor/sidecar command identities.
- The primary strict-replay CLI consumes that authority and cannot construct equivalent authority,
  relay handles, namespace readiness, or fallback providers itself.
- Unknown, stale, forged, caller-constructed, malformed, and mismatched authority is rejected
  fail closed; positive issuance/consumption and privacy-safe negative fixtures are included.
- No credentials, private paths, ambient host data, unbounded subprocess output, or runtime downloads
  enter evidence. Focused/full locked gates, review, signed+DCO exact-head CI, merge, and post-merge
  verification are required.

If the complete supervised lifecycle remains unavailable, stop at this boundary and create a
separate successor rather than claiming strict-replay execution.

- 2026-09-17T01:28:07+00:00: AR-1284 identified missing runtime-owned launch factory; promote narrow
  successor

- 2026-09-17T01:28:19+00:00: Claimed by asb_ar1024_lifecycle_router.

- 2026-09-17T01:30:21+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
