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
  "next_action": "No development action: deployment-owned authenticated authority is optional future production hardening. If live-provider production is later authorized, create a separately scoped successor; local/mock authority is sufficient for development qualification.",
  "owner": "",
  "priority": "P0",
  "schema_version": 1,
  "status": "cancelled",
  "summary": "Optional future production-live platform authority bootstrap; not a development qualification requirement.",
  "task_revision": 10,
  "title": "First-customer platform authority deployment bootstrap",
  "updated_at": "2026-09-30T03:11:41+00:00",
  "worktree_key": "",
  "plan": ""
}

---

# AR-1551

Record the optional future production-hardening work for a deployment-owned
authority source. AR-1523 no longer waits for this work: deterministic
local/mock and strict-replay authority are sufficient for development
qualification.
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

If this optional production-hardening work is later authorized, acceptance would require:

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

This AR is intentionally cancelled for the development path. It supplies no
development dependency and makes no live-provider or formal qualification
claim. Any future production implementation must be a new, explicitly scoped
AR with its own deployment owner.

- 2026-09-30T05:07:00+00:00: Runtime baseline gates passed, but no non-test deployment source or
  ordinary run/sweep production callsite exists in protected ASB. Local/mock authority remains
  deliberately non-qualifying; AR-1523 is still blocked pending this source.

- 2026-09-30T03:09:02+00:00: Dependencies AR-1505, AR-1513 and AR-1514 are done; the missing
  deployment-owned authority source is the canonical first-customer live-dispatch blocker.

- 2026-09-30T03:09:05+00:00: Claimed by coordinator-ar1551-platform-authority-20260930.

- 2026-09-30T03:09:16+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-09-30T03:09:34+00:00: Heartbeat by coordinator-ar1551-platform-authority-20260930.

- 2026-09-30T03:09:37+00:00: Recorded command exit 0; command argv SHA-256
  67348e3ff9b95e3f784d2495799176e1c6d53e658d3193972c3a9cb85e7ca378.

- 2026-09-30T03:10:29+00:00: Recorded command exit 0; command argv SHA-256
  f74a3e0c628aa519165a1e8299575f4a296a60e1a070dedb989674b1f7fffe94.

- 2026-09-30T03:10:57+00:00: Baseline exact-origin runtime gates pass: 164 asb-runtime unit tests, 3
  loopback tests, 8 process-boundary tests, 15 sandbox-boundary tests, 16 scheduler-boundary tests
  and 2 doctests. The implementation blocker is now explicit: protected ASB has no non-test
  deployment-owned platform authority source or ordinary run/sweep production callsite. Existing
  local/mock authority is deliberately development-only and cannot be promoted. AR-1523 remains
  blocked and must consume an authenticated opaque source from a future deployment implementation;
  no live-provider or formal qualification claim was made.

- 2026-09-30T06:00:00+00:00: Cancelled as a development blocker by coordinator policy update.
  No deployment-owned authenticated authority source exists or is required for development;
  AR-1523 uses deterministic local/mock and strict-replay authority. Preserve this record only as
  optional future production hardening, with any implementation requiring a new scoped AR.
