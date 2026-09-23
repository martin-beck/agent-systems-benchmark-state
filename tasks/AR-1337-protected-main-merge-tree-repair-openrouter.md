---
{
  "branch": "repair/ar-1337-openrouter-merge-tree-admission",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1226"],
  "id": "AR-1337",
  "next_action": "Reproduce the post-merge protected-main merge-tree mismatch from merge 56c882a, repair admission or merge procedure without weakening policy, and rerun every exact-main workflow.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1337.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Repair the protected-main merge-tree admission defect exposed after the OpenRouter provider merge.",
  "task_revision": 1,
  "title": "Repair protected-main merge-tree admission after OpenRouter merge",
  "updated_at": "2026-09-23T06:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1337-protected-main-merge-tree-repair"
}
---

The exact-head PR #249 checks were green, but post-merge Repository quality run
35825987339 rejected protected-main merge 56c882a06337a2b58c761bddaef2c743cba65712:
the protected-main merge tree differs from the reviewed topic tree. Reproduce
the mismatch against the immutable base and head, identify whether the merge
method or admission calculation is wrong, and repair the durable flow. Preserve
signature, DCO, exact-head and merge-tree checks; never add a one-off hash
exception or bypass the policy.

Acceptance requires a clean signed+DCO repair, independent review, exact-head
CI, a protected-main merge whose computed tree equals the reviewed topic tree,
and successful post-merge Repository quality, formal, fault, portability and
Rust workflows. Record the exact merge parents, tree IDs, run IDs and any
remaining evidence limits without private paths or credentials.
