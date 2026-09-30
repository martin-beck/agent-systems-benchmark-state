---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1505",
    "AR-1513",
    "AR-1514"
  ],
  "id": "AR-1551",
  "next_action": "Promote after AR-1505, AR-1513 and AR-1514 are done; implement and deploy the runtime/control-owned authenticated platform authority source, then hand its opaque materialization contract to AR-1523.",
  "owner": "",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provision the missing authenticated platform authority deployment required for first-customer live dispatch.",
  "task_revision": 1,
  "title": "First-customer platform authority deployment bootstrap",
  "updated_at": "2026-09-30T05:06:00+00:00"
}
---

# AR-1551

Provide the concrete deployment-owned source that AR-1523 is waiting for.
The source must issue or retrieve private runtime authority only after an
authenticated AR-1505 bootstrap binding, and must hand the runtime an opaque
materialization capability for ordinary ASB run/sweep. It must keep private
roots, namespace identity, relay/lease roots, tool pins, egress policy,
credential capability and enrollment inside the runtime/control owner.

The deployment may use a rootless owner-only Unix service or an isolated
container/VM on the second disk; it must not require a particular native host,
expose authority through CLI arguments, configuration, environment variables,
PATH lookup, fixed public paths or durable public evidence, and must not add a
runtime dependency on Agent Relay. Development and CI use deterministic local
mock/replay authority fixtures and never require an external provider.

Acceptance requires:

- an authenticated, versioned deployment-to-runtime handoff bound to session,
  generation, expiry, restart, cancellation, revocation and teardown;
- fail-closed rejection of missing, stale, replayed, alternate-egress,
  mismatched or tampered material, with no private values in tasks or logs;
- ordinary ASB run/sweep wiring through the opaque source, while local/mock and
  strict-replay paths remain unchanged;
- bounded provider-free positive and negative tests, exact-head review,
  signed+DCO PR, required hosted gates and a sanitized first-customer-style
  deployment receipt;
- no formal AR-1307/1308 qualification claim and no weakening of their gates.

This AR supplies deployment authority only; AR-1523 owns the ASB production
adapter and final live-dispatch qualification.
