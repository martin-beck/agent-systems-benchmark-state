---
{
  "branch": "feature/ar-1512-process-owner-material-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T07:04:46+00:00",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1512",
  "next_action": "Add runtime/control caller facade over validated owner store; then run focused, format, clippy, docs and serial workspace gates.",
  "observed_branch": "feature/ar-1512-process-owner-material-contract",
  "observed_dirty": 2,
  "observed_head": "f92c2e941913129d7db50480f71e8361a0d43a0c",
  "owner": "ar1512-process-owner-luna56",
  "plan": "../plans/AR-1512-process-owner-material-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the authenticated process-owner material source and ordinary CLI/control caller needed to consume runtime authority.",
  "task_revision": 13,
  "title": "Authenticated process-owner material contract",
  "updated_at": "2026-09-29T05:08:21+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1512-process-owner-material-contract"
}
---

AR-1511 proved that the runtime issuer and lifecycle fencing are implemented,
but protected main still lacks the source that can safely supply them. The
existing control records contain public digests only; no non-test provider or
ordinary CLI/control caller can reconstruct private roots, pinned tools,
policy/allowlist, namespace or launch-input provenance. This AR owns that
missing contract and source.

Acceptance requires:

- an ASB-only, versioned authenticated process-owner material contract issued
  by the runtime/control owner, carrying opaque capability references plus the
  private roots, namespace, pinned tool/adapter bundle, policy/allowlist,
  credential capability and launch provenance needed by the provider;
- a non-test control/runtime caller that obtains the contract from authenticated
  owner/enrollment state and feeds the runtime issuer/dispatch source without
  caller-built authority, PATH/config injection or digest-only reconstruction;
- explicit endpoint/session, generation, expiry, restart, cancellation,
  revocation, teardown, target and alternate-egress bindings, with unknown
  fields and replay/mismatch rejected;
- launch executable/adapter provenance is bound to the authenticated tool
  bundle, and ordinary CLI live run/sweep reaches the provider-owned source;
- deterministic provider-free positive/negative tests, generated docs, focused
  and serial workspace/formal/privacy gates, independent review, SSH-signed DCO
  exact-head PR, protected merge and post-merge assurance.

Non-goals: asb-tui, live provider reachability, public credentials, private
host data, synthetic authority, or weakening fail-closed/native/formal gates.

- 2026-09-29T04:56:00+00:00: Created as the prerequisite successor to blocked
  AR-1511. Its diagnostic audit showed that implementing a consumer over
  digest-only records would fabricate authority; build the authenticated
  process-owner source and ordinary caller first.

- 2026-09-29T04:56:08+00:00: AR-1511 diagnostic blocker reconciled; promote prerequisite
  authenticated process-owner material contract and ordinary caller.

- 2026-09-29T04:56:11+00:00: Claimed by ar1512-process-owner-luna56.

- 2026-09-29T04:58:03+00:00: Heartbeat by ar1512-process-owner-luna56.

- 2026-09-29T04:58:06+00:00: Setup audit: authoritative AR-1512 state is ASB state checkout;
  protected main is f92c2e941913129d7db50480f71e8361a0d43a0c. Existing product main is dirty and
  AR-1511 work must not be reused. Starting isolated worktree and contract audit.

- 2026-09-29T04:58:44+00:00: Recorded command exit 0; command argv SHA-256
  227bd2b8f251398a28e02809a6a2e32716ea68be7d6a13f02381b8daf3223aa1.

- 2026-09-29T05:04:46+00:00: Heartbeat by ar1512-process-owner-luna56.

- 2026-09-29T05:04:58+00:00: Audit complete: protected main has digest-only RuntimeAuthorityRecord
  and RuntimeBootstrapRecord; no non-test owner material source. RuntimeAuthorityInputs are internal
  and the materialization path is absent outside test/internal seams. AR-1511 dirty worktree is not
  reused.

- 2026-09-29T05:07:23+00:00: Recorded command exit 101; command argv SHA-256
  1c6e3d8d232e466e14598929e51bba34dbfff29b29579b2c872590b2de8e94e0.

- 2026-09-29T05:07:42+00:00: Recorded command exit 0; command argv SHA-256
  1c6e3d8d232e466e14598929e51bba34dbfff29b29579b2c872590b2de8e94e0.

- 2026-09-29T05:08:21+00:00: Focused test first failed at 05:07:23 during compilation: four test
  assertions compared Result<opaque capability/lease/store, error> with assert_eq!, requiring
  PartialEq on private opaque types. Patched tests to use matches! without exposing or deriving
  equality for capabilities/material. Retry at 05:08 passed 4 process_owner_material tests.
