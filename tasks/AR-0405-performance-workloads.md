---
{
  "branch": "feature/performance-workloads",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T00:06:49+00:00",
  "depends_on": [
    "AR-0401",
    "AR-0601",
    "AR-1002",
    "AR-1007"
  ],
  "id": "AR-0405",
  "next_action": "Run compatibility spikes and accept only workload subsets with stable independent oracles.",
  "observed_branch": "feature/performance-workloads",
  "observed_dirty": 0,
  "observed_head": "5294c471425d75ef10759d766a296c0c3d841eab",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0405.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Assess SWE-Perf, SWE-fficiency and CORE-Bench for correctness-preserving optimization and reproducibility.",
  "task_revision": 15,
  "title": "Add performance and reproducibility workloads",
  "updated_at": "2026-09-08T21:48:40+00:00",
  "worktree_key": "agent-systems-benchmark-performance-workloads"
}
---
## AR-0405

Assess SWE-Perf, SWE-fficiency and CORE-Bench for correctness-preserving optimization and reproducibility.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T21:06:46+00:00: Dependencies AR-0401, AR-0601, AR-1002, and AR-1007 are durably done.
  Selected as the highest-priority compatible unclaimed leaf after AR-0869 was concurrently claimed:
  P1 AR-0819 overlaps active AR-0806 frontend paths, AR-0832 lacks plan-required
  AR-0703/native-isolation capacity, and AR-0704 lacks explicit provider/account/cost authorization.
  AR-0405 owns isolated asb-workloads performance/reproducibility plugin paths; shared Cargo/schema
  changes remain separately fenced.

- 2026-09-08T21:06:49+00:00: Claimed by contracts_20260906.

- 2026-09-08T21:38:26+00:00: Recorded command exit 0; command argv SHA-256
  7d538c03358de61b5bffffd97f01190afc2e69175ea45f97ada177734453e82a.

- 2026-09-08T21:41:55+00:00: Recorded command exit 0; command argv SHA-256
  8ed5d33113c9938b3ea588958844e2f701613b10dd15eeda7bf2e6ae3c9c0c67.

- 2026-09-08T21:45:35+00:00: Recorded command exit 0; command argv SHA-256
  e9a90e835f854182aa6ec1de3c27c13064b7beacd0beaf7ba3d1b2c315edf8bd.

- 2026-09-08T21:46:05+00:00: Recorded command exit 1; command argv SHA-256
  d8a8031fe2565c30bb123323ae03c106e9903803f0028023767ef1a8bfa2257d.

- 2026-09-08T21:46:48+00:00: Recorded command exit 0; command argv SHA-256
  8a09ca1edbfc6d293546082d9c70fd3d2ab91aa2d7804df2c74487a54876d4e4.

- 2026-09-08T21:47:13+00:00: Recorded command exit 0; command argv SHA-256
  d8a8031fe2565c30bb123323ae03c106e9903803f0028023767ef1a8bfa2257d.

- 2026-09-08T21:47:43+00:00: Recorded command exit 1; command argv SHA-256
  37ef758e03fca3f14cd5dde7222f256afd337d93e6730e180942b12083030927.

- 2026-09-08T21:48:13+00:00: Recorded command exit 0; command argv SHA-256
  0bdd0cbf88dc6b192fc6b3eb70b8e67a2a8b89381cc5df9b4470176b9964c809.

- 2026-09-08T21:48:33+00:00: Recorded command exit 0; command argv SHA-256
  aedca27882b56568314a8f22652fde8eb8637ec4f5a3cb387cc9299bfe23c70c.
