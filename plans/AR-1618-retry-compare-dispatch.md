# AR-1618 — operator retry and comparison dispatch

Expose typed operator actions for benchmark repeat/agent retry and live versus
offline comparison through the ASB control route and TUI. Carry exact run,
cassette, profile, provider, agent, workload, and generation identities;
reject stale or incompatible requests before transport or mutation. Keep
retry bounded and idempotent, and make comparison return a typed digest-bound
result rather than only a local summary.

Development-only missing authentication, signatures, and key management remain
visible warnings and never block the prototype.

Required evidence: versioned wire/control schema, selectable actions, positive
retry and comparison paths, stale/mismatch/idempotency negatives, offline
compatibility, independent review, hosted checks, and exact-main verification.
