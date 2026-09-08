---
{
  "branch": "feature/shared-workflow-coordinator",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-08T08:56:54+00:00",
  "depends_on": [],
  "id": "AR-0851",
  "next_action": "After the canonical public release is verified, vendor its pinned artifact and run ASB-specific conformance, fault, race, renderer, schema, and live checks.",
  "owner": "codex-agent-workflow-coordinator-asb-20260908",
  "plan": "../plans/AR-0851.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Adopt the canonical coordinator as a pinned offline-capable vendor artifact while preserving ASB extensions.",
  "task_revision": 6,
  "title": "Adopt shared workflow coordinator",
  "updated_at": "2026-09-08T05:56:54+00:00",
  "worktree_key": "agent-systems-benchmark-shared-coordinator"
}
---

The canonical implementation and formal proof are maintained upstream. This task owns only the
ASB integration, compatibility evidence, and version pin.
- 2026-09-08T04:48:10+00:00: Claimed by codex-agent-workflow-coordinator-20260908.

- 2026-09-08T04:49:22+00:00: Recorded command exit 0; command argv SHA-256
  fa2584f233680b7135904d1bf97ee846d8a0dba6cc7744e4801b4d3ce9ba14fa.

- 2026-09-08T04:52:25+00:00: Reconciled cross-project claim: owner process operated Agent Relay
  AR-2203 instead of ASB state; no ASB worktree or product mutation found. Preserve AR-0851 planned
  for a correctly scoped worker.

- 2026-09-08T05:56:52+00:00: Canonical v0.1.1 release is published and its full verification
  workflow passed.

- 2026-09-08T05:56:54+00:00: Claimed by codex-agent-workflow-coordinator-asb-20260908.
