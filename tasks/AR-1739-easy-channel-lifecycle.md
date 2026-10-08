---
{
  "branch": "feature/ar-1739-easy-channel-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T11:18:19+00:00",
  "depends_on": [],
  "id": "AR-1739",
  "next_action": "Promote after reviewing the existing asb easy and TUI channel contracts; implement the native dependency-free build/install/update/test/status/remove lifecycle with explicit channel selection, a visibly labelled development stable mock, and safe human/JSON guidance.",
  "owner": "codex-ar1739-easy-lifecycle",
  "plan": "../plans/AR-1739-easy-channel-lifecycle.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1739.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Provide a user-friendly native asb easy lifecycle for building, installing, updating a selected channel, testing, inspecting, rolling back, and removing ASB without cargo or Make commands.",
  "task_revision": 4,
  "title": "Add easy channel build, install, update, and test lifecycle",
  "updated_at": "2026-10-08T09:18:19+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1739-easy-channel-lifecycle"
}
---

ASB currently exposes build and lifecycle operations through lower-level commands and `asb tui` and
developer-oriented command sequences. Users should not need to remember Cargo,
source checkout, or install commands to select a channel, update it, test the
installation, or recover from a failed update.

For development qualification, `--channel stable` is deliberately a local
mock channel. It exercises the stable-shaped UX and lifecycle without fetching
or depending on a future public stable channel. Every human and JSON result must
identify this as a development mock, and no mock run may create public-release
or stable-promotion evidence.

Extend the existing native `asb easy` family with `build`, `install`, `update`,
`test`, `status`, `rollback`, and `remove` rather than adding a Makefile or
Justfile. A Make/Just wrapper would require an extra tool and a source checkout,
while the ASB binary already owns channel manifests, installation state,
diagnostics, rollback, human output, and JSON contracts. Keep the lifecycle
provider-free by default and preserve all stable/production fail-closed gates.

- 2026-10-08T09:17:44+00:00: dependencies verified; ready for isolated implementation worker

- 2026-10-08T09:18:15+00:00: Claimed by codex-ar1739-easy-lifecycle.

- 2026-10-08T09:18:19+00:00: Heartbeat by codex-ar1739-easy-lifecycle.
