---
{
  "branch": "feature/authenticated-control-endpoint-handoff",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T06:28:38+00:00",
  "depends_on": [
    "AR-1022",
    "AR-1023"
  ],
  "id": "AR-1060",
  "next_action": "Freeze the descriptor and reconnect contract, then implement ASB provisioning and standalone asb-tui peer-authenticated consumption in separately reviewed repository changes.",
  "owner": "codex-ar1060-control-endpoint-handoff-state-20260911",
  "plan": "../plans/AR-1060.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Hand the standalone frontend an authenticated ASB control connection without exposing endpoint paths.",
  "task_revision": 3,
  "title": "Add authenticated control endpoint handoff",
  "updated_at": "2026-09-11T05:32:55+00:00",
  "worktree_key": "agent-systems-benchmark-authenticated-control-endpoint-handoff"
}
---

Define and implement the non-UI boundary that connects the separately installed `asb-tui` frontend
to the authoritative ASB control service. ASB owns endpoint discovery, connection provisioning and
reconnection authority. The standalone repository owns transport consumption and independent peer
re-authentication. Prefer a safely transferred, already-connected Unix descriptor; never disclose
raw socket paths or endpoints through environment variables, arguments, public responses, logs or
diagnostics.

This AR coordinates two repository-local implementation halves with separate commits, tests,
immutable reviews and protected merges. It assigns no renderer, Ratatui, Crossterm, navigation,
widget, screen or application-shell implementation to ASB. AR-1024 remains open and AR-1025 remains
planned until their full dependency sets are done.

- 2026-09-11T05:28:38+00:00: Created under the coordinator lock after confirming AR-1060 is the
  next free identifier. AR-1022 and AR-1023 are durably done; AR-1024 and AR-1025 retain their
  existing status and owner while gaining this prerequisite.

- 2026-09-11T05:28:38+00:00: Claimed by
  codex-ar1060-control-endpoint-handoff-state-20260911 for state-only task definition and graph
  validation; release OPEN/unowned after the signed state commit.

- 2026-09-11T05:32:00+00:00: Initial schema command exited 1 because the base Python environment
  lacks `jsonschema`; its automatic result reconciliation then detected the concurrently committed
  duplicate AR-1060 node. Preserved that commit in history, removed only its colliding task in this
  authorized successor, and restored AR-1010 byte-for-byte to origin/main so its dependency does not
  point at this unrelated endpoint-handoff task.

- 2026-09-11T05:32:22+00:00: Recorded command exit 1; command argv SHA-256
  f42ab07ce4e4d1a4d356a15458f58b78063c28c29356959d63aadf8968d17b7a.

- 2026-09-11T05:32:55+00:00: Recorded command exit 0; command argv SHA-256
  3adf945d41e31464bc901f1cb355cd00146cd5cb01e2faa01ac63df19394e675.
