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
  "task_revision": 13,
  "title": "Implement maintained OpenHands SDK client adapter",
  "updated_at": "2026-09-08T04:04:01+00:00",
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

- 2026-09-08T03:57:02+00:00: Recorded command exit 1; command argv SHA-256
  10c15ae9e6c277a981542655bf485392a3392b9b9505a04cd20806bfee47a5f6.

- 2026-09-08T03:57:30+00:00: Recorded command exit 1; command argv SHA-256
  66da4fbe5e6464ee9d68e3834c74fb42921242e766b1a2034ec420c1ef435f21.

- 2026-09-08T03:57:44+00:00: Recorded command exit 1; command argv SHA-256
  a70f1bec1335a8a298c55d63e5fc86519af84c76b83ea9cd68b18201618a534f.

- 2026-09-08T03:57:56+00:00: Recorded command exit 0; command argv SHA-256
  e046063cdec35e5ac2dbf813eb115fc953730f3e03311593c44b06f6516ac43b.

- 2026-09-08T03:58:16+00:00: Recorded command exit 0; command argv SHA-256
  9fe3ace62ad35d411bb905dd2705e9f7d79b3ceb478a126d89f6a69420d7abe6.

- 2026-09-08T04:00:15+00:00: Recorded command exit 2; command argv SHA-256
  cb76f2eadc7d84a08940326c617e2bf9e8f94bdca84bf86b5de2ac1eaaae9c80.

- 2026-09-08T04:04:01+00:00: Recorded command exit 0; command argv SHA-256
  62f7e88cca66e94b3960fdd21aea322fc297518ec6d1f8e85a57859d59815363.
