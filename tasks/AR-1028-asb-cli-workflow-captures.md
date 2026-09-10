---
{
  "branch": "docs/asb-cli-workflow-captures",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-10T23:03:42+00:00",
  "depends_on": [
    "AR-0872"
  ],
  "id": "AR-1028",
  "next_action": "Implement real-CLI normalized transcript fixture, provenance hash checks, drift/privacy negatives, and workflow documentation link.",
  "observed_branch": "docs/asb-cli-workflow-captures",
  "observed_dirty": 4,
  "observed_head": "32df706413a6f165f086941426a5c793bd5e01e8",
  "owner": "codex-ar1028-cli-captures-20260910",
  "plan": "../plans/AR-1028.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Produce reproducible ASB CLI transcripts separately from standalone TUI screenshots.",
  "task_revision": 10,
  "title": "Generate ASB CLI workflow captures",
  "updated_at": "2026-09-10T20:07:04+00:00",
  "worktree_key": "agent-systems-benchmark-asb-cli-workflow-captures"
}
---
Generate documentation transcripts from actual synthetic ASB CLI executions. This AR owns no
renderer, terminal application, Ratatui/Crossterm dependency, or asb-tui source.

- 2026-09-10T20:01:56+00:00: AR-0872 is durably done; CLI-only capture scope is dependency-ready and
  disjoint from all standalone TUI work.

- 2026-09-10T20:01:59+00:00: Claimed by codex-ar1028-cli-captures-20260910.

- 2026-09-10T20:02:02+00:00: Recorded command exit 0; command argv SHA-256
  48ce8c035d66a7ab0478204d6ea9ff42e080068ac6938ca529e2c4005f2449e2.

- 2026-09-10T20:03:42+00:00: Heartbeat by codex-ar1028-cli-captures-20260910.

- 2026-09-10T20:03:55+00:00: Recorded command exit 0; command argv SHA-256
  a2808036e9be365682dfe9eed52cfb76668c7c24ed86fdc4b59d26b160043f7d.

- 2026-09-10T20:05:21+00:00: Initial audit complete at ASB 32df706. Scope is text-only CLI evidence:
  doctor, plan, run, report, compare, record, replay. No screenshots, terminal renderer, TUI
  application, Ratatui/Crossterm, or asb-tui source. Classified initial exit 2 as read-only sed
  using the state checkout instead of sibling product docs; no mutation.

- 2026-09-10T20:06:55+00:00: Recorded command exit 0; command argv SHA-256
  f77810c92a0ebdfe32daa24865be55ae1eaea4ef4a8523cd21925d923d6398ad.
