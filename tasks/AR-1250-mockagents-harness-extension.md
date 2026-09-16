---
{
  "branch": "feature/ar-1250-mockagents-harness-extension",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0888", "AR-0889"],
  "id": "AR-1250",
  "next_action": "Extend the MockAgents harness with explicit platform selection and hostile lifecycle, network-denial, repeat-clean-state, and emulated-AArch64 tests.",
  "observed_branch": "feature/ar-1250-mockagents-harness-extension",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1250.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Extend the pinned MockAgents executable qualification harness.",
  "task_revision": 1,
  "title": "Extend MockAgents qualification harness",
  "updated_at": "2026-09-16T10:46:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1250"
}
---

Implement only the linked AR-1250 plan using the ASB development documentation and handoffctl.
Use the exact pinned artifacts recorded by AR-1249. Preserve offline-after-install, network denial,
privacy, signature, DCO, and exact-tree gates; do not claim support from host inference or cross-builds.
