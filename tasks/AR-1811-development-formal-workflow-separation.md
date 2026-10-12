---
{
  "branch": "feature/ar-1811-development-formal-workflow-separation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T11:46:27+00:00",
  "depends_on": [],
  "id": "AR-1811",
  "next_action": "Promote and implement the workflow separation on a clean exact-main worktree; ordinary development PRs must not invoke TLC/Alloy, while the final-delivery PR lane retains the sole formal execution gate.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1811-formal-separation-luna56",
  "plan": "../plans/AR-1811-development-formal-workflow-separation.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Separate development CI from the single future final-delivery TLC gate without weakening Kani, Loom, policy, Rust, privacy, or release assurance.",
  "task_revision": 6,
  "title": "Development/formal workflow separation",
  "updated_at": "2026-10-12T09:47:21+00:00",
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

- 2026-10-12T09:46:15+00:00: Claimed by ar1811-formal-separation-luna56.

- 2026-10-12T09:46:27+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T09:46:57+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-12T09:47:21+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.
