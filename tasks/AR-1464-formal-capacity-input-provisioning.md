---
{
  "branch": "repair/ar-1464-formal-capacity-input-provisioning",
  "checkpoint_commit": "ab485f767fbddbd8adfc27b5120f3df0a045b762",
  "claim_expires": "2026-09-26T22:32:23+00:00",
  "depends_on": [],
  "id": "AR-1464",
  "next_action": "Obtain the reviewed full-exhaustive seed whose SHA-256 is b3383756b5cd357f58d923216effea33be35b793034de321c3c9ce460ece4b28 and a safe runner-local or authorized host swap arrangement with at least 1 GiB free; rerun signed preflight, then hand inputs to AR-1308. Do not boot TLC before both pass.",
  "owner": "coordinator-ar1464-swap-recovery",
  "plan": "../plans/AR-1464.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provisioned exact signed source, reviewed Ubuntu image, 64 GiB overlay and canonical lock; signed preflight remains blocked only by exhausted host swap and unavailable exact seed digest.",
  "task_revision": 42,
  "title": "Formal capacity and signed-input provisioning repair",
  "updated_at": "2026-09-26T21:35:09+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1464-formal-capacity-input-provisioning"
}
---

This P0 repair owns only the missing infrastructure and immutable input
assembly identified by the AR-1308 preflight. It must not weaken AR-1307's
3G memory/3G swap/2-worker/2-core/8G/7200s contract, alter the formal model,
or claim qualification. All source, image, seed, lock, JDK/TLC and runner
artifacts must be digest-pinned, signed or otherwise reviewed under the
existing state policy, stored under `/srv/data/projects`, network-disabled at
execution, and privacy-safe. No ASB product or asb-tui source changes are in
scope.

- 2026-09-26T21:12:00+00:00: Created from AR-1308's terminal preflight:
  28 KiB host swap free, no reviewed Ubuntu image, ~3.5 GiB overlay instead of
  64 GiB, missing exact signed AR-1307 `ab485f767` source/tree, seed and
  canonical admission lock. No VM/TLC run was attempted.

- 2026-09-26T21:12:35+00:00: Provision exact formal inputs and disposable capacity identified by
  AR-1308 preflight.

- 2026-09-26T21:12:38+00:00: Claimed by coordinator-ar1464-formal-capacity.

- 2026-09-26T21:12:57+00:00: Heartbeat by coordinator-ar1464-formal-capacity.

- 2026-09-26T21:13:07+00:00: Recorded command exit 0; command argv SHA-256
  0ed28ab2d231d0b2bd8ef8fcc7c11bb59995fd48770e67cf2eb8a98065389117.

- 2026-09-26T21:13:26+00:00: Recorded command exit 0; command argv SHA-256
  a00daeb04eb8457c6b09b676f90fc96bb4017684b9666da4725e7e35499bd0eb.

- 2026-09-26T21:13:55+00:00: Recorded command exit 0; command argv SHA-256
  3d44ce891bef75d3f0b3972757ae869f385dedb01af176785cc5ff7240f3fd60.

- 2026-09-26T21:14:27+00:00: Recorded command exit 1; command argv SHA-256
  bb69a5e9071fd175408272dbfa67d57cac62c2168d12c8b707dae4d7e7145ce6.

- 2026-09-26T21:14:50+00:00: Recorded command exit 0; command argv SHA-256
  33efe247a4bde9723519d8b7359efa610e6ecb9d46b2885eeb9ddd9c8987975f.

- 2026-09-26T21:15:21+00:00: Recorded command exit 0; command argv SHA-256
  7f9bb8faedaf9a95b9bb54c73d552e7e205c2c405b568b22d87e6ec80d3ad26a.

- 2026-09-26T21:15:43+00:00: Recorded command exit 0; command argv SHA-256
  c4a16d26ad0679a4763593e416880695e694f9ecf9cb4414563f264d06a1ecd6.

- 2026-09-26T21:16:09+00:00: Recorded command exit 0; command argv SHA-256
  60f7d69654174c108c13adbcb29074f615dc58ec8ae54d87f5c104a3cb9741c9.

- 2026-09-26T21:16:24+00:00: Recorded command exit 0; command argv SHA-256
  2aa51383a66d6ad1b5229b2b6d9fb31a33f2ce0945fffb1b73d57e8c94da9406.

- 2026-09-26T21:16:38+00:00: Recorded command exit 0; command argv SHA-256
  669118dc240b84f3fc329b4a30399c9c855cc438ec5a9e2b02688ce0cd9e9bcd.

- 2026-09-26T21:16:54+00:00: Recorded command exit 1; command argv SHA-256
  ce42c369f0d189d31e740fe7870a183a2a0eb1a8fd293d7834aa3cf3d899b95b.

- 2026-09-26T21:17:14+00:00: Recorded command exit 0; command argv SHA-256
  5a9454aaa6303c1757c6d354a0442a5e03b8f5c9623365a3542d92a9243daa50.

- 2026-09-26T21:17:29+00:00: Recorded command exit 0; command argv SHA-256
  5215db4252c38c16d523da5e7ae230e8ffd28c222d93708a8f8f831b1d02ebe7.

- 2026-09-26T21:17:53+00:00: Recorded command exit 0; command argv SHA-256
  ba68d12db0f6ce6794f0fd974740e939e6212c97584563215163bb575f4f691b.

- 2026-09-26T21:18:16+00:00: Recorded command exit 1; command argv SHA-256
  44cfb06f5b0f6381a405c449c340ed99e0b9c83d4d3529605778b810d1479020.

- 2026-09-26T21:18:37+00:00: Recorded command exit 0; command argv SHA-256
  da8a20ba135dac14f073c2e67a9df9b45ba3bf9a7626f5a00003978cc17d10ee.

- 2026-09-26T21:19:06+00:00: Recorded command exit 0; command argv SHA-256
  cec63f9e7ac30b88671bc7a98dd54b6b7de86f124aee9e0f8bb4513ff9bc61b8.

- 2026-09-26T21:19:27+00:00: Recorded command exit 0; command argv SHA-256
  7fba61752bf5fa4e8c7bd4601593fb29551b82cd4f70a346ec72d65f9b47d730.

- 2026-09-26T21:19:54+00:00: Recorded command exit 0; command argv SHA-256
  479e91d0dd5e5bf32d2d06ae40cafcdf387c7e6806c7ec8ee658d0276597d94f.

- 2026-09-26T21:20:22+00:00: Recorded command exit 0; command argv SHA-256
  3aae7ba456cc8fee7c7739a61469ba0c9aa985468d181e72b7868a1c233f2600.

- 2026-09-26T21:20:47+00:00: Recorded command exit 0; command argv SHA-256
  9b604908d3704f6d683800641337e4c50594f39a14d0f60a5f00b1b2bdb7355f.

- 2026-09-26T21:21:14+00:00: Recorded command exit 1; command argv SHA-256
  5ec4dc67f6e4d4cc0219f22b8d6a4d7b9f852c828eb1b93c0d0daf924c71112a.

- 2026-09-26T21:21:45+00:00: Recorded command exit 0; command argv SHA-256
  03175676ed2d5f498c8f8e136e68432e263c8d3b744f32495e2b1a809b9bded8.

- 2026-09-26T21:22:04+00:00: Recorded command exit 0; command argv SHA-256
  4315fa2c0a4f74078e12ca0be050b65f0f97597bc9b1d613f5d18fd8a65896a2.

- 2026-09-26T21:22:18+00:00: Recorded command exit 0; command argv SHA-256
  55118419ebbba806e20450ddfb73fba378c10b2ac3a2bd08dbc3aa33cfd33c36.

- 2026-09-26T21:22:44+00:00: Recorded command exit 0; command argv SHA-256
  4a049b0f0dddf6229a16d03aa8bf4c976ad4198e08819c9081604f1cda08c46d.

- 2026-09-26T21:23:08+00:00: Recorded command exit 0; command argv SHA-256
  6dc5255f83280104af0a8edd0a6cd31313d08e2983ac57c651a22dbf01f95312.

- 2026-09-26T21:23:29+00:00: Recorded command exit 0; command argv SHA-256
  c07e8ab2e74f1a84d09f20e50e316c8024836d8dc42a39b8430c7f3f56a5e533.

- 2026-09-26T21:23:43+00:00: Recorded command exit 0; command argv SHA-256
  d5c5f9c96e03a912fd140c4fda18b7e54847c9c5a87cd0e2159034bb97239be3.

- 2026-09-26T21:24:22+00:00: Bounded provisioning/audit completed without QEMU/TLC execution. Exact
  AR-1307 source `/srv/data/projects/ar1308-ar1307-source` is ab485f767 with valid SSH signature and
  matching DCO; source/tree preflight passes. Reviewed Ubuntu image copied from
  `/srv/data/projects/asb-replay-vm/noble-server-cloudimg-amd64.img` and verified SHA-256
  612b2c0cc1bc413a6cb8c38fd611794caf0f2b436c50013d8b3794db12ad7354. Created
  `/srv/data/projects/asb-state-tlc-vm-ar1308-clean-v1/root-overlay-64g.qcow2` with 64 GiB virtual
  size and the verified image as qcow2 backing. Existing JDK 17, TLC digest
  936a262061c914694dfd669a543be24573c45d5aa0ff20a8b96b23d01e050e88, model digest and canonical
  `/srv/data/projects/.asb-tlc/admission.lock` pass preflight. Final signed preflight exit 1 reports
  only host available swap below 1 GiB and seed missing/wrong digest. All active swap devices are
  fully consumed (about 28 KiB free); available historical/user-data fixtures hash 66acede7... and
  generated current full-exhaustive seed hashes 7e1128a..., neither matches required receipt digest
  b3383756b5cd357f58d923216effea33be35b793034de321c3c9ce460ece4b28. No synthetic seed, unsigned
  input, swap mutation, QEMU boot or TLC run was attempted; exact 3G/3G/2-worker/2-core/8G/7200s
  contract preserved.

- 2026-09-26T21:24:35+00:00: Blocked after bounded provisioning. Exact signed source ab485f767,
  reviewed image SHA-256 612b2c0c..., 64 GiB overlay, JDK/TLC/model and canonical owner-private lock
  are provisioned and cross-validated. Signed preflight still fails only because host swap free is
  ~28 KiB (<1 GiB) and required full-exhaustive seed SHA-256
  b3383756b5cd357f58d923216effea33be35b793034de321c3c9ce460ece4b28 is unavailable; existing fixtures
  do not match. No synthetic seed, swap mutation, QEMU boot or TLC run. Next action: obtain exact
  seed and safe swap capacity, rerun preflight, then hand off to AR-1308.

- 2026-09-26T21:32:21+00:00: Coordinator resumed bounded swap-recovery audit; only AR-specific stale
  swap files may be reclaimed after ownership and process checks, and exact seed remains
  fail-closed.

- 2026-09-26T21:32:23+00:00: Claimed by coordinator-ar1464-swap-recovery.

- 2026-09-26T21:33:04+00:00: Recorded command exit 0; command argv SHA-256
  49e1488a8d0106553b6e684b354192d7d1e2e3dd0a43259d74860112003123c8.

- 2026-09-26T21:33:43+00:00: Recorded command exit 0; command argv SHA-256
  a580be556cfeff3989d412024e6e1764e7b110367baf3cbcce4f69fe73529eea.

- 2026-09-26T21:34:28+00:00: Recorded command exit 0; command argv SHA-256
  3e3392fe84e6bbdce6e53f005d2af6901009e5ca916c3d9266df8990764025af.

- 2026-09-26T21:34:55+00:00: Recorded command exit 0; command argv SHA-256
  0ebe481f443cf8fd02eae44636b8a3323b561081036b6a65c444ac409ff204d3.

- 2026-09-26T21:35:09+00:00: Recorded command exit 0; command argv SHA-256
  82d2c0889436abc8b7bf3dd1d134bf1364cf3717076622940eb78d17b6abb47e.
