---
{
  "branch": "feature/ar-1512-process-owner-material-contract",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T06:56:11+00:00",
  "depends_on": [
    "AR-1502",
    "AR-1484"
  ],
  "id": "AR-1512",
  "next_action": "Promote after AR-1511 blocker evidence is reconciled; define and implement the authenticated process-owner material contract and ordinary control caller.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1512-process-owner-luna56",
  "plan": "../plans/AR-1512-process-owner-material-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the authenticated process-owner material source and ordinary CLI/control caller needed to consume runtime authority.",
  "task_revision": 3,
  "title": "Authenticated process-owner material contract",
  "updated_at": "2026-09-29T04:56:11+00:00",
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
