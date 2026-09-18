---
{
  "branch": "feature/standalone-asb-tui-application",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-18T21:22:30+00:00",
  "depends_on": [
    "AR-0804",
    "AR-0805",
    "AR-0806",
    "AR-0870",
    "AR-0871",
    "AR-1010",
    "AR-1022",
    "AR-1023",
    "AR-1037",
    "AR-1060"
  ],
  "id": "AR-1025",
  "next_action": "Blocked: implementation belongs to asb-tui, but current scope forbids touching that repository; AR-1010/AR-1060 also retain unresolved publication blockers. Obtain explicit scope/dependency repair before re-opening.",
  "owner": "asb-ar1025-boundary-audit-20260918",
  "plan": "../plans/AR-1025.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Deliver the actual standalone interactive asb-tui application without an ASB workspace dependency.",
  "task_revision": 8,
  "title": "Build the standalone asb-tui application",
  "updated_at": "2026-09-18T20:52:52+00:00",
  "worktree_key": "agent-systems-benchmark-asb-tui-standalone-application"
}
---
Build the functional shell in the separate repository and implement the bounded
owner-authenticated ASB control wire client. Legacy frontend behavior is read-only migration input;
the standalone source must not depend on the ASB Cargo workspace or assume benchmark ownership.

Acceptance requires stable capability-gated routes and extension seams, launch/status/cancel and
reconnect state projection, terminal restoration and generic accessibility fallbacks, cross-contract
fixtures, complete tests and audits, exact-head CI and post-merge verification. Final landing,
measurement-selection, configuration, report/comparison, contextual-help and professional visual
implementation remains owned by AR-1014 and AR-1031 through AR-1035.

Repository boundary: the complete application lives in `martin-beck/asb-tui`; this AR owns no
product path in `martin-beck/agent-systems-benchmark`.

- 2026-09-11T04:12:48+00:00: Narrowed this AR to the functional application shell and stable
  extension seams so it can complete before, and without duplicating, the focused downstream UI ARs.

- 2026-09-11T05:05:00+00:00: Added ASB AR-1037 as a dependency and bound the standalone client to
  closed v1.3 precise-diagnostic parsing with exact v1.2 legacy fallback categories; visible
  validation presentation remains AR-1014-owned.

- 2026-09-11T05:28:38+00:00: Added AR-1060 as the prerequisite for receiving and independently
  re-authenticating a privacy-safe inherited control channel. Endpoint discovery/provisioning stays
  in ASB; all transport consumption and application behavior stays in standalone `asb-tui`.

- 2026-09-18T20:52:24+00:00: Dependencies are durably marked done by the coordinator; promotion is
  for boundary audit only. Before implementation, verify the repository authorization and semantic
  completion of AR-1010/AR-1060; AR-1025 implementation belongs only to standalone asb-tui and must
  not touch ASB product paths or blocked runner ARs.

- 2026-09-18T20:52:30+00:00: Claimed by asb-ar1025-boundary-audit-20260918.

- 2026-09-18T20:52:52+00:00: Boundary audit complete. AR-1025 owns only martin-beck/asb-tui: its
  plan and task explicitly forbid ASB product changes, while current coordinator scope forbids
  touching asb-tui. Therefore no worktree or source implementation was created. Dependency statuses
  are marked done, but AR-1010 next_action still requires AR-1062 publication/green exact-main gates
  and recovered AR-1060 provenance; AR-1060 next_action explicitly says keep AR-1060 blocked pending
  authorized repository-level recovery. These are semantic dependency blockers despite done labels.
  No ASB product, runner, or asb-tui files were modified.
