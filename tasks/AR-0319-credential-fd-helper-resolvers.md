---
{
  "branch": "feature/credential-fd-helper-resolvers",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T22:18:49+00:00",
  "depends_on": [
    "AR-0318"
  ],
  "id": "AR-0319",
  "next_action": "Run full exact-tree formal/fault/privacy/supply gates on signed successor 75094148, then request fresh independent immutable review; do not publish.",
  "observed_branch": "feature/credential-fd-helper-resolvers",
  "observed_dirty": 0,
  "observed_head": "75094148f951467a10f31e02aaf482b3fef9c4a8",
  "owner": "replay_20260906",
  "plan": "../plans/AR-0319.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add explicit file-descriptor and helper credential references without ambient-secret fallback.",
  "task_revision": 87,
  "title": "Implement credential FD and helper resolvers",
  "updated_at": "2026-09-08T19:33:33+00:00",
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

- 2026-09-08T17:19:21+00:00: Recorded command exit 0; command argv SHA-256
  0fc5cee85e5e201f3f1bf792b823b5c8c8324df0d3d534868322ee77de72fcd3.

- 2026-09-08T17:20:17+00:00: Recorded command exit 101; command argv SHA-256
  22b9e05f86710b7ae93d13d5a3e2e8184fcd5758de465a98f11500c2eb25ff58.

- 2026-09-08T17:20:37+00:00: Recorded command exit 0; command argv SHA-256
  2084d1d7ef24b79ada1b4298ed2372e4ffd4d82bdd5fc760f4c64bbf111442d2.

- 2026-09-08T17:21:45+00:00: Recorded command exit 0; command argv SHA-256
  2f461c2a588e1659d036906c34364246dfbdbe3f9331ff713d87eecf7b693391.

- 2026-09-08T17:22:05+00:00: Recorded command exit 0; command argv SHA-256
  ca8023753f0c7f0e8972c6ce18d8e7b6aa89ed4ee205a2000d13381d1e8b384e.

- 2026-09-08T17:22:17+00:00: Recorded command exit 0; command argv SHA-256
  ef7934f00f98755180e5d04c87b26345da55df74ede92b6bab926227bf08906e.

- 2026-09-08T17:22:56+00:00: Signed+DCO checkpoint d2e08d8d9bfa8b728fa93c1d1aa53a955573f03e (tree
  ca27f1b0e1c229e6a6ecab10bf2f0cf7b11ba87c, parent b2707c482876dcfb42c756c39165f6ecdb5c7c10)
  implements both AR-0319 boundaries in four paths. OwnedFd resolution is one-shot and validates
  logical reference, current UID, regular type, private mode and size before admission/read. Helper
  v1 binds logical locator plus exact executable SHA-256, revalidates metadata/hash pre-spawn, uses
  only the fixed protocol argv with cleared environment/stdin, bounded JSON/stdout/stderr/deadline,
  idempotent process-group cancellation/reaping, and generic non-secret errors. Negatives cover
  wrong source/digest/mode/type/locator/deadline, malformed/extra-field/stderr/nonzero/oversize
  response, timeout and double cancel. Exact Cargo delta is one existing-locked rustix 1.1.4 fs edge
  and one lock package-edge line. Focused locked credential tests pass 12/12; all-target Clippy -D
  warnings and fmt/diff-check pass. Failed intermediate commands are classified in the
  implementation history and repaired.

- 2026-09-08T18:33:39+00:00: Recorded command exit 0; command argv SHA-256
  144bf83ec51c4a44f3e0a3a06a1c4527fec12c8e38f72ff1fec5e4f27f57cad5.

- 2026-09-08T18:34:03+00:00: Recorded command exit 0; command argv SHA-256
  e5a18d1c951ecdc2179e06a0c0e439b982754b715287efb7980962cade804afd.

- 2026-09-08T18:34:34+00:00: Recorded command exit 0; command argv SHA-256
  4b1b3821a21bba208eab21046c7bb1222c370e032c73aaebd60e56cb4c4aca6f.

- 2026-09-08T18:34:59+00:00: Recorded command exit 0; command argv SHA-256
  1c242a8f337bda2e8798e3607ae99941d4bf6f08e0d9445a4bb170aa064da062.

- 2026-09-08T18:35:47+00:00: Recorded command exit 0; command argv SHA-256
  6287c5189171bba9c389820455bb937c8f1475f485536821344619059b97f8a3.

- 2026-09-08T18:36:16+00:00: Recorded command exit 1; command argv SHA-256
  b65dc4739fdac6cea4a53cffe6fa8a8b6fd8effa7d63f1948ca475dbbecf2c37.

- 2026-09-08T18:36:46+00:00: Recorded command exit 0; command argv SHA-256
  6a27cdaf0172997b81245a83f69f45c57748aa8f4f92c9babc5a893cff539d6d.

- 2026-09-08T18:37:13+00:00: Recorded command exit 101; command argv SHA-256
  7c836ec1e8fa49b52060ff7c4ef383e99f71cc4439c54a210cdad3f6f919c2f4.

- 2026-09-08T18:38:06+00:00: Recorded command exit 0; command argv SHA-256
  45a809fa68e77646ee070ad5a856fe7a7c0dca30bcbdcff003d09da6e9aed1b2.

- 2026-09-08T18:40:05+00:00: Recorded command exit 0; command argv SHA-256
  fc8881aefec9a5a1bd6b2d88b8c27f0abccaeec2917c03acf8c3b97ef971f9ad.

- 2026-09-08T18:40:50+00:00: Recorded command exit 0; command argv SHA-256
  21456a2b8d93eea394ba93118d52fbdc9f978156bb8f8cf71e472d126c244d8b.

- 2026-09-08T18:41:54+00:00: Recorded command exit 0; command argv SHA-256
  9f26f672441373aaf9730b919c92f40232a1eb2641e31cd57058be6a70a36d83.

- 2026-09-08T18:42:34+00:00: Recorded command exit 1; command argv SHA-256
  9e6a915b274d3eafe89687f14c7c0a09df49467da6aedac374c14dd2dba02128.

- 2026-09-08T18:42:54+00:00: Recorded command exit 0; command argv SHA-256
  67c3f5ffa15c01865ac41a027c483b5f663735d018751eb2169fe5aba0df327f.

- 2026-09-08T18:43:46+00:00: Exact immutable candidate d2e08d8d9bfa8b728fa93c1d1aa53a955573f03e
  (tree ca27f1b0e1c229e6a6ecab10bf2f0cf7b11ba87c, parent b2707c482876dcfb42c756c39165f6ecdb5c7c10)
  remains clean, SSH-signed by Martin Beck, and DCO-certified. Exact scope is four paths:
  Cargo.lock; crates/asb-agents/Cargo.toml; crates/asb-agents/README.md;
  crates/asb-agents/src/credential.rs. Terminal green gates: cargo test --workspace --all-targets
  --locked; cargo test --doc --workspace --locked; release workspace build; exact base..head
  repository policy; formal locked Rust/Loom/production/recovery tests; offline TLC 3,709-state
  depth-17 proof plus Alloy positive and six mutation receipts; mutation sentinels 7/7 caught; all
  four pinned fuzz targets at 256 runs each with lock digest and clean-tree checks; contract
  consistency; actionlint; zizmor; one-commit redacted Gitleaks; cargo-deny; cargo-audit; coverage
  floors (workspace lines 90.55%, core 99.40%, replay 97.73%); controlled quality failure paths;
  platform manifests and 23 platform tests; final clean tree. One initial quality-fixture invocation
  lacked cargo on PATH and was corrected without source change. Local cargo-kani 0.67.0 is
  environment-blocked before proof discovery: it reports failed to start cargo metadata, No such
  file or directory, despite the pinned real cargo binary being present; this candidate does not
  change formal harnesses and hosted formal CI must provide the independent Kani result. No product
  blocker found; ready for immutable review, not publication.

- 2026-09-08T19:13:27+00:00: Recorded command exit 127; command argv SHA-256
  3999ff83e280359932d71c7acb8e3a4eb73ae340e5bd3b9cebcf2200a93ade03.

- 2026-09-08T19:13:38+00:00: Recorded command exit 101; command argv SHA-256
  875cb5c5f39fe82e2182f24c8c91ef370cdcf2012f1c1eda4142ce7c3e4c06a5.

- 2026-09-08T19:14:14+00:00: Recorded command exit 127; command argv SHA-256
  787c693fcd4c3d96f4200c4acf49b5410d2f8d99ba2696400978096dddd5c663.

- 2026-09-08T19:14:39+00:00: Recorded command exit 0; command argv SHA-256
  e9bb85f53b519c10a9ba4268cb89577c78aff86c44f9c2d1520ac11958978266.

- 2026-09-08T19:15:02+00:00: Recorded command exit 0; command argv SHA-256
  875cb5c5f39fe82e2182f24c8c91ef370cdcf2012f1c1eda4142ce7c3e4c06a5.

- 2026-09-08T19:16:00+00:00: Recorded command exit 0; command argv SHA-256
  f19780845a36e4583fc2ae507141dbec3e11691c68a505dc9cfaf9a58637f604.

- 2026-09-08T19:16:26+00:00: Recorded command exit 0; command argv SHA-256
  875cb5c5f39fe82e2182f24c8c91ef370cdcf2012f1c1eda4142ce7c3e4c06a5.

- 2026-09-08T19:16:52+00:00: Recorded command exit 0; command argv SHA-256
  ff05d1eeb91a55403ea70f73a9c3f831a0b70408e72205a54b74fe4db20c3fad.

- 2026-09-08T19:17:16+00:00: Review-block repair produced new single signed+DCO candidate
  75094148f951467a10f31e02aaf482b3fef9c4a8 (tree 12654991a8114ae3daefdde7d7090d406f6fa6b8, parent
  b2707c482876dcfb42c756c39165f6ecdb5c7c10), replacing unpublished d2e08d8d. Helper admission now
  copies only exact expected-SHA bytes into a CLOEXEC memfd, chmods it owner read/execute, seals
  write/grow/shrink/further-seals, revalidates seals/hash before start, and launches through the
  still-open parent procfd without ever clearing CLOEXEC. Deterministic negatives prove the sealed
  FD rejects writes; original inode mutation then pathname replacement cannot alter executed bytes;
  the helper child sees no staged memfd descriptor; and 16 unrelated children spawned concurrently
  see no staged descriptor. Focused credential tests pass 14/14, including
  timeout/cancel/malformed/nonzero/oversize/privacy cases; all-target asb-agents Clippy -D warnings,
  fmt and diff-check pass. An initial compile exposed only Read/Write by_ref ambiguity and was
  repaired by fully qualified writes. Candidate worktree is clean. Full successor gates remain
  pending.

- 2026-09-08T19:18:01+00:00: Recorded command exit 0; command argv SHA-256
  3d560b4e9adeff801cf1cc1ffcfea302c3f94f9d6b23942a4f83c47d8bdc1717.

- 2026-09-08T19:18:37+00:00: Recorded command exit 0; command argv SHA-256
  e0654f13a662838befc37ca28d2061522d4660354f31cf19361820a78ed138f0.

- 2026-09-08T19:18:49+00:00: Heartbeat by replay_20260906.

- 2026-09-08T19:19:21+00:00: Recorded command exit 0; command argv SHA-256
  fe7c556fa54025ef47385a0c5b1ed6b2dee9ff9083ed17a6cc40f3976e6a4ae1.

- 2026-09-08T19:20:46+00:00: Recorded command exit 0; command argv SHA-256
  6d88d5445e00d7459082f62a3d4939d7bae348764809aeebcce16058424068c6.

- 2026-09-08T19:33:33+00:00: Recorded command exit 0; command argv SHA-256
  9f26f672441373aaf9730b919c92f40232a1eb2641e31cd57058be6a70a36d83.
