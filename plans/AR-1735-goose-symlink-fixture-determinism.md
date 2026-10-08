# AR-1735 plan: deterministic Goose diagnostic fixture

1. Reproduce the AArch64 post-merge observation where the diagnostic fixture
   sometimes returns a normal failed outcome instead of the expected setup
   error.
2. Identify the stderr/exit observation race without changing adapter product
   semantics or weakening the expected diagnostic classification.
3. Add repeated native and emulated regression coverage, then run full agent,
   workspace, and portability gates.

