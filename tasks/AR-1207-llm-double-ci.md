---
{
  "branch": "feature/llm-double-ci",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": ["AR-0890", "AR-1203", "AR-1206"],
  "id": "AR-1207",
  "next_action": "Adopt the pinned isolated LLM double as the credential-free loopback provider for the record/replay/benchmark integration tests and prove fail-closed startup, --network none, bounded artifact bind, and provenance verification in CI.",
  "owner": "",
  "plan": "../plans/AR-1207.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Wire the deterministic LLM double (tools/llm-double-spike, AR-0890) into credential-free CI so the full record/replay/benchmark journey is exercised on every PR without a paid key.",
  "task_revision": 1,
  "title": "Deterministic LLM-double CI coverage of the integrated workflow",
  "updated_at": "2026-09-22T09:39:55+00:00",
  "worktree_key": "agent-systems-benchmark-llm-double-ci"
}
---
Wire the deterministic LLM double into credential-free CI so every PR exercises the full
record/replay/benchmark journey (AR-1204 journeys, replay-mode sweeps) without a paid key or
external network. Adopt the pinned isolated double as a loopback provider, prove fail-closed
startup, `--network none`, bounded artifact bind and provenance verification, and add hostile
lifecycle tests. Synthetic double output never converts into cassette/replay or live evidence; the
double stays strictly separate from replay evidence. Repository: `martin-beck/agent-systems-benchmark`.

- 2026-09-22T09:39:55+00:00: Defined from the record/replay/benchmark integration proposal.
  Depends on the LLM-double integration (AR-0890), replay-mode run/sweep (AR-1203), and the
  published documentation (AR-1206).
