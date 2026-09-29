---
{
  "branch": "feature/ar-1506-runtime-platform-launcher-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-29T03:48:47+00:00",
  "depends_on": [
    "AR-1473",
    "AR-1474",
    "AR-1480",
    "AR-1484",
    "AR-1485",
    "AR-1502",
    "AR-1505"
  ],
  "id": "AR-1506",
  "next_action": "Promote after dependency verification; implement the runtime-owned platform launcher/session and wire ordinary asb-cli dispatch to an opaque authenticated source.",
  "observed_branch": "",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "ar1506-launcher-luna56",
  "plan": "../plans/AR-1506-runtime-platform-launcher-integration.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Connect the merged authenticated platform authority/bootstrap protocol to production ASB process startup and ordinary CLI dispatch.",
  "task_revision": 4,
  "title": "Runtime platform launcher integration",
  "updated_at": "2026-09-29T01:49:03+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1506-runtime-platform-launcher-integration"
}
---

AR-1503 and AR-1504 established the missing process-owner and platform-launcher gaps but
could not safely complete them before an authenticated platform bootstrap contract existed.
AR-1505 now provides that contract and is merged with full post-merge assurance. This AR
owns the narrow production integration slice that remains.

Acceptance requires:

- a runtime-owned, authenticated session/launcher that consumes only the AR-1505 bootstrap
  authority and never accepts caller/config/socket/chain/credential/policy/root/tool authority;
- ordinary `asb-cli` process startup and `run`/`sweep` dispatch to receive only an opaque,
  runtime-issued live dispatch source, with no `None,None` production fallback;
- lifecycle binding for cancellation, teardown, restart, expiry, revocation, and egress denial,
  with deterministic local/mock/replay tests for positive and every negative path;
- no live provider or external credential requirement for development or CI qualification;
- independent exact-head review, SSH-signed DCO commit, all hosted checks, protected merge,
  and terminal post-merge assurance on the exact resulting main SHA.

Non-goals: asb-tui changes, live OpenRouter/provider reachability, caller-built authority,
synthetic trust, weakening fail-closed behavior, or treating a mock fixture as first-customer
production evidence.

- 2026-09-29T03:46:10+02:00: Created as the narrow successor to the historical AR-1503/1504
  process-owner and launcher audits. AR-1505 merged at f92c2e941913129d7db50480f71e8361a0d43a0c,
  supplying the authenticated platform bootstrap contract required to implement this integration.

- 2026-09-29T01:47:30+00:00: Dependencies AR-1473, AR-1474, AR-1480, AR-1484, AR-1485, AR-1502, and
  AR-1505 verified done; begin production launcher integration.

- 2026-09-29T01:48:47+00:00: Claimed by ar1506-launcher-luna56.

- 2026-09-29T01:49:03+00:00: Recorded command exit 0; command argv SHA-256
  f5a589cdf7ff0b0c4aa322d6e6d65fbb05fd91306ad84af64030c0948de4ef59.
