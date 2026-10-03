# AR-1697 channel specification and current-head qualification repair

## Scope

Repair the state layer for the missing/incomplete AR-1674 and AR-1675
specifications, then requalify the channel propagation and default-dev
quickstart against the exact current product heads:

- ASB `ad43609b67825f7f422b371f5d8104e0a5b20f2e`
- asb-tui `1cf4b43d7c6e8782179bbdd448d8ae14aa91fb34`

The work is state-only unless the current-head runner exposes a product
defect. Product repairs require separate product PRs and must not be hidden in
the state change.

## Deliverables

1. Add complete, schema-valid `specs/AR-1674.json` and `specs/AR-1675.json`
   or an explicit revisioned repair reference accepted by handoffctl.
2. Record the exact dependencies and current-head inputs without changing
   predecessor status merely because an older receipt exists.
3. Run the paired channel matrix covering omitted/default `dev`, explicit
   channel selection, persistence through restart and lifecycle operations,
   unavailable future channels, rollback, manifest schema/provenance, stale
   and tampered inputs, and human/JSON diagnostics.
4. Run the current-head clone-to-quickstart checks through benchmark,
   selected/all recording, strict offline replay, comparison, and analysis
   boundaries, with network denied after materialization.
5. Publish a privacy-safe signed receipt containing exact source/tree/build
   identities, test commands/results, and no credentials, raw responses, or
   private paths.

## Coordination boundary

AR-1676 and AR-1677 consume this repaired evidence; they remain planned until
their own acceptance predicates and dependency policy are satisfied. The
repair must not mark AR-1674/1675/1676/1677 done directly from the existing
stale receipts.
