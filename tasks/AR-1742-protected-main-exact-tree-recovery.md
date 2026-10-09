---
{
  "branch": "repair/ar-1742-pr505-exact-tree",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T05:37:41+00:00",
  "depends_on": [],
  "id": "AR-1742",
  "next_action": "Promote after reviewing the preserved PR #505 mismatch and exact signed local integration procedure.",
  "observed_branch": "repair/ar-1742-pr505-exact-tree",
  "observed_dirty": 1,
  "observed_head": "69bf9029a4976f14739cf4c25949428ff2fe0bb7",
  "owner": "codex-asb-ar1742-recovery-20261009",
  "plan": "../plans/AR-1742-protected-main-exact-tree-recovery.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1742.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Recover PR #505 protected-main exact-tree publication failure without rewriting history.",
  "task_revision": 7,
  "title": "PR #505 exact-tree recovery",
  "updated_at": "2026-10-09T02:40:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1742-exact-tree-recovery"
}
---

This successor preserves the immutable PR #505 publication failure and owns
only its signed forward exact-tree recovery. It is separate from AR-1741 and
from AR-1740's default-lifecycle PR #507.

- 2026-10-08T09:55:14+00:00: dependencies verified; dedicated successor for preserved PR #505
  exact-tree recovery, separate from AR-1741 and AR-1740 PR #507

- 2026-10-08T16:13:17+00:00: Claimed by codex-asb-ar1742-exact-tree-20261008.

- 2026-10-08T16:16:41+00:00: Assignment superseded before product work; no AR-1742 product, branch,
  or worktree mutation performed.

- 2026-10-09T02:37:41+00:00: Claimed by codex-asb-ar1742-recovery-20261009.

- 2026-10-09T02:40:12+00:00: Recorded command exit 0; command argv SHA-256
  b3fabb7e2b1107ab3c87549923e4b2bb3fae0eff1d057d8b2d573fe8c66b4572.
