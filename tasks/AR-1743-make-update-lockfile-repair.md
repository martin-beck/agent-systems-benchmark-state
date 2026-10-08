---
{
  "branch": "repair/ar-1743-make-update-lockfile",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T13:19:56+00:00",
  "depends_on": [],
  "id": "AR-1743",
  "next_action": "Promote for implementation after confirming the current Makefile failure and preserving unrelated work.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1743-make-update",
  "plan": "../plans/AR-1743-make-update-lockfile-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1743.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Repair make update so dependency refresh never combines Cargo lockfile mutation with --locked and fails with cannot update the lock file.",
  "task_revision": 5,
  "title": "Repair Make update lockfile handling",
  "updated_at": "2026-10-08T11:21:48+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1743-make-update-lockfile"
}
---

The repository Makefile currently runs `cargo +1.93.0 update --locked` from
`make update`. Cargo refuses this combination when dependency resolution would
change Cargo.lock, producing `cannot update the lock file`. Repair the target
without weakening the pinned-toolchain, clean-tree, fast-forward, offline-after-
install, or bounded-command contracts.

The repaired workflow must make the intended distinction explicit: dependency
refresh may update the lockfile only through a deliberate, reviewable operation;
validation/build/test/install paths remain locked and must not mutate it. Add
actionable diagnostics and positive plus negative tests for an unchanged lock,
an intentional lock refresh, a dirty tree, and a refresh failure. Preserve all
unrelated product changes and record the exact failure and recovery evidence.

- 2026-10-08T11:19:42+00:00: Confirmed make update reproduces cargo update --locked lockfile
  mutation failure; repair scope and tests are defined.

- 2026-10-08T11:19:56+00:00: Claimed by codex-ar1743-make-update.

- 2026-10-08T11:21:19+00:00: Recorded command exit 2; command argv SHA-256
  071dd2d3df583a7d847ec9572789b07c5be72fc731397c41d0f076181e333214.

- 2026-10-08T11:21:48+00:00: Recorded command exit 2; command argv SHA-256
  071dd2d3df583a7d847ec9572789b07c5be72fc731397c41d0f076181e333214.
