# AR-1467: terminal AR metadata reconciliation

## Objective

Reconcile recently completed ASB AR records whose `status` is `done` but whose
`next_action` still describes a historical merge, review, or CI wait. Preserve
all evidence and do not change product code, formal contracts, or release gates.

## Scope

- Inspect the completed ARs identified in the task record and verify their
  recorded merge/release evidence against immutable GitHub state.
- Replace only demonstrably stale terminal next-action text with a concise
  no-further-action statement that points to the retained evidence.
- Leave any AR with an unresolved check, missing review, or open dependency
  unchanged and create a follow-up repair instead of claiming completion.

## Acceptance gates

- Every changed task retains its original status, revision history, evidence,
  checkpoint, dependencies, and owner boundary.
- State schema, generated views, privacy checks, focused tests, and exact-head
  Coordination verification pass.
- No product/asb-tui source, formal input, release artifact, or gate is changed.
