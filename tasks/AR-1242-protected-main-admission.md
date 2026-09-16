---
{
  "branch": "fix/protected-main-admission",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T09:20:26+00:00",
  "depends_on": [
    "AR-0003",
    "AR-0897"
  ],
  "id": "AR-1242",
  "next_action": "Resolve GitHub settings permission failure, then add and gate fail-closed protected-main admission fixtures.",
  "observed_branch": "fix/protected-main-admission",
  "observed_dirty": 0,
  "observed_head": "606375f613fc195f3e9ff697253f1cf20a3fec72",
  "owner": "asb_ar1242_merge_admission",
  "plan": "../plans/AR-1242.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent protected-main admission from creating unsigned GitHub merge commits.",
  "task_revision": 8,
  "title": "Enforce signed protected-main admission",
  "updated_at": "2026-09-16T08:50:26+00:00",
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

- 2026-09-16T08:46:07+00:00: Recorded command exit 0; command argv SHA-256
  f8c171345af01d7c25f3eed9491639bef708a9401fadbe78c7c5814758dfbc37.

- 2026-09-16T08:46:33+00:00: Recorded command exit 1; command argv SHA-256
  f2fe03c5bf3191d2e20bb15f3b3efff082d6b7634c123fd09cf82850b33ace2e.

- 2026-09-16T08:46:59+00:00: Created isolated worktree at main 606375f and audited repository
  settings: allow_merge_commit is still enabled. Authorized repository_settings.py --apply failed
  closed with generic GitHub settings update failure; no setting mutation can be claimed. Existing
  integration tool and policy are present, but recurring GitHub web merges 1c07e90/a7a64bc/606375f
  prove prevention remains incomplete. Preserve all history and obtain settings authority before
  retry.

- 2026-09-16T08:50:26+00:00: Heartbeat by asb_ar1242_merge_admission.
