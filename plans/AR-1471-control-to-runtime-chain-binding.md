# AR-1471: Control-owned enrollment to runtime chain binding

## Objective

Connect the authenticated control enrollment operation to
`RuntimeCertificateChainStore` and normal live-dispatch receipt issuance,
without accepting caller-supplied certificate chains or authority inputs.

## Dependencies

AR-1357, AR-1359 and AR-1362 are complete. AR-1470 and AR-1363/1368/1390/1391
remain blocked historical audits and must be preserved, not treated as done.

## Required work

- Add the smallest versioned control/runtime operation that obtains a
  control-authenticated enrollment record and atomically installs the resulting
  chain in the runtime-owned store.
- Verify chain authenticity, audience, target/tool/lease/relay bindings,
  freshness, generation and revocation before installation; reject replay,
  mismatch, alternate egress, and caller-provided chain material.
- Wire the installed opaque authority to ordinary `asb run`/`asb sweep`
  receipt issuance and teardown, preserving restart recovery and generation
  fencing. Keep private credentials and paths out of public state.
- Add deterministic local/mock positive and negative tests, schema/documentation
  updates, focused/full locked gates, and exact-head review/CI/post-merge
  evidence. Live provider access is optional and never a completion gate.

## Boundaries

No asb-tui changes, no authority fabrication, no credentials or live-provider
requirement, no privacy/egress/formal gate weakening, and no edits to
`handoffctl`.
