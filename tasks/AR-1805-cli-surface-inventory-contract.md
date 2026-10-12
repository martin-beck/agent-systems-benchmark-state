---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1773"
  ],
  "id": "AR-1805",
  "next_action": "Create the canonical public command-surface manifest and contract tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1805-cli-surface-inventory-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "",
    "evidence_ref": "",
    "spec_ref": "specs/AR-1805.json",
    "spec_revision": 1,
    "status": "pending"
  },
  "spec_ref": "specs/AR-1805.json",
  "spec_revision": 1,
  "status": "open",
  "summary": "Define one complete machine-checked inventory of every public ASB command and subcommand surface.",
  "task_revision": 2,
  "title": "CLI Surface Inventory and UX Contract",
  "updated_at": "2026-10-12T10:47:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1805-cli-surface-contract"
}
---

## Outcome

ASB has one generated, reviewable inventory of every public command route,
subcommand, alias, mode, selector, and output contract. New public routes fail
CI unless they declare human output, JSON, help, and discovery behavior.

## Acceptance

- Discover the complete CLI tree from parser/dispatch source and compare it to
  a versioned command-surface manifest; unknown, duplicate, or untested routes
  fail deterministically.
- Record whether each route has human output, `--json`, `--help`, and `--list`,
  including selector domains and mutation/network behavior.
- Cover root, project, config, auth, provider, agent, model/catalog, tool,
  workload, run, sweep, report, compare, replay, serve/control, easy, and TUI
  routes; aliases and error-only paths are not exempt.

- 2026-10-12T10:47:39+00:00: AR-1773 is done; dependency-safe P0 CLI contract work is ready
