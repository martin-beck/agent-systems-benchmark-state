# AR-1737 plan: development TUI linker handoff

## Phase 1: reproduce and bind the failure

1. Bind an isolated worktree to the current exact ASB `origin/main`, record the
   compatible asb-tui source identity, and reproduce `dev_command_failed` using
   the production materializer with `env_clear` and no ambient `PATH`.
2. Capture the bounded effective Cargo/rustc/GCC invocation and prove that the
   current global `RUSTFLAGS` suppresses
   `CARGO_TARGET_<TARGET>_RUSTFLAGS`, leaving `collect2` without its validated
   `ld` search root.
3. Record the validated Cargo, rustc, compiler, archiver, linker, target, and
   derived linker-parent identities without retaining private host paths in
   public evidence.

## Phase 2: implement one effective flag channel

1. Refactor environment construction so a single authoritative rustc flag
   channel contains all deterministic remap arguments and
   `-C link-arg=-B<validated-ld-parent>`. Prefer NUL-safe
   `CARGO_ENCODED_RUSTFLAGS`; do not join user-controlled shell text.
2. Remove the ineffective competing target-specific/global configuration and
   keep all tool variables absolute and descriptor-validated. Never restore or
   synthesize ambient `PATH`.
3. Preserve reproducible source, target, and Cargo-home remapping. Return a
   stable typed diagnostic for unsupported compiler-driver/linker combinations
   rather than silently falling back to host lookup.

## Phase 3: focused and hostile regression tests

1. Replace the environment-only assertion with a real minimal Cargo compile and
   link that invokes the production environment builder under `env_clear`.
2. Capture effective arguments and assert the remap flags and validated `-B`
   root arrive on every linking rustc invocation.
3. Add negative fixtures for hostile `PATH`, Cargo/rustc/compiler/linker/archiver
   overrides, missing and relative linker paths, symlink/ownership/write-mode
   violations, path escaping, malformed encoded flags, and incompatible driver
   behavior.
4. Build the same exact inputs in two unrelated temporary roots, compare the
   final executable SHA-256, and scan artifacts/diagnostics for staging-path
   leakage.

## Phase 4: lifecycle and repository qualification

1. Run `cargo fmt --all -- --check`, focused tests, Clippy with warnings denied,
   the relevant serialized workspace tests, docs, and applicable repository
   policy/coverage gates.
2. Exercise exact paired `asb tui install`, `status`, `doctor`, `upgrade`, bare
   controlling-PTY `asb tui`, and repeated `remove`. Assert that all local
   operations deny network and that install/upgrade use only their declared
   development acquisition behavior.
3. Commit the focused change and open a PR. Authentication, commit signing,
   DCO, and production publication checks are warning-only in this development
   cycle and must not prevent implementation, testing, review, or merge.

## Phase 5: independent review and integration

1. Have a separate worker review the exact candidate commit/tree, the effective
   compiler arguments, trust-boundary negatives, deterministic digest result,
   and public lifecycle. Any material change invalidates the prior review.
2. Merge only the reviewed functionally green candidate, then wait for and
   verify all required post-merge workflows at the exact merge SHA.
3. Record the merge SHA, test and CI evidence, paired asb-tui identity, and any
   development-policy warnings; release AR-1737 done and reconcile/doctor the
   state repository. Notify asb-tui AR-1575 that its ASB dependency can resume.
