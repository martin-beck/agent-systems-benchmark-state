---
{
  "branch": "feature/ar-1236-runtime-loopback-sidecar",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T09:12:07+00:00",
  "depends_on": [
    "AR-1100",
    "AR-1231"
  ],
  "id": "AR-1236",
  "next_action": "Design and implement an approved runtime-owned in-namespace loopback sidecar/relay capability; preserve NetworkPolicy::Deny, deny provider and ambient egress, and prove lifecycle cleanup and unrelated-process non-interference.",
  "observed_branch": "feature/ar-1236-runtime-loopback-sidecar",
  "observed_dirty": 0,
  "observed_head": "1c6ab1db1496250adb927a615e7751d376e8f1e9",
  "owner": "asb_ar1236_worker",
  "plan": "../plans/AR-1236.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide a runtime-owned private-namespace loopback sidecar capability.",
  "task_revision": 5,
  "title": "Runtime-owned loopback sidecar capability",
  "updated_at": "2026-09-16T07:14:16+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1236"
}
---

Create the runtime-owned capability missing from AR-1234. The child must remain in a private
network namespace while a pinned in-namespace sidecar exposes only the authenticated cassette
route through the existing Unix relay handoff.

Acceptance: use only reviewed in-tree or immutably pinned helper code; no host-network sharing,
global firewall mutation, ambient ip commands, credentials, or unreviewed privileged setup. Bind
socket path, route digest, and generation to one launch. Bound forwarding and teardown must cover
success, timeout, cancellation, crash, restart, stale generation, duplicate attempt, and partial
launch. Prove provider/external egress denial and unrelated-process non-interference. Preserve
NetworkPolicy::Deny and fail closed when the capability is unavailable. Run focused/full locked,
privacy, policy, native, signature, and exact-head gates.

- 2026-09-16T07:11:44+00:00: Dependencies AR-1100 and AR-1231 verified complete; promote
  runtime-owned loopback sidecar capability.

- 2026-09-16T07:12:07+00:00: Claimed by asb_ar1236_worker.
