---
{
  "branch": "feature/agent-openhands",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T06:49:55+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0102",
    "AR-0103"
  ],
  "id": "AR-0309",
  "next_action": "Extend checkpoint 725c40b with malformed-evidence, symlink, cancellation, action-ceiling and cleanup negatives, then request the serialized lib.rs registration fence.",
  "observed_branch": "feature/agent-openhands",
  "observed_dirty": 2,
  "observed_head": "e9af38b5be5140c8eaf4d1b55e1eebab07d0f311",
  "owner": "contracts_20260906",
  "plan": "../plans/AR-0309.md",
  "priority": "P2",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Run a maintained MIT OpenHands SDK or canonical headless client.",
  "task_revision": 63,
  "title": "Implement maintained OpenHands SDK client adapter",
  "updated_at": "2026-09-08T04:32:40+00:00",
  "worktree_key": "agent-systems-benchmark-agent-openhands"
}
---
## AR-0309

Run a maintained MIT OpenHands SDK or canonical headless client.

Implementation has not started. Read the linked plan before claiming.


- 2026-09-08T03:49:45+00:00: Verified AR-0101, AR-0102 and AR-0103 are durably done. Selected
  highest-priority safe disjoint leaf after P1 authorization/dependency/path blockers; OpenHands
  module and fixtures do not overlap active frontend protocol, verifier integrity, or kernel
  diagnostics paths.

- 2026-09-08T03:49:55+00:00: Claimed by contracts_20260906.

- 2026-09-08T03:50:41+00:00: Recorded command exit 0; command argv SHA-256
  07036c4ad1b996ca80da9bef22d326a3298e0fa2af6aa940f96f17b07676a4b3.

- 2026-09-08T03:55:22+00:00: Official-source boundary resolved: use active MIT
  OpenHands/software-agent-sdk v1.45.0, signed tag commit 49ea74587c376b90700f6eff128c3d9b57585d27
  and tree 639a6850375c0d8e04c9f045a5a74c15fea0406c. Exclude OpenHands/OpenHands enterprise paths.
  Do not use OpenHands-CLI 1.16.0 for this adapter: although MIT and maintained, its latest release
  pins older SDK/tools 1.21.0 and documented headless operation is always-approve, so it cannot
  expose the required bounded confirmation policy as cleanly as the SDK.

- 2026-09-08T03:57:02+00:00: Recorded command exit 1; command argv SHA-256
  10c15ae9e6c277a981542655bf485392a3392b9b9505a04cd20806bfee47a5f6.

- 2026-09-08T03:57:30+00:00: Recorded command exit 1; command argv SHA-256
  66da4fbe5e6464ee9d68e3834c74fb42921242e766b1a2034ec420c1ef435f21.

- 2026-09-08T03:57:44+00:00: Recorded command exit 1; command argv SHA-256
  a70f1bec1335a8a298c55d63e5fc86519af84c76b83ea9cd68b18201618a534f.

- 2026-09-08T03:57:56+00:00: Recorded command exit 0; command argv SHA-256
  e046063cdec35e5ac2dbf813eb115fc953730f3e03311593c44b06f6516ac43b.

- 2026-09-08T03:58:16+00:00: Recorded command exit 0; command argv SHA-256
  9fe3ace62ad35d411bb905dd2705e9f7d79b3ceb478a126d89f6a69420d7abe6.

- 2026-09-08T04:00:15+00:00: Recorded command exit 2; command argv SHA-256
  cb76f2eadc7d84a08940326c617e2bf9e8f94bdca84bf86b5de2ac1eaaae9c80.

- 2026-09-08T04:04:01+00:00: Recorded command exit 0; command argv SHA-256
  62f7e88cca66e94b3960fdd21aea322fc297518ec6d1f8e85a57859d59815363.

- 2026-09-08T04:04:30+00:00: Recorded command exit 1; command argv SHA-256
  6d819964b1301e94d9f87cb995f8e740fe9292a49829e809bcd0459299e90be5.

- 2026-09-08T04:04:42+00:00: Recorded command exit 0; command argv SHA-256
  6fc8587a9a6a662fe07b64324f08c93893fd0642ce7d3a85c73afd2fc988b76a.

- 2026-09-08T04:05:10+00:00: Recorded command exit 0; command argv SHA-256
  b843a942da9e23c42becd7c8321107d1e2604df3eb69e56d1497f6f28962d4a4.

- 2026-09-08T04:06:18+00:00: Native credential-free SDK probe succeeded with OpenHands SDK 1.45.0 on
  CPython 3.12: isolated HOME/XDG roots, no persistence_dir (InMemoryFileStore), AlwaysConfirm
  pending-action validation, a custom bounded write tool, finish event, positive aggregate usage (20
  input/8 output), and exact workspace edit. Closed proxies exposed one denied LiteLLM remote
  cost-map attempt, so production must force the local cost map and reject diagnostics. The first
  all-wheel install failed because func-timeout 4.3.5 is sdist-only; sdk-only resolves 136 packages,
  while adding openhands-tools/workspace expands to 194 packages. Use SDK-only plus ASB-owned
  bounded tool to minimize attack surface.

- 2026-09-08T04:13:03+00:00: Recorded command exit 0; command argv SHA-256
  f1ed95d4565d704f631d934aaba61d6ff0d10990eb20b1c29fe6b01067540429.

- 2026-09-08T04:13:41+00:00: Recorded command exit 0; command argv SHA-256
  f03f14a4247d608d63dd21bc9152c3cfbcb749c39750ac882aff3713eac8bfb5.

- 2026-09-08T04:14:07+00:00: Recorded command exit 101; command argv SHA-256
  73ace59d4f0fe2f69761406da10d9d0939a4b3f693e34b49bb753040bb97450d.

- 2026-09-08T04:14:16+00:00: Recorded command exit 0; command argv SHA-256
  1eaa9f61492f2fa1edf39d0edf9b9a06d9fed16270d338827188a7b0d21f64ba.

- 2026-09-08T04:14:44+00:00: Recorded command exit 101; command argv SHA-256
  14a63e3bea35a89d4ad3486f63c95f0799d2369b8ea961c6a9fe0d578f3dd77f.

- 2026-09-08T04:14:57+00:00: Recorded command exit 0; command argv SHA-256
  763962ff3b0e6a2f13ff08bc4467a1ec365ad6efaff40757cc7a074492f3b1ce.

- 2026-09-08T04:15:12+00:00: Recorded command exit 0; command argv SHA-256
  14a63e3bea35a89d4ad3486f63c95f0799d2369b8ea961c6a9fe0d578f3dd77f.

- 2026-09-08T04:15:40+00:00: Recorded command exit 0; command argv SHA-256
  fe167aadf3ab5243ef1c89cc19a5d83748303e4ac63fc017fcad23703e07b109.

- 2026-09-08T04:16:01+00:00: Recorded command exit 0; command argv SHA-256
  531b9f90f5f44de6e479e1a3ae7762a516f07d37bfa0224448d15838d76abfde.

- 2026-09-08T04:16:19+00:00: Recorded command exit 22; command argv SHA-256
  4361bfb8a54af48cb9c5c3320b0c554ac3350719262a8712779b286f1a0f9bdc.

- 2026-09-08T04:16:41+00:00: Recorded command exit 0; command argv SHA-256
  a718cc544b283cf7e07efd1fdfce7bdaabece280dbf5868d441f8986e4ed3167.

- 2026-09-08T04:17:35+00:00: Recorded command exit 0; command argv SHA-256
  3ce2ab4c31361a8955878a1aa819adb8c2414f77e819c19caed3b5a473acfa15.

- 2026-09-08T04:18:57+00:00: Recorded command exit 0; command argv SHA-256
  ba28b285a03f66cccfa4eec432ead2320829d85d5b615e7272000ba91c045618.

- 2026-09-08T04:19:15+00:00: Recorded command exit 0; command argv SHA-256
  1eaa9f61492f2fa1edf39d0edf9b9a06d9fed16270d338827188a7b0d21f64ba.

- 2026-09-08T04:19:29+00:00: Recorded command exit 0; command argv SHA-256
  14a63e3bea35a89d4ad3486f63c95f0799d2369b8ea961c6a9fe0d578f3dd77f.

- 2026-09-08T04:21:57+00:00: Isolated module and real fixture now exist in the declared worktree
  only. Focused compile/parser/config tests pass (3 passed, native ignored). Real credential-free
  SDK 1.45.0 test passed in 100.41s after content-verifying and privately copying 16,168 environment
  entries / 271,861,732 bytes: exact public sentinel auth, loopback-only request, AlwaysConfirm
  allowlist, one bounded write, finish, positive usage, empty private state, and cleanup.
  OpenHands/LiteLLM stdout and stderr were empty with local cost-map forcing. The wrapper
  evidence-record phase was interrupted while waiting on the shared state lock after the test had
  completed; no product or fixture residue remained.

- 2026-09-08T04:22:18+00:00: Recorded command exit 0; command argv SHA-256
  f973b1b00d8ef44cc057c439be98a059a4c095ca2591bf4a480693241e9805b9.

- 2026-09-08T04:23:06+00:00: Recorded command exit 1; command argv SHA-256
  a6635dd33f93e324c2835eec64ce508566d51eb4b340d8b9b26d8ed629b463e1.

- 2026-09-08T04:23:26+00:00: Recorded command exit 0; command argv SHA-256
  efcead93d4f345fcd9a05f6573f652228dcb288f10c8c4d9e55e0eba2b30a64e.

- 2026-09-08T04:23:53+00:00: Recorded command exit 0; command argv SHA-256
  f6d43615efafbbffd8a86df38f85d7c24acf169ba32d5fd7efcc735375a647b7.

- 2026-09-08T04:24:23+00:00: Recorded command exit 0; command argv SHA-256
  83a8b957bd3f6fb383d2333a77ffa903033c543696fcdf58eac689660dedf410.

- 2026-09-08T04:24:50+00:00: Recorded command exit 101; command argv SHA-256
  90aa1e8fe5e2eac3c795a2f8bbea5f42b5bfc1272fbf786ce93746e8d3bc2cf6.

- 2026-09-08T04:24:56+00:00: Recorded command exit 0; command argv SHA-256
  4924ef45fbaf0378af3ea6923746c20494cc87a01d8fc3a5668cec4698f045f4.

- 2026-09-08T04:25:14+00:00: Recorded command exit 0; command argv SHA-256
  5b4943d1ea56c24ad972cc0a28351ccfe4860920c3bcaee11c6846b4669e6209.

- 2026-09-08T04:25:40+00:00: Recorded command exit 0; command argv SHA-256
  790a009e741575e7c8951b389f84d9f707c77acfa8790d6f26e79a59c1294365.

- 2026-09-08T04:26:12+00:00: Signed+DCO isolated checkpoint 725c40bd41b18947d25a4a986dab4a3ba46f0cd6
  (tree 34eb8e470d879c701dc88ccab6446855b96f419e) adds only openhands.rs, openhands_boundary.rs and
  the 136-package exact freeze fixture. Focused rustfmt, 3 unit/contract tests and Clippy -D
  warnings pass; the real SDK fixture passed separately. Shared crates/asb-agents/src/lib.rs is
  intentionally untouched pending coordinator fence.

- 2026-09-08T04:27:20+00:00: Recorded command exit 1; command argv SHA-256
  96d8523cda3fe97b86a5b045170925c8f207b9f288878c9baf92757324b14493.

- 2026-09-08T04:28:01+00:00: Recorded command exit 0; command argv SHA-256
  edcfbed5462a80e00772e667d93baf42a4c5ac0339ed93379613cefdc65fa760.

- 2026-09-08T04:28:53+00:00: Recorded command exit 0; command argv SHA-256
  a613d10dfd08f1f641d75ff33b450ea149f2548068c5f2c454c52f4f8830a271.

- 2026-09-08T04:29:15+00:00: Recorded command exit 0; command argv SHA-256
  7801bda850e206ad701a1ab067be8d4c0930ded2684c102f016dd88599ec35a7.

- 2026-09-08T04:29:42+00:00: Recorded command exit 0; command argv SHA-256
  87d3733c7dbcba6482d99c63077993d80681429487d1fb28178b59989656077a.

- 2026-09-08T04:30:28+00:00: Recorded command exit 0; command argv SHA-256
  44b91f25e32038d1c57ad775c17b3bebdc7a2e92197d9c25a3dbc932a7687de2.

- 2026-09-08T04:31:04+00:00: Recorded command exit 0; command argv SHA-256
  0063246ff96023dbb8ebc44ebc7f5fe89f7745cd4686820ceec4ab79fbcc32a9.

- 2026-09-08T04:31:20+00:00: Recorded command exit 0; command argv SHA-256
  16a45b65981bfa4f98de7c169e8b1eaf1950e2edfa0cfaaa3e1837b64e697749.

- 2026-09-08T04:31:36+00:00: Recorded command exit 0; command argv SHA-256
  9a845769bcbe6eaf1d2d324f1ee96be0ac34028f726759f239844b21045535be.

- 2026-09-08T04:32:14+00:00: Recorded command exit 1; command argv SHA-256
  b71d40d81de2e7c7e14a7b4050927ef8acebf4fcb9cfddd4832f40a8f343f705.
