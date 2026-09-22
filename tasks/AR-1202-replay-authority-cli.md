---
{
  "branch": "feature/replay-authority-cli",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0102", "AR-0503", "AR-0504", "AR-0314", "AR-1201"],
  "id": "AR-1202",
  "next_action": "Add a runtime-supervised entry that constructs the ReplayLaunchFactory binding, spawns the loopback strict-replay sidecar with provider network denied, and hands the authority to the existing replay dispatch path.",
  "owner": "",
  "plan": "../plans/AR-1202.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "planned",
  "summary": "Close the authority gap so asb replay (and the runtime path behind it) issues a ReplayLaunchAuthority, launches the adapter against the loopback StrictReplayService with provider network denied, and returns the documented JSON/exit contract.",
  "task_revision": 1,
  "title": "Make asb replay end-to-end usable",
  "updated_at": "2026-09-22T09:39:55+00:00",
  "worktree_key": "agent-systems-benchmark-replay-authority"
}
---
Close the `ReplayLaunchAuthority` gap: `asb replay CASSETTE PROFILE_SHA256 AGENT` self-hosts the
runtime supervisor, issues a one-shot authority, launches the pinned adapter against the loopback
`StrictReplayService` with no outbound provider route, and emits the existing
`ReplayWorkflowOutput` with correct exit codes. All existing fail-closed rules (exact match,
one-shot authority, exhausted cursor, no fallback) stay in force. Repository:
`martin-beck/agent-systems-benchmark`.

- 2026-09-22T09:39:55+00:00: Defined from the record/replay/benchmark integration proposal.
  Depends on AR-0102, AR-0503, AR-0504, AR-0314 and the capture sidecar patterns from AR-1201.
  The standalone entry without authority must still fail safely (no regression in
  `workflow_transcript.rs` expectations, or the transcript is intentionally updated in AR-1206).
