# AR-1624 — AWQ/AWC quality and coordination gate

Run the paired implementation and release gates through the current
agent-workflow-quality and agent-workflow-coordinator contracts. Require
isolated worktrees, one AR per worker, exact-head hosted checks, independent
review, durable receipts, reconciliation, and truthful blocked status. Add a
small repair/recovery drill so a failed worker or stale projection cannot be
mistaken for completed wizard functionality.

This gate checks coordination and evidence quality; it does not add production
authentication requirements to the development prototype.
