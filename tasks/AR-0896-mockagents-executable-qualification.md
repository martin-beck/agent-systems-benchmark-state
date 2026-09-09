---
{
  "branch": "test/mockagents-executable-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T10:47:48+00:00",
  "depends_on": [
    "AR-0888",
    "AR-0889"
  ],
  "id": "AR-0896",
  "next_action": "Publish a signed+DCO follow-up commit atop 004d87252b065679d80ca9674356b47146754528, rerun exact-head and post-merge gates, then release only after all green.",
  "observed_branch": "test/mockagents-executable-qualification",
  "observed_dirty": 0,
  "observed_head": "3f1de4106adf9ad6c34759638d70e9001709ab0a",
  "owner": "codex-longrun-mockagents-20260909",
  "plan": "../plans/AR-0896.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Post-merge Repository quality failed on merge DCO; repair is preempting feature work.",
  "task_revision": 15,
  "title": "Qualify the pinned MockAgents executable",
  "updated_at": "2026-09-09T10:09:06+00:00",
  "worktree_key": "agent-systems-benchmark-mockagents-executable-qualification"
}
---
## AR-0896

Qualify only MockAgents v0.5.0 as the candidate executable selected for further
consideration by AR-0890. This repair AR exists because AR-0888 retained all four
candidates as `untested`; it must not substitute README claims or the ASB-owned
synthetic fixture for black-box executable evidence.

- 2026-09-09T09:55:13+00:00: Promote dependency-ready MockAgents executable qualification for the
  development loop.

- 2026-09-09T09:55:19+00:00: Claimed by codex-longrun-mockagents-20260909.

- 2026-09-09T09:55:41+00:00: Recorded command exit 0; command argv SHA-256
  74fbdb117ae7b36fdab88f7db32e8f5c5cceb95c78e3ace34c70a2284134fb26.

- 2026-09-09T10:01:30+00:00: Material milestone: isolated worktree contains closed lock parser,
  bounded archive/license verifier, unprivileged loopback subprocess qualification, protocol probes,
  deterministic semantic hashes, public fixture evidence, and negative archive tests. The exact
  v0.5.0 linux-amd64 release passed the implemented checks. AR-0890 remains blocked; no support
  catalog or CI workflow was changed.

- 2026-09-09T10:01:52+00:00: Recorded command exit 0; command argv SHA-256
  3b63290ca600a5863bd3bbdbf734b37a74913861a7ed3a4ba258ed703676cee1.

- 2026-09-09T10:02:01+00:00: Recorded command exit 0; command argv SHA-256
  d3720a1eb1a6c27cf813d78255327f5faee356be69b97e4080bec4a9769d789e.

- 2026-09-09T10:02:16+00:00: Recorded command exit 0; command argv SHA-256
  06c97c3ac06498041b764894cd0d33f558c890057cf487c180d031982747e27e.

- 2026-09-09T10:02:48+00:00: Heartbeat by codex-longrun-mockagents-20260909.

- 2026-09-09T10:08:28+00:00: PR #115 merged to product main as
  004d87252b065679d80ca9674356b47146754528 after all 14 exact-head checks passed. Post-merge six
  required workflows are running. The implementation does not claim AR-0890 readiness; unsupported
  cases remain explicit.

- 2026-09-09T10:09:06+00:00: Failure evidence: post-merge Repository quality run 34338578572 reports
  merge commit 004d87252b065679d80ca9674356b47146754528 lacks a matching Signed-off-by trailer. No
  product defect was reported. Feature work is preempted pending reviewed DCO repair.
