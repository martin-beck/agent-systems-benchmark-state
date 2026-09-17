---
{
  "branch": "feature/ar-1227-authenticated-startup-readiness",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-1060", "AR-1151", "AR-1160"],
  "id": "AR-1227",
  "next_action": "Complete dependencies, then implement and publish the bounded authenticated readiness schema, producer, fixtures, and compatibility tests.",
  "owner": "",
  "plan": "../plans/AR-1227.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Publish an authenticated, privacy-safe ASB startup-readiness contract for asb-tui.",
  "task_revision": 1,
  "title": "Authenticated startup-readiness contract",
  "updated_at": "2026-09-15T13:20:00+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1227-authenticated-startup-readiness"
}
---

ASB currently has no authoritative readiness command or control projection. Implement the linked
plan only after its dependencies are complete. This AR owns the producer contract and tests;
asb-tui owns the adapter, startup routing, persistence, rendering and all other UI behavior.

- 2026-09-15T13:20:00+00:00: Created from current-main audit: asb-tui's injected readiness seam
  exists, but ASB has no compatible authoritative producer. No implementation or TUI code is
  claimed by this planning AR.
