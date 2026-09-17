---
{
  "branch": "repair/ar-1295-vendor-fixtures",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-17T07:11:59+00:00",
  "depends_on": [],
  "id": "AR-1295",
  "next_action": "Update stale coordinator vendor test fixtures from v0.3.5 to verified immutable v0.3.7 and rerun the complete state test suite without changing vendor or handoffctl code.",
  "observed_branch": "repair/ar-1295-vendor-fixtures",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "asb-ar1295-vendor-tests",
  "plan": "../plans/AR-1295.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Align stale coordinator vendor tests with the verified immutable v0.3.7 pin.",
  "task_revision": 9,
  "title": "Coordinator vendor v0.3.7 fixture alignment",
  "updated_at": "2026-09-17T05:13:39+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1295-vendor-fixtures"
}
---

## AR-1295

AR-1294 restored the exact v0.3.7 coordinator payload and manifest. Existing
vendor tests still encode the superseded v0.3.5 fixture. This AR owns only the
fixture/test expectation update and must not alter vendor implementation,
handoffctl, formal runner behavior, ASB product, or asb-tui.

- 2026-09-17T05:11:42+00:00: Verified immutable v0.3.7 payload is present; stale v0.3.5 fixtures are
  an independent deterministic gate defect.

- 2026-09-17T05:11:59+00:00: Claimed by asb-ar1295-vendor-tests.

- 2026-09-17T05:12:05+00:00: Recorded command exit 0; command argv SHA-256
  d86cbe2231c7a3eb40e69e7556d13b1a845c3940bec346e84ad1d3f700d9ba9c.

- 2026-09-17T05:12:20+00:00: Recorded command exit 0; command argv SHA-256
  40bc78a21c6c5e34ef380e3b19d623f398ed92864ee20f7cc2366b00757f0698.

- 2026-09-17T05:12:29+00:00: Recorded command exit 0; command argv SHA-256
  11d3f9c064e83a5d45aed5f15205e4f08eac2a902eef5ec5bcc5829abb782c3c.

- 2026-09-17T05:13:12+00:00: Recorded command exit 0; command argv SHA-256
  0101c2d4302fb0c8c6c48bb8b52430f6378254ff1cd25b94cc16e70afcd9f4ab.

- 2026-09-17T05:13:21+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-17T05:13:39+00:00: Recorded command exit 0; command argv SHA-256
  cb32aba10be4d5137422b2b1511c1ca1522efbc213c74d3a3a2fa756678f4e3c.
