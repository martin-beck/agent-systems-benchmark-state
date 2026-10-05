# AR-1712 — Live recording and comparison handoff

Specify the ASB-owned handoff from an explicit live benchmark to selected/all
recording, cassette sealing, offline replay, and comparison. Bind every
artifact to the provider/model/agent/workload/run identity and generation;
make incomplete, stale, or mismatched artifacts typed unavailable. Provide
the TUI with a digest-only catalog and stable result/comparison projection.

Acceptance:

1. Selected and all-agent capture scopes are explicit and preserve workload
   coverage; empty selection is not inferred as all.
2. Sealed artifacts can be replayed offline with network denied and compared
   to the live baseline using exact identity and digest fences.
3. Incomplete/stale/mismatched captures fail closed without provider calls.
4. Handoff contract, human/JSON receipt, privacy, and hosted checks pass.
