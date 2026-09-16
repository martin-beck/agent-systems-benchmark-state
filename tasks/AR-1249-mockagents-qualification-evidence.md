---
{
  "branch": "feature/ar-1249-mockagents-qualification-evidence",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0888", "AR-0889"],
  "id": "AR-1249",
  "next_action": "Implement missing MockAgents hostile lifecycle, network-denial, repeat-clean-state, and emulated-AArch64 qualification evidence.",
  "observed_branch": "feature/ar-1249-mockagents-qualification-evidence",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1249.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Complete missing evidence for the pinned MockAgents executable qualification.",
  "task_revision": 1,
  "title": "Complete MockAgents executable qualification evidence",
  "updated_at": "2026-09-16T10:40:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1249"
}
---

Implement only the linked AR-1249 plan using the ASB development documentation and handoffctl.
Use the exact pinned artifact from the provenance contract; do not claim qualification from mocks,
replay-only evidence, or a cross-build. Preserve zero-runtime-dependency, offline-after-install,
network denial, privacy, signature, DCO, and exact-tree gates.
