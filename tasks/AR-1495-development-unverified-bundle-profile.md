---
{
  "branch": "feature/ar-1495-development-unverified-bundle-profile",
  "checkpoint_commit": "48f082234cbb6aa8997d5dd59a2308799233bf73",
  "claim_expires": "2026-09-28T15:06:21+00:00",
  "depends_on": [
    "AR-1314",
    "AR-1397",
    "AR-1491",
    "AR-1493"
  ],
  "id": "AR-1495",
  "next_action": "Run complete workspace/docs/policy/release/clean gates, independently review exact diff, then publish exact signed+DCO head.",
  "observed_branch": "feature/ar-1495-development-unverified-bundle-profile",
  "observed_dirty": 0,
  "observed_head": "48f082234cbb6aa8997d5dd59a2308799233bf73",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1495-development-unverified-bundle-profile.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add an explicit development-only unverified bundle profile without weakening production or customer-release verification.",
  "task_revision": 24,
  "title": "Development-only unverified bundle profile",
  "updated_at": "2026-09-28T13:07:34+00:00",
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
