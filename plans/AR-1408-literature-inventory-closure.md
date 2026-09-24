# AR-1408: Literature workload inventory closure

## Objective

Reconcile every benchmark candidate named in `docs/WORKLOADS.md`,
`docs/RELATED_WORK.md`, and linked methodology documents with the versioned
workload catalog.  Classify each item as an executable workload, a harness,
scorer, observability system, or methodology-only reference.  Add immutable
provenance records for benchmark families that are currently only mentioned in
prose, and record explicit non-workload boundaries for Harbor, Inspect AI, HAL,
AgentOps, and HELM where they provide infrastructure rather than a workload.

## Dependencies

- AR-1400 (catalog activation)
- AR-1399 (literature source audit)

## Acceptance

- A machine-checkable inventory lists every benchmark named in the literature
  docs, its stable ID, source/revision/license status, workload kind, and
  evidence state.
- AgentBench, tau-bench, and AgentDojo are represented as explicit planned
  interactive/tool-use workload boundaries, or have a documented, justified
  exclusion with a durable reason; no prose-only benchmark remains ambiguous.
- Frameworks and scorers are explicitly marked non-workloads and cannot be
  selected as benchmark tasks.
- Unknown, duplicate, malformed, mutable-reference, and unlicensed entries are
  rejected by positive and negative registry tests.
- No dataset, credential, provider, private path, or network download is added
  to the repository; all acquisition remains explicit and non-vendored.

## Verification

Run registry schema/validity tests, docs-to-catalog parity checks, repository
quality/privacy/DCO checks, and the full applicable workspace gates.  Review
the complete diff independently before publication.
