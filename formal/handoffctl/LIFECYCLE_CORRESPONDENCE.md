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

## Legacy task-spec binding

`bind-spec` is modelled as an owner and exact-revision-fenced active-task
transition.  It is admitted only when the lease is live and the task is still
unbound; an accepted transition makes `specBound` true, while stale, expired,
foreign-owner, or already-bound requests take `ExecuteReject(p)` and stutter.
`SpecBindingIsMonotonic` and `AcceptedSpecBindIsBound` make the one-way
binding property explicit.  This is bounded-model guidance and hostile test
correspondence, not a proof that the Python implementation refines the model.

## Legacy worktree binding

`bind-worktree` is the corresponding exact-revision transition for a claimed
legacy record with both worktree fields empty, or with an empty branch and a
valid predeclared worktree key matching the request. It requires a live owner
lease, rejects unsafe, conflicting, mismatched, or branch-only partial
identities, and changes the bounded
`worktreeBound`, branch, and worktree-key states only on acceptance. A retry
at the immediately resulting revision with the same owner and exact identity
is an accepted no-op: it preserves task/projection revisions and records no
second mutation. A different identity remains rejected.
`WorktreeBindingIsMonotonic`, `AcceptedWorktreeBindIsBound`, and
`UniqueActiveWorktreeIdentity` preserve the one-way binding and prohibit two
active tasks from sharing either bounded identity, while timeouts, stale
requests, expired leases, and conflicting requests stutter.
The model includes an empty legacy record and a record with one predeclared
matching worktree key; it does not model arbitrary pre-existing identities.
Hostile tests cover the branch-only and mismatched-key rejections.
This is bounded-model guidance and hostile test correspondence, not an
implementation-refinement proof.

The executable checker binds this vocabulary to the authoritative predicates:
`NoReplacementBeforeBackup` to `ProjectionAtomicity`, `AmbiguousIsWriteClosed`
to `LockSafety`, and `ReconcileRequiresFence` to `RevisionAccounting`. It also
records SHA-256 hashes of `Handoffctl.tla` and `Handoffctl.cfg` with each trace.
