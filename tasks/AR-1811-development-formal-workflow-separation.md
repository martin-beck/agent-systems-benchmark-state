---
{
  "branch": "feature/ar-1811-development-formal-workflow-separation",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T11:52:21+00:00",
  "depends_on": [],
  "id": "AR-1811",
  "next_action": "Promote and implement the workflow separation on a clean exact-main worktree; ordinary development PRs must not invoke TLC/Alloy, while the final-delivery PR lane retains the sole formal execution gate.",
  "observed_branch": "feature/ar-1811-development-formal-workflow-separation",
  "observed_dirty": 0,
  "observed_head": "309d16ca998679d26119e3c322ba082f45a957c5",
  "owner": "ar1811-formal-separation-luna56",
  "plan": "../plans/AR-1811-development-formal-workflow-separation.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Separate development CI from the single future final-delivery TLC gate without weakening Kani, Loom, policy, Rust, privacy, or release assurance.",
  "task_revision": 21,
  "title": "Development/formal workflow separation",
  "updated_at": "2026-10-12T09:52:21+00:00",
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

- 2026-10-12T09:48:12+00:00: Recorded command exit 0; command argv SHA-256
  046c0503ca59c590c18bd9ee7f8ae745744a0d24fb528ac7b48bd2f7be1a9447.

- 2026-10-12T09:48:34+00:00: Recorded command exit 0; command argv SHA-256
  d4d121064219dc7626da449789752a7f5ea2d79dbfe07ee4ffb9550dcb55c556.

- 2026-10-12T09:48:55+00:00: Recorded command exit 0; command argv SHA-256
  ec62c79b228f7de760486bd74752568c5534a803fad538ace016b239037d50bb.

- 2026-10-12T09:49:02+00:00: Recorded command exit 0; command argv SHA-256
  24f496bc51708459a0d1eb7a46999509df26464e87b1aad90564d77869e0e019.

- 2026-10-12T09:49:23+00:00: Heartbeat by ar1811-formal-separation-luna56.

- 2026-10-12T09:49:33+00:00: Recorded command exit 0; command argv SHA-256
  37a902b766633d89a3fe82e64dfe47ad2b2e736573bbed9015dd677621568ba9.

- 2026-10-12T09:49:37+00:00: Recorded command exit 0; command argv SHA-256
  3edd81fbfb0f6e8c1fa3b6845bc219d4957726f4bc9913c211359cff0359cbeb.

- 2026-10-12T09:49:54+00:00: Recorded command exit 0; command argv SHA-256
  542d74b51c6a99d32ca08bb3859111a8be1b3e5b4da052b37818d4491a7ca19b.

- 2026-10-12T09:50:06+00:00: Recorded command exit 0; command argv SHA-256
  b8ed48420f139dcbf658b4282285a9753813070c85cd0b874ffb5a83b17cd07a.

- 2026-10-12T09:50:16+00:00: Recorded command exit 0; command argv SHA-256
  7ae4f1187d992d3fe3e48f28ed0fd94fe58d516b6ac92347a0ef892ccfd039e0.

- 2026-10-12T09:52:21+00:00: Heartbeat by ar1811-formal-separation-luna56.
