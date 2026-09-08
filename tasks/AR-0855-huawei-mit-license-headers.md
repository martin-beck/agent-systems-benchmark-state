---
{
  "branch": "fix/huawei-mit-license-headers",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T14:04:49+00:00",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-0855",
  "next_action": "Claim, create the declared worktree, enforce exact first-party Huawei MIT source headers, test, and publish unmerged PRs.",
  "observed_branch": "fix/huawei-mit-license-headers",
  "observed_dirty": 0,
  "observed_head": "d8e9d0af21a0f5f29d2b1076f33ce8153e1d26fc",
  "owner": "asb-license-20260908",
  "plan": "../plans/AR-0855.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Enforce exact Huawei 2026 copyright and SPDX MIT headers across first-party product and state source files.",
  "task_revision": 11,
  "title": "Enforce Huawei MIT source headers",
  "updated_at": "2026-09-08T13:14:12+00:00",
  "worktree_key": "agent-systems-benchmark-huawei-mit-headers"
}
---
## AR-0855

Enforce the exact adjacent source header:

`Copyright (C) Huawei Technologies Co., Ltd. 2026. All rights reserved.`

followed immediately by `SPDX-License-Identifier: MIT`, using the language's comment syntax and
preserving a required shebang before the header.

This task is independent of active feature work but deliberately owns the repository-wide
first-party source-header normalization and its policy/CI enforcement. Read the complete linked plan
and fresh coordinator snapshot before claiming. Do not modify vendored coordinator or generated views.

- 2026-09-08T12:04:49+00:00: Claimed by asb-license-20260908.

- 2026-09-08T12:06:22+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-08T12:06:31+00:00: Recorded command exit 0; command argv SHA-256
  fac3a91f8189303be4ef194964934579e3e02c7ff5adc72bee93f57757f470b4.

- 2026-09-08T12:08:52+00:00: Recorded command exit 0; command argv SHA-256
  ac02fc7321156c892ccadad64a6da3760d971d00818d2156a66648f4589fa21e.

- 2026-09-08T12:09:01+00:00: Recorded command exit 0; command argv SHA-256
  7e0dcff2ee61f99fac0a79f3596565aac77e5ed1edb75c1efbf64a1fdb3fb34d.

- 2026-09-08T13:12:53+00:00: Recorded command exit 128; command argv SHA-256
  8dc21a6ce0d4263a1d793e955c6ed283d68199ad980d0802e50e714c01ae6cff.

- 2026-09-08T13:13:24+00:00: Recorded command exit 1; command argv SHA-256
  83d0b37eb55687a352ac03b2b490559a7b4a01c8622a798e9e4da775e9649065.

- 2026-09-08T13:13:54+00:00: Recorded command exit 1; command argv SHA-256
  83d0b37eb55687a352ac03b2b490559a7b4a01c8622a798e9e4da775e9649065.

- 2026-09-08T13:14:12+00:00: Recorded command exit 1; command argv SHA-256
  f0e414dfa1dd21b3af37e8816f96d64fb2afd3c45da5e00bfc591259ba9f8e03.
