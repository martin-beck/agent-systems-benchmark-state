# AR-1478: Repair topic synchronization topology

## Objective

Resolve the protected-main policy failure after AR-1477 merge `67fa0d1a`:
“topic synchronization merge must be at the tip.” Preserve the reviewed test
content while producing an allowed exact-head topology for post-merge policy.

## Dependencies

AR-1477 supplies the merged authority-resolver coverage tests; AR-1475 and
AR-1476 supply the repaired metrics and coverage evidence. This repair owns
only synchronization topology and must not alter product semantics.

## Required work

- Inspect the exact merge parents, branch tip, protected-main ancestry, and
  policy verifier to identify why the synchronization merge is not recognized
  as the tip.
- Create the smallest signed/DCO topology-only correction permitted by policy,
  preserving the reviewed AR-1477 tree and all required ancestry evidence.
- Run the exact policy/coordination checks plus focused/full gates, publish a
  clean PR, obtain independent review, merge only green, and verify all seven
  exact-main post-merge workflows.
- Reconcile durable state and requalify the dependent production PR without
  waiving topology, coverage, or authority gates.

## Boundaries

No product behavior changes, no test skipping, no threshold changes, no
asb-tui/provider requirement, no forceful history rewrite, and no edits to
`handoffctl`.
