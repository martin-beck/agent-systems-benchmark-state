# AR-1755 plan: idempotent `make install`

1. Reproduce the exact current-main behavior with a disposable absolute prefix:
   the first install succeeds, the second fails because Cargo refuses to replace
   `bin/asb`, and `make install --force` is rejected by Make itself.
2. Keep the user command as plain `make install`. Pass Cargo's overwrite flag at
   the Cargo boundary after the existing prefix and symlink validation succeeds.
   Update help or diagnostics only where needed so no output instructs users to
   pass Cargo-only flags to Make.
3. Extend the bounded Makefile harness so the fake Cargo implementation rejects
   repeat installation unless the production command contains the overwrite
   flag. Exercise two consecutive installs into the default disposable HOME and
   an explicit safe prefix, prove the installed executable is replaced, and
   prove unrelated prefix contents remain unchanged.
4. Retain negative coverage for relative, empty, root, repository-root,
   traversal, non-directory, and symlinked prefix/destination paths. Do not weaken
   the clean target's marker boundary or permit writes outside the selected
   prefix.
5. Run the focused shell harness and complete locked workspace gates. Record a
   privacy-safe receipt, obtain independent defect-focused review of the exact
   signed+DCO head/tree, require all hosted exact-head checks, integrate through
   the documented signed exact-tree merge path, and verify all exact-main checks
   before releasing the AR done.

