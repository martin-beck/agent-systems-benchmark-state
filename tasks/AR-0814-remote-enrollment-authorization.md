---
{
  "branch": "feature/remote-enrollment-authz",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T19:37:03+00:00",
  "depends_on": [
    "AR-0813"
  ],
  "id": "AR-0814",
  "next_action": "Repair detached AR-0814 worktree branch before running focused authz tests.",
  "observed_branch": "feature/remote-enrollment-authz",
  "observed_dirty": 2,
  "observed_head": "0a808a635d85fdc4a43b575e3711ef23b38089e3",
  "owner": "asb_ar0814_enrollment_authz",
  "plan": "../plans/AR-0814.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide the ASB protocol and CLI for explicit remote trust and least-privilege roles.",
  "task_revision": 10,
  "title": "Secure remote enrollment and authorization",
  "updated_at": "2026-09-16T17:39:23+00:00",
  "worktree_key": "agent-systems-benchmark-remote-enrollment-authz"
}
---
## AR-0814

Pair remote TUIs with runners using explicit trust and least-privilege roles.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-10T19:20:00+00:00: Removed TUI implementation from this ASB AR. The standalone asb-tui
  enrollment experience belongs to AR-0817 and consumes this protocol.

- 2026-09-16T17:24:41+00:00: AR-0813 completed with signed transport and post-merge gates; promote
  enrollment/authz implementation.

- 2026-09-16T17:24:44+00:00: Claimed by asb_ar0814_enrollment_authz.

- 2026-09-16T17:25:38+00:00: Recorded command exit 0; command argv SHA-256
  a2ed473f94ce905fc478776983cd071465a36de4319a44489aa21fa5c1167fef.

- 2026-09-16T17:37:03+00:00: Heartbeat by asb_ar0814_enrollment_authz.

- 2026-09-16T17:39:01+00:00: Implementation slice added crates/asb-control authorization contract
  and negative tests, but handoffctl run is blocked because worktree is detached while task declares
  feature/remote-enrollment-authz.

- 2026-09-16T17:39:16+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
