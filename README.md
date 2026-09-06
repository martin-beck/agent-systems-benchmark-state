# Agent Systems Benchmark coordination

Public tasks, plans and durable worker state for
[Agent Systems Benchmark](https://github.com/martin-beck/agent-systems-benchmark).

Read the product's [canonical development process](https://github.com/martin-beck/agent-systems-benchmark/blob/main/docs/DEVELOPMENT.md).
Start with [CURRENT.md](CURRENT.md), then the selected AR and its plan.
The AR identifier format is retained for compatibility with the reused coordinator.

- tasks/: strict JSON front matter plus concise durable evidence.
- plans/: implementation scope, dependencies, acceptance and test obligations.
- schema/: versioned task schema.
- tools/handoffctl: locked claims, revisions, leases, reconciliation and replication.
- tests/: generic coordinator fault, race and recovery tests.
- [PROVENANCE.md](PROVENANCE.md): the Agent Relay State reuse boundary.
- [SETUP.md](SETUP.md): local configuration and validation.

Never edit generated views directly. Private configuration, captures, credentials,
raw command output and transcripts stay outside Git. Source is MIT licensed.
