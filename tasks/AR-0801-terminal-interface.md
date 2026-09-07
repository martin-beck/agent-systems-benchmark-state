---
{
  "branch": "feature/terminal-interface",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-07T02:37:14+00:00",
  "depends_on": [
    "AR-0101",
    "AR-0104",
    "AR-0204"
  ],
  "id": "AR-0801",
  "next_action": "Audit public library seams and implement honest doctor/plan/run/sweep/compare/report boundaries with stable JSON, meaningful exits, cancellation and PTY tests.",
  "observed_branch": "feature/terminal-interface",
  "observed_dirty": 0,
  "observed_head": "b79534b627e28792a46e1a0074be762bb425d2a6",
  "owner": "root-coordination-20260906",
  "plan": "../plans/AR-0801.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Provide doctor, plan, run, sweep, compare and report with stable JSON output.",
  "task_revision": 7,
  "title": "Implement terminal and automation interfaces",
  "updated_at": "2026-09-07T01:10:52+00:00",
  "worktree_key": "agent-systems-benchmark-terminal-interface"
}
---
## AR-0801

Provide doctor, plan, run, sweep, compare and report with stable JSON output.

Implementation has not started. Read the linked plan before claiming.

- 2026-09-07T01:07:00+00:00: Dependencies AR-0101, AR-0104, and AR-0204 are durably done on
  synchronized signed product main b79534b; asb-cli ownership is disjoint from active Gemini, Goose,
  and mini-SWE adapter paths.

- 2026-09-07T01:07:14+00:00: Claimed by root-coordination-20260906.

- 2026-09-07T01:07:33+00:00: Recorded command exit 0; command argv SHA-256
  363c68c50f2b2e053c643e4c2b2f71566885660eb8e7d143586d2c240ab187b5.

- 2026-09-07T01:08:21+00:00: Fresh snapshot read after claim. Declared ownership: crates/asb-cli/**
  plus only its required Cargo dependency/lock integration and dedicated CLI fixtures; no asb-agents
  registration, schemas, or active adapter paths. Root holds the serialized Cargo.lock fence for
  AR-0801; Gemini separately holds only the additive asb-agents lib.rs fence.

- 2026-09-07T01:10:52+00:00: Recorded command exit 0; command argv SHA-256
  ad10ed9ff5eac4e58674b8db7e75e27da84a50f5ed14019df1f28374c7acefd0.
