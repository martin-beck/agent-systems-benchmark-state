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

Omit `--status-view` if the project has no `STATUS.md`. Omit `--commit-signoff` if DCO trailers
are not project policy. Commit both binding files with the vendor snapshot. There is deliberately
no rebind command: create a fresh state repository and initialize it separately.

Copy `examples/project/runtime-config.example.json` upstream to `.runtime/config.json`, replace
placeholders locally, and never commit it. The configured product repository must match the
tracked binding.

## Normal user and agent loop

1. Read the project's development policy, complete snapshot, selected task and plan.
2. Claim one dependency-ready open task with a stable unique owner.
3. Run every state-changing product, Git, review or publication command through `run`.
4. Record each material result immediately; heartbeat before lease expiry.
5. After interruption, inspect revisions, commits, refs, processes and CI before retrying.
6. Release to `done`, `open`, or `blocked`; reconcile and run the live doctor.

```sh
tools/handoffctl snapshot
tools/handoffctl claim AR-0001 --owner worker-unique --lease-minutes 120
tools/handoffctl run --owner worker-unique AR-0001 -- command arg
tools/handoffctl update AR-0001 --owner worker-unique --expected-revision 2 \
  --note "Verified result and exact next action"
tools/handoffctl release AR-0001 --owner worker-unique --status done \
  --note "Integrated and verified"
tools/handoffctl reconcile --commit --push
tools/handoffctl doctor --live
```

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

Use `promote` only for `planned -> open` after dependencies complete. Use `resume` only for
`blocked -> open` after independently verifying the external blocker. Both require the exact
current revision. Use `recover-expired` instead of impersonating the prior owner with `release`
when another process recovers an abandoned claim:

```sh
tools/handoffctl recover-expired AR-0001 --expected-revision REVISION \
  --note "UTC expiry and absence of the previous worker independently verified"
```

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

## Proof boundary

The bundled TLA+ models exhaustively check bounded transition, reader/writer lock, and project
binding abstractions. They do not prove Python, Git, Linux, NFS, arbitrary commands,
non-cooperating writers, malicious source edits, or power-loss atomicity. Read
`formal/handoffctl/README.md` before making stronger claims.
