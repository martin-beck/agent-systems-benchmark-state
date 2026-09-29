---
{
  "branch": "feature/ar-1507-runtime-owned-authority-materialization",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502",
    "AR-1505"
  ],
  "id": "AR-1507",
  "next_action": "Promote after dependency verification; define and implement the runtime-owned authority materializer that maps authenticated bootstrap state to private roots, tools, policy, and opaque dispatch source.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1507-runtime-owned-authority-materialization.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Materialize private runtime launch authority from authenticated AR-1505 bootstrap state without caller or synthetic authority.",
  "task_revision": 1,
  "title": "Runtime-owned authority materialization",
  "updated_at": "2026-09-29T04:06:00+02:00",
  "worktree_key": "agent-systems-benchmark-ar-1507-runtime-owned-authority-materialization"
}
---

AR-1506 proved that the platform launcher cannot safely be published until the
runtime owns construction of the private authority inputs required by the live
dispatch scheduler. AR-1505 authenticates bootstrap metadata and digest claims,
but deliberately does not expose lease/relay/tool/policy roots to the CLI.
This AR owns that missing runtime/control materialization boundary.

Acceptance requires:

- a runtime/control-owned materializer that consumes only authenticated AR-1505
  bootstrap state and constructs private `RuntimeAuthorityInputs`, certificate
  authority, enrollment/receipt source, launch policy, tool pins, lease root,
  relay root, namespace binding, and egress policy;
- no public constructor or argument that accepts caller/config/socket/credential/
  root/tool/policy authority, and no fixed-path, mock, or synthetic authority in
  production code;
- an opaque `LiveProviderRuntimeDispatchSource` factory that is reachable only
  from the authenticated runtime-owned path and can be handed to ordinary
  `asb-cli` run/sweep dispatch;
- deterministic provider-free local/mock/replay tests for missing, stale,
  mismatched, expired, cancelled, revoked, restarted, and alternate-egress
  authority, plus teardown and one-shot source consumption;
- independent exact-head review, SSH-signed DCO commit, all hosted checks,
  protected merge, and terminal post-merge assurance.

Non-goals: asb-tui changes, live provider reachability, credentials in tests,
fixed host paths, weakening fail-closed behavior, or treating a mock as
first-customer production evidence.

- 2026-09-29T04:06:00+02:00: Created from AR-1506 independent P1 findings. The
  launcher facade is intentionally preserved as unmerged evidence until this
  runtime-owned authority materialization contract exists.
