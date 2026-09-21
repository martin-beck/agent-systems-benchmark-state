---
{
  "branch": "feature/ar-1322-authenticated-release-index-source",
  "checkpoint_commit": "a4934fca0b528ac90d09fb537936584f5af0f75e",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1322",
  "next_action": "Run post-merge live ASB-to-asb-tui catalog projection with a configured signed index; keep unavailable fallback when trust configuration is absent.",
  "owner": "",
  "plan": "../plans/AR-1322.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "done",
  "summary": "Promote only completely verified agents from a signed local release index.",
  "task_revision": 5,
  "title": "Authenticated agent release-index source",
  "updated_at": "2026-09-21T03:20:13+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1322-authenticated-release-index-source"
}
---

AR-1320 persists the catalog and fences generations, but its source is still the
truthful unavailable roster. This AR supplies the missing bounded signed local
release-index reader and the complete-closure promotion path. It must reuse the
existing package/provenance types, reject unsigned/tampered/target-mismatched
entries, and leave incomplete entries visible but unavailable.

- 2026-09-21T02:50:34+00:00: Persistence/restart fencing is already merged; this AR owns only the
  signed source and closure promotion.

- 2026-09-21T02:50:41+00:00: Claimed by codex-ar1322.

- 2026-09-21T03:20:10+00:00: PR #247 merged via locally SSH-signed two-parent merge a4934fca; all
  hosted checks passed, including coverage after the signed positive-path test, Rust, policy,
  platform, fuzz, model and AWQ gates.

- 2026-09-21T03:20:13+00:00: Implementation and hosted/post-merge evidence complete; remaining live
  cross-repository projection is tracked as the next wizard acceptance slice.
