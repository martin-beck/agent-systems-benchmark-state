---
{
  "branch": "feature/ar-1514-runtime-auth-reconciliation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1499",
    "AR-1500"
  ],
  "id": "AR-1514",
  "next_action": "Implement and qualify the disposable runtime reconciliation repair, then rerun the v1.10 helper handoff and capture successful digest-only AuthStatus for paired asb-tui AR-1323.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1514-runtime-auth-reconciliation.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Repair ASB development-runtime reconciliation between digest-only enrollment and helper invocation.",
  "task_revision": 1,
  "title": "Reconciled development auth handoff runtime",
  "updated_at": "2026-09-29T12:30:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1514-runtime-auth-reconciliation"
}
---

The standalone asb-tui client and its deterministic socketpair fixture now
preserve the typed reconciliation failure and prove retry/reconnect behavior.
The ASB disposable runtime still returns `-33008 runner reconciliation is
required` after a committed digest-only enrollment. This AR owns the runtime
side of that repair.

- Development qualification may use an unauthorized local runtime; that is not
  an authorization blocker.
- The runtime must reconcile durable enrollment/catalog state before accepting
  `auth_helper_invoke`, while remaining fail-closed for uncertain mutations.
- No raw credentials, helper stdout, production claims, or provider reachability
  are allowed in fixtures or evidence.
- Paired consumer qualification is tracked by asb-tui AR-1323; this local ASB
  task does not modify the asb-tui repository.
