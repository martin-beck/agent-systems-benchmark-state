---
{
  "branch": "feature/ar-1229-auth-application-integration",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-15T23:45:37+00:00",
  "depends_on": [
    "AR-1228",
    "AR-1230"
  ],
  "id": "AR-1229",
  "next_action": "Promote after AR-1228 and AR-1230 are complete; implement durable config registry and authenticated CLI/control enrollment integration, then requalify AR-1120.",
  "observed_branch": "feature/ar-1229-auth-application-integration",
  "observed_dirty": 0,
  "observed_head": "05a937473f17529d1373f2f55cd5fa96f0114920",
  "owner": "asb_ar1229_auth_application",
  "plan": "../plans/AR-1229.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Integrate provider authentication into ASB config, control and CLI surfaces.",
  "task_revision": 16,
  "title": "Provider authentication application integration",
  "updated_at": "2026-09-15T21:45:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1229-auth-application-integration"
}
---

Own the cross-crate application integration split from AR-1228. Do not add credential values to
public state or weaken the existing resolver and authenticated-control boundaries.

- 2026-09-15T18:20:00+00:00: Created after AR-1228 implementation review identified that durable
  config/registry and authenticated CLI/control enrollment are a separate cross-crate contract.

- 2026-09-15T21:38:42+00:00: Dependencies AR-1228 and AR-1230 complete; AR-1228 merged at
  efe741a75a8a3e7bd14afd8c6cef119f46a21c74 with all required checks green.

- 2026-09-15T21:38:45+00:00: Claimed by asb_ar1229_auth_application.

- 2026-09-15T21:39:19+00:00: Heartbeat by asb_ar1229_auth_application.

- 2026-09-15T21:41:05+00:00: Heartbeat by asb_ar1229_auth_application.

- 2026-09-15T21:42:31+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T21:42:44+00:00: Recorded command exit 101; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-15T21:43:34+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-09-15T21:43:44+00:00: Recorded command exit 0; command argv SHA-256
  31a05f46a65b4172cfcc5ef4e1ed2b4ddd54c042ac56eff6dc51f4205a4051b1.

- 2026-09-15T21:43:53+00:00: Recorded command exit 0; command argv SHA-256
  36526a6e9ff3db476eb511221f8972449d92d2caa68260e3e97de3b8a6725047.

- 2026-09-15T21:44:02+00:00: Recorded command exit 0; command argv SHA-256
  1eadb9598d619901e8517867d52259abd2a268e158b1773b0f6ce878261d82e1.

- 2026-09-15T21:44:13+00:00: Recorded command exit 0; command argv SHA-256
  a0c2360b730c03657315f98732a490198a2b31e0fa7a67d72a11960872659141.

- 2026-09-15T21:45:37+00:00: Heartbeat by asb_ar1229_auth_application.
