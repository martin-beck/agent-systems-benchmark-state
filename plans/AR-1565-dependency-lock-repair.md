# AR-1565 — ASB yanked dependency lock repair

## Scope

Repair the minimal workspace and fuzz lockfile closure causing `cargo deny
--locked check` and `cargo audit --deny warnings` to fail on protected
branches.

## Acceptance

- No yanked crate remains in the locked graph.
- Both the workspace and `fuzz/Cargo.lock` graphs are covered.
- `cargo deny --locked check` and `cargo audit --deny warnings` pass.
- Full required ASB checks pass on the exact PR commit.
- No policy gate is weakened and no unrelated dependency drift is introduced.
- Independent review confirms the lockfile diff and fresh downstream build.

## Boundaries

This is infrastructure/dependency repair only. It does not implement channel
materialization, provider authentication, or asb-tui source changes.
