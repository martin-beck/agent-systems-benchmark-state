---
{
  "branch": "feature/native-capacity-controller",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T23:36:42+00:00",
  "depends_on": [
    "AR-0701",
    "AR-0103"
  ],
  "id": "AR-0704",
  "next_action": "Rebase PR #119 onto current main after merged formal provenance repairs; preserve signed lifecycle commits, run full gates, refresh exact-head CI, and merge only when every required check is green.",
  "observed_branch": "feature/native-capacity-controller",
  "observed_dirty": 0,
  "observed_head": "28f30eea80efef5a61ea438e77402f8640564cc9",
  "owner": "asb-ar0704-formal-rebase-20260918",
  "plan": "../plans/AR-0704.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Control genuine native platform capacity lifecycle.",
  "task_revision": 129,
  "title": "Control native capacity lifecycle",
  "updated_at": "2026-09-18T21:41:23+00:00",
  "worktree_key": "agent-systems-benchmark-native-capacity-controller"
}
---
## AR-0704

Define the credential-isolated reservation/provision/teardown controller for genuine Debian and
openEuler native x86_64 cells on the authorized development host, including local resource
ceilings, availability, privacy, boot identity, and evidence. No emulation or container
substitution satisfies the native x86_64 claim. Native ARM64 is optional future evidence and
must not block this AR or its dependents.

- 2026-09-09T12:11:35+00:00: Explicit authorization received for development-host lifecycle control:
  use existing x86_64 development capacity and keep AArch64 portability under AR-0702; no external
  provider provisioning, emulated-native substitution, or cost-bearing capacity claim. Dependencies
  AR-0701 and AR-0103 are durably done and the control-policy paths are disjoint from active AR-0702
  qualification paths.

- 2026-09-09T12:11:42+00:00: Claimed by contracts_20260906.

- 2026-09-09T12:12:56+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-09T12:13:04+00:00: Recorded command exit 0; command argv SHA-256
  c107569e774896d4dc2c977d011e1a56b9a47d6f8f4f9d1193cb71e139ba20f9.

- 2026-09-09T12:16:18+00:00: Recorded command exit 0; command argv SHA-256
  52fd83c7899d290fc71d2d2d53dd973b3a98a4458397bc437c2b928999700371.

- 2026-09-09T12:16:55+00:00: Recorded command exit 1; command argv SHA-256
  5fb36337b427a59e04ba695cfeb9b4c6f76b92b6a3b6b9d795eeb474b3425af5.

- 2026-09-09T12:17:13+00:00: Recorded command exit 0; command argv SHA-256
  cf516be0d775d0d75952f479dd98da416ebafb57c63cefd7cfc80c821c636266.

- 2026-09-09T12:17:20+00:00: Recorded command exit 1; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T12:17:49+00:00: Recorded command exit 0; command argv SHA-256
  7d20d601fc0189bac8f849a131ad230afed7543e9c0ddb5015f6b5706586bbbb.

- 2026-09-09T12:17:56+00:00: Recorded command exit 1; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T12:18:32+00:00: Recorded command exit 1; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:18:57+00:00: Recorded command exit 1; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:32:32+00:00: Recorded command exit 0; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:35:46+00:00: Recorded command exit 1; command argv SHA-256
  52fd83c7899d290fc71d2d2d53dd973b3a98a4458397bc437c2b928999700371.

- 2026-09-09T12:36:50+00:00: Recorded command exit 1; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:37:08+00:00: Recorded command exit 0; command argv SHA-256
  cf516be0d775d0d75952f479dd98da416ebafb57c63cefd7cfc80c821c636266.

- 2026-09-09T12:37:15+00:00: Recorded command exit 1; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:37:40+00:00: Recorded command exit 0; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:38:10+00:00: Implemented the provider-neutral persistent lifecycle core in two new
  AR-0704-only paths. The contract binds a sanitized x86_64 capacity pseudonym, trusted class, exact
  owner/revision/deadline, and zero external cost; expired or uncertain work requires positive
  reconciliation. The ledger enforces a private owner-only root, no-follow regular files,
  nonblocking exclusive lock, bounded canonical JSON, descriptor/path identity checks, fsync-backed
  atomic replacement, and fail-closed crash residue. Ten focused tests cover deterministic
  acquire/renew/release, stale/conflicting owner, expiry, cost/architecture/privacy bounds,
  uncertain recovery, corruption, symlink, lock contention, failed-transition atomicity, mid-read
  replacement, root modes, and stale temp state. Focused unittest 10/10, Ruff format/lint, strict
  mypy, and diff-check pass. Worktree remains dirty only in new tools/capacity and tests/capacity
  paths; AR-0702 and runner paths are untouched, and no private host identifier appears.

- 2026-09-09T12:40:21+00:00: Recorded command exit 1; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T12:40:40+00:00: Recorded command exit 0; command argv SHA-256
  cf516be0d775d0d75952f479dd98da416ebafb57c63cefd7cfc80c821c636266.

- 2026-09-09T12:40:47+00:00: Recorded command exit 0; command argv SHA-256
  d66ecd27cb8a7c91fbebde4d22782e9ed4eb1878bdb8ed40e8e707d47e87951f.

- 2026-09-09T12:42:32+00:00: Implemented the provider-neutral persistent lifecycle core in two new
  AR-0704-only paths. The contract binds a sanitized x86_64 capacity pseudonym, trusted class, exact
  owner/revision/deadline, and zero external cost; expired or uncertain work requires positive
  reconciliation. The ledger enforces a private owner-only root, no-follow regular files,
  nonblocking exclusive lock, bounded canonical JSON, descriptor/path identity checks, fsync-backed
  atomic replacement, and fail-closed crash residue. Twelve focused lifecycle and CLI tests cover
  deterministic acquire/renew/release, stale/conflicting ownership, expiry, uncertain recovery,
  corruption, symlink and TOCTOU replacement, lock contention, root modes, crash residue, canonical
  bounds, and privacy-safe CLI failure. Focused unittest 12/12, Ruff format/lint, strict mypy, and
  diff-check pass. Worktree
  remains dirty only in new tools/capacity and tests/capacity paths; AR-0702 and runner paths are
  untouched, and no private host identifier appears.

- 2026-09-09T12:43:16+00:00: Recorded command exit 0; command argv SHA-256
  b294a40c71023bdb6f56bc963a539b399873645f5b5fc3af8842bbe7439ab7b8.

- 2026-09-09T12:47:33+00:00: Recorded command exit 0; command argv SHA-256
  cf516be0d775d0d75952f479dd98da416ebafb57c63cefd7cfc80c821c636266.

- 2026-09-09T12:47:40+00:00: Recorded command exit 1; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T12:48:11+00:00: Recorded command exit 0; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T12:48:42+00:00: Recorded command exit 0; command argv SHA-256
  8325c586c7c796f25ff24b39090d62c712f6add324188338ea8d5b1b25c6bba4.

- 2026-09-09T12:49:08+00:00: Recorded command exit 2; command argv SHA-256
  8e3c41a04d1c0229f0c695356ed9f5cc32a0f9b30aff1febc9451472497854f1.

- 2026-09-09T12:49:38+00:00: Recorded command exit 0; command argv SHA-256
  3049280bee1bf2c89ec265727326e27bf58c81334bfb2fa92110b845d09d6576.

- 2026-09-09T12:52:08+00:00: Prepared focused product candidate
  5a0570fbce2fa77ab4baf6b34d2632d289a5ab36 (tree 019d46abbd72997f042f57087cf8a9e79f586928, parent
  b6d04a8305ce6d49cc327e4e6d2d6fa42a88050b). Exact scope is two new paths:
  tools/capacity/lifecycle.py and tests/capacity/test_lifecycle.py; worktree clean. Commit is
  SSH-signed and contains matching Signed-off-by. Corrected immutable gates pass: 13/13 focused
  tests, source-header unittest, Ruff format, Ruff lint, strict mypy, diff-check, exact two-path
  assertion, and private-host/path/token grep. Earlier exit 2 was only an invalid checker filename;
  corrected module gate passed. Review boundary: this candidate proves the provider-neutral local
  lifecycle/ledger and CLI only; it does not yet establish native Debian/openEuler provisioning,
  boot identity/persistence, resource enforcement, or native execution evidence, so AR-0704 must
  remain in progress and unpublished pending independent review and remaining evidence.

- 2026-09-09T12:56:35+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-09-09T12:57:03+00:00: Recorded command exit 0; command argv SHA-256
  9b57e0fa8779fdac36d56e3090db5156331a5fa0911d86a5600cc1f84e8ae7f0.

- 2026-09-09T12:57:20+00:00: Recorded command exit 1; command argv SHA-256
  207bca26f3cd6de6aef4da9ae5046aedadae2889c07be40016703290f16b08e7.

- 2026-09-09T12:59:02+00:00: Recorded command exit 0; command argv SHA-256
  864fb627596632d4450a05f4c29b2ffbc8adf3fc73078f27ddfd4d833f4610a7.

- 2026-09-09T13:00:03+00:00: Recorded command exit 0; command argv SHA-256
  ba460b452c4111d861edea8fe246c9cf54da944ffb5b5bd356cbfa0980e17dfc.

- 2026-09-09T13:01:29+00:00: Recorded command exit 0; command argv SHA-256
  621bde95183defbece57b6bc035bfad1ede3bfd1f53e2d89859e89ee0facc924.

- 2026-09-09T13:01:51+00:00: Recorded command exit 0; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T13:02:33+00:00: Recorded command exit 2; command argv SHA-256
  ec4aab59b3719fdc56fad8c2d91e9def2a1587a1648e8cda0f9f5f9fdff42e90.

- 2026-09-09T13:03:00+00:00: Recorded command exit 0; command argv SHA-256
  a133831e3b85454360718aea72ad3e757029d0a81a6bcd6f00c6f9bc71fc36c4.

- 2026-09-09T13:03:17+00:00: Recorded command exit 0; command argv SHA-256
  12af6705f973a02e5cceba14c2de2e755a8df9d4cb99881a1b4773d29388d322.

- 2026-09-09T13:03:46+00:00: Recorded command exit 0; command argv SHA-256
  efdeab4bf60e4a3077431e430cd774672f749e0fa4c96d620d3262486bf1c744.

- 2026-09-09T13:04:24+00:00: Recorded command exit 0; command argv SHA-256
  2fc538a4858bf6199d1c01f0e3adc6f88817fc0c336ae73fdf072ef0eaf1234c.

- 2026-09-09T13:04:41+00:00: Recorded command exit 0; command argv SHA-256
  9ed1e35e86b0023753fc75bef7f167b8eae6c99890cba437be31f459d6fe8a86.

- 2026-09-09T13:05:04+00:00: Recorded command exit 0; command argv SHA-256
  339be43053f77cabe188569e2067e114de26824ccc37e0265495819678a9c673.

- 2026-09-09T13:05:32+00:00: Recorded command exit 0; command argv SHA-256
  7c61011b91e77ce2a5f1477e3b4d6a3e748ff28408c6327e1b19f9551c1da508.

- 2026-09-09T13:06:01+00:00: Repaired all four independent-review blockers in signed successor
  d47f5031394e2390867aa750caf9494a8b81e36f (tree effe89538a5b586df695dc6beb957fba30dc4d82, parent
  5a0570fbce2fa77ab4baf6b34d2632d289a5ab36). Exact two-path scope remains
  tools/capacity/lifecycle.py and tests/capacity/test_lifecycle.py. State and cleanup schemas now
  require exact integers and reject unhashable state values as CapacityError; CLI lease time comes
  only from the process clock and no longer accepts --now; reconciliation requires a private
  no-follow canonical receipt bound to capacity/owner/revision/time plus an actually read teardown
  artifact whose SHA-256 matches. Hostile tests cover bools, state list, expired trusted time,
  unsafe evidence mode, and digest mismatch without ledger mutation. Postcommit: focused unittest
  14/14, source-header unittest 18/18, Ruff format/lint, strict mypy, diff-check, exact scope, clean
  tree and private-identifier grep pass. Both commits have valid matching SSH signatures/DCO;
  Gitleaks scanned both commits/51.33 KB with no leaks. AR remains unpublished and in progress
  pending independent review and later native cell/resource/boot evidence.

- 2026-09-09T13:10:51+00:00: Recorded command exit 0; command argv SHA-256
  4cedf36b300ccd67e8835016be5f4cbedf5e955b39f37d59e852322f35904816.

- 2026-09-09T13:11:12+00:00: Recorded command exit 0; command argv SHA-256
  2fc538a4858bf6199d1c01f0e3adc6f88817fc0c336ae73fdf072ef0eaf1234c.

- 2026-09-09T13:11:29+00:00: Recorded command exit 0; command argv SHA-256
  2077133942407f5db2c9c13687f3ecdff199b7f2c50e77563f12b8527d375459.

- 2026-09-09T13:11:56+00:00: Recorded command exit 0; command argv SHA-256
  d231a09f2fdbbbd51e288c943a8be4c76049205ebe0a14d401d878b373522868.

- 2026-09-09T13:12:22+00:00: Remaining trust defect repaired in signed successor
  28f30eea80efef5a61ea438e77402f8640564cc9 (tree 28885e94a94cebb745dd5c5be94998d936f86813, parent
  d47f5031394e2390867aa750caf9494a8b81e36f). Same-UID canonical receipts and matching teardown
  artifacts are validated only for diagnostics and can no longer transition needs_reconciliation to
  available: reconcile_clean always fails closed until a distinct authenticated cleanup verifier
  exists. The former positive arbitrary-byte fixture is now an explicit forged-but-self-consistent
  receipt/artifact atomic negative and proves the ledger remains at revision 2 needs_reconciliation.
  Exact two-path scope remains clean. Postcommit gates pass: focused unittest 14/14, source-header
  unittest 18/18, Ruff format/lint, strict mypy, full base-range diff-check/scope/privacy, valid SSH
  signature and DCO, and Gitleaks across all three commits (52.74 KB) with no leaks. Candidate
  remains unpublished; AR remains in progress with native provisioning/resource/boot and
  authenticated reconciliation evidence unclaimed.

- 2026-09-09T13:14:25+00:00: Recorded command exit 0; command argv SHA-256
  ebcfda9952c6830fa1c5453f9c7c8aa3998ff46acc7713315ca35431f84a3bcc.

- 2026-09-09T13:14:50+00:00: Recorded command exit 0; command argv SHA-256
  51313ca4da1202d105f528a2cfaaf1d46f9356470bccd4d489f271a9f7ed667d.

- 2026-09-09T13:15:09+00:00: Recorded command exit 0; command argv SHA-256
  14e77fccda7134ddc2101463045d500d1a9f6b31add7f09119809d42a60a826a.

- 2026-09-09T13:15:28+00:00: Recorded command exit 1; command argv SHA-256
  9cb862fd877129e1a5da38c8bda48bca0eaa4d30ba2fb8f201b0e3db17b50625.

- 2026-09-09T13:16:10+00:00: Recorded command exit 1; command argv SHA-256
  eac3d7807a31aafdf67776b3c1d09fac995b56aad2abb235f72083b850933bcc.

- 2026-09-09T13:16:24+00:00: Recorded command exit 0; command argv SHA-256
  9cb862fd877129e1a5da38c8bda48bca0eaa4d30ba2fb8f201b0e3db17b50625.

- 2026-09-09T13:17:05+00:00: Recorded command exit 0; command argv SHA-256
  89c9445bfe2e74d63f80d2faab598dce1344131b740d5fdd3ce7de29660628ee.

- 2026-09-09T13:20:03+00:00: Recorded command exit 1; command argv SHA-256
  c67106852a0572347e8565eef1b0401c25be3c98c53cf55261e555e3fcf6ed4c.

- 2026-09-09T13:20:36+00:00: Published independently approved exact candidate
  28f30eea80efef5a61ea438e77402f8640564cc9 as focused PR #119; remote branch was absent before the
  non-force push. PR head and base were verified as 28f30eea and b6d04a83. Exact-head CI is
  terminal: 11 checks succeeded and one failed. Formal assurance run 34355869235 job 102480266536
  failed in run_temporal_models.sh immediately after downloading the official TLA+ v1.8.0 asset.
  Sanitized reproduction confirms the asset retains expected 4490679 bytes but now hashes
  ae41e3f67f8f81de9788e348cac2c868f0fdf810e14c6b49fd759b3ef578562e instead of pinned
  a1fc0bfe391d99fdd86f579a63ff68c0950010e9dde551f1192b867d5c8f4efd. This is a fail-closed upstream
  provenance mismatch in unchanged formal paths, not an AR-0704 two-path regression. No merge
  attempted. Preserve exact approved scope and explicit unavailable-verifier/native-evidence
  limitations.

- 2026-09-09T15:16:11+00:00: Recovered expired claim formerly owned by contracts_20260906. Expired
  owner lease recovered after coordinator audit; preserve reviewed PR head and require fresh claim
  before further AR-0704 mutation.

- 2026-09-16T06:08:56+00:00: Claimed by asb_ar1232_lifecycle_router.

- 2026-09-16T06:09:31+00:00: Recorded command exit 0; command argv SHA-256
  a50ec52884b39a6263d3f4d81689c8edcda545ce93da7eaadf5d77a94476c492.

- 2026-09-16T06:09:55+00:00: Focused gate via handoffctl: python3 -m unittest
  tests.capacity.test_lifecycle tests.platforms.test_native_x86_capacity ran 25 tests, all OK.
  Expected bounded ERROR lines were emitted by negative fixtures; no test failure. Worktree remains
  clean at signed/DCO head 28f30ee. Next step is read-only exact PR #119/TLA provenance audit before
  any mutation.

- 2026-09-16T06:26:10+00:00: Recorded command exit 0; command argv SHA-256
  5926ed8425472b68624f5b2db4d7791bf802735f0228108e33149883e0f0f34d.

- 2026-09-16T06:26:25+00:00: Recorded command exit 0; command argv SHA-256
  1a49978bc89826a6f0252ab2c0d64311d64ed1b7dd5a23d2328d638dba243654.

- 2026-09-16T06:26:43+00:00: Exact PR #119 audit complete. Head 28f30ee is clean and signed/DCO;
  hosted checks were green except TLC and Alloy recovery models, which failed exit 1 during the
  pinned formal-tool download before model execution. gh run failed log confirms transfer reached
  100% then process exited 1, with no product assertion. Release ownerless blocked; rerun/rebase
  only after formal infrastructure/provenance lane is available.

- 2026-09-16T06:29:17+00:00: Formal infrastructure investigation is now actionable: inspect PR #119
  hosted TLC/Alloy artifact download/provenance failure without weakening gates.

- 2026-09-16T06:29:20+00:00: Claimed by asb_ar0704_formal_infra.

- 2026-09-16T06:29:32+00:00: Recorded command exit 0; command argv SHA-256
  e9db925db84dc3f183024ebb8977cf3c736f4d07b232ad284f18bfff4f967ece.

- 2026-09-16T06:29:50+00:00: Recorded command exit 0; command argv SHA-256
  f3d3db5f6371551ecfcc32755923dcf3f4793c4ba3aab39bcf920e7b656285b7.

- 2026-09-16T06:48:44+00:00: Heartbeat by asb_ar0704_formal_infra.

- 2026-09-16T06:48:54+00:00: Investigation complete: PR #119 exact head 28f30ee fails only formal
  run 34355869235 after the TLA v1.8.0 download; pinned TLA_BYTES/hash validation rejects the
  downloaded 4385 KiB asset against expected 4490679 bytes and SHA a1fc0bfe... All other checks
  passed. This is outside AR-0704 native-capacity scope. No product mutation or gate weakening.

- 2026-09-16T06:48:59+00:00: Released blocked and ownerless. Formal TLA artifact/provenance repair
  belongs to AR-0877/AR-0907; do not alter native-capacity code or weaken formal verification.

- 2026-09-18T20:55:59+00:00: Re-audit PR #119 without source mutation. PR #119 remains open with
  exact head 28f30ee; 11 checks passed and only Formal assurance failed after the official TLA+
  v1.8.0 asset download. The failure is an immutable artifact byte-count/hash mismatch outside
  AR-0704 native-capacity scope; matching formal/provenance successors AR-0877/AR-0907 (and AR-0906)
  have the repair boundary. Reopen only for a new native-capacity issue after formal provenance is
  repaired.

- 2026-09-18T20:56:19+00:00: Claimed by asb-ar0704-pr119-audit-20260918.

- 2026-09-18T20:56:34+00:00: PR #119 live audit: exact head 28f30eea80efef5a61ea438e77402f8640564cc9
  is SSH-signed with matching DCO; its two AR-0704 paths are exactly the reviewed lifecycle
  controller. GitHub reports 11 required checks green and only Formal assurance run 34355869235 job
  102480266536 failed. The failure occurs immediately after downloading the official TLA+ v1.8.0
  asset: transfer reports 4385 KiB / 4490679 bytes, but pinned validation observes SHA
  ae41e3f67f8f81de9788e348cac2c868f0fdf810e14c6b49fd759b3ef578562e instead of
  a1fc0bfe391d99fdd86f579a63ff68c0950010e9dde551f1192b867d5c8f4efd. No product assertion ran. PR
  #119 remains open/mergeable but unstable. Formal repair is outside AR-0704 and belongs to
  AR-0877/AR-0907/AR-0906; no native-capacity or formal gate was weakened.

- 2026-09-18T20:57:27+00:00: Released blocked and ownerless after exact PR #119 audit. Head 28f30ee
  is signed/DCO and all non-formal checks pass; formal assurance fails on the downloaded TLA+ v1.8.0
  artifact byte/hash mismatch (observed 4490679 bytes and ae41e3f6..., pinned a1fc0bfe...). This is
  outside AR-0704 native-capacity scope and must be repaired by AR-0877/AR-0907/AR-0906 before
  requalification. No product mutation, merge, or gate weakening performed.

- 2026-09-18T21:30:08+00:00: Fresh coordinator-authorized exact-head and formal provenance audit
  after formal successor merges; preserve native-capacity scope and fail closed.

- 2026-09-18T21:30:13+00:00: Claimed by asb-ar0704-pr119-audit-20260918.

- 2026-09-18T21:30:24+00:00: Recorded command exit 0; command argv SHA-256
  8835ca6afa124b5f0cfd058e18f654c75cfea93cbe35cb3c57d7948687d35db1.

- 2026-09-18T21:30:37+00:00: Recorded command exit 0; command argv SHA-256
  596be899947322679d57481669d39ebe710dad0cfc096af42bece308cb4ec8b3.

- 2026-09-18T21:30:48+00:00: Recorded command exit 0; command argv SHA-256
  6a125d4e0c3dd06065e7476b058ebef70d552dfca57580df05a7191033b128e1.

- 2026-09-18T21:31:00+00:00: Recorded command exit 0; command argv SHA-256
  ea158da9707c64c55a9bf7f723f87ddf5946a5a5febeba86e725dbaf146ae183.

- 2026-09-18T21:31:13+00:00: Recorded command exit 0; command argv SHA-256
  f3ee8e02a9bfd0a29686c93f72445327b2d56616a21cd4eb1dc471eb2f380b74.

- 2026-09-18T21:31:29+00:00: Recorded command exit 0; command argv SHA-256
  968e81ffd1de728167aa4801f76906236f286e2d6a1eb1ad74d1f42739e77faa.

- 2026-09-18T21:31:40+00:00: Recorded command exit 0; command argv SHA-256
  8d506528915cab6a6e94476d4b18ae03ec30ee83ed7beb36a9f1554cf3938318.

- 2026-09-18T21:31:52+00:00: Recorded command exit 0; command argv SHA-256
  fc194dc04c172e8dca899372021fcce70d1d613b5ccf41b567f2475bae637e57.

- 2026-09-18T21:32:04+00:00: Recorded command exit 0; command argv SHA-256
  b4bb90e931333e9cc29c1f0ce9afeb066718349ea789273f19d321b21dd2b5ed.

- 2026-09-18T21:32:18+00:00: Recorded command exit 0; command argv SHA-256
  e4ba5e4d82d11a5764bf72ccc9e5ceb1d456cecbead441a4f640878f39eab8ce.

- 2026-09-18T21:32:30+00:00: Recorded command exit 0; command argv SHA-256
  1f7721a097b2f9f0c2afe1b1aa4493e1ec3e24ed947fb815f11e3419f920d169.

- 2026-09-18T21:32:44+00:00: Recorded command exit 0; command argv SHA-256
  1fe90cace3641e75bb8b43baa6d6dfa99e27ec165a3ce86718c1e50bbc8c9045.

- 2026-09-18T21:32:58+00:00: Recorded command exit 0; command argv SHA-256
  6aeff8c998ae024367eca8c16238e2288e6b295737e8a938bae53d491e77f6ef.

- 2026-09-18T21:33:11+00:00: Recorded command exit 0; command argv SHA-256
  85d7142d31410f36754b5f94fe413fd8b7cd73320176211e67b59aada1ec4cf6.

- 2026-09-18T21:33:22+00:00: Recorded command exit 0; command argv SHA-256
  7673bb4a557f14fbe41247ace70e769bff5ab5b0541e38f2ba8617fcd239a26c.

- 2026-09-18T21:33:33+00:00: Recorded command exit 0; command argv SHA-256
  42a9e73e3f6ecad06c7dbc0817c84fea104e18d6d417f88b34ac58bfbe55d64b.

- 2026-09-18T21:33:45+00:00: Recorded command exit 0; command argv SHA-256
  5b4350712b6966ce02097b2394972070b49e1500c3e9a8e7ac7ff4c6cdea6021.

- 2026-09-18T21:33:57+00:00: Recorded command exit 0; command argv SHA-256
  bed7f1529be81a0156ad4f217f33c333005a019de2fe265aeaf0d6df5aa2d9fe.

- 2026-09-18T21:34:14+00:00: Recorded command exit 0; command argv SHA-256
  1817dc214eb97756a1765c85b4bb207ab62686f2247d29d01256348f8d44646d.

- 2026-09-18T21:34:27+00:00: Recorded command exit 0; command argv SHA-256
  5452a8ea4b4c3748234248f34058848542d7bbf8f2f4d259c7604e7bfca4fae4.

- 2026-09-18T21:34:41+00:00: Recorded command exit 0; command argv SHA-256
  b0e40f49285d776dd0391d210381cc3dac33cf4e7e1a8ff26079c7c797965102.

- 2026-09-18T21:35:07+00:00: Recorded command exit 0; command argv SHA-256
  3bee2b6f1a42420a61a68de904d6a618e55ee26f215b55d64fb56bb448b7c223.

- 2026-09-18T21:35:19+00:00: Recorded command exit 0; command argv SHA-256
  5452a8ea4b4c3748234248f34058848542d7bbf8f2f4d259c7604e7bfca4fae4.

- 2026-09-18T21:35:30+00:00: Recorded command exit 0; command argv SHA-256
  f3ee8e02a9bfd0a29686c93f72445327b2d56616a21cd4eb1dc471eb2f380b74.

- 2026-09-18T21:35:57+00:00: Fresh audit 2026-09-18: PR #119 remains exact head 28f30eea,
  signed/DCO, 11 required checks green, Formal assurance failed only because its old branch pins
  official TLA artifact 4490679 bytes/SHA a1fc0bfe. Current origin/main includes merged formal
  provenance repairs and pins deterministic source-build artifact 4512486 bytes/SHA 8c200a88 via
  AR-0877/0906/0907 merges. The AR-0704 branch still has the stale pin, so no rerun or merge is
  authorized until a signed rebase/update and complete exact-head CI.

- 2026-09-18T21:36:02+00:00: Audit complete; released ownerless for dependency-safe rebase and full
  requalification on repaired formal provenance. No source mutation, force push, merge, or gate
  weakening performed.

- 2026-09-18T21:36:42+00:00: Claimed by asb-ar0704-formal-rebase-20260918.

- 2026-09-18T21:36:57+00:00: Recorded command exit 0; command argv SHA-256
  4a73c3c01d06ab32f7ab9670ffe18da4e5ba09971fc15aeff38f745b2e49465b.

- 2026-09-18T21:37:14+00:00: Recorded command exit 0; command argv SHA-256
  3917ca79328acbf790afc87693b4b7511f618c74a037d9b2d282e37419ea0967.

- 2026-09-18T21:37:34+00:00: Recorded command exit 0; command argv SHA-256
  cbdfa4f7ee89f7202c51cc786378a93251ccf82236c9d0d27d1c40de704b0d73.

- 2026-09-18T21:37:52+00:00: Recorded command exit 0; command argv SHA-256
  d1e5f5cf70a3ca58bd83d0a7f5ed3de9646a207227f97c510201d6aba1fca8c9.

- 2026-09-18T21:38:15+00:00: Recorded command exit 0; command argv SHA-256
  42fde9e93abb6a51c26230fdb16b83fb237f8a1062a83c70346d5655839fb37c.

- 2026-09-18T21:38:31+00:00: Recorded command exit 1; command argv SHA-256
  a50ec52884b39a6263d3f4d81689c8edcda545ce93da7eaadf5d77a94476c492.

- 2026-09-18T21:38:56+00:00: Recorded command exit 5; command argv SHA-256
  7ee40efb926f92bc81c02b3d703959514191155a270c973207725c48f0ea57c3.

- 2026-09-18T21:39:22+00:00: Recorded command exit 0; command argv SHA-256
  8eb30259a8030e26a5e2643418643ccfee1857c41559ea6ec4dfbb87d094a851.

- 2026-09-18T21:39:36+00:00: Recorded command exit 1; command argv SHA-256
  2401fa73b1a0e8924bd0f9252a8b332cecc5c1795d1248bcd34a31a1bf047d24.

- 2026-09-18T21:39:56+00:00: Recorded command exit 0; command argv SHA-256
  45f6e879aad150f860c55ff81548646df3cddc4a4a7023449eb0bd76758f7426.

- 2026-09-18T21:40:40+00:00: Recorded command exit 1; command argv SHA-256
  380d06594ad8eed4c5e541c1bdf7bea27351fd74791810e35ebb4ca91e459b35.

- 2026-09-18T21:40:51+00:00: Recorded command exit 1; command argv SHA-256
  0497f999cc1d2998bac6524440d62aedd4733a53ee70ab9c1b5723c8a8ff58c1.

- 2026-09-18T21:41:23+00:00: Recorded command exit 0; command argv SHA-256
  9114a49c021532df5e18f70cadee0defb71615719c422b1ee76f6e308e37baac.
