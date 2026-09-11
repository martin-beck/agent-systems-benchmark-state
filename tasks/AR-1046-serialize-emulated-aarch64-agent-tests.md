---
{
  "branch": "test/serialize-emulated-aarch64-agents",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [],
  "id": "AR-1046",
  "next_action": "Obtain approval for the narrow two-file test/CI plan, then promote and claim before any product edit.",
  "owner": "",
  "plan": "../plans/AR-1046.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "open",
  "summary": "Make the emulated AArch64 asb-agents fake-node readiness fixtures deterministic without changing production semantics.",
  "task_revision": 2,
  "title": "Serialize emulated AArch64 agent tests",
  "updated_at": "2026-09-11T01:35:25+00:00",
  "worktree_key": "agent-systems-benchmark-emulated-aarch64-agent-serialization"
}
---

Two consecutive AArch64 QEMU lanes failed different Gemini fake-node tests with the same
`HookUnavailable`: current-main run `34550483005` failed the duplicate/stale-route fixture, while
PR #137 run `34550643921` job `103112635225` failed the ambient-config/cancellation fixture. Add
only `--test-threads=1` to the existing AArch64 `asb-agents --lib` command and bind that exact,
complete, non-retrying test inventory in `tests/platforms/test_emulated_aarch64.py`. Preserve the
existing skip and all budgets; do not change Rust production code or any UI/TUI repository.

- 2026-09-11T01:35:25+00:00: Root independently approved the narrow two-file AArch64 serialization
  plan after two distinct HookUnavailable failures.
