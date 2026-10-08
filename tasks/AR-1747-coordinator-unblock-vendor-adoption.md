---
{
  "branch": "repair/ar-1747-coordinator-unblock-vendor",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T18:17:08+00:00",
  "depends_on": [],
  "id": "AR-1747",
  "next_action": "Promote and claim; synchronize the reviewed upstream Coordinator development identity that adds provenance-checked unblock, then qualify the complete ASB state vendor closure and blocked-task transition fixtures.",
  "owner": "codex-asb-ar1747-vendor-20261008",
  "plan": "../plans/AR-1747-coordinator-unblock-vendor-adoption.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1747.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Adopt the official Coordinator development unblock capability in ASB state so AR-1722 can be reopened through a supported provenance-checked transition.",
  "task_revision": 12,
  "title": "Adopt Coordinator unblock support for AR-1722",
  "updated_at": "2026-10-08T16:52:14+00:00",
  "worktree_key": "agent-systems-benchmark-state-ar-1747-coordinator-unblock-vendor"
}
---

ASB state currently vendors Coordinator v0.3.57, whose `resume` command accepts
only a valid pause snapshot. AR-1722 is externally blocked and has no pause
snapshot, so it cannot be reopened safely with the installed command set.
Upstream development commit `e863b57edc7f7a21b2aff2c7b45ce226e12637d2`
(tree `eee603591b917eeca244425559d7c67bb88a7268`) contains the independently
reviewed provenance-checked `unblock` transition and its complete formal vendor
closure. This AR owns exact adoption and downstream qualification; it must not
fabricate a pause, edit AR-1722 directly, or change ASB product runtime code.

- 2026-10-08T16:15:59+00:00: Official upstream Coordinator e863b57 already contains the reviewed
  unblock repair; exact downstream development vendor adoption is dependency-ready and path-isolated
  from AR-1746.

- 2026-10-08T16:17:08+00:00: Claimed by codex-asb-ar1747-vendor-20261008.

- 2026-10-08T16:17:14+00:00: Recorded command exit 0; command argv SHA-256
  321c534968b9c456a64caf5e6d09b63780c507f97548057d2bfe31edcfd73ff4.

- 2026-10-08T16:18:22+00:00: Recorded command exit 0; command argv SHA-256
  9811681c1d756cb583e733f64feb3306dcb60dbccc1ce655f0e9d174df4d13ed.

- 2026-10-08T16:21:42+00:00: Recorded command exit 0; command argv SHA-256
  b441e12f5aaf7da29555cd380addd8e739f421fa238e5f229ef76c7ec0483513.

- 2026-10-08T16:22:17+00:00: Recorded command exit 0; command argv SHA-256
  ad0356d5ddf070012b883621bffe60f5e38f37a5bce5bed0322d506e33f34d89.

- 2026-10-08T16:23:25+00:00: Recorded command exit 0; command argv SHA-256
  fec63797cd58c7d66faaded7b85b6950838c1e070fb864fbab0c3b6e26eb5d6e.

- 2026-10-08T16:23:57+00:00: Recorded command exit 0; command argv SHA-256
  098032cc6f966bf4b8de6774d1870b51a66c7d8c6a1b2a8609d014022ba43e7a.

- 2026-10-08T16:35:48+00:00: Recorded command exit 128; command argv SHA-256
  6277e66c506fd007d5f2d98119f1c3fcdf03a71967b5e474185bc558f9e4904b.

- 2026-10-08T16:50:04+00:00: Recorded command exit 0; command argv SHA-256
  22fda1bfad2e346d78ef52139e226051d0eb6ebc6d4e886f541c2931d15a5f25.

- 2026-10-08T16:52:14+00:00: Recorded command exit 0; command argv SHA-256
  6532337c5032d4d6925093fcca4bb25098786bfa5cac379ac14f4d2d912001e3.
