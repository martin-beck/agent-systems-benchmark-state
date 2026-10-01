# AR-1619 — cross-repository lifecycle protocol repair

Repair and independently qualify the AR-1617/1618 implementation across ASB
and TUI before merge. Regenerate checked-in schemas and fixtures, make seal and
reopen states identical, make retry atomic with derived idempotency keys, wire
all TUI actions to executable control dispatch, and remove/tombstone the
explicitly selected development cassette artifact. Add exact-SHA paired tests
and keep missing development authentication, signatures, and key management
warning-only.

Required evidence: independent review, hosted quality checks, exact-main
verification, and positive/negative lifecycle, stale, idempotency, and
offline-replay tests.
