# AR-1716 — Cassette provider-profile identity binding

At `RecordingIndex::insert`, require the cassette entry's provider-profile
identity to equal the reviewed run/provider profile identity, including the
profile digest and generation fields used by the recording contract. Reject
missing, stale, or mismatched identity before writing or replacing an index
entry. Preserve deterministic typed diagnostics through human and `--json`
outputs without logging provider secrets or response content.

Acceptance:

1. Matching provider profile and cassette identity inserts successfully.
2. Missing, stale, and mismatched provider profile identities fail closed
   before mutation and produce stable typed diagnostics.
3. Tests prove no partial index/cassette mutation on rejection and preserve
   development warning-only authentication behavior.
4. Focused/full tests, privacy checks, independent review, and hosted gates
   pass at the exact current ASB head.
