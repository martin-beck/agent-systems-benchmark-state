# AR-1851 plan: AR-1793 v0.7.4 compatibility contracts

Update only non-vendor AR-1793 coverage fixtures and expected error contracts
to match the verified Coordinator v0.7.4 behavior.

1. Reproduce each failing fixture against the exact v0.7.4 snapshot.
2. Update positive and negative tests to the released contract without weakening fail-closed behavior.
3. Run focused and full locked quality gates with independent review.

Dependency: AR-1841 exact v0.7.4 adoption must be complete first.
