---
{
  "branch": "feature/agent-openhands",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T06:49:55+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103"
  ],
  "id": "AR-0309",
  "next_action": "Design a bounded Python shim against pinned OpenHands Software Agent SDK v1.45.0 and inspect its exact event, confirmation, metrics, persistence, and cancellation APIs.",
  "observed_branch": "feature/agent-openhands",
  "observed_dirty": 0,
  "observed_head": "3a07b57b8265d98eeebbcd4fd21339d72fac0663",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0309.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run a maintained MIT OpenHands SDK or canonical headless client.",
  "task_revision": 6,
  "title": "Implement maintained OpenHands SDK client adapter",
  "updated_at": "2026-09-08T03:55:22+00:00",
  "worktree_key": "agent-systems-benchmark-agent-openhands"
}
---
## AR-0309

Run a maintained MIT OpenHands SDK or canonical headless client.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-08T03:49:45+00:00: Verified AR-0101, AR-0102 and AR-0103 are durably done. Selected
  highest-priority safe disjoint leaf after P1 authorization/dependency/path blockers; OpenHands
  module and fixtures do not overlap active frontend protocol, verifier integrity, or kernel
  diagnostics paths.

- 2026-09-08T03:49:55+00:00: Claimed by contracts_20260906.

- 2026-09-08T03:50:41+00:00: Recorded command exit 0; command argv SHA-256
  07036c4ad1b996ca80da9bef22d326a3298e0fa2af6aa940f96f17b07676a4b3.

- 2026-09-08T03:55:22+00:00: Official-source boundary resolved: use active MIT
  OpenHands/software-agent-sdk v1.45.0, signed tag commit 49ea74587c376b90700f6eff128c3d9b57585d27
  and tree 639a6850375c0d8e04c9f045a5a74c15fea0406c. Exclude OpenHands/OpenHands enterprise paths.
  Do not use OpenHands-CLI 1.16.0 for this adapter: although MIT and maintained, its latest release
  pins older SDK/tools 1.21.0 and documented headless operation is always-approve, so it cannot
  expose the required bounded confirmation policy as cleanly as the SDK.
