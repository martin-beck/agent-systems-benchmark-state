---
{
  "branch": "feature/ar-1504-runtime-platform-launcher-seam",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502"
  ],
  "id": "AR-1504",
  "next_action": "Promote after dependency verification; implement and exercise the production runtime/platform launcher seam that invokes the authenticated process owner.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1504-runtime-platform-launcher-seam.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide the real runtime/platform-owned launcher and authenticated session discovery for AR-1503.",
  "task_revision": 1,
  "title": "Runtime/platform launcher seam",
  "updated_at": "2026-09-28T22:41:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1504-runtime-platform-launcher-seam"
}
---

Successor to the exact AR-1503 review finding. AR-1503's authenticated
process-owner contract and tests are retained as historical evidence, but its
implementation is not accepted as complete because it is a tests-only façade.

- 2026-09-28T22:41:00+00:00: Created from AR-1503's independent review. The
  runtime/platform launcher and authenticated session discovery are still absent:
  no production path constructs or invokes `RuntimeControlProcessOwner`, and
  ASB CLI entry/run/sweep continue to pass `None,None`. This AR must implement
  the real owner-only seam without caller/config authority injection.

Acceptance requires:

- a production runtime/platform-owned launcher or session-discovery path that
  constructs the owner from authenticated platform inputs and invokes the
  opaque dispatch source;
- no public CLI/config/socket/chain/authority bypass and fail-closed behavior
  for missing, stale, mismatched, revoked, cancelled, restarted, or expired
  sessions;
- deterministic provider-free tests covering launch, dispatch, cancellation,
  teardown, restart, and negative authority cases;
- independent diff review, SSH-signed DCO commit, exact-head hosted CI,
  protected merge, and all required post-merge verification.

Non-goals: asb-tui changes, live provider reachability, generated authority,
caller-built runtime inputs, or weakening native/credential/egress gates.
