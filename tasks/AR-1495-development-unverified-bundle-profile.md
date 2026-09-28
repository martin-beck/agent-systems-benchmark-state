---
{
  "branch": "feature/ar-1495-development-unverified-bundle-profile",
  "checkpoint_commit": "3b0bf6a4525c3d1382639761dc9d3a31c833906b",
  "claim_expires": "2026-09-28T15:15:31+00:00",
  "depends_on": [
    "AR-1314",
    "AR-1397",
    "AR-1491",
    "AR-1493"
  ],
  "id": "AR-1495",
  "next_action": "Monitor PR #373 fresh exact signed+DCO head 3b0bf6a and merge only after every required check and independent review is green.",
  "observed_branch": "feature/ar-1495-development-unverified-bundle-profile",
  "observed_dirty": 0,
  "observed_head": "4d63a6642c60bb203d5646a732d46b17c823a6d9",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1495-development-unverified-bundle-profile.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add an explicit development-only unverified bundle profile without weakening production or customer-release verification.",
  "task_revision": 57,
  "title": "Development-only unverified bundle profile",
  "updated_at": "2026-09-28T13:17:04+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1495-development-unverified-bundle-profile"
}
---

ASB development and local qualification are currently blocked by the absence of
external customer-release signing authority. Add a loudly labeled,
explicitly-selected `unsigned-development` bundle profile for credential-free
development and qualification only. This profile may accept a missing or
arbitrary detached signature, but its selection and resulting unverified
status must be visible in the bundle metadata and evidence.

The normal/default verifier and every production/customer-release path remain
signature-required and fail-closed. The development profile must never be
silently selected, inferred from a missing signature, or accepted as release
evidence. No asb-tui changes, provider access, credentials, network, generated
authority, or customer-release claims are in scope.

Record the AR-1314 audit and preserve any existing dirty user changes in the
canonical checkout; implementation belongs in the isolated worktree named
above.

- 2026-09-28: Created as the narrow successor for development-only
  qualification; AR-1490 remains the sole external signed-customer-release
  blocker.

- 2026-09-28T12:59:44+00:00: AR-1314 audit and explicit development-only unverified profile scope
  verified; AR-1490 remains external signed-release blocker

- 2026-09-28T12:59:54+00:00: Claimed by ar1332-record-replay-luna56.

- 2026-09-28T12:59:58+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-28T13:00:08+00:00: Recorded command exit 0; command argv SHA-256
  ff95da50359e977c1260ed1fd7a45ac1ea24b59127cbb6ea82680692bc9893bc.

- 2026-09-28T13:01:23+00:00: Recorded command exit 1; command argv SHA-256
  6cc8a648a3d5a6f772afa883ed5723ac007aa250b3606ee88ab5ae9863713c6f.

- 2026-09-28T13:01:43+00:00: Recorded command exit 101; command argv SHA-256
  7c21fd0f5b69294997cc892eb9800e84da4eea485c930220ea35533382758522.

- 2026-09-28T13:02:16+00:00: Recorded command exit 101; command argv SHA-256
  d2f9fe5cdfb13ee535561975a04af08ff01eb000a2e212df8b888e0f319b7d13.

- 2026-09-28T13:02:53+00:00: Recorded command exit 0; command argv SHA-256
  d2f9fe5cdfb13ee535561975a04af08ff01eb000a2e212df8b888e0f319b7d13.

- 2026-09-28T13:03:29+00:00: Recorded command exit 0; command argv SHA-256
  815afacc33bd93b435a9602a9685eb0973d91987c992afceed437b54676d032f.

- 2026-09-28T13:03:51+00:00: Recorded command exit 0; command argv SHA-256
  6174c135504165a74367603c7d76bafc780ca768baa56340cad0c853adec5541.

- 2026-09-28T13:03:55+00:00: Recorded command exit 0; command argv SHA-256
  6174c135504165a74367603c7d76bafc780ca768baa56340cad0c853adec5541.

- 2026-09-28T13:04:14+00:00: Recorded command exit 0; command argv SHA-256
  eacb430fcfa6df482bd1107b2428f64814f17a8cc642a0b97ec2a26da0d1529e.

- 2026-09-28T13:04:33+00:00: Recorded command exit 0; command argv SHA-256
  6d641cca764ff5d024d4d69a45e2a4983caedea4aadfdc5d831babec598fcc76.

- 2026-09-28T13:04:53+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-28T13:05:00+00:00: Recorded command exit 1; command argv SHA-256
  6d641cca764ff5d024d4d69a45e2a4983caedea4aadfdc5d831babec598fcc76.

- 2026-09-28T13:05:25+00:00: Signed+DCO product commit 48f082234cbb6aa8997d5dd59a2308799233bf73
  created after one shared coordinator LOCK_TIMEOUT retry. Focused profile tests 6/6 and complete
  asb-bundle offline_verifier 24/24 pass. The first new test run failed because exact inventory did
  not account for the tolerated development signature file; fixed expected_inventory to include it
  only for AllowUnsignedDevelopment, while default and unsigned-release remain strict. Canonical
  dirty user changes remain untouched; isolated worktree clean.

- 2026-09-28T13:05:56+00:00: Recorded command exit 0; command argv SHA-256
  be0b78e482ea004600dc60974e3eb629fe19aba615d56ddf85fc3ed7d777457c.

- 2026-09-28T13:06:21+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-28T13:07:14+00:00: Recorded command exit 0; command argv SHA-256
  78041b3e7e13276795cd5715bb05c8a7632d9913e4b86fb941ae87d0c4cdd4ee.

- 2026-09-28T13:07:34+00:00: Recorded command exit 0; command argv SHA-256
  dd53397ef679e79a9a43b59b26e691941a7da9ac972eeab77a63f727c06cdadb.

- 2026-09-28T13:08:00+00:00: Recorded command exit 0; command argv SHA-256
  90ff8ad249f0e08e9433813009c3e2414af85c42cd08d0893c76225bb857f786.

- 2026-09-28T13:08:24+00:00: Recorded command exit 0; command argv SHA-256
  fd457d954692c33148b755c3379deb79ca7b6b95d08af9ee1ce2f51887efb6ba.

- 2026-09-28T13:08:45+00:00: Recorded command exit 1; command argv SHA-256
  1d45851878ad98871965341b720aa2f000367eb9d1af341a2ed3360d71f4cbd7.

- 2026-09-28T13:09:05+00:00: Recorded command exit 0; command argv SHA-256
  52f5fe387de5769a89935d6f4a8f5cf19aff6e220484e3171876440363558ddd.

- 2026-09-28T13:09:32+00:00: Recorded command exit 0; command argv SHA-256
  006b9ec3f496009fc7ba9fce3f31ccaca88e1915fdcc9e5095c1b1d49cc2b8a5.

- 2026-09-28T13:10:02+00:00: Recorded command exit 0; command argv SHA-256
  83f1dc53e6472fa8ad1f9faeb0bb4c993a71da43677040aea65ddc501c2ccc4b.

- 2026-09-28T13:10:22+00:00: Recorded command exit 0; command argv SHA-256
  d7909284cbcd3230252c5fce9f3b1c35e1b6d2c31701cd0c54e49b00e87125ab.

- 2026-09-28T13:10:52+00:00: Independent diff review: four implementation/documentation files plus
  runtime-bundle schema description; only asb-bundle verifier/test/docs/schema changed, no
  asb-tui/provider/customer-release path. Explicit AllowUnsignedDevelopment is the sole policy that
  tolerates a bounded arbitrary signature file; default and unsigned-release negatives remain
  strict. Added schema boundary text and signed/DCO follow-up commit a714861. Full workspace cargo
  test, clippy, rustdoc, bundle tests 5/5, policy and DCO gates passed; one repository-policy
  polling LOCK_TIMEOUT was retried successfully.

- 2026-09-28T13:11:05+00:00: Recorded command exit 0; command argv SHA-256
  a40f1df5011d9a6563ea0b924e5b8cb13a53746710b2148292e3ea9446d67480.

- 2026-09-28T13:11:27+00:00: Recorded command exit 0; command argv SHA-256
  dcfb6bcf7d83c4e214be8694fd403fe17b5bb99047f9b03e1f4be782aac26018.

- 2026-09-28T13:11:47+00:00: Published exact SSH-signed+DCO head
  a714861edd489ad678f635b6aa3ad5834edb40f3 as PR #373:
  https://github.com/martin-beck/agent-systems-benchmark/pull/373. Scope is ASB asb-bundle
  verifier/tests/docs/schema only. AR-1490 remains blocked on external authorized signed customer
  package; no customer-release evidence is claimed.

- 2026-09-28T13:11:57+00:00: Recorded command exit 0; command argv SHA-256
  a9e8bf41eb80d6d983f7202ff3acabcb4913b90756bccac409c397d928c691e7.

- 2026-09-28T13:12:21+00:00: Recorded command exit 0; command argv SHA-256
  eb2a749c629375169d8c769954f631def2abb41aa518cd48b268c7928971a37d.

- 2026-09-28T13:12:42+00:00: Recorded command exit 0; command argv SHA-256
  fceda6b77c52c0e30dcfe3a72c36af1c971859c8dcd7cd0e8d8d7a89f955a60a.

- 2026-09-28T13:13:05+00:00: Recorded command exit 0; command argv SHA-256
  6747812c83c116313c61639bea9798b8af511cdb04d72ac724b207c8cf9629fd.

- 2026-09-28T13:13:27+00:00: Recorded command exit 0; command argv SHA-256
  720d731c5d457ef78d7c0a398f1e43164faf0a897457cc757ee951160731c7ed.

- 2026-09-28T13:13:46+00:00: CI Repository Quality failure 36426846077 was classified as stale-base
  policy: PR head a714861 was based on e1be259 while protected base had advanced; no product
  failure. Fetched origin/main e1be259 and created signed non-squash synchronization merge
  1f5b0f9e3c3782e1f202aa700f6515eb8e51417f, preserving the reviewed profile tree, then
  force-with-lease updated PR #373. Prior failure and one observed handoff lock timeout are
  preserved.

- 2026-09-28T13:13:57+00:00: Recorded command exit 0; command argv SHA-256
  cb50046674eb2c1d3ea08f00711676986af43541c56734ab4055a7fa2ce063c5.

- 2026-09-28T13:14:21+00:00: Recorded command exit 0; command argv SHA-256
  e1a1b8f701d77d228d3fc3217cb97d017b2ebe4df890f51c056271bfcdd0f5cb.

- 2026-09-28T13:14:40+00:00: Recorded command exit 0; command argv SHA-256
  8b482c2ca4b0775c2ac3bd4ad2a32c2436bebec13907ac896b28a2875661ee83.

- 2026-09-28T13:15:01+00:00: Recorded command exit 0; command argv SHA-256
  720d731c5d457ef78d7c0a398f1e43164faf0a897457cc757ee951160731c7ed.

- 2026-09-28T13:15:21+00:00: Second CI failure 36427086854 was classified precisely: synchronization
  merge 1f5b0f9 had two parents but lacked Signed-off-by. Amended the merge with SSH signature and
  matching DCO trailer, preserving parents (a714861 and e1be259) and reviewed tree; new exact head
  3b0bf6a4525c3d1382639761dc9d3a31c833906b force-with-lease pushed to PR #373. Prior stale-base and
  missing-DCO failures remain recorded; no product semantics changed.

- 2026-09-28T13:15:31+00:00: Heartbeat by ar1332-record-replay-luna56.

- 2026-09-28T13:15:41+00:00: Recorded command exit 0; command argv SHA-256
  cb50046674eb2c1d3ea08f00711676986af43541c56734ab4055a7fa2ce063c5.

- 2026-09-28T13:16:06+00:00: Recorded command exit 0; command argv SHA-256
  db28570ce228bd34303a8c42808571571849fdf6a8e4f02585ea85b2b0f2d282.

- 2026-09-28T13:16:29+00:00: Recorded command exit 0; command argv SHA-256
  83f1dc53e6472fa8ad1f9faeb0bb4c993a71da43677040aea65ddc501c2ccc4b.

- 2026-09-28T13:16:48+00:00: Recorded command exit 0; command argv SHA-256
  b4ae1ff55075dff859752999b5332fc462458d9f73f574682c1cdb5012e3b356.
