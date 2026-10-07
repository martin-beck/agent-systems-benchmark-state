---
{
  "branch": "repair/ar-1727-development-broker-foreground-terminal",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T01:31:36+00:00",
  "depends_on": [
    "AR-1590"
  ],
  "id": "AR-1727",
  "next_action": "Await independent exact-head review of PR #500 at 23138efcc45dc78232fdb13ebbf722f76f14824b; do not merge without review and required exact-head CI.",
  "observed_branch": "repair/ar-1727-development-broker-foreground-terminal",
  "observed_dirty": 0,
  "observed_head": "23138efcc45dc78232fdb13ebbf722f76f14824b",
  "owner": "codex-ar1727-independent-review",
  "plan": "../plans/AR-1727-development-broker-foreground-terminal.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1727.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Give the ASB development broker child correct foreground process-group ownership on the caller's controlling terminal without weakening descendant cleanup.",
  "task_revision": 36,
  "title": "Repair development broker foreground-terminal handoff",
  "updated_at": "2026-10-07T23:32:46+00:00",
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

- 2026-10-07T23:02:28+00:00: Recorded command exit 0; command argv SHA-256
  73d005d4c4983870f0c5405c6c97dffbf521d57825b14d75dae888988fbdcd03.

- 2026-10-07T23:03:34+00:00: Recorded command exit 101; command argv SHA-256
  5ec889fe8c38c8d1a32cf0e9094ce7fe137d8757ab39f2ce28bbeb1a2188cc10.

- 2026-10-07T23:04:15+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T23:05:08+00:00: Recorded command exit 0; command argv SHA-256
  5ec889fe8c38c8d1a32cf0e9094ce7fe137d8757ab39f2ce28bbeb1a2188cc10.

- 2026-10-07T23:06:22+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T23:06:46+00:00: Recorded command exit 101; command argv SHA-256
  5ec889fe8c38c8d1a32cf0e9094ce7fe137d8757ab39f2ce28bbeb1a2188cc10.

- 2026-10-07T23:07:12+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T23:07:35+00:00: Recorded command exit 101; command argv SHA-256
  5ec889fe8c38c8d1a32cf0e9094ce7fe137d8757ab39f2ce28bbeb1a2188cc10.

- 2026-10-07T23:08:42+00:00: Recorded command exit 101; command argv SHA-256
  5ec889fe8c38c8d1a32cf0e9094ce7fe137d8757ab39f2ce28bbeb1a2188cc10.

- 2026-10-07T23:09:23+00:00: Recorded command exit 0; command argv SHA-256
  cfddfc1b8766f37e6aede838c174f3c1396c0e28ea1eae79d472cf1b97a74f13.

- 2026-10-07T23:09:46+00:00: Recorded command exit 0; command argv SHA-256
  5ec889fe8c38c8d1a32cf0e9094ce7fe137d8757ab39f2ce28bbeb1a2188cc10.

- 2026-10-07T23:10:50+00:00: Recorded command exit 0; command argv SHA-256
  2eb57b2f8bcd09b047408f4fc2e4f35c2309ee120c2d687da18d72fe3ae8af1b.

- 2026-10-07T23:13:47+00:00: Recorded command exit 0; command argv SHA-256
  22fc19d872be75a975891ff0abd53f1c305974a409b50c49c5df5d842d033e81.

- 2026-10-07T23:14:19+00:00: Recorded command exit 0; command argv SHA-256
  eb8648d78be9d44db5631385c3fcbaaeaac0114989924fef6dc1415045ce0bfa.

- 2026-10-07T23:14:50+00:00: Recorded command exit 0; command argv SHA-256
  f7e20666638201d8567703a3d7bc028e04a5e8e4c6c509de13d4976b0c91a669.

- 2026-10-07T23:15:18+00:00: Recorded command exit 0; command argv SHA-256
  7c730eec3ea71bd24ffc5a9255bf7f542481bf601dba6c72bed6e00f6c2fab3c.

- 2026-10-07T23:16:44+00:00: Recorded command exit 0; command argv SHA-256
  f44e5b34cae283ed9dc8daee028e7e7ff47d25bb1125059c4faf03c6655777a4.

- 2026-10-07T23:17:16+00:00: Recorded command exit 0; command argv SHA-256
  3c4e8791f9549bea36de0ff214cbea1586d16c782df22df84785430650232127.

- 2026-10-07T23:17:50+00:00: Recorded command exit 0; command argv SHA-256
  7b051c0de11bcaca2bd062bef2a96ff27b195c43db8a938167da563eb5f8c122.

- 2026-10-07T23:18:29+00:00: Recorded command exit 0; command argv SHA-256
  0f6593c2fabffb24437f96375c518552aa7ec6b0b0278b23a30fbf11a85381f5.

- 2026-10-07T23:19:09+00:00: Implementation is signed+DCO and pushed in PR #500 at head
  23138efcc45dc78232fdb13ebbf722f76f14824b, tree 64b5b218de1d563cd1f875c82a6ee2b059d6922c. Focused
  real controlling-PTY development-broker regression passed, all 37 development broker tests passed,
  full asb-cli suite passed, cargo check/clippy/fmt and git diff --check passed. Stop for
  independent exact-head review.

- 2026-10-07T23:30:13+00:00: Implementation worker stopped after publishing PR #500 exact head
  23138efcc45dc78232fdb13ebbf722f76f14824b; release the author lease so a distinct independent
  reviewer can claim it.

- 2026-10-07T23:31:36+00:00: Claimed by codex-ar1727-independent-review.

- 2026-10-07T23:31:42+00:00: Recorded command exit 0; command argv SHA-256
  23ee6aeabffe88c31761aa4dd407eaafb7c3cd9285760703a094e55f5462c173.

- 2026-10-07T23:32:12+00:00: Recorded command exit 0; command argv SHA-256
  2f5a7e548b7427ecfc64b77a748590d085e263e87a423954d1d69ae25d0c7bb1.

- 2026-10-07T23:32:46+00:00: Recorded command exit 101; command argv SHA-256
  855999e59c388ec283d5a4d27165c343d9416af16710d3dd9bea90b79ad10a76.
