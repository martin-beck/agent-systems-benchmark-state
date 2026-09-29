# AR-1526 plan: first-customer local/replay qualification

1. Read the complete product development, architecture, quality and
   orchestration documentation and the six dependency ARs. Reconcile state,
   refs, worktrees and processes before execution.
2. Build from the exact protected-main head in an isolated clean worktree and
   run the repository's focused/full Rust, CLI, formal, privacy and schema
   gates.
3. Start the bounded control service with the explicit local/mock authority,
   exercise guided setup and a representative multi-agent benchmark, then run
   a strict authenticated replay with network denial. Verify cancellation,
   restart/reconciliation, evidence bounds and teardown.
4. Independently review all generated evidence for credentials, prompts,
   transcripts, private paths and raw provider output. Retain only sanitized
   digests and terminal outcomes.
5. Record exact commit, commands, gate results, runtime outcomes and cleanup;
   leave the AR blocked if any terminal or privacy evidence is missing. Do not
   infer live-provider or first-customer production readiness from this mock /
   replay qualification alone.
