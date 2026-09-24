# AR-1404: Literature workload documentation and matrix contract

## Objective

Keep `docs/WORKLOADS.md`, `docs/RELATED_WORK.md`, registry schemas, generated
catalog output, CLI help, and reproducibility guidance derived from the same
catalog and truthful about every evidence state.

## Acceptance

- Generated documentation and CLI inventory distinguish built-in qualified
  fixtures, local deterministic literature fixtures, explicit external
  candidates, and methodology-only references.
- CI fails when docs, registry, generated catalog, and CLI inventory diverge;
  examples include source/revision, scorer, adaptation, platform, licensing,
  and mock-versus-official result labels.

