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
- [docs/native-aarch64-policy.md](docs/native-aarch64-policy.md): required QEMU portability and optional native ARM64 policy.

Never edit generated views directly. Private configuration, captures, credentials,
raw command output and transcripts stay outside Git. Source is MIT licensed.

## Shared coordinator release

This repository vendors the signed `agent-workflow-coordinator` v0.3.5 release. Its exact upstream
commit and copied-file digests are locked in `coordinator.vendor.json`; verify them offline with
`python tools/handoffctl_vendor.py verify --target .`. The complete integration, use, extension,
and upgrade guide is [`docs/agent-workflow-coordinator.md`](docs/agent-workflow-coordinator.md).

The one-time `.handoffctl.json` and `coordinator.binding.json` identity permits supported commands
only from this state checkout or its configured Agent Systems Benchmark product checkout. Repository
identity and the immutable project UUID are checked before state access; a different project must
initialize its own coordinator and cannot rebind this one.

Run `tools/handoffctl render-status --check` to verify that `STATUS.md` matches every task. A plain
`tools/handoffctl render-status` performs an offline deterministic refresh; normal claim, update,
promote, release, and reconcile transactions refresh it automatically under the coordinator lock.

Pull requests that change `tasks/**`, `plans/**`, `CURRENT.md`, or `STATUS.md` always run the
exact-head Coordination verification workflow. That check validates schemas and generated views,
requires a clean tree, and verifies DCO for every commit in the pull-request base-to-head range.
An unrelated documentation-only change remains outside this coordination-content path filter.

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
