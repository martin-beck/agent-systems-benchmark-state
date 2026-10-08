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

The executable checker binds this vocabulary to the authoritative predicates:
`NoReplacementBeforeBackup` to `ProjectionAtomicity`, `AmbiguousIsWriteClosed`
to `LockSafety`, and `ReconcileRequiresFence` to `RevisionAccounting`. It also
records SHA-256 hashes of `Handoffctl.tla` and `Handoffctl.cfg` with each trace.
