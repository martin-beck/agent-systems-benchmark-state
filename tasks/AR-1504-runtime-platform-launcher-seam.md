---
{
  "branch": "feature/ar-1504-runtime-platform-launcher-seam",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T00:43:51+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502"
  ],
  "id": "AR-1504",
  "next_action": "Await AR-1503 protected merge; then rebase this isolated branch and implement production launcher/session-discovery seam against the merged owner. In parallel inspect existing runtime/CLI boundaries and draft tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1504-launcher-luna56",
  "plan": "../plans/AR-1504-runtime-platform-launcher-seam.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the real runtime/platform-owned launcher and authenticated session discovery for AR-1503.",
  "task_revision": 6,
  "title": "Runtime/platform launcher seam",
  "updated_at": "2026-09-28T22:45:34+00:00",
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

- 2026-09-28T22:42:58+00:00: Dependencies AR-1473, AR-1474, AR-1480, AR-1484, AR-1485, and AR-1502
  are done; promote the successor to implement the missing production runtime/platform launcher seam
  identified by AR-1503.

- 2026-09-28T22:43:05+00:00: Claimed by ar1504-launcher-luna56.

- 2026-09-28T22:43:51+00:00: Heartbeat by ar1504-launcher-luna56.

- 2026-09-28T22:44:50+00:00: Setup attempt at protected origin/main: handoffctl run rejected
  worktree creation because invocation worktree 'agent-systems-benchmark' does not match declared
  'agent-systems-benchmark-ar-1504-runtime-platform-launcher-seam'; no product mutation occurred.
  Next: create declared worktree using documented setup exception, then run all worktree operations
  through handoffctl.

- 2026-09-28T22:45:34+00:00: Protected origin/main is 3c6af6b (PR #381 merge). Dependencies
  AR-1473/1474/1480/1484/1485/1502 are durable done. AR-1503 is not merged and its process_owner.rs
  exists only in its dirty worktree; therefore AR-1504 cannot truthfully compile against
  RuntimeControlProcessOwner yet. Declared AR-1504 worktree created at protected origin/main; no
  product files changed.
