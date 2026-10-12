---
{
  "branch": "feature/ar-1811-development-formal-workflow-separation",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1811",
  "next_action": "Promote and implement the workflow separation on a clean exact-main worktree; ordinary development PRs must not invoke TLC/Alloy, while the final-delivery PR lane retains the sole formal execution gate.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1811-development-formal-workflow-separation.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Separate development CI from the single future final-delivery TLC gate without weakening Kani, Loom, policy, Rust, privacy, or release assurance.",
  "task_revision": 2,
  "title": "Development/formal workflow separation",
  "updated_at": "2026-10-12T09:45:28+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1811-development-formal-workflow-separation"
}
---

Implement a fail-closed workflow contract in which ordinary pull requests and
development pushes never invoke TLC/Alloy or require their result. Preserve
Kani, Loom, Rust, policy, privacy, fuzz, supply-chain, and platform checks.
Keep exactly one explicitly labelled final-delivery workflow path that invokes
TLC/Alloy, is not claimable as development work, and remains required only for
the finished-product delivery PR. Add positive and negative workflow-contract
tests and update the generated quality documentation.

- 2026-10-12T09:45:28+00:00: No dependencies; promote workflow separation to remove TLC from
  development CI while preserving final-delivery formal gate.
