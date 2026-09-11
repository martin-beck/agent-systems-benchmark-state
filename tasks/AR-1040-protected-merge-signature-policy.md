---
{
  "branch": "fix/protected-merge-signature-policy",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T02:06:18+00:00",
  "depends_on": [],
  "id": "AR-1040",
  "next_action": "Create isolated exact-cad9fa97 worktree, pin official GitHub Web Flow key, and implement narrowly gated protected-main verification with adversarial tests.",
  "owner": "codex-ar1040-merge-signature-20260911",
  "plan": "../plans/AR-1040.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Align offline signature policy with the repository-required GitHub merge path.",
  "task_revision": 4,
  "title": "Reconcile protected-merge signature verification",
  "updated_at": "2026-09-11T00:06:59+00:00",
  "worktree_key": "agent-systems-benchmark-protected-merge-signature-policy"
}
---

Protected main merge `cad9fa9777aaca45b9ee62801d89168c5f3e8c32` has a matching raw DCO
trailer and GitHub API verification `valid`, but offline Repository quality rejects GitHub's PGP
signature because it recognizes only the local SSH allowed signer. Fix the policy contradiction
without allowing Web Flow signatures on ordinary commits or PR heads. This AR owns no TUI code.

- 2026-09-11T00:06:02+00:00: Protected main demonstrates a live signature-policy contradiction;
  focused recovery is dependency-ready.

- 2026-09-11T00:06:18+00:00: Claimed by codex-ar1040-merge-signature-20260911.

- 2026-09-11T00:06:59+00:00: Initial audit complete: task/plan and ASB
  DEVELOPMENT/ARCHITECTURE/QUALITY read; origin/main is cad9fa9777aaca45b9ee62801d89168c5f3e8c32.
  Earlier handoffctl status attempt was an invocation-only error because status is not a supported
  subcommand; task JSON directly confirms the active claim.
