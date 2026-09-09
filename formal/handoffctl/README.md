# handoffctl transition and concurrency contract

This directory defines the machine-checked contract for every task-lifecycle
mutation performed by `tools/handoffctl`. The TLA+ model is an abstraction of
the Python implementation, not a replacement implementation.

## Transition contract

Every accepted lifecycle command increments `task_revision` exactly once and validates the result.
For Git authority, the task and generated projections update under the same repository lock and a
detected pre-commit failure restores them. For SQLite authority, one database transaction commits
the task first and generated projections are recoverable output. A rejected command leaves
authoritative revision, task state and owner unchanged.

| Command | Required source | Required actor/revision | Result |
| --- | --- | --- | --- |
| `promote` | `planned`, unowned, dependencies done | exact revision | `open` |
| `resume` | `blocked`, unowned | exact revision | `open` |
| `claim` | `open`, dependencies done | owner has no active task | `in_progress`, lease set |
| `heartbeat` | `in_progress` | current owner, positive lease | lease renewed |
| `update` | `in_progress` | current owner, exact revision | active fields updated |
| `release` | `in_progress` | current owner | chosen non-active state, owner and lease cleared |
| `recover-expired` | expired `in_progress` | exact revision | `open`, ownership cleared |
| `run` record | `in_progress`, unexpired | owner and current revision | bounded result recorded |

`release --status` currently accepts every schema status other than
`in_progress`; therefore the formal model checks releases to `planned`,
`open`, `blocked`, and `done`.

`run` checks runtime configuration and the live claim before executing outside the coordinator
lock. Immediately after execution it fsyncs a privacy-safe local journal entry, then commits the
task result before attempting live reconciliation. `HandoffctlRun.tla` proves that preflight
rejection has no external effect and that task-record or post-reconciliation failure cannot erase
journal evidence. Arbitrary command correctness remains outside the proof.

The linearization point is the successful transition while the process holds the lock below Git's
common directory. Every worktree of one local clone resolves the same lock path. Expected revisions
are checked only after acquisition, so two processes observing one revision cannot both mutate it.

For the default SQLite backend, the linearization point is the successful conditional task update
and commit inside one `BEGIN IMMEDIATE` transaction. The database enforces active-owner, branch and
worktree uniqueness. The repository-common lock protects only disposable projection generation;
it is not the SQLite mutation lock. `HandoffctlStorage.tla` models one transaction owner, monotonic
revision accounting, prepare-before-selector migration, projection-after-commit and optional
publication that cannot roll back local authority.

## Permanent project binding

`HandoffctlBinding.tla` models an initialized coordinator bound to exactly one project. A call
from the bound project is accepted; a call from any other project preserves state. The bound
identity is constant, accepted/rejected classification matches caller identity, and weak fairness
of correct calls establishes that a correctly invoked coordinator can continue to make progress.
The implementation refines this guard by checking the profile UUID, state Git root and origin,
product identity and origin, and caller working directory before normal command execution.

## Checked properties

`Handoffctl.tla` exhaustively enumerates two processes, two tasks, every
coherent initial status/owner combination, ready and blocked dependencies,
every lifecycle command, current and stale revisions, injected pre-commit
rollback, and every process interleaving. `HandoffctlLocks.tla` separately
enumerates three processes as readers and writers, including two simultaneous
readers, a competing writer, and bounded lock-wait timeout. TLC checks:

- exclusive-lock mutual exclusion and a single linearization point;
- coherent ownership and at most one active task per actor;
- no lost or duplicate accepted mutation through exact revision accounting;
- atomic task/projection revision advancement and rollback;
- rejection of invalid source, owner, dependency, and revision combinations;
- timeout without state mutation when another process holds the lock;
- deadlock freedom and eventual completion under weak process/lock fairness.

Two processes are sufficient for pairwise lifecycle races; two tasks cover the
one-active-task-per-actor invariant. The separate three-process lock model
covers two readers plus one writer and two worktree identities resolving one repository-common lock.
`HandoffctlRun.tla` covers preflight rejection, external execution, durable journaling, task-record
failure, and post-reconciliation success or failure. The binding model covers the configured
project and one foreign caller, including rejection without mutation and fair progress. These are
exhaustive proofs of the abstractions, not proofs of Linux, Git, Python, or the filesystem
implementation.

`HandoffctlStorage.tla` checks both selected backends, transaction mutual exclusion, one accepted
revision increment per process, prepared SQLite authority before selector switch, eventual command
completion and eventual migration switch under weak fairness. Real independent-process tests connect
that abstraction to SQLite WAL, busy deadlines, conditional updates and database constraints.

## Refinement obligations and assumptions

The implementation satisfies the model only while all of these obligations
hold:

1. Every cooperating reader and writer uses the repository-common coordinator lock below Git's
   common directory; the filesystem implements local POSIX `flock(2)` semantics. Separate clones,
   NFS, and non-cooperating direct file/Git writers are outside the proof boundary.
2. Task and projection replacement is atomic, validation occurs before commit,
   and detected pre-commit exceptions restore every touched path.
3. Lock acquisition and internal Git/GitHub scans have finite deadlines.
   External scheduling is weakly fair: a continuously runnable waiter
   eventually runs.
4. A process holding the lock eventually exits its critical section. Arbitrary
   `SIGKILL`, kernel failure, storage loss, and power loss during a multi-file
   transaction require reconciliation and are not claimed as atomic.
5. A failed push after a successful local commit does not roll back that durable
   commit; replication is retried by reconciliation.
6. SQLite processes use separate connections to one database on the same host and supported local
   filesystem. WAL shared-memory locking on NFS or other rejected network filesystems is outside the
   contract. The busy timeout bounds contention; weakly fair scheduling is required for eventual
   writer completion.
7. The SQLite transaction is durable before projection or publication. Projection files may be
   temporarily stale after a crash and are recoverable with `reconcile`.

The focused implementation tests exercise the real `flock`, atomic replacement,
rollback, concurrent mutation/reconciliation, revision fencing, ownership and
generated-view behavior. The model and tests must both pass before a
`handoffctl` change is accepted.

## CI scope

`.github/workflows/verify.yml` runs these models for coordinator changes. Downstream integrations
use path-filtered formal gates so ordinary high-frequency coordinator-state commits do not start
the expensive model checker.

## Run locally

```bash
formal/handoffctl/verify.sh
uv run python -m unittest discover -s tests -p 'test_*.py'
```

`verify.sh` downloads the official TLA+ 1.7.4 verifier into a temporary
directory and verifies its pinned SHA-256 before execution. It does not retain
the JAR or modify coordinator state.
