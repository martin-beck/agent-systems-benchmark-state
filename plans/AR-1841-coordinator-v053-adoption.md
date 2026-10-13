# AR-1841 plan: Coordinator v0.5.3 adoption

Adopt the immutable upstream Coordinator v0.5.3 release containing the
AR-0088 partial-legacy worktree binding repair. Preserve the vendor boundary,
all ASB-owned quality floors, and the existing fail-closed lifecycle rules.

1. Verify the clean upstream v0.5.3 tag, commit, tree, and source manifest.
2. Synchronize the snapshot only with `tools/handoffctl_vendor.py sync` into
   an isolated candidate state worktree; never patch vendored files manually.
3. Run vendor verification, schema/generated-view/privacy checks, state tests,
   formal gates and live doctor; repair only ASB-owned compatibility fixtures.
4. Independently review the complete diff, verify SSH/DCO, publish a reviewed
   state PR, wait for exact-head CI, and merge through the documented path.
5. Verify exact-main post-merge workflows and record the immutable vendor
   receipt so AR-1826 can bind its matching legacy worktree identity.

The adoption must retain the existing coverage floor and must not weaken any
authority, privacy, formal, or worktree-fence gate.
