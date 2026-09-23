---
{
  "branch": "feature/ar-1349-live-provider-runtime-service",
  "checkpoint_commit": "359f15af52aa2b0b31bb091b945e7de933960006",
  "claim_expires": "2026-09-23T18:30:27+00:00",
  "depends_on": [
    "AR-1327",
    "AR-1328",
    "AR-1339",
    "AR-1340",
    "AR-1347"
  ],
  "id": "AR-1349",
  "next_action": "Implement the production runtime-owned acquisition constructor: keep LiveProviderResolver authority-free, add a private resolver implementation only once a safe final credential sink exists, then atomically acquire gate/backend, lease, target/egress, observed namespace, token, relay, and opaque attempt with rollback tests. Current resolver seam is validated; CLI run/sweep remains fail-closed.",
  "observed_branch": "feature/ar-1349-live-provider-runtime-service",
  "observed_dirty": 2,
  "observed_head": "359f15af52aa2b0b31bb091b945e7de933960006",
  "owner": "codex-asb-ar1329-live-cli-luna56",
  "plan": "../plans/AR-1349-live-provider-runtime-service.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Implement production-owned atomic live-provider acquisition and wire it into asb run and sweep.",
  "task_revision": 117,
  "title": "Production live-provider runtime service",
  "updated_at": "2026-09-23T17:05:39+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1349-live-provider-runtime-service"
}
---

Coordinator successor for the exact authority gap recorded by AR-1348:
production asb run/sweep currently accepts only injected live-attempt factories,
while runtime constructors require caller-built leases, namespace handoffs,
tokens and relays. This task supplies the single rollback-safe owner for those
resources and preserves AR-1329 fail-closed until the service is merged and
qualified.

- 2026-09-23T16:30:20+00:00: Dependencies AR-1327, AR-1328, AR-1339, AR-1340 and AR-1347 are
  verified done. AR-1348 is superseded partial lifecycle evidence and intentionally removed from
  dependencies; promote this coordinator repair for claim readiness. AR-1329 remains fail-closed.

- 2026-09-23T16:30:27+00:00: Claimed by codex-asb-ar1329-live-cli-luna56.

- 2026-09-23T16:31:31+00:00: Recorded command exit 0; command argv SHA-256
  7c145cae25b02f870487e3a09450303496a9a72f7b01b10b754f5034e73197ad.

- 2026-09-23T16:32:49+00:00: Recorded command exit 0; command argv SHA-256
  d64018b6cc02f84681ffc81a8a687a9959932773ce8e540ab4b18e3a894b2ec5.

- 2026-09-23T16:33:05+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:33:20+00:00: Recorded command exit 101; command argv SHA-256
  f39ddc9090535b3b2a160bb90c4b1d5e119ca094c2325507a8605d9d70c7cc41.

- 2026-09-23T16:33:39+00:00: Recorded command exit 1; command argv SHA-256
  cfed275946058474104255568b4a97b2f5e01de3128ab82d9227d07909b6e35c.

- 2026-09-23T16:34:06+00:00: Recorded command exit 0; command argv SHA-256
  24423ae0d6263ecc645d6d714a004f5831d4b698d9b43fde431bd9ece2db1699.

- 2026-09-23T16:34:21+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:34:39+00:00: Recorded command exit 101; command argv SHA-256
  f39ddc9090535b3b2a160bb90c4b1d5e119ca094c2325507a8605d9d70c7cc41.

- 2026-09-23T16:34:56+00:00: Recorded command exit 1; command argv SHA-256
  55104e19d04ec3d1aa42c17252b2fc8e410d7becbd7a05cf9576bfd10db9bfc4.

- 2026-09-23T16:35:20+00:00: Recorded command exit 0; command argv SHA-256
  365c8f6a2163f4b9ff1d0af68f7e2da61b63671a11a716726d0a16aa57851301.

- 2026-09-23T16:35:35+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:35:49+00:00: Recorded command exit 0; command argv SHA-256
  f39ddc9090535b3b2a160bb90c4b1d5e119ca094c2325507a8605d9d70c7cc41.

- 2026-09-23T16:36:03+00:00: Recorded command exit 0; command argv SHA-256
  3c67c4833881f730ce72a765e5737a73baf8aba861438e8a87127a0f67ad6e60.

- 2026-09-23T16:36:17+00:00: Recorded command exit 0; command argv SHA-256
  a298b5318dd4e6c0119dd1178ea7ba52b9eeb8b2e9e5a38705367cf42fab255a.

- 2026-09-23T16:36:30+00:00: Recorded command exit 0; command argv SHA-256
  86f27a42fa21d59fa2778b589c752259a7fd0c1ad5ad46678846533bdb78d50f.

- 2026-09-23T16:36:52+00:00: Focused command initially failed missing-docs (11 public
  variant/accessor diagnostics); documentation was added. Next focused run failed because
  deterministic temp root reused a process-id-only path and returned LeaseError::Conflict(0);
  fixture now uses an atomic sequence and rerun passed 2/2. Product commit is SSH-signed with DCO.

- 2026-09-23T16:37:12+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-09-23T16:37:28+00:00: Recorded command exit 101; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:38:12+00:00: Recorded command exit 1; command argv SHA-256
  8a6e31cb818dcb1222ae07468911d8d10ac4e69b17f54071b14de329c6f11cbb.

- 2026-09-23T16:38:44+00:00: Recorded command exit 0; command argv SHA-256
  d33f5fb4a78eb721deabceca98cd7394238675ae3b19883e650daad653a3f10c.

- 2026-09-23T16:39:14+00:00: Recorded command exit 0; command argv SHA-256
  4c63dca99740f717218d79f6edb178041757d865b7f931a5b196d437693c133d.

- 2026-09-23T16:39:30+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:39:45+00:00: Recorded command exit 101; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:39:59+00:00: Recorded command exit 0; command argv SHA-256
  263e940e524da216d45cd3e8473e7e74273a57c4d49c9027ef3fbed491a0d8fc.

- 2026-09-23T16:40:14+00:00: Recorded command exit 0; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:40:29+00:00: Recorded command exit 0; command argv SHA-256
  f39ddc9090535b3b2a160bb90c4b1d5e119ca094c2325507a8605d9d70c7cc41.

- 2026-09-23T16:40:43+00:00: Recorded command exit 0; command argv SHA-256
  3c67c4833881f730ce72a765e5737a73baf8aba861438e8a87127a0f67ad6e60.

- 2026-09-23T16:40:58+00:00: Recorded command exit 0; command argv SHA-256
  0c6dfeea417fba46389637477cc5abc9e4fb6f687374c36681d050217bb949ae.

- 2026-09-23T16:41:12+00:00: Recorded command exit 0; command argv SHA-256
  43987d97dc56956b552198a06e4e2f896e43a7b7913c1a3e596b42a44e21da66.

- 2026-09-23T16:41:28+00:00: Recorded command exit 0; command argv SHA-256
  643da601527dbadf4103cccdc1a9fd542e36f7b77653982cc6fb4facfd524daf.

- 2026-09-23T16:41:42+00:00: Full applicable runtime gate passed after repair. First clippy failed
  on too_many_arguments for the 8-argument config constructor; grouped selection references into
  LiveProviderRuntimeSelection. The repair then had one compile diagnostic because not-a-digest was
  a string slice instead of String; converted explicitly. Final clippy passed, focused tests passed
  2/2, and full runtime tests passed 85/1.

- 2026-09-23T16:42:40+00:00: Recorded command exit 0; command argv SHA-256
  2ce745c8b75d61c003d6a7647d034b74f89a60ef240188d94e7f32b918d43777.

- 2026-09-23T16:42:55+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:43:09+00:00: Recorded command exit 101; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:43:24+00:00: Recorded command exit 0; command argv SHA-256
  b6f55af115fee906fe61e1dea381f9c8d73412ea37d8005f8e99bb35bc184640.

- 2026-09-23T16:43:40+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:43:56+00:00: Recorded command exit 0; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:44:12+00:00: Recorded command exit 0; command argv SHA-256
  f39ddc9090535b3b2a160bb90c4b1d5e119ca094c2325507a8605d9d70c7cc41.

- 2026-09-23T16:44:26+00:00: Recorded command exit 0; command argv SHA-256
  0c6dfeea417fba46389637477cc5abc9e4fb6f687374c36681d050217bb949ae.

- 2026-09-23T16:44:39+00:00: Recorded command exit 0; command argv SHA-256
  8eb2ae4dfaac2789a51076ff4dbb8729fb408a7f86b263caa352d2be488642b9.

- 2026-09-23T16:45:09+00:00: Composition clippy first failed with too_many_arguments (8/7) on
  compose_attempt; repaired by grouping the authority values into LiveProviderRuntimeAuthority
  without suppressing the lint. Focused tests and clippy then passed. Existing
  launch_factory/live_relay/live_namespace suites cover positive, expiry, revocation, duplicate and
  teardown behavior; this slice intentionally does not enable CLI wiring yet.

- 2026-09-23T16:45:55+00:00: Recorded command exit 0; command argv SHA-256
  ee0abc9cb299f26362ddfbfe3026d9d8dfec92547af47a68c4ece11ea436d860.

- 2026-09-23T16:46:10+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:46:26+00:00: Recorded command exit 101; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:46:46+00:00: Recorded command exit 0; command argv SHA-256
  1177666f9a2f12aced9cc8fcb7b1604001095b0da71f52d71fde14d462aa5aad.

- 2026-09-23T16:47:01+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:47:15+00:00: Recorded command exit 0; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:47:29+00:00: Recorded command exit 0; command argv SHA-256
  f39ddc9090535b3b2a160bb90c4b1d5e119ca094c2325507a8605d9d70c7cc41.

- 2026-09-23T16:47:43+00:00: Recorded command exit 0; command argv SHA-256
  0c6dfeea417fba46389637477cc5abc9e4fb6f687374c36681d050217bb949ae.

- 2026-09-23T16:47:56+00:00: Recorded command exit 0; command argv SHA-256
  0eea30cd930bf75eb2727f2831674dd7b8a58928af15d8004763b8e60c447a3e.

- 2026-09-23T16:48:17+00:00: Attempted composition clippy failed because private authority fields
  and compose_attempt had no legitimate production constructor (dead_code). This confirms the
  authority gap rather than a test defect. The public-field leak is repaired and the incomplete API
  removed in signed+DCO commit 97870c0. Existing CLI factory seams remain injection-only and are not
  wired into normal dispatch.

- 2026-09-23T16:49:13+00:00: Recorded command exit 0; command argv SHA-256
  7db9e0b56ba38f6ffcd94894208e1728b0c6d3c7c0c1f4ab31a8e90d511d2472.

- 2026-09-23T16:49:28+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:49:43+00:00: Recorded command exit 101; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:49:57+00:00: Recorded command exit 0; command argv SHA-256
  71cbdf274e7edf2cbdf5154bdba6f26d597813f526083003191cc0356011f70f.

- 2026-09-23T16:50:12+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:50:27+00:00: Recorded command exit 0; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:50:41+00:00: Recorded command exit 0; command argv SHA-256
  88ae6ad90f2deab7aaf1e8993c8be7a700129a314d466ba7949f76d449246e20.

- 2026-09-23T16:50:55+00:00: Recorded command exit 0; command argv SHA-256
  0e253cd3fad12735b85a07d0696e727acad419639d6ff94f924a89365fe3c9bd.

- 2026-09-23T16:51:09+00:00: Recorded command exit 0; command argv SHA-256
  18a65dddd9d5bfede44ca6f3b96429ae78f4628ad49be9e36c703267d445f326.

- 2026-09-23T16:51:33+00:00: Cross-crate audit confirmed asb-agents can depend on this runtime-owned
  trait without a runtime-to-agents cycle. The attempted public authority composition was removed in
  signed 97870c after independent review found externally constructible fields; no caller-built
  factory or CLI wiring was added. Initial credential boundary clippy failed on wrong SandboxSpec
  import and assert_eq requiring PartialEq on SandboxLaunchInput; repaired with correct import and
  matches!.

- 2026-09-23T16:52:37+00:00: Recorded command exit 0; command argv SHA-256
  13d48d34f5cca317272362b87e2c7f37865289326ed084a8c2a64cac5fd2f988.

- 2026-09-23T16:53:01+00:00: Recorded command exit 0; command argv SHA-256
  0aec8bebd20826fafa81557853aefdfaf0b1166bbde0d438fb695d9a0c50847b.

- 2026-09-23T16:53:23+00:00: Recorded command exit 0; command argv SHA-256
  152ba6e0ce9a4e2977eb5255dc4460f04257b4f093c6b33747e7d15d98f5b663.

- 2026-09-23T16:53:39+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:53:53+00:00: Recorded command exit 101; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:54:16+00:00: Recorded command exit 0; command argv SHA-256
  99d458d1154c1f2cedcb0054985ddbd8c99e0c8c5e37949988aeb1403f48f704.

- 2026-09-23T16:54:31+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:54:46+00:00: Recorded command exit 0; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:54:59+00:00: Recorded command exit 1; command argv SHA-256
  cd43b810873bebe59b1dc3af249f8c7a732d95cb6ea93b1f5208fe75343707d7.

- 2026-09-23T16:55:13+00:00: Recorded command exit 0; command argv SHA-256
  88ae6ad90f2deab7aaf1e8993c8be7a700129a314d466ba7949f76d449246e20.

- 2026-09-23T16:55:27+00:00: Recorded command exit 0; command argv SHA-256
  0c6dfeea417fba46389637477cc5abc9e4fb6f687374c36681d050217bb949ae.

- 2026-09-23T16:55:41+00:00: Recorded command exit 1; command argv SHA-256
  026476014347ae45229ab16e8f89e047318213f4513731d348b802c34bed7679.

- 2026-09-23T16:55:55+00:00: Attempted LiveRuntimeResolver acquisition boundary failed clippy with
  private_interfaces and dead_code because no production resolver or authority constructor exists.
  Removed the uninstantiated seam without suppressing gates. Final clippy passed and
  credential_injection tests passed 2/2. A combined cargo test invocation also failed with cargo
  usage error because cargo accepts one filter; reran the valid credential_injection filter
  successfully.

- 2026-09-23T16:57:03+00:00: Recorded command exit 0; command argv SHA-256
  4be9d08b47be99d60a4ea7209369f34b4a361977e5174b3f201e843401c557de.

- 2026-09-23T16:57:30+00:00: Recorded command exit 0; command argv SHA-256
  1dd652d0e5b1c98db25b00e8c612b45abed4d28c9597f83bd1ad8aed94e27314.

- 2026-09-23T16:57:52+00:00: Recorded command exit 0; command argv SHA-256
  8f5378d3805bd1ffb2e3dd6e52cd1b8c570afbee9d3516c8baa98580e094f9fe.

- 2026-09-23T16:58:18+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T16:58:33+00:00: Recorded command exit 0; command argv SHA-256
  0e8dce5ba5a78d9b987362d2ecd3e88d0c09e6e1e0255bb1426a359f52baf54f.

- 2026-09-23T16:58:47+00:00: Recorded command exit 0; command argv SHA-256
  f39ddc9090535b3b2a160bb90c4b1d5e119ca094c2325507a8605d9d70c7cc41.

- 2026-09-23T16:59:01+00:00: Recorded command exit 0; command argv SHA-256
  0c6dfeea417fba46389637477cc5abc9e4fb6f687374c36681d050217bb949ae.

- 2026-09-23T16:59:20+00:00: Recorded command exit 0; command argv SHA-256
  aa80c8ab38055ed90de36d909bf48c657f93219ea3b8de68cefa5ecaafede82f.

- 2026-09-23T17:00:06+00:00: Recorded command exit 0; command argv SHA-256
  8b7eaabb7c0b344d4f83f11f418e92d57616557626f32d523ad7d0066829e70f.

- 2026-09-23T17:00:35+00:00: Checkpoint 359f15a adds the cross-crate trait-first
  LiveProviderResolver seam. It accepts only LiveProviderRuntimeSelection and returns opaque
  CredentialInjection; resolver positive and fail-closed tests pass 3/3. Remaining exact blocker:
  CredentialInjection::inject currently receives SandboxLaunchInput but exposes no safe final
  credential target/sink, so asb-agents cannot implement a production adapter without exposing
  credential bytes or inventing authority. No CLI wiring added; AR-1329 remains fail-closed.

- 2026-09-23T17:00:45+00:00: Recorded command exit 0; command argv SHA-256
  cbae2543584d4d3bc8c81b1e1842c4dfb7ed56e3f75e18d5b9f9c9bfc41ef9af.

- 2026-09-23T17:01:01+00:00: Recorded command exit 0; command argv SHA-256
  fc5b4e5376bccccb5a56e54623314504eb4ec9b7ffb712e786dad39fa62d262d.

- 2026-09-23T17:01:17+00:00: Recorded command exit 0; command argv SHA-256
  7542d6cd9a5a1fe40492ebd7688db28e23911775442a508854c403190184a908.

- 2026-09-23T17:01:33+00:00: Recorded command exit 0; command argv SHA-256
  44d86351cf1eeec4aecfa9eb91983855aeabcb7aa743c8354c1a501364de2fbe.

- 2026-09-23T17:01:50+00:00: Recorded command exit 0; command argv SHA-256
  73ffde3f1ddbc3935e343856b3ee4d83fa6e852a62a904e9de21a50b9cb73153.

- 2026-09-23T17:02:06+00:00: Recorded command exit 0; command argv SHA-256
  1a473953d08a596658f361fd5a335254d77803f6ab025c09b6578261186f0179.

- 2026-09-23T17:02:23+00:00: Recorded command exit 0; command argv SHA-256
  493f4c18b30f59f4a19323512e986d727d99898eb16adf0771be62951d73a3aa.

- 2026-09-23T17:02:50+00:00: Recorded command exit 0; command argv SHA-256
  a64582dccae70efe022999691be5728b1a458437e0b606e276531f2ae5a4a24c.

- 2026-09-23T17:03:05+00:00: Recorded command exit 0; command argv SHA-256
  e80eada9395016fb494d0e499e1700e0dfac6886e22d6f0d5518352acb115eea.

- 2026-09-23T17:03:24+00:00: Recorded command exit 0; command argv SHA-256
  cc7f91b176c6fae066131d30a0a41521c68bbf28a61a6a64baf74c82f37a7008.

- 2026-09-23T17:04:43+00:00: Recorded command exit 0; command argv SHA-256
  aa58757cb4540dd7874bdc6eb14bab755335716044c1b10c7b9377414d716926.

- 2026-09-23T17:04:59+00:00: Recorded command exit 1; command argv SHA-256
  221aeaaf9040da0713a44881141249ab1c268472b3411539c3fcf9f8126eb37d.

- 2026-09-23T17:05:18+00:00: Recorded command exit 0; command argv SHA-256
  67138335f249d78ff455f950c8e42fb8019bc5afa30cdcc6ed983cefa0fabf35.

- 2026-09-23T17:05:39+00:00: Recorded command exit 101; command argv SHA-256
  caecff45df1811e9b7b1d0b7426674b16308e8441d3df922d993a212e331911b.
