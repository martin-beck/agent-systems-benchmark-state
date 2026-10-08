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
