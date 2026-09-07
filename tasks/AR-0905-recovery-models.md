---
{
  "branch": "feature/recovery-models",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T01:28:29+00:00",
  "depends_on": [
    "AR-0102",
    "AR-0104",
    "AR-0204",
    "AR-0503"
  ],
  "id": "AR-0905",
  "next_action": "Translate Agent Relay's TLA+/Alloy/executable-model pattern to ASB run and replay domains.",
  "observed_branch": "feature/recovery-models",
  "observed_dirty": 1,
  "observed_head": "462bd04a349dfbea1797c8a358e390544d51471e",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0905.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Apply bounded formal models to run lifecycle, leases, recovery, replay cursors and uncertain external effects.",
  "task_revision": 9,
  "title": "Model execution recovery and worker fencing",
  "updated_at": "2026-09-07T22:33:03+00:00",
  "worktree_key": "agent-systems-benchmark-recovery-models"
}
---
## AR-0905

Apply bounded formal models to run lifecycle, leases, recovery, replay cursors and uncertain external effects.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T22:14:48+00:00: Dependencies AR-0102, AR-0104, AR-0204 and AR-0503 are durably done.
  Selected highest-priority ready compatible task after excluding native-capacity work overlapping
  active AR-0707, AR-0832 with its plan-level blocked AR-0703 dependency, and schema/contract work
  overlapping active AR-0840. Declared recovery-model branch/worktree and remote ref are absent;
  docs/formal verifier/trace scope is disjoint from active AR-0505 replay integration.

- 2026-09-07T22:14:58+00:00: Claimed by replay_20260906.

- 2026-09-07T22:16:20+00:00: Recorded command exit 0; command argv SHA-256
  0c45238c27b38f287d8c104a676b9c8d75deee6985f9f757151d54374b7753fb.

- 2026-09-07T22:17:45+00:00: Recorded command exit 1; command argv SHA-256
  22ff8758a1a185c5a55cf2cf09eaba75a48facd2ca96d86d1fb9607238352604.

- 2026-09-07T22:28:29+00:00: Heartbeat by replay_20260906.

- 2026-09-07T22:33:03+00:00: Recorded command exit 0; command argv SHA-256
  4b9c02191e39deea93bb2bf1b82d95036ccf7daeee565282b629333974ee25fd.
