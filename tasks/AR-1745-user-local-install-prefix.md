---
{
  "branch": "feature/ar-1745-user-local-install-prefix",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T15:06:58+00:00",
  "depends_on": [
    "AR-1740"
  ],
  "id": "AR-1745",
  "next_action": "Audit the exact current-main install targets and define the shared user-local prefix contract before implementation.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "codex-ar1745-install",
  "plan": "../plans/AR-1745-user-local-install-prefix.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1745.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1745.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Make ASB development installation place the asb executable at the invoking user's $HOME/.local/bin/asb by default, with a safe explicit prefix override.",
  "task_revision": 3,
  "title": "Install ASB into the invoking user's local bin",
  "updated_at": "2026-10-08T13:06:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1745-user-local-install-prefix"
}
---

The current Make install workflow must be easy for a fresh user and must not
assume root access or place a user's development binary in a system prefix.
By default, `make install` (and any ASB command implementing the same install
contract) shall install `asb` at `$HOME/.local/bin/asb` for the user performing
the install. A caller may provide an explicit safe prefix for packaging or CI.

The implementation must not silently write outside the selected prefix, must
not alter unrelated TUI/runtime installation semantics, and must provide
clear PATH guidance when `$HOME/.local/bin` is not already on PATH.

- 2026-10-08T13:06:55+00:00: Promote high-priority user-local install-prefix AR after dependency
  audit; AR-1740 is done and exact current main shows repository-local .make/install default.

- 2026-10-08T13:06:58+00:00: Claimed by codex-ar1745-install.
