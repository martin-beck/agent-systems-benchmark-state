---
{
  "branch": "feature/ar-1232",
  "checkpoint_commit": "2543a4c213bc7a1f9b426cb8c0b95d815a0bf7e4",
  "claim_expires": "",
  "depends_on": ["AR-1232"],
  "id": "AR-1244",
  "next_action": "Review and publish signed AR-1232 head 2543a4c through protected-main gates; then verify exact-main post-merge workflows.",
  "observed_branch": "feature/ar-1232",
  "observed_dirty": 0,
  "observed_head": "2543a4c213bc7a1f9b426cb8c0b95d815a0bf7e4",
  "owner": "",
  "plan": "../plans/AR-1244.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Publish strict-replay supervision integration.",
  "task_revision": 1,
  "title": "Publish AR-1232 strict-replay supervision",
  "updated_at": "2026-09-16T09:32:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1244-publish"
}
---

Publish only the reviewed AR-1232 implementation. Preserve fail-closed network isolation and all
unrelated history; use the repository development workflow for every Git, gate, review, and merge
mutation.
