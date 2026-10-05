# AR-1718 — portable fault-matrix network isolation repair

This durable coordination record covers PR #487. It preserves a closed
backend abstraction, loopback/external preflight, bounded cleanup, typed
unavailable results, and redacted receipts. Approved backends are direct
`unshare --net`, systemd user `PrivateNetwork=yes`, and bubblewrap
`--unshare-net`; host-network fallback is forbidden.

Acceptance requires focused backend tests, the five-case fault matrix,
independent review, exact hosted checks, post-merge verification, and a
receipt suitable to requalify AR-1596. Development auth/signatures/key
management remain warning-only and are unrelated to network isolation.

Collision rationale: AR-1718 had concurrently been reused for the OpenRouter
free-model catalog. That scope is preserved under the fresh AR-1719 ID;
AR-1718 remains the portable fault-matrix repair.
