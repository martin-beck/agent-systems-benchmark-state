---
{
  "branch": "repair/ar-1292-tla-provenance",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1292",
  "next_action": "Await signed or attested immutable TLA+ v1.8.0 provenance, or deterministic source-build qualification for 142d0ba; do not update hash only.",
  "observed_branch": "repair/ar-1292-tla-provenance",
  "observed_dirty": 0,
  "observed_head": "c1b1860786e844adb69b8f74e39af290592a89c8",
  "owner": "",
  "plan": "../plans/AR-1292.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Repair or formally retain the pinned TLA+ artifact provenance mismatch blocking formal assurance.",
  "task_revision": 16,
  "title": "Pinned TLA+ artifact provenance repair",
  "updated_at": "2026-09-18T21:10:23+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1292-tla-provenance"
}
---

## AR-1292

PR #119 / AR-0704 is blocked before model execution because the downloaded
official TLA+ v1.8.0 asset has the expected size but does not match the pinned
SHA-256. This AR owns only evidence-led provenance repair or confirmation that
the external release remains unverifiable. It must not weaken or bypass formal
verification, alter native-capacity behavior, or touch asb-tui.

- 2026-09-17T04:34:39+00:00: Dependencies are external-provenance scoped; promote independent audit
  without weakening AR-0704 formal gate.

- 2026-09-17T04:35:18+00:00: Claimed by asb_ar1292_tla_provenance.

- 2026-09-17T04:36:32+00:00: Heartbeat by asb_ar1292_tla_provenance.

- 2026-09-17T04:36:35+00:00: Recorded command exit 0; command argv SHA-256
  146cc60c9b79021ba3ecc84c5e1163b9db4328738be7e71ebdf4f275ec94bb8e.

- 2026-09-17T04:37:37+00:00: Recorded command exit 0; command argv SHA-256
  770e0083dc32f22b0ecb13f98a20aa485bf3558c5eae2ef406000553f522d11e.

- 2026-09-17T04:38:08+00:00: Recorded command exit 0; command argv SHA-256
  d7ea8da35895297f9eebdcf26d7bd88efec48b1765744a58fc7ae71666de9147.

- 2026-09-17T04:38:23+00:00: Recorded command exit 12; command argv SHA-256
  0d990a752b2bea5a9dfd4b0f1363731b1e96873b1f4434a8765b6599015704ca.

- 2026-09-17T04:39:13+00:00: Heartbeat by asb_ar1292_tla_provenance.

- 2026-09-17T04:39:47+00:00: Provenance audit complete. GitHub release API reports v1.8.0 as a
  mutable prerelease published 2026-09-17T03:26:45Z; tla2tools.jar asset ID 569359548 was uploaded
  2026-09-17T03:25:15Z, size 4492966, API digest
  sha256:9d36716ffb5e49d1ba8fae4651eba59f3189887e12eb90e204a42d2e6e993fef. Independent download
  matched exactly and its manifest reports X-Git-Revision 142d0ba85e54a937c0fc5e1503941bd4cf46b684,
  matching the v1.8.0 tag commit; positive Recovery.tla TLC completed with 3709 distinct
  states/depth 17 and the deliberate stale mutation rejected with StaleEventsFenced. However the
  previous pinned asset ID 551753628 now returns 404, and the repository pin expected 4490679
  bytes/SHA a1fc0bfe...; the cached old artifact manifest reports revision 65fbace, while the
  repository source pin b123b226 is already 20 commits behind it and 54 commits behind current
  142d0ba. The current release tag is unsigned and mutable prerelease; no signed tag or artifact
  attestation binding source to binary was found. Updating only hash/size would accept a different
  source build and weaken provenance. Retain fail-closed; no product mutation, no asb-tui change, no
  PR #119 requalification.

- 2026-09-17T04:39:56+00:00: Blocked and released ownerless after independent provenance audit.
  Current v1.8.0 asset 569359548/API SHA 9d36716f/4492966 bytes and manifest revision 142d0ba
  execute the positive and deliberate-negative TLC model checks, but the mutable unsigned prerelease
  has no source-to-binary signature/attestation; old asset 551753628 is gone and prior
  source/artifact pins are inconsistent. Require signed/attested immutable provenance or
  deterministic current-source rebuild before any hash update or PR #119 requalification.

- 2026-09-18T21:09:56+00:00: Bounded provenance re-audit authorized; verify live v1.8.0 release, tag
  signature, artifact attestation, and source binding without changing the pinned fixture.

- 2026-09-18T21:09:59+00:00: Claimed by asb-ar1292-provenance-reaudit-20260918.

- 2026-09-18T21:10:16+00:00: Refreshed 2026-09-18 official GitHub evidence: release 25926686 remains
  draft=false/prerelease=true, published 2026-09-17T03:26:45Z; tla2tools.jar asset 569359548 is size
  4492966 with API SHA-256 9d36716ffb5e49d1ba8fae4651eba59f3189887e12eb90e204a42d2e6e993fef.
  Independent download matches those bytes and manifest X-Git-Revision
  142d0ba85e54a937c0fc5e1503941bd4cf46b684, matching lightweight refs/tags/v1.8.0. The tag has no
  annotated tag object, commit verification is null, and release assets/body expose no
  source-to-binary signature or attestation (body has only SHA-1 checksums). Prior asset 551753628
  remains unavailable and repository pin remains 4490679 bytes/SHA a1fc0bfe...; replacing hash/size
  would weaken fail-closed provenance. No product/asb-tui mutation and no PR #119 rerun.

- 2026-09-18T21:10:23+00:00: Refreshed audit confirms blocker unchanged: v1.8.0 is mutable
  prerelease with unsigned lightweight tag/unsigned commit and no source-to-binary attestation;
  current asset digest/manifest binding alone is insufficient. Released ownerless; require signed or
  attested immutable provenance or deterministic 142d0ba source build before any fixture update or
  PR #119 requalification.
