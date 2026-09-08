---
{
  "branch": "feature/replay-openhands",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0309",
    "AR-0503",
    "AR-0504",
    "AR-0401"
  ],
  "id": "AR-0514",
  "next_action": "Recover exact approved OpenHands environment digest 63727569 from immutable provenance; otherwise schedule pin-reproduction repair before native replay.",
  "observed_branch": "feature/replay-openhands",
  "observed_dirty": 1,
  "observed_head": "64f6eb4e5bc70c6d70997a463e7e4884555bc4da",
  "owner": "",
  "plan": "../plans/AR-0514.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Qualify replay conformance for OpenHands.",
  "task_revision": 26,
  "title": "Qualify OpenHands replay",
  "updated_at": "2026-09-08T08:52:11+00:00",
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
