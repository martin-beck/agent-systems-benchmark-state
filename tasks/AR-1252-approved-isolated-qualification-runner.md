---
{
  "branch": "feature/ar-1252-approved-isolated-runner",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T13:22:10+00:00",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-1252",
  "next_action": "Independent review runner contract; then integrate AR-1251 consumer and run full policy gates.",
  "observed_branch": "feature/ar-1252-approved-isolated-runner",
  "observed_dirty": 0,
  "observed_head": "16e5c3762eb4eb49c2c2b24e8c32f0d8bd380aea",
  "owner": "asb_ar1252_isolated_runner",
  "plan": "../plans/AR-1252.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provision an approved isolated qualification runner for ASB executable evidence.",
  "task_revision": 57,
  "title": "Provision approved isolated qualification runner",
  "updated_at": "2026-09-16T11:27:01+00:00",
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
