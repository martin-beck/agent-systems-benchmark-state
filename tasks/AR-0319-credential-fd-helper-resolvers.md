---
{
  "branch": "feature/credential-fd-helper-resolvers",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T19:20:40+00:00",
  "depends_on": [
    "AR-0318"
  ],
  "id": "AR-0319",
  "next_action": "Implement the bounded versioned allowlisted helper resolver and its timeout/cancellation/malformed/oversize/nonzero/privacy negatives; then run full focused gates and create a signed checkpoint.",
  "observed_branch": "feature/credential-fd-helper-resolvers",
  "observed_dirty": 3,
  "observed_head": "b2707c482876dcfb42c756c39165f6ecdb5c7c10",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0319.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add explicit file-descriptor and helper credential references without ambient-secret fallback.",
  "task_revision": 46,
  "title": "Implement credential FD and helper resolvers",
  "updated_at": "2026-09-08T17:18:27+00:00",
  "worktree_key": "agent-systems-benchmark-credential-fd-helper-resolvers"
}
---
## AR-0319

Implement the separately specified file-descriptor and helper credential boundaries. AR-0318 intentionally supports environment references only and rejects these sources fail-closed.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-08T14:06:44+00:00: Dependency AR-0318 is durably done for environment-only scope; assign
  FD/helper follow-up to an available worker under its separate contract.

- 2026-09-08T14:06:47+00:00: Claimed by quality_20260906.

- 2026-09-08T14:08:05+00:00: Recorded command exit 128; command argv SHA-256
  07fac809be61d7c080a8a5cda5d8e97d9997cedf5c681de74eb11e958d580bec.

- 2026-09-08T14:08:21+00:00: Recorded command exit 0; command argv SHA-256
  6e6df2a55efc77478194e288437c58d363861b4d7b304e38bd5d4b93b5b594d3.

- 2026-09-08T14:08:30+00:00: No worktree, heartbeat, command, or implementation appeared after
  repeated follow-ups; release the idle claim without losing any durable work. Reclaim when a worker
  can begin the declared FD/helper contract.

- 2026-09-08T15:01:34+00:00: Claimed by quality_20260906.

- 2026-09-08T15:03:02+00:00: Recorded command exit 0; command argv SHA-256
  f4376ee42e915b060ddb8bdb09d7931728d8d4b323edc9e2c7542ad151fa7439.

- 2026-09-08T15:08:17+00:00: Coordinator recovery after repeated live checks: lease remained valid
  but no worker process, heartbeat, checkpoint, or worktree change; no product mutation observed.
  Reopened for safe reassignment.

- 2026-09-08T16:20:40+00:00: Claimed by replay_20260906.

- 2026-09-08T16:21:07+00:00: Recorded command exit 0; command argv SHA-256
  6d00d6a2537319731c793799cc5964333d613efe4b6d7b16c38b23f33a1b00d4.

- 2026-09-08T16:36:13+00:00: Recorded command exit 1; command argv SHA-256
  ae7adfb84fb960d32209db091ec28c6c58abd444dc334f32e1fbc7676064b019.

- 2026-09-08T16:37:17+00:00: Recorded command exit 0; command argv SHA-256
  f18100a4b98ab47e39a6cb466d7c79af4d3f058a18369f768efa180248074bc0.

- 2026-09-08T16:38:08+00:00: Recorded command exit 0; command argv SHA-256
  83116e5b18bf1e859177bedff99e6bce69256477f57be09b48d3c2eed02ba24b.

- 2026-09-08T16:38:43+00:00: Recorded command exit 127; command argv SHA-256
  d87d777438e5646a04644833416e366081ee399a4d679784c41fdbae017b5b43.

- 2026-09-08T16:39:22+00:00: Recorded command exit 127; command argv SHA-256
  4e4abadb5ad6418e34d0c42aa4da77858dc7cfdda8e49c2e997bbdb482cea240.

- 2026-09-08T16:40:03+00:00: Recorded command exit 101; command argv SHA-256
  d76f8c8637306e15726c723d99d2fcc4dbdab74f661d488706b204b374e281a9.

- 2026-09-08T16:41:09+00:00: Recorded command exit 101; command argv SHA-256
  20cab3a823766424e0af4bccec487b202566710cf0b4de8fa377b6ac11263be7.

- 2026-09-08T16:41:48+00:00: Recorded command exit 0; command argv SHA-256
  cd418ae892bbfcbd6010238674a7d5d8011b1191688c64c613b8c9640f563709.

- 2026-09-08T16:42:52+00:00: Recorded command exit 101; command argv SHA-256
  a1368ed62b2458d0f21b5fee833011aa9b4bc5b1925ea0e80ebdc54f10255e78.

- 2026-09-08T16:43:12+00:00: Recorded command exit 101; command argv SHA-256
  0f4bb0d5655d9a0478980b4b5064e6332c3aa64e370abca0f78dc9d527121458.

- 2026-09-08T16:43:39+00:00: Recorded command exit 0; command argv SHA-256
  70ee44c9614a05994b53d15d8661f95a6f73b78064910e37ab606499e4d72d77.

- 2026-09-08T16:44:04+00:00: Implemented the one-shot OwnedFd half of AR-0319 in
  crates/asb-agents/src/credential.rs. The resolver accepts only an already-open owned descriptor
  plus bounded public logical locator, domain-separates the non-secret reference digest, validates
  current-process ownership, regular-file type, private mode, and size both before admission and
  immediately before the bounded read, consumes the resolver once, and explicitly makes no pre-open
  path-traversal claim. Added wrong-source, malformed-locator, group-readable, oversize, directory,
  one-shot resolution, and debug-redaction tests. Focused locked test passed: cargo test -p
  asb-agents credential --locked, 8 passed; cargo fmt check passed. Earlier cargo-not-found and
  duplicate-match failures were operator/source issues respectively and are repaired. Dirty scope is
  exactly crates/asb-agents/src/credential.rs; helper boundary remains.

- 2026-09-08T17:06:36+00:00: Recorded command exit 1; command argv SHA-256
  939d4a52f649c11fcd56281cc1de5c7b47301c656c173320d55daea5e0128ee0.

- 2026-09-08T17:07:11+00:00: Recorded command exit 0; command argv SHA-256
  a89abe4083db8c8cb663d5430d5d84ae9da99fc83a4e1ce435d7b7c9f71862d0.

- 2026-09-08T17:08:21+00:00: Recorded command exit 0; command argv SHA-256
  7f065c5dd01b3f3f12b53c7b133fadfa19e77fb356e0837e94b5eca2c1d4334f.

- 2026-09-08T17:09:03+00:00: Recorded command exit 0; command argv SHA-256
  ada2c7f12365a898b1d3e990becc8ddd0b1b8d924e80be902fb20c00fca7d3b3.

- 2026-09-08T17:09:45+00:00: Recorded command exit 0; command argv SHA-256
  e7a82fbd8dd4103e10e97858b85d5a20c7587ebc2623aaaef997460ac2d5f13b.

- 2026-09-08T17:10:33+00:00: Recorded command exit 0; command argv SHA-256
  ba3db8de73d7a2eb0384ae5c6e19d125cf4d691de56fe284d6b3419944d141fb.

- 2026-09-08T17:11:10+00:00: Recorded command exit 0; command argv SHA-256
  9a7fe2a57be2af048ce2f10bece8d0b736c2da18026bc6dc125b724451ae9e39.

- 2026-09-08T17:11:31+00:00: Recorded command exit 0; command argv SHA-256
  aca51f4b30728db5f7f8f50ad5215b5b887c86b04da76b1f6e317aa967506470.

- 2026-09-08T17:12:26+00:00: Recorded command exit 0; command argv SHA-256
  dad4017be4e8fa4d9df1c3f47f38e422a48e19477a26780fabec06c323b886fe.

- 2026-09-08T17:13:17+00:00: Recorded command exit 0; command argv SHA-256
  da1dd5761fd949f8fe994bbe554637dca833b31153dd1105ec3e20c9f4c74183.

- 2026-09-08T17:14:44+00:00: Recorded command exit 0; command argv SHA-256
  b4533c0c4538226c9cb5b2a8daee70c92ea0e88f0a7099e7f68375c51be00481.

- 2026-09-08T17:15:19+00:00: Recorded command exit 0; command argv SHA-256
  81c3e582cb4be9e3d55da7368fd7c1133e28c172fcb1b59050175f310ab9ea21.

- 2026-09-08T17:16:47+00:00: Recorded command exit 101; command argv SHA-256
  98f4a48fea5233f86f6fec1d4db0fb63b660389e7fee74de415f3bfa4ad595d5.

- 2026-09-08T17:17:13+00:00: Recorded command exit 101; command argv SHA-256
  3d45decc5c9297812ee7f1443daabf5271da86ea64b89994d04fb21726eda3a2.

- 2026-09-08T17:17:28+00:00: Recorded command exit 127; command argv SHA-256
  09f392711d1f36ef80867870516c34cacc8468b6838aa86bc0743264fc4a9039.

- 2026-09-08T17:17:42+00:00: Recorded command exit 1; command argv SHA-256
  6137587357eb24179f0acfd124c58ff041b286b7890d048d7c5abd2c8a043f07.

- 2026-09-08T17:17:57+00:00: Recorded command exit 1; command argv SHA-256
  97abb82dc91fc4cfc676c1652c1e06931f7944053a50bcc5040789e97003ba7e.

- 2026-09-08T17:18:27+00:00: Recorded command exit 0; command argv SHA-256
  de4697aa985563f9b99c51afdf58ef275ae0e03e62d28aa0a22183fdbbb21b86.
