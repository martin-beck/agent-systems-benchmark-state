---
{
  "branch": "feature/ar-1253-pinned-python-transport-runtime",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-16T15:18:50+00:00",
  "depends_on": [
    "AR-1252"
  ],
  "id": "AR-1253",
  "next_action": "Provision and qualify an immutable Python fixture runtime through the approved isolated runner.",
  "observed_branch": "feature/ar-1253-pinned-python-transport-runtime",
  "observed_dirty": 4,
  "observed_head": "85bcd1e423a6bd7da29a29cac4dbdcf9e4822837",
  "owner": "asb_ar1253_python_runtime",
  "plan": "../plans/AR-1253.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provision pinned Python transport fixture runtime.",
  "task_revision": 8,
  "title": "Provision pinned Python transport fixture runtime",
  "updated_at": "2026-09-16T13:20:53+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1253"
}
---

Implement only the linked AR-1253 plan using ASB development documentation and handoffctl.
Keep runtime images, caches, provenance, and all test activity under `/srv/data/projects`.

- 2026-09-16T13:18:48+00:00: AR-1252 completed with reviewed immutable Python image allowlist and
  exact-head evidence; promote runtime fixture successor.

- 2026-09-16T13:18:50+00:00: Claimed by asb_ar1253_python_runtime.

- 2026-09-16T13:19:05+00:00: Recorded command exit 0; command argv SHA-256
  eaa6bca78b91f67bb7aa44895c2a2056ccb44cfde9e2427c8f5830265b90b196.

- 2026-09-16T13:20:35+00:00: Recorded command exit 2; command argv SHA-256
  d4e2bee60595fe120ad7eded61b8217ae4d6ccf96558c587157ea92b28a28d2a.

- 2026-09-16T13:20:53+00:00: Recorded command exit 0; command argv SHA-256
  28d43d22f359a22bd0ca7c607add0b0027c1e04c9b8f12bc98809f42868628e8.
