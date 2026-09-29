# AR-1527 plan: normalize the AR-1307/1308 development seed policy

## Scope

1. Read the complete AR-1307/1308 chain and classify every seed/digest
   requirement as development, formal qualification, publication, or release.
2. Remove reviewed-seed and signed/digest-bound-input prerequisites from the
   development and diagnostic path. Use generated disposable seeds and local
   fixtures; record `qualification_authorized=false`.
3. Keep formal/publication/release successors fail-closed and explicit. A
   formal task may still require exact signed or digest-bound inputs, but that
   requirement must not be inherited by ordinary development dependents.
4. Repair task summaries, plans, dependency edges and generated views through
   the state workflow. Add positive and negative metadata validation for the
   policy split.

## Acceptance

- No open/planned development AR in the 1307/1308 chain requires archival or
  reviewed seed material before local execution.
- Formal ARs still state their exact-input and terminal-attestation gates.
- State schema, generated views, privacy checks, and `doctor --live` pass.
- No product or asb-tui files change.
- Durable evidence identifies every edited AR and the remaining formal blocker.
