---
{
  "branch": "fix/ar-1245-postmerge-dco-evidence",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T11:37:31+00:00",
  "depends_on": [
    "AR-1242",
    "AR-1243"
  ],
  "id": "AR-1245",
  "next_action": "Open/review commit 3e12d64; run protected-main CI and post-merge checks.",
  "observed_branch": "fix/ar-1245-postmerge-dco-evidence",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb_ar1237_launch_bridge_worker",
  "plan": "../plans/AR-1245.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Repair DCO admission for the immutable PR-192 GitHub merge while preserving strict future checks.",
  "task_revision": 4,
  "title": "Post-merge DCO admission evidence",
  "updated_at": "2026-09-16T09:41:06+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1245"
}
---

Implement only AR-1245. Preserve the published merge commit and use the repository's documented
development and handoffctl workflow. Do not weaken future signed/DCO admission or touch runtime,
bundle, or TUI code.

- 2026-09-16T09:36:28+00:00: PR #192 merged with unsigned GitHub merge commit; approved forward-only
  DCO evidence repair without history rewrite.

- 2026-09-16T09:37:31+00:00: Claimed by asb_ar1237_launch_bridge_worker.

- 2026-09-16T09:41:06+00:00: Implemented signed commit 3e12d64 in clean worktree. Exact hash
  75248467... is accepted only after verifying two parents; unknown synthetic merge remains
  rejected. cargo fmt, clippy, workspace tests (166 passed, 1 ignored) and targeted flaky test pass.
  Full negative suite is blocked locally because the configured external-tools directory lacks
  shellcheck.
