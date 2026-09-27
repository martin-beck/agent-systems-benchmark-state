---
{
  "branch": "feature/ar-1471-control-to-runtime-chain-binding",
  "checkpoint_commit": "d76d099dcaa551c14c97e89c524e83bec6facd93",
  "claim_expires": "2026-09-27T03:28:58+00:00",
  "depends_on": [
    "AR-1357",
    "AR-1359",
    "AR-1362"
  ],
  "id": "AR-1471",
  "next_action": "Run independent review, publish exact signed head, monitor required checks, and merge only after all green.",
  "observed_branch": "feature/ar-1471-control-to-runtime-chain-binding",
  "observed_dirty": 0,
  "observed_head": "d76d099dcaa551c14c97e89c524e83bec6facd93",
  "owner": "ar1332_record_replay_luna56",
  "plan": "../plans/AR-1471-control-to-runtime-chain-binding.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Bind authenticated control enrollment to runtime certificate-chain storage and live dispatch.",
  "task_revision": 40,
  "title": "Control-to-runtime certificate-chain binding",
  "updated_at": "2026-09-27T00:28:58+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1471-control-to-runtime-chain-binding"
}
---

Narrow successor created from AR-1470’s protected-main audit. The predecessor
remains blocked because no control-owned chain population path exists; this AR
must provide that path or leave equally precise evidence without fabricating
authority.

- 2026-09-27T00:12:19+00:00: Dependencies AR-1357, AR-1359 and AR-1362 are done; promote the narrow
  control-to-runtime chain-binding successor from AR-1470 evidence.

- 2026-09-27T00:12:25+00:00: Claimed by ar1332_record_replay_luna56.

- 2026-09-27T00:12:47+00:00: Heartbeat by ar1332_record_replay_luna56.

- 2026-09-27T00:12:53+00:00: Recorded command exit 0; command argv SHA-256
  c6b5fb795af5d82a83fddb4a753a58a55724195a6c5b9aa78e1bb81a7cd2e8c4.

- 2026-09-27T00:14:27+00:00: Heartbeat by ar1332_record_replay_luna56.

- 2026-09-27T00:15:31+00:00: Recorded command exit 1; command argv SHA-256
  cb5df6982462d580e10b872468a9972740d1adb535a0f2b4d3efe1388b17aee5.

- 2026-09-27T00:15:51+00:00: Recorded command exit 0; command argv SHA-256
  5ac5bb6d548fcd1d8dd781f8adbe9ac1b816f52e1e2d03b36aeb25ab9c291aed.

- 2026-09-27T00:16:23+00:00: Recorded command exit 101; command argv SHA-256
  43ad1e1762aaf6e2461602705a37a10d3c527405f483846356f563f268ebf665.

- 2026-09-27T00:16:53+00:00: Recorded command exit 0; command argv SHA-256
  5ac5bb6d548fcd1d8dd781f8adbe9ac1b816f52e1e2d03b36aeb25ab9c291aed.

- 2026-09-27T00:17:20+00:00: Recorded command exit 101; command argv SHA-256
  43ad1e1762aaf6e2461602705a37a10d3c527405f483846356f563f268ebf665.

- 2026-09-27T00:17:50+00:00: Recorded command exit 0; command argv SHA-256
  5ac5bb6d548fcd1d8dd781f8adbe9ac1b816f52e1e2d03b36aeb25ab9c291aed.

- 2026-09-27T00:18:09+00:00: Recorded command exit 0; command argv SHA-256
  b0574b086b95a3d30d5aa2aeb0f191e494cdea0822bbad6a5ffd4eff116ea86e.

- 2026-09-27T00:18:34+00:00: Recorded command exit 101; command argv SHA-256
  43ad1e1762aaf6e2461602705a37a10d3c527405f483846356f563f268ebf665.

- 2026-09-27T00:19:04+00:00: Recorded command exit 0; command argv SHA-256
  397cd1664a932264a64e7cb13b68af27c7fd76c35acd4b37c3b2a758420b4363.

- 2026-09-27T00:19:24+00:00: Recorded command exit 101; command argv SHA-256
  bf6179ac6f458d1d25c7ea63058d8790c8f21397d369d3aa72a635e28d3e5933.

- 2026-09-27T00:20:23+00:00: Recorded command exit 0; command argv SHA-256
  8ada9c2867efaa0f9e37e332018f1142197ced00495ac3a66c52f3075da80da1.

- 2026-09-27T00:20:42+00:00: Recorded command exit 0; command argv SHA-256
  bf6179ac6f458d1d25c7ea63058d8790c8f21397d369d3aa72a635e28d3e5933.

- 2026-09-27T00:21:27+00:00: Recorded command exit 0; command argv SHA-256
  5ac5bb6d548fcd1d8dd781f8adbe9ac1b816f52e1e2d03b36aeb25ab9c291aed.

- 2026-09-27T00:21:48+00:00: Recorded command exit 0; command argv SHA-256
  5237ac57d60411756c6d7816afe217bab9ca6292e940921524d10f0ed918f376.

- 2026-09-27T00:22:34+00:00: Recorded command exit 0; command argv SHA-256
  ef1046126e0853167171fb6e0bc4c5bbf98c0acfb6e4fd09e7a7a9a1d76fae62.

- 2026-09-27T00:22:53+00:00: Recorded command exit 0; command argv SHA-256
  197a0d2cc50e88864281b3ee6506ef4427debef55f125f99596502e874512adb.

- 2026-09-27T00:23:49+00:00: Recorded command exit 0; command argv SHA-256
  41364c6a85aa67df0f68b6a3e4b6e793b7180c88f549c5e63640e504d709055e.

- 2026-09-27T00:24:29+00:00: Heartbeat by ar1332_record_replay_luna56.

- 2026-09-27T00:25:09+00:00: Recorded command exit 0; command argv SHA-256
  41364c6a85aa67df0f68b6a3e4b6e793b7180c88f549c5e63640e504d709055e.

- 2026-09-27T00:25:30+00:00: Recorded command exit 0; command argv SHA-256
  62f033d95327217a56911a46b908d58f64582ded6714e375bd965c89aac59ee4.

- 2026-09-27T00:26:19+00:00: Recorded command exit 0; command argv SHA-256
  d56ad5ded434658ec4b613d23736c5d18a365c4cec2b32b0fd9ce184a783d66a.

- 2026-09-27T00:26:34+00:00: Recorded command exit 0; command argv SHA-256
  bc07ba6eb09415f280be66128c917f1aeaf834d0f998b034df74addbdaf154ec.

- 2026-09-27T00:26:56+00:00: Recorded command exit 0; command argv SHA-256
  405e54f124981551b897e161159e652b5422355e3d8037198a8f188c92a48079.

- 2026-09-27T00:27:15+00:00: Recorded command exit 0; command argv SHA-256
  d0cef0e3c71fa5e52969e8f967cc48b078347f6acaede3d03cb9768f1bd8fd24.

- 2026-09-27T00:27:44+00:00: Implemented smallest control-owned chain binding.
  RuntimeReceiptResponseV1 now carries AuthenticatedChainEnrollmentV1 public metadata and validates
  the receipt chain digest against canonical metadata. Control emits the persisted authority chain;
  runtime reconstructs the opaque chain through issue_runtime_chain only from the control response,
  installs it into RuntimeCertificateChainStore, and the store install API is crate-private so
  callers cannot inject chains. Existing generation/freshness/target/tool/lease/relay/nonce/replay
  checks remain enforced. Added positive reconstruction and tampered generation tests, corrected
  response fixtures, regenerated v1.5/v1.6/v1.7 schemas, and documented the boundary. Focused tests:
  asb-control 67, asb-runtime 132, asb-cli 113; schema conformance 4; full workspace locked tests
  green; clippy -D warnings, rustdoc -D warnings, release build and diff-check green. Product commit
  d76d099dcaa551c14c97e89c524e83bec6facd93 is SSH-signed and DCO.

- 2026-09-27T00:27:52+00:00: Recorded command exit 0; command argv SHA-256
  17852d1beb84a2037d27f21780dd583d73bc1fddfa385fd67e5c97c68e0098f8.

- 2026-09-27T00:28:18+00:00: Recorded command exit 0; command argv SHA-256
  977d52791a1c88733052cda6878cbed3f49dc44401163887481d5a1645c0ea52.

- 2026-09-27T00:28:38+00:00: Recorded command exit 0; command argv SHA-256
  216df90683ebc03d630c9c6e5c0e4c418e5741461f2ed1800c02589da344fce9.

- 2026-09-27T00:28:58+00:00: Heartbeat by ar1332_record_replay_luna56.
