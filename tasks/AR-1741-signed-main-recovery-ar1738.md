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
  "observed_head": "0c100e4624a6dc3972660dc24713940d87753709",
  "owner": "codex-ar1738-rustup-permission",
  "plan": "../plans/AR-1741-signed-main-recovery-ar1738.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1741.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Recover signed protected-main provenance after the preserved GitHub-generated AR-1738 merge.",
  "task_revision": 5,
  "title": "Signed protected-main recovery for AR-1738",
  "updated_at": "2026-10-08T09:50:08+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1741-signed-main-recovery-ar1738"
}
---

AR-1741 is an independent publication-integrity recovery for AR-1738/PR #504.
Preserve historical merge `2f7387e`; do not rewrite or force-update protected
main. AR-1740 is a separate publication incident and is intentionally excluded.

- 2026-10-08T09:48:24+00:00: Claimed by codex-ar1738-rustup-permission.

- 2026-10-08T09:49:37+00:00: Recorded command exit 0; command argv SHA-256
  8955c1a4f9d012421dbe400da15b32bf2b4d6fd81e7b7229f8d7a55bcc174a6c.
