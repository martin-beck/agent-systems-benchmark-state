# Extending the coordinator

## Downstream extensions

Keep these in the consuming state repository:

- task-schema constraints and additional metadata;
- project worktree/branch naming rules;
- development, verification and publication policy;
- extra read-only reports derived from task data;
- project-specific tests and CI integration.

A downstream extension must not bypass the repository-common coordinator lock, alter task files
during a read, mutate generated files directly, or monkeypatch a vendored module in production.
Prefer a separate deterministic command that consumes snapshots when the existing optional status
view is insufficient.

A project may extend only the task-spec evidence vocabulary with a tracked
`task-spec-policy.json` at the bound state root. The schema is
`schema/task-spec-policy.schema.json`. The version-1 file contains only
`schema_version` and `additional_evidence_classes`; additions are lowercase
hyphenated identifiers and cannot duplicate, remove, or reinterpret a built-in
class. The Coordinator rejects untracked, dirty, oversized, symlinked, replaced,
or malformed policy files before lifecycle effects. Environment variables,
runtime configuration, command arguments, home directories, and network input
cannot select another policy.

## Upstream extensions

### Predicate evidence ledger

Spec-bound tasks may use `handoffctl accept --predicate ID --candidate-ref PATH`
with `--candidate-digest` and the evidence artifact's `--evidence-ref` and
`--evidence-digest`.  Both references are bounded repository-relative regular
files and their SHA-256 digests are verified before the transition commits.
Every accepted predicate is bound to the current candidate.  Recording a new
candidate requires `--reopen`; existing passing predicates become `stale` and
must be accepted again for the new candidate before `release --status done`.
This proves artifact identity and binding only, never the semantic correctness
of arbitrary evidence.  `snapshot TASK` emits `NEXT_UNMET_STEP` when a
specification still has a predicate without current-candidate passing evidence.

### Assumption revalidation

`handoffctl assumption` records an opt-in, bounded history for inputs whose
freshness matters to a task. A declaration names a `base` Git HEAD, a
dependency task revision, or a regular-file `observation`, and explicitly
chooses `--material` or `--non-material`. The Coordinator compares each active
material binding before `accept` and `release --status done`. A changed binding
requires either `assumption revalidate` (which records the new binding) or
`assumption dispose --reason ...`; non-material assumptions remain visible but
never block these transitions. This is a local developer workflow control, not
an authentication, signature, or reviewer gate.

An installation may also opt into `autonomy-limits-policy.json` at the bound
state root. Its version-1 schema declares one or more bounded maxima for elapsed
time, retries, commands, local diff size, self-reported cost units, and declared
external side effects. The file is a tracked, clean, regular Git blob; a missing,
replaced, dirty, oversized, or malformed policy rejects command admission.
Limits are workflow controls, not authentication or approval controls. A breach
records a privacy-safe diagnostic hold on the current task revision. The active
owner can clear that exact hold with `autonomy-limits dispose` and a concise local
reason; no signature, account, external service, or reviewer is involved.

Change upstream when behavior affects:

- lifecycle transitions, ownership, revisions or dependencies;
- lock acquisition, timeouts or transaction rollback;
- command execution/recording and replication;
- project binding or trusted identity;
- the tracked profile schema;
- a common generated view or vendor format.

An upstream change needs unit and multiprocess fault tests, compatibility fixtures for all known
profiles, documentation, and a version bump. Update TLA+ whenever the abstract transition, lock,
binding, safety or liveness contract changes.

Storage implementations conform to the `Backend` protocol in `sqlite_storage.py`: load one
consistent task snapshot and durably append command evidence. Mutations must preserve the shared
lifecycle functions, exact-revision semantics, permanent binding and deterministic projection.
New embedded or server backends require schema migration, crash recovery, independent-process
stress tests and updated best-effort model guidance where useful; executable
downstream backend plugins are not supported.

## Compatibility rules

- Patch releases preserve CLI, record and profile schemas.
- Minor releases may add backward-compatible commands or optional profile fields.
- Major releases may intentionally migrate schemas and require a documented downstream procedure.
- Vendor sync never changes the downstream profile or binding.
- Vendor sync and upgrade never change `coordinator.backend.json` or create a SQLite database.
- A consuming repository pins one exact tag and commit; ranges and floating branches are forbidden.
- Bug-for-bug compatibility is not required for behavior documented as a defect, but the release
  notes and regression tests must name the correction.

## Adding a profile capability

Propose the smallest deterministic setting, define its type and default, update both JSON Schema and
runtime validation, add enabled/disabled tests, document its effect, and verify it cannot weaken the
binding or concurrency contract. Avoid executable plugin paths in tracked configuration: importing
arbitrary project code into the mutation process would enlarge the trusted computing base.
# Audited predicate-ledger repair

`repair-predicate-ledger` is a narrow recovery transition for a completed,
inactive, unowned task whose predicate evidence must be refreshed after
acceptance. It requires the exact task revision, an explicitly named predicate,
a *new* candidate and freshly matching evidence digest, and a bounded reason.
The transition appends one passing correction row and marks only the prior
matching passing row stale. Every retained historical row is copied unchanged,
including rows that are no longer locally reconstructible; the fresh candidate,
predicate, evidence class, reference, and digest are still validated strictly.
Active, owned, stale-revision, malformed-target, symlink, traversal, same-
candidate, or digest-mismatched requests fail closed. Ordinary `accept` remains
owner- and active-task-bound and does not inherit this repair exception.
