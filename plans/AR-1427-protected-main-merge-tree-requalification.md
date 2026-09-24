# AR-1427: Protected-main merge-tree requalification repair

## Objective

Repair the coordinator merge/requalification path after AR-1215 PR #310
merged onto AR-1214's newer protected main and post-merge Repository Quality
rejected merge `f511645` because its protected merge tree differed from the
reviewed topic tree. Preserve sequential merges without weakening exact-tree
or policy gates.

## Dependencies and scope

- Depends on completed AR-1421's existing protected-main repair baseline.
- Incident input is AR-1215 PR #310 and post-merge run 36060277237.
- Coordinator/integration boundary only; no tutorial semantics, provider
  behavior, native evidence, or `asb-tui` changes.

## Acceptance

1. Reproduce the exact base/topic/merge-parent/tree mismatch from PR #310 and
   distinguish a valid sequential merge from a stale or tampered topic.
2. Make merge admission compare the reviewed topic tree with the exact tree
   that would result from the current protected target and record both parent
   identities. If the target advances, require fresh exact-head qualification
   or fail closed before publication.
3. Add positive and hostile regression tests for sequential merges, target
   advancement during publication, stale topic refs, altered merge trees, and
   cancelled post-merge checks. No commit-specific allowlist or skipped gate.
4. Requalify the AR-1215 merge incident and rerun all seven exact-main
   post-merge workflows for the corrected integration evidence. Keep AR-1215
   unreleased until Repository Quality, aarch64, Rust, and all other required
   workflows are terminal-success.
5. Use signed+DCO commits, independent diff review, exact-head CI, and durable
   state evidence. No live provider, network acquisition, native host, or
   signed bundle is required for development tests.

## Non-goals

Do not modify workload/tutorial behavior, suppress the protected-main policy,
rewrite historical failures, or touch `asb-tui`.
