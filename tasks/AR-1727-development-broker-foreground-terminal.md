---
{
  "branch": "repair/ar-1727-development-broker-foreground-terminal",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T00:55:31+00:00",
  "depends_on": [
    "AR-1590"
  ],
  "id": "AR-1727",
  "next_action": "Promote and claim after coordinator reconciliation; repair the ASB development broker foreground-terminal handoff, add a controlling-PTY regression on the actual broker launch path, and retain bounded process-group cleanup.",
  "observed_branch": "repair/ar-1727-development-broker-foreground-terminal",
  "observed_dirty": 3,
  "observed_head": "f535e3cb327b99b35bae2ddae9f0086b3c211303",
  "owner": "codex-ar1727-broker-foreground",
  "plan": "../plans/AR-1727-development-broker-foreground-terminal.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1727.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Give the ASB development broker child correct foreground process-group ownership on the caller's controlling terminal without weakening descendant cleanup.",
  "task_revision": 9,
  "title": "Repair development broker foreground-terminal handoff",
  "updated_at": "2026-10-07T23:00:02+00:00",
  "worktree_key": "agent-systems-benchmark-ar-1727-development-broker-foreground-terminal"
}
---

ASB currently starts the development asb-tui child in a private process group
but leaves the caller's controlling terminal foreground group unchanged. The
child then opens the validated development terminal while still in a background
group, so normal terminal I/O can stop it with `SIGTTOU`/`SIGTTIN` and the
public `asb tui` route reports `development_launch_failed`.

Repair only the ASB development broker launch in `crates/asb-cli/src/tui.rs`.
The interactive child must own the caller's controlling terminal foreground
while it runs, and the exact prior foreground group must be restored on every
success and failure path. Keep the child in an ASB-owned private process group
so timeout, failure, cancellation, and descendant-held broker cleanup remain
bounded. Use safe Rust interfaces; do not add first-party unsafe code.

Add a focused regression that establishes a real controlling PTY and exercises
`launch_development_broker_with_backend`; checking the stable `run_candidate`
path or only unit-testing a foreground helper is insufficient. Preserve typed
failure behavior for absent, non-controlling, changed, or unusable terminals.
The separate asb-tui operator qualification-runner zero-size/non-controlling
PTY repair is outside this AR.

Completion requires signed+DCO commits, focused and full relevant tests,
independent exact-head review, protected merge, and terminal-green post-merge
CI before the downstream asb-tui AR-1654 qualification is rerun.

- 2026-10-07T22:54:25+00:00: AR-1590 is done; downstream TUI AR-1654 has exact evidence of the ASB
  development child remaining in a background terminal group. Begin the bounded foreground-terminal
  repair and real controlling-PTY regression.

- 2026-10-07T22:55:31+00:00: Claimed by codex-ar1727-broker-foreground.

- 2026-10-07T22:56:21+00:00: Recorded command exit 0; command argv SHA-256
  bf36bfe9ad14dc3de9999bf713e52ca5565dc82bea504d546e94f18538a6d291.

- 2026-10-07T22:56:52+00:00: Recorded command exit 0; command argv SHA-256
  66f3054578b4141f56ec6355840cff3716a5c7ed2247e40bd21854fb35013e78.

- 2026-10-07T22:59:09+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.
