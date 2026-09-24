---
{
  "branch": "codex/ar-1431-stale-base",
  "checkpoint_commit": "bd694233fd95941bfc02cdd4e7f0fd3b124d0f4e",
  "claim_expires": "2026-09-25T00:25:29+00:00",
  "depends_on": [
    "AR-1427"
  ],
  "id": "AR-1431",
  "next_action": "Open repair PR from bd69423; obtain independent review and exact-head CI, then verify all seven post-merge workflows before AR-1216 release.",
  "observed_branch": "codex/ar-1431-stale-base",
  "observed_dirty": 0,
  "observed_head": "bd694233fd95941bfc02cdd4e7f0fd3b124d0f4e",
  "owner": "ar1431-stale-base-luna56",
  "plan": "../plans/AR-1431-protected-main-stale-base-repair.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Prevent stale-base sequential merges from passing review but failing protected-main merge-tree policy.",
  "task_revision": 19,
  "title": "Protected-main stale-base merge requalification repair",
  "updated_at": "2026-09-24T22:25:47+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1431"
}
---

Failure evidence is immutable: AR-1216 post-merge Repository Quality run
`36066329347` rejected merge `e82e2e6` because the protected target advanced from
review base `d9eb6c2` to `8d1889b` before publication.  This AR must preserve
that incident and must not waive the policy.

- 2026-09-24T22:16:46+00:00: AR-1427 is done; promote repair for AR-1216 protected-main stale-base
  merge-tree failure 36066329347.

- 2026-09-24T22:19:23+00:00: Claimed by ar1431-stale-base-luna56.

- 2026-09-24T22:22:12+00:00: Recorded command exit 0; command argv SHA-256
  aae66aab4fdf8f873e2ba3b94e322d63ce9d5491cf6dfef4475319458372bc01.

- 2026-09-24T22:22:26+00:00: Recorded command exit 0; command argv SHA-256
  e068eb8b14408e12418fa448e734a204f65427e486bbbb0aba93576c5f8c4f26.

- 2026-09-24T22:23:34+00:00: Recorded command exit 1; command argv SHA-256
  05164c9e42c6b112328298c1fd514ca9fd2e95fc55acf75a098368f1d6f7624b.

- 2026-09-24T22:23:57+00:00: Recorded command exit 0; command argv SHA-256
  05164c9e42c6b112328298c1fd514ca9fd2e95fc55acf75a098368f1d6f7624b.

- 2026-09-24T22:24:11+00:00: Recorded command exit 1; command argv SHA-256
  053a953a8533985d69cd596872ffe27fefa3f9ca58ceae1901a1cd4627604564.

- 2026-09-24T22:24:26+00:00: Recorded command exit 0; command argv SHA-256
  0c632280b62808e521b049b72a175972d9c44cd13a421f68a729152d7c7d42fc.

- 2026-09-24T22:24:40+00:00: Recorded command exit 128; command argv SHA-256
  0c632280b62808e521b049b72a175972d9c44cd13a421f68a729152d7c7d42fc.

- 2026-09-24T22:24:54+00:00: Recorded command exit 0; command argv SHA-256
  6cd64a7028d09e958c1399b2f1bfd6b4e50ab23d317020c202adb4303b17e108.

- 2026-09-24T22:25:08+00:00: Recorded command exit 0; command argv SHA-256
  d04aa803a9fcb854b247572f9b417fd1935a57ca978bb887d2e7c188e99db043.

- 2026-09-24T22:25:29+00:00: Heartbeat by ar1431-stale-base-luna56.

- 2026-09-24T22:25:38+00:00: Reproduced immutable incident e82e2e6: protected-main policy now
  reports exact base/topic/merge and reviewed-vs-merge trees. Added deterministic merge-tree preview
  binding and bounded identity diagnostics; focused 31-test suite passed. Signed+DCO product commit
  bd69423.

- 2026-09-24T22:25:47+00:00: Recorded command exit 0; command argv SHA-256
  e47406bbe0009f768d573698a7ada7f7fcafa22c51e99ddb8503152b2f1a69b6.
