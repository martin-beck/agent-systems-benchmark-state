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
release, and reconcile transactions refresh it automatically under the coordinator lock.
