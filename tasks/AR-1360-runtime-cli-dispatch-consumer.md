---
{
  "branch": "feature/ar-1360-runtime-cli-dispatch-consumer",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1359"
  ],
  "id": "AR-1360",
  "next_action": "Promote after AR-1359 is done, then implement the production asb run/sweep consumer for authenticated runtime enrollment receipts with fail-closed tests.",
  "observed_branch": "feature/ar-1360-runtime-cli-dispatch-consumer",
  "observed_dirty": 0,
  "observed_head": "be9af3d6fb22818e95f51b9640b10c5eb6e043f3",
  "owner": "",
  "plan": "../plans/AR-1360-runtime-cli-dispatch-consumer.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Connect authenticated runtime enrollment receipts to asb run and sweep without exposing authority.",
  "task_revision": 7,
  "title": "Runtime CLI dispatch consumer",
  "updated_at": "2026-09-23T23:02:32+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1360-runtime-cli-dispatch-consumer"
}
---

Successor for blocked AR-1358. Do not touch asb-tui, weaken AR-1329 fail-closed
behavior, or let CLI arguments synthesize provider authority.

- 2026-09-24T00:00:00+00:00: Created after AR-1359 merged the authenticated
  control/runtime bridge and all post-merge workflows passed. This task owns the
  remaining asb run/sweep dispatch consumer only.

- 2026-09-23T22:58:10+00:00: Dependency AR-1359 is done with merged bridge and all seven post-merge
  workflows green; promote CLI dispatch consumer.

- 2026-09-23T22:58:13+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T22:58:59+00:00: Recorded command exit 0; command argv SHA-256
  2003e0b8ce3713dc69d0040c6745e35f14ca5395b5e4352506ce3b311314b770.

- 2026-09-23T23:00:38+00:00: Recorded command exit 0; command argv SHA-256
  b7c438686581cf292b6cd41497ceabb3af42dfed57e04dfd6cc89efed8e2d15b.

- 2026-09-23T23:02:13+00:00: Recorded command exit 0; command argv SHA-256
  3efcb93fc4c8985c1a6fe4b3e5dff0b8822462f5ef60f4619564e0f9d85a0f23.

- 2026-09-23T23:02:32+00:00: Blocked after exact protected-main audit at be9af3d6: asb-control
  exposes ControlClient but no receipt/validated-chain control call; asb-runtime exposes receipt
  ingestion only, while acquire_from_record and LiveProviderBootstrapSpec remain crate-private. CLI
  therefore cannot safely consume a runtime receipt or obtain runtime-owned policy/tools/lease/relay
  authority. Do not expose caller-supplied authority. Create successor AR for authenticated control
  receipt source and runtime-owned dispatch factory, then resume CLI run/sweep consumer.
