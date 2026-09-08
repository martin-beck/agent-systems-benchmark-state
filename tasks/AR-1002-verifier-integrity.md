---
{
  "branch": "feature/verifier-integrity",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T06:46:18+00:00",
  "depends_on": [
    "AR-0103",
    "AR-0104",
    "AR-0401"
  ],
  "id": "AR-1002",
  "next_action": "Design the immutable observation and score-revision contract using Inspect and Harbor concepts.",
  "observed_branch": "feature/verifier-integrity",
  "observed_dirty": 6,
  "observed_head": "3a07b57b8265d98eeebbcd4fd21339d72fac0663",
  "owner": "replay_20260906",
  "plan": "../plans/AR-1002.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Separate immutable graders from agent work and version scoring independently of execution.",
  "task_revision": 19,
  "title": "Protect verifiers and support offline rescoring",
  "updated_at": "2026-09-08T04:03:03+00:00",
  "worktree_key": "agent-systems-benchmark-verifier-integrity"
}
---
## AR-1002

Separate immutable graders from agent work and version scoring independently of execution.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T00:44:45+00:00: Dependencies AR-0103, AR-0104, and AR-0401 are durably done. Selected
  highest-priority safe dependency-ready P1 leaf aligned with workload integrity; owned
  asb-workloads grader, asb-store observation, and asb-analysis scoring paths are disjoint from
  active AR-0505 replay integration, AR-0840 frontend protocol, and AR-0848 native-capacity
  evidence. Declared branch, worktree, remote ref, and related processes are absent.

- 2026-09-08T00:44:48+00:00: Claimed by replay_20260906.

- 2026-09-08T00:44:57+00:00: Recorded command exit 0; command argv SHA-256
  bdcaa9f19a30302c554a18a1e3bb84e9045c77088ffcbebc5ef28be0f0f65159.

- 2026-09-08T03:46:15+00:00: Heartbeat by replay_20260906.

- 2026-09-08T03:46:18+00:00: Heartbeat by replay_20260906.

- 2026-09-08T03:47:06+00:00: Recorded command exit 0; command argv SHA-256
  69b531e371883039903d27e72f53fc1cbdc379f762213dcf308e0e95b745561f.

- 2026-09-08T03:50:33+00:00: Recorded command exit 127; command argv SHA-256
  d9fcafa262ed3b569d01ec92a0b0d2e9fab9e6fb58283def6b138abe9551dcd8.

- 2026-09-08T03:51:18+00:00: Recorded command exit 0; command argv SHA-256
  d0cb03940536c1ec8566ab07b56ea04c56b1ad352662cdf0b2fa104635f966c0.

- 2026-09-08T03:56:44+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-08T03:59:23+00:00: Recorded command exit 0; command argv SHA-256
  967e6565a4a96fed0566887df27efd5e05afe8f5a8b7c0f405842dad1a56da55.

- 2026-09-08T03:59:46+00:00: Recorded command exit 0; command argv SHA-256
  7adff5c9982c58d834a2cc5c934b9108633db329eda7ac62c69875b74d5749d9.

- 2026-09-08T04:00:09+00:00: Recorded command exit 0; command argv SHA-256
  6558858c9ac17555bce93be8970259721c67e56c01e5ef9c6cd5f42c713769c3.

- 2026-09-08T04:03:03+00:00: Recorded command exit 0; command argv SHA-256
  89fd642565113e4add029a6448ac91ce2a79a14257b8224f4eefa069b09d4a5f.
