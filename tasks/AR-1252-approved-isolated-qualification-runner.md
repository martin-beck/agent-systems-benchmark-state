---
{
  "branch": "feature/ar-1252-approved-isolated-runner",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-1252",
  "next_action": "Monitor post-merge workflows for main 85bcd1e until terminal; verify exact tree/signature/DCO/policy, then release AR-1252 done.",
  "observed_branch": "feature/ar-1252-approved-isolated-runner",
  "observed_dirty": 0,
  "observed_head": "1d0c3cd017e8d486231dabbd1c590b654f74cc9c",
  "owner": "",
  "plan": "../plans/AR-1252.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Provision an approved isolated qualification runner for ASB executable evidence.",
  "task_revision": 114,
  "title": "Provision approved isolated qualification runner",
  "updated_at": "2026-09-16T13:15:04+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1252"
}
---

Implement only the linked AR-1252 plan using ASB development documentation and handoffctl.
All runner images, scripts, and caches remain under `/srv/data/projects`; preserve offline-after-install,
privacy, credential isolation, network denial, bounded execution, signatures, DCO, and exact-tree gates.

- 2026-09-16T11:04:39+00:00: AR-1251 confirmed host namespace restriction; Docker service is
  available via sudo. Promote digest-pinned isolated runner prerequisite.

- 2026-09-16T11:05:01+00:00: Claimed by asb_ar1252_isolated_runner.

- 2026-09-16T11:05:33+00:00: Recorded command exit 0; command argv SHA-256
  9a629caf66475420aed9c07df8c351e422dcf1776f37f894d6b6623e938fb0c9.

- 2026-09-16T11:06:08+00:00: Recorded command exit 1; command argv SHA-256
  c79e6d417ab6578a138bbbedff733c06012990297ed6d0d0ba852eb8fd34512e.

- 2026-09-16T11:06:24+00:00: Recorded command exit 0; command argv SHA-256
  d16d280113e9d0105b159d0bd5515aa8b6d8df8447ebaaeb47277816b58ef411.

- 2026-09-16T11:06:36+00:00: Recorded command exit 125; command argv SHA-256
  95ec1a0d737b6748cf01ee01e6c764a3a35da0785ec598ab9b3b975873dabcfe.

- 2026-09-16T11:06:47+00:00: Recorded command exit 125; command argv SHA-256
  9cb76c682135b7c1df55b4f185c0cf15debaa7e59b7ff2ba1a1a2f4fc4fed1ad.

- 2026-09-16T11:07:04+00:00: Recorded command exit 0; command argv SHA-256
  d334738d04af54e3296ee7652e656e446479bbacaa208268a7d21af2b0634f7b.

- 2026-09-16T11:07:29+00:00: Recorded command exit 0; command argv SHA-256
  4698efe4e54ccfebe5af98ff99ea6d3b57a41c3c2c6643be9f0c0fb77fee4202.

- 2026-09-16T11:08:02+00:00: Docker audit: unprivileged docker API denied; sudo -n docker available.
  Cached immutable image
  ubuntu@sha256:33ceb71981b602c1a7443a53469e4dba065f7503eab3078a2d7a57a2ab987517 verified via image
  listing. Initial wrapper probe failed exit 125 because Docker rejects --pid private; fixed by
  relying on Docker default private PID namespace. Signed+DCO commit 8014ef7 pushed. Wrapper
  positive /bin/true run now exits 0; command output is sanitized to status/exit/elapsed.

- 2026-09-16T11:08:20+00:00: Recorded command exit 0; command argv SHA-256
  065377320539a3ee25fafdf9cd8d154a4cd9cbeca95496fc25b5853eabf4db48.

- 2026-09-16T11:08:32+00:00: Recorded command exit 0; command argv SHA-256
  39059b7c1cd82b6a868a9664b24fb3304554af65573f82cb7ce48f4ad80d3937.

- 2026-09-16T11:08:55+00:00: Recorded command exit 0; command argv SHA-256
  40a5b0a64387f7d1a073e8de8d81edec7f62f2db2d5ea27f44fea553c6471243.

- 2026-09-16T11:09:08+00:00: Recorded command exit 1; command argv SHA-256
  0e7f81d31a9a97a40f77b25e4849d68b381c74b2050a170ec6f394bd5de72618.

- 2026-09-16T11:09:22+00:00: Recorded command exit 0; command argv SHA-256
  37cda48b5a7064eb7a272d920098717c9b16134b77bb06bfff0b3255eaafe15f.

- 2026-09-16T11:09:36+00:00: Recorded command exit 0; command argv SHA-256
  4698efe4e54ccfebe5af98ff99ea6d3b57a41c3c2c6643be9f0c0fb77fee4202.

- 2026-09-16T11:09:54+00:00: Recorded command exit 0; command argv SHA-256
  dac569a532375b0ecc12c01187363c25711c5158da1aa86872f15422dd70877f.

- 2026-09-16T11:10:06+00:00: Recorded command exit 0; command argv SHA-256
  39059b7c1cd82b6a868a9664b24fb3304554af65573f82cb7ce48f4ad80d3937.

- 2026-09-16T11:10:36+00:00: Runner wrapper now at signed+DCO head 1200066, pushed cleanly. Uses
  immutable ubuntu@sha256:33ceb71981b602c1a7443a53469e4dba065f7503eab3078a2d7a57a2ab987517, verifies
  docker image RepoDigest before launch, --network none, --read-only, cap-drop ALL,
  no-new-privileges, private IPC/default PID, bounded memory/CPU/PIDs, no shell command vectors, and
  only validated non-symlink artifact bind under /srv/data/projects. Positive /bin/true run passes;
  symlink and shell vectors rejected. Initial exit-125 was invalid --pid private and is fixed.
  Remaining fixture-backed network denial/timeout/no-mount evidence and integration pending.

- 2026-09-16T11:11:40+00:00: Recorded command exit 0; command argv SHA-256
  3af53959683acc2074d8240d90bc92faf55fb1dc04ac4caa2f09e21460417b2d.

- 2026-09-16T11:12:07+00:00: Recorded command exit 124; command argv SHA-256
  8393560d499bd6a91d66aeedee2ad74270192ad9033f8efae75c6ba08443a95b.

- 2026-09-16T11:12:16+00:00: Recorded command exit 0; command argv SHA-256
  2babd8e5ca6b8deda709518540df712ba9bb1aa025a15947d23cb710bb983539.

- 2026-09-16T11:12:41+00:00: Signed+DCO head 8513a90 pushed. Added test_run_isolated.py: isolation
  command flags and shell-vector rejection pass (2/2). Actual Docker timeout probe with --timeout 1
  and /bin/sleep 2 returned sanitized status timeout and exited 124. Image digest verification,
  network none, read-only root, dropped caps, private IPC/default PID, bounded resources, and single
  read-only artifact bind remain enforced. Fixture-backed network-denial and AR-1251 integration
  remain.

- 2026-09-16T11:18:30+00:00: Recorded command exit 0; command argv SHA-256
  f782820ab730d62e1c2c064eb85993943adb7f3be571d96f9d3f0873126e85ce.

- 2026-09-16T11:18:48+00:00: Recorded command exit 0; command argv SHA-256
  5c3b981d0c480355fef14ba919888fbec5f6f3587a4308faecb34e8a1f36176d.

- 2026-09-16T11:18:59+00:00: Recorded command exit 0; command argv SHA-256
  39059b7c1cd82b6a868a9664b24fb3304554af65573f82cb7ce48f4ad80d3937.

- 2026-09-16T11:19:26+00:00: Signed+DCO commits bde4bf8 and 6103976 pushed. Added fixed
  --verify-network-none probe executing /bin/cat /proc/net/route in the digest-pinned container;
  initial assertion incorrectly rejected the standard empty-route header, corrected to require
  exactly header-only output. Probe now returns network-none-verified. Existing 2/2 isolation
  contract tests and timeout 124 test remain passing. One validated read-only artifact bind is the
  sole host input; no other mounts are created. AR-1251 integration and no-mount evidence remain.

- 2026-09-16T11:20:23+00:00: Recorded command exit 0; command argv SHA-256
  7322a9e64c1dc820dea80fe57baadb27af15b4d1a1a6c03f465f6d0f2b8c3489.

- 2026-09-16T11:20:50+00:00: Recorded command exit 0; command argv SHA-256
  722f461dce024ce365bb2dccd65647616a7c269101de06d1b493b32008e0b86d.

- 2026-09-16T11:21:00+00:00: Recorded command exit 0; command argv SHA-256
  e2c69e84eb60704245c2212b61cb15373120182e122fce12ca9dc123ba647f3f.

- 2026-09-16T11:21:20+00:00: Recorded command exit 0; command argv SHA-256
  35d0cce9b7cc9477132759189b7e6e4ea153433f5e329d105d93ab4b99719d4a.

- 2026-09-16T11:21:33+00:00: Recorded command exit 0; command argv SHA-256
  3a2774183717bd33bb38bf1f5718628257cd75ac81a361b260f50173a968b2d7.

- 2026-09-16T11:21:43+00:00: Recorded command exit 0; command argv SHA-256
  39059b7c1cd82b6a868a9664b24fb3304554af65573f82cb7ce48f4ad80d3937.

- 2026-09-16T11:22:03+00:00: Signed+DCO head d72c419 pushed. Added required --artifact-sha256 and
  pre-bind digest verification, closing caller-self-consistency/TOCTOU gap for the input archive.
  Consumer README documents the sole validated read-only artifact bind and direct-vector contract.
  Network-none probe with pinned artifact digest returns network-none-verified; isolation tests 2/2
  pass; timeout probe returns 124. Descendant cleanup evidence and AR-1251 integration remain
  outstanding.

- 2026-09-16T11:22:10+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T11:26:03+00:00: Recorded command exit 0; command argv SHA-256
  65e4ad8e9b3ce5e578103acff01f0fca47517ecdf4bfd95514086aec51fd504c.

- 2026-09-16T11:26:13+00:00: Recorded command exit 1; command argv SHA-256
  785d17e05727a5109535ced6e1106fdcf6265541b6f1b06b8f59ce5d2afc34a6.

- 2026-09-16T11:26:28+00:00: Recorded command exit 0; command argv SHA-256
  f8f0fb4ea6fc2c212d49abd3443023d3ce7e2c6bdfc09917a82d10092e1fca02.

- 2026-09-16T11:26:46+00:00: Recorded command exit 0; command argv SHA-256
  e19c8db1391ce1c573bdb3d0378ad71ee591aeabcd22d2e7464b361aac7f73f6.

- 2026-09-16T11:27:01+00:00: Signed+DCO head 16e5c37 pushed. Added explicit no-mount regression:
  exactly one bind matching the validated read-only artifact and no --volume; cleanup --rm assertion
  passes. Documented AR-1251 invocation with artifact digest and network preflight. Full
  llm-double-spike Python suite passes 12/12. Network-none probe and timeout evidence remain valid;
  descendant cleanup is container-owned via --rm. Remaining: independent review, AR-1251 consumer
  wiring, full policy gates.

- 2026-09-16T11:27:17+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T11:36:22+00:00: Worker process is no longer present; preserving signed head 16e5c37 and
  all evidence. Releasing claim for safe reassignment to continue AR-1251 integration and
  independent review.

- 2026-09-16T11:36:52+00:00: Claimed by asb_ar1252_isolated_runner.

- 2026-09-16T11:37:03+00:00: Recorded command exit 127; command argv SHA-256
  0d81043765432a4e70cb5fb657ea348619f14574a9fabcd10e715ae89ca6c946.

- 2026-09-16T11:37:31+00:00: Recorded command exit 0; command argv SHA-256
  f4bfa8116ab2a8a815126497cf3a77fb0d28663ac1aa04fc979d7807d89b57b9.

- 2026-09-16T11:37:44+00:00: Recorded command exit 0; command argv SHA-256
  5254b0ae9bf4cdb435a081ca6446c9fa0f40bee8e10256aaf59f6071cf331988.

- 2026-09-16T11:37:57+00:00: Recorded command exit 0; command argv SHA-256
  39059b7c1cd82b6a868a9664b24fb3304554af65573f82cb7ce48f4ad80d3937.

- 2026-09-16T11:38:18+00:00: Signed+DCO head d7ed229 pushed. Direct consumer integration slice
  added: --verify-artifact-version executes the pinned MockAgents binary itself inside the
  digest-pinned container and verifies 0.5.0, avoiding absent/ambient host Python (Ubuntu image has
  no python3). With executable digest d62c55e4..., mode returned artifact-version-verified. Existing
  network-none, timeout, no-mount, shell rejection and cleanup contract tests remain passing. Full
  AR-1251 harness invocation and descendant-process cleanup proof remain.

- 2026-09-16T11:38:30+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T11:39:21+00:00: Recorded command exit 1; command argv SHA-256
  533068052d36f458c7d13fbd4f69c5535af004bbb86076e54039e13cebc8460b.

- 2026-09-16T11:41:45+00:00: Recorded command exit 2; command argv SHA-256
  5041e4ef75d415ee2d2125324cd52cb4d78206c0fa47526d3b3efa3908a1984d.

- 2026-09-16T11:42:02+00:00: Recorded command exit 0; command argv SHA-256
  ae064ff20abc7349f398fea6f8aa73ed2ecfde6fd0c15879e5962d2415cc42d8.

- 2026-09-16T11:42:17+00:00: Recorded command exit 1; command argv SHA-256
  b49213298622818afa17c2bb15bc781a42c4e9a5d4ca8950cc323e440ddc734b.

- 2026-09-16T11:42:43+00:00: Recorded command exit 0; command argv SHA-256
  849186f86f97af98fc07d3ae24fe2d7e9fe0e32a133be4b3cc68479aef61efe8.

- 2026-09-16T11:43:06+00:00: Recorded command exit 1; command argv SHA-256
  223779935704aa9d900cba247e8cbe44b100e05ffa6221e9de8efcba14d048d7.

- 2026-09-16T11:43:26+00:00: Recorded command exit 1; command argv SHA-256
  ffa930f171a987ee24e914a0a149b672f6f3d661d1c969a42927eba5a407b828.

- 2026-09-16T11:44:18+00:00: Recorded command exit 0; command argv SHA-256
  56eb86be92f5134bbe66ade4db7534c4a09e53281a50690fdab48e75ab8cf7f1.

- 2026-09-16T11:44:44+00:00: Recorded command exit 0; command argv SHA-256
  af010d681907e58d300a58b682d6e98f3acf885c06546a8df1ed980bd38b4c62.

- 2026-09-16T11:45:30+00:00: Recorded command exit 0; command argv SHA-256
  f795e0089112a2698a26146b18991137b5ef2ff2415aaf8e485402264735b262.

- 2026-09-16T11:46:02+00:00: Signed+DCO head 249dac1 pushed. Runner now assigns an internal per-run
  Docker name and verifies docker ps has no matching container after success or timeout, removing
  unexpected residue before rechecking. Focused contract tests pass 4/4; live network-none probe
  passes; bounded /bin/sleep timeout returns 124 and cleanup check passes. Earlier cleanup false
  result was diagnosed as an over-escaped Docker format template and corrected. AR-1251 remains
  pending real transport fixture invocation; no merge requested.

- 2026-09-16T11:46:35+00:00: Recorded command exit 0; command argv SHA-256
  b4b1e590df058031e8e5e9b40af9764a40d1bc3edfe9638181cceb5e4c9bc2fc.

- 2026-09-16T11:47:03+00:00: Recorded command exit 0; command argv SHA-256
  302920456fc719a3886aac3147c18f66b18523f0261bec1755baf173550ea302.

- 2026-09-16T11:47:25+00:00: Focused runner contract 4/4 and full llm-double-spike suite 13/13 pass.
  Source policy headers and signature/failure-path tests pass (16/16); git diff --check clean. Live
  digest-pinned Docker network-none preflight passes and bounded timeout returns 124 with
  named-container cleanup verification. Signed+DCO commit 249dac1 pushed. The runner now proves no
  matching container remains after each run, including timeout cleanup. Remaining AR-1251 transport
  fixture/real descendant behavior is not falsely claimed complete; requires AR-1251-owned fixture
  work.

- 2026-09-16T11:47:57+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T11:58:15+00:00: Recorded command exit 0; command argv SHA-256
  cad6690e76a32bd640aa452bc6f3fa2c75328705583e1ad1bedca740e1959d05.

- 2026-09-16T11:58:41+00:00: Released blocked/ownerless after independent review. Signed+DCO f0f3d67
  adds artifact digest-mismatch rejection; focused runner tests 5/5 and prior full 13/13 pass.
  Reviewer blockers remain: no actual outbound endpoint-denial proof (route-table probe is
  insufficient), no real AR-1251 transport consumer invocation, no full cancellation/backpressure
  cleanup or descendant-process evidence, and executable identity is version-only rather than
  independently pinned runtime identity. AR-1251 is the existing successor/consumer task and must
  implement the transport sandbox fixture; do not weaken gates or claim AR-1252 complete.

- 2026-09-16T12:51:09+00:00: Cached Python runtime is an immutable local digest compatible with the
  runner plan; add an explicit reviewed image allowlist without mutable tags.

- 2026-09-16T12:51:12+00:00: Claimed by asb_ar1252_isolated_runner.

- 2026-09-16T12:51:43+00:00: Recorded command exit 0; command argv SHA-256
  cc88fcf2bafcc53f3d7ceb947f39d0854240e1596cbadda9b2bd04256ae42c8a.

- 2026-09-16T12:52:01+00:00: Recorded command exit 0; command argv SHA-256
  5312b0e7cbc1fba5d8c94e5a92335b57da5c4b0731f79aeef5d12f1b272b5167.

- 2026-09-16T12:52:19+00:00: Recorded command exit 0; command argv SHA-256
  e00a9b68decf4b922bd4831bbb3b39f7fb51156600d020c0fb25002b3be655b0.

- 2026-09-16T12:52:41+00:00: Resumed after AR-1253 runtime audit. Added explicit immutable image
  allowlist for approved Ubuntu digest and cached Python digest ed86c822; mutable tags are rejected.
  Both images undergo RepoDigest verification and retain network-none, read-only,
  dropped-capability, bounded-resource, private-IPC, single read-only mount, shell rejection,
  timeout and named cleanup controls. Focused runner tests 6/6 and full llm-double-spike suite 15/15
  pass; source policy and diff checks pass. Live Python-image network-none and MockAgents
  artifact-version probes pass. Signed+DCO head d5f21ce pushed. AR-1251 can now consume the pinned
  Python image after independent review/CI.

- 2026-09-16T12:52:44+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T12:53:51+00:00: Independent exact-head review approved
  d5f21cebefbc0d532537fbdbdffc998d62e92255: complete diff adds explicit Ubuntu/Python immutable
  image allowlist with RepoDigest verification, preserves
  network-none/read-only/cap-drop/private-IPC/bounded resources/single read-only bind/shell
  rejection/named cleanup, adds artifact digest/version verification and live probes. Focused 6/6
  and full llm-double-spike 15/15 pass; source policy/diff checks pass; all commits SSH-signed+DCO.
  AR-1251 invocation remains correctly separate. No PR currently exists; publication authorized.

- 2026-09-16T12:54:03+00:00: Recorded command exit 0; command argv SHA-256
  4d4924e3fa5769f950c31020702bf2259d16238425a10ddd564a511b3815d3c1.

- 2026-09-16T12:54:14+00:00: Recorded command exit 0; command argv SHA-256
  156da97e1ffb252c0e803cfa31f17447daea50ee19eece8febee25fcafc2e33d.

- 2026-09-16T12:56:17+00:00: PR #200 platform run 35098561126 failed before runner checks:
  hosted_portability source identity is not immutable. Exact diagnosis: PR head d5f21ce has
  merge-base 128ecdd with current protected main 4e2820b; workflow BASE_COMMIT is 4e2820b, so
  source_identity correctly rejects stale ancestry. This is a branch synchronization blocker, not a
  platform/runner defect. Do not merge d5f21ce; rebase onto 4e2820b, re-sign/DCO commits, push new
  exact head and rerun CI.

- 2026-09-16T12:56:46+00:00: Recorded command exit 0; command argv SHA-256
  003c0b0bb467dc9c325a2a9ded7954aace0286b38518a7495ebeceac9d5b3693.

- 2026-09-16T12:57:07+00:00: Recorded command exit 0; command argv SHA-256
  cdf9be364b7ccf082ca18af2b0480405d49fe02297e3316ce304a6bcb750694f.

- 2026-09-16T12:57:24+00:00: Recorded command exit 0; command argv SHA-256
  db4f92a1d13e3e74221f4464c98b1f8ec96fb71473f85e96db90e1e82c2a5ba3.

- 2026-09-16T12:57:45+00:00: Rebased clean branch onto protected main 4e2820b via handoffctl. Git
  rebase preserved SSH-valid signatures on all 16 feature commits; refreshed exact head 1d0c3cd
  pushed with force-with-lease against prior d5f21ce. Full llm-double-spike suite 15/15, source
  policy headers, and diff checks pass on rebased tree. Platform source identity is now current-base
  eligible; request fresh PR checks and independent review.

- 2026-09-16T12:57:47+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T13:03:21+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T13:04:35+00:00: Recorded command exit 0; command argv SHA-256
  a5b44d7df2e4e9a6c037caf63b9381c58c2818a9c21426259a7dcba67066791a.

- 2026-09-16T13:04:52+00:00: Recorded command exit 0; command argv SHA-256
  dba6cdbbb102ea853ecaa43ea3dcb3c60b8f0ca56b2e813e536013dc321ae814.

- 2026-09-16T13:05:32+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T13:05:43+00:00: PR #200 merged via signed local integration as
  85bcd1e423a6bd7da29a29cac4dbdcf9e4822837. Exact parents 4e2820bffe93234d02ca39b59067bf4442b08f95
  and 1d0c3cd017e8d486231dabbd1c590b654f74cc9c; exact reviewed tree
  c43eef8c950dc88ac6f545bc01f9e94896d4144e; remote ref, SSH signature and DCO verified. All
  refreshed PR checks green after rebasing stale base. Post-merge runs started: 35099645723 Rust,
  35099645731 hosted portability, 35099645713 AArch64, 35099645777 formal, 35099645699 fault
  assurance, 35099645736 repository quality; headers 35099645875 green.

- 2026-09-16T13:08:07+00:00: Recorded command exit 0; command argv SHA-256
  f666e483c5a828c75e9e3b215d3b00b7684c45798aa2e15c1885be7b99093fe1.

- 2026-09-16T13:09:46+00:00: Heartbeat by asb_ar1252_isolated_runner.

- 2026-09-16T13:15:04+00:00: AR-1252 complete. PR #200 rebased exact head
  1d0c3cd017e8d486231dabbd1c590b654f74cc9c merged via signed local integration as
  85bcd1e423a6bd7da29a29cac4dbdcf9e4822837. Remote main exact, parents 4e2820b and 1d0c3cd, tree
  c43eef8c950dc88ac6f545bc01f9e94896d4144e, SSH signature and DCO verified. Initial platform failure
  was stale-base ancestry and was resolved by rebase. All PR checks and all seven post-merge
  workflows terminal SUCCESS: AArch64 35098855882, formal 35098855958, hosted 35098855888,
  repository quality 35099645736 rerun success, Rust 35098855858, fault assurance 35098855880,
  headers 35098855898. Immutable Ubuntu/Python image allowlist, RepoDigest verification,
  network-none/read-only bounded isolation, artifact digest/version checks, cleanup, live probes and
  AR-1251 separation satisfied.
