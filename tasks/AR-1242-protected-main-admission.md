---
{
  "branch": "fix/protected-main-admission",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T09:15:37+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0897"
  ],
  "id": "AR-1242",
  "next_action": "Promote after dependency verification; audit protected-branch merge modes and add fail-closed admission controls for signed SSH+DCO merges.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "c261af069c5ce7ecb84b2acfc56f12d2a4cb116a",
  "owner": "asb_ar1242_merge_admission",
  "plan": "../plans/AR-1242.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent protected-main admission from creating unsigned GitHub merge commits.",
  "task_revision": 3,
  "title": "Enforce signed protected-main admission",
  "updated_at": "2026-09-16T08:45:37+00:00",
  "worktree_key": "agent-systems-benchmark-protected-main-admission"
}
---
## AR-1242

Repair the recurring protected-main admission gap exposed by unsigned GitHub-generated merges
`1c07e907`, `a7a64bcc`, and `606375f`. Preserve all published history and add a forward-only,
reviewed integration boundary that cannot silently create an unsigned or non-DCO main commit.

This AR owns repository settings/documentation, merge admission tooling, and policy fixtures only.
It must not weaken native, formal, privacy, signature, DCO, exact-tree, or post-merge gates.

- 2026-09-16T08:45:19+00:00: Dependencies AR-0003 and AR-0897 verified done; recurring unsigned
  protected-main merges require admission-control implementation.

- 2026-09-16T08:45:37+00:00: Claimed by asb_ar1242_merge_admission.
