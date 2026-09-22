---
{
  "branch": "feature/ar-1331-runtime-replay-launch-authority",
  "checkpoint_commit": "",
  "claim_expires": "",
  "depends_on": [
    "AR-1330"
  ],
  "id": "AR-1331",
  "next_action": "Provide the runtime-owned ReplayLaunchAuthority so asb replay can invoke strict replay of sealed cassettes, and prove the CLI cannot fabricate one.",
  "owner": "",
  "plan": "../plans/AR-1331.md",
  "priority": "P1",
  "schema_version": 1,
  "status": "planned",
  "summary": "Deliver the runtime-owned strict-replay launch authority required by the replay CLI contract.",
  "task_revision": 1,
  "title": "Runtime-owned strict-replay launch authority",
  "updated_at": "2026-09-22T13:39:37+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1331-runtime-replay-launch-authority"
}
---

The replay CLI contract requires a `ReplayLaunchAuthority` that can only be
issued by the runtime, but no code path constructs one, so `asb replay` can
never run. This AR delivers the runtime-owned launch authority: a constructor-
or lifecycle-owned value that binds a live run context to the sealed cassettes
produced by AR-1330, is injected through the supervised context the CLI already
requires, and cannot be fabricated by a caller-supplied manifest or CLI flag.
Replay remains strict, offline-only, and without any fallback to a live
provider.
