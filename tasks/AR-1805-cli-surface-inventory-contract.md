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
  "observed_branch": "feature/ar-1805-cli-surface-inventory-contract",
  "observed_dirty": 5,
  "observed_head": "5a6c5477cd171606da3aaa0cae9950453ea8dc5c",
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
  "task_revision": 20,
  "title": "CLI Surface Inventory and UX Contract",
  "updated_at": "2026-10-12T10:51:29+00:00",
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

- 2026-10-12T10:49:10+00:00: Recorded command exit 1; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-12T10:49:15+00:00: Recorded command exit 101; command argv SHA-256
  7d789907f8bd7249669c4d354efb08f8894ba0a32eb28132f2cf709015b77d60.

- 2026-10-12T10:49:22+00:00: Recorded command exit 1; command argv SHA-256
  a15b746008790e08dea19da8af5d20d0e3932ab4639acecc408627965619d892.

- 2026-10-12T10:49:51+00:00: Recorded command exit 101; command argv SHA-256
  585b909aff778920875f1293802eecd19965d82e9b7f836b224ba4022d3ecb05.

- 2026-10-12T10:50:04+00:00: Recorded command exit 0; command argv SHA-256
  c7b136d59b59e995a7ff41972401a98a7ebfda8695ada4faf168c197f1d3a6a4.

- 2026-10-12T10:50:10+00:00: Recorded command exit 101; command argv SHA-256
  585b909aff778920875f1293802eecd19965d82e9b7f836b224ba4022d3ecb05.

- 2026-10-12T10:50:36+00:00: Recorded command exit 0; command argv SHA-256
  c7b136d59b59e995a7ff41972401a98a7ebfda8695ada4faf168c197f1d3a6a4.

- 2026-10-12T10:50:41+00:00: Recorded command exit 101; command argv SHA-256
  585b909aff778920875f1293802eecd19965d82e9b7f836b224ba4022d3ecb05.

- 2026-10-12T10:50:55+00:00: Recorded command exit 0; command argv SHA-256
  c7b136d59b59e995a7ff41972401a98a7ebfda8695ada4faf168c197f1d3a6a4.

- 2026-10-12T10:51:02+00:00: Recorded command exit 0; command argv SHA-256
  585b909aff778920875f1293802eecd19965d82e9b7f836b224ba4022d3ecb05.

- 2026-10-12T10:51:09+00:00: Recorded command exit 0; command argv SHA-256
  e3a8da7e2c0eacda08755ef9ff4d6170bbb1421cb5c4e0c98e4e32810bf795d4.

- 2026-10-12T10:51:25+00:00: Recorded command exit 0; command argv SHA-256
  0ae8d3cd282cf47957ebcacbb3e74a0653509096421cc6af5e72b977cb685cb8.

- 2026-10-12T10:51:29+00:00: Recorded command exit 0; command argv SHA-256
  d06fe1f0ef13e94b35e06e538f18fc903560b2ec5e78afb4900e4feda220a360.
