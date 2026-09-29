---
{
  "branch": "feature/ar-1508-platform-owned-authority-provider",
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
  "id": "AR-1508",
  "next_action": "Promote after dependency verification; define the platform-owned authority provider and verified root/tool/policy source consumed by runtime materialization.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1508-platform-owned-authority-provider.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Provide an authenticated platform-owned source for private runtime roots, tools, policy, and enrollment material.",
  "task_revision": 2,
  "title": "Platform-owned authority provider",
  "updated_at": "2026-09-29T02:15:14+00:00",
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
