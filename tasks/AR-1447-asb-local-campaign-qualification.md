---
{
  "branch": "qualification/ar-1447-asb-local-campaign",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1433",
    "AR-1437",
    "AR-1442"
  ],
  "id": "AR-1447",
  "next_action": "Remain planned until local mock AR-1433, recording/replay AR-1437, and ASB setup AR-1442 are released; then qualify the existing bounded easy run/sweep and offline local campaign journey. The broader AR-1338 interactive wrapper remains a separate enhancement.",
  "observed_branch": "qualification/ar-1447-asb-local-campaign",
  "observed_dirty": 0,
  "observed_head": "2872a31f2ee90ac5df1a47203b2a618b1829cfec",
  "owner": "",
  "plan": "../plans/AR-1447.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Qualify the complete credential-free ASB local campaign and replay journey.",
  "task_revision": 11,
  "title": "ASB local campaign qualification",
  "updated_at": "2026-09-25T15:31:12+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1447"
}
---

This is the ASB-only local campaign gate. It intentionally does not replace or
close the optional live capture chain AR-1330 through AR-1333.

- 2026-09-25T15:40:00+00:00: Created to separate first-customer credential-free
  qualification from optional live-provider capture dependencies.

- 2026-09-25T15:27:13+00:00: Local ASB campaign qualification is dependency-ready: AR-1433, AR-1437
  and ASB CLI setup AR-1442 are released. Optional live capture and broad wrapper remain separate.

- 2026-09-25T15:27:16+00:00: Claimed by coordinator-ar1447.

- 2026-09-25T15:27:34+00:00: Recorded command exit 0; command argv SHA-256
  b90815e56704d6579354b40d8bbf8af9f68ad57bc438b40ba42c594845b7247d.

- 2026-09-25T15:28:39+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-09-25T15:30:19+00:00: Recorded command exit 0; command argv SHA-256
  c3f9678d3206e0fbf13f2d34754ef97ba70edb240f3eb5508653b98109335725.

- 2026-09-25T15:30:35+00:00: Recorded command exit 0; command argv SHA-256
  81be0cf2ddf0130bfc32dab388241304e226bdf3836fc3a90feecc2af2ad151b.

- 2026-09-25T15:30:54+00:00: Recorded command exit 0; command argv SHA-256
  3d4cc54827fa0ae5c402321266e4a8e9a84a69a17f7ff27b7a0f0c858d454784.

- 2026-09-25T15:31:12+00:00: ASB-only local campaign qualification complete on protected merge
  2872a31f2ee90ac5df1a47203b2a618b1829cfec. Targeted guided-local and exact-campaign tests passed;
  full cargo test --locked -p asb-cli --lib passed 107/107. Qualification is credential-free,
  local-mock, offline replay capable, and does not depend on live-provider reachability.
