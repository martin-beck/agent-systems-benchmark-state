---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1773", "AR-1805"],
  "id": "AR-1806",
  "next_action": "Implement route-by-route human-output journey tests and repair non-human default output.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1806-human-output-contract-audit.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {"evidence_class":"contract-test","evidence_digest":"","evidence_ref":"","spec_ref":"specs/AR-1806.json","spec_revision":1,"status":"pending"},
  "spec_ref": "specs/AR-1806.json",
  "spec_revision": 1,
  "status": "planned",
  "summary": "Guarantee clear human-default success, warning, and failure journeys for every ASB CLI route.",
  "task_revision": 1,
  "title": "Exhaustive Human Output Contract Audit",
  "updated_at": "2026-10-12T10:15:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1806-human-output-contract"
}
---

## Outcome

Every public command and subcommand produces concise, useful human output by
default. JSON appears only after explicit `--json`; commands such as `asb tool
foo` may not leak raw machine envelopes in normal human mode.

## Acceptance

- Generate route-by-route success, invalid-input, unavailable-prerequisite, and
  recoverable-failure transcript tests from AR-1805's inventory.
- Assert default output names the result, concrete cause, and next command or
  action; do not expose raw JSON, debug structures, private paths, or secrets.
- Assert `--json` preserves its schema and is silent on human/status streams;
  quiet and writer-level behavior remain governed by AR-1775.
- Repair divergent routes using the shared output router/diagnostic catalog,
  not ad-hoc formatting; add regression fixtures for every repaired family.
