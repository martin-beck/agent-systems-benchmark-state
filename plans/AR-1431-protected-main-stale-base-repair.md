# AR-1431: Protected-main stale-base merge requalification repair

## Objective

Repair the protected-main integration boundary exposed by AR-1216 post-merge
run `36066329347`.  A pull request reviewed against one protected-main commit
must not be merged after the target advances unless the exact two-parent merge
tree is freshly reviewed and requalified.  The repair must prevent a stale-base
merge from reaching main or make the expected merge tree explicit and
fail-closed at every publication and post-merge policy check.

## Scope

Reproduce the sequence `d9eb6c2 -> 8d1889b -> e82e2e6` and the policy diagnostic
that the protected-main merge tree differs from the reviewed topic tree.
Inspect the integration helper, repository policy, workflow range identity, and
tests.  Prefer rejecting a stale PR base and requiring a fresh exact-base
qualification/review before publication.  If policy compares a merge result,
bind it to the exact reviewed base/head pair and record the merge-tree identity;
never weaken the protected-main gate or accept an unreviewed result.

## Dependencies

- AR-1427 (initial merge-preview repair)

## Acceptance

- A deterministic regression reproduces the stale-base sequential merge and
  fails before publication, with the exact base/head/tree diagnostic recorded.
- The integration and policy paths agree on the same reviewed base, topic head,
  merge parents, and tree; target advancement invalidates prior qualification.
- A fresh rebase/requalification path is tested positively; stale-base,
  target-advance, conflict, tree-mismatch, and missing-review cases fail closed.
- Existing signature, DCO, exact-head CI, no-force-update, and post-merge gates
  remain intact.  Independent review and all seven post-merge workflows must
  pass before release.
