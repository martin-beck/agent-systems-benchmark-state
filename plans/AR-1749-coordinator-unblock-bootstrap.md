# AR-1749 plan: canonical Coordinator unblock vendor bootstrap

## Bootstrap invariant

Canonical ASB-state main must never be mutated by lifecycle code that has not
first passed the repository's normal review and merge boundary. AR-1747 cannot
use `unblock` because main's current vendor lacks it; a topic-local invocation
would combine an unreviewed tool installation with an authoritative state
transition. This AR is independently claimable with the installed Coordinator
and owns only the reviewed vendor bootstrap. AR-1747 remains blocked and PR
#106 remains unmerged until this AR completes.

## Exact upstream input

- Repository: `martin-beck/agent-workflow-coordinator`.
- Development merge: `113dc61029f0e0c57bc7832e1e41430eafa17e73`.
- Tree: `45ae6988ccd1c88230f262d735ff24d9d9b3bc4b`.
- Upstream independently reviewed head/tree: `7314d02311487904b3fe66b38f0f98da27a14d62` /
  `45ae6988ccd1c88230f262d735ff24d9d9b3bc4b`.
- Development vendor-manifest SHA-256:
  `02149740b14a554d784e2f0fd8572a67dbf3faabe379fc39b4e9703de74e9936`.
- Post-merge Formal run `37824043227` and Verify run `37824043261`, both
  successful.

## Implementation

1. Claim AR-1749 from a clean exact canonical state main and create an isolated
   topic worktree. Rebuild the topic from current `origin/main`; do not rebase
   stale PR #106 state records or carry its in-progress AR-1747 lifecycle copy.
2. Run the official upstream `sync-development` path against the exact merge
   above. Verify every declared path, byte, mode, commit, tree, version/channel,
   and manifest digest. No vendored file may be patched downstream.
3. Preserve ASB-owned policy through the upstream project-bound
   `task-spec-policy.json` contract. The five additive evidence classes
   `hosted`, `offline`, `privacy`, `journey`, and `quality` must validate through
   task-spec checks, render, doctor, lifecycle preflights, Git and SQLite paths,
   migration, and rollback without replacing the upstream default vocabulary.
4. Keep only downstream-owned integration repairs outside the exact vendor set:
   route `TLC_ADMISSION_QUEUE` and `TLC_ADMISSION_LOCK` below the existing
   private run-id runtime root; use privacy-scanner-safe constructed fixture
   identifiers in ASB-owned tests. Do not add broad scanner exemptions.
5. Prove `handoffctl unblock` rejects wrong task/revision/status, fabricated or
   missing external evidence, stale sessions, and concurrent mutation, and that
   it can transition an isolated externally blocked fixture without requiring a
   pause snapshot. Do not invoke it on live AR-1747 before this PR is merged.
6. Run vendor verification, task/spec/schema validation, privacy and size
   scans, source headers, Ruff format/lint, strict mypy, full branch-aware
   tests under the repository's configured coverage threshold, formal portable
   and required-cgroup tiers, deterministic projections, and clean-tree checks.
   Record exact percentages without representing rounded output as literal.
7. Obtain independent exact-head technical review from a separate worker and
   isolated checkout. The reviewer must validate exact vendor closure, policy
   behavior, downstream path ownership, lifecycle safety, formal evidence,
   signature/DCO, and the absence of task-state/history drift.
8. Replace or close stale PR #106 without merging its old state history. Publish
   one clean PR from current main, wait for every exact-head required check,
   construct the signed DCO two-parent merge locally with the reviewed tree,
   and push only with an exact target-ref lease.
9. Watch every exact-main post-merge state workflow to terminal success. Verify
   remote merge parents, tree, signature, DCO, vendor identity, generated views,
   clean state, and `doctor --live`.

## Handoff to AR-1747

After this AR is terminal done, use canonical main's installed
`tools/handoffctl unblock AR-1747 --expected-revision 27` with a bounded note
identifying the exact merged vendor and green post-merge evidence. Then claim
AR-1747, verify its original adoption obligations are satisfied by the exact
canonical handoff, close/replace stale PR #106, and release it done. No pause
snapshot may be fabricated and no direct task edit is permitted.
