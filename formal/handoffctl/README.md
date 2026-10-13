# handoffctl transition and concurrency contract

This directory defines the machine-checked contract for every task-lifecycle
mutation performed by `tools/handoffctl`. The TLA+ model is an abstraction of
the Python implementation, not a replacement implementation.

## Evidence classification

[`../evidence.json`](../evidence.json) records the structured formal-evidence contract required by
Agent Workflow Quality v0.24.0. It classifies these tracked TLC runs as bounded-model evidence and
records the largest finite process, task, actor, project, worktree, and revision domains used by
their checked configurations. Each `.cfg` file remains authoritative for the exact bound of its
model.

The correspondence classification is `best-effort`. Passing TLC establishes the invariants and
temporal properties below only for the tracked TLA+ specifications under those finite bounds and
assumptions. The implementation tests are separate evidence that selected Python behavior
corresponds to the abstractions; neither evidence source claims or requires implementation refinement or the
correctness of Python, Git, SQLite, operating-system, kernel, filesystem, or arbitrary wrapped
commands. The explicit assumptions, non-claims, and limitations in `formal/evidence.json` are part
of this contract and must remain aligned with the configurations and runner.

## Transition contract

Every accepted lifecycle command increments `task_revision` exactly once and validates the result.
Task hierarchy edges are reciprocal and acyclic; the bounded lifecycle model includes one parent
with one child and rejects `release --status done` while that child is non-terminal. The Python
validator additionally checks arbitrary task graphs and migration preservation.
For Git authority, the task and generated projections update under the same repository lock and a
detected pre-commit failure restores them. For SQLite authority, one database transaction commits
the task first and generated projections are recoverable output. A rejected command leaves
authoritative revision, task status and owner unchanged.

| Command | Required source | Required actor/revision | Result |
| --- | --- | --- | --- |
| `promote` | `planned`, unowned, dependencies done | exact revision | `open` |
| `pause` | `in_progress`, owned | exact revision and owner | `blocked`, ownership and lease cleared |
| `resume` | `blocked`, unowned, paused session | exact revision and session reference | `open` |
| `unblock` | `blocked`, unowned, no current-revision session | exact revision | `open` |
| `claim` | `open`, dependencies done | owner has no active task | `in_progress`, lease set |
| `heartbeat` | `in_progress` | current owner, positive lease | lease renewed |
| `update` | `in_progress` | current owner, exact revision | active fields updated |
| `accept` | `in_progress`, referenced spec | current owner, exact revision, valid evidence metadata | spec acceptance recorded; lifecycle status unchanged |
| `bind-envelope` | `in_progress`, referenced spec | current owner, exact revision, immutable matching envelope | envelope reference, revision, and digest recorded |
| `release` | `in_progress` | current owner | chosen non-active state, owner and lease cleared |
| `recover-expired` | expired `in_progress` | exact revision; a verified claim-time worker identity must now be absent unless a validated exact-current session exists; pre-identity records require explicit `--allow-legacy-without-identity` | `open`, ownership cleared; restores `next_action` only from an exact-current session snapshot |
| `run` record | `in_progress`, unexpired | owner and current revision | bounded result recorded |

The model includes `accept` as a status-preserving, exact-revision transition.
Its task-spec and evidence-field validation is checked by the concrete Git/SQLite
tests; the bounded model does not claim to prove evidence contents.

`release --status` currently accepts every schema status other than
`in_progress`; therefore the formal model checks releases to `planned`,
`open`, `blocked`, and `done`.

`run` checks runtime configuration and the live claim before executing outside the coordinator
lock. A bound run first records one revision-CAS execution fence; only that fence
holder may start its external effect. Immediately after execution it fsyncs a privacy-safe local
journal entry, then records the task result, clears the exact fence, and attempts live
reconciliation. `HandoffctlRun.tla` proves that preflight rejection has no external effect, an
effect requires a fence, and task-record, fence-completion, or post-reconciliation
task-record, fence-completion, or post-reconciliation failure cannot erase journal evidence.
After task recording or fence completion fails, expired-fence recovery may clear only the exact fence
whose durable command-result evidence exists. A journal-write failure retains an execution-unknown
fence that ordinary expiry recovery cannot clear. An operator must reconcile durable command-result
evidence before resolving that ambiguity.
Arbitrary command correctness remains outside the model.

For a task with a bound execution envelope, `run` additionally requires a declared allowed command
class and evaluates its declared scope paths before the external effect. This is a deterministic
admission check, not a claim that the wrapped command respects its declaration. The concrete
Git/SQLite tests cover envelope identity, private Bubblewrap mounts, two-clone contention, and
recovery; the bounded run model abstracts the envelope to preflight readiness and its single live
execution-fence slot. It models durable recovery evidence as a record with explicit `task_id`,
`owner`, `argv_sha256`, and `execution_id` fields in either the Git or SQLite evidence backend;
recovery requires the exact record for its reserved execution. It does not model evidence contents
beyond that identity.

Unbound `run` calls may additionally use the retry circuit. It reserves a privacy-safe command
identity slot under the task lock before launch and resolves it after child completion, but only at
the revision immediately following slot creation; an intervening mutation leaves the result
stale. Slots have a durable bounded expiry. A child crash, interrupt, or command-result recording
fault leaves an auditable abandoned slot which a later launch retires only after expiry, so it
cannot exhaust the retry window permanently. Expired-claim recovery rejects live unbound slots.
`HandoffctlRetryCircuit.tla` models owner and revision fencing, bounded slots, stale-result
rejection, expiry cleanup, expired-claim recovery, and fresh held-command recovery series. Bound
envelope runs do not use these slots and retain their execution-fence sequencing.

An opt-in tracked autonomy-limits policy records only a policy digest, bounded
counters, timestamps, and concise local dispositions. `HandoffctlAutonomyLimits.tla`
models a command/cost-like budget, elapsed expiry, a held revision fence, a
no-effect bypass attempt, and explicit local disposition. It is bounded
best-effort design guidance; concrete Git and SQLite tests cover the typed policy,
all six budget triggers, and task-record parity.

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
product identity and origin, and caller working directory before normal command execution. A
wrapped command started from a product checkout has an additional runtime guard: its Git root and
branch must match the active task's declared worktree key and branch. This command preflight is
outside the lifecycle abstraction below and does not alter the TLA+ transition relation.

## Checked properties

`Handoffctl.tla` exhaustively enumerates two processes, two tasks, every
coherent initial status/owner combination, absent, unique-valid,
unique-incoherent and duplicate pause provenance, ready and blocked dependencies,
every lifecycle command, current and stale revisions, injected pre-commit
rollback, and every process interleaving. `HandoffctlLocks.tla` separately
enumerates three processes as readers and writers, including two simultaneous
readers, a competing writer, and bounded lock-wait timeout. TLC checks:

- exclusive-lock mutual exclusion and a single linearization point;
- coherent ownership and at most one active task per actor;
- no lost or duplicate accepted mutation through exact revision accounting;
- atomic task/projection revision advancement and rollback;
- reciprocal, bounded acyclic parent/child edges and done-rollup admission;
- rejection of invalid source, owner, dependency, and revision combinations;
- rejection of pause/external-block cross-mode transitions without mutation;
- rejection of missing, incoherent, or duplicate provenance for paused resume;
- timeout without state mutation when another process holds the lock;
- acceptance of eligible recovery despite simultaneous expiries and an unrelated repository
  finding;
- deadlock freedom and eventual completion under weak process/lock fairness.

Two processes are sufficient for pairwise lifecycle races in the general model; its two tasks cover
the one-active-task-per-actor invariant. `HandoffctlRecovery.tla` separately starts two tasks as
simultaneously expired claims owned by two distinct actors while an unrelated repository finding
persists. Without injected I/O failure or lock timeout, which the general transition and lock
models cover, it proves every eligible held recovery is accepted and both distinct claims are
eventually recovered.

The separate three-process lock model covers two readers plus one writer and two worktree
identities resolving one repository-common lock.
`HandoffctlRun.tla` covers preflight rejection, durable execution fence, external execution, durable
journaling, task-record failure, fence-completion failure, and post-reconciliation success
or failure. The binding model covers the configured
project and one foreign caller, including rejection without mutation and fair progress. These are
exhaustive proofs of the abstractions, not proofs of Linux, Git, Python, or the filesystem
implementation.

HandoffctlReceipts.tla checks bounded opt-in receipt phases: an enqueued
intent is not a successful transition, local completion requires a verified
commit, remote completion requires an observed remote ref, and crash recovery
either finds that commit or retains an explicit ambiguous outcome. It models
finite executor/publisher crash and restart with weak fairness; it does not
prove operating-system service supervision, denial-of-service resistance, or
implementation correspondence. Its liveness property is conditional on both
services eventually remaining available; repeated crashes are therefore an
explicitly nonterminal environmental condition, not a false completion claim.

`HandoffctlPublication.tla` checks candidate-bound protected-main publication: idempotent admission,
descriptor-change rejection, one publisher lease, expected-base compare-and-swap, remote observation
before success, and observation-based recovery from ambiguous pushes. It is a one-candidate
abstraction: database-wide liveness across historical jobs is established by executable sweep tests,
not claimed as a refinement result. The fast PR tier checks its
safety invariants; publication and full tiers also check eventual terminal resolution after the
publisher eventually remains available. Repeated publisher crashes remain a nonterminal
environmental condition, rather than an unsound completion guarantee. The finite model includes
at most one ambiguous push and one competing remote advance.
Git ancestry and transport are abstracted as finite head values; this is not
implementation-correspondence evidence.

HandoffctlObservation.tla checks the bounded opt-in `cached-observation-v1`
contract: cache hits require the exact current input generation, one refresh
serves concurrent waiters, an input change rejects the in-flight generation,
and timeout is terminal. It is an abstraction of the resident socket cache;
it does not claim operating-system event delivery or implementation refinement.
[`OBSERVATION_CORRESPONDENCE.md`](OBSERVATION_CORRESPONDENCE.md) maps the
abstraction to focused implementation evidence and records those limits.

HandoffctlPredicateLedger.tla checks predicate-aware `accept`: exact
candidate ref/digest binding, revision and owner fencing, explicit candidate
reopen, stale-history conversion, and done admission only after complete
current-candidate predicate evidence. It explores two workers, two predicates,
and the complete two-reference by two-digest candidate identity cross-product,
including same-ref/changed-digest and different-ref/same-digest transitions;
it is a bounded abstraction, not
implementation-refinement evidence.

HandoffctlAssumptions.tla checks opt-in material freshness bindings for a
base, dependency, and local observation. It explores moved binding races, stale
and current revisions, explicit revalidation/disposition, non-material
assumptions, and owner-and-revision-fenced `accept`. It requires both acceptance
and a task released `done` to have every material declared input fresh or
explicitly disposed; it is bounded best-effort design guidance, not an
implementation-refinement proof.

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

## Human TUI handoff

An interaction gate may retain one current `human_session` record while a decision is presented
through a human TUI. The record binds its public session/request references and activation reason to
the gate-opening revision. The `OracleInteractionGates` model checks that a presented session is
revision-bound and cannot admit autonomous claim, run, or release work; resolution changes the
session to a terminal public status. This is bounded best-effort design guidance, not a proof of
the Python, TUI, or external decision system.

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

Formal tiers are explicit: `verify.sh --tier portable-smoke` runs one model
and is non-exhaustive; it cannot produce publication or full evidence.
`verify.sh --tier pr-publication` is reduced bounded release qualification for
its declared model set. Seven models use their full configurations; the general
lifecycle model uses the explicitly named one-process `HandoffctlLiveness.cfg`.
`LIVENESS_COVERAGE.json` maps each omitted dimension to focused models and
concrete tests, while the separate lock and recovery models retain
independent-process races. The reduced configuration retains every lifecycle
safety invariant and `EventualCompletion`. This is a bounded coverage argument,
not refinement evidence or the complete two-process lifecycle cross-product,
and cannot produce full formal or release evidence.

`HandoffctlPR.cfg` is a source-only compatibility bootstrap for snapshots
created before AR-0101. It is deliberately excluded from every tier. An old
vendored updater needs it for one sync that installs the new updater; the new
updater removes the bootstrap on its next atomic sync.
`verify.sh --tier full-exhaustive` runs every full focused configuration plus
the complete two-process lifecycle domain as fifteen disjoint immutable-
operation slices. Each slice fixes one process's request operation and leaves
the competing process's operation domain complete; because requests do not
change operation, their union is exactly the original aggregate state graph.
The scheduled weekly run or an explicit dispatch of the separate **Advisory
Formal Stress** workflow on `main` checks every slice as exploratory evidence.
It uses a dedicated runner label, private workspace, queue, and admission lock;
it can be canceled or retried independently of bounded validation. Its receipt
and any partial or interrupted outcomes are explicitly exploratory. A failed or
missing full-exhaustive run cannot block normal progression, acceptance, merge,
or release. Neither a missing slice nor a smaller tier supports a full formal
claim.

Each model is executed through `tools/tlc_runner.py`, never directly through
TLC. The runner uses finite workers (`2`), a dedicated `48g` heap and `64G`/`64G`
memory/swap cgroup limits for full-exhaustive runs, a `2g` heap and `3G`/`3G`
limits for ordinary same-repository PR publication, and a `512m` heap for hosted
smoke. It retains CPU quota (`200%`), process limit (`64`), a 300-second
`pr-fast` or 900-second `pr-publication` aggregate end-to-end budget (including
queue/lock admission), and an 86400-second advisory full-exhaustive aggregate
budget, plus a fail-closed 64 GiB
host/parent-cgroup prerequisite for full evidence. Before every required TLC
execution, the runner reads `memory.max`, `memory.high`, and
`memory.swap.max` from inside the transient unit and all of its ancestors; the
leaf limits must exactly match the requested bounds and no ancestor may be
lower. A canonical host-wide admission lock prevents
multiple formal jobs from competing for memory while leaving coordinator worker
processes and leases untouched. A durable per-job queue record survives caller
death for stale-job recovery; completed, failed, and canceled outcomes retain
the exact resource bounds and exit classification. `systemd-run` owns the process group (`KillMode=control-group`) on hosts with a user systemd bus. Hosted CI selects an explicit `portable` containment mode: GNU `timeout` and `prlimit` enforce aggregate address-space, process-count, CPU-time, and wall-clock limits; the runner fails closed if either tool is unavailable.

Every verifier invocation creates a private workspace below the first configured
root: `TLC_WORK_ROOT`, then `TLC_RUNTIME_ROOT`, then the temporary root. TLC
receives that path as both its Java
temporary directory and working directory, so standard modules and state files
cannot collide with another verifier through shared `/tmp`. The runner rejects
a metadir outside that workspace, preflights available storage against
`TLC_STORAGE_RESERVE`, and terminates a run that exceeds `TLC_STORAGE_MAX` with
a durable `storage-exhausted` outcome rather than misclassifying it as a model
success.

The runner retains `/tmp/agent-workflow-coordinator-tlc-admission.lock` as the canonical
publication lock. Bounded validation uses that shared admission path by default.
Exploratory stress uses an explicit private queue and lock pair, as can an
isolated clean-destination diagnostic on a host where the shared path is inaccessible:

```bash
formal/handoffctl/verify.sh --tier portable-smoke \
  --diagnostic-queue /absolute/private-tlc-queue \
  --diagnostic-admission-lock /absolute/private-tlc-admission.lock
```

Both distinct absolute paths are required together and are propagated as explicit runner CLI
arguments; there is no verifier environment override. The resulting attestation is classified
`diagnostic-private-admission`, sets `canonical_publication_evidence` to false, and states that it
cannot support publication or release claims. Hosted and checked-in workflows omit these flags and
therefore retain the canonical shared admission path and fail-closed publication semantics.

## Candidate-bound formal jobs

`tools/formal_job_receipts.py` separates long-running formal execution from
coordinator authority. A short SQLite transaction records a `started` job bound
to the exact candidate object ID, tier-contract digest, and resource class.
Beginning a run writes a fenced execution token and releases the database before
the executor is called. Completion, failure, cancellation, recovery, and
supersession are separate atomic transitions. A replacement candidate
supersedes any active job in that scope, and a late worker cannot write a
terminal result because it lacks the current revision and execution token.

Only a zero-exit `completed` receipt whose candidate and tier digest exactly
match the consumer's current inputs is usable as formal evidence. `failed`,
`cancelled`, `superseded`, incomplete, and mismatched receipts are explicitly
not evidence. The receipt store is local operational state; it uses no
coordinator task lease, external authentication, signature, or review gate.

## Exact-head bounded receipts

The main formal workflow runs the fixed `pr-publication` tier rather than
accepting a workflow input that could select a different profile. After the
verifier writes its attestation, `tools/formal_receipt.py` checks it against the
locally checked-out commit, each declared model and configuration digest, and
the tier's fixed aggregate budget. A stale candidate, timeout, or resource
exhaustion is rejected with concise remediation guidance. This validation is
locally reproducible:

```bash
python3 tools/formal_receipt.py \
  --receipt /path/to/formal-attestation.json \
  --candidate "$(git rev-parse HEAD)" \
  --tier pr-publication
```

Hosted CI can publish this receipt as advisory operational evidence, but it is
not an authentication, signature, approval, review, merge, acceptance, or
release gate.

## Tier-migration qualification

`tests/test_formal_tier_qualification.py` exercises the local end-to-end
evidence boundary with controlled runner projections: exact candidate identity
is rendered into a bounded receipt and then validated against the checked-out
tree. It also verifies typed storage/admission and deadline remediation,
noncanonical cancellable advisory-stress receipts, and the one-sync legacy
`HandoffctlPR.cfg` vendor migration. These are deterministic boundary tests;
the tier runners remain responsible for executing TLC itself. No hosted CI,
external account, signature, or independent review is needed to reproduce or
use this qualification evidence.
