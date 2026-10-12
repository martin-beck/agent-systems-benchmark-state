---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1805"],
  "id": "AR-1807",
  "next_action": "Implement and test complete contextual help for every public command path.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1807-complete-help-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class":"contract-test","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1807.json","spec_revision":1,"status":"pending"},
  "spec_ref": "specs/AR-1807.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Provide useful --help on every ASB command and subcommand, including the TUI lifecycle.",
  "task_revision": 1,
  "title": "Complete Contextual CLI Help Contract",
  "updated_at": "2026-10-12T10:15:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1807-complete-help"
}
---

## Outcome

`--help` works on every public ASB command path, including `asb tui --help`,
and explains purpose, syntax, selectors, output modes, safe next steps, and
where applicable `--list` discovery.

## Acceptance

- Test `--help` and `-h` on every AR-1805 route with no configuration,
  network, installation, credential, or other side effect.
- Require concise command description, argument/flag meaning, examples where
  needed, JSON/quiet behavior, and discovery/selection guidance.
- Include errors for unknown commands/arguments with contextual suggestions and
  the immediately relevant help path.
- Generate shell-completion/help consistency checks from the same route source
  so new commands cannot omit help.
