---
{
  "branch": "feature/ar-1508-platform-owned-authority-provider",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T04:18:11+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502",
    "AR-1505"
  ],
  "id": "AR-1508",
  "next_action": "Implement and verify provider contract on isolated AR-1508 worktree based on protected AR-1505 merge f92c2e9; then independent exact-head review and hosted checks.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1508_provider_luna56",
  "plan": "../plans/AR-1508-platform-owned-authority-provider.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide an authenticated platform-owned source for private runtime roots, tools, policy, and enrollment material.",
  "task_revision": 5,
  "title": "Platform-owned authority provider",
  "updated_at": "2026-09-29T02:18:21+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1508-platform-owned-authority-provider"
}
---

AR-1507 proved that the existing bootstrap contract authenticates only digest
claims and that `RuntimeControlBootstrap::materialize_provisioner` still takes
caller-supplied `RuntimeAuthorityInputs`. This AR owns the missing platform
authority-provider boundary; it must produce verified private material without
exposing it to CLI callers or synthesizing it from fixed paths.

Acceptance requires:

- a runtime/control-owned authority provider authenticated to the AR-1505
  bootstrap session, with verified source/digest binding for namespace, lease,
  relay, tool pins, policy, credential reference, and enrollment material;
- a private materialization API consumed by `RuntimeControlBootstrap` and the
  live scheduler, with no caller/config/socket/path/PATH/fixed-root injection;
- fail-closed behavior for missing, stale, mismatched, expired, revoked,
  restarted, cancelled, or tampered authority, plus alternate-egress denial;
- provider-free deterministic local/mock/replay tests that qualify the contract
  without pretending to be first-customer production evidence;
- independent review, SSH-signed DCO, exact-head hosted checks, protected merge,
  and post-merge assurance.

Non-goals: asb-tui, live provider reachability, public credentials, synthetic or
fixed-path authority, weakening formal/privacy/native gates.

- 2026-09-29T04:14:00+02:00: Created from AR-1507 blocker evidence. The required
  source must be platform-owned and verified; no fixed path or mock authority is
  acceptable in production code.

- 2026-09-29T02:15:14+00:00: Dependencies through AR-1505 verified done; AR-1507 established the
  missing platform-owned authority provider contract.

- 2026-09-29T02:17:57+00:00: Claimed by ar1508_provider_luna56.

- 2026-09-29T02:18:11+00:00: Heartbeat by ar1508_provider_luna56.

- 2026-09-29T02:18:21+00:00: Setup audit: state reconciled and live doctor prerequisites refreshed;
  task revision 2 promoted/open then claimed at revision 3; dependencies include AR-1505 and are
  recorded done; AR-1505 product worktree inspected for requested merge base f92c2e9. Product docs
  and plan inspection now underway.
