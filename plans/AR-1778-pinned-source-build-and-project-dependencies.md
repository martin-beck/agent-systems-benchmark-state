# AR-1778 plan: pinned source builds and project dependencies

1. Extend acquisition recipes with exact source/build dependency closure,
   toolchain, commands/API, expected outputs, resource bounds, and allowed
   network phases.
2. Implement project-prefix dependency materialization and identity-validated
   system dependency reuse; never mutate global package-manager state or require
   root.
3. Execute builds in a bounded staging environment with cleared credentials,
   controlled environment/path, declared toolchain, cancellation, cleanup, and
   safe bounded logs.
4. Verify produced tool/workload entrypoints and dependency closure, atomically
   publish them, and retain a receipt sufficient for later repair/removal.
5. Add reproducible source and dependency fixtures plus hostile build-script,
   missing compiler, mismatch, timeout, cancellation, cleanup, and repeat-build
   tests; qualify at least one supported tool per supported build family.
