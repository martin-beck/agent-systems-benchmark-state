---
{
  "branch": "repair/ar-1751-gcc-linker-prefix-confinement",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T02:28:21+00:00",
  "depends_on": [
    "AR-1737"
  ],
  "id": "AR-1751",
  "next_action": "Repair independent-review P1 on PR #518 without rewriting d0ab2af: isolate the GCC capability probe in an owned process group, bound descendant termination/output drain after leader exit, prove linker-prefix CLOEXEC restoration on hostile descendant and timeout paths, then publish a new signed+DCO head and rerun exact-head gates.",
  "observed_branch": "repair/ar-1751-gcc-linker-prefix-confinement",
  "observed_dirty": 0,
  "observed_head": "abf4b6566c6e8bd519840587f440c0977652cc5b",
  "owner": "codex-asb-ar1751-linker-confinement-20261009",
  "plan": "../plans/AR-1751-gcc-linker-prefix-confinement.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1751.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Confine the PATH-free development linker handoff to validated linker material without trusting sibling GCC helpers or libraries.",
  "task_revision": 111,
  "title": "Confine GCC linker-prefix trust after AR-1737",
  "updated_at": "2026-10-09T01:42:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1751-gcc-linker-prefix-confinement"
}
---

AR-1737 repaired env-cleared TUI source materialization by preserving one
`CARGO_ENCODED_RUSTFLAGS` channel and passing `-B<validated-ld-parent>` to the
validated GCC driver. PR #509 merged that repair as signed reviewed-tree commit
`9aeea48c40417108b95c0a2743b2d4b3220f56bd`; its exact post-merge workflows
are green and the original `collect2: cannot find ld` failure is resolved.

Independent follow-up review found that the accepted trust claim is broader
than the implementation proves. GCC treats `-B` as a general program and
library prefix, not an `ld`-only locator. When `ASB_DEV_LD` names an otherwise
valid current-user-owned private `ld`, an unvalidated sibling `collect2`,
compiler helper, startup object, or library may be selected from the same
directory. A bounded `cc -### -B<private-root>` reproduction selected a sibling
`collect2` and added the directory to `COMPILER_PATH`, `LIBRARY_PATH`, and
linker `-L` inputs. Existing AR-1737 tests reject malformed or untrusted `ld`
paths but do not exercise a trusted `ld` with hostile siblings.

This successor owns only that trust-confinement defect. It must preserve the
successful PATH-free materialization, absolute descriptor-bound Cargo/rustc/
compiler/archiver selection, deterministic remap flags, content-addressed
installation, and typed unsupported-driver behavior. Development
authentication, production signing, provider credentials, and release
qualification remain visible warning-only concerns and are not blockers.

The repair must not trust or execute a directory merely because one file in it
passed validation. Acceptable designs include a private materialized linker
tool directory whose complete executable and library closure is explicitly
validated and descriptor-bound, or a compiler/linker invocation that selects
the validated linker without introducing a general GCC prefix. The worker must
measure the real GCC invocation and prove the selected design, rather than
assuming `LD`, `-fuse-ld`, or a wrapper has narrower semantics.

- 2026-10-09T00:12:29+00:00: AR-1737 is done; independent follow-up reproduced GCC -B trust widening
  to unvalidated helper and library siblings, so this P0 repair is dependency-ready.

- 2026-10-09T00:16:21+00:00: Claimed by codex-asb-ar1751-linker-confinement-20261009.

- 2026-10-09T00:16:48+00:00: Recorded command exit 0; command argv SHA-256
  20d576e89aa897f3a625489c98c4d7b6954cbd9822989ab00bde278518c51dad.

- 2026-10-09T00:22:31+00:00: Recorded command exit 0; command argv SHA-256
  7e367e178dfa59bbd2c8dc6fb3c0e1c884771571e39247ba7f21df312ff191b0.

- 2026-10-09T00:23:00+00:00: Heartbeat by codex-asb-ar1751-linker-confinement-20261009.

- 2026-10-09T00:23:28+00:00: Recorded command exit 2; command argv SHA-256
  48458d4adcbc2714c4ae60f17ec39d916357031118af6e75d9a5cd826c73f20e.

- 2026-10-09T00:24:11+00:00: Recorded command exit 0; command argv SHA-256
  f3b460b0087d7d95cfb915e359913c9d9b1b5ee1ae2853c80ef8112308f2318c.

- 2026-10-09T00:24:56+00:00: Recorded command exit 0; command argv SHA-256
  d5620ab877cae3855549555197859e75acbda4423fb56f74652b2979fd8fdde8.

- 2026-10-09T00:25:37+00:00: Recorded command exit 0; command argv SHA-256
  6b173dba5abaaaa9c5f467d5758b8a58db89c080b93d3f0d18476ab73bcd4aca.

- 2026-10-09T00:26:40+00:00: Recorded command exit 0; command argv SHA-256
  d7986ddbd301194ce24ff2c0a07814d371841a2df27a65b97a90cb7119a4bf5a.

- 2026-10-09T00:27:11+00:00: Recorded command exit 0; command argv SHA-256
  0e16666b13275f377ce506458d38de58bff2ad74054ea0d066ca8f73522bc17a.

- 2026-10-09T00:27:53+00:00: Recorded command exit 0; command argv SHA-256
  9d909bb688c2d95f68db246de98b0523f95f8c1ec95b958d8ec5751ebc5e2263.

- 2026-10-09T00:28:21+00:00: Heartbeat by codex-asb-ar1751-linker-confinement-20261009.

- 2026-10-09T00:28:28+00:00: Recorded command exit 1; command argv SHA-256
  57520e6591677431383d3c0c116e82e39183114204a0d60326fe8cc2de895f35.

- 2026-10-09T00:28:52+00:00: Recorded command exit 0; command argv SHA-256
  fb4b8baf40d5dd4a8518e90f3cbf47f476b8dc680bacf8835e9d4ed7ffa22ef4.

- 2026-10-09T00:29:40+00:00: Recorded command exit 0; command argv SHA-256
  f724ed9202346f83db2fb5ba9ea6f0c67ca7dbd6ebc289b470cc9110480758c3.

- 2026-10-09T00:30:03+00:00: Recorded command exit 0; command argv SHA-256
  e547da491a3bfba5eb64d002d442a5b4dcd8e5ba1a282b9a95f97e3c701b1a86.

- 2026-10-09T00:30:34+00:00: Recorded command exit 101; command argv SHA-256
  7b6ab384037369692da6979ff23adbb72eaaeebba0446123fbe6b74e7149c318.

- 2026-10-09T00:31:19+00:00: Recorded command exit 0; command argv SHA-256
  721e99fdcf45164ef137af52b92ac7dbf907ed17d77ddc7dbc1ca462b305dd3b.

- 2026-10-09T00:31:55+00:00: Recorded command exit 0; command argv SHA-256
  7b6ab384037369692da6979ff23adbb72eaaeebba0446123fbe6b74e7149c318.

- 2026-10-09T00:32:29+00:00: Recorded command exit 0; command argv SHA-256
  6ae73296c78856fe58a5fed504e3fac3202f49deeff6fd9d9c2313cdfc611332.

- 2026-10-09T00:33:34+00:00: Recorded command exit 0; command argv SHA-256
  3055801af6460b5969d3841203c313bcbe7c601c041b4d335d979f9a69b71156.

- 2026-10-09T00:34:00+00:00: Recorded command exit 0; command argv SHA-256
  fb4b8baf40d5dd4a8518e90f3cbf47f476b8dc680bacf8835e9d4ed7ffa22ef4.

- 2026-10-09T00:34:35+00:00: Recorded command exit 101; command argv SHA-256
  755deb167b3c50bacaba5b8cb6acf06603c8cb08f22da41a78e5ea9c89875e25.

- 2026-10-09T00:35:33+00:00: Recorded command exit 0; command argv SHA-256
  bd4d8ff2c6455dc4a9cda15145cb6cb96ab249918ff2c68e5b304b42625bfff8.

- 2026-10-09T00:36:13+00:00: Recorded command exit 0; command argv SHA-256
  755deb167b3c50bacaba5b8cb6acf06603c8cb08f22da41a78e5ea9c89875e25.

- 2026-10-09T00:36:48+00:00: Recorded command exit 0; command argv SHA-256
  4ab06b4f5470c9c04604f1ca0195e3451adc51f6902ec42caff8847ae3f6d174.

- 2026-10-09T00:37:29+00:00: Recorded command exit 101; command argv SHA-256
  31560e2e5dc7a77f3cc461c7f92b112bc80eb91e6018a16614325b5bdbcc9c78.

- 2026-10-09T00:38:05+00:00: Recorded command exit 0; command argv SHA-256
  67d58de66fa42891d6883e4bc4a927465dd667745f0bfbd38a580e40562cd30f.

- 2026-10-09T00:38:41+00:00: Recorded command exit 0; command argv SHA-256
  31560e2e5dc7a77f3cc461c7f92b112bc80eb91e6018a16614325b5bdbcc9c78.

- 2026-10-09T00:39:08+00:00: Recorded command exit 0; command argv SHA-256
  80ccb6f9b9fc91ee962c78557c30d5faeb59b0c82db8e60d86d5ba2aaf781ecb.

- 2026-10-09T00:40:04+00:00: Recorded command exit 0; command argv SHA-256
  f00f2cde68a37ff08c6f2cae3bc87692618d2e8c5d94de608bb2acc493b6d165.

- 2026-10-09T00:40:37+00:00: Recorded command exit 0; command argv SHA-256
  bead7c07c5303e762b6d89faab2b39e7dd362eda55ee8f7ad9e8a9891fa35b2c.

- 2026-10-09T00:41:16+00:00: Recorded command exit 0; command argv SHA-256
  a769f0def3b6320fbaefcc4adfbe75e5c60a423c7325948e2c829233c5f7bcf3.

- 2026-10-09T00:41:50+00:00: Recorded command exit 0; command argv SHA-256
  fb4b8baf40d5dd4a8518e90f3cbf47f476b8dc680bacf8835e9d4ed7ffa22ef4.

- 2026-10-09T00:42:28+00:00: Recorded command exit 0; command argv SHA-256
  13c39bfabde755f2383acb94a75d7cf59e9b3a61bf5b3b57ab0af6c2da1ae65e.

- 2026-10-09T00:43:14+00:00: Recorded command exit 0; command argv SHA-256
  b7025edc1cbcb4e54a1a121fb09ec9e259c5e1148efa26b91c0d45861f868841.

- 2026-10-09T00:44:09+00:00: Recorded command exit 0; command argv SHA-256
  1192246c336ff11519735d66981813d3984217358e752808a9829a1935cba65e.

- 2026-10-09T00:44:50+00:00: Recorded command exit 0; command argv SHA-256
  f43e02552ae55771106250a738e23b6aa55653d24e5725f327d7e99f646a159e.

- 2026-10-09T00:45:20+00:00: Recorded command exit 0; command argv SHA-256
  d0bdbc42a0893a7a4b2217805de3c9f10ea490d0318ab7cda33fc15401bdc202.

- 2026-10-09T00:46:04+00:00: Recorded command exit 0; command argv SHA-256
  f98ad1b35c9c3126afdeb9655e85d4429c75e774c38ba10e636a937e0707a119.

- 2026-10-09T00:46:56+00:00: Recorded command exit 101; command argv SHA-256
  3fcce20bed07e7718f811eb4fd2d125b559f0254db12d1231c42cc957b41925e.

- 2026-10-09T00:47:23+00:00: Recorded command exit 0; command argv SHA-256
  b6743fb070da21d0e990d7dfdce616e23a5604f6552465f92fb78bc1593e385b.

- 2026-10-09T00:48:23+00:00: Recorded command exit 0; command argv SHA-256
  2ecba79404c32ce62d79a4217472274185c19a054549daf4e5765eb1d9950555.

- 2026-10-09T00:48:46+00:00: Recorded command exit 0; command argv SHA-256
  57520e6591677431383d3c0c116e82e39183114204a0d60326fe8cc2de895f35.

- 2026-10-09T00:49:16+00:00: Recorded command exit 0; command argv SHA-256
  ed560a138611157382ecff34acbe7992d6645bc6ed77dcf1e28e3432967f7b60.

- 2026-10-09T00:49:52+00:00: Recorded command exit 0; command argv SHA-256
  3c1491cb17d0f655aa1e73087038b959374f4c9fa146ca45dc3cead79c8f3e77.

- 2026-10-09T00:50:49+00:00: Recorded command timeout; classification=SUBPROCESS_TIMEOUT;
  deadline=30.0s; command argv SHA-256
  3359ea7f6c49a63a81c01f5eb97457f80dcb945b3cf5c15263bdc90f018fa8c2.

- 2026-10-09T00:51:54+00:00: Recorded command timeout; classification=SUBPROCESS_TIMEOUT;
  deadline=30.0s; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-10-09T00:52:47+00:00: Recorded command exit 0; command argv SHA-256
  3359ea7f6c49a63a81c01f5eb97457f80dcb945b3cf5c15263bdc90f018fa8c2.

- 2026-10-09T00:54:46+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-10-09T00:55:33+00:00: Recorded command exit 0; command argv SHA-256
  c0f57d1d798b7a8917d4abf09040e8fabdb33d8832cd535fbe763651686434fc.

- 2026-10-09T00:56:31+00:00: Recorded command exit 2; command argv SHA-256
  e91ce9e360b2ef23caf02c647ed67656d50994585c9eea194cba44de848dadc2.

- 2026-10-09T00:57:06+00:00: Recorded command exit 1; command argv SHA-256
  1016e0c7824e83945479932b108de7e0c7d9910dcb0498794b2c8f7e93a79187.

- 2026-10-09T00:58:42+00:00: Recorded command exit 0; command argv SHA-256
  ffe340c31318347c5b854c0ac30f09bd03bc74b929e218c23f2aac2c86b3ce81.

- 2026-10-09T00:59:17+00:00: Recorded command exit 0; command argv SHA-256
  d63d7312423827138a245cbd71da98280daffead44100a18e2373f24d915510d.

- 2026-10-09T01:00:01+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-09T01:00:54+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-09T01:01:31+00:00: Recorded command exit 1; command argv SHA-256
  a67afb658e54fcdf9243291109f9ffd640f5eec8fd2e678729ae69ed886c0495.

- 2026-10-09T01:02:34+00:00: Recorded command exit 0; command argv SHA-256
  0224becc96abe9a3efaaf104916ea030d109e9da14229bec86c4f3997c16d2bd.

- 2026-10-09T01:03:10+00:00: Recorded command exit 0; command argv SHA-256
  5fbf8cf5f7a5033b168f87348a1437fc40d72ecd1e1d68cf72198b21c522c119.

- 2026-10-09T01:03:49+00:00: Recorded command exit 0; command argv SHA-256
  c91f3e5478c7be4eebf65c02b491563b30a55d29cc816ccd5010d4763e5e2ed9.

- 2026-10-09T01:04:28+00:00: Recorded command exit 0; command argv SHA-256
  135dd029d6eb25cc93b115df3a1b5a365dd48f9579819dc173ab8055b21d0964.

- 2026-10-09T01:05:13+00:00: Recorded command exit 0; command argv SHA-256
  692e6a393f530544f87bf3f04d107d200bc76e40bf9a03bc6f8cf117b171c9a9.

- 2026-10-09T01:05:48+00:00: Recorded command exit 2; command argv SHA-256
  38f8e785410e1ac95c495596106e2d18b34191db3f2c73c5c2ba5fb43360d00c.

- 2026-10-09T01:06:53+00:00: Recorded command exit 0; command argv SHA-256
  068ac1bbb9bb8fd61e34a1baa5c104dd47c832ca41f5b2ef0ab556fe2dfce952.

- 2026-10-09T01:07:29+00:00: Recorded command exit 0; command argv SHA-256
  2dcee4ba2e5fc305f725a24b2d75ea65ede63cbf62ba861cb87b304fec91104a.

- 2026-10-09T01:08:01+00:00: Recorded command exit 0; command argv SHA-256
  c91af6b9389ebd6ee7eb9e04f24befe09ac576a8c96e974c30b57403446423e4.

- 2026-10-09T01:08:45+00:00: Recorded command exit 0; command argv SHA-256
  1a0188ded711ad0cd9da3c2c01be3cb7daee4e9f2d1d5bba2ae3294d5a65c6c3.

- 2026-10-09T01:09:29+00:00: Recorded command exit 0; command argv SHA-256
  dc4a8581b37a2bf9f6f393251c1a291b2dfeee075edbcc11e15b492901a0105b.

- 2026-10-09T01:10:21+00:00: Implemented GCC -B trust confinement at signed+DCO head
  d0ab2af3fed2f73f4c31c56dfbe715f897483e94 and opened PR #518. The fresh 0500 descriptor-bound
  prefix contains exactly one retained regular ld; empty ambient PATH is preserved; GCC driver
  semantics fail closed; adversarial siblings, startup/library inputs, pathname/inode substitution,
  descriptor lifetime, real Cargo linking, and deterministic roots are tested. Local fmt, clippy,
  workspace tests, docs, release build, coverage, cargo-deny, cargo-audit, contract consistency,
  repository policy, and revision-scoped Gitleaks passed. Awaiting exact-head hosted CI and
  independent review.

- 2026-10-09T01:18:46+00:00: All 15 hosted checks on exact PR #518 head
  d0ab2af3fed2f73f4c31c56dfbe715f897483e94 reached terminal SUCCESS, including Rust verification,
  repository policy/coverage/supply chain, Exact TUI inherited-fd and PTY journey, emulated AArch64,
  formal, fault, platform, provider journey, headers, provenance, and AWQ shadow evidence. Head/base
  remain immutable and GitHub reports MERGEABLE. Stop implementation now for independent review.

- 2026-10-09T01:18:57+00:00: Correction: the previous CI-complete update transcribed an incorrect
  tree identifier. Direct git show verification binds immutable head
  d0ab2af3fed2f73f4c31c56dfbe715f897483e94 to actual tree 529eb72b41b7a9692dffa2cf041d99bb9264cb25.
  No product or PR head changed; all 15 exact-head checks remain terminal SUCCESS.

- 2026-10-09T01:20:06+00:00: Independent review rejected exact head d0ab2af with one P1:
  validate_development_gcc_driver invokes the accepted compiler without an owned process group; a
  hostile unsupported driver can leave a descendant retaining stdout and the linker-prefix
  descriptor after the leader exits, causing an unbounded reader join and delayed CLOEXEC
  restoration. Repair is active within AR-1751; no merge authorized.

- 2026-10-09T01:21:11+00:00: Recorded command exit 1; command argv SHA-256
  4fe5e6df52eee69f9abda47b6896be6dcde0d41f363cfac5b974b99168d876d4.

- 2026-10-09T01:21:45+00:00: Recorded command exit 0; command argv SHA-256
  5efa18de19f3a3e5585d90236c05598ade10ce6412423fbbe963e30f5c46b0f0.

- 2026-10-09T01:22:30+00:00: Recorded command exit 0; command argv SHA-256
  7b156112aa4a88b51b6049649edc1f0a823796afe35fb6f82149d0c42514af2e.

- 2026-10-09T01:23:53+00:00: Recorded command exit 0; command argv SHA-256
  8fdde20983e4c77ecab7f81031f637b058134f1a675ef0db44d1fc645c483f03.

- 2026-10-09T01:24:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-09T01:25:12+00:00: Recorded command exit 0; command argv SHA-256
  135dfd9e5eb6a46062c009508e08c1a6f55eed876599e3dcf89741d215dab2e6.

- 2026-10-09T01:25:53+00:00: Recorded command exit 0; command argv SHA-256
  291fabd83bf08a767418181c052af16df89b1ad4479b78758e72c89c9c1f0ad8.

- 2026-10-09T01:26:59+00:00: Recorded command exit 0; command argv SHA-256
  3517f2b26eadb6609af14a58c82536802012e0fa6d66c24f147f9f62f61582df.

- 2026-10-09T01:27:48+00:00: Recorded command exit 0; command argv SHA-256
  d316f9e6400aa4376f45b8c54329dc128b3090d1e089574a2b28a1fc3225c953.

- 2026-10-09T01:28:31+00:00: Recorded command exit 101; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-09T01:29:10+00:00: Recorded command exit 0; command argv SHA-256
  97e7816e83edf5a2d4f4653887d8078397837e3cf36c4ac9a4568339eb0c9652.

- 2026-10-09T01:29:56+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-10-09T01:30:48+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-09T01:31:53+00:00: Recorded command exit 0; command argv SHA-256
  534f8613e1c316db8f0f46dd989e44e14a8ca74304a94791b4e4a1c59b2fbb1d.

- 2026-10-09T01:32:32+00:00: Recorded command exit 0; command argv SHA-256
  8f020a8266d9eda8e0ed704996e99736ad1cf29c0294cefaaa456dc2d9fb4d92.

- 2026-10-09T01:33:19+00:00: Recorded command exit 0; command argv SHA-256
  b49a90ee600c1023cee9ee9f9e8a4f9a06c53eef8c48d3932d88e482126c7c01.

- 2026-10-09T01:35:14+00:00: Recorded command exit 0; command argv SHA-256
  428457ea9cc6a21bd46c5be6651ba2faccb5b0b07ddc2fd6f96eca730dea5ab7.

- 2026-10-09T01:36:00+00:00: Recorded command exit 0; command argv SHA-256
  a8bfa440da1f12609ada01706cdfa120ee974b03f536a1cf08c038c4d47aad08.

- 2026-10-09T01:36:59+00:00: Recorded command exit 0; command argv SHA-256
  1c54efcf97a8d6ca0d40110ce0c16d144f594daa8ccc247053c5eafb09e35dd1.

- 2026-10-09T01:37:39+00:00: Recorded command exit 0; command argv SHA-256
  45b5dee649fa61e12cc2b66b33dce91304987e6ec92f4f5d2115a0b0973ee782.

- 2026-10-09T01:38:18+00:00: Recorded command exit 0; command argv SHA-256
  1024fc1e6cefa31b078f0b5d2ed85c7ea4586897b388bf1e308f62db58574461.

- 2026-10-09T01:38:59+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-09T01:39:39+00:00: Recorded command exit 0; command argv SHA-256
  ca99b5a10295bded484eb593d2cee41502083c20fecd1bf8462bce5abbf3173e.

- 2026-10-09T01:40:16+00:00: Recorded command exit 0; command argv SHA-256
  a467e292008164cbf906c15cdae5a26bd9a6eecd744d133672dd03c54f9a225a.

- 2026-10-09T01:41:32+00:00: Recorded command exit 0; command argv SHA-256
  68a858452d9e83512d3b8e0136d37361cc4ffa703cc8f71cb7e06a58f98721bf.

- 2026-10-09T01:42:15+00:00: Recorded command exit 0; command argv SHA-256
  a130d68a3f619cb2e704bef42739a4afaa9d969fc1eb3044974386a52a9beae3.
