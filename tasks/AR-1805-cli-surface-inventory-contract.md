---
{
  "branch": "",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1773"
  ],
  "id": "AR-1805",
  "next_action": "Create and claim a narrowly scoped forward-only provenance-recovery successor for PR #608; use tools/integration/merge_pr.py from clean exact base 5c843a12 and reviewed topic 0fec6465, publish signed local merge, then watch all exact-main gates.",
  "observed_branch": "feature/ar-1805-cli-surface-inventory-contract",
  "observed_dirty": 0,
  "observed_head": "0fec6465dbb1934904fef8d9f79dd1c565c661fc",
  "owner": "",
  "plan": "../plans/AR-1805-cli-surface-inventory-contract.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_acceptance": {
    "evidence_class": "contract-test",
    "evidence_digest": "sha256:7b085cf88dca04871a16632551b51f2ced70c2c3af263c8354fed143f0a1b512",
    "evidence_ref": "quality/AR-1815-protected-main-recovery-postmerge-receipt.txt",
    "spec_ref": "specs/AR-1805.json",
    "spec_revision": 1,
    "status": "pass"
  },
  "spec_ref": "specs/AR-1805.json",
  "spec_revision": 1,
  "status": "done",
  "summary": "Independent exact-head review accepted PR #608 at 0fec6465.",
  "task_revision": 91,
  "title": "CLI Surface Inventory and UX Contract",
  "updated_at": "2026-10-12T12:51:12+00:00",
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

- 2026-10-12T11:01:22+00:00: Recorded command exit 0; command argv SHA-256
  c822935410cd969a0a6e9fec16a591f6bd2774067a880d74878f98acedd4c0b5.

- 2026-10-12T11:01:34+00:00: Diagnosed deterministic pre-rebase failure: stale legacy diagnostic
  catalog line collision classified the output-path test as cancellation. Repaired catalog call-site
  mapping, signed commit, rebased onto 5c843a12, pushed with force-with-lease; post-rebase focused
  test passes 5/5.

- 2026-10-12T11:04:47+00:00: Recorded command exit 101; command argv SHA-256
  e535f40e03c7cd48e895dace0edc7ff83c02ad09a44cf0b8426e54fc2fc98605.

- 2026-10-12T11:05:01+00:00: Independent exact-head review of PR #608 at
  a0d780b0f818f6468bedf07702fc83cc54eebef2: SSH signatures and matching DCO trailers valid on both
  commits; git diff --check and privacy scan clean; focused command_surface_contract,
  diagnostic_journey, and asb-cli lib gates pass (437/437). Full cargo test -p asb-cli --tests
  --offline fails at diagnostic_contract ordinary_cli_producers_are_mechanically_closed: legacy CLI
  producer lacks reviewed identity for human.rs lines 3570, 3611, 3702-3707. Hosted checks were
  still pending and no TLC was run. Review disposition: changes requested; do not merge.

- 2026-10-12T11:05:42+00:00: Recorded command exit 0; command argv SHA-256
  fa3556b91735662cfe83b71d9218fca3cbbd41fb3c466a9d180a974143ef7bb0.

- 2026-10-12T11:05:54+00:00: Recorded command exit 101; command argv SHA-256
  48b75ec0431f217b7d1f9a2964a5a9cbf647f9b16e8c15d68d0e40ca11aa1381.

- 2026-10-12T11:06:08+00:00: Recorded command exit 0; command argv SHA-256
  3a78f27b6b4270907b02783cb551cc88cb937373e0a4e09c3d20e420911c8261.

- 2026-10-12T11:06:15+00:00: Recorded command exit 0; command argv SHA-256
  48b75ec0431f217b7d1f9a2964a5a9cbf647f9b16e8c15d68d0e40ca11aa1381.

- 2026-10-12T11:06:23+00:00: Recorded command exit 0; command argv SHA-256
  2aa764634b50a5fec8cc28d39f303117e8ad4cf857f66d269b098312732c9776.

- 2026-10-12T11:06:29+00:00: Recorded command exit 0; command argv SHA-256
  7849067484dd266b7be7e0d13f8f49837a19e90ee4caa3234907339f0b3f2d11.

- 2026-10-12T11:06:34+00:00: Recorded command exit 0; command argv SHA-256
  dc2aa747a3964d16be0bef1d87399c73679354c72cb0db4d9d565249ffcf6b0d.

- 2026-10-12T11:06:43+00:00: Full workspace test exposed stale catalog identities at human.rs 3570,
  3611, 3702-3707; refreshed generated catalog mappings, signed commit 5cb931f5, pushed. Review
  requested again.

- 2026-10-12T11:07:24+00:00: Recorded command exit 101; command argv SHA-256
  e535f40e03c7cd48e895dace0edc7ff83c02ad09a44cf0b8426e54fc2fc98605.

- 2026-10-12T11:07:49+00:00: Recorded command exit 0; command argv SHA-256
  01188ac7de4608c6dee41a5154e05bd53d58ff7cd80eb70fc617e627b46f0726.

- 2026-10-12T11:07:53+00:00: Recorded command exit 0; command argv SHA-256
  31b44c1d3600cbfed72a8c428c5e1083e263b7249aa1eef9cbccd569df9d579a.

- 2026-10-12T11:08:10+00:00: Second independent exact-head review of PR #608 at
  5cb931f55fa7210afd58e70de25f0d2fce67107a: all three commits SSH-signed with matching DCO; diff
  check/privacy clean; diagnostic_contract 9/9, command_surface_contract, diagnostic_journey, and
  asb-cli lib 437/437 pass. Full cargo test -p asb-cli --tests --offline now fails only at human_cli
  executable_public_family_golden_is_inventory_complete_and_privacy_safe: expected golden family
  count 28 but inventory has 29 after adding workload. Hosted checks remain pending; no TLC run.
  Review remains changes requested; do not merge.

- 2026-10-12T11:08:30+00:00: Recorded command exit 0; command argv SHA-256
  6236eb7675e97867f72179ae41293a169904d9e9b0146b06aeb39eb3ff92c36c.

- 2026-10-12T11:08:34+00:00: Recorded command exit 0; command argv SHA-256
  5d5282b1ec42131875c7f5dfbea224f68a9388320ed659d33b2020965e73facd.

- 2026-10-12T11:08:38+00:00: Recorded command exit 0; command argv SHA-256
  950cb2aee7f8731ccc4bd187ebe8633061f38051121bc4f2733f238e2b766ca9.

- 2026-10-12T11:08:43+00:00: Recorded command exit 0; command argv SHA-256
  dc2aa747a3964d16be0bef1d87399c73679354c72cb0db4d9d565249ffcf6b0d.

- 2026-10-12T11:09:11+00:00: Recorded command exit 0; command argv SHA-256
  fb2e756a36f808ddc9cc1e39321efec13418ef7cb2515fb0de38b129f44c88af.

- 2026-10-12T11:09:19+00:00: Reviewed deterministic failures repaired: stale human diagnostic
  catalog identities and 28-vs-29 public family golden count. Full asb-cli test suite passes after
  commit 0fec6465; repeat independent review required.

- 2026-10-12T11:13:33+00:00: Heartbeat by asb-queue-next-luna56.

- 2026-10-12T11:22:38+00:00: Recorded command exit 0; command argv SHA-256
  fb2e756a36f808ddc9cc1e39321efec13418ef7cb2515fb0de38b129f44c88af.

- 2026-10-12T11:23:01+00:00: Fresh exact-head review at 2026-10-12T13:22Z: verified PR #608 head
  0fec6465dbb1934904fef8d9f79dd1c565c661fc and base 5c843a12e976bc7be6c32e9fc653e566bdf20450;
  working tree clean; git diff --check clean; all four commits SSH-signed and DCO-trailer matched;
  cargo test -p asb-cli --tests --offline passed 437 unit tests plus all applicable integration
  suites; hosted Emulated aarch64 and Policy/coverage/supply-chain checks terminal success, no TLC
  executed. Review disposition accepted for exact head.

- 2026-10-12T11:23:08+00:00: Recorded command exit 0; command argv SHA-256
  700758e1fbf138bc47ef0b38a5e947d6d89916d45bced0eea81fd69ed0b07923.

- 2026-10-12T11:23:15+00:00: Fresh independent exact-head review accepted PR #608 at
  0fec6465dbb1934904fef8d9f79dd1c565c661fc. Full diff reviewed (7 files, 167 insertions, 8
  deletions); SSH signatures and matching DCO trailers valid on all four PR commits; git diff
  --check and changed-file privacy scan clean. Full cargo test -p asb-cli --tests --offline passes.
  All hosted PR checks terminal-success. No TLC/model checks run locally. Review disposition
  accepted; merge may proceed through protected exact-head workflow.

- 2026-10-12T11:24:09+00:00: Post-merge verification at 2026-10-12T13:24Z: PR #608 exact head
  0fec6465 merged onto base 5c843a12 as 15c80511. AArch64 and pre-merge checks were green.
  Exact-main runs 38242303503 (Repository quality) and 38242303428 (Portable protected-main
  provenance) failed with identical policy error: protected-main merge committer is not the local
  integration identity. This is a coordinator/release-identity gate failure, not a product test
  failure; no gate weakened and no force action taken.

- 2026-10-12T11:25:17+00:00: Released completed merge worker lease; post-merge provenance-policy
  repair remains open.

- 2026-10-12T11:26:59+00:00: Claimed by ar1805_postmerge_repair.

- 2026-10-12T11:27:13+00:00: Claimed for post-merge recovery. Exact runs 38242303503 and 38242303428
  failed solely because GitHub Web Flow merge 15c80511 committer is GitHub <noreply@github.com>;
  merge parents/tree and reviewed evidence are preserved. Existing AR-1794 local merge tool is the
  authorized repair path; no gate weakening or history rewrite.

- 2026-10-12T11:38:36+00:00: Post-merge provenance recovery is transferred to successor AR-1815;
  preserved merge 15c80511 and exact-main failures remain documented.

- 2026-10-12T12:50:59+00:00: Claimed by ar1805_postmerge_repair.

- 2026-10-12T12:51:06+00:00: AR-1805 route inventory was independently accepted at 0fec6465 and
  merged as preserved tree 15c80511; AR-1815 forward-only signed recovery e57982a restored
  exact-main provenance and all required post-merge gates. Receipt is the durable evidence for the
  completed contract result.

- 2026-10-12T12:51:12+00:00: AR-1805 complete. Route inventory and contract tests were accepted on
  exact reviewed head 0fec6465, PR #608 preserved the reviewed tree as 15c80511, and AR-1815
  recovered protected-main provenance forward-only as signed merge e57982a. All PR and exact-main
  required workflows are terminal-success; see
  quality/AR-1815-protected-main-recovery-postmerge-receipt.txt. No TLC or live-provider gate was
  required.
