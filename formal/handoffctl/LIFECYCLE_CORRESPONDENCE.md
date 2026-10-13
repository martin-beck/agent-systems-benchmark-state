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
`tests/test_handoffctl.py`, `tests/test_predicate_evidence_ledger.py`, and
`tests/test_sqlite_storage.py`, including
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

## Predicate evidence ledger acceptance

`HandoffctlPredicateLedger.tla` is the bounded model for the predicate-aware
form of `accept`. It keeps `candidateRef` and `candidateDigest` as separate
state variables. Its finite candidate domain is the complete `Refs × Digests`
cross-product: a reference can retain its name while its artifact digest
changes, and two distinct references can identify identical artifact content.
Each accepted predicate row carries that exact pair; a row with either
a different reference or a different digest cannot be live evidence for the
current candidate.

The model uses two workers, two predicates, four candidate identities (the
full two-reference by two-digest cross-product), current and
stale expected revisions, valid and invalid evidence, and both settings of
`--reopen`. `AcceptEnabled` maps to
`predicate_ledger.apply_predicate_acceptance` after bound-spec and evidence
preflight; its owner and `expectedRevision` conditions map to `handoffctl`'s
shared active-owner and revision-CAS checks. `Accept` preserves `status` and
`owner`, advances `revision` once, and writes a passing row bound to the
requested pair.

`CandidateChanged` is admitted only with `requestedReopen`. The separate
`ref_only`, `digest_only`, and `ref_and_digest` change kinds are checked as
invariants, so both same-ref/changed-digest and different-ref/same-digest
counterexamples are included rather than excluded by the bounded domain.
`MarkPassesStale` is the bounded representation of `_historical_steps`: on a
candidate transition it retains well-formed historical rows and changes old
passing rows to `stale` before recording the new pass. The runtime first
validates prospective history and then its final ledger; a malformed row maps
to `Reject` and leaves all modelled durable state unchanged. Subsequent
evidence for the same predicate replaces that predicate's current row,
matching `_record_step`; stale evidence cannot satisfy completion.
`RequestedCandidateHasNoStaleHistory` also rejects reopening an already
retired ref/digest pair, because making its retained stale row current would
violate the ledger validator's candidate-binding rule.

`ReleaseDone` maps to `release --status done` after shared done admission.
`PredicateComplete` requires one live pass for every declared bounded
predicate for the current ref/digest pair.
`CandidateBinding`, `ExplicitReopenOnCandidateChange`,
`StaleEvidenceIsHistorical`, `StaleEvidenceCannotComplete`, and
`DoneRequiresCompletePredicates` are checked at every state. The model is
included in the `pr-publication` and `full-exhaustive` tiers. Concrete
Git/SQLite tests provide hostile file, schema, digest, malformed-history, and
post-write validation evidence outside this finite abstraction.
