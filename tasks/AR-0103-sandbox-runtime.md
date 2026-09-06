---
{
  "branch": "feature/sandbox-runtime",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-06T19:44:13+00:00",
  "depends_on": [
    "AR-0102"
  ],
  "id": "AR-0103",
  "next_action": "Implement isolated asb-runtime sandbox/resource modules and real native tests only; keep root Cargo.toml/Cargo.lock untouched until AR-0502 hands off the serialized fence.",
  "observed_branch": "feature/sandbox-runtime",
  "observed_dirty": 4,
  "observed_head": "e6a81e8644c692d5b0aa84a86b385ff4da327292",
  "owner": "contracts-20260906",
  "plan": "../plans/AR-0103.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Isolate untrusted generated code and allocate cgroup/CPU/memory/PID budgets.",
  "task_revision": 22,
  "title": "Implement isolated execution and resource leases",
  "updated_at": "2026-09-06T17:57:56+00:00",
  "worktree_key": "agent-systems-benchmark-sandbox-runtime"
}
---
## AR-0103

Isolate untrusted generated code and allocate cgroup/CPU/memory/PID budgets.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-06T17:44:13+00:00: Claimed by contracts-20260906.

- 2026-09-06T17:44:30+00:00: Recorded command exit 0; command argv SHA-256
  f5db5950ed3ebac6fe52d904adc7fa04c8635a51a93dcdb8a5d853a5095dabf8.

- 2026-09-06T17:45:41+00:00: Recorded command exit 0; command argv SHA-256
  54e2df778337ab245f4101716dc1ded6767e6c307e0ca87e616ece75bdca17a2.

- 2026-09-06T17:46:21+00:00: Recorded command exit 1; command argv SHA-256
  1bb9e1171df9c2bff2b89e43f7e63eb1fe501f03f003662952c3f581e4e0ac5b.

- 2026-09-06T17:46:58+00:00: Reconciled signed promotion repair d763c7f and fresh state, then
  claimed AR-0103 in its declared feature/sandbox-runtime worktree at exact integrated main e6a81e8.
  The earlier f166248 promotion effect is preserved and its generated-view repair is durable. Native
  probe found bubblewrap 0.9.0 and a working systemd 255 user scope with cgroup v2 controllers,
  while direct current-session cgroup writes and plain unshare user/network are unavailable. A real
  disposable MemoryMax/TasksMax/CPUQuota user scope succeeded. Design will therefore fail closed
  around exact executable/version probes, bubblewrap namespaces with network denial and minimal
  mounts, systemd user-scope resource properties, explicit CPU reservation leases disjoint from CI
  resources, bounded inputs, and documented cgroup/daemonization/platform limits. No root Cargo/lock
  mutation.

- 2026-09-06T17:48:05+00:00: Recorded command exit 1; command argv SHA-256
  db87c36f5743872c9f740f2105268de6e24fec38fa74e935a559fae7d506dbb7.

- 2026-09-06T17:48:22+00:00: Recorded command exit 0; command argv SHA-256
  41ecf8bd73d31df144c9c2b44abcf9d80e802e020e6f2bcea2ac4522765368af.

- 2026-09-06T17:52:56+00:00: Recorded command exit 0; command argv SHA-256
  f08e25c5942d67126891fb0ad368829f711225a34fc131e9c2d23b31544226b7.

- 2026-09-06T17:53:18+00:00: Recorded command exit 0; command argv SHA-256
  55330e4811159a70ea1f1fa36f542979bdc13a976674bccd6daadc497b13e922.

- 2026-09-06T17:54:51+00:00: Recorded command exit 0; command argv SHA-256
  f7688bab73070b01c61efff2a6a36e072f969058eaa52f7e898a45d5c2cdf1f2.

- 2026-09-06T17:55:08+00:00: Recorded command exit 101; command argv SHA-256
  55330e4811159a70ea1f1fa36f542979bdc13a976674bccd6daadc497b13e922.

- 2026-09-06T17:55:24+00:00: Recorded command exit 0; command argv SHA-256
  772bd5425180ceb77c624e02d6b34195aa84bbf2cdfad9956b705148186d324d.

- 2026-09-06T17:55:37+00:00: Recorded command exit 0; command argv SHA-256
  8bf3fb31fedd4b3e4bc70bef5f0f1459f25c3da4bfea60ad9e5e554fd97bd1a6.

- 2026-09-06T17:55:59+00:00: Recorded command exit 101; command argv SHA-256
  aa3ea198239b622282057090afa407ff0f6e5a461ce9c64566c4a49f2e433c59.

- 2026-09-06T17:56:20+00:00: Recorded command exit 0; command argv SHA-256
  b8fc6fdf20d89464d9e88015b4166013689114a3b4b6278ea9ebc96d4e9cfe06.

- 2026-09-06T17:57:08+00:00: Recorded command exit 101; command argv SHA-256
  8f56e04f8b968e399900e6993b1115ae07f0e705af87a57e617d6a8ae2d4f158.

- 2026-09-06T17:57:56+00:00: Recorded command exit 0; command argv SHA-256
  05fff524a446fa054e46432a604e39b5562e3d9caa20403fe0552bbf7d3f6fe3.
