---
{
  "branch": "feature/ar-1495-development-unverified-bundle-profile",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-28T14:59:54+00:00",
  "depends_on": [
    "AR-1314",
    "AR-1397",
    "AR-1491",
    "AR-1493"
  ],
  "id": "AR-1495",
  "next_action": "Promote and claim AR-1495, audit AR-1314 on protected main, and implement or repair the explicit development-only unverified bundle profile.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1332-record-replay-luna56",
  "plan": "../plans/AR-1495-development-unverified-bundle-profile.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Add an explicit development-only unverified bundle profile without weakening production or customer-release verification.",
  "task_revision": 3,
  "title": "Development-only unverified bundle profile",
  "updated_at": "2026-09-28T12:59:54+00:00",
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
