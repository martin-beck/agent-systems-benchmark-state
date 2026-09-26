# AR-1469: AR-1392 protected-main topology repair

## Objective

Repair the invalid protected-main topology produced when PR #339 was merged as
a single-parent commit, while preserving the already-reviewed AR-1392 code and
all prior evidence.

## Required evidence

- Preserve PR #339 head `78ab92bdb87645ac5567fb3341b1b0b73dba5029`, merge
  `3cd6a5a84493842e402dff55e1c2c266f2454752`, and Repository Quality failure
  `36279474851` as immutable evidence.
- Produce a signed+DCO repair topic and a normal two-parent protected merge with
  current `main` as first parent and the reviewed AR-1392 tree as second parent.
- Require exact-head checks, independent review, and all seven post-merge
  workflows on the repair merge. Do not alter implementation behavior or skip
  policy.

## Boundaries

No asb-tui changes, live-provider access, formal seed use, squash merge,
protected-history rewrite, or repository-policy weakening. The repair must be
the smallest topology-only descendant that preserves the AR-1392 tree.
