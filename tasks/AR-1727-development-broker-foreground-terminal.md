---
{
  "branch": "repair/ar-1727-development-broker-foreground-terminal",
  "checkpoint_commit": "",
  "claim_expires": "2026-10-08T01:38:17+00:00",
  "depends_on": [
    "AR-1590"
  ],
  "id": "AR-1727",
  "next_action": "Repair PR #500 changed-foreground ownership race: revalidate the captured terminal foreground group under scoped SIGTTOU masking before tcsetpgrp, preserve the new owner on mismatch, restore the prior signal mask on every path, and add a real controlling-PTY changed-owner failure/cleanup regression; then rerun exact-head review and CI.",
  "observed_branch": "repair/ar-1727-development-broker-foreground-terminal",
  "observed_dirty": 1,
  "observed_head": "23138efcc45dc78232fdb13ebbf722f76f14824b",
  "owner": "codex-ar1727-p1-repair",
  "plan": "../plans/AR-1727-development-broker-foreground-terminal.md",
  "priority": "P0",
  "schema_version": 1,
  "spec_ref": "specs/AR-1727.json",
  "spec_revision": 1,
  "status": "in_progress",
  "summary": "Give the ASB development broker child correct foreground process-group ownership on the caller's controlling terminal without weakening descendant cleanup.",
  "task_revision": 59,
  "title": "Repair development broker foreground-terminal handoff",
  "updated_at": "2026-10-08T00:02:16+00:00",
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

- 2026-10-07T23:34:13+00:00: Recorded command exit 0; command argv SHA-256
  8028f0a5c7512a5d24b7766f5407ec99f03689ab62c4af8570ec23260fdd461a.

- 2026-10-07T23:34:43+00:00: Recorded command exit 0; command argv SHA-256
  b2a8a44d6785058ceaadb8be2c9f3dbfc4d5a472b8e30b0422d89c1dac1323ef.

- 2026-10-07T23:36:02+00:00: Recorded command exit 0; command argv SHA-256
  bbfb3d04c990bd9a126526c0548ba0d1d058dc1a5c3e1603fad4b119edb4020d.

- 2026-10-07T23:36:43+00:00: Independent review at exact head
  23138efcc45dc78232fdb13ebbf722f76f14824b/tree 64b5b218de1d563cd1f875c82a6ee2b059d6922c found one
  P1. DevelopmentForegroundTerminal::assign calls tcsetpgrp without revalidating tcgetpgrp against
  the captured original group and without blocking SIGTTOU. If terminal ownership changes during
  setup/spawn, ASB may stop as a background pgrp or overwrite a new owner instead of returning the
  required typed failure with bounded cleanup. Exact focused controlling-PTY regression passed; all
  37 development tests passed; 14 hosted checks terminal green; signature, DCO, scope, privacy,
  safe-Rust boundary clean. GitHub exact-head review comment records the repair and regression
  requirements.

- 2026-10-07T23:36:49+00:00: Independent exact-head review completed with one merge-blocking P1
  changed-foreground/SIGTTOU race. PR #500 must be repaired and re-reviewed at its new exact head;
  current success and development suites plus hosted CI are green but do not cover terminal
  ownership changing between capture and assignment.

- 2026-10-07T23:38:17+00:00: Claimed by codex-ar1727-p1-repair.

- 2026-10-07T23:39:45+00:00: Recorded command exit 2; command argv SHA-256
  ff9297d17c0732874297929773bce1e7f679caddd77de7a11179d73b2a300879.

- 2026-10-07T23:41:18+00:00: Recorded command exit 0; command argv SHA-256
  329cfaab5497eb08c4eba0e21fb9bac6fe08f011863f70db6045184762a32cfe.

- 2026-10-07T23:41:52+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-07T23:42:28+00:00: Recorded command exit 0; command argv SHA-256
  8114a6f745a29526f4bf4122ace0f8efbd71bec84ffbec019f15120d6c058f56.

- 2026-10-07T23:43:00+00:00: Recorded command exit 101; command argv SHA-256
  0f50b755977151fcac363d0652f91bcdc391b62a5b332583e13356809b0b347d.

- 2026-10-07T23:43:36+00:00: Recorded command exit 0; command argv SHA-256
  38f6e5d1baf7baec0b118bfa81303e0bb46f914855a714205751aa9ef9b236b4.

- 2026-10-07T23:44:08+00:00: Recorded command exit 0; command argv SHA-256
  c3699fc1b8efb9be2369b056d9961b5f56728cd33639780a266f0a7014536608.

- 2026-10-07T23:44:44+00:00: Recorded command exit 0; command argv SHA-256
  0f50b755977151fcac363d0652f91bcdc391b62a5b332583e13356809b0b347d.

- 2026-10-07T23:45:15+00:00: Recorded command exit 0; command argv SHA-256
  4e2ec95e86bbdfc43c8b630cb9dfe2bc66d915f0441d5685bba9470486aff196.

- 2026-10-07T23:46:16+00:00: Repaired the P1 foreground race in the isolated PR #500 worktree:
  assignment now blocks SIGTTOU, revalidates the captured caller foreground group immediately before
  tcsetpgrp, restores the prior mask on all paths through an RAII guard, and restoration only
  replaces the exact assigned child group or accepts an already-restored caller group. A
  deterministic real controlling-PTY launch regression changes foreground ownership between capture
  and assignment, verifies typed development_terminal_unavailable, preserves the intervening owner,
  reaps the launched group, and removes broker state. The new test and Clippy -D warnings pass;
  continue full relevant gates, signed commit, push, and fresh independent review.

- 2026-10-07T23:48:02+00:00: Recorded command exit 0; command argv SHA-256
  722f17f3639258310af15b497a1d4e65160d6373081d0f45a79aee0a7e580a03.

- 2026-10-07T23:48:35+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T00:00:25+00:00: Recorded command exit 0; command argv SHA-256
  2fa3f3fae6bd0e812da5618f94099d26ff4c3c62a9c6579bae3ed3693904d3f5.

- 2026-10-08T00:01:10+00:00: Recorded command exit 0; command argv SHA-256
  79da272f7e4e7a786ca90e5ea99a1b051339fd1ac5cd8d61b67c8ebfbc695ad8.

- 2026-10-08T00:01:47+00:00: Recorded command exit 0; command argv SHA-256
  ccddac8fd2e77fa49c0709e2997277873753d5b1ea427d766e348f4e699badea.

- 2026-10-08T00:02:16+00:00: Recorded command exit 0; command argv SHA-256
  b3f5e011e60ef5c71bfa91e4f8731ef42e7b810feada2a1609cb8929c8a8ce65.
