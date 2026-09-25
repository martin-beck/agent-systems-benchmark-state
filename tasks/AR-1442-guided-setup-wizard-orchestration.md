---
{
  "branch": "feature/ar-1442-guided-setup-wizard-orchestration",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1441",
    "AR-1316",
    "AR-1328",
    "AR-1436"
  ],
  "id": "AR-1442",
  "next_action": "Complete ASB CLI catalog-driven setup/reconfiguration qualification against the existing versioned contracts; preserve separate TUI wiring as downstream cross-repository work.",
  "observed_branch": "feature/ar-1442-guided-setup-wizard-orchestration",
  "observed_dirty": 0,
  "observed_head": "2872a31f2ee90ac5df1a47203b2a618b1829cfec",
  "owner": "",
  "plan": "../plans/AR-1442.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Qualify ASB CLI first-run and reconfiguration of agents, providers, auth methods, models and defaults.",
  "task_revision": 10,
  "title": "Guided setup wizard orchestration",
  "updated_at": "2026-09-25T15:23:41+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1442"
}
---

The wizard is a first-class product boundary, not a documentation layer. It
must delegate to authoritative ASB catalogs and runtime-owned credential
enrollment and remain safe when the provider is not reachable.

The first-customer ASB gate is CLI-only. Standalone asb-tui consumption remains
independently tracked and is not modified by this AR.

- 2026-09-25T15:20:07+00:00: Dependencies AR-1441, AR-1316, AR-1328 and AR-1436 are released;
  promote the catalog-driven ASB setup/reconfiguration contract while keeping provider reachability
  optional.

- 2026-09-25T15:20:10+00:00: Claimed by coordinator-ar1442.

- 2026-09-25T15:20:47+00:00: Recorded command exit 0; command argv SHA-256
  952c230617030cdb9ac7cccad9580e9e872536ff13620701c6f7dde17602e980.

- 2026-09-25T15:21:20+00:00: Recorded command exit 0; command argv SHA-256
  952c230617030cdb9ac7cccad9580e9e872536ff13620701c6f7dde17602e980.

- 2026-09-25T15:22:19+00:00: Recorded command exit 0; command argv SHA-256
  4437157c2910dd27cf5a92a2d8bf16b93f23354fadb4ffcbcd0bd71ee4100d2c.

- 2026-09-25T15:22:40+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-09-25T15:23:41+00:00: ASB CLI-only guided setup qualification complete against protected
  merge 2872a31f. Focused setup contract tests 5/5 passed: machine-readable preflight,
  unknown-option rejection, cross-provider/model mismatch rejection without provider contact, atomic
  no-half-apply failure, and validated selection commit. Full asb-cli library suite 107 passed.
  Existing catalog/provider-plan/config contracts remain authoritative; TUI wiring is separate and
  untouched.
