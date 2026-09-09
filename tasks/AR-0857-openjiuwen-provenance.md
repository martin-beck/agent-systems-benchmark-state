---
{
  "branch": "feature/openjiuwen-provenance",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T04:48:17+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103",
    "AR-0310",
    "AR-0315",
    "AR-0317",
    "AR-0503",
    "AR-0855"
  ],
  "id": "AR-0857",
  "next_action": "Pin official source, package, dependency closure, license, executable digest, protocol mode, and supported platform before any adapter claim.",
  "observed_branch": "feature/openjiuwen-provenance",
  "observed_dirty": 0,
  "observed_head": "05d30426919a6a08818be6a26b44356669e37645",
  "owner": "replay_20260909",
  "plan": "../plans/AR-0857.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Pin OpenJiuwen source, package, and license provenance.",
  "task_revision": 10,
  "title": "Pin OpenJiuwen source, package, and license provenance",
  "updated_at": "2026-09-09T02:50:40+00:00",
  "worktree_key": "agent-systems-benchmark-openjiuwen-provenance"
}
---
## AR-0857

Pin official source, package, dependency closure, license, executable digest, protocol mode, and supported platform before any adapter claim.

This phase cannot claim support from mocks, parser fixtures, source inspection, compilation, or mutable artifacts. If its executable evidence is unavailable, leave this child blocked with exact provenance evidence while the sibling agent series proceeds.

- 2026-09-09T02:48:11+00:00: All eight dependencies are done; promote OpenJiuwen provenance as the
  next highest-priority dependency-ready implementation track.

- 2026-09-09T02:48:14+00:00: Claimed by replay_20260909.

- 2026-09-09T02:48:17+00:00: Heartbeat by replay_20260909.

- 2026-09-09T02:48:40+00:00: Recorded command exit 1; command argv SHA-256
  ca1d169a1e60eead106f7e38f4a4f06b253d5ed306c90b04ef637013256ca566.

- 2026-09-09T02:49:08+00:00: Recorded command exit 0; command argv SHA-256
  19766149c12eac4a9990a83b585c9ef2b1bab01a1070c80a4e64fdbb4ffde972.

- 2026-09-09T02:49:53+00:00: Recorded command exit 0; command argv SHA-256
  6e2da119873f397d0c934eebd5febde79653c170772610aefae6a1a96b81bba9.

- 2026-09-09T02:50:10+00:00: Recorded command exit 0; command argv SHA-256
  edf1baf5c4cc61af37795993bd3eae4f0639c1383c089f262644f61f5820424f.

- 2026-09-09T02:50:40+00:00: Recorded command exit 2; command argv SHA-256
  584ec4529c0c66af37e063034fc6ea853115c09ec17193b1aed7b83036987365.
