# AR-1852 plan: role-store v0.7.4 compatibility contracts

Align downstream role authorization tests with the verified Coordinator v0.7.4
durable role-store semantics while preserving authorization and fail-closed gates.

1. Reproduce role doctor and lifecycle admission failures against exact v0.7.4.
2. Update non-vendor fixtures and positive/negative assertions only where the released contract changed.
3. Run locked focused/full gates and independent exact-head review.

Candidate binding: exact ASB v0.7.4 candidate worktree commit `180c96b25d`; do not promote until this binding is recorded.
