---
{
  "branch": "feature/replay-openhands",
  "checkpoint_commit": "3ccee91118b3a43eda123b0107d04ea4c2e3d80a",
  "claim_expires": "",
  "depends_on": [
    "AR-0309",
    "AR-0503",
    "AR-0504",
    "AR-0401"
  ],
  "id": "AR-0514",
  "next_action": "Independent review and exact-head CI of 3ccee911; exact approved OpenHands environment digest remains unrecoverable, so native replay stays blocked pending AR-0521 pin-reproduction repair.",
  "observed_branch": "feature/replay-openhands",
  "observed_dirty": 0,
  "observed_head": "3ccee91118b3a43eda123b0107d04ea4c2e3d80a",
  "owner": "",
  "plan": "../plans/AR-0514.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Qualify replay conformance for OpenHands.",
  "task_revision": 59,
  "title": "Qualify OpenHands replay",
  "updated_at": "2026-09-29T10:11:53+00:00",
  "worktree_key": "agent-systems-benchmark-replay-openhands"
}
---
## AR-0514

Qualify OpenHands record/replay, network denial, parity, retries, tool calls, cancellation, and malformed-record failures.

- 2026-09-08T07:00:07+00:00: AR-0309 is durably done at 52f884b; AR-0503, AR-0504 and AR-0401
  verified done. Promoted highest-priority ready OpenHands replay qualification.

- 2026-09-08T07:00:09+00:00: Claimed by contracts_20260906.

- 2026-09-08T07:00:57+00:00: Recorded command exit 0; command argv SHA-256
  799e7bb404f086a50e4307294f7aabc23b78f3356f22193c257483fb30b435d0.

- 2026-09-08T07:02:44+00:00: Recorded command exit 0; command argv SHA-256
  91e71c56047ea4f6ab7316738b32cc82647964bce6e70d87c138ed608266cf55.

- 2026-09-08T07:03:13+00:00: Recorded command exit 0; command argv SHA-256
  d3bd891753f2e4054144c1e6ac5879ad5964605079c2e2a0aca755fd9ab0021a.

- 2026-09-08T07:05:33+00:00: Recorded command exit 0; command argv SHA-256
  8820aa35d73941216018410c314e8a92b4650310d62af6cc531943ddf29a7de5.

- 2026-09-08T07:06:03+00:00: Recorded command exit 0; command argv SHA-256
  a29404d336c450b8c6648548e77f07a2b0e318ba15eeb27b2967c4c5772297ce.

- 2026-09-08T07:06:32+00:00: Recorded command exit 0; command argv SHA-256
  01335908bddfa15a31e9c23c0ff50e6a7dbaf2d8f99336856af39ee6113a488e.

- 2026-09-08T07:07:07+00:00: Recorded command exit 0; command argv SHA-256
  d354198187ca6ef877bbf7e8d8b0a0c0f3f8be72c874004aa90094543028d882.

- 2026-09-08T07:07:23+00:00: Recorded command exit 1; command argv SHA-256
  e18b4026adf2c13795d45446d2d1c3d72a1a6b5a51bcefc0caddbf3ebd5053d6.

- 2026-09-08T07:07:48+00:00: Recorded command exit 0; command argv SHA-256
  86783e6a56f4f0ccd7019b93d08458bbd063ce056e2099ac51c50bcaa16541f9.

- 2026-09-08T07:08:21+00:00: Recorded command exit 101; command argv SHA-256
  4afa1d889face0be6c98a7787c00e2cbe66c757d3cc843cf3996639f861873aa.

- 2026-09-08T07:10:41+00:00: Recorded command exit 0; command argv SHA-256
  79c1444aaf2b12b769bd137cb67df30b1d721e3842436a9607ff4655d1a28a23.

- 2026-09-08T07:11:10+00:00: Recorded command exit 101; command argv SHA-256
  4dcb93acf0d1de535426c68dd8319424038a56c3f019ea2694d20ad09db277e5.

- 2026-09-08T07:12:42+00:00: Recorded command exit 101; command argv SHA-256
  8e8bd89c14698ee330fe8db4289db4b9739bbb5204d0ab8df284f92ac7dee18b.

- 2026-09-08T07:14:01+00:00: Recorded command exit 0; command argv SHA-256
  29d14278555f304cb6ec35ffd94deb08428954f19724242d5ac599121e3167fe.

- 2026-09-08T07:15:07+00:00: Recorded command exit 2; command argv SHA-256
  18792ce7640ad9053622fef9bf8df93d8d69c53377ee884126fec23a72793bec.

- 2026-09-08T07:15:48+00:00: Recorded command exit 0; command argv SHA-256
  cf519d48b9c2567e149c618f43c29b518ee25688e4a0131ffffc9a9820af6cc7.

- 2026-09-08T07:20:11+00:00: Recorded command exit 0; command argv SHA-256
  b89de90b8e6942880cd6abbad8a339cdae995de479e81e0aa5063a46d025b1a4.

- 2026-09-08T07:43:49+00:00: Recorded command exit 0; command argv SHA-256
  5f3003e3a17dae5fea7b8dc095a4ca55a76a0896eaabea7140c1b816910f1ab6.

- 2026-09-08T07:44:47+00:00: Fail-closed provenance blocker: exact retained lock SHA dfc3b9e and
  wheel SHA 3b771e were reconstructed with three distinct bounded recipes. stdlib venv+pip digest
  10857178; stdlib venv+uv digest 74e71e58; stdlib venv --without-pip+uv digest 006ea070 (uv venv
  earlier cb50d5ad; direct target bca74255). All dependency checks pass and proprietary
  openhands_aci is absent, but none equals production multi-file digest 63727569. No digest override
  or native run performed; all roots retained for comparison.

- 2026-09-08T08:50:17+00:00: Heartbeat by contracts_20260906.

- 2026-09-08T08:52:11+00:00: Owner stopped after durable heartbeat: exact approved OpenHands
  environment digest 6372756912734f6275362a8b66c3758fd2b2adeab776eb2a0be7935f34abb9b2 could not be
  reproduced by five bounded dependency-preserving recipes (all roots retained). No override/native
  replay. Worktree remains feature/replay-openhands at 64f6eb4e5bc70c6d70997a463e7e4884555bc4da with
  only untracked crates/asb-agents/tests/replay_openhands.rs; do not clean. Next action:
  create/review a pin-reproduction repair with immutable environment provenance before reclaiming.

- 2026-09-29T09:54:24+00:00: Coordinator takeover: prior worker stopped after immutable OpenHands
  environment digest could not be reproduced. Start bounded repair worker on the same AR to recover
  or formally repair pin provenance; do not override digest or perform native replay.

- 2026-09-29T09:54:27+00:00: Claimed by ar0514-repair-luna56.

- 2026-09-29T09:56:10+00:00: Heartbeat by ar0514-repair-luna56.

- 2026-09-29T09:58:48+00:00: Heartbeat by ar0514-repair-luna56.

- 2026-09-29T09:58:50+00:00: Recorded command exit 0; command argv SHA-256
  2a84530d80c5ef6128bac6e359dc311c5c13c57d7d1e507e94c848b149fb3e06.

- 2026-09-29T09:59:08+00:00: Recorded command exit 1; command argv SHA-256
  21497edebd13d0136c7f15db13db60c6cef4386dc3f1b6451312e0f65d3ce3b7.

- 2026-09-29T09:59:52+00:00: Recorded command exit 0; command argv SHA-256
  fe96654aaaba4069d8810f2458a91e491f069688a22ecac9ecd59656151cb678.

- 2026-09-29T10:00:53+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T10:01:11+00:00: Recorded command exit 101; command argv SHA-256
  fe96654aaaba4069d8810f2458a91e491f069688a22ecac9ecd59656151cb678.

- 2026-09-29T10:01:30+00:00: Recorded command exit 0; command argv SHA-256
  3555758ac8225f55c064ea50edcabac75226d1747e356f3522b4158ae28bb7ce.

- 2026-09-29T10:01:57+00:00: Recorded command exit 0; command argv SHA-256
  e35d033d7a7950d97c3dc450ead4cfb662d480e22cbd0600b92b4d72806ac02c.

- 2026-09-29T10:02:15+00:00: Recorded command exit 0; command argv SHA-256
  19fa7ac60602abc163c7bc32e7a049e6b79e0880899030c008f3b243da365bb6.

- 2026-09-29T10:02:37+00:00: Recorded command exit 1; command argv SHA-256
  58efd0affcb2c9f32aaf8ca3f4bc33231fb90a3629aaa22f553e12fb696e2042.

- 2026-09-29T10:02:54+00:00: Bounded repair committed as 3ccee91118b3a43eda123b0107d04ea4c2e3d80a
  (SSH-signed, DCO): retained the prior ignored OpenHands replay fixture and added provider-free
  local mock strict-replay qualification. Focused cargo test passes: 2 deterministic tests passed, 1
  native OpenHands test remains intentionally ignored because exact CPython/wheel/site-packages
  provenance is absent. Earlier five digest recipes remain non-matching; no override, credentials,
  native replay, or external provider effect. Exact digest is still blocked; AR-0521 must publish an
  immutable environment bundle/verifier before native replay.

- 2026-09-29T10:03:02+00:00: Recorded command exit 0; command argv SHA-256
  3c96acaf60ffa8bf99feba8f091ce5c047786b4250d95c723a7f72079f8f7360.

- 2026-09-29T10:03:20+00:00: Recorded command exit 0; command argv SHA-256
  fe96654aaaba4069d8810f2458a91e491f069688a22ecac9ecd59656151cb678.

- 2026-09-29T10:03:50+00:00: Recorded command exit 1; command argv SHA-256
  aa635cf14f01d7c3c510ec2850c005cde159391e2909b2c37f12525a5716ea55.

- 2026-09-29T10:04:07+00:00: Truthful blocked boundary after bounded repair 3ccee911: immutable
  AR-0309 metadata preserves SDK 1.17.0 upstream commit/tree, wheel/source hashes, freeze and
  approved digest, but no retained environment bundle, lock archive, exact Python executable or
  matching site-packages tree exists. Five dependency-preserving recipes produced non-matching
  digests. Provider-free local mock strict-replay and malformed/tool-inconsistent negative tests
  pass; native journey remains ignored. No digest override, credentials or native replay. Unblock
  only after AR-0521 publishes an independently verified content-addressed environment bundle,
  offline verifier and altered-input rejection, then requalify AR-0514.

- 2026-09-29T10:04:40+00:00: Run independent review and exact-head CI for bounded repair commit
  3ccee911 before retaining the truthful AR-0521 provenance block.

- 2026-09-29T10:04:43+00:00: Claimed by ar0514-review-luna56.

- 2026-09-29T10:06:21+00:00: Recorded command exit 0; command argv SHA-256
  eb0bda22244ba2ee1fb6df77e8248fc5c8f5e866e08a5e496ebbacfe5d1ce828.

- 2026-09-29T10:06:43+00:00: Recorded command exit 0; command argv SHA-256
  43f4b2332b948b205f01d549c1328286649e565c9f8b9fb6819b3427103fef46.

- 2026-09-29T10:07:02+00:00: Recorded command exit 0; command argv SHA-256
  22ebc4ca7068cf43345deae7d5e22f55dd0e338acc6da57c4b0d026e7f4ae08d.

- 2026-09-29T10:07:31+00:00: Recorded command exit 0; command argv SHA-256
  f3c801178df90aca24d688ffedb4ccba7b5a00056b45518e49ccf5736ba34124.

- 2026-09-29T10:07:49+00:00: Recorded command exit 0; command argv SHA-256
  360c2489affc56e82bc996d4debd2e3d0e694eae0d4ac1ac81fa58ec3abf17ac.

- 2026-09-29T10:08:06+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-29T10:08:32+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-09-29T10:09:20+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-09-29T10:09:48+00:00: Recorded command exit 0; command argv SHA-256
  649e9e1ebfaf13c15c95c6360ca922c0b7c73a9a7fd2cf6943002779fca093b1.

- 2026-09-29T10:10:21+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-09-29T10:11:07+00:00: Recorded command exit 0; command argv SHA-256
  eb0bda22244ba2ee1fb6df77e8248fc5c8f5e866e08a5e496ebbacfe5d1ce828.

- 2026-09-29T10:11:53+00:00: Independent review of exact clean head 3ccee911 passed SSH signature
  and DCO verification; focused replay_openhands passed 2 provider-free local strict-replay and
  malformed/tool-inconsistent negative tests, and cargo fmt, clippy -D warnings, locked workspace
  tests, docs, and release build all passed. No remote branch or PR exists. Native OpenHands journey
  remains explicitly ignored because AR-0309 metadata has no retained immutable bundle, lock
  archive, exact interpreter, or matching site-packages tree; five prior recipes remain
  non-matching. No digest override, live credentials, or provider effect. Keep AR-0521 provenance
  blocker; unblock only after its signed content-addressed bundle, offline verifier, reproducible
  approved digest, and altered-input rejection are independently verified, then requalify AR-0514.
