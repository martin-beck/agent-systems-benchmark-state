# AR-1752 plan: development broker v1.15 projection repair

## Scope and ownership

This P0 repair belongs entirely to `agent-systems-benchmark`. It owns the
read-only development control backend, negotiated-version forwarding, public
`asb tui` lifecycle routing tests, and privacy-safe qualification evidence. It
does not own the standalone `asb-tui` renderer or interaction model.

## Implementation sequence

1. Reproduce the exact public failure from immutable ASB/asb-tui heads using a
   content-addressed development bundle, isolated XDG roots, a controlling PTY,
   and provider network denied. Preserve only sanitized result codes, source
   identities, digests, and typed diagnostics.
2. Add a focused regression that negotiates v1.15 through
   `DevelopmentBackend` and proves a refresh/status call returns
   `DynamicProviderCatalog`; prove v1.14 and older clients retain their legacy
   `ProviderCatalog` projection.
3. Repair delegation at the narrowest boundary. The development wrapper must
   forward admitted read-only calls through the inner backend's negotiated
   execution path while retaining its existing capability override and
   mutation deny-list. Do not copy dynamic-catalog construction logic or make
   the development backend an authority.
4. Add negative tests for configuration/auth/profile/run/recording mutations,
   stale identity/generation, unavailable/static/empty projections, malformed
   responses, older protocol negotiation, and transport failure. Explicit
   dynamic/live routes must never fall back to static/mock/replay success.
5. Build exact ASB and standalone TUI candidates, publish a private immutable
   dev bundle, and run `asb tui install`, `asb tui status`, bare `asb tui`, and
   `asb tui dynamic-catalog` through the public ASB binary with a real
   controlling PTY. Require bounded cleanup, exact source/tree/digest binding,
   warning-only development auth/signing/key diagnostics, and no secrets.
6. Run fmt, Clippy with warnings denied, locked focused/workspace tests, rustdoc,
   coverage, dependency/security/workflow/shell/privacy checks, and applicable
   inherited-fd/PTTY/cross-repository qualification.
7. Commit with SSH signature and matching DCO, publish one focused PR from an
   isolated registered worktree, and obtain independent review of the exact
   head/tree and public-journey receipt. Repair every finding additively.
8. If main advances, synchronize without rewriting published history, rerun
   exact-head tests/CI and independent review, then merge only the reviewed tree
   through the documented signed integration path.
9. Require every exact-main post-merge workflow to finish successfully. Attach
   an immutable privacy-safe receipt, accept the spec, release AR-1752 done,
   then requalify and close parent AR-1721.

## Stop conditions

- Stop fail-closed if v1.15 cannot be projected without widening development
  mutation authority or duplicating authoritative provider-catalog logic.
- Do not change the TUI renderer/application, permit provider egress in the
  credential-free fixture, persist credentials/raw payloads, or convert typed
  route failures into generic or successful fallbacks.
- Do not treat missing production authentication/signatures/key management or
  lack of a second GitHub identity as a blocker for this development repair.
