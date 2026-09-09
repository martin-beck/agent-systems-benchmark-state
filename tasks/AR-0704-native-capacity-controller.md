---
{
  "branch": "feature/native-capacity-controller",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-09T15:11:42+00:00",
  "depends_on": [
    "AR-0701",
    "AR-0103"
  ],
  "id": "AR-0704",
  "next_action": "Independent immutable review of 28f30ee; keep reconciliation fenced and do not publish.",
  "observed_branch": "feature/native-capacity-controller",
  "observed_dirty": 0,
  "observed_head": "28f30eea80efef5a61ea438e77402f8640564cc9",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0704.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Control genuine native platform capacity lifecycle.",
  "task_revision": 67,
  "title": "Control native capacity lifecycle",
  "updated_at": "2026-09-09T13:17:05+00:00",
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
