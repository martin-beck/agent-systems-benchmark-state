# AR-1747 plan: Coordinator unblock vendor adoption

## Incident and source identity

The ASB state repository is pinned to Coordinator v0.3.57 and cannot perform a
supported blocked-to-open transition. `resume` is intentionally limited to
paused tasks with a matching pause snapshot, while ASB AR-1722 is externally
blocked. The required upstream repair already exists at signed development
commit `e863b57edc7f7a21b2aff2c7b45ce226e12637d2`, tree
`eee603591b917eeca244425559d7c67bb88a7268`, including the dedicated `unblock`
command, provenance validation, rollback behavior, and complete formal vendor
closure.

This AR owns only exact Coordinator adoption in
`agent-systems-benchmark-state`. It must use the official upstream
`sync-development` handoff path and must not modify the Coordinator upstream,
ASB product runtime, or AR-1722 by hand.

## Required implementation

1. Re-fetch the official upstream Coordinator repository and verify the exact
   source commit, tree, SSH signature/DCO where applicable, development
   manifest identity, copied-file modes, and SHA-256 digests. Do not source
   files from worker checkouts, downstream copies, mutable tags, or unreviewed
   local branches.
2. Run the official `sync-development` path into a clean isolated ASB-state
   worktree. Adopt the complete declared vendor closure, including runtime,
   schema, migration, rollback, test, formal-model, TLC runner, and manifest
   files. Reject undeclared extras, missing transitive files, mode drift, and
   any generated cache or private runtime artifact.
3. Preserve the ASB immutable project binding, Git/Markdown authority backend,
   task schema, local development-review policy, source-header policy, and
   generated-view contract. Do not create or consult SQLite authority state.
4. Add downstream contract tests for `unblock` that require: status `blocked`;
   exact expected task revision; a distinct recorded blocking event; matching
   task and nested `step_state` identity/status/revision; terminal prior
   in-progress/open lineage; non-empty reason and evidence; atomic Git commit,
   render, and replication; and safe retry/reconcile after an ambiguous push.
5. Add hostile tests rejecting use on paused/open/done tasks, duplicate unblock
   at the same revision, wrong task identity, missing or forged block event,
   mismatched nested status/revision, stale expected revision, dirty state,
   failed render, failed commit, failed push, and rollback/reconciliation
   ambiguity. Prove `resume` remains limited to authentic pause snapshots.
6. Run vendor verification, source headers, formatting/lint/types, schema and
   privacy validation, every ASB-state unit/fault/race/recovery test, unchanged
   95% branch-aware coverage, render-status check, deterministic doctor, and
   the complete declared TLA+/formal tiers from clean destinations. Ensure no
   file over the repository size limit and no `__pycache__`, bytecode, token,
   prompt, private path, or raw transcript is tracked.
7. Publish the state/tooling change as an SSH-signed, matching-DCO pull request.
   Obtain independent exact-head technical review, require hosted Coordination
   verification green, merge without rewriting history, then verify the exact
   merged state head and post-merge hosted run.
8. Release AR-1747 only after its acceptance receipt is bound to the exact
   merged vendor identity. After AR-1746 is also done, use the newly supported
   `handoffctl unblock AR-1722 --expected-revision 80` transition with a concise
   evidence-bound reason; never replace this with direct Markdown editing or a
   fabricated pause session.

## Development policy

This is development adoption, not a verified Coordinator release. Missing
production authentication, release signing, or a second GitHub account cannot
block it. Exact source identity, complete manifest/digests, functional and
formal tests, independent technical-worker review, SSH signature/DCO, hosted
CI, merge identity, and post-merge verification remain mandatory.
