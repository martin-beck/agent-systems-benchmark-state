# AR-1816 implementation plan

## Scope

1. Reproduce the two observed coordinator failures from disposable state copies:
   stale generated `PROJECT_STATE.md`/`WORKTREES.md`, and an oversized
   `tools/__pycache__/handoffctl*.pyc` created by supported coordinator usage.
2. Inventory every supported coordinator entry point, subprocess, and test
   launcher that can import coordinator Python. Establish a central bytecode
   policy: prevent repository-local bytecode or redirect it to a private
   ephemeral cache outside the state repository. Do not depend on each caller
   setting `PYTHONDONTWRITEBYTECODE` manually.
3. Make reconciliation lock-aware and projection-atomic. Build candidate views
   off-path, validate their shared source revision and size/privacy constraints,
   and publish the complete matched set only while holding the appropriate
   coordinator lock. On lock timeout or interrupted publish, preserve the last
   valid pair and return a typed recoverable diagnostic.
4. Add a supported recovery command/path that refreshes stale views through
   `handoffctl`; never direct users to edit `CURRENT.md`, `PROJECT_STATE.md`, or
   `WORKTREES.md`. It must be idempotent and leave unrelated active task files
   untouched.
5. Keep concurrent task ownership and AR-1815 merge recovery out of scope.
   The repair must coexist with another valid coordinator holder and must not
   delete broad caches, rewrite history, force-push, or relax state-size guards.

## Validation

- Focused unit and fault-injection tests cover bytecode behavior, render
  interruption, contention, stale-pair detection, retry/idempotence, and
  privacy/size guards.
- A concurrent-process integration test proves only one reconciliation wins;
  the loser returns the documented typed lock diagnostic and neither exposes a
  mixed projection pair.
- A configured primary-checkout journey runs `reconcile`, `snapshot`, and
  `doctor --live` cleanly without repository-local bytecode.
- An independent exact-head review and required coordinator checks verify the
  signed DCO change; no giant TLC or live-provider run is part of this repair.
