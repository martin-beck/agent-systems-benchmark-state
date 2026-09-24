---
{
  "branch": "codex/ar-1431-stale-base",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-25T00:19:23+00:00",
  "depends_on": [
    "AR-1427"
  ],
  "id": "AR-1431",
  "next_action": "Reproduce the AR-1216 post-merge merge-tree failure and repair stale-base protected-main requalification before releasing AR-1216.",
  "observed_branch": "codex/ar-1431-stale-base",
  "observed_dirty": 0,
  "observed_head": "e82e2e6f8a03815fb5e39bf64c59dac9911e3312",
  "owner": "ar1431-stale-base-luna56",
  "plan": "../plans/AR-1431-protected-main-stale-base-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent stale-base sequential merges from passing review but failing protected-main merge-tree policy.",
  "task_revision": 7,
  "title": "Protected-main stale-base merge requalification repair",
  "updated_at": "2026-09-24T22:22:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1431"
}
---

Failure evidence is immutable: AR-1216 post-merge Repository Quality run
`36066329347` rejected merge `e82e2e6` because the protected target advanced from
review base `d9eb6c2` to `8d1889b` before publication.  This AR must preserve
that incident and must not waive the policy.

- 2026-09-24T22:16:46+00:00: AR-1427 is done; promote repair for AR-1216 protected-main stale-base
  merge-tree failure 36066329347.

- 2026-09-24T22:19:23+00:00: Claimed by ar1431-stale-base-luna56.

- 2026-09-24T22:22:12+00:00: Recorded command exit 0; command argv SHA-256
  aae66aab4fdf8f873e2ba3b94e322d63ce9d5491cf6dfef4475319458372bc01.

- 2026-09-24T22:22:26+00:00: Recorded command exit 0; command argv SHA-256
  e068eb8b14408e12418fa448e734a204f65427e486bbbb0aba93576c5f8c4f26.
