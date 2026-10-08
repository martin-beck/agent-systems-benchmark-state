# AR-1742 protected-main exact-tree recovery

Recover the PR #505 publication-integrity failure without rewriting the
published merge. Preserve `a9abcf2`, base `2f7387e`, topic `e424c39`, reviewed
tree `1aa96736`, and merge tree `befcb782`. Independently review the mismatch,
use the documented signed local integration procedure, and rerun all exact-main
required workflows. Record that AR-1740 follow-up PR #507 is a separate
default-lifecycle product change and does not replace this recovery.

The recovery must remain fail-closed: no history rewrite, policy exception,
unsigned merge, or credential output. Release only after the forward signed
result and every required hosted check are green.
