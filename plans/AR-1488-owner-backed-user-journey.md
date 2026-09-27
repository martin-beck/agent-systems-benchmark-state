# AR-1488: Owner-backed first-customer user journey

## Objective

Qualify and document the shortest ASB-only first-customer path over the
runtime-owned CLI: install/bootstrap, credential-free local/mock setup, an
owner-backed run and sweep, strict offline replay/comparison, bounded
evidence/receipt inspection, cancellation/restart recovery, and cleanup.

## Dependencies

AR-1441, AR-1442, AR-1450, AR-1455, and AR-1487 are complete. This task does
not depend on or modify asb-tui and does not require provider reachability,
credentials, downloads, or native ARM.

## Acceptance

- A disposable local/mock walkthrough starts from the supported install and
  setup contract, executes owner-backed run and sweep, and produces bounded
  machine-readable result and receipt evidence.
- The same evidence can be consumed by strict offline replay/comparison using
  runtime-issued authority; missing, stale, copied, tampered, and reused
  authority fail closed before execution effects.
- Cancellation/restart recovery and teardown leave no runnable owner/backend
  resources and expose no credentials, prompts, transcripts, raw captures, or
  private host paths.
- Positive and hostile tests, docs, privacy/policy gates, full workspace gates,
  signed DCO review, exact-head CI, and all post-merge workflows pass.

## Boundaries

Prefer a deterministic qualification harness and docs over production changes.
If a concrete ASB-only gap exists, implement the smallest fail-closed repair.
Never claim live-provider quality, native-platform support, or paired asb-tui
journey evidence from local/mock/replay fixtures.
