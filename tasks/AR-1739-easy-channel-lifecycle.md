---
{
  "branch": "feature/ar-1739-easy-channel-lifecycle",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T11:18:19+00:00",
  "depends_on": [],
  "id": "AR-1739",
  "next_action": "Add focused lifecycle contract tests, run the exact current-main gates, then review and publish the PR.",
  "observed_branch": "feature/ar-1739-easy-channel-lifecycle",
  "observed_dirty": 3,
  "observed_head": "1a5888ce1c96414015bbaf223ac42302871d47fe",
  "owner": "codex-ar1739-easy-lifecycle",
  "plan": "../plans/AR-1739-easy-channel-lifecycle.md",
  "priority": "P1",
  "schema_version": 1,
  "spec_ref": "specs/AR-1739.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Provide a user-friendly native asb easy lifecycle for building, installing, updating a selected channel, testing, inspecting, rolling back, and removing ASB without cargo or Make commands.",
  "task_revision": 14,
  "title": "Add easy channel build, install, update, and test lifecycle",
  "updated_at": "2026-10-08T09:30:48+00:00",
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

- 2026-10-08T09:18:27+00:00: Recorded command exit 0; command argv SHA-256
  8bf703ba30d60fa6ec9451cd6cc87f9e3c335b7cd3dd545fee5de054d6de7eab.

- 2026-10-08T09:19:37+00:00: Recorded command exit 0; command argv SHA-256
  a8ead32e951460d96f5ef53ad26f5f0381d0ad41b3580927aa87ff0757275af4.

- 2026-10-08T09:20:46+00:00: Recorded command exit 101; command argv SHA-256
  3efbc34b923d266e0fc349bbfd5dac9463a898353cd31bf3028eb4016520a7fd.

- 2026-10-08T09:24:11+00:00: Implemented native asb easy
  build/install/update/test/status/rollback/remove with explicit dev/stable mock channel validation,
  --yes/--dry-run, versioned JSON mock labeling, provider-free test behavior, completion and
  EASY_LIFECYCLE.md docs. cargo test -p asb-cli --lib --no-run --locked passes after fixing one
  dispatcher return-type error (prior exit 101). Build/journey retry is currently contending on
  shared coordinator lock held by another worker; no product failure observed.

- 2026-10-08T09:28:45+00:00: Recorded command exit 0; command argv SHA-256
  a8ead32e951460d96f5ef53ad26f5f0381d0ad41b3580927aa87ff0757275af4.

- 2026-10-08T09:30:15+00:00: Recorded command exit 0; command argv SHA-256
  a781977e20250c15b70b9e0d848860886820271b280fa4591200b3ede69bc2ec.

- 2026-10-08T09:30:48+00:00: Recorded command exit 0; command argv SHA-256
  9bb05bc481223373dff232a927ca06c7e75b291c6f6a43f851b4494c69fdd97e.
