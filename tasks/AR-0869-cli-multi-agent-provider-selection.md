---
{
  "branch": "feature/cli-multi-agent-provider-selection",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T00:38:23+00:00",
  "depends_on": [
    "AR-0313",
    "AR-0318",
    "AR-0320",
    "AR-0801"
  ],
  "id": "AR-0869",
  "next_action": "Implement and qualify explicit CLI selection of several agents and one advertised provider profile.",
  "observed_branch": "feature/cli-multi-agent-provider-selection",
  "observed_dirty": 0,
  "observed_head": "559fbcc825234bb98a64ba554a53f38b004d24f6",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0869.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Select several agents and apply one preconfigured provider profile through inspectable command-line options.",
  "task_revision": 7,
  "title": "Add CLI multi-agent provider selection",
  "updated_at": "2026-09-08T21:42:46+00:00",
  "worktree_key": "agent-systems-benchmark-cli-multi-agent-provider-selection"
}
---
## AR-0869

Add a safe command-line workflow for selecting several agents and one advertised provider profile.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T21:05:54+00:00: Fresh dependency/overlap audit: AR-0869 dependencies AR-0313, AR-0318,
  AR-0320, and AR-0801 are all durably done. Its CLI-only agent/provider selection, plan rendering,
  validation, help/examples and focused-test paths are disjoint from active AR-0806 TUI
  history/analysis and AR-0855 state/vendor header work. Higher numeric-frontier P1 leaves are not
  safely claimable: AR-0704 lacks its plan-required external authorization, AR-0819 overlaps active
  TUI/frontend paths, and AR-0832 is blocked by AR-0703 in its complete plan. Declared worktree and
  branch do not exist locally or remotely. Promote AR-0869 as the highest-priority compatible ready
  leaf.

- 2026-09-08T21:05:57+00:00: Claimed by replay_20260906.

- 2026-09-08T21:38:23+00:00: Heartbeat by replay_20260906.

- 2026-09-08T21:38:42+00:00: Recorded command exit 0; command argv SHA-256
  ebc36c2c7dfb453910e2ae0d87dd6d64b4a10b9fb1f64d02c36afd5d0c1cc857.

- 2026-09-08T21:42:46+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.
