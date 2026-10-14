# Embedded project guide

This guide travels with every vendored release so users and agents can operate it offline. The
canonical project is <https://github.com/martin-beck/agent-workflow-coordinator>.

## What is bound to a project

Initialization creates three tracked files:

- `.handoffctl.json`: non-secret identity and presentation settings.
- `coordinator.binding.json`: an immutable project UUID plus state and product repository IDs.
- `coordinator.backend.json`: the project-bound authoritative backend (`sqlite` or `git`).

Every command after `init` verifies the profile UUID, state checkout root and origin, product
identity from private runtime configuration, product checkout origin, and the caller's current
working directory. Calls from another project fail before locking or reading/mutating task status.
The binding is an accidental-misuse boundary, not protection against someone who deliberately
rewrites the coordinator source, Git history, and binding files.

## Files in an integrated state repository

- `.runtime/config.json`: ignored, mode 0600, with machine-local paths and optional push.
- `.runtime/coordinator.sqlite3`: ignored SQLite WAL authority for default-backend projects.
- `tasks/`: Markdown records with strict JSON front matter.
- Hierarchical task records may set `parent_task_ref` and the reciprocal `children` list. Both
  sides are required to name existing tasks, edges must be acyclic, and a parent cannot release
  to `done` while any child is non-terminal. The task-record schema is
  `schema/task-record.schema.json`.
- `plans/`: detailed plans referenced by tasks.
- `CURRENT.md`: deterministic compact queue; never edit directly.
- `STATUS.md`: optional deterministic portfolio view or, for large projects, a compact index to
  generated `status/STATUS-####.md` pages; never edit directly. The linked pages together contain
  the complete graph, dependency index and AR inventory.
- `PROJECT_STATE.md` and `WORKTREES.md`: generated live observations.
- `coordinator.vendor.json`: upstream version, commit and SHA-256 for every vendored file.
- Optional `task-spec-policy.json`: a tracked version-1 project policy that
  adds a bounded evidence-class vocabulary without changing the five built-in
  classes. Validate it with `schema/task-spec-policy.schema.json`; the file
  must remain clean, regular, state-root-bound, and non-symlinked.
- `sessions/AR-####.jsonl`: bounded, content-minimized session snapshots. Each record stores
  only a context digest, step state, safe artifact references and the next action; raw prompts,
  logs and command output are never retained. The latest record can be replayed with
  `tools/handoffctl snapshot --task AR-####`.
- `checkpoints/AR-####.jsonl`: bounded task checkpoints. Each record stores task metadata,
  artifact references, a body digest and the signed source commit; raw command output is never
  retained. Create one with `tools/handoffctl checkpoint AR-#### --owner OWNER
  --expected-revision REV`.
- `rollbacks/operations.jsonl`: bounded rollback journal. Planned, restore-started, completed and
  ambiguous states are durable; an ambiguous operation must be reconciled before retrying.
- `directives/records.jsonl`: bounded board-directive journal. Each revision carries its authority,
  precedence, role/task scope, lease and lifecycle. Equal-precedence overlapping active directives
  are rejected unless they are escalated to guidance AR-0053.

## Initialize exactly once

Run from the state repository root after vendoring and before any other command:

```sh
tools/handoffctl init \
  --state-repository OWNER/STATE_REPOSITORY \
  --product-repository OWNER/PRODUCT_REPOSITORY \
  --project-name example-project \
  --project-title "Example Project" \
  --status-view \
   --commit-signoff
```

This defaults to SQLite WAL. Add `--backend git` to retain Markdown/Git authority. Normal SQLite
commands work without `.runtime/config.json`, GitHub CLI or network access. Runtime configuration is
needed only for product-checkout calls, live observations, or optional publication.

Existing initialized projects without `coordinator.backend.json` remain Git-backed after upgrades.
Never manufacture that file to migrate; use `handoffctl migrate --to sqlite`, verify the database
and projections, and retain the Git files for the documented `migrate --to git` rollback.

## Concise task titles

Task records may carry an optional `short_title`: one to four human-readable words used beside
the task ID in operator-facing views. `title` remains the full durable description. During the
v0.5 compatibility window, records without `short_title` render their full title after the ID and
remain valid; the coordinator never derives or writes a short title while reading a record.

Migrate a Git-backed project in one reviewable state change: add a valid `short_title` to each
task front matter, regenerate `CURRENT.md` and `STATUS.md` with `render-status`, then require
`render-status --check` and `doctor` in the state PR. For SQLite authority, use the supported
`migrate --to git` export, apply and review that same mapping in Git, then `migrate --to sqlite`;
the migration equivalence check must preserve the distinct field. Before the next schema-major
release, the project must explicitly either complete that mapping or retain the v0.5 compatibility
policy; a future required-field change must reject missing titles during validation rather than
silently inventing them.

Omit `--status-view` if the project has no `STATUS.md`. Omit `--commit-signoff` if DCO trailers
are not project policy. Commit both binding files with the vendor snapshot. There is deliberately
no rebind command: create a fresh state repository and initialize it separately.

Copy `examples/project/runtime-config.example.json` upstream to `.runtime/config.json`, replace
placeholders locally, and never commit it. The configured product repository must match the
tracked binding.

## Normal user and agent loop

Local reproducible functional and privacy evidence is sufficient for normal
development integration and release. External signatures, authentication,
GitHub approval, and independent review may supplement that evidence but are
not lifecycle, merge, or release prerequisites; see
[`DEVELOPMENT_REVIEW_POLICY.md`](DEVELOPMENT_REVIEW_POLICY.md).

1. Read the project's development policy, complete snapshot, selected task and plan.
2. Claim one dependency-ready open task with a stable unique owner.
3. Run every state-changing product, Git, review or publication command through `run`.
4. Record each material result immediately; heartbeat before lease expiry.
5. After interruption, inspect revisions, commits, refs, processes and CI before retrying.
6. For `done`, record locally verifiable task-spec acceptance at the exact
   current revision; supplementary review is optional.
7. Release to `done`, `open`, or `blocked`; reconcile and run the live doctor.

```sh
tools/handoffctl snapshot
tools/handoffctl claim AR-0001 --owner worker-unique --lease-minutes 120
tools/handoffctl bind-envelope AR-0001 --owner worker-unique --expected-revision 2 \
  --envelope-ref envelopes/AR-0001-e1.json --envelope-revision 1
tools/handoffctl preflight AR-0001 --owner worker-unique --command-class source-write \
  --scope-path tools --json
tools/handoffctl run --owner worker-unique --command-class source-write --scope-path tools \
  AR-0001 -- command arg
tools/handoffctl update AR-0001 --owner worker-unique --expected-revision 2 \
  --note "Verified result and exact next action"
tools/handoffctl accept AR-0001 --owner worker-unique --expected-revision 3 \
  --evidence-class contract-test --evidence-ref quality/AR-0001-tests.txt \
  --evidence-digest sha256:YOUR_EXACT_64_HEX_DIGEST \
  --note "Accepted task spec against reviewed evidence"
tools/handoffctl release AR-0001 --owner worker-unique --status done \
  --note "Integrated and verified"
tools/handoffctl reconcile --commit --push
tools/handoffctl doctor --live
```

Workers that need snapshotless expired-claim recovery pass their live Linux PID and start-time
with `claim --worker-pid PID --worker-start-time START_TIME`. Coordinator verifies that exact
identity at claim time and later recovers only after it is absent.

`accept` records the active owner's acceptance assertion for the task's referenced
spec and validates the metadata. It does not independently inspect or prove the
evidence contents; project review and evidence-class obligations still apply.
The `done` release gate remains fail closed when acceptance is missing or invalid.

## Change-drift guard

Use `change-drift baseline` before source work, then `change-drift delta` before completion.
The baseline and delta preserve Git rename pairs and generated-file markers without touching the
worktree. Every changed path remains material until it is explicitly explained; generated output is
not silently exempt. `explain` and `rescope` require the active owner and exact task revision, so a
concurrent lifecycle change cannot be overwritten.

```sh
tools/handoffctl change-drift baseline AR-0001 --owner worker-unique --expected-revision 2 \
  --scope-path tools --scope-path tests
tools/handoffctl change-drift delta AR-0001 --owner worker-unique --expected-revision 3
tools/handoffctl change-drift explain AR-0001 --owner worker-unique --expected-revision 4 \
  --path build/output.generated --generated --reason "Documented local build output"
tools/handoffctl change-drift rescope AR-0001 --owner worker-unique --expected-revision 5 \
  --scope-path tools --scope-path tests --scope-path docs
```

Both the Git task record and the SQLite task row carry the same bounded canonical history. A task
cannot transition to `done` while its latest delta has material paths without matching explanations.

An execution envelope is an optional, immutable, revision-bound task contract. Once bound, every
`run` must declare an allowed command class and, for mutations, at least one allowed scope path.
`preflight` gives a machine-readable explanation without changing state. The bound envelope is the
durable authority and its write paths are enforced by a Bubblewrap sandbox; `--scope-path` remains
an auditable admission declaration and cannot expand that envelope-wide write capability. Commands
without a mutating class receive no writable project path. Before a bound command starts,
`handoffctl` commits a revision-CAS execution fence carrying the owner, envelope digest,
command class, scope digest, argv digest, and deadline. With replicated Git authority, workers
begin only after that mutation has been pushed; competing clones therefore fail before launching a
subprocess. Lifecycle changes
cannot bypass either live or expired execution fences. An expired execution fence normally requires the explicit
`recover-execution` path, which independently verifies the claim worker has exited and the exact durable
command-result evidence exists before clearing it. If no matching result can be recovered, a state-root
operator may use `abandon-execution` only with the exact current revision and execution ID, an expired
execution fence, an absent claim worker, and a local evidence reference plus digest. It rejects a matching
result, retains a bounded structured abandonment audit record, and appends the normal immutable state
history; it does not edit task files directly or authorize a live worker. This is a safety fence, not a remote kill switch: a worker that loses authority must terminate
its subprocess, and strict cross-host fencing still requires a target-side gateway.

Execution envelopes are offline by default. A version-2 envelope may explicitly grant the
`git_metadata` and `network` capabilities, but only `git-publication` may use them. The network
capability also requires the invocation flag `--authorize-external-side-effects`; the sandbox then
mounts only the admitted worktree metadata (`.git`) read-only and shares the caller's network.
Version-1 envelopes and all read, test, and source-write commands retain the isolated network-denied
behavior. Missing, partial, or ambiguous capability declarations fail closed.

Restore a verified checkpoint only from a clean descendant product checkout:

```sh
tools/handoffctl rollback --checkpoint AR-####-r####
tools/handoffctl rollback --checkpoint AR-####-r####
tools/handoffctl rollback --checkpoint AR-####-r#### --reconcile
```

Create and transition a directive with exact ownership and revision fencing:

These commands are currently available for the Git authority backend; AR-0083
tracks the corresponding SQLite migration and doctor coverage.

```sh
tools/handoffctl directive create --directive-id UD-0001 --authority BOARD-001 \
  --precedence 10 --role-scope implementer --statement "Preserve the release boundary." \
  --owner BOARD_OWNER
tools/handoffctl directive transition UD-0001 activate --owner BOARD_OWNER \
  --expected-revision 1
tools/handoffctl directive list --lifecycle active
```

An overlapping directive at the same precedence cannot become active. Supplying
`--guidance-ref AR-0053` records it as `escalated` instead, leaving the conflict
visible for board guidance resolution.

`--reconcile` is required only after a rollback is recorded as `restore_started`
or `ambiguous`. It may continue only when the product checkout is at the exact
durable rollback head (or at the previously recorded pre-rollback head when no
product commit was published); otherwise the operation remains fail-closed.

Use `promote` only for `planned -> open` after dependencies complete. Use `resume --session` only
to restore a task from one unique, coherent pause record at that exact task and revision. Duplicate,
cross-task, or internally inconsistent history fails closed. After independently verifying an external blocker,
use `unblock` on a task that reached `blocked` through `release --status blocked`; it preserves the
current `next_action` and creates no session snapshot. These commands require the exact current
revision and reject cross-mode provenance. Use `recover-expired` instead of impersonating the prior owner with `release`
when another process recovers an abandoned claim:

```sh
tools/handoffctl recover-expired AR-0001 --expected-revision REVISION \
  --note "UTC expiry and absence of the previous worker independently verified"
tools/handoffctl unblock AR-0002 --expected-revision REVISION \
  --note "External blocker and exact revision independently verified"
```

Pre-identity task records have no durable worker identity to inspect. They remain fail closed by
default, but an operator can use the one-time compatibility route only after confirming the record
has no `claim_process` field and its lease has expired:

```sh
tools/handoffctl recover-expired AR-0001 --expected-revision REVISION \
  --allow-legacy-without-identity \
  --note "Legacy worker identity was never recorded; recovery is explicitly acknowledged"
```

The resulting task history is prefixed `LEGACY_NO_IDENTITY_RECOVERY`; it is an audit marker, not
evidence that the former worker was observed absent.

A future or malformed deadline and a stale revision are rejected before mutation.

Dependencies normally require status `done`. A task with status `superseded` can satisfy a
dependency only when its optional `superseded_by` field names an existing task (or finite chain of
such tasks) ending in a task with status `done`. Missing, malformed, cyclic, or unfinished
successors remain unsatisfied; old superseded records without this field therefore fail closed.

On the Git backend, recover expired claims one at a time even when several leases elapsed. An
unrelated expired claim or pre-existing repository privacy/size finding does not block a valid
lifecycle transition, but it remains a strict `doctor` error until remediated. A transition still
fails and rolls back if its resulting target or global active keys are invalid, or if it introduces
a new privacy/size finding in a file it writes.

## Extend safely

Do not patch vendored files. Project-specific task fields and constraints belong in the downstream
schema and tests. Project process belongs in its development policy. The supported runtime profile
only controls identity, optional status output, and commit signoff. A new core hook requires an
upstream proposal, contract tests, formal-model review when it changes transitions or concurrency,
and a new version.

## Upgrade and verify offline

Use a clean checkout at an exact upstream release tag:

```sh
python /path/to/agent-workflow-coordinator/tools/vendor.py sync \
  --source /path/to/agent-workflow-coordinator \
  --target /path/to/project-state \
  --version v0.3.5
python tools/handoffctl_vendor.py verify --target .
```

Sync stages the complete file set before rollback-capable rename installation. It never copies or
regenerates the project profile or binding. Review the full vendor diff and run project integration
tests before committing. On interruption, inspect the manifest, hashes, refs, release and CI before
retrying.

For development integration from an untagged Coordinator head, use the explicit development-only
path with a full immutable commit identifier:

```sh
python /path/to/agent-workflow-coordinator/tools/vendor.py sync-development \
  --source /path/to/agent-workflow-coordinator \
  --target /path/to/project-state \
  --commit FULL_40_CHARACTER_HEAD_COMMIT
```

The source must be clean and its `HEAD` must equal the requested commit. The resulting schema-v2
manifest is explicitly classified as `development` and binds the exact Git tree plus every vendored
file digest. It is not release evidence. Normal `sync --version vMAJOR.MINOR.PATCH` behavior remains
tag-bound and emits the existing schema-v1 release manifest.

The vendor boundary includes the complete first-party Coordinator formal
verification closure: lifecycle, binding, lock, run, storage, recovery and
interaction-gate models/configurations; the verifier, runner, attestation
helper; and evidence metadata. Vendor verification rejects runtime/model
operation drift. Additional qualification models and launchers owned by
downstream quality projects remain downstream-owned and are not overwritten.
An empty-destination vendor diagnostic may supply the paired absolute
`--diagnostic-queue` and `--diagnostic-admission-lock` verifier flags. That execution is explicitly
noncanonical (`diagnostic-private-admission`) and cannot support publication or release claims;
normal hosted verification continues to use the shared canonical admission path.

## Proof boundary

The bundled TLA+ models exhaustively check bounded transition, reader/writer lock, and project
binding abstractions. They do not prove Python, Git, Linux, NFS, arbitrary commands,
non-cooperating writers, malicious source edits, or power-loss atomicity. Read
`formal/handoffctl/README.md` before making stronger claims.
