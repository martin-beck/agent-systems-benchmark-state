# AR-1397: Protected-main post-merge concurrency and tree repair

## Scope

Repair the signed integration and post-merge admission flow exposed by the
AR-1314 merge `c58b0b0a4d9023e3831f9c750edbb9b30ab4bad4` and the AR-1395 merge
`130ff91ec3ac875ac9c370ab67dd9934d830ccdf`. Both merges were reviewed against
one topic tree, but protected-main verification observed a later target state:
Repository quality rejected the resulting merge tree, while Rust verification
was cancelled by subsequent main activity. Preserve every original PR and
post-merge evidence record; do not add hash exceptions, suppress cancellation,
or weaken the merge-tree invariant.

The repair must make the authorized merge operation revalidate the exact target
head, topic head, reviewed tree, parent topology, and required checks immediately
before publication, then serialize the seven post-merge workflows for one exact
merge commit so a later push cannot silently invalidate their evidence. Any
stale target or cancellation remains a fail-closed failure with actionable
durable evidence.

## Acceptance

- A signed+DCO implementation is reviewed independently and adds positive and
  hostile tests for target advancement, competing post-merge pushes, tree
  mismatch, and cancelled exact-merge workflows.
- The exact merge tree, parents, topic head, and protected target are recorded
  and revalidated without private data or one-off commit exceptions.
- All applicable focused/full gates, DCO/signature/privacy checks, exact-head
  PR checks, and all seven exact-merge post-merge workflows reach terminal
  success for a fresh controlled repair merge.
- AR-1314 and AR-1395 retain their original merge evidence and are only closed
  after their required post-merge evidence is truthfully replaced or confirmed.
