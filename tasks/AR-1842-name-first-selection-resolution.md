---
{
  "branch": "feature/ar-1842-name-first-selection-resolution",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1832"],
  "id": "AR-1842",
  "next_action": "Promote after AR-1832 is complete; inventory every user-facing selection and freeze the shared name-to-identity resolver contract before implementation.",
  "owner": "",
  "plan": "../plans/AR-1842-name-first-selection-resolution.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "journey", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1842.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1842.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Make logical names the only user-facing selection keys while ASB and asb-tui resolve and verify paths, hashes, versions, providers, and models internally.",
  "task_revision": 1,
  "title": "Name-first selection and internal identity resolution",
  "updated_at": "2026-10-13T00:00:00Z",
  "worktree_key": "agent-systems-benchmark-ar-1842-name-first-selection-resolution"
}
---

After AR-1832, users should choose names such as `opencode`, `openrouter`,
`free-model`, `coding`, or `tui` and never have to handle executable paths,
SHA-256 values, opaque versions, or provider endpoint identifiers. ASB must
resolve those details from the selected catalog/config entry, verify that the
resolved artifact matches its logical identity, and show only actionable
name-based choices in human-facing flows.

The resolver must be shared by the CLI and both TUI surfaces. Internal paths,
hashes, versions, and endpoints remain available to machine-readable state and
diagnostic evidence where required, but must not leak into default prompts,
status, errors, reports, or setup instructions. This AR preserves structural
safety checks, privacy guarantees, and the development-channel warning-only
scope; it does not weaken execution safety or create provider fallback.
