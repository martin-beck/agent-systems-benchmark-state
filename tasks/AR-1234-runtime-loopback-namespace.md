---
{
  "id": "AR-1234",
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1100", "AR-1231"],
  "next_action": "Promote after review; implement runtime-owned loopback namespace capability with fail-closed fallback.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1234.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Provide an approved runtime-owned loopback-only sandbox namespace capability.",
  "task_revision": 1,
  "title": "Runtime-owned loopback namespace capability",
  "updated_at": "2026-09-16T05:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1234"
}
---

- Created from AR-1233 architecture audit. The current bubblewrap `--unshare-all` backend has no
  approved loopback-only setup; host sharing and ambient privileged helpers are prohibited.
