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
  "owner": "asb-license-20260908",
  "plan": "../plans/AR-0855.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Enforce exact Huawei 2026 copyright and SPDX MIT headers across first-party product and state source files.",
  "task_revision": 2,
  "title": "Enforce Huawei MIT source headers",
  "updated_at": "2026-09-08T12:04:49+00:00",
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
