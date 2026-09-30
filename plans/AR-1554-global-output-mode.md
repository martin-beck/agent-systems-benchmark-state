# AR-1554 plan: global output mode

1. Inventory every public ASB command and current output/error path.
2. Introduce one global output policy and renderer; make human output the
   default and expose the canonical JSON envelope via `--json`.
3. Keep credentials, private paths, prompts, and responses out of both modes.
4. Add representative command tests, help/ordering tests, and regression tests
   for existing JSON consumers.
5. Update CLI documentation and run focused and workspace gates.
