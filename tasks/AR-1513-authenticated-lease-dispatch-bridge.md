---
{
  "branch": "feature/ar-1513-authenticated-lease-dispatch-bridge",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1502", "AR-1484"],
  "id": "AR-1513",
  "next_action": "Promote after AR-1512 review evidence is reconciled; replace public self-authenticated owner material with authenticated issuance and wire the lease to live dispatch.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1513-authenticated-lease-dispatch-bridge.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Authenticate process-owner material, validate executable provenance, and connect leases to ordinary live dispatch.",
  "task_revision": 1,
  "title": "Authenticated lease-to-live-dispatch bridge",
  "updated_at": "2026-09-29T05:24:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1513-authenticated-lease-dispatch-bridge"
}
---

AR-1512 delivered a provider-free material contract and lifecycle store but its
independent review found three P1s: public constructors self-authenticate
arbitrary material, no non-test path consumes the lease into live dispatch, and
absolute launch paths are only lexical checks without executable/hash/symlink
provenance. This AR owns the bounded production bridge.

Acceptance requires:

- owner/enrollment-authenticated issuance that cannot be forged by public
  constructors or digest-only records; private roots and tools stay behind
  opaque runtime-owned capability handles;
- a non-test runtime/control/CLI adapter that consumes an authenticated lease
  and reaches `LiveProviderRuntimeHandle`/`LiveProviderRuntimeDispatchSource`
  for ordinary run/sweep, without caller/PATH/config authority injection;
- executable and adapter provenance is validated against pinned tool material:
  reject symlinks, nonexistent/non-executable paths, digest mismatch, absolute
  path drift, alternate target/egress, unknown fields and replay;
- expiry, restart, cancellation, remote revoke and teardown propagate through
  the real dispatch bridge, with deterministic provider-free negative tests;
- focused, serial workspace, clippy/docs/fmt, formal/privacy gates, independent
  exact-head review, SSH-signed DCO PR, protected merge, and post-merge proof.

Non-goals: asb-tui, live provider reachability, public credentials, private host
data, synthetic authority, or weakening fail-closed/native/formal gates.

- 2026-09-29T05:24:00+00:00: Created as the narrow successor to blocked
  AR-1512. Review evidence showed the material contract is not safe to publish
  until issuance authenticity, path provenance, and live dispatch consumption
  are implemented.
  AR-1512 remains historical blocked evidence rather than a prerequisite;
  this task starts from protected main and owns the missing production bridge.
