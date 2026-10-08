---
{
  "branch": "repair/ar-1741-signed-main-recovery-ar1738",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T10:48:24+00:00",
  "depends_on": [],
  "id": "AR-1741",
  "next_action": "Create a fresh recovery worktree from protected main 2f7387e, prepare a minimal signed+DCO forward-only descendant PR, and integrate it only with tools/integration/merge_pr.py after independent review.",
  "observed_branch": "repair/ar-1741-signed-main-recovery-ar1738",
  "observed_dirty": 0,
  "observed_head": "a9abcf2e63f761e314593e9abc6bf074b7418e5e",
  "owner": "codex-ar1738-rustup-permission",
  "plan": "../plans/AR-1741-signed-main-recovery-ar1738.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1741.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Recover signed protected-main provenance after the preserved GitHub-generated AR-1738 merge.",
  "task_revision": 3,
  "title": "Signed protected-main recovery for AR-1738",
  "updated_at": "2026-10-08T09:49:33+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1741-signed-main-recovery-ar1738"
}
---

AR-1741 is an independent publication-integrity recovery for AR-1738/PR #504.
Preserve historical merge `2f7387e`; do not rewrite or force-update protected
main. AR-1740 is a separate publication incident and is intentionally excluded.

- 2026-10-08T09:48:24+00:00: Claimed by codex-ar1738-rustup-permission.
