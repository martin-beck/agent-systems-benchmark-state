---
{
  "branch": "test/mockagents-executable-qualification",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T10:40:19+00:00",
  "depends_on": [
    "AR-0888",
    "AR-0889"
  ],
  "id": "AR-0896",
  "next_action": "Qualify the exact MockAgents v0.5.0 executable against the complete hostile synthetic protocol and isolation suite; do not unblock AR-0890 unless every required case passes.",
  "observed_branch": "test/mockagents-executable-qualification",
  "observed_dirty": 4,
  "observed_head": "adac76558387cb0bdd09e2ba6cbfe49b9bc205be",
  "owner": "codex-longrun-mockagents-20260909",
  "plan": "../plans/AR-0896.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Qualify one pinned MockAgents executable before deterministic-double CI integration.",
  "task_revision": 7,
  "title": "Qualify the pinned MockAgents executable",
  "updated_at": "2026-09-09T10:00:46+00:00",
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
