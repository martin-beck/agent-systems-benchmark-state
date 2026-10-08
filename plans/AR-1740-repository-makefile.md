# AR-1740 plan: repository Makefile developer workflow

1. Add a repository-root `Makefile` as an optional developer convenience;
   ASB runtime, release, and installed-user paths must not depend on Make.
2. Provide discoverable targets for `help`, `check-deps`, `build`, `install`,
   `clean`, `update`, and `test`, with stable defaults, overridable `CARGO`/
   `RUSTUP_TOOLCHAIN`/target variables, and no shell-spawned unbounded command
   strings.
3. Make `check-deps` verify the pinned Rust toolchain, Cargo, required target
   and host utilities before mutating targets, with actionable diagnostics and
   offline-safe behavior. Do not install packages or download tools implicitly.
4. Make `build` and `test` use the documented locked workspace gates; make
   `install` use a bounded staging/prefix variable and refuse unsafe paths;
   make `clean` remove only the declared Cargo target/staging directories; and
   make `update` perform a safe fast-forward source/dependency refresh only
   after a clean-tree check, then run dependency validation.
5. Add positive and negative shell/Makefile tests, documentation, completion or
   help coverage, and checks for missing Cargo/toolchain/target/path inputs.
   Reuse the exact commands from `docs/QUALITY.md` and `docs/QUALITY_GATES.md`;
   preserve offline-after-install and second-disk boundaries.

