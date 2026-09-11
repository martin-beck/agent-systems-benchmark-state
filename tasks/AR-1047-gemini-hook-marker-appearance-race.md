---
{
  "branch": "fix/gemini-hook-marker-appearance-race",
  "checkpoint_commit": "",
  "claim_expires": "2026-09-11T03:59:36+00:00",
  "depends_on": [],
  "id": "AR-1047",
  "next_action": "Obtain approval for the exact marker-appearance interleaving plan, then promote and claim before product edits.",
  "observed_branch": "fix/gemini-hook-marker-appearance-race",
  "observed_dirty": 0,
  "observed_head": "2ecb876b82a91a8103926b298c42ad49ce8dd143",
  "owner": "codex-ar1047-gemini-marker-race-20260911",
  "plan": "../plans/AR-1047.md",
  "priority": "P0",
  "schema_version": 1,
  "status": "in_progress",
  "summary": "Treat a regular marker published between absent open and fallback lstat as pending for descriptor validation on the next poll.",
  "task_revision": 7,
  "title": "Close the Gemini hook-marker appearance race",
  "updated_at": "2026-09-11T02:00:10+00:00",
  "worktree_key": "agent-systems-benchmark-gemini-hook-marker-appearance-race"
}
---

Three AArch64 runs failed different Gemini fixtures with `HookUnavailable`, including serialized
PR #138 run `34552034116`. Repair only the race where a valid regular marker appears after
`open(O_NOFOLLOW)` reports `NotFound` but before fallback lstat. A regular appearance is `Pending`
and must be reopened and fully validated on the next poll; symlink and non-regular appearances
remain `Invalid`. Add an exact deterministic interposition test and preserve all existing checks.

- 2026-09-11T01:59:34+00:00: Root approved the exact one-file marker-appearance interleaving plan as
  written.

- 2026-09-11T01:59:36+00:00: Claimed by codex-ar1047-gemini-marker-race-20260911.

- 2026-09-11T01:59:47+00:00: Recorded command exit 0; command argv SHA-256
  5345cd4b5f66285dc80cddfe59c0a95475263f9ff88d25d2639fce3c300aa4b9.

- 2026-09-11T01:59:56+00:00: Recorded command exit 0; command argv SHA-256
  cb829e9c4e7c7cffe24d5a6161df617fb253eb697a3402baff2975d02e925261.

- 2026-09-11T02:00:04+00:00: Recorded command exit 0; command argv SHA-256
  fcafd29cc68cb7dbd13e99fe2391391b29bf9302ac0c501b264c59c4834ca48e.
