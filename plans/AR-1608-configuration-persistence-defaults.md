# AR-1608 — configuration persistence and shared defaults

Materialize the wizard selection as a durable, redacted per-user
configuration. Support editing existing entries, adding providers, selecting
agents/models/authentication, and applying one setting as the default for all
or selected agents on the next run. Provide atomic update, migration,
cancellation, and recovery behavior plus a clear status/doctor view.

Dependencies: AR-1607. Downstream: AR-1603 and AR-1604.

Development-only generated keys/signatures and absent authentication services
are visible warnings and never block setup or offline execution. Secrets must
remain in the enrolled environment channel and never enter configuration,
JSON output, or evidence.

Required evidence: schema/migration fixtures, restart and cancellation tests,
multi-agent default propagation, provider-addition and stale-selection
negatives, atomicity/redaction checks, exact-head CI, review, and receipt.
