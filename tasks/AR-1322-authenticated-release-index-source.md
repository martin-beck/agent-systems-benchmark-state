---
{
  "branch": "feature/ar-1322-authenticated-release-index-source",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1322",
  "next_action": "Define and implement the bounded local signed release-index envelope, explicit trust-root configuration, hostile mutation tests, and verified closure promotion into the persisted catalog.",
  "owner": "",
  "plan": "../plans/AR-1322.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Promote only completely verified agents from a signed local release index.",
  "task_revision": 2,
  "title": "Authenticated agent release-index source",
  "updated_at": "2026-09-21T02:50:34+00:00",
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
