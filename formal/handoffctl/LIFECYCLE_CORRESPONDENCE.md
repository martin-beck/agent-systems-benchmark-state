# Backup lifecycle correspondence

The backend backup tests exercise an observational lifecycle that maps to the
refinement model without claiming that backup/restore authorizes a transition:

| concrete outcome | model predicate | durable-state requirement |
| --- | --- | --- |
| verified backup and fresh restore | `ExecuteSuccess(p)` | state is unchanged by observation |
| publication or restore fault | `ExecuteReject(p)` | state and destination remain unchanged |
| retry after a fault | a later `ExecuteSuccess(p)` | only the successful operation publishes |

This is an evidence mapping only. The current implementation does not route
backup/restore through the phase machine or execute rollback authorization.

## Project task-spec policy guard

`task-spec-policy.json` is a preflight input, not a new lifecycle state or
transition. The runtime opens it only from the verified state root, validates
its tracked Git identity and bounded additive vocabulary, and carries one
immutable policy snapshot through task/spec validation, done admission,
rendering, Git or SQLite mutation, migration, rollback, and reconciliation.
A missing policy selects the original built-in vocabulary. A malformed,
removed, dirty, replaced, or concurrently changed policy maps to
`ExecuteReject(p)`: no task, session, authoritative backend, or lifecycle
phase changes. Consequently no TLA+ action or default vocabulary changes; the
existing rejection/stuttering invariants remain authoritative.

The correspondence inventory is exercised by `tests/test_task_spec.py`,
`tests/test_handoffctl.py`, and `tests/test_sqlite_storage.py`, including
policy identity races, failed Git mutation restoration, and interrupted
Git-to-SQLite migration before authority selection changes.

The executable checker binds this vocabulary to the authoritative predicates:
`NoReplacementBeforeBackup` to `ProjectionAtomicity`, `AmbiguousIsWriteClosed`
to `LockSafety`, and `ReconcileRequiresFence` to `RevisionAccounting`. It also
records SHA-256 hashes of `Handoffctl.tla` and `Handoffctl.cfg` with each trace.
