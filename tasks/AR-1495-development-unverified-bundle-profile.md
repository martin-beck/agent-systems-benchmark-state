---
{
  "branch": "feature/ar-1495-development-unverified-bundle-profile",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-28T14:59:58+00:00",
  "depends_on": [
    "AR-1314",
    "AR-1397",
    "AR-1491",
    "AR-1493"
  ],
  "id": "AR-1495",
  "next_action": "Promote and claim AR-1495, audit AR-1314 on protected main, and implement or repair the explicit development-only unverified bundle profile.",
  "observed_branch": "feature/ar-1495-development-unverified-bundle-profile",
  "observed_dirty": 4,
  "observed_head": "a2d9be3eb3c77331a7a3498fdec8e54fb74ae8d6",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1495-development-unverified-bundle-profile.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add an explicit development-only unverified bundle profile without weakening production or customer-release verification.",
  "task_revision": 9,
  "title": "Development-only unverified bundle profile",
  "updated_at": "2026-09-28T13:01:43+00:00",
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
