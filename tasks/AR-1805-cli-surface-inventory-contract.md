---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-12T12:52:52+00:00",
  "depends_on": [
    "AR-1773"
  ],
  "id": "AR-1805",
  "next_action": "PR #608 opened at exact head 01631b5bbe14ba856a8993cc7fb8c4be6aa76fcc. Await independent review and all non-TLC hosted checks, then protected exact-head merge and post-merge verification.",
  "observed_branch": "feature/ar-1805-cli-surface-inventory-contract",
  "observed_dirty": 0,
  "observed_head": "a0d780b0f818f6468bedf07702fc83cc54eebef2",
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
  "task_revision": 52,
  "title": "CLI Surface Inventory and UX Contract",
  "updated_at": "2026-10-12T11:01:18+00:00",
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

- 2026-10-12T10:51:40+00:00: Recorded command exit 0; command argv SHA-256
  b6e455353a42b3d0459c297428f6c730ebf429b1704bbe1cf07d321241f50af0.

- 2026-10-12T10:51:50+00:00: Recorded command exit 0; command argv SHA-256
  a54fbb8e1da25f8e24ed1affa79342bf52d318fb92ff400187269fc1e962afef.

- 2026-10-12T10:52:00+00:00: Implemented versioned command-surface manifest, workload human route
  inventory, and drift/negative-journey contract tests; focused tests pass.

- 2026-10-12T10:52:52+00:00: Heartbeat by asb-queue-next-luna56.

- 2026-10-12T10:57:38+00:00: Recorded command exit 1; command argv SHA-256
  bf6fa10bb2fbebb3498754e1cfd69c8d355a36a64d45c0028b7cea192e6fa427.

- 2026-10-12T10:57:43+00:00: Recorded command exit 101; command argv SHA-256
  77ea5679682b2c559a6e8501f727beb4f5921ad3e1a7c873e9001094ee2e46ac.

- 2026-10-12T10:57:51+00:00: Recorded command exit 101; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T10:57:58+00:00: Recorded command exit 101; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T10:58:04+00:00: Recorded command exit 101; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T10:58:10+00:00: Recorded command exit 101; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T10:58:15+00:00: Recorded command exit 101; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T10:59:01+00:00: Recorded command exit 101; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T10:59:23+00:00: Recorded command exit 101; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T10:59:44+00:00: Recorded command exit 1; command argv SHA-256
  12ef2c204bc0319d6cc7d72b7e7e2731d0f7a08439681a5448028359fd520a71.

- 2026-10-12T10:59:51+00:00: Recorded command exit 0; command argv SHA-256
  461215b81ce75d33846a9de97fe0c0a914ca4a7d55c65c81fbce8c82336bd591.

- 2026-10-12T11:00:00+00:00: Recorded command exit 0; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T11:00:10+00:00: Recorded command exit 0; command argv SHA-256
  2aa764634b50a5fec8cc28d39f303117e8ad4cf857f66d269b098312732c9776.

- 2026-10-12T11:00:15+00:00: Recorded command exit 0; command argv SHA-256
  2984e06b93b1bc245f4ce5665cdca42302d4a78ce09c9d8bb66006cb7afbca5d.

- 2026-10-12T11:00:23+00:00: Recorded command exit 0; command argv SHA-256
  0cf5535f3b9dc120e36eed832572b6cd5cbdc308c2e2509adc167d3dfe444a2a.

- 2026-10-12T11:00:33+00:00: Recorded command exit 0; command argv SHA-256
  ffa66fa7a7ae6ecf96ac7e32424bddc3cc8980c6c61297043a47ccadd44cb247.

- 2026-10-12T11:00:37+00:00: Recorded command exit 0; command argv SHA-256
  7b867f45f681d4bca4dddffe98cc3b3bc0636d7b62a86fed2d5b481fe5e71f04.

- 2026-10-12T11:00:47+00:00: Recorded command exit 0; command argv SHA-256
  dc2aa747a3964d16be0bef1d87399c73679354c72cb0db4d9d565249ffcf6b0d.

- 2026-10-12T11:01:02+00:00: Recorded command exit 0; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T11:01:10+00:00: Recorded command exit 0; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T11:01:14+00:00: Recorded command exit 0; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T11:01:18+00:00: Recorded command exit 0; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.
