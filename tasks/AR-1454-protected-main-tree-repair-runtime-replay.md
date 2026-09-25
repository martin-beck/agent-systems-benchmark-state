---
{
  "branch": "repair/ar-1454-protected-main-tree-repair-runtime-replay",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1451",
    "AR-1452"
  ],
  "id": "AR-1454",
  "next_action": "Promote a current-main descendant repair, preserve the failed post-merge policy evidence, and require exact two-parent tree-equal merge plus seven post-merge successes.",
  "observed_branch": "repair/ar-1454-protected-main-tree-repair-runtime-replay",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1454.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair the protected-main tree mismatch after the runtime replay merge.",
  "task_revision": 2,
  "title": "Protected-main tree-equality repair for runtime replay",
  "updated_at": "2026-09-25T20:57:31+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1454-protected-main-tree-repair-runtime-replay"
}
---

PR #328 merged at `452f3ca29390ab37cf3aff8c813b92b54b163b20`, but the exact-main
repository-policy gate rejected the merge because the reviewed topic tree did
not contain the then-current base tree. Preserve that failure and the merge as
immutable evidence; do not weaken the policy or rewrite protected history.

Create the smallest reviewed descendant from the current protected `main` that
records this repair and exercises the normal non-squash merge path. The repair
must have a signed+DCO topic commit, exact-head required checks, independent
review, a two-parent merge whose tree equals the reviewed topic and deterministic
base/topic merge preview, and all seven exact-main post-merge workflows green.

After successful post-merge verification, update AR-1450 with the repair and
failure evidence and release both AR-1450 and this repair AR only when the
runtime replay capability remains covered by its original tests and no gate is
waived. Keep asb-tui out of scope.

- 2026-09-25T20:57:31+00:00: Post-merge policy rejected PR #328 because stale topic tree differed
  from protected-main merge tree; current-main descendant repair is dependency-safe.
