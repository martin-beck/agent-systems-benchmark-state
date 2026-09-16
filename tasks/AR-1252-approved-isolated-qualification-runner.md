---
{
  "branch": "feature/ar-1252-approved-isolated-runner",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T13:05:01+00:00",
  "depends_on": [
    "AR-0003"
  ],
  "id": "AR-1252",
  "next_action": "Provision and qualify a digest-pinned Docker runner with network none, bounded resources, no host mounts, and deterministic cleanup for AR-1251.",
  "observed_branch": "feature/ar-1252-approved-isolated-runner",
  "observed_dirty": 1,
  "observed_head": "128ecddbfdb7fcfff6e257adf3237b5866aca481",
  "owner": "asb_ar1252_isolated_runner",
  "plan": "../plans/AR-1252.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provision an approved isolated qualification runner for ASB executable evidence.",
  "task_revision": 7,
  "title": "Provision approved isolated qualification runner",
  "updated_at": "2026-09-16T11:06:15+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1252"
}
---

Implement only the linked AR-1252 plan using ASB development documentation and handoffctl.
All runner images, scripts, and caches remain under `/srv/data/projects`; preserve offline-after-install,
privacy, credential isolation, network denial, bounded execution, signatures, DCO, and exact-tree gates.

- 2026-09-16T11:04:39+00:00: AR-1251 confirmed host namespace restriction; Docker service is
  available via sudo. Promote digest-pinned isolated runner prerequisite.

- 2026-09-16T11:05:01+00:00: Claimed by asb_ar1252_isolated_runner.

- 2026-09-16T11:05:33+00:00: Recorded command exit 0; command argv SHA-256
  9a629caf66475420aed9c07df8c351e422dcf1776f37f894d6b6623e938fb0c9.

- 2026-09-16T11:06:08+00:00: Recorded command exit 1; command argv SHA-256
  c79e6d417ab6578a138bbbedff733c06012990297ed6d0d0ba852eb8fd34512e.
