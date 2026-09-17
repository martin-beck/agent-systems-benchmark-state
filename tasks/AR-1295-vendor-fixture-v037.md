---
{
  "branch": "repair/ar-1295-vendor-fixtures",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1295",
  "next_action": "Update stale coordinator vendor test fixtures from v0.3.5 to verified immutable v0.3.7 and rerun the complete state test suite without changing vendor or handoffctl code.",
  "observed_branch": "repair/ar-1295-vendor-fixtures",
  "observed_dirty": 0,
  "observed_head": "",
  "owner": "",
  "plan": "../plans/AR-1295.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "blocked",
  "summary": "Align stale coordinator vendor tests with the verified immutable v0.3.7 pin.",
  "task_revision": 19,
  "title": "Coordinator vendor v0.3.7 fixture alignment",
  "updated_at": "2026-09-17T05:17:05+00:00",
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

- 2026-09-17T05:13:48+00:00: Recorded command exit 0; command argv SHA-256
  5fee026f8e9a7f506fee8acb40e6d7ba17ca1871cd06c4470eab260e3070f672.

- 2026-09-17T05:13:57+00:00: Recorded command exit 0; command argv SHA-256
  57aa684661b9badaf5caf256706c0ff03f2aa97681862aa8ba378effbed4e08c.

- 2026-09-17T05:14:06+00:00: Recorded command exit 2; command argv SHA-256
  b39a86595fdff2d53bb611c0b0ba124d1b7628a3cd61c31f0af8283fc7e6cce7.

- 2026-09-17T05:14:47+00:00: Recorded command exit 2; command argv SHA-256
  b25e4f8b368b5a27aba7cf0e474d9f348cc923b0b2d183faf08df6c155175434.

- 2026-09-17T05:15:16+00:00: Recorded command exit 2; command argv SHA-256
  813de908ce043ab99009827e211d9d020304e713c6a563d19a5133d64e53af62.

- 2026-09-17T05:16:11+00:00: Recorded command exit 0; command argv SHA-256
  de60a3a7978b91181af8a719f64921210649cb36dd613c8be2c510c74fab68ac.

- 2026-09-17T05:16:29+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-09-17T05:16:38+00:00: Recorded command exit 0; command argv SHA-256
  5ad1a7755d175d3509168f6815456f005c8eb536f432b713f249f38fc31f4d00.

- 2026-09-17T05:16:46+00:00: Recorded command exit 0; command argv SHA-256
  d44e83ddb263e3c08341617b78eb268a9e3355cb7a9b6285ddc0b3befa9fe56c.

- 2026-09-17T05:17:05+00:00: Updated only tests/test_handoffctl_vendor.py from superseded v0.3.5
  fixture to verified immutable v0.3.7 commit 550c014c440cc9bc45727fea71d90a9025c554c3 and manifest
  SHA-256 bbde3b173f9e1904de583a6f686b71647942a4bb4e0062343ca99e5575c49512. Commit 53fd66118 is
  SSH-signed with DCO; focused vendor suite passes 8/8, Ruff format/check passes, and
  handoffctl_vendor verify passes. Full required state gates remain blocked by pre-existing mypy
  import/package errors and coverage report 84% below 95%; no vendor implementation, handoffctl,
  formal runner, product, asb-tui, or host-capacity changes.
