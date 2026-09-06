# Agent Systems Benchmark coordination

Public tasks, plans and durable worker state for
[Agent Systems Benchmark](https://github.com/martin-beck/agent-systems-benchmark).

Read the product's [canonical development process](https://github.com/martin-beck/agent-systems-benchmark/blob/main/docs/DEVELOPMENT.md).
Start with the polished [STATUS.md](STATUS.md) portfolio and dependency graph. Use
[CURRENT.md](CURRENT.md) for the compact operational queue, then read the selected AR and its plan.
The AR identifier format is retained for compatibility with the reused coordinator.

- tasks/: strict JSON front matter plus concise durable evidence.
- plans/: implementation scope, dependencies, acceptance and test obligations.
- schema/: versioned task schema.
- tools/handoffctl: locked claims, revisions, leases, reconciliation and replication.
- STATUS.md: deterministic complete AR inventory, graphical dependency map and text alternative.
- tests/: generic coordinator fault, race and recovery tests.
- [PROVENANCE.md](PROVENANCE.md): the Agent Relay State reuse boundary.
- [SETUP.md](SETUP.md): local configuration and validation.

Never edit generated views directly. Private configuration, captures, credentials,
raw command output and transcripts stay outside Git. Source is MIT licensed.

Run `tools/handoffctl render-status --check` to verify that `STATUS.md` matches every task. A plain
`tools/handoffctl render-status` performs an offline deterministic refresh; normal claim, update,
promote, release, and reconcile transactions refresh it automatically under the coordinator lock.

## Opening dependency-ready work

After reviewing dependencies and path ownership, the coordinator promotes a planned AR with:

    tools/handoffctl promote AR-NNNN --expected-revision REVISION --note "dependencies verified"

Promotion accepts only an inactive planned task whose dependencies are done. It rejects stale
revisions, invalid task or generated state, and a dirty state checkout. The task transition and
automatic CURRENT.md and graphical STATUS.md regeneration share one lock, validation, signed DCO
commit, and replication transaction.

If promotion is interrupted, inspect the task revision and status, signed local commits, generated
views, and remote main before retrying. A signed local commit is a durable effect even when
replication fails: reconcile and retry replication instead of repeating the transition.
