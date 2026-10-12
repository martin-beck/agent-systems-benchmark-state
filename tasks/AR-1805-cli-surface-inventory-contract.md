---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T12:47:51+00:00",
  "depends_on": [
    "AR-1773"
  ],
  "id": "AR-1805",
  "next_action": "Create the canonical public command-surface manifest and contract tests.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb-queue-next-luna56",
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
  "status": "in_progress",
  "summary": "Define one complete machine-checked inventory of every public ASB command and subcommand surface.",
  "task_revision": 5,
  "title": "CLI Surface Inventory and UX Contract",
  "updated_at": "2026-10-12T10:48:19+00:00",
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

- 2026-10-12T10:47:51+00:00: Claimed by asb-queue-next-luna56.

- 2026-10-12T10:48:10+00:00: Recorded command exit 0; command argv SHA-256
  a1159e9df3670d549d04524532629f5477ceb7deec9b45e47e8c009506ecb2c8.

- 2026-10-12T10:48:19+00:00: Recorded command exit 0; command argv SHA-256
  3aa193679a1f3bbbcda65c494e479eac70a0362107e46f55351a6fe0a3ab44bf.
