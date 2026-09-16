---
{
  "branch": "feature/ar-1250-mockagents-harness-extension",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T12:46:35+00:00",
  "depends_on": [
    "AR-0888",
    "AR-0889"
  ],
  "id": "AR-1250",
  "next_action": "Extend the MockAgents harness with explicit platform selection and hostile lifecycle, network-denial, repeat-clean-state, and emulated-AArch64 tests.",
  "observed_branch": "feature/ar-1250-mockagents-harness-extension",
  "observed_dirty": 0,
  "observed_head": "128ecddbfdb7fcfff6e257adf3237b5866aca481",
  "owner": "asb_ar1250_mockagents_harness",
  "plan": "../plans/AR-1250.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Extend the pinned MockAgents executable qualification harness.",
  "task_revision": 6,
  "title": "Extend MockAgents qualification harness",
  "updated_at": "2026-09-16T10:48:03+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1250"
}
---

Implement only the linked AR-1250 plan using the ASB development documentation and handoffctl.
Use the exact pinned artifacts recorded by AR-1249. Preserve offline-after-install, network denial,
privacy, signature, DCO, and exact-tree gates; do not claim support from host inference or cross-builds.

- 2026-09-16T10:45:50+00:00: AR-1249 artifact audit identified explicit platform-selection and
  hostile/lifecycle harness gaps; promote focused repair.

- 2026-09-16T10:46:35+00:00: Claimed by asb_ar1250_mockagents_harness.

- 2026-09-16T10:46:48+00:00: Recorded command exit 0; command argv SHA-256
  c9f44399408b4505dc741f93b9769056dea0675c4b67400b05a133b96b6e3012.

- 2026-09-16T10:48:03+00:00: Recorded command exit 0; command argv SHA-256
  6bc4f61e7c167faf9c0f4525a105ae1cb82775733c2f11aad43efd6daa7346b7.
