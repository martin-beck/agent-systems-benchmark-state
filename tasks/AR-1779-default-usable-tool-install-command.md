---
{
  "branch": "feature/ar-1779-default-usable-tool-install-command",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1777", "AR-1778"],
  "id": "AR-1779",
  "next_action": "Make asb tool install supported-id resolve, acquire/build, validate, and register a usable project-local executable tool by default.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1779-default-usable-tool-install-command.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class": "integration-test", "evidence_digest": "", "evidence_ref": "", "spec_ref": "specs/AR-1779.json", "spec_revision": 1, "status": "pending"},
  "spec_ref": "specs/AR-1779.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Make default asb tool install produce and verify a usable project-local supported executable tool without manual source copying.",
  "task_revision": 1,
  "title": "Default usable tool-install command",
  "updated_at": "2026-10-10T09:49:36+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1779-default-usable-tool-install-command"
}
---

Change the public experience to `asb tool install <supported-id> [--project PATH]`.
It resolves the catalog, reuses a compatible verified local binary when one is
available, otherwise retrieves a verified official prebuilt artifact, otherwise
uses the pinned source-build/dependency fallback. A success is valid only after
an executable smoke check proves the installed entrypoint can be used
by the target ASB adapter. Persist the complete receipt and active usable state
only after that check passes.

Keep explicit local-file or fixture installation as a clearly labelled
development/import mode rather than the default supported-user flow. Offer
`status`, `repair`, `update`, and `remove` semantics that expose current
catalog/source/digest/platform/build state without downloading on read-only
commands. Human output must explain selection, downloads/builds, reused versus
created dependencies, result location, and next action; JSON retains its stable
machine contract and never includes secrets. The command must not silently use a
wrong binary, silently fall back to an unrelated tool, or claim installation when
the adapter smoke check failed.
