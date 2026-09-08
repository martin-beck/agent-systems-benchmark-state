---
{
  "branch": "feature/tui-settings-wizard",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0313",
    "AR-0314",
    "AR-0803"
  ],
  "id": "AR-0804",
  "next_action": "Obtain serialized Cargo workspace/lock fence, then add standalone asb-tui crate with a pure capability-driven wizard state model and snapshot/negative tests before terminal rendering dependencies.",
  "observed_branch": "feature/tui-settings-wizard",
  "observed_dirty": 0,
  "observed_head": "76497db8f22c43762f0b5bcbc7f2549c1d17281d",
  "owner": "",
  "plan": "../plans/AR-0804.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "open",
  "summary": "Guide users through agents, providers, workloads, resources, replay, metrics, and output settings.",
  "task_revision": 7,
  "title": "Build the terminal settings wizard",
  "updated_at": "2026-09-08T15:18:01+00:00",
  "worktree_key": "agent-systems-benchmark-tui-settings-wizard"
}
---
## AR-0804

Guide users through agents, providers, workloads, resources, replay, metrics, and output settings.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T15:10:03+00:00: Coordinator verified AR-0313, AR-0314, and AR-0803 are durably done;
  promote TUI settings wizard for next safe worker slot.

- 2026-09-08T15:14:52+00:00: Claimed by quality_20260906.

- 2026-09-08T15:15:51+00:00: Recorded command exit 0; command argv SHA-256
  ae8fb19894ace7028ed539e8025f93162b05b3be4e83eed8a3aa7056e24aa5ec.

- 2026-09-08T15:16:36+00:00: Initial exact-main audit at 76497db is complete in clean declared
  worktree. AR-0803 exposes typed negotiate/capabilities/validate_settings/create_plan calls but no
  TUI crate exists. The narrow first slice is a dependency-light pure wizard model: negotiated
  choices only, explicit replay/live source, bounded repetitions/concurrency/budgets/paths,
  backtracking/reset/import/export/dry-run/final review, with launch impossible from wizard state.
  Adding the required standalone executable changes root Cargo.toml and Cargo.lock, so
  implementation is paused at the serialized workspace fence rather than mutating shared manifests
  implicitly.

- 2026-09-08T15:18:01+00:00: Coordinator recovery after repeated no-process/no-worktree checks
  despite explicit Cargo fence authorization; no product mutation observed. Reopen for reassignment.
