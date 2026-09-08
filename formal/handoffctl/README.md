# handoffctl transition and concurrency contract

This directory defines the machine-checked contract for every task-lifecycle
mutation performed by `tools/handoffctl`. The TLA+ model is an abstraction of
the Python implementation, not a replacement implementation.

## Transition contract

Every accepted lifecycle command increments `task_revision` exactly once, updates the
generated projections under the same exclusive repository lock, validates the
result, creates at most one local state commit, and releases the lock. A rejected
command and any detected pre-commit failure leave the task revision, task state,
owner and generated projections unchanged.

| Command | Required source | Required actor/revision | Result |
| --- | --- | --- | --- |
| `promote` | `planned`, unowned, dependencies done | exact revision | `open` |
| `resume` | `blocked`, unowned | exact revision | `open` |
| `claim` | `open`, dependencies done | actor holds no other task | `in_progress`, actor and lease set |
| `heartbeat` | `in_progress` | current owner, positive lease | lease renewed |
| `update` | `in_progress` | current owner, exact revision | active fields updated |
| `release` | `in_progress` | current owner | chosen non-active state, owner and lease cleared |
| `run` record | `in_progress`, unexpired | current owner, latest locked revision | bounded external result appended as `update` |

`release --status` currently accepts every schema status other than
`in_progress`; therefore the formal model checks releases to `planned`,
`open`, `blocked`, and `done`.

`run` executes the caller's command outside the coordinator lock, with a finite
deadline. Its result record then uses the same locked `update` transition at the
latest revision. The arbitrary external command is outside the TLA+ proof; its
coordinator-state effect is inside it.

The linearization point is the successful transition while the process holds
`.runtime/state.lock`. Expected revisions are checked only after lock
acquisition. Consequently two processes that observed the same revision cannot
both apply revision-guarded changes, and two claimants cannot both claim one
open task.

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
covers two readers plus one writer. These are finite exhaustive proofs of the
abstractions, not proofs of Linux, Git, Python, or the filesystem implementation.

## Refinement obligations and assumptions

The implementation satisfies the model only while all of these obligations
hold:

1. Every cooperating reader and writer uses the same local
   `.runtime/state.lock`; the filesystem implements local POSIX `flock(2)`
   semantics. NFS and non-cooperating direct file/Git writers are outside the
   proof boundary.
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

The focused implementation tests exercise the real `flock`, atomic replacement,
rollback, concurrent mutation/reconciliation, revision fencing, ownership and
generated-view behavior. The model and tests must both pass before a
`handoffctl` change is accepted.

## CI scope

`.github/workflows/handoffctl-formal.yml` is path-filtered to the handoffctl
implementation, its focused test, this model, and the workflow itself. Ordinary
high-frequency coordinator-state commits do not start this gate.

## Run locally

```bash
formal/handoffctl/verify.sh
uv run python -m unittest tests.test_handoffctl
```

`verify.sh` downloads the official TLA+ 1.7.4 verifier into a temporary
directory and verifies its pinned SHA-256 before execution. It does not retain
the JAR or modify coordinator state.
