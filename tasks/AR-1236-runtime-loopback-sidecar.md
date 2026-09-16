---
{
  "branch": "feature/ar-1236-runtime-loopback-sidecar",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1100",
    "AR-1231"
  ],
  "id": "AR-1236",
  "next_action": "Implement the versioned runtime-issued sidecar handoff: same-private-namespace sidecar and adapter, authenticated route/generation/command metadata, listener readiness, bounded forwarding, teardown, and non-interference tests; preserve NetworkPolicy::Deny.",
  "observed_branch": "feature/ar-1236-runtime-loopback-sidecar",
  "observed_dirty": 0,
  "observed_head": "df4debddb24205fe2f6ab21e4dfe574cc8af44b1",
  "owner": "",
  "plan": "../plans/AR-1236.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide a runtime-owned private-namespace loopback sidecar capability.",
  "task_revision": 11,
  "title": "Runtime-owned loopback sidecar capability",
  "updated_at": "2026-09-16T07:27:05+00:00",
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

- 2026-09-16T07:15:03+00:00: Implemented authenticated per-launch loopback sidecar seam at signed
  commit 1c6ab1d; cargo fmt, clippy -p asb-runtime, cargo test -p asb-runtime, and cargo test
  --workspace all pass. Capability probe: rootless unshare -Urn is available but loopback is DOWN
  and no reviewed mechanism exists to configure child-visible TCP; bwrap --unshare-net remains
  isolated and cannot inject a sidecar/bridge. Final in-namespace TCP-to-Unix forwarding and
  provider/descendant denial therefore remain blocked pending reviewed launcher/namespace contract.
  No host sharing, firewall mutation, ambient ip command, privileged helper, credentials, or
  unrelated AR changed.

- 2026-09-16T07:21:58+00:00: Resuming AR-1236 exclusively to implement and test the missing
  runtime-owned namespace bridge; preserve fail-closed isolation and NetworkPolicy::Deny.

- 2026-09-16T07:22:00+00:00: Claimed by asb_ar1236_worker.

- 2026-09-16T07:22:54+00:00: Extended AR-1236 at signed commits 1c6ab1d and df4debd. Added
  SidecarAttestation requiring explicit private namespace handoff proof; false/unavailable handoff
  fails closed. Added tests for attestation rejection/success; runtime suite 30 passed, process 8,
  sandbox 10, scheduler 16; formatting and clippy pass; full workspace previously passed. Host
  capability remains insufficient for actual in-namespace TCP bridge: rootless unshare -Urn has
  loopback DOWN and no reviewed launcher handoff exists. No host-network sharing, firewall mutation,
  ambient ip, privileged helper, credentials, or unrelated AR changed.

- 2026-09-16T07:27:05+00:00: Authorized next implementation pass for the specified runtime-issued
  sidecar handoff contract.
