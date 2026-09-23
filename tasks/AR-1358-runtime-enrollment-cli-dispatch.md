---
{
  "branch": "feature/ar-1358-runtime-enrollment-cli-dispatch",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-24T00:26:05+00:00",
  "depends_on": [
    "AR-1357"
  ],
  "id": "AR-1358",
  "next_action": "Promote after AR-1357 is done, then wire asb run/sweep through runtime-attested enrollment records with fail-closed positive and negative tests.",
  "observed_branch": "feature/ar-1358-runtime-enrollment-cli-dispatch",
  "observed_dirty": 0,
  "observed_head": "a6f1915aa5117f0296b1b8f4b9c4692a956b3d86",
  "owner": "codex-asb-runtime-attested-enrollment-luna56",
  "plan": "../plans/AR-1358-runtime-enrollment-cli-dispatch.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Consume runtime-attested enrollment records in asb run and sweep without exposing authority.",
  "task_revision": 6,
  "title": "Runtime enrollment CLI dispatch",
  "updated_at": "2026-09-23T22:26:27+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1358-runtime-enrollment-cli-dispatch"
}
---

Coordinator-created consumer repair for AR-1329 after AR-1357 delivered the
runtime-owned record transport. Do not touch asb-tui or weaken replay/offline
gates.

- 2026-09-24T00:30:00+00:00: Created because AR-1329's remaining dispatch gap is
  distinct from the completed runtime transport primitive.

- 2026-09-23T22:26:02+00:00: AR-1357 is done with merge and post-merge evidence; promote the
  runtime-owned CLI dispatch consumer repair.

- 2026-09-23T22:26:05+00:00: Claimed by codex-asb-runtime-attested-enrollment-luna56.

- 2026-09-23T22:26:12+00:00: Recorded command exit 0; command argv SHA-256
  1068daf3aa96ce8739897a79927707a44394caf77b7b575a00fed63e8d9a446d.

- 2026-09-23T22:26:27+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.
