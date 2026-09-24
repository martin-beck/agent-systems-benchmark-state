# AR-1409: Interactive literature workload adapters

## Objective

Make the documented interactive benchmark families selectable beside the
built-in software-engineering workloads.  Add catalog/adapter contracts for
AgentBench, tau-bench, and AgentDojo (including their stateful environment,
tool-use, simulated-user, and safety dimensions) and provide bounded local
fixtures for development and CI.

## Dependencies

- AR-1408 (complete literature inventory)
- AR-1401 (deterministic local mock execution)

## Acceptance

- Each family has a stable workload ID, pinned provenance metadata, capability
  tags, adaptation/evidence status, and an explicit evaluator/oracle boundary.
- Local deterministic fixtures exercise task setup, tool calls, state reset,
  grading, policy-violation reporting, pass^k/reliability where applicable,
  and bounded failure paths without contacting a live provider or backend.
- The normal catalog and adapter APIs can select these families alongside
  built-in and repository-repair workloads; unsupported external execution
  fails closed with an actionable message.
- Positive and negative tests cover unknown IDs, stale revisions, unsafe tool
  calls, reset leakage, malformed simulated users, and scorer mismatches.
- No framework, scorer, or observability package is accidentally exposed as a
  benchmark workload, and no credentials or private transcripts are retained.

## Verification

Run focused adapter/mock tests, complete CLI/catalog tests, full workspace
quality gates, and an independent review of provenance and privacy boundaries.
