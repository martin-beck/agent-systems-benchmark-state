---
{
  "branch": "repair/ar-1751-gcc-linker-prefix-confinement",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-09T02:28:21+00:00",
  "depends_on": [
    "AR-1737"
  ],
  "id": "AR-1751",
  "next_action": "Constrain development Cargo linker handoff so a validated ld cannot widen GCC helper or library trust through -B; add adversarial collect2/library regressions, independent exact-head review, signed reviewed-tree merge, and exact-main post-merge verification.",
  "observed_branch": "repair/ar-1751-gcc-linker-prefix-confinement",
  "observed_dirty": 2,
  "observed_head": "31ca7a481fca8b79bfbff126b92db6c6118beb7c",
  "owner": "codex-asb-ar1751-linker-confinement-20261009",
  "plan": "../plans/AR-1751-gcc-linker-prefix-confinement.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1751.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Confine the PATH-free development linker handoff to validated linker material without trusting sibling GCC helpers or libraries.",
  "task_revision": 54,
  "title": "Confine GCC linker-prefix trust after AR-1737",
  "updated_at": "2026-10-09T00:52:47+00:00",
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
